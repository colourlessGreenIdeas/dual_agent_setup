# project-init.md

## Initial Idea
[Paste your app idea here - can be rough, conversational]

## Clarifying Questions
[Orchestrator/Planner will fill this out if idea is unclear]
- What's the primary use case?
- What's the input/output?
- Any specific tech stack requirements?
- Performance/scale requirements?

## Extracted Requirements
[Broken down from idea]

### Core Functionality
- [Feature 1]
- [Feature 2]

### Technical Requirements
- Language/Framework: [e.g., Python, Node.js]
- Storage: [e.g., SQLite, JSON files, PostgreSQL]
- External APIs: [if any]

### Non-Requirements (Out of Scope)
- [Things explicitly NOT building]

## Generated Goals
[This becomes the seed for goals.md]

---

## INSTRUCTIONS FOR PLANNER

When you receive a new app idea:

1. **Read the idea** - Understand what the user wants
2. **Ask clarifying questions** if needed (fill "Clarifying Questions" section)
3. **Extract requirements** - Break down into concrete features
4. **Define non-requirements** - What we're NOT building (prevent scope creep)
5. **Generate goals** - Create 5-10 small, testable goals
6. **Populate goals.md** - Transfer goals in priority order
7. **Archive this file** - Move to `archive/project-init-[date].md`

### Goal Generation Guidelines

**Good goals are:**
- ✅ Small (completable in 1-3 dev-critic cycles)
- ✅ Testable (clear success criteria)
- ✅ Ordered (each builds on previous)
- ✅ Focused (one thing at a time)

**Example breakdown:**
Idea: "Build a CLI tool that tracks my daily habits"

Goals:

- Create CLI that accepts habit name and logs it with timestamp to JSON file
- Add command to view today's logged habits
- Add command to view habits for specific date
- Add streak calculation (consecutive days)
- Add weekly summary report
- Add data validation (prevent duplicate entries same day)

  
**Bad goals (too big):**  
- ❌ "Build the entire habit tracker"  
- ❌ "Implement all CRUD operations"  
- ❌ "Add reporting features"