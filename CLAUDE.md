# template-data-pipeline — Claude Code Context

This is a **Copier template** repo. It is NOT an application — it generates new data engineering projects.

## Structure

- `copier.yml` — Template configuration and interactive questions
- `template/` — All templated files (Jinja2 `.jinja` suffix)
- `tests/` — Tests for the template itself

## How Copier Works

- Files in `template/` are copied to the target directory
- Files ending in `.jinja` have variables substituted (e.g. `{{ project_name }}`)
- Directories with `{{ variable }}` in the name are renamed
- Conditional blocks (`{% if use_dbt %}...{% endif %}`) include/exclude content

## Key Variables

- `project_name` — Human-readable name
- `project_slug` — Repo/dir name (lowercase, hyphens)
- `python_module_name` — Importable name (lowercase, underscores)
- `python_version` — 3.11 / 3.12 / 3.13
- `use_databricks`, `use_dbt`, `use_terraform` — Feature toggles
- `github_username` — For CI workflow references
- `platform_repo_ref` — Version tag for platform repo

## Testing Changes

```bash
# Generate a test project from local template
copier copy . /tmp/test-project --defaults

# Verify it works
cd /tmp/test-project
uv sync
uv run pytest
uv run ruff check .
```

## Conventions

- All `.jinja` files must be valid after variable substitution
- Conditional files should degrade gracefully (empty file if condition is false = OK)
- Keep the template minimal — don't add things users will immediately delete
