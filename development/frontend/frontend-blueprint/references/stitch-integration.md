# Stitch Integration Guide

> Load this when entering Phase 4 (Stitch Prototyping) or when the user asks about Google Stitch, MCP setup, or visual prototyping.

## Table of Contents
1. What is Google Stitch
2. Stitch Prompt Formula & Templates
3. MCP Setup Guide
4. Design Systems Mapping
5. Variants Workflow
6. Device Type Guidance
7. MCP Tools Reference (14 tools)
8. Troubleshooting

---

## 1. What is Google Stitch

Google Stitch (stitch.withgoogle.com) is a browser-based UI prototyping tool that generates visual screen designs from text prompts. It outputs editable HTML/CSS that can be exported and used as a code starting point.

**Key capabilities:**
- Generate screens from text prompts
- Create and apply Design Systems for consistency
- Generate Variants (multiple design options)
- Edit Theme (colors, fonts, dark mode, corner radius)
- Create interactive Prototypes
- Export to HTML

**When to use it:** Before writing code, to visually validate the direction. Particularly valuable when the user has no Figma/Sketch mockups.

---

## 2. Stitch Prompt Formula & Templates

### The Formula
```
[Idea] + [Theme] + [Content] + [Image (optional)]
```

Every prompt should include all three required parts. Be specific. Use UI/UX vocabulary.

### Vocabulary that works well in Stitch prompts
**Layout terms:** navigation bar, sidebar, hero section, card layout, grid, bento grid, data table, form, modal, drawer, bottom sheet, tab bar, breadcrumb, pagination

**Interaction terms:** call-to-action button, toggle, dropdown, search bar, filter panel, stepper, progress bar

**Visual terms:** drop shadow, glassmorphism, gradient overlay, frosted glass, divider, avatar, badge, chip/tag, tooltip

**Quality adjectives:** clean, minimal, spacious, elegant, bold, dense, modern, editorial, professional, playful

### Style Word Bank
Use these as theme modifiers in your prompts:

| Style | Description | Use for |
|-------|-------------|---------|
| Bento Grid | Asymmetric card-based layout | Dashboards, feature showcases |
| Editorial | Magazine-style, strong typography | Content sites, portfolios |
| Glassmorphism | Frosted glass effect, blur backgrounds | Modern apps, overlays |
| Neumorphism | Soft shadows, extruded feel | Settings, controls |
| Brutalist | Raw, unpolished, high contrast | Bold brands, statement pages |
| Cyberpunk | Neon, dark, glitch aesthetics | Gaming, tech, edgy brands |
| Swiss/Grid | Rigid grid, typographic focus | Professional, corporate |
| Wabi-sabi | Organic, imperfect, warm | Artisan brands, lifestyle |
| Skeuomorphic | Real-world textures and depth | Niche/retro contexts |
| Memphis | Geometric shapes, bold colors | Playful, creative brands |

### Prompt Templates

**Dashboard:**
```
[SaaS analytics dashboard for [domain]]. [Clean, minimal design with [color] accent on [light/dark] background]. [Sidebar navigation with [items]. Main area shows [KPI cards] at top, [chart type] in center, and [table/list] below. Header with user avatar and notifications].
```

**Landing Page Hero:**
```
[Landing page hero for [product type]]. [Bold, modern design with [color] gradient and dark background]. [Centered headline "[placeholder text]", supporting paragraph, primary CTA button "[text]" and secondary link. Abstract background element. Navigation bar with logo left, links center, sign up button right].
```

**Onboarding / Auth:**
```
[Sign up screen for [app type]]. [Clean light theme, single-column centered layout]. [Logo at top, "Create your account" heading, form with name/email/password fields, submit button, "Already have an account? Sign in" link. Optional: social login buttons above form with divider].
```

**Settings Page:**
```
[User settings page for [app type]]. [Minimal light design with subtle borders]. [Left sidebar with settings categories: [list]. Main content area shows [category] settings with toggle switches, input fields, and save button. Danger zone section at bottom for destructive actions].
```

**Mobile App Screen:**
```
[Mobile app [screen name] for [app type]]. [iOS-style design with [theme] background]. [Status bar at top. [Screen-specific content description]. Bottom tab navigation with [tab items]]. Choose Mobile device type.
```

### Refinement Prompt Patterns
When the user wants to tweak a generated screen, use these focused patterns:

- **Color change:** "Change [element] background to [color/hex]. Update [related elements] to maintain contrast."
- **Layout shift:** "Move [element] to [position]. Adjust spacing to maintain visual balance."
- **Typography:** "Increase [heading/body] font size to [size]. Change font weight to [weight]."
- **Component swap:** "Replace [old element] with [new element]. Keep the same position and surrounding layout."
- **Density:** "Make the layout [more spacious/more dense]. Adjust padding on [elements] to [increase/reduce] by about [amount]."
- **Dark mode:** "Convert to dark mode. Use #0f172a for the main background, #1e293b for cards. Adjust text colors for contrast."

---

## 3. MCP Setup Guide

### Generic MCP Configuration Pattern
Most MCP clients follow this config structure (Claude Desktop, Cursor, etc.):

```json
{
  "mcpServers": {
    "stitch": {
      "command": "npx",
      "args": ["-y", "@google/stitch-mcp"],
      "env": {
        "STITCH_API_KEY": "YOUR_API_KEY_HERE"
      }
    }
  }
}
```

