import json
import os
import subprocess
import tempfile
import threading
import time
import uuid

from .formats import check_student, student_id, text, validate_tests
from .processes import ProcessGuard, worker_command


class Jobs:
    def __init__(self, store):
        self.store = store
        self.lock = threading.RLock()
        self.jobs = {}

    def start(self, pack_id, exercise_id, code, student=None):
        text(code, "Code")
        if student is not None:
            student = student_id(student)
        pack = self.store.pack(pack_id)
        if student is not None or pack.get("assignment"):
            student = check_student(pack, student)
        exercise = self.store.exercise(pack_id, exercise_id)
        if not exercise:
            raise ValueError("Exercice introuvable.")
        validate_tests(exercise)
        with self.lock:
            if any(j["state"] == "running" for j in self.jobs.values()):
                raise ValueError("Une exécution est déjà en cours. Arrêtez-la avant de recommencer.")
            if student:
                self.store.save_draft(student, pack_id, exercise_id, code)
            # Only completed jobs are evicted.
            if len(self.jobs) >= 100:
                self.jobs.pop(next(iter(self.jobs)))
            key = uuid.uuid4().hex
            self.jobs[key] = {"id": key, "state": "running", "cancel": threading.Event()}
            threading.Thread(target=self._run, args=(key, pack_id, exercise, code, student), daemon=True).start()
            return {"id": key, "state": "running"}

    def _run(self, key, pack_id, exercise, code, student):
        job = self.jobs[key]
        started = time.monotonic()
        report = {"status": "error", "diagnostics": [], "tests": [], "output": "", "passed": 0,
                  "total": len(exercise["tests"]), "score": 0, "max_score": exercise["points"]}
        guard = process = None
        try:
            with tempfile.TemporaryDirectory(prefix="mrpython-run-") as directory:
                process = subprocess.Popen(worker_command(), stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE, cwd=directory,
                                           start_new_session=os.name != "nt",
                                           creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0)
                guard = ProcessGuard(process)
                payload = json.dumps({"source": code, "tests": exercise["tests"], "points": exercise["points"]}, ensure_ascii=False).encode()
                # communicate() drains pipes while supervising the deadline; worker
                # output is capped before it reaches the pipe.
                deadline = time.monotonic() + exercise["timeout"]
                first = True
                while True:
                    if job["cancel"].is_set() or time.monotonic() >= deadline:
                        report["status"] = "cancelled" if job["cancel"].is_set() else "timeout"
                        guard.stop()
                        process.communicate(timeout=3)
                        break
                    try:
                        stdout, stderr = process.communicate(payload if first else None, timeout=0.1)
                        if process.returncode != 0:
                            raise RuntimeError("Le processus s'est arrêté (ressources dépassées ou erreur interne).")
                        report = json.loads(stdout.decode("utf-8"))
                        break
                    except subprocess.TimeoutExpired:
                        first = False
                guard.stop()
                guard = None
        except Exception as exc:
            report["diagnostics"].append({"severity": "error", "message": "Exécution interrompue", "details": str(exc)})
        finally:
            if guard:
                guard.stop()
            if process:
                if process.poll() is None:
                    process.kill()
                process.communicate()
        report["duration_ms"] = round((time.monotonic() - started) * 1000)
        if student:
            try:
                self.store.record_attempt(student, pack_id, exercise, code, report)
            except Exception:
                report["diagnostics"].append({"severity": "warning", "message": "Résultat non sauvegardé", "details": "Exportez vos réponses et réessayez."})
        with self.lock:
            job["report"] = report
            job["state"] = "done"

    def get(self, key):
        with self.lock:
            if key not in self.jobs:
                raise ValueError("Exécution introuvable.")
            job = self.jobs[key]
            return {k: v for k, v in job.items() if k != "cancel"}

    def cancel(self, key):
        with self.lock:
            if key not in self.jobs:
                raise ValueError("Exécution introuvable.")
            self.jobs[key]["cancel"].set()
        return {"ok": True}

    def close(self):
        with self.lock:
            for job in self.jobs.values():
                job["cancel"].set()
        deadline = time.monotonic() + 4
        while time.monotonic() < deadline:
            with self.lock:
                if not any(j["state"] == "running" for j in self.jobs.values()):
                    break
            time.sleep(0.05)
