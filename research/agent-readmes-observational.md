# Agent READMEs — Observational Study Report (arXiv:2511.12884)

> **Study type: OBSERVATIONAL.** Content analysis of existing agent context files and their commit history. The paper reports **no experiment on agent performance**. Every statistic here describes *what the files contain / how they are maintained* — it is NOT evidence that context files help or hurt agents.

## 1. Citation

- **Title:** "Agent READMEs: An Empirical Study of Context Files for Agentic Coding"
- **Authors (in order; affiliations from HTML v2 author block):**
  1. Worawalan Chatlatanagulchai — "Faculty of Engineering, Kasetsart University, Bangkok, Thailand"; "Nara Institute of Science and Technology, Ikoma, Japan"
  2. Hao Li — "Queen's University, Kingston, Canada"
  3. Yutaro Kashiwa — "Nara Institute of Science and Technology, Ikoma, Japan"
  4. Brittany Reid — Nara Institute of Science and Technology, Ikoma, Japan
  5. Kundjanasith Thonglek — Kasetsart University
  6. Pattara Leelaprute — Kasetsart University
  7. Arnon Rungsawang — Kasetsart University
  8. Bundit Manaskasemsak — Kasetsart University
  9. Bram Adams — Queen's University
  10. Ahmed E. Hassan — Queen's University
  11. Hajimu Iida — Nara Institute of Science and Technology
- **arXiv:** 2511.12884 · **v1:** 17 Nov 2025 · **v2 (latest revision):** 9 Aug 2026 · Category: cs.SE · No comments field, no venue note.
- **Abstract (v2), assembled from consecutive verbatim fragments:**
  "Agentic coding tools receive goals written in natural language, break them down into specific tasks, and write or execute code with minimal human intervention. Central to this process are agent context files (e.g., AGENTS.md and CLAUDE.md) that provide persistent, project-level instructions. In this paper, we conduct the first large-scale empirical study of 2,303 agent context files from 1,925 repositories to characterize their structure, maintenance, and content. We find that these files are not static documentation but complex, difficult-to-read artifacts that evolve like configuration code through frequent, small additions. Our content analysis of 16 instruction types shows that developers prioritize functional context, such as test procedures (75.9%), implementation details (70.8%), and architecture (68.1%). We also identify a significant gap: non-functional requirements such as security (14.8%) and performance (14.5%) are rarely specified. These findings indicate that while developers use context files to make agents functional, they provide few guardrails to ensure that agent-written code is secure or performant, highlighting the need for improved tools and practices."
- **Abstract (v1), same assembly method — differs from v2 (see §5):**
  "Agentic coding tools receive goals written in natural language as input, break them down into specific tasks, and write or execute the actual code with minimal human intervention. Central to this process are agent context files ("READMEs for agents") that provide persistent, project-level instructions. In this paper, we conduct the first large-scale empirical study of 2,303 agent context files from 1,925 repositories to characterize their structure, maintenance, and content. We find that these files are not static documentation but complex, difficult-to-read artifacts that evolve like configuration code, maintained through frequent, small additions. Our content analysis of 16 instruction types shows that developers prioritize functional context, such as build and run commands (62.3%), implementation details (69.9%), and architecture (67.7%). We also identify a significant gap: non-functional requirements like security (14.5%) and performance (14.5%) are rarely specified. These findings indicate that while developers use context files to make agents functional, they provide few guardrails to ensure that agent-written code is secure or performant, highlighting the need for improved tooling and practices."

## 2. Corpus and collection (§3, v2)

Verbatim:
- "This study systematically collects and analyzes agent context files from open-source repositories for three agentic coding tools: Claude Code, OpenAI Codex, and GitHub Copilot."
- "We identify repositories that use agentic coding tools through the AIDev dataset" / "which provides a curated list of repositories where agentic coding tools contribute to development."
- "From this dataset, we select 8,370 repositories with at least 5 GitHub stars to exclude toy projects."
- "We use the GitHub API to scan the root directory of each selected repository" / "for files whose filenames follow the official naming convention specified in each agent's documentation."
- "We search for CLAUDE.md, AGENTS.md, and copilot-instructions.md using case-insensitive filename matching."
- "This process yields 922 Claude Code files, 694 OpenAI Codex files, and 687 GitHub Copilot files across 1,925 repositories."

Corpus totals (identical in v1 and v2): **2,303 files / 1,925 repositories** (922 + 694 + 687 = 2,303).

