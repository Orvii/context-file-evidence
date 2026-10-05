# Primary-source extraction — "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"

Extraction note: produced by a read-only research pass using ~20 targeted fetches across v1, v2 and v3 of arXiv:2602.11988. Every headline number below is version-tagged, because the numbers changed between versions. Items absent from the primary source are recorded as absent rather than filled from secondary coverage.

## 0. READ FIRST — version drift changes headline numbers

arXiv:2602.11988 has THREE versions and the benchmark was renamed mid-life. Numbers widely quoted in secondary coverage (AGENTbench, 4%/3%, "22%/14%/14%/10%") match **v1 only**. The current arXiv version is **v3**, which uses a different benchmark name and different headline percentages. Cite with an explicit version or the numbers will be wrong.

| Item | v1 (12 Feb 2026) | v2 (23 Jun 2026) | v3 (29 Sep 2026, current) |
|---|---|---|---|
| Benchmark name | **AGENTbench** | **CTXbench** | **CTXbench** |
| Author 2 | Niels Mündler | — | Niels Mündler-Sasahara |
| Author 3 | Mark Müller | — | Mark Niklas Müller |
| Dev-vs-None intro claim | "+4% on average" | — | "2.4% on average (p=21%)"; dev-vs-LLM "7% on average" |
| Reasoning tokens, GPT-5.1 mini, SWE-bench | 14% | 10% | 10% |
| Tables | 3 tables | — | 8 tables (adds significance tests, success rates, category + description ablations) |
| Condition label | None / LLM / Human ("Hum." in table) | — | None / LLM / Dev |

InfoQ coverage (Mar 2026) quotes the v1 numbers (3%, 4%, over 20%, up to 19%). Any citation of the InfoQ-era findings is a citation of **v1**.

## 1. Citation block

