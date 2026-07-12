# Claude Code Instructions

## Effort Levels

Select effort based on task complexity — state which level you're using and why.

| Task type | Effort |
|---|---|
| Typos, simple renames, obvious one-liners | standard |
| New features, bug investigation, refactors | high |
| Architecture decisions, migrations, unknown failure modes, cross-cutting changes | xhigh |

Drop back to `high` after a heavy task is done. Do not run `xhigh` on routine work.

## Workflow Orchestration

### 1. Plan First

Enter plan mode for ANY non-trivial task (3+ steps or architectural decisions).

If something goes sideways: STOP and re-plan immediately — do not keep pushing.

Use plan mode for verification steps, not just building.

Write detailed specs upfront to reduce ambiguity.

### 2. Extended Thinking for Hard Problems

For architectural decisions, non-obvious bugs, or unfamiliar failure modes:
reason through at least 3 approaches before recommending one.
Show trade-offs explicitly. Do not jump to the first solution that comes to mind.

### 3. When to Suggest a Dynamic Workflow

If a task spans 5+ files, requires parallel investigation, or involves a migration:
suggest running as a Dynamic Workflow before starting.
Include the word "workflow" in the plan summary so Claude Code can trigger orchestration.

### 4. Subagent Strategy

Use subagents to keep the main context window clean.

Offload research, exploration, and parallel analysis to subagents.

One task per subagent for focused execution.

For complex problems: throw more compute at it via subagents rather than cramming into one context.

### 5. Self-Improvement Loop

After ANY correction from the user: update `tasks/lessons.md` with the pattern.

Write rules that prevent the same mistake from recurring.

Ruthlessly iterate on these lessons until mistake rate drops.

Review lessons at session start for relevant context.

### 6. Verification Before Done

Never mark a task complete without proving it works.

**Mandatory checklist before marking done:**
- [ ] Tests pass
- [ ] No regressions introduced
- [ ] Edge cases considered
- [ ] Diff reviewed against main

If any item fails: re-enter planning. Do NOT patch around it.

Ask yourself: "Would a staff engineer approve this?"

### 7. Demand Elegance (Balanced)

For non-trivial changes: pause and ask "is there a more elegant way?"

If a fix feels hacky: "Knowing everything I know now, implement the elegant solution."

Skip this for simple, obvious fixes — do not over-engineer.

Challenge your own work before presenting it.

### 8. Autonomous Bug Fixing

When given a bug report: just fix it. Do not ask for hand-holding.

Point at logs, errors, failing tests — then resolve them.

Zero context switching required from the user.

Go fix failing CI tests without being told how.

## Task Management

1. **Plan First**: Write plan to `tasks/todo.md` with checkable items
2. **Verify Plan**: Check in before starting implementation
3. **Track Progress**: Mark items complete as you go
4. **Explain Changes**: High-level summary at each step
5. **Document Results**: Add review section to `tasks/todo.md`
6. **Capture Lessons**: Update `tasks/lessons.md` after corrections

## Core Principles

**Simplicity First**: Make every change as simple as possible. Impact minimal code.

**No Laziness**: Find root causes. No temporary fixes. Senior developer standards.

**Minimal Impact**: Changes should only touch what is necessary. Avoid introducing bugs.

**Comment on Code**: Write clear and understandable comments for developers to follow.

**Think Before Proposing**: For architectural decisions or non-obvious bugs, reason through trade-offs before presenting a solution. Show your reasoning when it matters.

# Claude commands
- /ultraplan
- /ultracode
- /plan
- /implement
- /review
