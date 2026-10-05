# Two-Agent Ablation — Experimental Report (context-files-coding-agents)

> **Study type: EXPERIMENT.** Controlled ablation on real tasks measuring agent correctness and efficiency. This is the source for "does it help" claims.

## 1. Citation

- **Title:** "Do Context Files Help Coding Agents? A Two-Agent Ablation Study on Real Repositories" (arXiv title confirmed); repo subtitle/title: "Do Context Files Help Coding Agents?".
- **Venue:** "Submitted to REALM @ EMNLP 2026 workshop; under review." (repo paper/README.md; main README states "REALM @ EMNLP 2026; under review"). arXiv abs page shows no comments/venue note.
- **Author:** Prakhar Khatri (sole author, per arXiv page). Repo owner: `codeprakhar25`. No maintainer otherwise listed.
- **Repos:** https://github.com/codeprakhar25/context-files-coding-agents (MIT). Preprint: https://arxiv.org/abs/2607.27250, submitted 28 July 2026, cs.SE + cs.AI, v1 only.

## 2. Design

- **Agents and models (exact):** "Claude Code (claude-sonnet-4-6, Anthropic)." and "Codex CLI (gpt-5.5, OpenAI, ChatGPT-plan auth)." No CLI version numbers are stated anywhere found. Invocations: `claude --print --bare --output-format stream-json`; `codex exec --json`.
- **Repositories:** OpShin/opshin, firebase/firebase-admin-python, pdm-project/pdm.
- **Tasks:** Claude Code 15 tasks; Codex 17 tasks — abstract: "17 real tasks from 3 repositories (15 shared + 2 Codex-only)". Task IDs seen: opshin 510/554/593/595/598/605/610/616, firebase 907.
- **Repeats:** 3 per task and condition ("3 per task and condition", README; "15/17 tasks with 3 repeats", paper limitations).
- **Runs:** abstract: "288 evaluated runs with gold-test evaluation" (15×9 + 17×9 = 288). README labels the shipped database "291-run ablation" (experiment_full.db) and key_numbers.md cell n's sum to 291 (Claude 47+46+45 = 138; Codex 51×51×51 = 153). Discrepancy 288 vs 291 is not explained in any file read; key_numbers.md states run counts 288/290/291 are "not stated". Flag when citing.
- **Evaluation:** "Tier-C gold-test evaluation"; pass requires all gold PR tests to pass with zero failures or errors (README, near-verbatim). CSV `eval_method` column also contains `line_overlap` (secondary; not used for any figure here).
- **Strategies, verbatim (paper text):**
  - `none`: "The AGENTS.md file is removed from the workspace." / "No repository context is provided in the system prompt or accessible to the agent." / "The agent works from the codebase alone."
  - `always_on`: "The full AGENTS.md content is injected into the system prompt every turn," / "preceded by a framing sentence ('The following is the repository's AGENTS.md guide…')." / "The file is removed from the workspace to prevent double-reading."
  - `selective`: "Topic-organized wiki files (e.g., wiki/architecture.md, wiki/error-handling.md) are placed in the workspace," / "and a system-prompt hint tells the agent to consult wiki/*.md;" / "the agent retrieves relevant files on demand via its Read tool."
- README shorthand: none "strip AGENTS.md/CLAUDE.md from the workspace; no system-prompt context."; always_on "inject the full context file into the system prompt."; selective "split the file into a wiki and give the agent a retrieval hint."

## 3. Correctness results (verbatim; column order confirmed none / always_on / selective)

| Agent | none | always_on | selective |
|---|---:|---:|---:|
| Claude Code (15 tasks) | 53.3% (24/45) | 55.6% (25/45) | 55.6% (25/45) |
| Codex (17 tasks) | 58.8% (30/51) | 56.9% (29/51) | 52.9% (27/51) |

From key_numbers.md (experiment_full.db): claude_code "none 24/45 = 53.3%; always_on 25/45 = 55.6%; selective 25/45 = 55.6%"; codex "none 30/51 = 58.8%; always_on 29/51 = 56.9%; selective 27/51 = 52.9%". Statistical unit is the task; repeats are averaged for task-level analyses. Headline framing: "Headline finding — a correctness null, replicated across both agents."

## 4. Statistics (verbatim with provenance)

