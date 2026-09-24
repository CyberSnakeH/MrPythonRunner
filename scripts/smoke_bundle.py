"""Exercise the real worker and HTTP application from sources or a desktop build."""
import json
import argparse
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import urllib.request

ROOT = Path(__file__).resolve().parent.parent
parser = argparse.ArgumentParser()
parser.add_argument('--dist-dir', type=Path, default=ROOT / 'dist')
parser.add_argument('--source', action='store_true', help='Vérifier le lancement depuis les sources')
args = parser.parse_args()
distribution = args.dist_dir.resolve()
folder = distribution / 'MrPythonRunner'
worker = folder / ('MrPythonWorker.exe' if os.name == 'nt' else 'MrPythonWorker')
if sys.platform == 'darwin':
    worker = distribution / 'MrPythonRunner.app/Contents/MacOS/MrPythonWorker'
command = [sys.executable, str(ROOT / 'run.py')] if args.source else [str(worker)]
payload = {'source': 'def carre(n: int) -> int:\n    """Carré de n."""\n    return n*n\n',
           'tests': [{'id': 'test', 'label': 'Carré négatif', 'code': 'assert carre(-3) == 9'}], 'points': 4}
with tempfile.TemporaryDirectory() as directory:
    result = subprocess.run([*command, '--worker'], input=json.dumps(payload).encode(),
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=directory, timeout=30,
                            creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
if result.returncode:
    raise SystemExit(result.stderr.decode('utf-8', errors='replace'))
report = json.loads(result.stdout)
if report['status'] != 'passed' or report['score'] != 4:
    raise SystemExit(str(report))
print('Worker : test réussi, score 4/4.')

# Exercise the frozen application's HTTP API, asset paths and supervised worker,
# rather than only invoking grade() directly. The console sibling shares the
# desktop's entry point and resources; --serve does not need a graphical session.
with tempfile.TemporaryDirectory() as directory:
    server = subprocess.Popen([*command, '--serve', '--data-dir', directory], cwd=directory,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
    try:
        import queue
        import threading
        lines = queue.Queue()
        threading.Thread(target=lambda: lines.put(server.stdout.readline()), daemon=True).start()
        try:
            line = lines.get(timeout=20).decode('utf-8', errors='replace').strip()
        except queue.Empty:
            raise SystemExit('Le serveur embarqué ne démarre pas dans les 20 secondes.')
        if not line.startswith('MrPython Runner : http://127.0.0.1:'):
            raise SystemExit('Démarrage inattendu : ' + line)
        url = line.split(' : ', 1)[1]
        base, fragment = url.split('#', 1)
        token = fragment.split('=', 1)[1]

        def call(path, data):
            request = urllib.request.Request(base + 'api/' + path, data=json.dumps(data).encode(),
                                             headers={'Content-Type': 'application/json', 'X-Runner-Token': token})
            with urllib.request.urlopen(request, timeout=5) as response:
                return json.load(response)

        with urllib.request.urlopen(base, timeout=5) as response:
            assert b'<title>MrPython Runner</title>' in response.read()
        state = call('state', {})
        assert state['packs'][0]['id'] == 'premiers-pas'
        exported = call('pack/export', {'pack_id': 'premiers-pas', 'student': 'bundle-smoke'})
        personal = call('pack/import', {'data': exported['data']})['pack']
        job = call('jobs/start', {'pack_id': personal['id'], 'exercise_id': 'carre',
                                  'code': payload['source'], 'student': 'bundle-smoke'})
        deadline = time.monotonic() + 15
        while time.monotonic() < deadline:
            status = call('jobs/get', {'id': job['id']})
            if status['state'] == 'done': break
            time.sleep(.1)
        else:
            raise SystemExit('Le worker supervisé ne termine pas.')
        if status['report']['status'] != 'passed':
            raise SystemExit(str(status['report']))
        print('Application : interface, API, sauvegarde et correction vérifiées.')
    finally:
        server.terminate()
        server.communicate(timeout=5)
