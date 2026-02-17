#!/usr/bin/env bash
set -euo pipefail

echo "==> Installing project dependencies..."
uv sync --all-extras --dev

echo "==> Installing pre-commit hooks..."
uv run pre-commit install

echo "==> Post-create setup complete."
