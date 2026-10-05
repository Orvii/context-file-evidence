# Primary-source extraction — "On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents"

Extraction note: produced by a read-only research pass over arXiv:2601.20404 (v2) using ~20 targeted extraction passes with different queries over the same URLs. Column order was resolved three independent ways (header transcription, §4 prose labelling, abstract cross-check) and the arithmetic of all 15 table rows was verified. Items not found in the primary source are marked `unknown — not found in the primary source` rather than filled from secondary coverage.

## 1. Citation block

- **Title:** "On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents"
- **Authors, in order, with affiliations (as printed on page 1):**
  1. Jai Lal Lulla — Singapore Management University, Singapore, Singapore
  2. Seyedmoein Mohsenimofidi — Heidelberg University, Heidelberg, Germany
  3. Matthias Galster — University of Bamberg, Bamberg, Germany
  4. Jie M. Zhang — King's College London, London, United Kingdom
  5. Sebastian Baltes — Heidelberg University, Heidelberg, Germany
  6. Christoph Treude — Singapore Management University, Singapore, Singapore
- **arXiv ID:** 2601.20404. **Versions:** v1 — 28 Jan 2026; v2 — 30 Mar 2026 (v2 used throughout).
- **Categories:** cs.SE, cs.AI, cs.ET, cs.HC. **Comments field:** "5 pages, 1 figure, 1 table".
- **Abstract (verbatim; reconstructed from two independent transcription passes — an Atom API fragment chain and an HTML fragment chain; all overlapping text identical word-for-word):**

> "AI coding agents such as Codex and Claude Code are increasingly used to autonomously contribute to software repositories. However, little is known about how repository-level configuration artifacts affect operational efficiency of the agents. In this paper, we study the impact of AGENTS.md files on the runtime and token consumption of AI coding agents operating on GitHub pull requests. We analyze 10 repositories and 124 pull requests, executing agents under two conditions: with and without an AGENTS.md file. We measure wall-clock execution time and token usage during agent execution. Our results show that the presence of AGENTS.md is associated with a lower median runtime (Δ28.64%) and reduced output token consumption (Δ16.58%), while maintaining a comparable task completion behavior. Based on these results, we discuss immediate implications for the configuration and deployment of AI coding agents in practice, and outline a broader research agenda on the role of repository-level instructions in shaping the behavior, efficiency, and integration of AI coding agents in software development workflows."

## 2. Corpus and sampling

- **Source of corpus (§3.1.2):** "We begin from a corpus of repositories sampled in previous work (Mohsenimofidi et al., 2026) that analyzed the adoption of agent instruction files, such as AGENTS.md." Repos in that corpus "may contain (i) multiple instruction files of different names, (ii) multiple copies in different subdirectories, or (iii) only one file at the root."
- **Total corpus:** 132 repositories. Constraint applied: exactly one AGENTS.md at repository root, to "minimize confounding effects from overlapping or conflicting instruction files". Result: "Applying this constraint yields 89 repositories (from 132 total)."
- **Content filter:** taxonomy from Mohsenimofidi et al. 2026 (dimensions include coding conventions and best practices; architecture and project structure; project description; testing instructions; security). Retained only files covering (i) conventions/best practices, (ii) architecture/project structure, (iii) project description. Classification via gpt-oss-120b (Ollama) + manual verification. Result: "After applying this filtering step, we retain 26 repositories, each containing a qualifying root AGENTS.md file."
- **Measured experiment:** "From the 26 repositories, we randomly sample 10 and select up to 15 merged pull requests (PRs) from each." Total: **10 repositories, 124 PRs** (matches abstract). "The cap reflects resource constraints while still enabling coverage across repositories."
- **PR criteria (§3.1.3, verbatim list):** "(1) Size constraint: total additions + deletions ≤ 100 LoC; (2) Scope constraint: ≤ 5 modified files; (3) Status: merged PRs only; (4) Temporal constraint: PR created and merged after the introduction of AGENTS.md in that repository; (5) Change type constraint: PR modifies code files only (excluding documentation and configuration changes)." How many PRs were discarded, and the per-repository distribution of the 124: **unknown — not found in the primary source.**
- **Languages:** **unknown — not found in the primary source** (neither for the 26 nor the 10 repositories).
- **Prior-work citation as given in the paper's References:** "S. Mohsenimofidi, M. Galster, C. Treude, and S. Baltes. Context engineering for ai agents in open-source software. In Proceedings of the 23rd IEEE/ACM International Conference on Mining Software Repositories (MSR 2026)". **No arXiv ID or DOI is given in that entry.** No other Mohsenimofidi-led reference appears.

