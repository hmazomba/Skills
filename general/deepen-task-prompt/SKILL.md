---
name: deepen-task-prompt
description: Deepen an existing task prompt without expanding its scope. Use when asked to sharpen, deepen, rewrite, or improve a prompt by identifying expert practices, raw source material, specific methods and tools, and independent evidence that would establish correctness.
---

# Deepen a Task Prompt

Keep the task's intended outcome and scope fixed. Increase rigor, evidence quality, and verifiability; do not add deliverables or broaden the problem.

## Workflow

1. Parse the supplied prompt. State its intended outcome, boundaries, and any assumptions that matter. Preserve the user's voice and constraints where practical.
2. Identify what a strong practitioner in the relevant field would do that the prompt omits. Name only actions that improve the same outcome; avoid generic best-practice padding.
3. Identify the least-processed useful source material to start from: primary records, raw data, source files, direct observations, original measurements, or equivalent evidence for the domain. Explain briefly why it is closer to the facts than summaries or digests. Do not claim unavailable material exists.
4. Name the concrete methods and tools suited to this task. Match them to the domain and scale. Prefer specific analysis or production methods and tool categories; name products or versions only when useful and verified. Browse for current, niche, or fast-changing tool details when needed.
5. Define independent evidence that could show the result is right. Use observable acceptance criteria, reproducible checks, authoritative references, instrumented measurements, domain-expert review, or real-world outcomes as appropriate. Do not make the model or the user's approval the sole proof. Distinguish what can be verified now from what requires later testing or access.
6. Deliver two parts:
   - **Expert gap analysis:** concise answers to the four questions: what expert does beyond request; rawest starting material; specific methods and tools; independent evidence of correctness.
   - **Rewritten prompt:** a ready-to-use prompt that asks for this rigorous approach while keeping the original goal and scope intact.
7. In the rewritten prompt, require the future agent to inspect available source material before relying on digests, state assumptions and unknowns, choose methods/tools for reasons, and tie each major claim or deliverable to evidence. Ask it to report limitations instead of filling gaps with guesses.

## Rewrite quality checks

- Keep the original objective recognizable and bounded.
- Add depth through better inputs, methods, reasoning, and checks—not through extra features, broader research, or more deliverables.
- Make methods and tools concrete to the subject. Avoid pretending one workflow fits every field.
- Make validation independent and observable. A checklist written by the same agent is not sufficient by itself.
- Keep the final prompt directly usable. Replace unspecified details with clear placeholders such as `[task]` or `[available source material]`; do not invent context.
- Be concise. Include only instructions that change the quality or verifiability of the requested result.

## Response shape

### What an expert would add
[One short, task-specific answer.]

### Raw material to start from
[Name most direct available inputs and why.]

### Methods and tools
[Concrete methods/tools with fit to task.]

### Independent proof
[Observable criteria and independent checks.]

### Rewritten prompt
[Ready-to-use prompt preserving the original goal and scope.]
