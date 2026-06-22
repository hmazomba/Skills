# Design Principles Reference

> This reference file is loaded ON DEMAND during Phase 3 (Design Direction) or Phase 6 (Atomic Build).
> Read it when you need detailed guidance on any of the topics below.

## Table of Contents
1. Typography Pairing Rules
2. Color Systems
3. Spacing & Rhythm
4. Layout Patterns
5. Accessibility Standards
6. Animation Guidelines
7. Icon Selection

---

## 1. Typography Pairing Rules

### The Golden Rule
Never use more than 2 typefaces in a single interface. One for headings, one for body. If you need a third, use a monospace for code only.

### Pairing Strategies
| Heading Style | Body Pair | Mood |
|--------------|-----------|------|
| Serif (e.g., Playfair Display) | Sans-serif (e.g., Inter) | Editorial, trustworthy |
| Geometric sans (e.g., Geist) | Humanist sans (e.g., Inter) | Modern, tech |
| Display/variable (e.g., Cabinet Grotesk) | Neutral sans (e.g., DM Sans) | Bold, contemporary |
| Slab serif (e.g., Bitter) | Clean sans (e.g., Source Sans) | Friendly, readable |

### Weight Hierarchy
- Hero/Display: 700–900
- H1: 600–700
- H2–H3: 500–600
- Body: 400 (never go below for readability)
- Caption/Label: 400–500

### Size Scale (Typographic Scale — 1.25 ratio)
- xs: 12px
- sm: 14px
- base: 16px
- lg: 18px
- xl: 20px
- 2xl: 24px
- 3xl: 30px
- 4xl: 36px
- 5xl: 48px
- 6xl: 60px

### Anti-patterns to catch
- Light weight (300) on small body text — kills readability
- All-caps for long text — fatigue after ~6 words
- Mixing two serifs or two geometric sans — they compete
- Identical weights for heading and body — no hierarchy

---

## 2. Color Systems

### Color Roles (always define these)
- **Primary**: Main brand color. Used for CTAs, active states, key UI elements.
- **Secondary**: Supports primary. Accents, secondary actions.
- **Neutral**: Grays. Backgrounds, borders, text.
- **Semantic**: Success (green), Warning (amber), Error (red), Info (blue).

### Shade Generation
For each color, generate a 50–950 scale:
- 50: Near white tint (backgrounds)
- 100–200: Light tints (hover states, subtle backgrounds)
- 300–400: Mid tones (borders, placeholders)
- 500: Base color
- 600–700: Darken for hover/active states
- 800–900: Near black (text on light, inverted contexts)
- 950: Darkest (dark mode surfaces)

### Accessibility — Contrast Ratios (WCAG AA)
- Normal text (<18px): 4.5:1 minimum
- Large text (≥18px bold or ≥24px): 3:1 minimum
- UI components (buttons, inputs): 3:1 minimum
- Always test: use https://webaim.org/resources/contrastchecker/

