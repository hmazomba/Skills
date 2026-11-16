# AI Coding Agent Instructions — [Project]

> Apply only in this project. Status: [observed/proposed]. Canonical file: [AGENTS.md or AI-AGENTS.md]

## Mission and scope
[Product purpose; exact repo boundaries and definition of successful contribution]

## Source-of-truth priority
1. Explicit user instructions and applicable platform/security rules.
2. Repository-specific instructions already in force; preserve nested AGENTS.md scopes.
3. Current PRD for product behaviour, DESIGN-SYSTEM for UI, ARCHITECTURE for system boundaries.
4. Observed code and tests for **current implemented behaviour**; record conflicts with specs rather than blindly follow outdated prose.
5. Proposals and defaults, clearly marked.

When sources conflict, report the exact mismatch and obtain needed decision; do not silently override higher-authority rules.

## Repository map
| Path | Responsibility | Editing guidance |
|---|---|---|
| [verified path] | [role] | [rules] |

## Allowed / forbidden changes
**Allowed:** [scoped source/tests/docs modifications and approved tooling].
**Forbidden without explicit authorization:** deleting user data, force pushes, publishing releases, changing paid services, installing unverified dependencies, exfiltrating secrets, turning off security, migrating production data, expanding repo scope.

## Required implementation process
1. Read task, relevant PRD IDs and existing tests/source.
2. Reproduce or characterize current behaviour; record uncertainty.
3. Make smallest coherent changes; follow existing naming, style, type, dependency and architectural conventions.
4. Add tests for positive, negative and boundary behaviours; update affected docs and change/decision records.
5. Run relevant build/lint/test/security/accessibility checks that actually exist; distinguish Passed, Failed, Not run.
6. Review diff for unrelated changes, secrets, generated artifacts, accessibility gaps and breaking contracts.
7. Handoff: changed paths, requirements covered, checks and outputs, residual risks/open decisions.

## Verified commands
| Task | Command | Evidence/path | Status |
|---|---|---|---|
| Install | [only command verified against manifest/README] | [source] | Verified / Unknown |
| Build | [command] | [source] | Verified / Unknown |
| Test | [command] | [source] | Verified / Unknown |
| Lint | [command] | [source] | Verified / Unknown |

Never fabricate command names. Never claim a command ran without tool output.

## Coding standards and boundaries
[Language/runtime versions evidenced by manifests; module structure; error handling; types; test placement; logging; environment variables; data handling; performance guardrails]

## UI standards
[Use DESIGN-SYSTEM tokens/components, accessible labels/focus, empty/error/loading states, responsive patterns; mark N/A if headless]

## Security and privacy
[Never output real credentials; no secrets in client code; auth/authz at trusted boundary; validate untrusted inputs; avoid destructive operations without authorization]

## Decision and documentation maintenance
[How to handle open questions, ADRs and cross-document traceability; PRD FR-ID → code/tests and design tokens]

## Definition of done
[Behaviour meets acceptance criteria, applicable checks pass or limitations disclosed, no scope creep, docs synced, deploy/rollback notes where required]

## Handoff template
- Task / PRD IDs:
- Files changed:
- Behaviour and alternatives:
- Tests run and actual results:
- Tests not run and why:
- Security/accessibility review:
- Remaining risks and decisions:
