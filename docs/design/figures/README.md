# PA3 figures

Editable sources for the figures in the PA3 report (`T06-PA3`). Each diagram has a
`.drawio` source and a `.png` export with the same name. 

## Editing a diagram

1. Open the `.drawio` file in [diagrams.net](https://app.diagrams.net) (File > Open from > Device)
   or in VS Code with the *Draw.io Integration* extension.
2. Edit and save the `.drawio` file.
3. Export a PNG (File > Export as > PNG, zoom 200%, border 16) over the old `.png`.

## Diagrams

| Figure | Source | Content |
|---|---|---|
| 3.1 | `F3.1-c4-system-context.drawio` | C4 level 1, system context |
| 3.2 | `F3.2-c4-containers.drawio` | C4 level 2, containers |
| 3.3 | `F3.3-api-components.drawio` | Express API components |
| 3.4 | `F3.4-deployment.drawio` | Deployment: browser, Vercel, Supabase |
| 4.1 | `F4.1-domain-model.drawio` | Conceptual domain model |
| 4.2 (a) | `F4.2-class-diagram.drawio` | Design class diagram: service classes and TransactionContext |
| 4.2 (b) | `F4.2b-entity-classes.drawio` | Entity classes with relationship types and multiplicities |
| 4.3 (a, b) | `F4.3a/b-uc05-draft-sequence.drawio` | UC-05 sequence: draft generation, then adjustment and save |
| 4.4 (a, b) | `F4.4a/b-uc05-publish-sequence.drawio` | UC-05 sequence: publication |
| 4.5 (a, b) | `F4.5a/b-uc01-login-sequence.drawio` | UC-01 sequence: login |
| 4.6 (a, b) | `F4.6a/b-uc09-offer-sequence.drawio` | UC-09 sequence: candidates and offer |
| 4.7 | `F4.7-uc09-response-sequence.drawio` | UC-09 sequence: response and cancellation |
| 4.8 (a, b) | `F4.8a/b-uc09-confirm-sequence.drawio` | UC-09 sequence: confirmation |
| 4.9 | `F4.9-state-replacement-offer.drawio` | State diagram: replacement offer |
| 4.10 | `F4.10-state-coverage-request.drawio` | State diagram: coverage request |
| 4.11 | `F4.11-state-acknowledgement.drawio` | State diagram: schedule acknowledgement |
| 5.1 (a, b, c) | `F5.1a-erd-planning.drawio`, `F5.1b-erd-schedules.drawio`, `F5.1c-erd-coverage.drawio` | ERD in crow's foot notation, key columns only: (a) teams, users and planning inputs; (b) draft and official schedules; (c) absence and coverage |
| 6.1 | `F6.1-screen-flow.drawio` | Screen flow |

## Notes

- The report now uses these exports for Figures 4.1 to 4.8
- Sequence diagrams use class lifelines (`:SchedulingService`, `:CoverageService`, ...) and
  label service calls with the operations of the class diagram. Tall diagrams are split into
  parts (a) and (b) under one figure number.
- 4.1: AbsenceReport is linked to ShiftAssignment (`reported in`), as in the ERD
  (`absence_reports.origin_assignment_id`). Each association shows its multiplicity at
  each end and its name in the middle; crossings are drawn with a small arc.
- 5.1: built from the columns listed in Section 5.2. Each part shows only PK, FK and UQ
  columns; Section 5.2 lists every column. Grey dashed boxes are tables drawn in full in
  another part. The report uses these three parts for Figure 5.1.
