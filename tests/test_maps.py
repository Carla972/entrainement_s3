"""Supplied: every distributed JSON map is checked, including subfolders."""
from pathlib import Path

import pytest

from map_check import validate

MAPS = sorted(Path("levels").rglob("*.json"))
if not MAPS:
    raise RuntimeError("No maps found in levels/: refusing an empty validation")


@pytest.mark.parametrize("path", MAPS, ids=lambda path: path.as_posix())
def test_map_structure(path):
    validate(path)