**Config file locations:**
- Claude Desktop (Mac): `~/Library/Application Support/Claude/claude_desktop_config.json`
- Claude Desktop (Windows): `%APPDATA%\Claude\claude_desktop_config.json`
- Cursor: `.cursor/mcp.json` in the project root or global settings
- Other clients: check the client's documentation for MCP server configuration

### Getting a Stitch API Key
1. Go to stitch.withgoogle.com
2. Sign in with your Google account
3. Navigate to Settings → API Keys
4. Create a new key and copy it
5. Add it to your MCP config as shown above

### Verifying the Connection
After configuring, restart your MCP client. You should see Stitch tools available. Test with: "Create a new Stitch project called 'test'."

---

## 4. Design Systems Mapping

When creating a Design System in Stitch from a Phase 3 Design Direction:

| Design Direction property | Stitch Design System field |
|--------------------------|---------------------------|
| Primary color (hex) | `customColor` → primary |
| Secondary/accent color | `customColor` → secondary |
| Preset color name (if using standard) | `preset` (e.g., "blue", "violet", "emerald") |
| Light/Dark theme | `colorMode` → "light" or "dark" |
| Heading font | `font` → heading |
| Body font | `font` → body |
| Border radius style | `roundness` → "none", "small", "medium", "large", "full" |

### Supported Fonts in Stitch (29 fonts)
Inter, Roboto, Open Sans, Lato, Montserrat, Raleway, Poppins, Nunito, Source Sans Pro, PT Sans, Ubuntu, Merriweather, Playfair Display, Lora, Georgia, Times New Roman, DM Sans, Space Grotesk, Outfit, Sora, Plus Jakarta Sans, Geist, IBM Plex Sans, IBM Plex Mono, JetBrains Mono, Fira Code, Source Code Pro, Cabinet Grotesk, Clash Display

**If the requested font is not in this list:** Pick the closest match and note the substitution. Example: "Geist Mono isn't available in Stitch — I'll use JetBrains Mono as a stand-in for prototyping. We'll use the actual font in code."

---

## 5. Variants Workflow

Use variants when the user wants to compare design options before committing.

### When to suggest variants
- User isn't sure between 2 directions
- A major layout decision needs validation
- Exploring different levels of density or visual weight

### How to guide the user (manual workflow)
1. "In Stitch, with your screen open, click 'Generate' → 'Variants'"
2. "Set Creative Range to 'Explore' for maximum diversity, or 'Refine' to stay close to the current design"
3. "Select which Aspects to vary: Layout, Colors, Typography, or Imagery"
4. "Generate 3 variants and share screenshots of the ones you like"

### With MCP connected
Use `generate_variants` with:
- `creativeRange`: "explore" (more diverse) or "refine" (subtle changes)
- `aspects`: array of ["layout", "colors", "typography", "imagery"] — include only what you want to vary

---

## 6. Device Type Guidance

| Project type | Stitch device setting |
|-------------|----------------------|
| Website / landing page | Web |
| Dashboard / admin panel | Web |
| Mobile app (iOS/Android) | Mobile |
| Tablet app | Tablet |
| Email template | Web (narrow viewport) |
| Browser extension | Web (compact) |

Always specify device type when generating prompts manually. For MCP: use the `deviceType` parameter.

---

## 7. MCP Tools Reference (14 tools)

### Project Management
- `create_project(title)` — Create a new Stitch project. Returns project_id.
- `list_projects()` — List all projects. Returns array of {project_id, title, created_at}.
- `get_project(project_id)` — Get project details including all screens.
- `delete_project(project_id)` — Delete a project and all its screens.

### Design System
- `create_design_system(project_id, options)` — Create a design system. Options: `preset`, `customColor`, `colorMode`, `font`, `roundness`.
- `update_design_system(project_id, options)` — Update existing design system properties.
- `apply_design_system(project_id, screen_ids?)` — Apply design system to all screens (or specific ones).

### Screen Generation
- `generate_screen_from_text(project_id, prompt, deviceType?)` — Generate a screen from a text prompt. Returns screen_id and screenshot URL.
- `generate_variants(project_id, screen_id, creativeRange, aspects)` — Generate design variants. Returns array of {screen_id, screenshot_url}.
- `edit_screens(project_id, screen_ids, edit_prompt)` — Apply a targeted edit to one or more screens.

### Screen Management
- `list_screens(project_id)` — List all screens in a project with IDs and names.
- `get_screen(project_id, screen_id, format?)` — Get screen data. Format: "screenshot" (default) or "html". Returns URL or HTML string.
- `rename_screen(project_id, screen_id, name)` — Rename a screen.
- `delete_screen(project_id, screen_id)` — Delete a specific screen.

### Usage Notes
- Always get `project_id` before working with screens
- `generate_screen_from_text` takes 10-30 seconds — inform the user
- `get_screen` with `format: "html"` returns the full HTML/CSS source
- Stitch HTML uses inline styles — always rewrite for the target framework

---

## 8. Troubleshooting

| Issue | Likely cause | Solution |
|-------|-------------|---------|
| Stitch tools not showing | MCP not configured or not restarted | Re-check config, restart client |
| API key error | Wrong key or expired | Generate new key at stitch.withgoogle.com |
| "Font not found" | Font not in Stitch's 29-font library | Pick closest supported font, note substitution |
| Generated design looks generic | Prompt too vague | Add specific colors, layout details, content examples |
| Variants too similar | Creative range too low | Set `creativeRange` to "explore", vary more aspects |
| HTML export looks different in browser | Inline styles, no reset | Add CSS reset, convert inline to classes, test in target browser |
| Stitch screen doesn't match design direction | Design system not applied | Run `apply_design_system` after creating/updating it |
