# Design System — [Project]

> Status: Observed / Proposed · Owner: [role] · Last reviewed: [YYYY-MM-DD]
> Canonical implementation: [token files, components, Figma or Unknown]

## 1. Design principles
[3–5 testable principles derived from users, constraints and brand; evidence for existing decisions]

## 2. Foundations and token taxonomy
Use **primitive** values only where known and **semantic** roles for usage. Align to existing CSS, tokens or platform conventions rather than inventing a palette.

| Token | Light | Dark | Use | Source/status |
|---|---|---|---|---|
| color.text.primary | [value or TBD] | [value or TBD] | Primary text | Observed / Proposed |
| color.surface.default | [value or TBD] | [value or TBD] | Page background | Observed / Proposed |
| color.action.primary | [value or TBD] | [value or TBD] | Primary actions | Observed / Proposed |
| color.feedback.error | [value or TBD] | [value or TBD] | Error state | Observed / Proposed |

Specify units and token representation (CSS variables, JSON or platform style resources). Include semantic tokens for foreground/background pairs, focus indicators, borders, disabled, warning, success and links.

## 3. Typography
| Role | Font family/fallback | Size | Line height | Weight | Tracking |
|---|---|---|---|---|---|
| Body | [font] | [rem/px] | [ratio] | [weight] | [value] |
| H1–H6 | [scale] | [size] | [ratio] | [weight] | [value] |

[Font loading, licensing, text scaling, overflow, long text and localization]

## 4. Spacing, dimensions and elevation
| Primitive | Value | Usage |
|---|---|---|
| space.1 | [unit] | [usage] |
| radius.sm | [unit] | [usage] |
| shadow.1 | [definition] | [usage] |

[Density, grid, max content width, icon sizes, borders, motion durations, reduced-motion policy]

## 5. Responsive breakpoints
| Name | Width range | Layout behaviour | Verified source |
|---|---|---|---|
| compact | [range] | [rules] | [observed/proposed] |
| medium | [range] | [rules] | [observed/proposed] |
| expanded | [range] | [rules] | [observed/proposed] |

Base breakpoints on **content needs**, not copied device assumptions. Describe touch, pointer and keyboard contexts.

## 6. Component inventory and contracts
For each actual/planned component:
- Name, purpose, source file or proposed location
- API/props or design properties; anatomy/slots
- Variants and sizes; interactive states (default, hover, focus-visible, active, loading, disabled, invalid, success)
- Keyboard behaviour, accessible name, error feedback, ARIA only when necessary
- Responsive behaviour, content restrictions, empty/loading/error states
- Tokens consumed; examples and visual regression references

| Component | Variants | States | Accessibility contract | Source/status |
|---|---|---|---|---|
| Button | primary, secondary, ghost | idle/loading/disabled | focus visible; keyboard activation | [source] |
| Input | text, etc. | idle/invalid/disabled | persistent label; error association | [source] |

## 7. Accessibility and inclusive design
[WCAG version/target, verified contrast ratios, focus visibility/order, hit areas, labels, zoom/reflow, screen readers, reduced motion, error prevention; do not claim compliance without testing]

## 8. Content, icons, imagery and motion
[Voice, capitalization, icon library/licensing, alt-text decision rules, image aspect/asset sources, motion purpose, animation limits]

## 9. Implementation guidance
[Where tokens/components live; naming conventions; theming; storybook/style guide integration; versioning/deprecation]

## 10. QA and governance
[Automated accessibility/visual regression checks, manual keyboard/screen-reader audit, ownership, token change approval]

## 11. Links to requirements
| PRD ID | Screen/flow | Component/pattern | Test evidence |
|---|---|---|---|
| FR-001 | [flow] | [component] | [actual/planned] |

## 12. Unknowns and decisions
[Open brand or interaction decisions; do not guess values]