- **Title (as printed):** "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"
- **Authors (v1 as printed):** "Thibaud Gloaguen" (Department of Computer Science, ETH Zurich); "Niels Mündler" (ETH Zurich); "Mark Müller" (LogicStar.ai); "Veselin Raychev" (LogicStar.ai); "Martin Vechev" (ETH Zurich).
- **Authors (v3 as printed):** Thibaud Gloaguen (ETH Zurich), Niels Mündler-Sasahara (ETH Zurich), Mark Niklas Müller (LogicStar.ai), Veselin Raychev, Martin Vechev. (v3 fetch confirmed the first three affiliations; Raychev's LogicStar.ai affiliation confirmed in v1 only.)
- **arXiv ID:** 2602.11988. **Versions:** v1 "Thu, 12 Feb 2026 14:15:22 UTC"; v2 "Tue, 23 Jun 2026 20:26:50 UTC"; v3 "Tue, 29 Sep 2026 14:58:01 UTC" ("last revised 29 Sep 2026 (this version, v3)").
- **Categories:** cs.SE; cs.AI.

**Abstract v1** (reassembled from consecutive verbatim fragments): "A widespread practice in software development is to tailor coding agents to repositories using context files, such as AGENTS.md, by either manually or automatically generating them. Although this practice is strongly encouraged by agent developers, there is currently no rigorous investigation into whether such context files are actually effective for real-world tasks. In this work, we study this question and evaluate coding agents' task completion performance in two complementary settings: established SWE-bench tasks from popular repositories, with LLM-generated context files following agent-developer recommendations, and a novel collection of issues from repositories containing developer-committed context files. Across multiple coding agents and LLMs, we find that context files tend to reduce task success rates compared to providing no repository context, while also increasing inference cost by over 20%. Behaviorally, both LLM-generated and developer-provided context files encourage broader exploration (e.g., more thorough testing and file traversal), and coding agents tend to respect their instructions. Ultimately, we conclude that unnecessary requirements from context files make tasks harder, and human-written context files should describe only minimal requirements."

**Abstract v3** (reassembled from consecutive verbatim fragments): "A widespread practice in software development is to tailor coding agents to repositories using context files, such as AGENTS.md. Although this practice is strongly encouraged by agent developers, there is currently no rigorous investigation into whether such context files are actually effective for real-world tasks. In this work, we study this question and evaluate coding agents' task completion performance in two complementary settings: established SWE-bench tasks from popular repositories, with LLM-generated context files, and a novel collection of issues from repositories containing developer-committed context files. Surprisingly, we find that providing context files does not generally improve task success rates, while increasing inference cost by over 20% on average. Specifically, we find that while instructions in the context files are well followed by coding agents, repository overviews, although popular and recommended by model providers, are not helpful. We conclude that while context files are useful for specifying non-standard coding practices, any attempts to improve performance should be rigorously evaluated before deployment."

## 2. BENCHMARK NAME — RESOLVED

- **v1 body:** "AGENTbench" throughout (abstract via "novel collection", §1 "we construct a novel benchmark, AGENTbench, comprising 138 unique instances", §3.2, §6 conclusion, Table 1 caption). Table 2 row label renders as "Agent-bench" (line-break artifact). "AGENT-Bench", "AGENTBENCH", "CTXbench" do not appear in v1 (explicitly checked).
- **v2/v3 body:** "CTXbench" (abstract, intro, conclusion). Tables render "CTX-Bench" ("CTX- Bench" in Table 2 layout). Appendix A Table 5 row label prints **"Plan-Bench"** — reproduced identically in two independent fetches — while its caption says "per SWE-bench and CTXbench". Observed inconsistency in the v3 paper/HTML; likely a paper-side typo. Flag it if quoting Table 5.
- **"CTXBENCH" all-caps: NOT FOUND anywhere in v1, v2, or v3** (explicitly asked each). Secondary sources use that spelling; the paper does not.
- **Authoritative name:** v1 = **AGENTbench**; v2/v3 = **CTXbench**. There is no version-independent name.

## 3. Benchmark construction (v1 §3.2; unchanged in v3)

- Five stages (verbatim names): "Finding repositories", "Filtering pull requests", "Environment Set-Up", "Task Descriptions", "Generating Unit Tests".
- Repo criteria: "we select codebases that contain a context file such as AGENTS.md or CLAUDE.md at the root directory", "using Python as the main language and featuring a test suite", "requiring at least 400 PRs". `.cursorrules` is not named in the criteria.
- PR criteria: "reference at least one issue", "modify at least one Python file", LLM-assessed "deterministic, testable behaviors". Unit-test edits not required.
- Env setup: agent-produced script; instances kept if at least one test passes.
- Task descriptions: LLM-generated "based on the PR description, associated issues if available, and the original patch"; random 10% inspected, "found that none of them leaked the solution".
- Unit tests: must "fail on R and pass on R∘X*".
- Counts: "138 instances from a total of 5694 PRs from 12 repositories", "12 repositories, each containing context files." Repos were required to have committed root context files (yes).
- SWE-bench Lite (v1/v3 §4.1): "300 tasks sourced from GitHub issues across 11 popular Python repositories", "none containing developer-written context files." (Note: official SWE-bench Lite is commonly described as 300 tasks / 12 repos; the paper says 11.)

## 4. Experimental setup (§4.1)

- Agents + models: "Claude Code with Sonnet-4.5"; "Codex with GPT-5.2 and GPT-5.1 mini"; "Qwen Code with Qwen3-30b-coder". Four agents total.
- Benchmarks: SWE-bench Lite and the paper's own benchmark (AGENTbench in v1 / CTXbench in v2+).
- Conditions: v1 None/LLM/Human — None: "No context files are available, i.e., we remove developer-provided files for AGENTbench."; LLM: "An LLM-generated context file is available."; Human: "A developer-provided context file is available." using "the context file of the pre-patch repository state R", "Only available for AGENTbench." v3 renames Human→Dev ("i.e., we remove developer-provided files for CTXbench.").
- Generation of LLM files: "We use the recommended initialization command and model for each agent individually to generate the context file", using "the pre-patch repository state R." Command names/prompt text are not in §4.1 (prompts are in Appendix B).
- Steps definition: "Each step is one interaction with the environment, e.g., calling a shell tool or modifying a file."
- Sampling: "We sample completions for each agent once." — one completion per task per agent, no repeated sampling reported.

## 5. Headline results

### 5a. v1 prose percentages (§4.2, §4.3)

- LLM files, resolution: "In more detail, the average resolution rate is reduced by 0.5% and 2% on average on SWE-bench Lite and AGENTbench, respectively."
- Steps/cost: "Meanwhile, the context files increase the # steps in every setting on average by 2.45 and 3.92 steps, respectively, which leads to a cost increase of 20% and 23% on average, respectively (see Table 2)."
- Dev files: "However, developer-provided context files also increase the average number of steps and costs required to solve the task, on average by 3.34 steps and at most 19%, respectively." Plus: "developer-provided context files outperform the LLM-generated ones for all four agents" and "improve the performance compared to no context files for all agents but Claude Code".
- Intro: "developer-provided files only marginally improve performance compared to omitting them entirely (an increase of 4% on average)"; "LLM-generated context files have a small negative effect (a decrease of 3% on average)."
- Reasoning tokens — **v1 verbatim**: "LLM-generated context files indeed increase the average number of reasoning tokens by 22% for GPT-5.2 and 14% for GPT-5.1 mini on SWE-bench Lite (respectively 14% and 10% on AGENTbench)". Then: "developer-written context files increase the number of reasoning tokens by 20% and 2% for GPT-5.2 and GPT-5.1 mini, respectively." The dev 20%/2% sentence does NOT state a benchmark; since the Human condition exists only on AGENTbench, it is implicitly AGENTbench.

### 5b. v3 prose percentages (§4.2, §4.3)

- Steps: "they increase the # steps in every setting, on average by 2.45 and 3.92, respectively"; "leading to a significant (p-value < 0.001%) cost increase of 20% and 23% on average, respectively". Steps/cost deltas and significance corroborated by Table 6.
- Dev: "Developer-provided context files improve agent performance by 2.4% on average (p=21%)", "significantly outperforming LLM-generated ones (p=3.8%)" (corroborated by Table 3: None vs Dev p=0.21; LLM vs Dev p=0.038). Intro: "However, developer-committed files outperform LLM-generated ones by a significant margin of 7% on average."
- Dev steps/cost: "However, developer-provided context files also increase the average number of steps and the cost, on average by 3.34 steps and at most 19%, respectively."
- Reasoning tokens (v3, verbatim): "LLM-generated context files increase the average number of reasoning tokens by 22% for GPT-5.2 and 10% for GPT-5.1 mini on SWE-bench (respectively 14% and 10% on CTXbench), and developer-provided context files increase it by 20% for GPT-5.2 and 2% for GPT-5.1 mini." **Change vs v1: GPT-5.1 mini on SWE-bench is 10%, not 14%.**
- No "4%" appears anywhere in the v3 intro (explicitly checked); v3 uses 2.4% and 7%.

### 5c. v1 Table 1

Caption verbatim: "Average, minimum, and maximum of key statistics of AGENTbench across the 138 instances. For context files, a section is the content between Markdown headers." Headers: Statistic | Mean | Min | Max.

Rows: PR body # words 415.3 / 5 / 4961 · Issue I # words 211.6 / 96 / 500 · Codebase # files 3337 / 151 / 26602 · PR patch # lines edited 118.9 / 12 / 1973 · # files edited 2.5 / 1 / 23 · Test Coverage 75% / 2.5% / 100% · Context file # words 641.0 / 24 / 2003 · # sections 9.7 / 1 / 29.

(v3 Table 1: identical numbers, caption says "CTXbench".)

### 5d. v1 Table 2 (steps and cost)

Caption verbatim: "The average number of steps (lower is better) and execution cost (in USD — lower is better) per SWE-bench Lite and AGENTbench instance without context files (None), with LLM-generated context files (LLM), and with developer-written context files (Hum). We bold the best setting." Headers: Type | Sonnet-4.5 (Steps, Cost) | GPT-5.2 (Steps, Cost) | GPT-5.1 M. (Steps, Cost) | Qwen3-30B (Steps, Cost). No Δ column; no stated sign convention.

| Type | Setting | Sonnet-4.5 | GPT-5.2 | GPT-5.1 M. | Qwen3-30B |
|---|---|---|---|---|---|
| SWE-Bench Lite | None | 54.4 steps, $1.30 | 12.5, $0.32 | 40.9, $0.18 | 29.7, $0.12 |
| SWE-Bench Lite | LLM | 57.2, $1.51 | 12.7, $0.43 | 45.2, $0.22 | 32.2, $0.13 |
| Agent-bench | None | 40.7, $1.15 | 12.1, $0.38 | 40.6, $0.18 | 31.5, $0.13 |
| Agent-bench | LLM | 46.5, $1.33 | 13.1, $0.57 | 46.9, $0.20 | 34.2, $0.15 |
| Agent-bench | Hum. | 45.3, $1.30 | 13.6, $0.54 | 46.6, $0.19 | 32.8, $0.15 |

**v3 Table 2: identical point estimates, plus standard errors** (caption "(in USD, lower is better)... developer-context files (Dev.)"): SWE-Bench None 54.4±2.2 / $1.30±0.07 | 12.5±0.8 / $0.32±0.05 | 40.9±4.2 / $0.18±0.03 | 29.7±1.9 / $0.12±0.01 · SWE-Bench LLM 57.2±2.3 / $1.51±0.08 | 12.7±0.8 / $0.43±0.05 | 45.2±4.2 / $0.22±0.03 | 32.2±1.9 / $0.13±0.01 · CTX-Bench None 40.7±3.0 / $1.15±0.10 | 12.1±1.6 / $0.38±0.11 | 40.6±6.7 / $0.18±0.05 | 31.5±3.1 / $0.13±0.02 · CTX-Bench LLM 46.5±3.9 / $1.33±0.14 | 13.1±1.5 / $0.57±0.18 | 46.9±6.4 / $0.20±0.04 | 34.2±3.4 / $0.15±0.02 · CTX-Bench Dev. 45.3±3.6 / $1.30±0.13 | 13.6±1.7 / $0.54±0.23 | 46.6±7.1 / $0.19±0.04 | 32.8±3.7 / $0.15±0.03.

### 5e. v1 Table 3 (= v3 Table 4)

Caption: "Equivalence classes used to group the different tool calls."
Edit → sed → "sed, edit" · Write → apply_patch → write_file · Grep → "grep, rg" → grep · Read → cat → "cat, read_file, search_file_content" · TodoWrite → update_plan → todo_write.

### 5f. v3-only tables

**Table 3** — "Two-sided Cochran-Mantel-Haenszel test comparing the effect of different context files on the resolution rate. The null hypothesis is that resolution rates are equal. We bold significant p-values." SWE-bench None vs LLM 0.87 · CTXbench None vs LLM 0.37 · CTXbench None vs Dev 0.21 · CTXbench LLM vs Dev **0.038**.

**Table 5** — "The success rate (in %) plus or minus the standard error per SWE-bench and CTXbench. We bold the best setting." Columns Sonnet-4.5 / GPT-5.2 / GPT-5.1 M. / Qwen3-30B. Row labels as printed: SWE-Bench None 59.9±3.0 / 56.6±2.9 / 47.7±3.1 / 31.1±2.7; SWE-Bench LLM 58.7±2.9 / 54.4±2.9 / 47.6±3.2 / 32.4±2.7; **Plan-Bench** (sic — a paper-side label inconsistency, see §2) None 73.2±3.8 / 65.2±4.1 / 54.3±4.3 / 45.7±4.3; Plan-Bench LLM 65.2±4.1 / 68.1±4.0 / 50.7±4.3 / 47.1±4.3; Plan-Bench Dev. 70.3±3.9 / 68.1±4.0 / 55.8±4.2 / 53.6±4.3.

**Table 6** — "Stratified permutation tests comparing the effect of different context files on cost and number of steps..." SWE-bench Steps None vs LLM p=0.0287 (significant) · SWE-bench Cost None vs LLM p<0.00001 · CTXbench Steps None vs LLM p=0.00004 · CTXbench Steps None vs Human p=0.00002 · CTXbench Cost None vs LLM p=0.00064 · CTXbench Cost None vs Human p=0.0126. (Row label "Human" as transcribed once; the v3 body otherwise says Dev.)

**Table 7** — "Ablating common categories from LLM-generated context files does not significantly improve accuracy on either benchmark. For accuracy, p-values are computed with McNemar's test against the full context file condition; for cost, p-values are computed with a permutation test."
CTXbench Accuracy 68.12% / without testing 66.67% (p=0.80) / without overview 62.32% (p=0.15) / without tooling 63.77% (p=0.31) · CTXbench Cost $0.4715 / $0.3730 (p=0.023) / $0.4027 (p=0.24) / $0.4815 (p=0.97) · SWE-bench Accuracy 54.36% / 57.72% (p=0.099) / 54.20% (p=0.73) / 53.69% (p=0.85) · SWE-bench Cost $0.3272 / $0.2756 (p=0.0035) / $0.3018 (p=0.10) / $0.2715 (p=0.0012).

**Table 8** — "Resolution rate on SWE-bench for different models with either LLM-generated or original issue descriptions, under two context-file settings: no context files (None) and LLM-generated context files (LLM). Values in parentheses indicate the change relative to the corresponding no-context setting."
GPT-5.2, LLM-generated Desc.: 70.8% → 66.8% (-4%) · GPT-5.2, Original Desc.: 57.0% → 54.9% (-2%) · Qwen3-30B, LLM-generated Desc.: 46.9% → 44.9% (-2%) · Qwen3-30B, Original Desc.: 30.3% → 32.4% (+2%).

## 6. Qualitative findings (verbatim)

- Instruction following: v1 §4.3 "We find that agents generally follow instructions present in the context files."; v1 abstract "coding agents tend to respect their instructions."; v3 "instructions in context files are well followed". **The phrase "almost to a fault" does NOT appear in v1, v2, v3, or the InfoQ piece** (explicitly searched). Do not attribute that phrasing to the paper.
- Key causal sentence, v1 §4.3: "This effect is observable across almost all measured tools displayed in Figure 6, as we show in a more in-depth analysis in Appendix A. In particular, this result implies that the absence of improvements with context files is not due to a lack of instruction-following." (v3: "...not due to a lack of instruction-following capabilities.")
- Tool use: "when context files are present, the coding agents run more tests."; "They also tend to navigate the repository more: they search more files (grep), read more files, and write more files."; "adding context files causes agents to use more repository-specific tooling". Numbers: "uv is used 1.6 times per instance on average when mentioned in the context files, compared to fewer than 0.01 times when it is not mentioned, and repository-specific tools are used 2.5 times per instance on average when mentioned, compared to fewer than 0.05 times when they are not mentioned."
- Steps increase: v1 §6 "We find that all context files consistently increase the number of steps required to complete tasks."; v1 §1 "context files lead to increased exploration, testing, and reasoning by coding agents"; "as a result, increase costs by over 20%." v3 §6: "We find that all context files consistently increase the cost and number of steps required to complete tasks."
- Repository overviews: v1 §4.2 "We conclude that context files, even developer-provided ones, are not effective at providing a repository overview." (v3 §4.3 drops "even developer-provided ones".)
- Redundancy: v1 §4.2 as fetched: "LLM-generated context files are highly redundant with existing documentation". One v3 fetch attributed "LLM-generated context files are mostly redundant with existing documentation" and "developer-provided context files add additional information" to Appendix B — **the wording ("highly" vs "mostly") and section differ between fetches; verify before quoting**.
- Intrinsic harm: v1 abstract "unnecessary requirements from context files make tasks harder"; "human-written context files should describe only minimal requirements." v3: "Human-written context files should only include instructions required for coding agents that are not already present in the README (e.g., specific conventions or non-functional requirements), and be rigorously evaluated before adoption."
- Verification-beats-instruction: no such claim found in the paper (see §10). This phrasing comes from secondary commentary.

## 7. Ablations

- Generator model (§4.4, both versions): GPT-5.2+Codex-generated files vs each agent's own files — v1 "This improves performance on SWE-bench Lite across all models (2% on average), but degrades performance on AGENTbench across all models (3% on average)." v3 carries the same numbers with the SWE-bench/CTXbench names. Heading-like line: "Stronger models don't generate better context files".
- Generation prompt (§4.4): "No difference between the specific prompts"; "neither the prompt that matches the underlying agent nor a specific prompt performs consistently best" (v3). Details: Claude Code did better with the Codex prompt; GPT-5.2 and GPT-5.1 mini did better on SWE-bench but worse on CTXbench with it.
- Category ablation (v3 Table 7 only): removing testing/overview/tooling sections never significantly improves accuracy; removing testing significantly cuts cost (CTXbench p=0.023; SWE-bench p=0.0035); removing tooling cuts SWE-bench cost (p=0.0012).
- Issue-description ablation (v3 Table 8): LLM-rewritten issue descriptions raise accuracy in the no-context setting, but context files still reduce it (-4% GPT-5.2, -2% Qwen); with original descriptions, Qwen +2%.
- No ablation was found varying file length or section count (see §10).
- Documentation-removal ablation — **percentage recovered from the PDF: 2.7%.** The authors manually remove all documentation (files ending `.md`, example code, and the contents of `docs/`) after generating the context file and before evaluating, to test the redundancy hypothesis. v3 verbatim (Appendix B, "Context files are redundant documentation", PDF p. 16): "In this setting, where context files are the only source of documentation available, we find that LLM-generated context files not only consistently improve performance by 2.7% on average, but also out[perform developer-provided ones]". Figure 12 caption: "When removing all documentation-related files from the codebase, LLM-generated context files tend to outperform developer-provided (Human) ones on CTX BENCH." Claude Code excluded "for cost reasons" (v1 wording, typo intact: "due to its hight cost"); Figure 12 shows only GPT-5.2, GPT-5.1 Mini, Qwen3-30B.
- **Location correction:** in v3 this ablation lives in **Appendix B / Figure 12**, not §4.2/Figure 5 — that numbering is v1's (§4.3 "Trace analysis", Figure 5, dataset "AGENT BENCH"). The v1 percentage is the same 2.7%.
- **Why HTML extraction dropped the number:** arXiv HTML v3 carries the value inside MathML (`<math alttext="2.7"><mn>2.7</mn>…`), so naive HTML-to-text scraping loses it while the number is present in the HTML source. Any future extraction of arXiv HTML must parse MathML, not strip tags.
- Figure 12 has **no data labels**: per-agent success-rate values for this ablation exist nowhere in the PDF text (bar plot only, y-axis 30–70). The 2.7% average is the only number.

## 8. Limitations / threats to validity (Section 5, both versions)

- Languages: v1 "The current evaluation is focused heavily on Python." v3 "The current evaluation is focused on Python." Plus: "Since this is a language that is widely represented in the training data, detailed knowledge about tooling, dependencies, and other repository specifics might be present in the models' parametric knowledge, nullifying the effect of context files." Future work: "more niche programming languages and toolchains that are less represented in the training data".
- Scope: "we evaluate the impact of context files on task resolution rate" — code efficiency and security are future work.
- Generation: "human developers appear to dominate per our evaluation" (v1); improving automatic generation is future work; "Our work may serve as a baseline for how to rigorously evaluate automatically generated context files."
- **Nothing on sample size, determinism, or agent/model version drift was found in the limitations section.** The only determinism-adjacent statement is §4.1: "We sample completions for each agent once."

## 9. Evidence log

All fetches returned usable content; the fetch tool does not expose HTTP status codes.

1. https://arxiv.org/abs/2602.11988 — 3 fetches. Title, authors, version history (v1/v2/v3 dates), categories, v3 abstract excerpt.
2. https://arxiv.org/abs/2602.11988v3 — 1 fetch. Old-style abs page; author list; abstract paraphrase.
3. https://arxiv.org/html/2602.11988v1 — 8 fetches with distinct queries. Full v1: abstract fragments, §1 intro numbers, §3.2 construction, §4.1 setup, §4.2/§4.3 percentages, §4.4 ablations, §5 limitations, §6 conclusion, Tables 1–3.
4. https://arxiv.org/html/2602.11988v2 — 1 fetch. Benchmark renamed to CTXbench; reasoning-token sentence (10%/10%).
5. https://arxiv.org/html/2602.11988v3 — 6 fetches. Author line, conditions, Tables 1–8, §4.2/§4.3/§4.4, §5, §6, abstract fragments.
6. https://www.infoq.com/news/2026/03/agents-context-file-value-review — SECONDARY only. Says AGENTbench; 3% drop / 4% gain / over 20% cost / up to 19%; matches v1. Note: it calls the Claude model "Claude 3.5 Sonnet" while the paper says "Sonnet-4.5" — a secondary error; do not cite from it.
7. https://www.alphaxiv.org/abs/2602.11988 — SECONDARY only. Abstract paraphrase; named no benchmark.

## 10. UNVERIFIED / ABSENT FROM THE PRIMARY SOURCE

- "agents follow instructions almost to a fault" — **not found** in v1, v2, or v3, nor in InfoQ. Closest primary phrasings: "coding agents tend to respect their instructions" (abstract), "agents generally follow instructions present in the context files" (§4.3), "instructions in context files are well followed". Attribute only these.
- "CTXBENCH" all-caps — not found in any primary version; secondary-source spelling only.
- Reproducibility / sample-size / determinism limitation — not found beyond "We sample completions for each agent once."
- Version-drift discussion — not found in the paper.
- "Verification beats instruction" — not found in the primary source. It is secondary commentary (blog-level), not a paper finding.
- File-length ablation — not found; only Table 1's descriptive word-count statistics (641.0 mean words, 24–2003 range) exist.
- v3 Table 5's "Plan-Bench" label and Table 6's "Human" label — reproduced identically across fetches; likely paper-side typos; verified only as printed text, not semantically.
- The dev-files 20%/2% reasoning-token attribution to AGENTbench (v1) is inferred from the Human condition existing only there; the sentence itself does not name the benchmark.
- v1 Table 2 error bars — the v1 transcription showed no ± values; v3 shows them. Unconfirmed whether v1 prints them.
- The "highly redundant" vs "mostly redundant" wording discrepancy (§6) — one of the two fetch results is misattributed; the exact sentence and section are unverified.
- The percentage in the documentation-removal ablation — **resolved 2026-10-05 via the PDF: 2.7%** (Appendix B/Figure 12 in v3). Per-agent values for that figure remain unavailable (no data labels).

## Five most important verified facts

1. Three versions exist and differ: v1 uses AGENTbench, v3 (current) renames it CTXbench and changed the GPT-5.1 mini SWE-bench reasoning-token increase from 14% to 10%, plus the dev gain from 4% to 2.4% (p=21%) with "7% on average" versus LLM.
2. "CTXBENCH" appears nowhere in the paper.
3. The widely quoted v1 headline numbers are exactly: 22%/14% (SWE-bench Lite) and 14%/10% (their benchmark) reasoning-token increases for GPT-5.2/GPT-5.1 mini, 20%/2% for developer files, cost +20%/+23%, steps +2.45/+3.92, dev steps +3.34 and cost up to +19%.
4. The benchmark is 138 instances drawn from 5,694 PRs across 12 repositories, built by a five-stage pipeline, restricted to Python repos with a root AGENTS.md/CLAUDE.md, a test suite, and ≥400 PRs.
5. Agents tested: Claude Code + Sonnet-4.5, Codex + GPT-5.2 and GPT-5.1 mini, Qwen Code + Qwen3-30b-coder; one completion sampled per task per agent.
