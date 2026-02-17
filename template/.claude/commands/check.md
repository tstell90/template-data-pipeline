Run ALL quality gates — the same checks CI runs. This is the "is it safe to merge?" command.

Steps:
1. Run `uv run ruff check .` (do NOT auto-fix — just report)
2. Run `uv run ruff format --check .`
3. Run `uv run mypy src/`
4. Run `uv run pytest tests/ -v --tb=short`
5. Provide a clear pass/fail summary for each step
