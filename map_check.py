"""Supplied structural checks for this small JSON-map exercise."""
import json
from pathlib import Path


def validate(path: Path) -> dict:
    """Load one map; identify the file and rule when a check fails."""
    data = json.loads(path.read_text(encoding="utf-8"))
    grid = data["grid"]
    assert grid and all(isinstance(row, str) and row for row in grid), f"{path}: empty grid or row"
    width = len(grid[0])
    assert all(len(row) == width for row in grid), f"{path}: rows must have the same width"
    assert all(set(row) <= {"#", "."} for row in grid), f"{path}: unknown tile symbol"
    for name in ("start", "exit"):
        x, y = data[name]["x"], data[name]["y"]
        assert type(x) is int and type(y) is int, f"{path}: {name} coordinates must be integers"
        assert 0 <= y < len(grid) and 0 <= x < width, f"{path}: {name} outside grid"
        assert grid[y][x] == ".", f"{path}: {name} must be on floor"
    return data


if __name__ == "__main__":
    import sys
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("levels/n0.json")
    data = validate(path)
    print(f"{path}: valid structure ({len(data['grid'][0])} x {len(data['grid'])})")
    print("\n".join(data["grid"]))
