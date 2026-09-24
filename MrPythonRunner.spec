# Build on each target OS; PyInstaller does not cross-compile.
import sys
from pathlib import Path
from PyInstaller.utils.hooks import collect_submodules

root = Path(SPECPATH)
a = Analysis(
    [str(root / 'run.py')], pathex=[str(root)],
    binaries=[],
    datas=[
        (str(root / 'frontend/dist'), 'frontend/dist'),
        (str(root / 'examples'), 'examples'),
        (str(root / 'runner/vendor/mrpython/LICENSE.python'), 'licenses/mrpython'),
        (str(root / 'runner/vendor/mrpython/AUTHORS'), 'licenses/mrpython'),
        (str(root / 'runner/vendor/mrpython/NOTICE.md'), 'licenses/mrpython'),
        (str(root / 'README.md'), '.'),
        (str(root / 'LICENSE'), '.'),
        (str(root / 'docs'), 'docs'),
        (str(root / 'THIRD_PARTY_NOTICES.md'), 'licenses'),
        (str(root / 'build/licenses'), 'licenses/dependencies'),
    ],
    hiddenimports=collect_submodules('runner'),
    hookspath=[], hooksconfig={}, runtime_hooks=[],
    excludes=['tkinter', 'idlelib'], noarchive=False,
)
pyz = PYZ(a.pure)
desktop = EXE(pyz, a.scripts, [], exclude_binaries=True, name='MrPythonRunner',
              console=sys.platform not in ('win32', 'darwin'), debug=False, strip=False, upx=False)
# A console worker keeps binary stdin/stdout usable even when the desktop
# executable was built without a console on Windows/macOS.
worker = EXE(pyz, a.scripts, [], exclude_binaries=True, name='MrPythonWorker',
             console=True, debug=False, strip=False, upx=False)
folder = COLLECT(desktop, worker, a.binaries, a.datas, strip=False, upx=False, name='MrPythonRunner')
if sys.platform == 'darwin':
    app = BUNDLE(folder, name='MrPythonRunner.app', bundle_identifier='org.mrpython.runner')
