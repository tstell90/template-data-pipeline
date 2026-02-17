# template-data-pipeline

A [Copier](https://copier.readthedocs.io/) template for Python data engineering projects with Databricks, dbt, Terraform, and CI/CD pre-configured.

## Usage

### Create a new project

```bash
copier copy gh:tstell90/template-data-pipeline ./my-new-pipeline
```

You'll be prompted for project name, Python version, and which features to include (Databricks, dbt, Terraform).

### Update an existing project (when template improves)

```bash
cd my-existing-project
copier update
```

## What you get

- **Python project** with `src/` layout and `pyproject.toml`
- **uv** for dependency management (fast, with lock file)
- **ruff** for linting and formatting (replaces black + isort + flake8)
- **mypy** for type checking
- **pytest** for testing
- **pre-commit** hooks (ruff, mypy, file hygiene, secret detection)
- **GitHub Actions CI** via reusable workflows from [tstell90/platform](https://github.com/tstell90/platform)
- **VS Code devcontainer** for reproducible dev environments
- **CLAUDE.md** for Claude Code context

### Optional features

- **Databricks Asset Bundles** — deploy notebooks and jobs
- **dbt** — medallion architecture (bronze/silver/gold)
- **Terraform** — Azure infrastructure as code

## Prerequisites

Install with the bootstrap script:

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/tstell90/platform/main/scripts/bootstrap.sh)
```

Or manually: [uv](https://docs.astral.sh/uv/), [copier](https://copier.readthedocs.io/), [pre-commit](https://pre-commit.com/), [gh CLI](https://cli.github.com/).
