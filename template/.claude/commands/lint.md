Run all linting and formatting checks. Fix any auto-fixable issues, then report what remains.

Steps:
1. Run `uv run ruff check . --fix` to auto-fix lint issues
2. Run `uv run ruff format .` to format all Python files
3. Run `uv run mypy src/` for type checking
4. Summarize: what was fixed automatically, what needs manual attention
