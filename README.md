# 🧠 ai-skills

> A personal collection of custom AI skills — structured prompt instruction sets that extend Claude with expert personas, opinionated workflows, and hard-won methodology. Some are production-grade. Some are experiments. All of them are built for real work.

---

## What is a skill?

A skill is a `.md` file that tells Claude *how to think* about a specific class of task — not just what to do. Each one encodes a persona, a phased workflow, smart defaults for ambiguous inputs, and guardrails that prevent common failure modes.

The goal: high-quality first output, without five rounds of back-and-forth calibration.

Skills live in `/skills/user/` and are automatically triggered by Claude when a matching request comes in.

---

## Skills

### 🏗️ `vibe-coding-architect`
**Status:** Production · **Domain:** App architecture & AI-assisted development

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

### 🎨 `frontend-blueprint`
**Status:** Production · **Domain:** UI/UX & frontend implementation

A senior frontend design consultant persona. Runs a structured discovery process before generating a single line of code — collecting visual references, design tokens, typography preferences, icon style, and layout direction to ensure pixel-perfect fidelity on the first attempt.

**Workflow:** `BRIEFING → REFERENCES → DESIGN DIRECTION → [STITCH PROTOTYPING] → EXECUTION PLAN → ATOMIC BUILD → REVIEW`

**Core principle:** A wrong first draft costs more time than two minutes of discovery. Never generate code without context.

**Triggers on:** "build me a UI", "design a page", "create a component", "improve this layout", "redesign", or any frontend/interface request with or without mockups.

---

### 🔍 `deep-research`
**Status:** Production · **Domain:** Research & content generation

Replaces shallow single-search lookups with a four-phase systematic research methodology. Load this before any content generation task — presentations, articles, UI designs, reports — to ensure output is grounded in real, multi-angle evidence rather than general knowledge.

**Phases:** Broad Exploration → Deep Dive → Diversity & Validation → Synthesis Check

**Quality bar:** Research is sufficient only when you have key facts and data, 2–3 concrete real-world examples, expert perspectives, current trends, and known limitations. Not before.

**Triggers on:** "what is X", "explain X", "compare X and Y", "research X", or any question that a single web search wouldn't answer properly.

---

### 🗺️ `docs-sitemap-extractor`
**Status:** Production · **Domain:** Developer tooling & documentation

Extracts a complete, deduplicated list of every page URL in a documentation or help site, grouped by the site's own sidebar sections. Handles the two hardest cases: Astro/static sidebars (single-fetch strategy) and JS-rendered navs (search-cached snippet stitching).

**Workflow:** Check for sitemap/JSON search index → Fetch landing page → Cross-reference JS-rendered sections via search → Walk every top-level section → Normalize & deduplicate → Flag gaps with a confidence note.

**Why it exists:** A single homepage fetch surfaces a fraction of real page count. Collapsed sub-sections and JS-rendered navs hide the rest.

**Triggers on:** "get me every link from these docs", "map the full structure of this site", any docs URL where you need section-grouped page lists.

---

### 🎵 `strudel-agent`
**Status:** Experimental / Personal · **Domain:** Algorithmic music & live coding

An AI-powered live-coding composer and sound designer for [Strudel.cc](https://strudel.cc) — a browser-based port of TidalCycles to JavaScript. Generates complete, runnable Strudel patterns from a genre and/or BPM, with verified API calls, modular layer architecture, and genre-specific defaults built in.

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

### ☕ `vaadin-dev`
**Status:** Production · **Domain:** Enterprise Java / Spring Boot UI

An expert Senior Vaadin Developer persona for designing, building, debugging, and optimizing Vaadin web applications. Targets Vaadin 24+ (Flow and Hilla) with Spring Boot. Produces production-ready, idiomatic code — no tutorials unless explicitly requested.

**Core expertise:** Clean MVP architecture · Grid & DataProvider (lazy-loading enforced for >100 rows) · Binder with full validation · Push and `UI.access()` for async · Lumo theme customization · JS interop · Accessibility compliance · `@Route` navigation · Spring Security integration.

**Stack defaults:** Vaadin 24+ · Spring Boot · Maven/Gradle · Java (Kotlin on request).

**Triggers on:** any mention of Vaadin, Flow, Hilla, Binder, DataProvider, `@Route`, `@Push`, Vaadin Grid, Lumo theme, or Vaadin component errors.

---

## Structure

```
skills/
└── user/
    ├── vibe-coding-architect/
    │   └── SKILL.md
    ├── frontend-blueprint/
    │   └── SKILL.md
    ├── deep-research/
    │   └── SKILL.md
    ├── docs-sitemap-extractor/
    │   └── SKILL.md
    ├── strudel-agent/
    │   ├── SKILL.md
    │   └── references/
    │       ├── api.md
    │       ├── sounds.md
    │       └── genres.md
    └── vaadin-dev/
        └── SKILL.md
```

---

## Philosophy

Skills encode hard-won trial-and-error. The methodology inside each one is the result of iterating on real tasks — not writing ideal specs from scratch.

A skill that works is one where Claude behaves differently (and better) than it would without it. The test is always: *does this save meaningful time on the second and third run?*

---

## Roadmap / In Progress

- `lyra` — Prompt optimization persona using a 4-D methodology, for cross-platform AI prompt engineering
- `ui-ux-pro-max` — Design system specialist, higher fidelity than frontend-blueprint for complex multi-screen products
- `skill-creator` — Meta-skill for building, testing, and benchmarking new skills

---

*Built by [Hlumisa Mazomba](https://github.com) · Deviare / HWY Creative Studio · Johannesburg, ZA*