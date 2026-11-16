# ADR-001 Deploy one modular Express API

## Status

Accepted

## Context

One production team uses the same eligibility rules for scheduling and replacement coverage. PA2 requires protected endpoints and consistent roster writes.

## Decision

Deploy React and one modular Express Function on Vercel. Use Supabase Auth for identity and PostgreSQL for business data. Express verifies JWTs and enforces active account, role, team and object scope.

## Alternatives considered

Separate services offer independent deployment but add coordination for shared writes. Direct browser access to business tables would add a second path for eligibility and authorization rules.

## Consequences

Scheduling and Coverage share the eligibility and publication logic. All modules share one deployment and its database capacity. Measure serverless startup and connection overhead with NFR-01.

Source: PA3 Software Design report, Section 3.6.
