"""Headless adapter. Call in a disposable worker, never in the UI process.

This is an educational runner, not a security sandbox for hostile Python.
"""
import ast
import contextlib
import copy
import io
import time
import traceback
import typing

from .vendor.mrpython.typechecking import typechecker
from .vendor.mrpython.typechecking.translate import set_translator_locale
from .vendor.mrpython.typechecking.type_ast import PREDEFINED_TYPE_VARIABLES

MAX_OUTPUT = 32_000


class LimitedOutput(io.StringIO):
    def __init__(self):
        super().__init__()
        self.truncated = False

    def write(self, value):
        remaining = MAX_OUTPUT - self.tell()
        super().write(value[:max(0, remaining)])
        self.truncated |= len(value) > remaining
        return len(value)

    def content(self):
        return self.getvalue() + ("\n[Sortie limitée à 32 000 caractères]" if self.truncated else "")


class DiagnosticReport:
    def __init__(self):
        self.diagnostics = []

    def add_convention_error(self, severity, err_type, line=None, offset=None, details=""):
        self.diagnostics.append({"severity": severity, "message": err_type,
                                 "line": line, "column": offset, "details": details})


class Preconditions(ast.NodeTransformer):
    def visit_FunctionDef(self, node):
        checks = []
        for expression in typechecker.preconditions.get(node.name, []):
            expression = copy.deepcopy(expression)
            for child in ast.walk(expression):
                if hasattr(child, "lineno"):
                    child.lineno = node.lineno
                    child.end_lineno = node.lineno
                    child.col_offset = 0
                    child.end_col_offset = 0
            check = ast.Assert(test=expression, msg=ast.Constant(
                f"Précondition non respectée : {node.name}"))
            ast.copy_location(check, node)
            checks.append(check)
        # Keep the docstring as the first statement.
        index = int(bool(node.body and isinstance(node.body[0], ast.Expr)
                         and isinstance(node.body[0].value, ast.Constant)
                         and isinstance(node.body[0].value.value, str)))
        node.body[index:index] = checks
        return node


def exception_details(exc):
    frames = traceback.extract_tb(exc.__traceback__)
    frame = next((f for f in reversed(frames) if f.filename in ("eleve.py", "test.py")), None)
    return {"severity": "error", "message": type(exc).__name__,
            "details": str(exc) or "Une assertion n'est pas vérifiée.",
            "line": getattr(exc, "lineno", None) or (frame.lineno if frame else None),
            "file": getattr(exc, "filename", None) or (frame.filename if frame else "eleve.py")}


def namespace():
    env = {"__name__": "__student__", "__file__": "eleve.py"}
    for name in ("Sequence", "List", "Set", "Iterable", "Tuple", "Dict", "Optional", "Callable"):
        env[name] = getattr(typing, name)
    for name in PREDEFINED_TYPE_VARIABLES:
        env[name] = typing.TypeVar(name)

    def no_input(*args):
        raise RuntimeError("input() n'est pas disponible. Utilisez les paramètres de la fonction.")
    env["input"] = no_input
    return env


def grade(source, tests, points=1):
    start = time.monotonic()
    output = LimitedOutput()
    report = {"status": "failed", "diagnostics": [], "tests": [], "output": "",
              "passed": 0, "total": len(tests), "score": 0, "max_score": points}
    with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
        try:
            tree = ast.parse(source, "eleve.py")
            set_translator_locale("fr")
            typechecker.preconditions.clear()
            ctx = typechecker.typecheck_from_ast(tree, "eleve.py", source)
            collector = DiagnosticReport()
            for error in ctx.type_errors:
                error.report(collector)
            report["diagnostics"] = collector.diagnostics
            if any(error.is_fatal() for error in ctx.type_errors):
                report["status"] = "type_error"
            else:
                program = compile(ast.fix_missing_locations(Preconditions().visit(tree)), "eleve.py", "exec")
                # Every teacher test gets fresh student globals. One failed test does
                # not prevent the remaining tests from running.
                for test in tests:
                    item = {"id": test["id"], "label": test["label"], "hidden": test.get("hidden", False)}
                    try:
                        env = namespace()
                        exec(program, env, env)
                        exec(compile(test["code"], "test.py", "exec"), env, env)
                        item["passed"] = True
                        report["passed"] += 1
                    except BaseException as exc:
                        item["passed"] = False
                        item["error"] = exception_details(exc)
                    report["tests"].append(item)
                if tests:
                    report["score"] = round(points * report["passed"] / len(tests), 2)
                    report["status"] = "passed" if report["passed"] == len(tests) else "failed"
                else:
                    env = namespace()
                    exec(program, env, env)
                    report["status"] = "no_tests"
        except BaseException as exc:
            report["diagnostics"].append(exception_details(exc))
            report["status"] = "syntax_error" if isinstance(exc, SyntaxError) else "error"
    report["output"] = output.content()
    report["duration_ms"] = round((time.monotonic() - start) * 1000)
    return report