## 3. Experimental setup

- **Agent/model (§3.1.1):** OpenAI Codex, model `gpt-5.2-codex`: "The agent used in this study is OpenAI Codex." / "At the time of experimentation, the latest available Codex model was gpt-5.2-codex ([4]), which we use consistently across all experiments." Invoked via the Codex CLI through a "lightweight Python wrapper". **Claude Code was NOT used as an experimental agent** (it appears only as motivation in the abstract/intro). No reasoning effort, temperature, or Codex sandbox settings are stated.
- **Conditions (§3.1.6):** paired runs per task — with the repository's root AGENTS.md present, versus "The same snapshot is used, but the AGENTS.md file is removed (all other files unchanged)."
- **Task (§3.1.4):** reconstruct each repo to the state immediately before the selected PR was merged (checkout pre-merge commit; extract the AGENTS.md version at that commit); "The agent is then tasked with recreating the PR's changes from this pre-merge state."
- **Task input (§3.1.5):** a GitHub-issue-style task statement generated per PR by a local LLM (gpt-oss-120b), prompted with the PR diff and repository structure; output has "problem statement, expected behavior, constraints, and acceptance criteria". Same generated input in both conditions. Rationale: "This step standardizes the agent's input format across PRs and reduces variance introduced by incomplete PR metadata."
- **What was measured:** wall-clock execution time (s); tokens split into Input, Cached Input, Output, and Total. Arithmetic identity verified: **Total = Input + Cached Input + Output** (e.g. 353,010.01 + 328,877.31 + 5,744.81 = 687,632.13 exactly; same for the With column: 318,651.51 + 296,078.73 + 4,591.46 = 619,321.70).
- **Repetitions:** paired design — one run per condition per task instance (i.e., 124 × 2 runs). No extra repetitions, no temperature/seeding controls reported. Threat statement acknowledges "agent stochasticity".
- **Environment (§3.1.7):** "experiments were conducted in isolated Docker environments at the repository level"; fresh container per repository; clean-state reset between tasks; "The agent was granted access only to this sandboxed environment and could modify files exclusively within the container."; "No state (e.g., caches, artifacts, or intermediate files) was reused across tasks beyond the version-controlled repository contents, ensuring that every task began from an identical repository snapshot." Artifacts: "The code used to run the experiments, including Dockerfiles, is provided as part of the supplementary material (Lulla et al., 2026)."
- **Experiment dates / total run count:** **unknown — not found in the primary source** (run count 248 is only an inference from the paired design; the paper never states it).

## 4. CRITICAL — Table 1, verbatim

**The paper has exactly ONE table** (arXiv comment "5 pages, 1 figure, 1 table"). Runtime and tokens are all in Table 1; there is no separate runtime-only table. **Figure 1** caption: "Wall-clock time-to-completion distributions for agent runs with and without AGENTS.md."

