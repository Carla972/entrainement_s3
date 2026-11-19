# S3 — checks before delivery

This is an isolated CI exercise using small JSON maps, not the full game.
Use Python 3.12 and uv. Open a terminal in this folder, then run:

```sh
uv sync --locked
uv run ruff check map_check.py tests
uv run python -m pytest -q
uv run python map_check.py levels/n0.json
```

The initial map passes its structural test. This does not prove that a player
can reach the exit. The S3 practical explains the workflow exercise.

## Supplied and editable parts

The checker, tests and archive builder are supplied. Complete the test command
in `.github/workflows/checks.yml` if it contains a TODO. Add a map to demonstrate
a failing check and its correction. Then add the Ruff step before pytest, as
explained in the practical. Ruff and its three-rule configuration are supplied.
Keep all existing checks.

## From an Actions artifact

Download the artifact of a successful main push and extract it. GitHub wraps the
`map-kit-<SHA>.zip` in an artifact ZIP; extract the inner archive too. Open a
terminal next to `pyproject.toml`, run the commands above, and read
`REVISION.txt`. Its SHA must match that successful workflow run.
The archive contains maps, checker, tests and locked dependencies; no Git clone,
virtual environment, credentials or model weights. Installing dependencies needs
network access unless they are already cached.

## Course source only

The complete workflow lives in the course sources. The download builder creates
an exercise starter by replacing its test command with an explicit TODO failure and removing the
Ruff step, which students add later.
Do not copy this practical over your group's game repository.
