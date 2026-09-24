"""Create a portable archive of the complete desktop distribution."""
import argparse
from pathlib import Path
import platform
import shutil
import sys

ROOT = Path(__file__).resolve().parent.parent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dist-dir', type=Path, default=ROOT / 'dist')
    distribution = parser.parse_args().dist_dir.resolve()
    folder = 'MrPythonRunner.app' if sys.platform == 'darwin' else 'MrPythonRunner'
    source = distribution / folder
    executable = source / ('Contents/MacOS/MrPythonRunner' if sys.platform == 'darwin'
                           else 'MrPythonRunner.exe' if sys.platform == 'win32' else 'MrPythonRunner')
    if not executable.is_file():
        raise SystemExit('Distribution absente. Lancez scripts/build_desktop.py avant de créer une archive.')
    system = {'win32': 'Windows', 'darwin': 'macOS'}.get(sys.platform, 'Linux')
    machine = platform.machine().lower()
    arch = {'amd64': 'x64', 'x86_64': 'x64', 'aarch64': 'arm64'}.get(machine, machine)
    archive = shutil.make_archive(str(distribution / f'MrPythonRunner-{system}-{arch}'),
                                  'zip' if sys.platform == 'win32' else 'gztar',
                                  root_dir=distribution, base_dir=folder)
    print('Archive créée :', archive)


if __name__ == '__main__':
    main()