- **Caption:** "Table 1. Resource Usage With and Without AGENTS.md"
- **Column headers, verbatim (left to right):** `Metric | Without | With | Diff | Δ%`
- **RESOLVED: column 1 = "Without" (no AGENTS.md) = the baseline/reference condition; column 2 = "With" (AGENTS.md present).** `Diff = Without − With`; `Δ% = Diff / Without × 100` (positive Δ% = reduction attributable to AGENTS.md; negative Δ% = increase with the file). **Warning: the caption's word order ("With and Without") does NOT match the column order ("Without", "With"). Do not infer column order from the caption.**
- **Footnote, verbatim:** "∗ Statistically significant difference, Wilcoxon signed-rank test (p<0.05)." (HTML source renders a duplicated MathML/LaTeX artifact; intended "p<0.05".) The ∗ markers appear on the **Wall-Clock Time (s)** rows and the **Output Tokens** rows only.
- **Row labels:** repeated per metric block as "Mean", "Median", "Std Dev".

| Metric (rows: Mean / Median / Std Dev) | Without | With | Diff | Δ% |
|---|---:|---:|---:|---:|
| Wall-Clock Time (s)∗ — Mean | 162.94 | 129.91 | 33.03 | 20.27% |
| Wall-Clock Time (s)∗ — Median | 98.57 | 70.34 | 28.23 | 28.64% |
| Wall-Clock Time (s)∗ — Std Dev | 182.24 | 136.84 | 45.40 | 24.91% |
| Input Tokens — Mean | 353,010.01 | 318,651.51 | 34,358.50 | 9.73% |
| Input Tokens — Median | 116,609.00 | 120,587.00 | −3,978.00 | −3.41% |
| Input Tokens — Std Dev | 654,603.95 | 510,776.51 | 143,827.43 | 21.97% |
| Cached Input Tokens — Mean | 328,877.31 | 296,078.73 | 32,798.58 | 9.97% |
| Cached Input Tokens — Median | 103,424.00 | 104,448.00 | −1,024.00 | −0.99% |
| Cached Input Tokens — Std Dev | 632,622.27 | 494,157.89 | 138,464.38 | 21.89% |
| Output Tokens∗ — Mean | 5,744.81 | 4,591.46 | 1,153.35 | 20.08% |
| Output Tokens∗ — Median | 2,925.00 | 2,440.00 | 485.00 | 16.58% |
| Output Tokens∗ — Std Dev | 6,987.74 | 5,161.67 | 1,826.06 | 26.13% |
| Total Tokens — Mean | 687,632.13 | 619,321.70 | 68,310.43 | 9.93% |
| Total Tokens — Median | 223,707.00 | 226,582.00 | −2,875.00 | −1.29% |
| Total Tokens — Std Dev | 1,293,176.16 | 1,009,338.80 | 283,837.36 | 21.95% |

**Arithmetic verification (all 15 rows; Diff = col1 − col2 checked, Δ% = Diff/col1 checked to printed precision):**
- Every Diff equals Without − With at printed precision, with two 0.01 rounding exceptions: Input Std Dev printed 143,827.43 vs computed 143,827.44; Output Std Dev printed 1,826.06 vs computed 1,826.07. Both are rounding artifacts of unrounded underlying values (percentages match at 2 dp either way).
- Δ% values verified: e.g. 33.03/162.94 = 20.27%; 28.23/98.57 = 28.64%; 68,310.43/687,632.13 = 9.93%; −2,875.00/223,707.00 = −1.29%; 283,837.36/1,293,176.16 = 21.95%.
- **Sign proof against a reversed reading:** if column 1 were "With", the abstract's own claim "lower median runtime (Δ28.64%)" would be false (98.57 > 70.34), the §4 sentence "decreases from 162.94s (without AGENTS.md ...) to 129.91s (with AGENTS.md ...)" would be inverted, and the negative-Diff rows would carry the wrong sign. All three cross-checks confirm: **col1 = Without, col2 = With.**

## 5. Direction of the finding (anchored to verified column order)

