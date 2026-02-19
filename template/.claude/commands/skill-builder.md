# Skill Builder

Research best practices and create a new Claude Code skill (slash command) for a workflow.

## Usage
Invoke when user says: "build a skill for...", "create a skill that...", "turn this into a skill"

## Process

1. **Understand the workflow** — ask the user to describe the workflow they want to automate:
   - What triggers it? (a phrase, a situation, a file type)
   - What are the steps?
   - What tools/CLIs does it use?
   - What does success look like?

2. **Research current best practices** — use Context7 or web search to find:
   - Existing Claude Code skill patterns
   - Anthropic's documentation on custom slash commands
   - Similar workflows in the community

3. **Draft the skill** as a Markdown file in `.claude/commands/`:
   ```markdown
   # Skill Name

   One-line description.

   ## Usage
   Invoke when user says: "trigger phrase 1", "trigger phrase 2"

   ## Process
   Step-by-step instructions Claude should follow...

   ## Notes
   Edge cases, caveats, prerequisites...
   ```

4. **Show draft to user** and iterate

5. **Save the skill** to `.claude/commands/<skill-name>.md`

6. **Test the skill** — invoke it once to verify it works as expected

## Skill Design Principles
- Skills are invoked by **semantic understanding** of the user's intent
- Keep each skill focused on ONE workflow
- Include concrete CLI commands, not just concepts
- Add "Notes" for edge cases and prerequisites
- If it touches files by type (e.g., `.sql`, `.tf`), consider making it a **rule** in CLAUDE.md instead
- Skills should be idempotent where possible — safe to run multiple times

## Skill vs Rule vs Command
| Type | When to use | Where |
|------|-------------|-------|
| Skill (command) | User invokes with a phrase or `/slash` | `.claude/commands/` |
| Rule | Triggered automatically by file type or action | `CLAUDE.md` Rules section |
| Global rule | Always active regardless of project | `~/.claude/CLAUDE.md` |
