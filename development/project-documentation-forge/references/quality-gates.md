# Project Documentation Forge — Quality Gates

## Evidence gate
- [ ] Repo inspected: README, source, manifests, tests, existing instructions and design tokens where available.
- [ ] Observed/Provided/Proposed/Unknown claims distinguish fact from suggestion.
- [ ] No invented users, interviews, KPIs, exact design-token values, API endpoints, infrastructure, dependency versions or successful checks.
- [ ] Paths, commands, external standards and dependency names verified before labelled real.
- [ ] Existing documentation and agent instruction scopes preserved; conflicts made visible.

## PRD gate
- [ ] Problem, audience, outcomes, MVP boundary and non-goals are explicit.
- [ ] Stable unique FR/NFR IDs, testable acceptance criteria, error/permission paths, and measures.
- [ ] Outcomes not confused with output counts; baseline unknowns declared.
- [ ] Risks, decisions, assumptions, and dependencies assigned when possible.

## Design gate
- [ ] Foundations include primitive and semantic colours, type, spacing, radius, breakpoints and relevant states, or declare N/A.
- [ ] Component interactions cover hover/focus/loading/disabled/invalid and keyboard semantics.
- [ ] Contrast, reflow, reduced motion and screen-reader considerations specified; compliance not self-certified.
- [ ] Token values anchored to sources or marked proposed/TBD.

## Architecture gate
- [ ] Context and container boundaries accurate to evidence; deploy vs proposed views separated.
- [ ] Contracts, data ownership, trust boundaries, secrets and failure/recovery paths addressed.
- [ ] Decisions enumerate considered alternatives and acceptance status.
- [ ] Commands, stacks, version numbers and diagrams correspond to observed project state.

## Agent gate
- [ ] Canonical instruction file chosen without competing AGENTS.md/AI-AGENTS.md policies.
- [ ] Commands checked against actual repo files; destructive actions gated.
- [ ] Testing, reporting and handoff instructions concrete and scoped.
- [ ] Agent guidelines explicitly require docs sync and truthfully reporting unrun checks.

## Cross-document gate
- [ ] One vocabulary for actors, entities and services across all four docs.
- [ ] Each substantive FR maps to implementation/design (if relevant) and real or planned verification.
- [ ] Relative links resolve and any N/A references explained.
- [ ] Open questions not converted into phantom implementation claims.
- [ ] Changes reviewed against existing docs; no unrelated files silently altered.

## Independent validation
Prefer existing tests, actual configuration/file inspection, accessibility/visual audits, API contract tests and stakeholder sign-off. Run `skills-ref validate <skill-directory>` when available to check the skill packaging itself; this does **not** prove generated project documents are correct. If a check is unavailable, report Not run and why.
