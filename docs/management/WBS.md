# ShiftManager – Work Breakdown Structure (WBS)

**Course:** Introduction to Software Engineering (HCMUS)  
**Team:** 404NotFound (Team 6)  
**Project:** ShiftManager  
**Document:** PA1 – Section 4.2  
**Status:** Draft for team review

## Scope and structure

This deliverable-oriented WBS uses four levels: **0.0 Project → 1.0–7.0 Phase/Workstream → x.y Deliverable Group → x.y.z Work Package**. Work-package IDs match PA1 Section 4.3 (Estimation) and should be reused in GitHub Projects and the Gantt chart.

**MVP scope:** F01 Sign-in and role-based access; F02 Shift assignment; F03 Schedule views; F04 Swap requests; F05 Co-worker response; F06 Manager decision and atomic shift exchange. **F07** detailed decision history and **F08** email notifications are optional, not required implementation deliverables.

**Tech stack:** React, Node.js/Express, Supabase Auth and Supabase Database (PostgreSQL).

---

## 1.0 Project Initiation & Planning (PA1)

### 1.1 Vision & Scope

- **1.1.1** Preliminary Problem Statement
- **1.1.2** Product Position Statement
- **1.1.3** MoSCoW priorities, scope & exclusions
- **1.1.4** Stakeholders and user interests

### 1.2 Preliminary Solution

- **1.2.1** C4 System Context diagram
- **1.2.2** Technology stack and operating environment

### 1.3 Project Planning

- **1.3.1** Phase gates, exit criteria, roles
- **1.3.2** Three-level WBS for whole project
- **1.3.3** Estimate work-package person-hours
- **1.3.4** Gantt schedule, dependencies & critical path
- **1.3.5** Human resources and project cost

### 1.4 Risk & Tools

- **1.4.1** Risk register, RE, mitigation and owners
- **1.4.2** Repo, board, comms and access evidence

### 1.5 PA Submission

- **1.5.1** Final review, contribution, AI log, export

## 2.0 Requirements Engineering (PA2)

### 2.1 Software Requirements

- **2.1.1** Functional requirements F01–F06 (FRs)
- **2.1.2** NFRs, business rules & acceptance criteria

### 2.2 Use Case Modeling

- **2.2.1** Actors, Use Case diagram
- **2.2.2** Use Case specifications incl exceptions

### 2.3 Requirements Validation

- **2.3.1** UI mockups and screen flows
- **2.3.2** Traceability and review issue log

### 2.4 PA Submission

- **2.4.1** SRS final review, contribution, AI log

## 3.0 Software Design (PA3)

### 3.1 Software Architecture

- **3.1.1** C4 Container, Component, Deployment
- **3.1.2** At least 3 ADRs with justification

### 3.2 Object-Oriented Design

- **3.2.1** Class diagram & class specs
- **3.2.2** Sequence & State diagrams

### 3.3 Database Design

- **3.3.1** ERD and normalized schema
- **3.3.2** Constraints, table specs & indexes

### 3.4 UI/UX Design

- **3.4.1** Screen specs, flow, accessibility checklist

### 3.5 PA Submission

- **3.5.1** Design/SRS traceability review & finalize PA3

## 4.0 Test Planning (PA4)

### 4.1 Test Strategy

- **4.1.1** Test Plan, environment, entry/exit, defect process

### 4.2 Test Design

- **4.2.1** Equivalence Partitioning and BVA design
- **4.2.2** Decision tables for shift/swap constraints

### 4.3 Test Cases & Coverage

- **4.3.1** Detailed test cases for F01–F06
- **4.3.2** Requirements–test traceability review

### 4.4 PA Submission

- **4.4.1** Final test plan review, contribution & AI log

## 5.0 Implementation, Testing & Deployment (PA5)

### 5.1 Development Foundation

- **5.1.1** Create React/Express project and local dev config
- **5.1.2** Supabase PostgreSQL schema, migrations, user profiles and test data

### 5.2 Authentication & Shift Management

- **5.2.1** Supabase Auth integration, JWT verification and role-based authorization (F01)
- **5.2.2** Shift assignment + overlap validation (F02)
- **5.2.3** Employee/manager roster views (F03)

### 5.3 Shift Swap Workflow

- **5.3.1** Create and validate swap requests (F04)
- **5.3.2** Co-worker accept/reject response (F05)
- **5.3.3** Manager approval, recheck & atomic exchange (F06)
- **5.3.4** Integrate swap workflow UI with REST API

### 5.4 Software Verification

- **5.4.1** Unit tests and coverage report
- **5.4.2** Automated cases (2 use cases × 2 scenarios), PR CI
- **5.4.3** Test execution, defect fixes and PR reviews

### 5.5 Deployment & Delivery

- **5.5.1** Deploy and verify live demo
- **5.5.2** Demo video, implementation report, retrospective

## 6.0 Final Presentation & Demo

### 6.1 Presentation Preparation

- **6.1.1** Prepare slides and project summary
- **6.1.2** Demo script + practice all speakers

### 6.2 Final Delivery

- **6.2.1** Final demo and presentation

## 7.0 Project Management & Monitoring

### 7.1 Weekly Monitoring

- **7.1.1** Weekly status meetings W02–W10
- **7.1.2** Weekly Status Report W03
- **7.1.3** Weekly reports W02 and W04–W10 (8 reports)

### 7.2 Project Control

- **7.2.1** Maintain GitHub task board
- **7.2.2** Git/PR reviews, risks, baselines, change records

---

## Tracking notes

- **Each x.y.z entry is an assignable work package.** Assign one accountable owner and a person-hour estimate in PA1 Section 4.3; establish dates and dependencies in the Gantt chart (PA1 Section 4.4).
- **7.1.1 and 7.1.3 are effort roll-ups for recurring activities.** Track each weekly meeting and each weekly report (W02–W10) as a separate dated issue. Do not rewrite or backdate earlier reports.
- **Supabase update:** Work packages 5.1.2 and 5.2.1 reflect the team's agreed use of Supabase Database and Supabase Auth; confirm their exact labels match the latest PA1 Estimation table.
- **Review:** The work packages below are planning deliverables. The team must validate work assignments, estimates and scope before treating this as the final PA1 baseline.