With AGENTS.md present, compared to without:
- (a) **Mean total tokens: DECREASE** — 687,632.13 → 619,321.70 (−9.93%).
- (b) **Median total tokens: INCREASE** — 223,707.00 → 226,582.00 (+1.29%). **Mean and median move in OPPOSITE directions.** Same opposition for input tokens (mean −9.73%, median +3.41%) and cached input (mean −9.97%, median +0.99%).
- (c) **Variance: DECREASE everywhere** — Total Std Dev −21.95%; Output Std Dev −26.13%; Input Std Dev −21.97%; Cached Std Dev −21.89%; Wall-clock Std Dev −24.91% (182.24 → 136.84).
- (d) **Median wall-clock runtime: DECREASE** — 98.57s → 70.34s (−28.64%); mean wall-clock −20.27% (162.94s → 129.91s). Here mean and median agree in direction (paper: "The close alignment between mean and median improvements indicates that the reduction is not driven solely by a small number of extreme runs, but reflects a general shift toward faster task completion.").
- (e) **Task completion:** claimed only qualitatively: "maintaining a comparable task completion behavior" (abstract). No rates.
- **The disagreement to flag:** for tokens, the file reduces the MEAN (fat tail shrinks — paper: "the presence of AGENTS.md primarily reduces token usage in a small number of very high-cost runs, rather than uniformly lowering token consumption across all task instances") while slightly RAISING the MEDIAN (typical run costs marginally more). For wall-clock time, both mean and median improve. **Caveat:** the paper's prose discusses means/medians only for output, input, and cached-input tokens; the total-token median increase (223,707 → 226,582) appears in the table **without** a corresponding prose sentence — table-only evidence.

## 6. Task completion comparison

- Abstract only, unquantified: "while maintaining a comparable task completion behavior". **No success-rate, pass-rate, or resolution-rate number appears anywhere in the paper.**
- §3.1.8 sanity check: "Nevertheless, to ensure that the observed efficiency differences are not simply due to agents producing degenerate or trivially incomplete output, we performed a manual sanity check." / "Specifically, we randomly sampled 50 PR tasks and inspected the corresponding agent outputs, comparing them against the human-written merged pull requests, to confirm that they resulted in non-empty, non-trivial code changes consistent with the intended task, rather than aborted runs or random edits."
- §4/§5: "A comprehensive evaluation of the output quality, e.g., the semantic correctness or the functional equivalence to the merged PR, is beyond the scope of this paper. However, it is part of our research roadmap described in Section 5."

## 7. Qualitative claims (verbatim fragments, section numbers)

- **Why the file changes efficiency (§5):** "some of the efficiency gains reported in this paper arise because AGENTS.md files describe repository structure and conventions upfront", "reducing the need for agents to infer project organization through exploratory navigation." Future work proposes execution traces to test whether gains relate to fewer planning iterations, less exploration, or fewer repeated model requests.
- **§4:** "Providing an AGENTS.md file reduces generation cost."
- **§1:** "In practice, developers have begun to introduce agent context files such as AGENTS.md or CLAUDE.md that serve as 'READMEs for agents,' specifying architecture, build commands, coding conventions, and operational constraints (Mohsenimofidi et al., 2026)." Also: "The AGENTS.md format, for example, has been adopted by more than 60,000 repositories to date ([1])."
- **§3.1.1 (why Codex):** "We selected Codex because it is specifically designed for software engineering tasks, supports repository-scale context and tool use, and is representative of production-grade AI coding agents used in practice." Also: "AGENTS.md was first used with Codex before becoming an open format."
- **Long vs short files:** not discussed — **unknown — not found in the primary source**.
- **Files restating the README:** no analysis; the word README appears only in the metaphor "'READMEs for agents.'" (Introduction).
- **Maintenance / staleness:** not discussed — **unknown — not found in the primary source**.
- **When the file hurts:** the paper does not identify conditions where AGENTS.md hurts (only the marginal median-token increase).

## 8. Statistical caveats

