# Chatlatanagulchai et al. — what is actually inside 2,303 context files?

> **Primary source:** Worawalan Chatlatanagulchai, Hao Li, Yutaro Kashiwa, Brittany Reid, Kundjanasith Thonglek, Pattara Leelaprute, Arnon Rungsawang, Bundit Manaskasemsak, Bram Adams, Ahmed E. Hassan, Hajimu Iida. "Agent READMEs: An Empirical Study of Context Files for Agentic Coding." arXiv:2511.12884 **v2** (9 Aug 2026). Full extraction: [research/agent-readmes-observational.md](../research/agent-readmes-observational.md).
>
> **Axis:** content. **Study type:** observational — *this paper runs no agent experiments.* Every number here describes what files contain and how they are maintained, not whether they help.

## What it measured

The first large-scale census of agent context files: **2,303 files from 1,925 open-source repositories** (922 `CLAUDE.md`, 694 `AGENTS.md`, 687 `copilot-instructions.md`), drawn from the AIDev dataset of repos where agentic tools actually contribute, filtered to ≥5 stars. Four research questions: characteristics, maintenance frequency, instruction content (16-type taxonomy), and automatic classifiability.

## The content finding — the guardrail gap

Percentage of files containing each instruction type (v2, Table 3):

| Instruction type | % of files | | Instruction type | % of files |
|---|---:|---|---|---:|
| Testing | **75.9%** | | Maintenance | 44.6% |
| Impl. Details | **70.8%** | | Conf. & Env. | 38.9% |
| Architecture | **68.1%** | | Documentation & Refs | 26.8% |
| Development Process | 65.1% | | Debugging | 25.3% |
| Build and Run | 63.0% | | AI Integration | 24.1% |
| System Overview | 59.0% | | DevOps | 18.4% |
| | | | **Security** | **14.8%** |
| | | | **Performance** | **14.5%** |
| | | | UI/UX | 8.7% |
| | | | Project Mgmt | 5.4% |

The paper's reading, verbatim: *"developers use context files to make agents functional, they provide few guardrails to ensure that agent-written code is secure or performant."* Roughly one file in seven mentions security at all.

## ⚠️ The version drift — and why this repo exists

**v1 (17 Nov 2025) and v2 (9 Aug 2026) disagree on 11 of the 16 percentages**, and secondary coverage still quotes v1:

| | v1 | v2 |
|---|---:|---:|
| Testing | 75.0% | **75.9%** |
| Impl. Details | 69.9% | **70.8%** |
| Architecture | 67.7% | **68.1%** |
| Build and Run | 62.3% | **63.0%** |
| Security | 14.5% | **14.8%** |
| Development Process | 63.3% | **65.1%** |

The v1 abstract's headline example was "build and run commands (62.3%)"; v2's is "test procedures (75.9%)". If a blog quotes 62.3%, it is citing a nine-month-old version. The corpus itself did not change (still 2,303/1,925) — the classification did. Full delta table in the [extraction report](../research/agent-readmes-observational.md).

## The maintenance finding — files grow, they don't shrink

- **67.0%** of Claude Code files are modified across multiple commits (Copilot 59.8%, Codex 59.4%).
- Median interval between changes: **23.8 hours** (Claude Code), 22.3 h (Codex), 68.0 h (Copilot). These are active configuration surfaces, not documentation.
- Edits are "small, incremental additions"; **deletions are negligible** (median deleted words < 15). The ratchet only turns one way — the mechanism behind every "my AGENTS.md became a ball of mud" story.
- The files are hard to read: Flesch Reading Ease medians of 42.4–51.4 (lower = harder), and the paper calls them "complex, difficult-to-read artifacts" whose length "cannot be explained by task difficulty."

## What this study does NOT say

It says nothing about whether any of this content helps agents — no agent was run. The natural temptation is to read "security appears in 14.8% of files" as "files make code insecure"; the paper makes no such claim, and neither should anyone citing it. What it *does* supply is the base rate for the other three studies: the files being tested are mostly functional instructions (tests, build, architecture), maintained by accretion, and rarely say anything about security or performance.

## Why it is in this grid

It is the observational anchor. When [Gloaguen](gloaguen-success.md) finds that LLM-generated repository overviews do nothing, this study shows the overviews are in ~59% of real files anyway; when [the two-agent ablation](two-agent-ablation.md) finds the file helped most where it warned "the test suite is slow", this study shows testing instructions are the single most common content (75.9%). The census tells you what the experiments were actually testing.

---

## What the paper says about its own numbers

The §7 the HTML rendering hides (recovered from the PDF) bounds how the table above may be used: the 16 labels are **binary**, so "75.9% Testing" means *mentions testing somewhere*, not that tests are well specified — "the frequency reported for a category represents only the prevalence of the topic, not the depth, complexity, or qualitative richness". Labels were set by two independent inspectors at **80.3% agreement** with a third resolving conflicts. The readability scores measure surface form, not comprehension ("low FRE scores ... may partly reflect technical vocabulary and document form rather than genuine comprehension difficulty"). And the corpus is three tools — Claude Code, Codex, Copilot — which the authors themselves call limiting.

*Version pin: arXiv:2511.12884 **v2** (9 Aug 2026); v1 values recorded in the delta table above; §7 recovered verbatim from the v2 PDF.*
