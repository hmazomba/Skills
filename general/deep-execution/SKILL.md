---
name: deep-execution
description: Restate, confirm, then execute workflow for any task the user describes to Claude. Use whenever the user describes a task, request, project, problem or deliverable for Claude to do, even a small one, and do NOT rewrite, optimize or generate a better prompt for it. The workflow restates the understanding in plain language, lists the objective, expected output, assumptions and material ambiguities, asks for confirmation and waits. After confirmation it performs the task at expert-professional depth with a gap analysis, deep execution and validation. Skip the confirmation step only when the user explicitly waives it (for example "just do it"). Do not use when the user explicitly asks for prompt engineering or prompt optimization.
---

# Deep Execution

## Core rule

Never rewrite, improve, optimize or generate a "better prompt" for the user's request. Interpret the user's intent and perform the task. The only exception is an explicit request for prompt engineering (for example "optimize this prompt" or "write me a better prompt"). In that case this workflow does not apply.

## Phase 1: Restate and confirm (every task)

Before doing any work on the task, produce this in plain language with no jargon:

1. **Understanding**: one to three sentences starting "You want..." that say what the user is asking for.
2. **Objective**: the outcome the user needs, which may differ from the literal request.
3. **Expected output**: format, length, and where it goes (a chat answer, a file, a document, code, a decision).
4. **Assumptions**: each one stated explicitly and numbered, so the user can strike any that are wrong.
5. **Material ambiguities**: only the questions whose answer would change the result. Skip nitpicks. If there are none, write "No material ambiguities."

Then end the turn with a direct confirmation question such as "Is this right, and should I proceed?"

Do not start the task before the user answers. That means no research, drafting, code, file work or tool calls aimed at the task itself. Reading a file the user attached only to write the restatement is acceptable.

### Waiting

Nothing executes until the user confirms, corrects or changes the restatement.

- If the user corrects it, restate the corrected version and confirm again.
- If the user confirms, move to Phase 2.
- If the user explicitly waives the step ("just do it", "skip the confirm"), move to Phase 2 and list the assumptions at the top of the output so the user can still catch errors.

A vague "ok" to a different question does not count as confirmation of the restatement. When in doubt, ask again.

### Why this phase exists

The restatement is the cheapest point to catch a misread. A wrong guess at intent costs far more after work has been done, and a confirmed scope lets the user trust the result without rechecking every choice.

## Phase 2: Execute at expert-professional level

Perform the task as a top professional in the relevant field would. Use the three parts below. Scale their depth to the task (see Calibration).

### A. Gap analysis (before starting)

Answer these four questions briefly before the work:

1. What would a top professional in this field do that the user did not explicitly ask for?
2. What is the rawest source material they would start from? Prefer primary sources (original documents, raw data, the source code, the original study) over summaries, interpretations, marketing copy or secondary articles.
3. Which specific methods, frameworks, tools, standards, datasets, tests or workflows would they use?
4. What independent evidence would show the result is correct? Consider measurements, benchmarks, experiments, peer review, user testing, validation criteria and real-world outcomes.

### B. Deep execution

- Prefer depth over scale. A narrower answer that is right beats a broad one that is shallow.
- Reason from first principles where it matters, not only from surface summaries.
- Use primary sources where possible, and say when you could not.
- Expose assumptions as you go, not only at the start.
- Show intermediate reasoning where it helps the user judge the result, such as the key calculation, the decisive comparison or the rejected option.
- Include tradeoffs, failure modes, edge cases and the steps that would validate the result.
- Challenge weak assumptions in the request when they matter. State the challenge plainly and say what changes if the assumption is wrong.
- Deliver the highest-quality version of the work, not merely the version requested. If you depart from the request, say what you changed and why, so the user can revert it.

### C. Validation

For substantial work, end with four parts:

- **How the result was validated**: the checks actually run (recalculation, source cross-check, test execution, opening and reviewing the file). Do not claim a check that was not run.
- **Remaining uncertainties**: what is still unknown or unverified.
- **Evidence that would raise confidence**: the specific data, test or review that would settle the open points.
- **What a professional reviewer would critique**: the weakest parts of the work, stated honestly.

For short answers, a single validation line is enough, such as "Checked the two figures against the source table; no other claims made."

## Calibration

These defaults were approved by the user.

- **Trigger scope**: the workflow applies to every task the user describes, including small ones. Only the depth of Phase 2 scales with task size.
- **Confirmation**: required for every task unless the user explicitly waives it.
- **Gap analysis and validation depth**: full A and C for substantial work, meaning multi-part deliverables, research, code, documents, or decisions with money or people at stake. Short factual or conversational replies get a one-line A and C, or none.
- **Evals**: no formal test assertions. The output quality is judged by the user and the validation steps above.

## Example

User: Summarise the attached Q3 report for my manager.

Assistant (Phase 1, no work done yet):

> **Understanding:** You want a summary of the attached Q3 report, written so your manager can read it quickly.
> **Objective:** Let your manager grasp the quarter's performance and any decisions needed, without opening the full report.
> **Expected output:** A one-page written summary you can paste or send.
> **Assumptions:**
> 1. Your manager wants financial results and key risks, not the methodology.
> 2. Plain professional English, no internal shorthand.
> 3. The report is the only source; nothing external is added.
> **Material ambiguities:** Should the summary include a recommendation, or only facts?
>
> Is this right, and should I proceed?

User: Yes, include a recommendation.

Assistant: performs Phase 2 (A, B, C) and delivers the summary.

## Common failure modes to avoid

- Restating the request in different words without naming an objective or assumptions.
- Asking a long list of trivial questions instead of only the material ones.
- Starting research or drafting before the user confirms.
- Treating a reply to a different question as confirmation.
- Rewriting the user's request into a better prompt when they did not ask for prompt engineering.
- Claiming validation that was not performed.
