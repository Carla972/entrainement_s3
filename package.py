"""Supplied archive builder; CI decides when this script may run."""
import os
from pathlib import Path
import re
import subprocess
from zipfile import ZIP_DEFLATED, ZipFile


def main():
    revision = os.environ.get("GITHUB_SHA")
    if not revision:
        revision = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise ValueError("Expected a full Git commit SHA")
    maps = sorted(Path("levels").rglob("*.json"))
    if not maps:
        raise RuntimeError("No maps to package")
    files = [Path(name) for name in (
        "README.md", "map_check.py", "pyproject.toml", "uv.lock", "tests/test_maps.py"
    )] + maps
    Path("dist").mkdir(exist_ok=True)
    output = Path("dist") / f"map-kit-{revision}.zip"
    with ZipFile(output, "w", ZIP_DEFLATED) as bundle:
        for path in files:
            bundle.write(path, path.as_posix())
        bundle.writestr("REVISION.txt", revision + "\n")
    print(output)


if __name__ == "__main__":
    main()
