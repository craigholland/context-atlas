"""Configure the repository to use the tracked `.githooks` directory."""

import subprocess
from pathlib import Path


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        ["git", "config", "core.hooksPath", ".githooks"],
        cwd=repo_root,
        text=True,
    )
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
