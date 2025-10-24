# critic-notes.md

## Current Review Cycle
**Reviewing**: [Goal #X from goals.md]
**Dev Cycle**: 0
**Date**: [Date]

---

## Review Checklist

### Tests ✓
- [ ] Tests exist for new functionality
- [ ] Tests are meaningful (not just checking implementation)
- [ ] Tests follow TDD pattern (test first, then code)
- [ ] All tests passing
- [ ] Edge cases covered

### Goal Alignment ✓
- [ ] Changes address active goal only
- [ ] No scope creep or extra features
- [ ] Success criteria from goals.md met

### Code Quality ✓
- [ ] Simple, not clever
- [ ] No premature abstractions
- [ ] Functions are small and focused
- [ ] Naming is clear and descriptive
- [ ] No unnecessary dependencies

### Anti-Patterns ✗
- [ ] Over-engineering detected?
- [ ] Abstractions without 3+ use cases?
- [ ] "Might need later" code?
- [ ] Untested code paths?

---

## Issues Found

### Critical 🔴 _(Blocking approval)_
_None yet_

### Improvements 🟡 _(Non-blocking suggestions)_
_None yet_

### Praise ✅ _(Good work to acknowledge)_
_None yet_

---

## Changes Made by Critic

### [Timestamp] - Cycle X
**File**: _None yet_
**Reason**: _Critic hasn't needed to intervene yet_
**Change**: _N/A_

---

## Review History

### Cycle 1
**Status**: PENDING
**Summary**: _Awaiting first dev submission_

---

## CRITIC GUIDELINES

### When to BLOCK (Critical Issues)
- Tests missing or failing
- Code doesn't address active goal
- Obvious bugs or security issues
- Scope creep (features not in goal)
- Over-engineering without justification

### When to SUGGEST (Improvements)
- Code clarity/readability
- Better test coverage
- Simpler approaches
- Refactoring opportunities
- Documentation gaps

### When to INTERVENE (Make Changes Yourself)
**DO intervene for:**
- Critical bugs blocking all progress
- Missing tests that are obvious
- Simple refactors that clarify intent

**DON'T intervene for:**
- Implementing new features
- Overriding dev's valid approach
- Style preferences

**ALWAYS document interventions above**

### Feedback Style
Be specific and constructive:
- ❌ "This code is bad"
- ✅ "In `auth.py:45`, the validation logic could be extracted to a separate function for testability. Example: [snippet]"

### Remember
- You're a quality gate, not a blocker
- Praise good work, don't just criticize
- Focus on simplicity and goal alignment
- Trust the dev unless there's a clear issue