### Dark Mode Strategy
- Don't invert — dark mode is not "flip all colors"
- Use a distinct neutral scale: avoid pure black (#000), prefer #0f0f0f or #111
- Elevation via lightness, not shadows: dark surfaces go lighter as they elevate
- Reduce saturation slightly on dark: vivid colors are harsh on dark backgrounds

### Anti-patterns
- Pure black (#000000) backgrounds — use very dark gray instead
- Too many accent colors — one accent, used sparingly
- Gradient abuse — one gradient per page, max
- Low-contrast disabled states — still needs 3:1

---

## 3. Spacing & Rhythm

### 8pt Grid
Base all spacing on multiples of 8px (or 4px for fine-grained control):
4, 8, 12, 16, 24, 32, 40, 48, 64, 80, 96, 128

### Component Internal Spacing
- Tight (dense UIs): 8–12px padding
- Comfortable (default): 16–24px padding
- Spacious (marketing/editorial): 32–48px padding

### Section Spacing (vertical rhythm)
- Between related elements: 16–24px
- Between sections: 48–80px
- Hero to first section: 80–120px

### Line Height
- Body text: 1.5–1.6
- Headings: 1.1–1.3 (tighter for large display)
- Code: 1.6–1.8

---

## 4. Layout Patterns

### Grid Systems
- **12-column grid**: Standard for marketing pages. 1-4 columns for content.
- **CSS Grid**: Prefer over flexbox for 2D layouts.
- **Auto-fill/auto-fit**: For responsive card grids without media queries.

### Common Layout Patterns
| Pattern | Use Case | CSS Approach |
|---------|----------|-------------|
| Holy Grail | App with sidebar + main + optional right panel | `grid-template-areas` |
- Bento Grid | Dashboard or feature showcase | CSS Grid with `span` |
- Card Grid | Products, team, posts | `grid-template-columns: repeat(auto-fill, minmax(280px, 1fr))` |
- Sticky Sidebar | Long-form content with TOC | `position: sticky; top: 24px` |
- Full-bleed Hero | Landing pages | `width: 100vw; margin-left: calc(50% - 50vw)` |
- Split Screen | Comparison, auth pages | Two equal columns, `min-height: 100vh` |

### Container Widths
- Narrow (articles): max-width: 65ch
- Content: max-width: 768px
- Standard: max-width: 1200px
- Wide: max-width: 1440px
- Always: padding: 0 16px (mobile) to 0 32px (desktop) for gutters

---

## 5. Accessibility Standards

### WCAG 2.1 AA Checklist (Essentials)
- [ ] Color contrast: 4.5:1 for body, 3:1 for large text and UI
- [ ] Focus visible: All interactive elements have visible focus ring
- [ ] Alt text: All meaningful images have descriptive alt
- [ ] ARIA labels: Icon-only buttons have `aria-label`
- [ ] Keyboard navigation: All interactions reachable via keyboard
- [ ] Form labels: Every input has an associated `<label>`
- [ ] Skip links: Long pages have "Skip to main content"
- [ ] Headings: Logical h1–h6 hierarchy (no skipping levels)

### Focus Ring Implementation
```css
/* Never do this: */
*:focus { outline: none; }

/* Do this instead: */
*:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
  border-radius: 2px;
}
```

### Motion / Reduced Motion
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## 6. Animation Guidelines

### Principles
- **Purpose first**: Every animation must communicate something (state change, hierarchy, feedback)
- **Speed**: UI animations: 150–300ms. Page transitions: 300–500ms. Never exceed 600ms.
- **Easing**: Use `ease-out` for elements entering, `ease-in` for leaving, `ease-in-out` for repositioning.

### Easing Cheat Sheet
| Intent | CSS Value |
|--------|-----------|
| Natural feel | `cubic-bezier(0.4, 0, 0.2, 1)` (Material standard) |
| Snappy/responsive | `cubic-bezier(0, 0, 0.2, 1)` |
| Bounce/playful | `cubic-bezier(0.34, 1.56, 0.64, 1)` |
| Linear (progress bars) | `linear` |

### Micro-interaction Checklist
- Button hover: scale(1.02) or background shift — 150ms
- Card hover: translateY(-2px) + shadow increase — 200ms
- Modal enter: fade + translateY(8px→0) — 250ms
- Tooltip: fade — 150ms
- Toast: slide in from edge — 300ms

### Anti-patterns
- Animating all properties at once — animate 1–2 properties max
- Long delays on page load animations — users perceive as lag
- Infinite spinning/pulsing decorative elements — distracting
- Parallax on mobile — causes jank, skip it

---

## 7. Icon Selection

### Library Comparison
| Library | Style | Best For | Size |
|---------|-------|----------|------|
| Lucide | Outlined, 2px stroke | Modern apps, dashboards | ~1200 icons |
| Phosphor | Multi-weight (thin→bold), versatile | Any project, maximum flexibility | ~7000 icons |
| Heroicons | Outlined + Solid | Tailwind projects, clean UIs | ~300 icons |
| Radix Icons | 15px grid, minimal | Small UI elements, dense layouts | ~300 icons |
| Tabler Icons | Outlined, consistent | Data-heavy apps | ~4000 icons |

### Icon Usage Rules
- Never mix styles (outlined with filled) in the same context
- Size: 16px for inline, 20px for UI actions, 24px for navigation, 32px+ for feature icons
- Always pair icons with labels (or aria-label) — icons alone are ambiguous
- Maintain consistent stroke width across all icons

### Icon Anti-patterns
- Different icon libraries mixed together — visual inconsistency
- Resizing icons beyond their intended grid (blurriness/misalignment)
- Using icons as primary navigation without labels on desktop
- Decorative icons without `aria-hidden="true"`
