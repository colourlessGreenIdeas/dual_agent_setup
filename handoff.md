# handoff.md

## Current Turn: CRITIC

## Status: READY_FOR_REVIEW

**Valid statuses**: WORKING | READY_FOR_REVIEW | NEEDS_WORK | APPROVED | BLOCKED

---

## Dev → Critic Handoff

### Latest Handoff
**Timestamp**: _Not yet_
**Goal Addressed**: [Goal #X from goals.md]
**Cycle**: 0

**Changes Made**:
- _None yet_

**Tests Added/Modified**:
- _None yet_

**Files Changed**:
- _None yet_

**Request to Critic**: 
_What specifically should the critic focus on?_

---

## Critic → Dev Handoff

### Latest Feedback
**Timestamp**: _Not yet_
**Review Status**: PENDING

**Critical Issues** 🔴 _(Must fix before approval)_:
- _None yet_

**Improvements Suggested** 🟡 _(Should consider)_:
- _None yet_

**Approved Items** ✅:
- _None yet_

**Action Items for Dev**:
- [ ] _Waiting for first review_

**Next Steps**:
_Waiting for dev to complete first task_

---

## COMMUNICATION PROTOCOL

### Dev Signals
When ready for review, Dev must:
1. Update "Status:" to `READY_FOR_REVIEW`
2. Fill out "Dev → Critic Handoff" section completely
3. Ensure all tests are passing
4. Stop and wait for critic

### Critic Signals
After review, Critic must:
1. Update "Status:" to `APPROVED`, `NEEDS_WORK`, or `BLOCKED`
2. Fill out "Critic → Dev Handoff" section completely
3. Provide specific, actionable feedback
4. If APPROVED: Update goals.md to mark goal complete

### Blocked Status
If either agent is blocked:
1. Update "Status:" to `BLOCKED`
2. Document the blocker clearly
3. Suggest what information/help is needed
4. Wait for human intervention