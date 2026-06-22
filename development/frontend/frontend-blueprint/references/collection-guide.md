# Reference Collection Guide

> Load this during Phase 2 (Reference Collection) when the user struggles to articulate preferences.

## Table of Contents
1. Question Strategies by User Confidence Level
2. Contrast Pairs for Quick Alignment
3. Design Direction Templates

---

## 1. Question Strategies by User Confidence Level

### High Confidence User (has references, knows what they want)
Minimal questions needed. Confirm what you already have:
- "What specifically do you like about [reference]?"
- "Anything from [reference] you want to avoid?"
- "Are there constraints I should know about? (existing design system, brand guidelines)"

Move quickly to Phase 3.

### Medium Confidence User (has some ideas, can't fully articulate)
Use anchoring — tie abstract to concrete:
- "You mentioned 'clean'. Is that more like Apple.com (lots of whitespace, restrained) or Linear.app (dark, focused, slightly denser)?"
- "When you say 'modern', do you mean tech/startup modern (Vercel, Figma) or bold/editorial modern (Awwwards style)?"
- "What product do you use daily that you think is well-designed? Let's start there."

### Low Confidence User (no references, unsure)
Use elimination and contrast pairs. Don't overwhelm. Ask one question at a time:

**Round 1 — Vibe:**
"Let's find your direction. Which of these three feels closest to what you're after?
- (A) Minimal and airy — lots of whitespace, subtle grays, refined typography
- (B) Bold and high-contrast — dark backgrounds, vivid accents, strong type
- (C) Warm and approachable — rounded corners, soft colors, friendly feel"

**Round 2 — Density (after Round 1):**
"And in terms of how much info is shown at once:
- Spacious — one focus at a time, breathing room between elements
- Balanced — standard density, content-forward
- Dense — lots of data visible, power-user feel"

**Round 3 — Color Temperature:**
"Color direction:
- Cool (blues, grays, white — tech, professional)
- Warm (amber, terracotta, cream — human, approachable)
- Neutral (no strong temperature — flexible, safe)"

After 3 rounds you have enough to propose a Design Direction in Phase 3.

---

## 2. Contrast Pairs for Quick Alignment

Use these when the user gives you an adjective. Offer the pair and ask which end they're closer to:

| Adjective given | Contrast pair to ask |
|----------------|---------------------|
| "Clean" | Clean like Apple (spacious, lots of white) or clean like Notion (dense, functional)? |
| "Modern" | Modern like Vercel (dark, minimal, tech) or modern like Stripe (light, colorful, editorial)? |
| "Professional" | Professional like McKinsey.com (formal, serif, dark blue) or professional like Linear (dark, sleek, efficient)? |
| "Fun" | Fun like Duolingo (character-driven, playful illustrations) or fun like Framer (bold gradients, kinetic type)? |
| "Minimal" | Minimal like Swiss/grid design (strict, typographic) or minimal like Japanese aesthetic (wabi-sabi, asymmetric whitespace)? |
| "Bold" | Bold in color (vivid palette, high contrast) or bold in type (large, heavy weight headlines)? |
| "Dark" | Dark like VS Code (pure utility, no flair) or dark like Raycast (dark with color accents and depth)? |
| "Elegant" | Elegant like high-fashion sites (serif, black/white, luxury feel) or elegant like Craft (soft shadows, smooth transitions)? |

---

## 3. Design Direction Templates

Use these as starting points when you don't have strong references to build from.
Modify based on Phase 2 findings. Always present as a starting point, not a final decision.

### Template A: Modern SaaS (Light)
```
Mood: Clean and focused
Color palette:
  Primary: #6366f1 (indigo)
  Neutral: #f1f5f9 (slate-100) to #0f172a (slate-900)
  Accent: #f59e0b (amber) for highlights
Typography:
  Headings: Geist (700) — geometric, technical
  Body: Inter (400) — highly legible, neutral
Layout: 12-column, max-width 1200px, 24px gutters, cards with 8px radius
Icons: Lucide (outlined, 1.5px stroke)
```

### Template B: Dark Tech Dashboard
```
Mood: Focused and data-dense
Color palette:
  Background: #0a0a0f (near-black)
  Surface: #111118
  Border: #1e1e2e
  Primary accent: #7c3aed (violet)
  Secondary accent: #06b6d4 (cyan)
  Text: #e2e8f0
Typography:
  Headings: IBM Plex Mono or JetBrains Mono — code aesthetic
  Body: Inter (400/14px) — compact but legible
Layout: Sidebar (240px) + main area, 8px base unit, tight density
Icons: Lucide or Tabler (16px for inline, consistent stroke)
```

### Template C: Warm Editorial / Content Site
```
Mood: Warm and readable
Color palette:
  Background: #fafaf9 (warm off-white)
  Surface: #ffffff
  Primary: #a16207 (warm amber-800)
  Text: #1c1917 (warm near-black)
  Accent: #dc2626 (red for highlights)
Typography:
  Headings: Playfair Display (700) — editorial, authoritative
  Body: Source Serif 4 or Lora (400/18px) — long-form readable
  UI: Inter (400/14px) — for nav, labels, buttons
Layout: Narrow max-width (768px) for content, generous line height (1.7)
Icons: Minimal — use sparingly, prefer text labels
```

### Template D: Bold Marketing / Landing Page
```
Mood: Bold and energetic
Color palette:
  Background: #09090b (near black)
  Primary gradient: from #7c3aed to #db2777 (purple → pink)
  Text: #ffffff
  Muted: #71717a
Typography:
  Headings: Cabinet Grotesk or Clash Display (800) — loud, distinctive
  Body: Inter or DM Sans (400/16px)
Layout: Full-width hero, bento-style feature section, generous section spacing (100px+)
Icons: Phosphor (light weight for contrast against bold type)
Animation: Subtle gradient mesh, floating elements, scroll-triggered reveals
```

### Template E: Clean Admin / Internal Tool
```
Mood: Efficient and trustworthy
Color palette:
  Background: #f8fafc (very light gray)
  Surface: #ffffff
  Primary: #2563eb (blue-600)
  Border: #e2e8f0
  Text: #0f172a
Typography:
  All: Inter (400 body, 500 labels, 600 headings) — single family, multiple weights
Layout: Sidebar navigation (256px) + content area, 8px grid, compact density
Icons: Heroicons (outlined) — clean, standard sizes
```
