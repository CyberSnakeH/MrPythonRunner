import json
import os
import sqlite3
import sys
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

from .formats import check_student, fingerprint, identifier, student_id, text, validate_pack


def data_directory():
    if sys.platform == "win32":
        root = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData/Local"))
    elif sys.platform == "darwin":
        root = Path.home() / "Library/Application Support"
    else:
        root = Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local/share"))
    return root / "MrPythonRunner"


def now():
    return datetime.now(timezone.utc).isoformat()


class Store:
    def __init__(self, directory):
        directory = Path(directory)
        directory.mkdir(parents=True, exist_ok=True)
        self.path = directory / "runner.sqlite3"
        with self.connect() as db:
            db.executescript("""
                CREATE TABLE IF NOT EXISTS packs (id TEXT PRIMARY KEY, payload TEXT NOT NULL, updated TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS drafts (
                    student TEXT NOT NULL, pack_id TEXT NOT NULL, exercise_id TEXT NOT NULL,
                    code TEXT NOT NULL, report TEXT, exercise_hash TEXT, updated TEXT NOT NULL,
                    PRIMARY KEY(student, pack_id, exercise_id));
                CREATE TABLE IF NOT EXISTS attempts (
                    id INTEGER PRIMARY KEY, student TEXT NOT NULL, pack_id TEXT NOT NULL,
                    exercise_id TEXT NOT NULL, code TEXT NOT NULL, report TEXT NOT NULL,
                    exercise_hash TEXT NOT NULL, created TEXT NOT NULL);
            """)

    @contextmanager
    def connect(self):
        db = sqlite3.connect(self.path, timeout=10)
        db.row_factory = sqlite3.Row
        try:
            with db:
                yield db
        finally:
            db.close()

    def packs(self):
        with self.connect() as db:
            return [json.loads(row[0]) for row in db.execute("SELECT payload FROM packs ORDER BY updated DESC")]

    def pack(self, pack_id):
        identifier(pack_id)
        with self.connect() as db:
            row = db.execute("SELECT payload FROM packs WHERE id=?", (pack_id,)).fetchone()
        if row is None:
            raise ValueError("Série introuvable.")
        return json.loads(row[0])

    def save_pack(self, pack):
        validate_pack(pack)
        with self.connect() as db:
            db.execute("INSERT INTO packs VALUES (?,?,?) ON CONFLICT(id) DO UPDATE SET payload=excluded.payload, updated=excluded.updated",
                       (pack["id"], json.dumps(pack, ensure_ascii=False, allow_nan=False), now()))
        return pack

    def exercise(self, pack_id, exercise_id):
        return next((ex for ex in self.pack(pack_id)["exercises"] if ex["id"] == exercise_id), None)

    def save_draft(self, student, pack_id, exercise_id, code):
        student = check_student(self.pack(pack_id), student)
        text(code, "Code")
        if self.exercise(pack_id, exercise_id) is None:
            raise ValueError("Exercice introuvable.")
        with self.connect() as db:
            db.execute("""INSERT INTO drafts VALUES (?,?,?,?,NULL,NULL,?)
                ON CONFLICT(student,pack_id,exercise_id) DO UPDATE SET
                report=CASE WHEN drafts.code=excluded.code THEN drafts.report ELSE NULL END,
                code=excluded.code, updated=excluded.updated""",
                       (student, pack_id, exercise_id, code, now()))

    def record_attempt(self, student, pack_id, exercise, code, report):
        with self.connect() as db:
            values = (json.dumps(report, ensure_ascii=False), fingerprint(exercise))
            db.execute("INSERT INTO attempts(student,pack_id,exercise_id,code,report,exercise_hash,created) VALUES (?,?,?,?,?,?,?)",
                       (student, pack_id, exercise["id"], code, *values, now()))
            # Do not attach an old result to code edited while its job ran.
            db.execute("UPDATE drafts SET report=?, exercise_hash=? WHERE student=? AND pack_id=? AND exercise_id=? AND code=?",
                       (*values, student, pack_id, exercise["id"], code))

    def drafts(self, student, pack_id):
        pack = self.pack(pack_id)
        student = check_student(pack, student)
        with self.connect() as db:
            rows = db.execute("SELECT * FROM drafts WHERE student=? AND pack_id=?", (student, pack_id)).fetchall()
        hashes = {ex["id"]: fingerprint(ex) for ex in pack["exercises"]}
        result = {}
        for row in rows:
            if row["exercise_id"] in hashes:
                result[row["exercise_id"]] = {
                    "code": row["code"], "updated": row["updated"],
                    "report": json.loads(row["report"]) if row["report"] and row["exercise_hash"] == hashes[row["exercise_id"]] else None}
        return result

    def work(self, student, pack_id):
        student = student_id(student)
        pack = self.pack(pack_id)
        drafts = self.drafts(student, pack_id)
        result = {"format": "mrpython-work", "version": pack["version"], "student": student,
                "pack_id": pack_id, "pack_title": pack["title"], "pack_fingerprint": fingerprint(pack),
                "exported": now(), "answers": [
                    {"exercise_id": ex["id"], "code": drafts.get(ex["id"], {}).get("code", ex["starter"]),
                     "local_report": drafts.get(ex["id"], {}).get("report")}
                    for ex in pack["exercises"]]}
        if pack.get("assignment"):
            result["source_pack_id"] = pack["assignment"]["source_pack_id"]
        return result
