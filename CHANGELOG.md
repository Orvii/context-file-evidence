# Changelog

## [2026-10-06] - SYNTHESIS rule 6: check the casing

### Modified
- `SYNTHESIS.md` §7 — new action rule: verify the filename casing your harness reads. convention-map v3.4 found Bolt auto-reading lowercase `agents.md` with no documented `AGENTS.md`; shipping only the uppercase standard is invisible to it.

Newest first. Format: date — headline, then Added/Modified per file.

## [2026-10-05] - PDF gap-fill: two unknowns resolved

### Modified
- `research/agent-readmes-observational.md` §7 — Threats to Validity recovered verbatim from the v2 PDF (the HTML truncates before it): 80.3% inter-inspector agreement, binary labels measure prevalence not depth, FRE measures form not difficulty, header counts capture only formal Markdown.
- `research/evaluating-agents-md.md` — the documentation-removal ablation's missing percentage recovered: **2.7%** (v3 Appendix B / Figure 12; v1 §4.3 / Figure 5). Root cause of the miss recorded: arXiv HTML carries the value in MathML, which tag-stripping extraction drops.
- `studies/agent-readmes.md` — new "what the paper says about its own numbers" section; footer updated.
- `studies/gloaguen-success.md` — the ablation paragraph now carries 2.7% and the redundancy-conditional reading it supports.

## [2026-10-05] - Initial release: four studies, one grid

### Added
- `README.md` — entry point: the four studies, the short answer, why the citation discipline exists.
- `matrix.md` — study × axis grid; every cell cites a primary source; symbols for ▲/▼/∅/⚠; "where they agree" and "where they disagree — and why it is not a contradiction" sections.
- `SYNTHESIS.md` — the reconciliation: question partition (§1), the mean-artifact token finding verified against Table 1 (§2), the power band bridging the null and the negative (§3), version drift (§4), obedience as mechanism (§5), evidence gaps (§6), action rules (§7). Honest about what secondary commentary already said vs what this repo adds.
- `studies/lulla-efficiency.md` — efficiency axis; Table 1 verbatim with resolved sign convention; mean/median split; "what it does NOT say" (no correctness metric; Codex only).
- `studies/gloaguen-success.md` — success axis; v1-vs-v3 delta table; Tables 2/5/6/7 numbers; the phantom-quote warnings (CTXBENCH, "almost to a fault").
- `studies/two-agent-ablation.md` — correctness null; TOST bounds; power honesty; manipulation-validity probe; the author's confound list including the 288-vs-291 run discrepancy.
- `studies/agent-readmes.md` — observational census; 16-type content table; v1→v2 delta (11 of 16 changed); accretion-not-deletion maintenance finding.
- `research/` — four full extraction reports with evidence logs, arithmetic verification, UNVERIFIED sections.
- `METHODOLOGY.md` — evidence contract; experimental-vs-observational separation; metric axes; the mean/median rule.
- `hero.svg` — animated mean-vs-median divergence, numbers from Lulla Table 1; reduced-motion honored.
- `CONTRIBUTING.md`, `LICENSE` (MIT), `CITATION.cff`.
- `scripts/pins.json` + `scripts/version-drift.py` + `.github/workflows/version-drift.yml` — monthly CI reports whether any pinned arXiv version has moved upstream; drift is flagged as a research task, never auto-applied.
