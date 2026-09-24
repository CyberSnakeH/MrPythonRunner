"""Run the included upstream MrPython regression programs without another checkout."""
import contextlib
import io
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from runner.vendor.mrpython.typechecking import typechecker
from runner.vendor.mrpython.typechecking.prog_ast import Program

files = sorted((ROOT / 'tests/fixtures/mrpython').glob('*.py'))
if not files:
    raise SystemExit('Les programmes de régression tests/fixtures/mrpython sont absents.')
failures = []
for path in files:
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            typechecker.preconditions.clear()
            program = Program()
            program.build_from_file(str(path))
            ctx = program.type_check()
        if 'OK' in path.name:
            ok = not ctx.type_errors
        else:
            header = path.read_text(encoding='utf-8').splitlines()[0]
            ok = header.startswith('##!FAIL:') and bool(ctx.type_errors) and ctx.type_errors[0].fail_string().splitlines()[0].strip() == header[8:].strip()
        if not ok:
            failures.append(path.name)
    except Exception as exc:
        failures.append(f'{path.name}: {exc}')
print(f'{len(files) - len(failures)}/{len(files)} tests MrPython réussis.')
if failures:
    raise SystemExit('\n'.join(failures))
