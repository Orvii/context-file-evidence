# Lulla et al. — does an AGENTS.md make an agent faster and cheaper?

> **Primary source:** Jai Lal Lulla, Seyedmoein Mohsenimofidi, Matthias Galster, Jie M. Zhang, Sebastian Baltes, Christoph Treude. "On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents." arXiv:2601.20404 **v2** (30 Mar 2026). 5 pages, 1 figure, 1 table. Full extraction: [research/impact-agents-md-efficiency.md](../research/impact-agents-md-efficiency.md).
>
> **Axis:** efficiency + cost. **Study type:** experimental (paired). **Agent:** OpenAI Codex with `gpt-5.2-codex` only — *not* Claude Code.

## What it measured

The same 124 GitHub pull-request tasks, run twice each by Codex — once with the repository's root `AGENTS.md` present, once with that file deleted and nothing else changed — measuring wall-clock time and token consumption. 10 repositories sampled from a filtered corpus (132 → 89 with a single root file → 26 whose file covered conventions/architecture/description → 10 at random). Runs happened in isolated per-repository Docker containers with no state carried between tasks.

## The result, stated plainly

**Adding the file made runs faster and, on the mean, cheaper — but the token savings are an artifact of the average.** The distributions are heavily right-skewed (the total-token standard deviation, 1,293,176, is nearly twice the mean, 687,632), so a handful of very expensive runs dominate the mean. The file shrank that expensive tail; it did **not** make the typical run cheaper. The typical run — the median — got *slightly more* expensive.

The paper's own prose says this: *"AGENTS.md primarily reduces token usage in a small number of very high-cost runs, rather than uniformly lowering token consumption across all task instances."* But note the total-token **median** rise appears only in the table — §4 narrates the mean/median split for output, input and cached-input tokens and does not comment on the total-token median. A reader who takes only the abstract's "reduced output token consumption" away will not see it.

## Table 1, verbatim

Column order resolved three ways (header labels, §4 prose, abstract cross-check) and all 15 rows' arithmetic verified. **`Diff = Without − With`; positive `Δ%` = a reduction with the file, negative `Δ%` = an increase with the file.** The caption reads "With and Without" but the columns are ordered `Without | With` — cite the column headers, not the caption's word order.

| Metric | Statistic | Without | With | Diff | Δ% |
|---|---|---:|---:|---:|---:|
| Wall-Clock Time (s) ∗ | Mean | 162.94 | 129.91 | 33.03 | **20.27%** |
| Wall-Clock Time (s) ∗ | Median | 98.57 | 70.34 | 28.23 | **28.64%** |
| Wall-Clock Time (s) ∗ | Std Dev | 182.24 | 136.84 | 45.40 | 24.91% |
| Input Tokens | Mean | 353,010.01 | 318,651.51 | 34,358.50 | 9.73% |
| Input Tokens | Median | 116,609.00 | 120,587.00 | −3,978.00 | **−3.41%** |
| Input Tokens | Std Dev | 654,603.95 | 510,776.51 | 143,827.43 | 21.97% |
| Cached Input Tokens | Mean | 328,877.31 | 296,078.73 | 32,798.58 | 9.97% |
| Cached Input Tokens | Median | 103,424.00 | 104,448.00 | −1,024.00 | **−0.99%** |
| Cached Input Tokens | Std Dev | 632,622.27 | 494,157.89 | 138,464.38 | 21.89% |
| Output Tokens ∗ | Mean | 5,744.81 | 4,591.46 | 1,153.35 | 20.08% |
| Output Tokens ∗ | Median | 2,925.00 | 2,440.00 | 485.00 | 16.58% |
| Output Tokens ∗ | Std Dev | 6,987.74 | 5,161.67 | 1,826.06 | 26.13% |
| Total Tokens | Mean | 687,632.13 | 619,321.70 | 68,310.43 | **9.93%** |
| Total Tokens | Median | 223,707.00 | 226,582.00 | −2,875.00 | **−1.29%** |
| Total Tokens | Std Dev | 1,293,176.16 | 1,009,338.80 | 283,837.36 | 21.95% |

`∗ Statistically significant difference, Wilcoxon signed-rank test (p<0.05)` — the marker appears on the wall-clock and output-token rows only. No exact p-values or confidence intervals are reported.

**Read the two bolded median rows against the two bolded mean rows.** Total tokens: mean −9.93%, median **−1.29% → i.e. up 1.29%**. Input tokens: mean −9.73%, median **up 3.41%**. Same runs, two statistics, opposite directions. Wall-clock time is the one metric where mean and median agree (both fall) — and the paper is explicit that this agreement means the speed-up is general, not tail-driven.

## What this study does NOT say

- **It does not measure correctness.** "Comparable task completion behavior" is qualitative — the abstract's words. No success rate, pass rate, or resolution rate appears anywhere in the paper. A 50-task manual sanity check confirmed the outputs were "non-empty, non-trivial code changes," and that is the whole of the quality evidence. So "faster and cheaper" here says nothing about "more often right" — that is [Gloaguen](gloaguen-success.md) and the [two-agent ablation](two-agent-ablation.md)'s axis.
- **It is not about Claude Code.** One agent, one model (`gpt-5.2-codex`), one completion per condition per task. The authors themselves list replication across "multiple agent systems and model families" as future work.
- **It found no case where the file hurts** beyond the marginal median-token rise. The paper does not explore long-vs-short files, README-restating files, or staleness.
- **Secondary sources got it wrong.** alphaXiv's overview claims the mean/median alignment "suggests a general benefit across most tasks" — true for wall-clock, false for total and input tokens, where the median moved the other way. That sentence is where the "AGENTS.md saves tokens" headline comes from, and it does not survive the table.

## Why it is in this grid

This is the efficiency pole of the disagreement. It is the study most often cited for "AGENTS.md helps," and the citation is usually the mean. The median is in the same table. [SYNTHESIS.md](../SYNTHESIS.md) §2 works through what happens when you put this next to the success-rate and correctness studies.

---

*Version pin: arXiv:2601.20404 v2. If you cite a number from this page, cite v2 — the paper has a v1 (28 Jan 2026) that was not checked here.*
