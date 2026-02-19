# Create Pull Request

Create a well-structured pull request for the current branch.

## Usage
Invoke when user says: "create a PR", "open a pull request", "submit my changes"

## Process

1. **Verify quality gates pass first**:
```bash
uv run pytest && uv run ruff check . && uv run mypy src/
```
If anything fails, stop and fix before continuing.

2. **Gather PR context**:
```bash
git log main..HEAD --oneline   # commits in this branch
git diff main...HEAD --stat    # files changed
```

3. **Draft PR** with this structure:
```markdown
## Summary
- What changed and why (2-3 bullets)

## Changes
- `path/to/file.py` — description of change
- `tests/test_file.py` — tests added/updated

## Testing
- [ ] All tests pass (`uv run pytest`)
- [ ] Lint/format clean (`uv run ruff check .`)
- [ ] Type check passes (`uv run mypy src/`)

## Related Issues
Closes #N
```

4. **Show draft to user** — confirm before creating

5. **Create via gh**:
```bash
git push -u origin HEAD
gh pr create --title "..." --body "..." --base main
```

6. **Return the PR URL** to the user

## Notes
- One PR per issue — keep them focused
- Title: imperative mood, under 70 chars ("Add monthly production rollup model")
- Link to the issue it closes with "Closes #N" in the body
- Request review if the repo has a CODEOWNERS file
