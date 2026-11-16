---
name: project-documentation-forge
description: Create, audit, or synchronize four evidence-grounded project documents (PRODUCT-REQUIREMENTS.md, DESIGN-SYSTEM.md, ARCHITECTURE.md, AI-AGENTS.md or AGENTS.md) from a codebase, product idea, prototype, or repository. Use for project documentation setup, spec-driven development, vibe coding handoffs, design systems, architecture documentation, and coding-agent instructions.
---

# Project Documentation Forge

Create four coherent, actionable, traceable documents—not four generic Markdown files. For existing software, describe **observed reality** separately from **planned changes**. For a greenfield project, mark proposed decisions as proposed. Read each relevant template from `assets/` before writing, and apply `references/quality-gates.md` before delivery.

## Trigger and outputs

Use when asked for "the four vibe coding docs", PRD + design system + architecture + AI agent guidelines, project specs, repo documentation setup, or to bring those documents up to date.

Default outputs at target project root:
- `PRODUCT-REQUIREMENTS.md` (PRD)
- `DESIGN-SYSTEM.md`
- `ARCHITECTURE.md`
- `AI-AGENTS.md`

Respect the user's explicit names and established project conventions. `AGENTS.md` is the common instruction filename recognized by coding agents; `AI-AGENTS.md` is the filename in the social post. If the target repo already uses `AGENTS.md`, update it carefully instead of creating competing instructions; optionally maintain `AI-AGENTS.md` as a link/index pointing to the canonical `AGENTS.md`. If tooling uses `CLAUDE.md`, `.github/copilot-instructions.md`, or another runtime-specific instruction file, preserve existing precedence and link rather than blindly duplicate. Never silently overwrite user-owned files.

## Phase 1 — Evidence inventory (required)

1. Identify project root and target branch. Inspect README, manifests and lockfiles, source tree, tests, CI, deployment files, existing specs, agent instructions, design assets, tokens, design files, accessibility checks, and decision logs where available.
2. For each assertion, assign provenance: **Observed** (file path and relevant symbol or line), **Provided** (user or product brief), **Proposed** (recommendation), or **Unknown** (requires confirmation). Avoid presenting proposals as implemented behavior.
3. If input is only an idea: produce useful initial specifications with **Proposed** labels, explicit assumptions and open questions. Do not invent customer interviews, measured KPIs, deployed infrastructure, dependencies or test outcomes.
4. Extract system boundaries, user roles, business outcomes, constraints, journeys, states, interfaces, risks, design foundations and existing agent policies. Prefer raw code, tests, configuration, and direct user requirements to secondary summaries.
5. If missing details do not block a first draft, proceed with documented assumptions; ask only about truly consequential irreversible decisions.

## Phase 2 — Build four documents in dependency order

1. **PRD** — read `assets/product-requirements.template.md`. Capture problem, target audiences, measurable outcomes, scope, journeys, functional requirements with stable IDs and Given/When/Then acceptance tests, nonfunctional requirements, dependencies, risks and open decisions. Never confuse a feature list with user value.
2. **Design system** — read `assets/design-system.template.md`. Inventory existing tokens/components first; document semantic and primitive colour tokens, typography, spacing, density, radii, elevation, breakpoints, states, interaction, accessible contrast and keyboard/focus behaviour, responsive patterns and concrete implementation locations. For non-visual systems, explicitly mark visual sections N/A rather than fabricate a UI.
3. **Architecture** — read `assets/architecture.template.md`. Show C4-style context/container views and only justified component detail; choose Mermaid where text diagrams improve clarity. Document runtime, ownership, data flows, protocols, interfaces, data model, security, operations, failure recovery, testing and ADRs. Mark deployments and integrations as observed/proposed; never leak secrets.
4. **Agent instructions** — read `assets/ai-agents.template.md`. Define repo-specific commands and runbooks; order of authority, allowed edits, safety limits, security, dependencies, tests, change verification, definition of done and documentation sync. Commands must be verified from the repo before marked runnable. Prevent generic policy text from replacing repo conventions.

## Phase 3 — Cross-document traceability

- Every major user-facing capability must map: PRD requirement ID → UI components and states (where applicable) → system component/API/data → tests/verification → agent implementation guidance.
- Use the **same terminology** for roles, domain entities, permissions, environments, and services in all four files.
- Surface contradictions; do not silently choose one source when requirements disagree. Maintain a decision register with owner/status and evidence.
- Apply security-by-design: trust boundaries, authentication, authorization, least privilege, sensitive data classification, auditability, accessibility and error states where relevant.
- Keep exact existing filenames as requested, but use relative links between documents.

## Phase 4 — Publish safely and verify

1. Inspect existing files and diff. Preserve established structure and material decisions. On ambiguous conflicts, record them rather than overwrite.
2. Use Git branching and a reviewable pull request where appropriate and authorized; never force-push or introduce unrelated changes. Respect existing project rules and protected branches.
3. Run available Markdown link checks and `references/quality-gates.md` gates. Validate all referenced commands and paths against the repo. Use independent evidence (tests, source inspection, actual design tokens, real stakeholder sign-off) where possible, never self-assert passing checks.
4. Summarize created/changed files, evidence, verified vs unverified claims, remaining decisions, and commands/tests executed. Clearly disclose any checks that could not run.

## Operating modes

- **Bootstrap**: generate initial four-doc suite from a project idea, making assumptions visible.
- **Reverse-document**: derive the suite from an existing repo; observed architecture first.
- **Sync**: update affected requirements, tokens, architecture and agent guidance after changes; preserve stable IDs.
- **Audit**: report gaps/contradictions without editing unless asked.

## Example invocation

"Use project-documentation-forge on this repository. Inspect source and tests, generate the four documents, preserve existing AGENTS.md rules, link requirements to components and checks, and open a reviewable PR."

## Sources and conventions

- Agent Skills standard: https://agentskills.io/specification
- AGENTS.md convention: https://agents.md/
- C4 model: https://c4model.com/
- Architecture decision records: https://adr.github.io/
- WCAG: https://www.w3.org/TR/WCAG22/
- Design tokens format: https://www.designtokens.org/

Use linked standards as references, not as proof that a particular project implements them.