- "task-clustered bootstrap (10k) on paired strategy differences" (README lists "Wilson CIs, task-clustered bootstrap (10k), sign-flip permutation, within-task omnibus permutation, TOST equivalence, Monte-Carlo power").
- Omnibus: "The omnibus permutation test shows no detectable strategy effect (p=1.00 Claude; p=0.66 Codex)."
- TOST: "bounds every pairwise strategy difference to ≤10pp for Claude and ≤15pp for Codex" — with the honesty caveat "not a powered equivalence claim given n=15–17 clusters." Abstract: "Context strategy does not measurably move correctness on either agent (bounded to ≤10–15pp via equivalence testing)."
- TOST bootstrap CIs (key_numbers.md, source power_analysis.py), Claude paired differences: always−none [−4.4,+8.9]pp; sel−none [+0.0,+6.7]pp; sel−always [−6.7,+6.7]pp — "All within ±10pp."
- Power: "MDE at n=17, reps=3: even a large Δ=30pp effect is caught only 57% of the time"; "Detecting Δ=10pp at 80% power requires ∼120–200 tasks."; "a 10pp effect is undetectable." README states the same more loosely: "~120 tasks" and "the minimum detectable effect is >30pp". (Cite the paper's "∼120–200 tasks" range and README's "~120 tasks" as stated — they differ.)
- Power-limited honesty: README TL;DR: "The result is power-limited, and we say so" (excerpt).
- **Wilson CIs:** listed as an analysis in README but **no numeric Wilson intervals found** in README, paper HTML passes, or key_numbers.md ("Other bootstrap intervals: not stated"; one paper-text pass reported the results table "gives no Wilson 95% confidence intervals"). Numeric Wilson CIs: UNVERIFIED — not found.
- Agent-specific difficulty: "borderline task difficulty is agent-specific (Spearman ρ=0.75)" (abstract; key_numbers: rho 0.75, p=0.001, Pearson r=0.77, n=15 shared tasks; exactly-one-agent-borderline 6/15).

## 5. Efficiency finding (OpShin)

- "the number of _blind full-suite_ runs per cell falls monotonically none 3.67→always_on 2.44→selective 1.67"
- "Claude's within-task wall-clock time is ∼24% lower under context (none 2689s vs. always_on 2066s vs. selective 2032s; faster-with-context on 4/5 tasks" … "sign-flip p=0.125, underpowered at n=5"
- "the effect appears only for Claude (Codex duration is flat) and only on opshin"
- "It is a _process_ effect (how the agent works), not an _outcome_ effect (correctness, still null)." / README: "The takeaway is *process, not pass-rate*."
- Cause: "because the `AGENTS.md` warns the suite is slow and nudges the agent toward targeted tests." (README)
- Per-task within-task durations (key_numbers.md, opshin): 595: none 2243s / always 1588s / sel 1193s; 598: 2377/1332/1637; 605: 2872/2743/3031; 610: 3108/2831/2852; 616: 2759/1838/1447; "Mean Δ: +623s; faster with context on 4/5 tasks"; opshin marginal none 2689s / always_on 2066s / selective 2032s; full-suite-count subset (595/605/610/616): fewer with context on 3/4 tasks, "exact sign-flip p=0.250, n=4", "Marked exploratory post-hoc mechanism".

## 6. Manipulation-validity probe

- Setup: "we re-ran the two convention-closest near-misses (opshin 554, firebase 907) under all three strategies, 3 repeats, on both agents (36 cells)".
- Quality rubric: "on this rubric _firebase_ rates 'Excellent,' _pdm_ and _opshin_ 'Good'".
- Result quotes: "The real AGENTS.md never converts a failure to a pass on either agent"; "The real AGENTS.md never rescues a near-miss"; "The manipulation is not inert (it can perturb behavior, and our files rate Good/Excellent on our quality rubric); it simply does not supply the implementation skill that gates these tasks."
- README formulation: "A targeted probe confirms the injection channel is live (the agent reads and rates the file as useful)" / "yet does not flip skill-gated tasks upward — context can narrowly depress correctness but never manufactured a pass."
- Raw probe data (key_numbers.md): probe_codex — task 554: 0/3 all strategies; task 907: 0/3 all strategies. probe_claude — task 554: 0/3 all strategies; task 907: none 2/3, always_on 1/3, selective 0/3 (context depressed correctness here; still no manufactured pass).
- Failure-mode triage examples: task 510 (opshin) "engineering precision, not a missing fact"; task 907 (firebase) "architectural pattern choice, not secret knowledge"; task 554 (opshin) "exact behavioral specification"; task 593 (opshin) "deep type-system reasoning". No category percentages reported.

## 7. Limitations (verbatim, condensed to the load-bearing quotes)

1. Sample size: "15/17 tasks with 3 repeats. MDE >>30pp; a 10pp effect is undetectable." / "Our TOST bounds the effect to ≤10–15pp but cannot achieve narrower equivalence without ∼120 tasks."
2. Repository diversity: "Three Python repositories." / "Results may not generalize to other languages, larger codebases, or repositories with exceptionally detailed context files."
3. Injection-channel asymmetry: "Claude receives context via system prompt; Codex via user-turn prepend (no system-prompt flag)." / "This is a confound between the agent arms, though the within-agent strategy comparison remains clean."
4. Ecological validity: always_on "is stronger than the natural workflow (agent reads the file once from the workspace)." / "We argue that if guaranteed presence does not help, natural discovery cannot either—but this is an inference, not a direct measurement."
5. Selective construction/corpus: "the selective wiki equals the AGENTS.md only for opshin; for pdm and firebase it is a broader auto-generated repository wiki (∼10×/18× larger)" / "we cannot cleanly attribute the selective cache-footprint reduction to channel alone."
6. Inert-manipulation concern: "the real AGENTS.md _can_ perturb behavior but never converts a near-miss to a pass" / "the null is not an artifact of low-quality or inert context." / "Whether _purpose-built, task-specific_ context … would help remains an open question for future work."
7. Model-version snapshot: "All results are specific to claude-sonnet-4-6 and gpt-5.5 as of this study; agent behavior, and hence the null, may shift as these models are updated."
8. Mixed provenance: "Claude repeat-0 ran on a local machine; repeats 1–2 on the pod." Sensitivity: "Claude's marginal pass-rates remain 53–55% under all three strategies" and contrasts "stay within ±3.3pp (largest shift: selective − none moves from +2.2 to 0.0pp)"; "The provenance split therefore does not drive the result."

## 8. Evidence log and UNVERIFIED

| URL | Status | Yield |
|---|---|---|
| https://raw.githubusercontent.com/codeprakhar25/context-files-coding-agents/main/README.md | 200 (4 passes; main branch worked, master not needed) | Design, strategies, results table, stats, efficiency, probe, TL;DR |
| https://github.com/codeprakhar25/context-files-coding-agents | 200 | Repo description, MIT, top-level tree (data/, harness/, paper/, pod/, tasks/; analyze.py, power_analysis.py, efficiency_*.py, run_pilot.py, …) |
| https://api.github.com/repos/.../contents/paper | 200 | paper/README.md (1,050 B), paper/data/ |
| https://raw.githubusercontent.com/.../main/paper/README.md | 200 | Venue statement, Table 1–5 pointers, key_numbers.md pointer |
| https://api.github.com/repos/.../contents/paper/data | 200 | key_numbers.md (2,433 B) |
| https://raw.githubusercontent.com/.../main/paper/data/key_numbers.md | 200 (2 passes) | Cell n's, efficiency table, probe per-cell results, TOST bootstrap CIs, provenance notes |
| https://raw.githubusercontent.com/.../main/data/results_summary.csv | 200 | Schema: 18 columns (run_id, task_id, repo, strategy, agent, model, repeat_index, totals for turns/duration/tokens/tool_calls, unique_files_read/written, task_passed, eval_method, created_at). Distinct agent values: claude_code, codex; distinct model values: claude-sonnet-4-6, gpt-5.5. Row-level aggregation NOT reliable via fetch tool (two passes disagreed) — not used for any cited statistic. |
| https://arxiv.org/abs/2607.27250 | 200 (2 passes) | Author, submission 28 July 2026, cs.SE + cs.AI, abstract |
| https://arxiv.org/html/2607.27250v1 | 200 (3 passes) | Abstract, strategy definitions, results with n, statistics, efficiency, probe, failure triage, full limitations, model snapshot |

UNVERIFIED / UNKNOWN:
- Numeric Wilson 95% CIs — method listed in README, no values found anywhere (see §4).
- CLI version numbers — none stated (only model snapshot claude-sonnet-4-6 / gpt-5.5).
- 288 (paper "evaluated runs") vs 291 (README "291-run ablation" DB) — unexplained; key_numbers.md does not state either number.
- Provenance scripts for some key_numbers.md entries: "Source/script not stated" for the difficulty correlation and opshin full-suite subset.
- Failure-mode triage percentages — not reported by the paper (examples only).
