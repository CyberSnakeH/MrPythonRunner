import argparse
import base64
import hmac
import json
import mimetypes
import os
import re
import secrets
import sys
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit

from .formats import assign_pack, check_student, export_pack, export_work, fingerprint, import_pack, import_work
from .jobs import Jobs
from .storage import Store, data_directory

ROOT = Path(__file__).resolve().parent.parent
MAX_REQUEST = 24 * 1024 * 1024


class Application:
    def __init__(self, directory, seed=True):
        self.store = Store(directory)
        self.jobs = Jobs(self.store)
        self.token = secrets.token_urlsafe(32)
        if seed and not self.store.packs():
            self.store.save_pack(json.loads((ROOT / "examples/premiers-pas.json").read_text(encoding="utf-8")))

    def call(self, path, data):
        if path == "/api/state":
            return {"packs": self.store.packs(), "platform": sys.platform, "version": "0.1.0"}
        if path == "/api/pack/save":
            if data["pack"].get("assignment") or any(p["id"] == data["pack"]["id"] and p.get("assignment") for p in self.store.packs()):
                raise ValueError("Ce fichier élève est en lecture seule. Modifiez le modèle professeur.")
            return {"pack": self.store.save_pack(data["pack"])}
        if path == "/api/student/open":
            student = check_student(self.store.pack(data["pack_id"]), data.get("student"))
            return {"student": student}
        if path == "/api/pack/import":
            pack = import_pack(base64.b64decode(data["data"], validate=True))
            # Imports never silently replace an author's existing local series.
            existing = next((p for p in self.store.packs() if p["id"] == pack["id"]), None)
            if existing and existing.get("assignment") and existing["assignment"] != pack.get("assignment"):
                raise ValueError("L’attribution de ce fichier élève ne peut pas être retirée ou remplacée.")
            if existing and fingerprint(existing) != fingerprint(pack) and not data.get("replace"):
                return {"conflict": True, "title": existing["title"]}
            return {"pack": self.store.save_pack(pack)}
        if path == "/api/pack/export":
            pack = assign_pack(self.store.pack(data["pack_id"]), data.get("student"))
            label = re.sub(r"[^a-zA-Z0-9_-]", "_", pack["assignment"]["student_id"])[:40]
            return {"filename": "exercices-" + label + "-" + pack["id"] + ".mrpack", "data": base64.b64encode(export_pack(pack)).decode()}
        if path == "/api/pack/backup":
            pack = self.store.pack(data["pack_id"])
            if pack.get("assignment"):
                raise ValueError("Ouvrez le modèle professeur pour le sauvegarder.")
            return {"filename": "modele-" + pack["id"] + ".mrpack", "data": base64.b64encode(export_pack(pack)).decode()}
        if path == "/api/draft/save":
            self.store.save_draft(data["student"], data["pack_id"], data["exercise_id"], data["code"])
            return {"ok": True}
        if path == "/api/drafts":
            return {"drafts": self.store.drafts(data["student"], data["pack_id"])}
        if path == "/api/work/export":
            work = self.store.work(data["student"], data["pack_id"])
            return {"filename": "reponses-" + data["pack_id"] + ".mrwork",
                    "data": base64.b64encode(export_work(work)).decode()}
        if path == "/api/work/import":
            work = import_work(base64.b64decode(data["data"], validate=True))
            if data.get("purpose") == "restore":
                pack = self.store.pack(work["pack_id"])
                student = check_student(pack, data.get("student"))
                if student != work["student"]:
                    raise ValueError("Ces réponses appartiennent à un autre identifiant élève.")
                expected = pack
            else:
                # Teacher retains the unassigned source; personalized files have
                # separate IDs so distributing to another pupil never replaces it.
                pack = self.store.pack(work.get("source_pack_id", work["pack_id"]))
                expected = assign_pack(pack, work["student"]) if work["version"] == 2 else pack
            return {"work": work, "pack_id": pack["id"], "matching": work["pack_fingerprint"] == fingerprint(expected)}
        if path == "/api/work/restore":
            work = import_work(base64.b64decode(data["data"], validate=True))
            pack = self.store.pack(work["pack_id"])
            student = check_student(pack, data.get("student"))
            if student != work["student"]:
                raise ValueError("Ces réponses appartiennent à un autre identifiant élève.")
            ids = {ex["id"] for ex in pack["exercises"]}
            if not all(answer["exercise_id"] in ids for answer in work["answers"]):
                raise ValueError("Ces réponses ne correspondent pas aux exercices de la série.")
            for answer in work["answers"]:
                self.store.save_draft(work["student"], work["pack_id"], answer["exercise_id"], answer["code"])
            return {"student": work["student"], "pack_id": pack["id"]}
        if path == "/api/jobs/start":
            return self.jobs.start(data["pack_id"], data["exercise_id"], data["code"], data.get("student"))
        if path == "/api/jobs/get":
            return self.jobs.get(data["id"])
        if path == "/api/jobs/cancel":
            return self.jobs.cancel(data["id"])
        raise ValueError("Action inconnue.")


