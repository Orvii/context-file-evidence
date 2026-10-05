# The grid — four studies, one question per axis

Snapshot date: **2026-10-05**. Every cell cites a primary source; versions pinned per study. Secondary coverage is linked as corroboration only and is never the citation for a number.

## Symbols

| | |
|---|---|
| ▲ | the file helped this metric (direction verified against the source's own column headers / sign convention) |
| ▼ | the file hurt this metric |
| ∅ | measured, no detectable effect — with the power bound the study reports |
| — | not measured by this study |
| ⚠ | mean and median disagree, or the finding is exploratory/underpowered — read the note |

## Experimental studies — does the file change agent outcomes?

| Metric | [Lulla et al.](studies/lulla-efficiency.md) · efficiency | [Gloaguen et al.](studies/gloaguen-success.md) · success | [Khatri](studies/two-agent-ablation.md) · correctness |
|---|---|---|---|
| **Agents** | Codex (`gpt-5.2-codex`) only | Claude Code (Sonnet-4.5), Codex (GPT-5.2, GPT-5.1 mini), Qwen Code (Qwen3-30b-coder) | Claude Code (`claude-sonnet-4-6`), Codex CLI (`gpt-5.5`) |
| **Tasks** | 124 real merged PRs, 10 repos | SWE-bench Lite (300) + own benchmark (138 instances, 12 repos) | 17 real merged PRs × 3 repeats, 3 repos |
| **Conditions** | with vs without the repo's file | None / LLM-generated / developer-written | none / always_on / selective-wiki |
| **Task success / correctness** | — (only a 50-task manual "non-trivial output" sanity check) | ▼ LLM files: −0.5% (SWE) / −2% (own bench) resolution (v1); "does not generally improve" (v3) · ▲ Dev files: +2.4%, **p=0.21 — not significant** (v3) · ▲ Dev over LLM: +7%, **p=0.038** | ∅ null on both agents; TOST bounds ≤10pp (Claude) / ≤15pp (Codex); omnibus p=1.00 / 0.66 |
| **Wall-clock time** | ▲ mean −20.27%, median −28.64% (Wilcoxon p<0.05) | — | ⚠ −24% on one repo, one agent, exploratory (p=0.125, n=5) |
| **Token cost** | ⚠ mean ▼9.93% cheaper, **median ▲1.29% dearer** (total); same split for input tokens | ▼ inference cost +20%/+23% (LLM files, SWE/own bench), up to +19% (Dev files) | — |
| **Steps / effort** | — | ▼ +2.45/+3.92 steps (LLM files); +3.34 (Dev files); permutation p≤0.03 on all | ⚠ full-suite test runs 3.67→2.44→1.67 with context (opshin only) |
| **Reasoning tokens** | — | ▼ +22%/+10% (GPT-5.2/5.1-mini, SWE, v3); +14%/+10% (own bench); Dev +20%/+2% | — |
| **Significance testing** | Wilcoxon signed-rank (2 row groups only), no p-values or CIs reported | CMH + stratified permutation tests, p-values reported (v3) | bootstrap + permutation + TOST + Monte-Carlo power; **the most rigorous uncertainty reporting in the set** |
| **Repeats per task** | 1 (paired) | 1 ("We sample completions for each agent once") | 3 |
| **What it cannot tell you** | correctness — no success metric exists in the paper | wall-clock efficiency; non-Python behavior | effects smaller than ~10–15pp; non-Python repos; whether *task-specific* files would help |

## The observational study — what the files contain

| [Chatlatanagulchai et al.](studies/agent-readmes.md) | v2 (9 Aug 2026), 2,303 files / 1,925 repos |
|---|---|
| Most common content | Testing 75.9% · Impl. details 70.8% · Architecture 68.1% · Dev process 65.1% · Build/run 63.0% |
| Rare content | Security **14.8%** · Performance **14.5%** · UI/UX 8.7% · Project mgmt 5.4% |
| Maintenance | 67% of Claude files touched in multiple commits; median interval 23.8h; edits accrete — deletions negligible |
| Run by this study | **no agents.** Content statistics are not performance evidence. |
| Version hazard | v1→v2 changed **11 of 16** percentages; most secondary coverage still quotes v1 (62.3% build/run, 14.5% security) |

## Where the three experiments agree

Not in their headlines — in their mechanisms:

1. **Instructions are followed.** Gloaguen: "the absence of improvements with context files is not due to a lack of instruction-following." Khatri's probe: the channel is live, files rate Good/Excellent, behavior moves. Lulla: exploration drops when structure is described upfront. All three measured the agent *obeying the file*.
2. **Behavior moves in the direction the file points.** Gloaguen's files add process requirements → more tests, more steps, more reasoning tokens. Khatri's opshin file warns the suite is slow → *fewer* full-suite runs, less wall-clock. Same obedience, opposite efficiency sign. The file's content, not its existence, is the variable.
3. **The measured effect on being *right* is small.** Gloaguen's point estimates: −3% (LLM) to +2.4% (Dev, p=0.21). Khatri's power analysis: a 10pp effect is undetectable below ~120 tasks; even 30pp would be caught only 57% of the time at this n. Every success-axis number in circulation is inside the band where the largest study in the set can see nothing.
4. **Cost and steps go up wherever both are measured.** Gloaguen: +20–23% cost, +2.45–3.92 steps, significant. Lulla's token mean falls only via the tail; its median rises. There is no study in this set where the typical run got cheaper *and* more correct.

## Where they disagree — and why it is not a contradiction

| Headline | Source | The resolution |
|---|---|---|
| "AGENTS.md saves 20% of tokens" | Lulla mean, quoted secondhand | The median rose 1.29%. The saving is a shrunken expensive tail, not a cheaper typical run. Same table. |
| "AGENTS.md cuts runtime 28%" | Lulla median | True for wall-clock on this corpus — the one metric where mean and median agree. Says nothing about correctness, which the paper does not measure. |
| "Context files reduce success" | Gloaguen v1 (−3% LLM) | v3 softens to "does not generally improve"; Dev-vs-None is p=0.21. Direction survives; strength does not. And it is v1 that InfoQ quoted. |
| "Context files don't matter" | Khatri null | A null with a stated 10–15pp bound is not "no effect"; it is "no effect bigger than this, undetectable at this n". The author says so explicitly. |
| "Files make agents test more" vs "files cut test runs" | Gloaguen vs Khatri | Both true — see agreement #2. Opposite file contents, obedient agents, opposite behavior. |

---

*Regeneration note: cells were transcribed from the four extraction reports under [research/](research/), each of which carries its own evidence log, arithmetic checks, and UNVERIFIED sections. Where a source disagrees with itself across versions, the cell carries the version tag.*
