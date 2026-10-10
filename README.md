# DevOps Class


A small Flask app that divides two numbers and writes a timestamped log after each step.

## Setup

```bash
./setup.sh
```

This creates a `.venv` virtual environment and installs the packages in `requirements.txt`.

## Run



```bash
.venv/bin/python app.py
```

The app listens on `http://127.0.0.1:5050`.

## Divide two numbers

Pass `a` and `b` as query parameters. The response is `a / b`.

```bash
curl "http://127.0.0.1:5050/?a=10&b=2"
```

```text
5.0
```

Each request logs the inputs and the result:

```text
INFO app: 2026-10-10 14:35:15 a = 10.0
INFO app: 2026-10-10 14:35:15 b = 2.0
INFO app: 2026-10-10 14:35:15 result = 5.0
```

If `b` is missing or `0`, the request fails with a division-by-zero error.

## Tests

```bash
.venv/bin/python -m unittest discover -s tests -p "test_*.py"
```

GitHub Actions runs the same command on every push and pull request. The workflow is `.github/workflows/tests.yml`.

## Project layout

| File | Purpose |
| --- | --- |
| `app.py` | Flask app and `/` route |
| `src/logger.py` | Logger that prefixes every message with a timestamp |
| `src/utility.py` | Division logic |
| `tests/test_utility.py` | Unit tests for division |
| `.github/workflows/tests.yml` | GitHub Actions workflow that runs the unit tests |
| `requirements.txt` | Python dependencies |
| `setup.sh` | Creates the virtual environment and installs dependencies |
