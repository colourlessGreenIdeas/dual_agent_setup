
### 3. Run the Orchestrator

```bash
chmod +x smart-orchestrator.py
./smart-orchestrator.py --cycles 20
```

### 4. Work in Cursor

The orchestrator will prompt you to:

**INITIALIZATION (first time):**
1. Open Cursor Composer (Cmd+I / Ctrl+I)
2. Say: "Read project-init.md and generate goals"
3. Cursor will populate goals.md
4. Press Enter in terminal
5. Cursor switches to CRITIC mode to review goals
6. Say: "Review the generated goals"
7. Press Enter when approved

**DEVELOPMENT CYCLES:**
1. **DEV mode**: Implement active goal with TDD
2. Press Enter when done
3. **CRITIC mode**: Review the implementation (can switch autonomously)
4. Press Enter when reviewed
5. Repeat until goal approved

**AUTONOMOUS MODE SWITCHING:**
- The AI operates completely autonomously, switching between DEV and CRITIC modes without user prompts
- When DEV completes work (Status: READY_FOR_REVIEW), it automatically switches to CRITIC mode
- When CRITIC approves work (Status: APPROVED), it automatically switches to DEV mode for next goal
- When CRITIC finds issues (Status: NEEDS_WORK), it automatically switches to DEV mode to address feedback
- This eliminates ALL need for manual mode switching

**CONTINUOUS AUTONOMOUS OPERATION:**
- The AI continues working through goals without ANY human intervention
- After completing a goal, immediately starts the next goal in the sequence
- Only stops if truly blocked (Status: BLOCKED) or if all goals are completed
- NEVER waits for "continue" instructions from the human
- Updates handoff.md automatically when switching modes
- Operates as a fully autonomous development system

## How It Works

```
┌─────────────────────────────────────────────────┐
│ 1. DEV MODE (Autonomous)                       │
│    - AI reads .cursorrules (DEV section)       │
│    - AI writes tests first (TDD)               │
│    - AI implements minimally                   │
│    - AI updates handoff.md → READY_FOR_REVIEW  │
│    - AI automatically switches to CRITIC mode  │
└─────────────────────────────────────────────────┘
                    ↓ (AUTOMATIC)
┌─────────────────────────────────────────────────┐
│ 2. CRITIC MODE (Autonomous)                    │
│    - AI reads .cursorrules (CRITIC section)    │
│    - AI reviews tests, code, goal alignment    │
│    - AI checks for over-engineering            │
│    - AI updates handoff.md → APPROVED/NEEDS_WORK│
│    - AI automatically switches based on status │
└─────────────────────────────────────────────────┘
                    ↓ (AUTOMATIC)
        APPROVED? → Switch to DEV mode for next goal
        NEEDS_WORK? → Switch to DEV mode to address feedback
        BLOCKED? → Wait for human intervention
```

## Key Files

- **`.cursorrules`**: Instructions for both DEV and CRITIC modes
- **`goals.md`**: Project vision and goal tracking
- **`handoff.md`**: Communication between modes
- **`scratchpad.md`**: Working memory (keep short!)
- **`critic-notes.md`**: Detailed review feedback
- **`project-init.md`**: Your initial app idea (archived after init)

## Working in Cursor

### DEV Mode

Open Composer and say things like:
- "Implement the active goal from goals.md"
- "Write tests for user login functionality"
- "Address the critic feedback from handoff.md"

Cursor will:
- Read goals.md for what to build
- Read handoff.md for feedback
- Follow TDD (tests first)
- Avoid over-engineering
- Update handoff.md when done

### CRITIC Mode

Open Composer and say things like:
- "Review the dev's implementation"
- "Check for over-engineering and scope creep"
- "Verify tests exist and pass"

Cursor will:
- Review code and tests
- Check goal alignment
- Look for over-engineering
- Update critic-notes.md
- Update handoff.md with feedback

## Example Session

```bash
# 1. Create idea
cat > project-init.md << 'EOF'
## Initial Idea
Build a password generator CLI tool.
- Generate random passwords
- Configurable length
- Options for numbers, symbols, etc.
Tech: Python
EOF

# 2. Run orchestrator
./smart-orchestrator.py --cycles 15

# 3. AI (INIT mode - Autonomous):
#    → Reads project-init.md and generates 6-8 small goals
#    → Updates handoff.md: Status READY_FOR_REVIEW
#    → Automatically switches to CRITIC mode

# 4. AI (CRITIC mode - Autonomous):
#    → Reviews generated goals
#    → Updates handoff.md: Status APPROVED
#    → Automatically switches to DEV mode

# 5. AI (DEV mode - Cycle 1 - Autonomous):
#    → Writes tests, implements basic password generation
#    → Updates handoff.md: Status READY_FOR_REVIEW
#    → Automatically switches to CRITIC mode

# 6. AI (CRITIC mode - Cycle 1 - Autonomous):
#    → Checks tests, code quality
#    → Updates handoff.md: Status APPROVED
#    → Automatically switches to DEV mode for next goal

# 7. AI continues autonomously through Goals #2-6...

# 8. Done! Working password generator with tests
#    → AI stops when all goals completed
```

