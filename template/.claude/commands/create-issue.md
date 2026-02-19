# Create GitHub Issue

Create a well-structured GitHub issue for a feature, bug, or task.

## Usage
Invoke when user says: "create an issue", "file an issue", "log a bug", "document this as an issue"

## Process

1. **Gather context** — ask the user to describe the problem or feature in plain language (paste a conversation, describe a bug, or outline a feature request)
2. **Analyze codebase** — read relevant source files, dbt models, or schemas to reference actual code in the issue
3. **Draft the issue** with this structure:

```markdown
## Problem Statement
Clear description of the problem or opportunity.

## Proposed Solution
Step-by-step approach with actual code references from the codebase.

## Acceptance Criteria
- [ ] Specific, verifiable criterion 1
- [ ] Specific, verifiable criterion 2
- [ ] Tests added/updated to cover the change

## Example Output / Expected Behavior
Show what success looks like (sample data, query results, etc.)

## Why This Matters
Business or technical justification.

## Stretch Goals (optional)
Nice-to-have improvements beyond the core ask.
```

4. **Get user approval** — show the draft and ask "Does this look right?"
5. **Create via gh CLI**:
```bash
gh issue create --title "..." --body "..." --label "..." --assignee "@me"
```
6. **Link to project** if applicable: `gh issue edit <num> --add-project "..."`

## Notes
- Include actual code snippets and file references from the repo
- Be specific about data types, column names, table paths
- One issue = one focused change (not a mega-issue)
- After creation, confirm the issue URL to the user
