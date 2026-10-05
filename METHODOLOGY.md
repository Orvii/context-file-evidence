# Methodology — how a cell in this grid is produced

This grid collects what four primary studies actually measured about agent-instruction files (`AGENTS.md`, `CLAUDE.md`, and their cousins). It does not re-run any of them. Its whole job is **traceability**: a number here must lead back to a table or a verbatim sentence in the source, with the version pinned.

## The evidence contract

Every quantitative claim in this repository carries, at minimum:

1. **The primary source.** An arXiv paper (with version) or a code-and-data release. A blog, a tweet, or a secondary summary is never the citation for a number — it may be linked as *corroboration* and labelled as such.
2. **A verbatim quote or a table transcription.** The surrounding sentence, not a paraphrase of it, whenever the claim is a number or a direction.
3. **A version pin.** Papers get revised; numbers move between versions. Where v1 and v2 differ, both are recorded (see [studies/agent-readmes.md](studies/agent-readmes.md)).
4. **The metric and its statistic.** `mean` is not `median`, `success rate` is not `wall-clock time`. A cell that omits which is incomplete.
5. **`unknown` over a guess.** If the primary source does not state a figure, the cell says `unknown — not in the primary source`. We do not fill gaps with a plausible number.

## Two study types — never mix them

The four studies answer two different questions, and collapsing them is the most common error in secondary coverage.

| Type | Question | Studies here |
|---|---|---|
| **Experimental** | Does adding the file change what the agent *does* or *produces*? | Lulla (efficiency), Gloaguen (success), two-agent ablation (correctness) |
| **Observational** | What is *in* the files, and how do they evolve? | Agent READMEs (content) |

An observational statistic — "14.8% of files mention security" — is a fact about files. It is **not** evidence about whether files help agents. This repository keeps the two in separate sections and never lets a content statistic masquerade as a performance result.

## The metric axes

The three experimental studies disagree in the headlines and agree underneath. The disagreement is almost entirely a choice of axis:

- **Correctness / success** — did the agent's patch pass the gold tests? (Gloaguen, two-agent ablation)
- **Efficiency** — wall-clock time to finish. (Lulla, two-agent ablation)
- **Cost** — tokens consumed, and *which* token statistic. (Lulla)
- **Effort** — steps, tool calls, exploration breadth. (all three, and they converge)

A study that reports "faster" and a study that reports "less often correct" are not contradicting each other; they are reading different axes of the same phenomenon. [SYNTHESIS.md](SYNTHESIS.md) is where that reconciliation is written out.

## The mean/median rule

Cost and time results in this space are reported as means, and the distributions are heavily right-skewed — a handful of very expensive runs dominate the average. This repository records the **median alongside the mean wherever the source provides it**, and flags every case where they point in opposite directions. The flagship example is in the hero: one paper's own table shows total-token *mean* falling while total-token *median* rises. A mean-only headline from that table is not wrong so much as it is incomplete in a way that reverses the takeaway. (This is the same failure mode [bench-notes](https://github.com/Orvii/bench-notes) note 1 exists to prevent; it is not a coincidence that it shows up here.)

## Re-running / extending

To add a study: fetch the primary source, extract every results table with its column headers verbatim, resolve the sign convention explicitly (which column is "without", which is "with"), and record the version. Add a row to [matrix.md](matrix.md) and a page under [studies/](studies/). Do not add a study you have only read about second-hand; if the primary source is unreachable, say so and mark the cells `unknown`.

---

Orvii — Open, Research, Vision, Innovation & Ideas.