def create_server(app, port=0):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def reply(self, status, body, content_type="application/json; charset=utf-8"):
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Referrer-Policy", "no-referrer")
            # Only the TikZ compiler worker requires WebAssembly compilation.
            # The document keeps its original script policy (no eval/inline JS).
            wasm = " 'wasm-unsafe-eval'" if urlsplit(self.path).path == "/vendor/tikzjax/run-tex.js" else ""
            self.send_header("Content-Security-Policy", f"default-src 'self'; script-src 'self'{wasm}; style-src 'self' 'unsafe-inline'; img-src 'self' data: blob:; font-src 'self'; worker-src 'self' blob:; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'; object-src 'none'")
            self.end_headers()
            self.wfile.write(body)

        def do_POST(self):
            expected_origin = f"http://127.0.0.1:{self.server.server_port}"
            if (self.headers.get("Host") != f"127.0.0.1:{self.server.server_port}"
                or self.headers.get("Origin", expected_origin) != expected_origin
                or not hmac.compare_digest(self.headers.get("X-Runner-Token", ""), app.token)):
                self.reply(403, b'{"error":"Session locale non autorisee."}')
                return
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if not 0 < length <= MAX_REQUEST:
                    raise ValueError("Requête trop volumineuse ou vide.")
                data = json.loads(self.rfile.read(length))
                if not isinstance(data, dict):
                    raise ValueError("Requête invalide.")
                result = app.call(urlsplit(self.path).path, data)
                self.reply(200, json.dumps(result, ensure_ascii=False, allow_nan=False).encode())
            except (ValueError, KeyError, TypeError, OSError) as exc:
                self.reply(400, json.dumps({"error": str(exc)}, ensure_ascii=False).encode())
            except Exception:
                self.reply(500, b'{"error":"Erreur interne. Vos fichiers existants sont conserves."}')

        def do_GET(self):
            if self.headers.get("Host") != f"127.0.0.1:{self.server.server_port}":
                self.reply(403, b"Forbidden", "text/plain")
                return
            path = unquote(urlsplit(self.path).path)
            if path == "/":
                path = "/index.html"
            root = (ROOT / "frontend/dist").resolve()
            target = (root / path.lstrip("/")).resolve()
            if not target.is_relative_to(root) or not target.is_file():
                self.reply(404, b"Fichier introuvable. Lancez npm run build dans frontend.", "text/plain; charset=utf-8")
                return
            mime = {".js": "text/javascript", ".css": "text/css", ".svg": "image/svg+xml"}.get(target.suffix)
            self.reply(200, target.read_bytes(), mime or mimetypes.guess_type(target.name)[0] or "application/octet-stream")

    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    server.daemon_threads = True
    return server


class DesktopApi:
    def save_file(self, filename, data):
        import webview
        if Path(filename).name != filename or Path(filename).suffix not in (".mrpack", ".mrwork"):
            raise ValueError("Nom de fichier invalide.")
        payload = base64.b64decode(data, validate=True)
        if len(payload) > 16 * 1024 * 1024:
            raise ValueError("Fichier trop volumineux.")
        result = webview.windows[0].create_file_dialog(webview.FileDialog.SAVE, save_filename=filename)
        if result:
            target = Path(result[0] if isinstance(result, (tuple, list)) else result)
            target.write_bytes(payload)
            return True
        return False


def main():
    parser = argparse.ArgumentParser(description="MrPython Runner — atelier hors ligne")
    parser.add_argument("--browser", action="store_true", help="Ouvrir dans le navigateur local")
    parser.add_argument("--serve", action="store_true", help="Serveur local sans ouvrir de fenêtre")
    parser.add_argument("--port", type=int, default=0)
    parser.add_argument("--data-dir", type=Path, default=data_directory())
    args = parser.parse_args()
    if not (ROOT / "frontend/dist/index.html").exists():
        parser.error("Interface absente. Dans frontend, lancez npm ci puis npm run build.")
    app = Application(args.data_dir)
    server = create_server(app, args.port)
    url = f"http://127.0.0.1:{server.server_port}/#token={app.token}"
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    if sys.stdout:
        print(f"MrPython Runner : {url}", flush=True)
        print(f"Données locales : {args.data_dir}", flush=True)
    try:
        if not args.browser and not args.serve:
            try:
                import webview
            except ImportError:
                if sys.stdout:
                    print("pywebview absent : ouverture dans le navigateur. Ctrl+C pour fermer.", flush=True)
            else:
                webview.create_window("MrPython Runner", url, js_api=DesktopApi(), width=1440, height=920, min_size=(820, 600))
                webview.start()
                return
        if not args.serve:
            webbrowser.open(url)
        while thread.is_alive():
            thread.join(0.5)
    except KeyboardInterrupt:
        pass
    finally:
        app.jobs.close()
        server.shutdown()
        server.server_close()