## 3. Research questions (identical in v1 and v2, §1)

- **RQ1** (§4.1): "What are the characteristics of agent context files?"
- **RQ2** (§4.2): "How often do developers maintain agent context files?"
- **RQ3** (§4.3): "What instructions are included in agent context files?"
- **RQ4** (§4.4): "To what extent can instructions in agent context files be classified automatically?"

## 4. Instruction types — v2 Table 3, all 16 types (§4.3.2)

| Label | Description (verbatim) | % of ACFs (v2) |
|---|---|---:|
| System Overview | "Provides a general overview or describes the key features of the system." | 59.0% |
| AI Integration | "Contains specific instructions on the desired behavior and roles of agentic coding, as well as methods for integrating other AI tools." | 24.1% |
| Documentation and References | "Lists supplementary documents, links, or references for additional context." | 26.8% |
| Architecture | "Describes the high-level structure, design principles, or key components of the system's architecture." | 68.1% |
| Impl. Details | "Provides specific details for implementing code or system components, including coding style guidelines." | 70.8% |
| Build and Run | "Outlines the process for compiling source code and running the application, often including key commands." | 63.0% |
| Testing | "Details the procedures and commands for executing automated tests." | 75.9% |
| Conf.&Env. | "Instructions for configuring the system and setting up the development or production environment." | 38.9% |
| DevOps | "Covers procedures for software deployment, release, and operations, such as CI/CD pipelines." | 18.4% |
| Development Process | "Defines the development workflow, including guidelines for version control systems like Git." | 65.1% |
| Project Management | "Information related to the planning, organization, and management of the project." | 5.4% |
| Maintenance | "Guidelines for system maintenance, including strategies for improving readability, detecting and resolving bugs." | 44.6% |
| Debugging | "Explains error handling techniques and methods for identifying and resolving issues." | 25.3% |
| Performance | "Focuses on system performance, quality assurance, and potential optimizations." | 14.5% |
| Security | "Addresses security considerations, vulnerabilities, or best practices for the system." | 14.8% |
| UI/UX | "Contains guidelines or details concerning the user interface (UI) and user experience (UX)." | 8.7% |

Note: the v2 abstract's "test procedures (75.9%)" is the Table 3 label **Testing**.

## 5. VERSION DELTA (v1 17 Nov 2025 → v2 9 Aug 2026) — secondary sources still quote v1

| Instruction type | v1 | v2 | Changed? |
|---|---:|---:|---|
| System Overview | 59.0% | 59.0% | no |
| AI Integration | 24.4% | 24.1% | YES |
| Documentation (v1) / Documentation and References (v2) | 26.8% | 26.8% | no (label extended) |
| Architecture | 67.7% | 68.1% | YES |
| Impl. Details | 69.9% | 70.8% | YES |
| Build and Run | 62.3% | 63.0% | YES |
| Testing | 75.0% | 75.9% | YES |
| Conf.&Env. | 38.0% | 38.9% | YES |
| DevOps | 18.1% | 18.4% | YES |
| Development Process | 63.3% | 65.1% | YES |
| Project Management | 5.4% | 5.4% | no |
| Maintenance | 43.7% | 44.6% | YES |
| Debugging | 24.4% | 25.3% | YES |
| Performance | 14.5% | 14.5% | no |
| Security | 14.5% | 14.8% | YES |
| UI/UX | 8.7% | 8.7% | no |

Abstract-level wording changes: v1 headline "build and run commands (62.3%)" → v2 "test procedures (75.9%)"; v1 "security (14.5%) and performance (14.5%)" → v2 "security (14.8%) and performance (14.5%)"; v1 quote marks ("READMEs for agents") dropped in v2; v1 ends "improved tooling and practices" → v2 "improved tools and practices". Corpus numbers did NOT change (same 2,303/1,925; same 922/694/687).

**Warning for citers:** any number set containing "build and run commands 62.3%" or "Testing 75.0%" is quoting v1. The current (v2) headline values are Testing 75.9%, Impl. Details 70.8%, Architecture 68.1%, Security 14.8%, Performance 14.5%.

## 6. Readability and maintenance findings (v2)

