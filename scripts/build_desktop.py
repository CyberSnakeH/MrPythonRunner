"""Compile frontend + native distribution, including dependency licenses."""
import importlib.metadata
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent


def licenses():
    output = ROOT / 'build/licenses'
    output.mkdir(parents=True, exist_ok=True)
    # Preserve complete license files of installed JS dependencies, including
    # scoped packages and bundled font licenses.
    modules = ROOT / 'frontend/node_modules'
    packages = list(modules.glob('*/package.json')) + list(modules.glob('@*/*/package.json'))
    for manifest in packages:
        for path in manifest.parent.rglob('*'):
            if path.is_file() and (path.name.upper().startswith(('LICENSE', 'LICENCE', 'COPYING', 'NOTICE')) or path.name.upper() == 'OFL.TXT'):
                relative = path.relative_to(modules)
                target = output / 'npm' / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(path, target)
    for distribution in importlib.metadata.distributions():
        for path in distribution.files or []:
            if any(word in str(path).upper() for word in ('LICENSE', 'LICENCE', 'COPYING', 'NOTICE')):
                source = Path(distribution.locate_file(path))
                if source.is_file():
                    relative = Path(*[part for part in Path(path).parts if part not in ('..', '.')])
                    target = output / 'python' / distribution.metadata['Name'] / relative
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(source, target)
    python_license = Path(sys.base_prefix) / 'LICENSE.txt'
    if python_license.is_file():
        shutil.copy2(python_license, output / 'LICENSE.python-runtime.txt')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dist-dir', type=Path, default=ROOT / 'dist')
    distribution = parser.parse_args().dist_dir.resolve()
    npm = shutil.which('npm.cmd' if os.name == 'nt' else 'npm')
    if not npm:
        raise SystemExit('Node.js / npm est requis pour construire la distribution.')
    if not (ROOT / 'frontend/node_modules').exists():
        subprocess.run([npm, 'ci'], cwd=ROOT / 'frontend', check=True)
    subprocess.run([npm, 'run', 'build'], cwd=ROOT / 'frontend', check=True)
    subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s', 'tests'], cwd=ROOT, check=True)
    subprocess.run([sys.executable, str(ROOT / 'scripts/check_upstream.py')], cwd=ROOT, check=True)
    licenses()
    subprocess.run([sys.executable, '-m', 'PyInstaller', '--noconfirm', '--distpath', str(distribution), str(ROOT / 'MrPythonRunner.spec')], cwd=ROOT, check=True)
    subprocess.run([sys.executable, str(ROOT / 'scripts/smoke_bundle.py'), '--dist-dir', str(distribution)], cwd=ROOT, check=True)
    print('Distribution créée :', distribution)
