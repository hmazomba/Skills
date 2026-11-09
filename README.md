# 🧠 ai-skills

> A personal collection of custom AI skills — structured prompt instruction sets that extend AI coding assistants with expert personas, opinionated workflows, and hard-won methodology. Some are production-grade. Some are experiments. All of them are built for real work.

---

## What is a skill?

A skill is a `SKILL.md` file that tells an AI assistant *how to think* about a specific class of task — not just what to do. Each one encodes a persona, a phased workflow, smart defaults for ambiguous inputs, and guardrails that prevent common failure modes.

The goal: high-quality first output, without five rounds of back-and-forth calibration.

---

## Skills

### 🧰 General

---

#### 🤝 [`cedric`](file:///Q:/AI/Skills/general/cedric/SKILL.md)
**Status:** Production · **Domain:** Ideation & Design Thinking

Cedric is a design thinking ideation partner that nurtures an idea from first spark to a working solution. It guides through the five stages of human-centered design — Empathize, Define, Ideate, Prototype, and Test — iteratively rather than as a fixed checklist. Challenges assumptions, defers judgment during ideation, and delivers honest critique during validation stages.

**Triggers on:** "I have an idea for", "help me develop this", "brainstorm", "ideate", "how might we", "prototype this", "is this idea worth pursuing", or any request to take a concept from inception to a real solution.

---

#### ⚡ [`deep-execution`](file:///Q:/AI/Skills/general/deep-execution/SKILL.md)
**Status:** Production · **Domain:** Task Execution & Workflow

A structured restate-confirm-execute workflow for any task. Before doing any work, it restates the user's request in plain language (objective, expected output, assumptions, material ambiguities) and waits for confirmation. After confirmation, it executes at expert-professional depth with a gap analysis, deep execution, and validation. Scales from one-liners to complex multi-part deliverables.

**Core rule:** Never rewrite or optimize the user's request into a "better prompt" — it interprets intent and performs the task.

**Triggers on:** Any task, request, project, problem, or deliverable the user describes.