File size & readability (§4.1):
- Word counts via regex `\w+` (§4.1.2). Median words: GitHub Copilot "median 535.0 words", Claude Code "median 485.0 words", Codex "median 335.5 words" (§4.1.3, Fig. 3a).
- Readability = Flesch Reading Ease (§4.1.2). Medians: Claude Code "median complexity score of 42.39", Copilot "median score 44.39", Codex "median complexity score of 51.41" (§4.1.3, Fig. 3b). Human judgments "trend in the same direction"; correlation described as "a weak positive relationship": "ρ=0.19 (p=0.05)" (§4.1.3).
- "This difference in context-file length cannot be explained by task difficulty." (§4.1.3)
- Abstract framing: files are "complex, difficult-to-read artifacts".

Maintenance (§4.2):
- "A majority of Claude Code context files (67.0%) are modified in multiple commits" (§4.2.3); Copilot 59.8%, Codex 59.4%.
- Commits touching context files analyzed: 5,655 Claude Code / 2,767 Codex / 2,237 Copilot (§4.2.2).
- Median interval between changes: Claude Code 23.8 hours, Codex 22.3 hours; "The median interval is 68.0 hours (around 3 days) for GitHub Copilot" (§4.2.3).
- Change pattern "small, incremental additions": additions appeared 78 times across 66 of 100 sampled commits (48 line-level, 30 section-level); instruction fixes in 32 commits; deletion labels in 19 (§4.2.3).
- "deletions are consistently negligible across all agent context file types" — median deleted words below 15.0 (§4.2.3).
- "Some form of substantive instruction edit (adding, fixing, or deleting directives) appears in 92%" of sampled commits; purely non-functional maintenance was the only label in 8% (§4.2.3).
- Abstract summary quote: files "evolve like configuration code through frequent, small additions".

RQ4 bonus (§4.4 v1, §1 v2): classifier **GPT-5**; v1 §4.4: "micro-average F1-score of 0.79"; v2 intro: "Automatic classification is highly effective (0.79 F1-score) for concrete functional topics" and "struggles with abstract or nuanced topics (e.g., Maintenance)". Taxonomy construction (§4.3.2): H1/H2 titles seeded candidate labels; "Claude Opus 4.1, Gemini 2.5 Pro, and GPT-5" prompted for suggestions; "61 initial labels" consolidated to "a final taxonomy of 16 categories"; 332-file proportional sample used for validation. Per-category F1 scores: **not found** (see §8).

## 7. Limitations / Threats to Validity — NOT RETRIEVABLE

- Section 7 "Threats to Validity" exists in both versions; table of contents shows subsections **7.1 Internal Validity, 7.2 Construct Validity, 7.3 External Validity**.
- The section text was **not reachable** in any fetch (document truncation cuts off inside §6 Related Work / §6.1 "AI agents in software engineering" for v1, earlier for v2). Places checked: arxiv.org/html v2 (4 attempts incl. #S7 anchor), arxiv.org/html v1 (2 attempts), alphaxiv.org/abs/2511.12884, ar5iv.labs.arxiv.org, r.jina.ai proxy (HTTP 403). → **UNVERIFIED — not found in the primary source via available tooling.** Do not paraphrase this section from memory.

## 8. Evidence log and UNVERIFIED

| URL | Status | Yield |
|---|---|---|
| https://arxiv.org/abs/2511.12884 | 200 | Title, 11 authors, v1 17 Nov 2025, v2 9 Aug 2026, cs.SE |
| https://arxiv.org/html/2511.12884v2 | 200 (7 passes) | v2 abstract, §3 corpus, RQs, Table 3 (all 16), §4.1.3, §4.2.3, §4.3.2, affiliations; deepest reach ~§4.3.3 |
| https://arxiv.org/html/2511.12884v1 | 200 (3 passes) | v1 abstract, v1 Table 3 (all 16), v1 corpus, §4.4 GPT-5/0.79; reach ended ~§6.1 |
| https://ar5iv.labs.arxiv.org/html/2511.12884 | 200 | Truncated before §7 (mentions §7 only in outline) |
| https://www.alphaxiv.org/abs/2511.12884 | 200 | Summary page; classifier conclusion sentence; no §7 |
| https://r.jina.ai/https://arxiv.org/html/2511.12884v2 | 403 | Blocked |

UNVERIFIED / UNKNOWN:
- §7 Threats to Validity text — unknown, not found (see §7 above).
- RQ4 per-category F1 scores — unknown, not found (only micro-average 0.79).
- v2 §4.4 classifier attribution — GPT-5/0.79 confirmed in v1 §4.4 and v2 intro; v2 §4.4 body text not directly reached.
- Any effect of context files on agent performance — not measured by this paper (observational by design; the paper states no performance result in any reachable text).
