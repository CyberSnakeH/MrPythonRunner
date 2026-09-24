"""Entry point for source installs, frozen desktops, and isolated workers."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))


def worker():
    import json
    from runner.processes import limit_worker
    limit_worker()
    # Read the protocol before redirecting student stdout inside grade().
    payload = json.loads(sys.stdin.buffer.read(2_000_000).decode("utf-8"))
    from runner.engine import grade
    result = grade(payload["source"], payload["tests"], payload["points"])
    sys.stdout.buffer.write(json.dumps(result, ensure_ascii=False).encode("utf-8"))
    sys.stdout.buffer.flush()


if __name__ == "__main__":
    if "--worker" in sys.argv:
        worker()
    else:
        from runner.app import main
        main()
