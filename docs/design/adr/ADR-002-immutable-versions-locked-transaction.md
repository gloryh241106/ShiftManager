# ADR-002 Publish immutable schedule versions in one locked transaction

## Status

Accepted

## Context

Each publish (UC-05) and each confirmed replacement (UC-09) must create a new official version while earlier versions stay readable (FR-08, AC-13). The same write also changes assignments, the offer, the coverage request and the acknowledgements. FR-18, NFR-05 and AC-37 require that repeated or concurrent submission creates no duplicates and that a failure leaves the assignment, the current version, the offer outcome and the coverage status unchanged.

## Decision

SchedulingService and CoverageService each open one PostgreSQL READ COMMITTED transaction, take SELECT ... FOR UPDATE on the team row and re-read state inside the lock before writing. That transaction writes the new published_schedule_versions row with version_number + 1, the assignments, the offer, the coverage request and the acknowledgements, then commits once or rolls back. A partial unique index allows one current version per team and week, and confirm_idempotency_key makes a repeated confirmation return the recorded result.

## Alternatives considered

Editing assignments in place in one mutable schedule would lose the earlier versions that FR-08 and AC-13 require. Optimistic version checks without a row lock find a conflict only when the write fails, after the Manager has confirmed, and every write path would need retry handling. SERIALIZABLE isolation with retries adds retry handling that the team row lock already makes unnecessary, because writes of one team run one at a time.

## Consequences

A reader always sees one complete current version, and earlier versions with their assignments remain readable. Publishes and confirmations of one team run one at a time. Version rows grow with every publish and every confirmed replacement, and the partial unique index is maintained on each of those writes.

Source: PA3 Software Design report, Section 3.6.
