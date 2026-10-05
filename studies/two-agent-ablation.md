# Khatri — a correctness null, with the confidence intervals to prove how much it isn't

> **Primary source:** Prakhar Khatri. "Do Context Files Help Coding Agents? A Two-Agent Ablation Study on Real Repositories." REALM @ EMNLP 2026 (under review), arXiv:2607.27250 (28 Jul 2026, v1). Code + data: [codeprakhar25/context-files-coding-agents](https://github.com/codeprakhar25/context-files-coding-agents). Full extraction: [research/two-agent-ablation.md](../research/two-agent-ablation.md).
>
> **Axis:** correctness + process efficiency. **Study type:** experimental ablation. **Agents:** Claude Code (`claude-sonnet-4-6`) and Codex CLI (`gpt-5.5`).

## What it measured

17 real merged-PR tasks (15 shared + 2 Codex-only) from three Python repositories — `OpShin/opshin`, `firebase/firebase-admin-python`, `pdm-project/pdm` — each run 3 times per condition by both agents, scored by **gold-test evaluation**: the agent's patch passes only if the real PR's test suite passes with zero failures. Three context strategies, verbatim from the paper:

- `none` — "The AGENTS.md file is removed from the workspace." The agent works from the codebase alone.
- `always_on` — "The full AGENTS.md content is injected into the system prompt every turn," and removed from the workspace to prevent double-reading. The strongest possible injection.
- `selective` — the file is split into topic-organized wiki files the agent retrieves on demand via a system-prompt hint.

## The headline: a null, replicated

| Agent | none | always_on | selective |
|---|---:|---:|---:|
| Claude Code (15 tasks) | 53.3% (24/45) | 55.6% (25/45) | 55.6% (25/45) |
| Codex (17 tasks) | 58.8% (30/51) | 56.9% (29/51) | 52.9% (27/51) |

Up for Claude, down for Codex, and **none of it detectable**: omnibus permutation p=1.00 (Claude), p=0.66 (Codex); TOST equivalence bounds every pairwise difference to ≤10pp (Claude) / ≤15pp (Codex).

## The part other summaries skip: the null is honest about its own power

The author does not claim "context files have no effect." The claim is narrower and better:

- "MDE at n=17, reps=3: even a large Δ=30pp effect is caught only 57% of the time."
- "Detecting Δ=10pp at 80% power requires ∼120–200 tasks."
- "The result is power-limited, and we say so."

So the correct reading of this study is: *any effect of a repository context file on correctness is smaller than ~10–15 percentage points, and this experiment could not have seen anything smaller.* That is a real constraint on the debate — the +2.4% and −3% point estimates in [Gloaguen](gloaguen-success.md) live comfortably inside it — and it is also a model for how to report a null. Contrast with a headline like "AGENTS.md doesn't work," which this data cannot support.

## Where context DID move something: process, not pass-rate

On `opshin` tasks, Claude Code with context ran the **blind full test suite** far less often — 3.67 → 2.44 → 1.67 runs per cell across none → always_on → selective — cutting wall-clock ~24% (2689s → 2066s → 2032s; sign-flip p=0.125 at n=5, flagged exploratory). The mechanism, from the README: *"the AGENTS.md warns the suite is slow and nudges the agent toward targeted tests."*

That is a different picture from [Gloaguen](gloaguen-success.md)'s "agents run more tests with context files." Both are true: Gloaguen's files add *requirements* (more thorough testing as instructed, on repos where the file describes process); this file contained a *warning* (suite is slow → run less of it, more precisely). What the file says determines which way behavior moves. The effect was Claude-only and opshin-only — Codex durations were flat.

## The manipulation-validity probe — the null is not an inert-file artifact

A fair objection to any null: maybe the injected file was junk. The author tested that directly: re-ran the two convention-closest near-miss tasks (opshin 554, firebase 907) under all three strategies, both agents, 3 repeats (36 cells). Result: *"The real AGENTS.md never converts a failure to a pass on either agent"* — but the channel is demonstrably live: the agents read the files and rate them Good/Excellent on the study's own quality rubric, and on Claude's firebase-907 cell context actually **depressed** correctness (none 2/3 → always_on 1/3 → selective 0/3).

The study's summary: *"context can narrowly depress correctness but never manufactured a pass."* The tasks that failed were skill-gated — "engineering precision, not a missing fact", "deep type-system reasoning". A file cannot hand an agent a capability.

## Known confounds (the author's list, condensed)

1. Injection-channel asymmetry: Claude gets context via system prompt, Codex via user-turn prepend — a between-agent confound; within-agent comparisons stay clean.
2. `always_on` is stronger than the natural workflow (agent discovers the file itself) — the author argues guaranteed presence bounds natural discovery, but flags it as inference, not measurement.
3. The `selective` wiki equals the AGENTS.md only for opshin; for pdm/firebase it was a ~10–18× larger auto-generated repo wiki.
4. Mixed run provenance (Claude repeat-0 local, repeats 1–2 on a pod) — sensitivity check shows pass-rates move ≤3.3pp, so it does not drive the result.
5. Run-count discrepancy: the paper says 288 evaluated runs, the shipped database says 291. Unexplained; flagged here rather than papered over.
6. Three Python repos, two models, one date — "the null may shift as these models are updated."

## Why it is in this grid

It is the correctness pole with the most rigorous uncertainty reporting in the set: pre-registered-style strategy definitions, gold-test oracle, permutation + equivalence testing, an explicit power analysis, and a validity probe. Its null is what keeps the [Gloaguen](gloaguen-success.md) "context files reduce success" headline honest — a 2–3pp reduction is exactly the size this study proves nobody can currently detect. [SYNTHESIS.md](../SYNTHESIS.md) §3.

---

*Version pin: arXiv:2607.27250 v1 (28 Jul 2026) + repository `main` as fetched 2026-10-05. Model pins: `claude-sonnet-4-6`, `gpt-5.5`.*
