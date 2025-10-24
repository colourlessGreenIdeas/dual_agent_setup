# goals.md

## Project Vision
A countdown app that helps users track important dates and events by showing remaining days until specific dates. Users can manage multiple countdowns for different events (birthdays, vacations, project deadlines) and receive notifications when countdowns reach zero. This solves the problem of keeping track of upcoming important dates and staying aware of approaching deadlines.

## Active Goal (Current Sprint)
**Goal #1**: Create basic CLI that accepts countdown name and target date, saves to JSON file
- **Success criteria**: 
  - [ ] Command `countdown add "Birthday" "2024-12-25"` creates countdown entry
  - [ ] Data persists to `countdowns.json` file
  - [ ] Timestamp is recorded for when countdown was created
  - [ ] All tests pass
- **Tests required**: 
  - [ ] test_add_countdown_creates_entry
  - [ ] test_data_persists_to_file
  - [ ] test_entry_has_timestamp
  - [ ] test_invalid_date_format_handled
- **Status**: NOT_STARTED

## Up Next (Prioritized)
**Goal #2**: Add command to list all countdowns with days remaining
**Goal #3**: Add command to calculate and display days remaining for each countdown
**Goal #4**: Add command to remove/delete countdowns
**Goal #5**: Add command to update existing countdowns

## Backlog
- Goal #6: Add notification system for zero-day countdowns
- Goal #7: Add command to view countdowns by date range
- Goal #8: Add data validation and error handling improvements
- Goal #9: Add command to export countdowns to different formats
- Goal #10: Add command to set countdown categories/tags

## Completed ✓
_None yet_

---
## RULES FOR THIS FILE
- ONE active goal at a time
- Goals must be testable/measurable
- New ideas go to backlog, not active
- Both agents update this file
- Keep goals small and focused (completable in 1-3 cycles)