- Significance: only one test is mentioned — the Table 1 footnote "∗ Statistically significant difference, Wilcoxon signed-rank test (p<0.05)." applies to wall-clock and output-token rows. **No exact p-values and no confidence intervals are reported.**
- Outliers/mean-vs-median: "The larger reduction in mean output tokens compared to the median suggests that AGENTS.md primarily reduces token usage in a small number of very high-cost runs, rather than uniformly lowering token consumption across all task instances."
- Runtime: "The close alignment between mean and median improvements indicates that the reduction is not driven solely by a small number of extreme runs, but reflects a general shift toward faster task completion."
- Skew context (from table, not prose): std devs exceed means for token metrics (e.g., Total Tokens: mean 687,632.13 vs std dev 1,293,176.16; a ~1.9× ratio), i.e. heavily right-skewed distributions; the paper provides **no formal skewness measure** and does not explicitly discuss this.
- Sample size: 124 PRs / 10 repos; no power or adequacy claim; the 15-PR cap "reflects resource constraints while still enabling coverage across repositories."

## 9. Limitations / threats to validity

No section titled "Limitations" or "Threats to Validity" exists. Relevant content is in §5 Research Roadmap and §3.1.8:
- "Although we control for task, repository state, and agent configuration through a paired design, observed effects may still depend on agent stochasticity, the specific agent framework and model used, and the characteristics of the selected tasks."
- "Replicating the study across additional repositories, larger and more diverse pull requests, and multiple agent systems and model families will help assess the robustness and generality of the observed efficiency effects." (Also proposed: relaxing task-size and scope limits.)
- Correctness scoping: "A comprehensive evaluation of the output quality, e.g., the semantic correctness or the functional equivalence to the merged PR, is beyond the scope of this paper."
- (Close paraphrase, §5, not verbatim): the authors note efficiency metrics alone do not establish correctness, maintainability, or alignment, and propose future correctness/alignment evaluation.

## 10. Evidence log

All fetches succeeded (content returned on every call; the fetch tool does not expose raw HTTP status codes).
- `https://arxiv.org/abs/2601.20404` — fetched once. Yielded: title, author list, abstract fragment, v1/v2 dates (28 Jan 2026 / 30 Mar 2026), categories, "5 pages, 1 figure, 1 table".
- `https://arxiv.org/html/2601.20404v2` — fetched repeatedly (about 20 passes with different extraction queries). Yielded: Table 1 in full (three independent header-row transcriptions agreeing on `Metric | Without | With | Diff | Δ%`), footnote, caption, Figure 1 caption; §1 Introduction; §2 Background; §3.1.1–§3.1.8 (agent, model, corpus, criteria, environment, sanity check); §4 Results narrative; §5 Research Roadmap; author affiliations; References entry for Mohsenimofidi et al.
- `https://export.arxiv.org/api/query?id_list=2601.20404` — fetched once. Yielded: arXiv Atom metadata, including the abstract fragment chain.

## 11. UNVERIFIED / UNKNOWN

- Experiment dates / calendar window: unknown — not found in the primary source.
- Total number of agent executions: unknown — not stated (248 paired runs is inference from design, not a paper statement).
- Programming languages of the repositories: unknown — not found in the primary source.
- Per-repository distribution of the 124 PRs and how many PRs were discarded by the criteria: unknown — not found in the primary source.
- Prose discussion of the total-token median (223,707 → 226,582): unknown — table-only; §4 prose covers output, input, and cached-input tokens but not the total-token median rise.
- Exact p-values / confidence intervals: unknown — not reported (p<0.05 threshold only).
- Task success rates: none reported; "comparable task completion behavior" is never quantified.
- Numerical content of Figure 1 (distribution plot): not extracted (caption only).
- arXiv ID/DOI for Mohsenimofidi et al. 2026: none given in the paper's reference entry (MSR 2026 proceedings citation only).
- Whether v1 (28 Jan 2026) differs numerically from v2: not checked (v2 used throughout).
- Minor: the Mohsenimofidi reference title's exact capitalization as printed ("Context engineering for ai agents in open-source software") — possible fetch normalization; flag for anyone quoting the reference verbatim.

**Most important caveat for citing:** the caption "Table 1. Resource Usage With and Without AGENTS.md" lists "With" first in prose while the columns are "Without | With" — cite the columns by their header labels, and remember positive Δ% = reduction with the file, negative Δ% = increase with the file (only the three median token rows are negative).