## Tips

### For Better Results

1. **Be specific in project-init.md**
   - List concrete features
   - Mention tech stack
   - Note what you DON'T want

2. **Keep goals small**
   - Each goal should be completable in 1-3 cycles
   - If stuck, break goal into smaller pieces

3. **Trust the process**
   - Write tests first (even if it feels slow)
   - Let critic be strict about over-engineering
   - Don't skip cycles

4. **Use Cursor's features**
   - Composer for multi-file changes
   - Inline edit for small fixes
   - Terminal for running tests
   - File tree to navigate between goals.md, handoff.md, etc.

### Common Issues

**"Cursor isn't following the rules"**
- Make sure `.cursorrules` is in project root
- Explicitly say "I'm in DEV mode" or "I'm in CRITIC mode"
- Reference the files: "Read handoff.md and work on the active goal"

**"Context is growing too large"**
- Archive scratchpad.md when >200 lines:
  ```bash
  mkdir -p archive
  mv scratchpad.md archive/scratchpad-$(date +%Y-%m-%d).md
  # Orchestrator will create new one
  ```

**"Goals are too big"**
- In Cursor, say: "Break Goal #X into smaller sub-goals"
- Update goals.md with smaller, testable goals

**"Stuck in a cycle"**
- Check handoff.md for status
- Make sure you're updating Status: READY_FOR_REVIEW or Status: APPROVED
- If truly stuck, set Status: BLOCKED and describe the issue

## Advanced Usage

### Manual Mode (No Orchestrator)

You can work without the orchestrator:

1. Manually update `handoff.md` "Current Turn: DEV" or "Current Turn: CRITIC"
2. Open Cursor Composer
3. Say: "I'm in DEV mode, implement active goal" or "I'm in CRITIC mode, review changes"
4. Cursor reads `.cursorrules` and follows the appropriate mode

### Multiple Goals Per Session

```bash
# Run with high cycle count
./smart-orchestrator.py --cycles 50

# When a goal is approved, Cursor will prompt you to move next goal to active
# Press Enter to continue with next goal
```

### Resuming After Break

```bash
# Just run orchestrator again
./smart-orchestrator.py --cycles 10

# It will pick up from current state in handoff.md
```

## Core Principles

### 1. Test-Driven Development (TDD)
```
RED → GREEN → REFACTOR
1. Write failing test
2. Write minimal code to pass
3. Refactor if needed
```

### 2. Resist Over-Engineering
- No abstractions until 3+ use cases
- No "might need later" code
- Simplest solution wins
- Functions over classes when possible

### 3. Stay Focused
- One goal at a time
- No scope creep
- New ideas go to backlog

## What Gets Built

This system is ideal for:
- ✅ CLI tools
- ✅ APIs and backends
- ✅ Data processing scripts
- ✅ Libraries and packages
- ✅ Automation tools
- ✅ Bots and scrapers

Less ideal for:
- ❌ Complex UIs (no visual feedback loop)
- ❌ Real-time systems (hard to test)
- ❌ Projects requiring external services (unless mocked)

## License

MIT

---

## Complete File List for Cursor

Here's what you need:

1. ✅ `.cursorrules` - Single instruction file (replaces instructions-dev.md and instructions-critic.md)
2. ✅ `goals.md` - Same as before
3. ✅ `scratchpad.md` - Same as before
4. ✅ `handoff.md` - Same as before
5. ✅ `critic-notes.md` - Same as before
6. ✅ `project-init.md` - Same as before
7. ✅ `smart-orchestrator.py` - Updated for Cursor (prompts you instead of running commands)
8. ✅ `README.md` - Included so documentation is updated continually

## Workflow Summary

```bash
# 1. Setup
mkdir my-app && cd my-app
# Copy all files

# 2. Create idea
cat > project-init.md << 'EOF'
## Initial Idea
[Your app idea here]
EOF

# 3. Run orchestrator
./smart-orchestrator.py --cycles 20

# 4. Work in Cursor when prompted
# - Open Composer (Cmd+I / Ctrl+I)
# - Follow the mode instructions
# - Press Enter in terminal when done

# 5. Repeat until all goals complete!