> **Note:** Also available under [`productivity/deep-execution`](file:///Q:/AI/Skills/productivity/deep-execution/SKILL.md).

---

#### 🔍 [`deep-research`](file:///Q:/AI/Skills/general/deep-research/SKILL.md)
**Status:** Production · **Domain:** Research & Content Generation

Replaces shallow single-search lookups with a four-phase systematic research methodology. Must be loaded before any content generation task to ensure output is grounded in real, multi-angle evidence.

**Phases:** `Broad Exploration → Deep Dive → Diversity & Validation → Synthesis Check`

**Quality bar:** Research is sufficient only when you have key facts and data, 2–3 concrete real-world examples, expert perspectives, current trends, and known limitations. Never generate content from general knowledge alone.

**Triggers on:** "what is X", "explain X", "compare X and Y", "research X", or any question that a single web search wouldn't answer properly; and before creating presentations, articles, UI mockups, or any content requiring real-world information.

---

### 🏗️ Development

---

#### 🏛️ [`vibe-coding-architect`](file:///Q:/AI/Skills/development/frontend/vibe-coding-architect/SKILL.md)
**Status:** Production · **Domain:** App Architecture & AI-Assisted Development

Transforms a raw app idea, a competitor teardown, an article, or a URL into a production-ready architectural spec and a copy-paste-ready prompt for AI coding tools like Lovable, Bolt, v0, Cursor, and Claude Code.

**What it produces:**
- Intelligence Summary (for source-based inputs like URLs or articles)
- App naming options
- User journey and state model
- Ring-fenced FOSS tech stack (Next.js · Tailwind · shadcn/ui · Zustand · TanStack Query · Zod) — zero hallucinated packages
- Bespoke design system that avoids generic SaaS aesthetics
- Accessibility, resilience, and performance constraints
- Final execution prompt block, ready to paste

**Triggers on:** "turn this idea into a build prompt", "spec this app", "competitor teardown", "vibe coding prompt", any website URL or blog post you want to reverse-engineer into a build plan.

---

#### 🎨 [`frontend-blueprint`](file:///Q:/AI/Skills/development/frontend/frontend-blueprint/SKILL.md)
**Status:** Production · **Domain:** UI/UX & Frontend Implementation

A senior frontend design consultant persona. Runs a structured discovery process before generating a single line of code — collecting visual references, design tokens, typography preferences, icon style, and layout direction to ensure pixel-perfect fidelity on the first attempt. Supports Google Stitch prototyping (via MCP or manual prompts) for visual validation before code.

**Workflow:** `BRIEFING → REFERENCES → DESIGN DIRECTION → [STITCH PROTOTYPING] → EXECUTION PLAN → ATOMIC BUILD → REVIEW`

**Core principle:** A wrong first draft costs more time than two minutes of discovery. Never generate code without context.

**Triggers on:** "build me a UI", "design a page", "create a component", "improve this layout", "redesign", or any frontend/interface request with or without mockups.

---

#### 🎛️ [`ui-ux-pro-max`](file:///Q:/AI/Skills/development/design/ui-ux-pro-max/SKILL.md)
**Status:** Production · **Domain:** UI/UX Design Intelligence

A comprehensive design intelligence system covering 50+ styles, 97 color palettes, 57 font pairings, 99 UX guidelines, and 25 chart types across 9 technology stacks (React, Next.js, Vue, Svelte, SwiftUI, React Native, Flutter, Tailwind, shadcn/ui). Uses a searchable CLI tool to generate full design systems — style, palette, typography, effects, and anti-patterns — from a single keyword query.

**Workflow:** Analyze requirements → `--design-system` query → supplement with domain searches → stack-specific guidelines → implement.

**Priority categories:** Accessibility (CRITICAL) → Touch & Interaction (CRITICAL) → Performance (HIGH) → Layout & Responsive (HIGH) → Typography & Color → Animation → Style Selection → Charts & Data.

**Triggers on:** Any UI design, build, review, or improvement request; button, modal, navbar, card, dashboard, landing page, mobile app, or any visual element in any supported stack.

---

#### ☕ [`vaadin-dev`](file:///Q:/AI/Skills/development/frontend/vaadin-dev/SKILL.md)
**Status:** Production · **Domain:** Enterprise Java / Spring Boot UI

An expert Senior Vaadin Developer persona for designing, building, debugging, and optimizing Vaadin web applications. Targets Vaadin 24+ (Flow and Hilla) with Spring Boot. Produces production-ready, idiomatic code — no tutorials unless explicitly requested.

**Core expertise:** Clean MVP architecture · Grid & DataProvider (lazy-loading enforced for >100 rows) · Binder with full validation · Push and `UI.access()` for async · Lumo theme customization · JS interop · Accessibility compliance · `@Route` navigation · Spring Security integration.

**Stack defaults:** Vaadin 24+ · Spring Boot · Maven/Gradle · Java (Kotlin on request).

**Triggers on:** Any mention of Vaadin, Flow, Hilla, Binder, DataProvider, `@Route`, `@Push`, Vaadin Grid, Lumo theme, or Vaadin component errors.

---

### 🎮 Three.js & Game Development

---

#### 🧪 [`threejs-prompt-optimizer`](file:///Q:/AI/Skills/development/threejs-prompt-optimizer/SKILL.md)
**Status:** Production · **Domain:** Three.js / WebGL Prompt Engineering

Turns rough, vague, or underspecified Three.js / WebGL / 3D game ideas into precise, production-ready prompts for AI coding agents. Uses the **4-D method** (Deconstruct → Diagnose → Develop → Deliver) to surface performance traps, verify API names against real Three.js docs, and bake constraints into the output prompt so the downstream agent can't miss them.

**Output:** A structured prompt with System Role, Technical Task Overview, Non-Negotiables & Performance Constraints, Architecture & Stack, and Step-by-Step Implementation Instructions.

**Triggers on:** Any Three.js, WebGL, 3D scene, shader, particles, `InstancedMesh`, raycasting, splines, physics, post-processing, or browser 3D game idea — even if the user never says the word "prompt".

> **Note:** Also available at the top level under [`threejs-prompt-optimizer`](file:///Q:/AI/Skills/threejs-prompt-optimizer/SKILL.md).

---

#### 🔨 [`game-forge`](file:///Q:/AI/Skills/development/threejs/game-forge/SKILL.md)
**Status:** Production · **Domain:** Three.js Game Recreation

An autonomous game development orchestrator. Takes a reference game (title, screenshots, videos, descriptions, or playable builds) and transforms it into a playable, well-documented Three.js recreation using **specification-driven development**. Never jumps from description to implementation — always produces a full spec first (requirements, design, architecture, test plan, traceability matrix) and verifies against it.

**Process:** Initialisation → Reference Acquisition → Reverse Engineering → Specification → Design → Architecture → Implementation Planning → Execution → Testing → Fidelity Refinement.

**Triggers on:** "recreate this game in Three.js", "build a browser version of [game]", any named game + screenshots/videos + a request to build it.

---

#### 🎮 [`unity-gamedev-advisor`](file:///Q:/AI/Skills/gamedev/unity-gamedev-advisor/SKILL.md)
**Status:** Production · **Domain:** Unity Game Development (Unity 6 LTS)

An expert advisor for Unity 6.x LTS game development. Gives accurate, version-aware advice on scripting, Input System, physics, Animator, ScriptableObjects, tilemaps, NavMesh, builds, performance, and genre architecture. Diagnoses before prescribing for bugs — names the most likely causes in order and says how to confirm each in the Editor before giving the fix.

**Coverage:** C# scripting & lifecycle · Input System 1.x · PhysX (Unity 6 renames) · Animator & blend trees · ScriptableObjects & event channels · 2D tilemaps & RuleTiles · NavMesh (AI Navigation 2.0) · Build pipeline & CI.

**Genre playbooks:** RPG, FPS, Platformer, Roguelike, Card Game, Puzzle, Survival/Crafting, Tower Defense, Visual Novel, Prototype/Jam.

**Triggers on:** Any Unity question, bug report, architecture question, or genre design request.

---

#### 🧩 [`godot-prompt-optimizer`](gamedev/godot-prompt-optimizer/SKILL.md)
**Status:** Production · **Domain:** Godot Game Development / MCP Prompt Engineering

Turns rough game ideas into precise Godot 4 prompts, specs, implementation plans, and test criteria. Integrates **NPGameDev Godot MCP Toolkit**, **IvanMurzak Godot-MCP** (Asset Library 5245), and **Coding-Solo godot-mcp**. Includes pinned, non-destructive [NPGameDev installer](gamedev/godot-prompt-optimizer/scripts/install_mcp_toolkit.py) and [setup guide](gamedev/godot-prompt-optimizer/references/mcp-installation.md).

**Triggers on:** Godot project setup, MCP installation, Godot scene/script planning, game idea optimization, Godot debugging, and spec-driven game development.

---

### 🎵 Creative

---

#### 🎵 [`strudel-agent`](file:///Q:/AI/Skills/creative/strudel-agent/SKILL.md)
**Status:** Experimental / Personal · **Domain:** Algorithmic Music & Live Coding

An AI-powered live-coding composer and sound designer for [Strudel.cc](https://strudel.cc) — a browser-based port of TidalCycles to JavaScript. Generates complete, runnable Strudel patterns from a genre and/or BPM, with verified API calls, modular layer architecture, and genre-specific defaults built in. Ships with two performance variations per response.

**Smart defaults (no form-filling required):**

| Genre | BPM | Scale |
|---|---|---|
| Techno | 134 | A minor |
| Afrobeats | 110 | F minor |
| Ambient | 85 | D dorian |
| House | 128 | C minor |
| Drill | 140 | G minor |
| Jazz | 95 | C minor |

**Includes reference modules** for the full verified API, sample banks & scales, and genre presets with performance techniques.

**Triggers on:** "make a beat", "live code a track", "generate a [genre] pattern", "strudel", "algorithmic music".

---

### 🗺️ Context Engineering

---

#### 🗺️ [`docs-sitemap-extractor`](file:///Q:/AI/Skills/context-engineering/docs-sitemap-extractor/SKILL.md)
**Status:** Production · **Domain:** Developer Tooling & Documentation

Extracts a complete, deduplicated list of every page URL in a documentation or help site, grouped by the site's own sidebar sections. Handles the two hardest cases: Astro/static sidebars (single-fetch strategy) and JS-rendered navs (search-cached snippet stitching).

**Workflow:** Check for sitemap/JSON search index → Fetch landing page → Cross-reference JS-rendered sections via search → Walk every top-level section → Normalize & deduplicate → Flag gaps with a confidence note.

**Why it exists:** A single homepage fetch surfaces a fraction of real page count. Collapsed sub-sections and JS-rendered navs hide the rest.

**Triggers on:** "get me every link from these docs", "map the full structure of this site", any docs URL where you need section-grouped page lists.

---

## Repository Structure

```
Skills/
├── archives/                        # Legacy .skill format archives
├── context-engineering/
│   └── docs-sitemap-extractor/
│       └── SKILL.md
├── creative/
│   └── strudel-agent/
│       ├── SKILL.md
│       └── references/
│           ├── api.md
│           ├── sounds.md
│           └── genres.md
├── development/
│   ├── design/
│   │   └── ui-ux-pro-max/
│   │       └── SKILL.md
│   ├── frontend/
│   │   ├── frontend-blueprint/
│   │   │   ├── SKILL.md
│   │   │   └── references/
│   │   ├── vaadin-dev/
│   │   │   ├── SKILL.md
│   │   │   ├── assets/
│   │   │   └── references/
│   │   └── vibe-coding-architect/
│   │       └── SKILL.md
│   ├── threejs/
│   │   └── game-forge/
│   │       └── SKILL.md
│   └── threejs-prompt-optimizer/
│       └── SKILL.md
├── gamedev/
│   └── unity-gamedev-advisor/
│       └── SKILL.md
├── general/
│   ├── cedric/
│   │   └── SKILL.md
│   ├── deep-execution/
│   │   └── SKILL.md
│   └── deep-research/
│       └── SKILL.md
├── productivity/
│   └── deep-execution/
│       └── SKILL.md
└── threejs-prompt-optimizer/
    └── SKILL.md
```

---

## Philosophy

Skills encode hard-won trial-and-error. The methodology inside each one is the result of iterating on real tasks — not writing ideal specs from scratch.

A skill that works is one where the AI behaves differently (and better) than it would without it. The test is always: *does this save meaningful time on the second and third run?*

---

*Built by [Hlumisa Mazomba](https://github.com) · Deviare / HWY Creative Studio · Johannesburg, ZA*
