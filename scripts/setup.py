"""Build the local web interface after a fresh source checkout."""
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent


def main():
    if sys.version_info < (3, 11):
        raise SystemExit('Python 3.11 ou plus récent est requis.')
    node = shutil.which('node')
    npm = shutil.which('npm.cmd' if os.name == 'nt' else 'npm')
    if not node or not npm:
        raise SystemExit('Installez Node.js 22.12+ (ou 24+), puis relancez cette commande.')
    version = subprocess.check_output([node, '--version'], text=True).strip()
    parts = tuple(int(part) for part in version.lstrip('v').split('.')[:2])
    if parts < (22, 12):
        raise SystemExit(f'Node.js {version} est trop ancien ; version 22.12+ requise.')
    subprocess.run([npm, 'ci'], cwd=ROOT / 'frontend', check=True)
    subprocess.run([npm, 'run', 'build'], cwd=ROOT / 'frontend', check=True)
    print('Installation terminée. Lancez : python run.py --browser')


if __name__ == '__main__':
    main()
