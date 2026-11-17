# ADR-003 Generate drafts with deterministic greedy scheduling

## Status

Accepted

## Context

FR-04 and FR-05 require a valid weekly draft, coverage first and fairness over available history. NFR-01 limits generation to 30 seconds end to end.

## Decision

Process slots with the fewest eligible candidates first, then by start time and slot ID. Reject candidates who fail a hard constraint. Choose the least increase in target-hour deviation, then fewer night shifts for night slots, fewer Prefer Not conflicts and employee ID.

## Alternatives considered

An exact solver can search more combinations but adds modeling and runtime work. Manual assignment lets the Manager refine a draft but does not provide automatic generation.

## Consequences

The same snapshot yields the same draft. Greedy selection can leave a shortage even when a different combination would fill it. Report shortages and fairness metrics so the Manager can adjust or regenerate. Stop the engine by 25 seconds and return a validated result within the 30-second budget, or preserve the saved draft and official schedule.

Source: PA3 Software Design report, Section 3.6.
