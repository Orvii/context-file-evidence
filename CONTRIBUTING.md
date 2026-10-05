# Contributing

This repository's value is its citation discipline. A contribution that weakens it — a number without a primary source, a claim from a blog, a version-unpinned quote — is worse than no contribution.

## Adding a study

1. **Primary source or nothing.** Fetch the paper / code release itself. If you only found it via a summary, find the original or don't add it. Secondary sources may be linked as *corroboration*, never as the citation for a number.
2. **Write the extraction report first** — under `research/<slug>.md`: citation block with **version**, setup, every results table transcribed with column headers verbatim, sign convention resolved explicitly (which column is the baseline), qualitative claims as verbatim quotes with section numbers, an evidence log, and an UNVERIFIED list. Multi-pass extraction of the same URL with different queries is the normal technique; one pass returns a subset.
3. **Then the study page** — under `studies/<slug>.md`: what it measured, the result in plain language, the verbatim tables that matter, **"what this study does NOT say"**, and why it is in the grid. Pin the version in the footer.
4. **Then the grid** — add the column to `matrix.md`. Every cell: statistic named (mean vs median), direction symbol, significance where it exists, version tag where versions differ.
5. **Check versions.** If the source has multiple arXiv versions, diff the numbers between them. If they moved, record the delta — see `studies/gloaguen-success.md` and `studies/agent-readmes.md` for the format.
6. **Update SYNTHESIS only if the new study changes a conclusion.** It should cite study pages, never restate raw numbers that live in the matrix.

## Rules that are not negotiable

- **`unknown` over a guess.** If the primary source does not state it, the cell says `unknown — not in the primary source`.
- **Mean and median are different claims.** Report both whenever the source provides both; flag every divergence with ⚠.
- **A null is not a zero.** Report the power bound with any ∅.
- **Observational ≠ experimental.** Content statistics about files are never evidence about agent performance.
- **No phantom quotes.** Verify a phrase exists in the source before quoting it. Two phrases circulating as quotes from these papers exist in no version of them (see `SYNTHESIS.md` §4).

## Style

English everywhere. Markdown tables over prose walls for numbers. Verbatim quotes in quotation marks with section numbers. Every page self-contained enough to cite without reading the rest of the repo.

---

Orvii — Open, Research, Vision, Innovation & Ideas.
