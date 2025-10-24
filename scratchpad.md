# scratchpad.md

## Current Session
**Date**: [Auto-updated]
**Active Goal**: [Reference from goals.md - Goal #X]
**Cycle**: 0

## Recent Changes
_Last 5-10 changes only - archive older ones to archive/ folder_

### [Timestamp] - Cycle X
**Agent**: DEV | CRITIC
**Action**: [Brief description]
**Files changed**: [List]
**Tests**: [Status]

## Active Considerations
- [ ] Tests written BEFORE implementation
- [ ] All tests passing
- [ ] Code reviewed by critic
- [ ] Documentation updated
- [ ] No scope creep - staying focused on active goal

## Parking Lot
_Items to revisit later - move to goals.md backlog when appropriate_

---

## RULES FOR THIS FILE

### 1. Keep it SHORT
- Archive to `archive/scratchpad-YYYY-MM-DD.md` when >200 lines
- Only keep last 5-10 changes visible
- Reference goals.md instead of duplicating goal descriptions

### 2. Test-First Mindset (TDD)
RED → GREEN → REFACTOR

1. Write failing test
2. Write minimal code to pass
3. Refactor only after passing

- **NO implementation without corresponding test**  
- Tests define behavior, code fulfills tests  
- If you can't write a test for it, you don't understand it yet  
  
### 3. Resist Feature Creep & Over-Engineering  
**STOP before adding:**  
- ❌ "This might be useful later"  
- ❌ "Let me add this extra feature"  
- ❌ Abstractions for single use cases  
- ❌ Premature optimization  
- ❌ Frameworks/libraries not strictly needed  
  
**ASK instead:**  
- ✅ "Does this serve the current goal?"  
- ✅ "Is there a test for this?"  
- ✅ "What's the simplest way to make the test pass?"  
- ✅ "Can I do this with less code?"  
  
### 4. Code Discipline  
- Write the simplest code that passes tests  
- No abstractions until you have 3+ similar cases  
- Prefer duplication over wrong abstraction  
- Keep functions small (< 20 lines ideal)  
- One level of indentation per function when possible  
- No "clever" code - prefer obvious and boring  
  
### 5. Critic Approval Required  
- Mark changes as `[PENDING REVIEW]` until critic approves  
- Address ALL critical feedback before proceeding  
- Document critic's suggestions even if not implemented  
  
### 6. Communication Protocol  
- Update this file after every significant change  
- Be specific: "Added user validation test" not "worked on auth"  
- Link to specific files and line numbers when relevant