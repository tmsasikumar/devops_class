#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

python3 -m venv .venv
.venv/bin/pip install -r requirements.txt


# run the tests
.venv/bin/python -m unittest discover -s tests -p "test_*.py"
