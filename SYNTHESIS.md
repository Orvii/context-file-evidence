# Synthesis — what four studies actually establish

As of 2026-10-05. Every claim below traces to a [study page](studies/), every study page to an [extraction report](research/) with verbatim quotes and arithmetic checks.

**Honest framing first:** the qualitative shape of this reconciliation — "faster but not more correct", "it depends what's in the file" — is already in the secondary commentary; a good blog post made the axis distinction before this repo existed. What this repo adds is the part blogs don't: version-pinned numbers, resolved sign conventions, a grid where every cell is traceable to a primary-source table, and two corrections that only survive contact with the raw sources (§2, §4). Read this as a citation atlas, not a scoop.

## 1. The question splits into four, and each study answers one

"Do context files help?" is not one question. The four studies here partition it:

- **Does the agent finish faster?** → Lulla: yes, meaningfully (mean −20%, median −29%, significant).
- **Does the agent solve more tasks?** → Gloaguen: LLM-generated files, no (slightly worse); developer files, maybe (+2.4%, p=0.21 — cannot reject no-effect).
- **Can we detect any correctness effect at all?** → Khatri: no, and here is the power curve proving the experiment couldn't have.
- **What is in the files anyway?** → Chatlatanagulchai: tests, builds, architecture; almost never security (14.8%) or performance (14.5%).

Every headline fight about AGENTS.md is two of these answers being quoted at each other.

## 2. The token-savings headline is a mean artifact — verified from the source table

The most-cited claim in this space is some variant of "AGENTS.md reduces token usage ~20%." The number is real and the reading is wrong. From Lulla's Table 1 (columns `Without | With`, sign convention resolved three ways and all 15 rows' arithmetic re-verified):

| Total tokens | Without | With | Δ% |
|---|---:|---:|---:|
| **Mean** | 687,632.13 | 619,321.70 | **−9.93%** |
| **Median** | 223,707.00 | 226,582.00 | **+1.29%** |

The standard deviation (1.29M) is ~1.9× the mean: the distribution is a long expensive tail. The file shrank the tail — the paper says exactly this, *"primarily reduces token usage in a small number of very high-cost runs, rather than uniformly lowering token consumption"* — and the **typical run got marginally more expensive**. Input tokens show the same split (mean −9.73%, median +3.41%). Wall-clock is the exception where mean and median agree, which is why the speed result is solid and the cost result is not.

This is [bench-notes](https://github.com/Orvii/bench-notes) note 1 (median-over-mean) caught in the wild, in a peer-adjacent paper, propagated by secondary sources that inverted it: alphaXiv's overview generalizes the wall-clock mean/median agreement to "a general benefit across most tasks" — true for time, false for tokens. The total-token median rise appears **only in the table**; the paper's prose never narrates it. The general rule now lives as [bench-notes note 15](https://github.com/Orvii/bench-notes): say which part of the distribution moved.

## 3. The null and the negative are compatible — the power band is the bridge

Gloaguen reports LLM files *reducing* resolution by 0.5–3%. Khatri reports *no detectable* correctness effect. These are not in conflict once you put Khatri's power analysis next to Gloaguen's point estimates:

- Khatri: at n=17 tasks × 3 repeats, a **30pp** effect is caught only 57% of the time; 10pp needs ~120–200 tasks; TOST bounds any effect to ≤10–15pp.
- Gloaguen: the effects in play are 2–3pp — an order of magnitude below anything any study in this set can resolve individually. Gloaguen's own v3 walked its headline back accordingly: v1's "+4% for developer files" became "2.4% (p=21%)" with eight tables and significance tests added.

The honest synthesis sentence: **the best current estimate of a context file's effect on correctness is "within a few points of zero, in either direction, depending on the file" — and no published study can yet distinguish that from zero at conventional power.** Anyone selling you a confident sign on this axis is selling a point estimate without its interval. The discipline for reporting such results — bound first, headline second — is [equivalence-notes note 12](https://github.com/Orvii/equivalence-notes).

## 4. Version drift is not pedantry — it changes conclusions

Two of the four primary sources have had their numbers move:

- **Gloaguen** has three versions; v1 and v3 differ in benchmark name (AGENTbench→CTXbench), the developer-file gain (4%→2.4% with p=0.21), and a reasoning-token figure (14%→10%). The InfoQ piece everyone cites quotes v1 — and also misnames the model ("Claude 3.5 Sonnet"; the paper says Sonnet-4.5).
- **Chatlatanagulchai** v1→v2 changed **11 of 16** content percentages; most blogs still quote v1's "build and run commands (62.3%)" where v2 says Testing (75.9%) leads.

And the drift is not only across versions: phrases that never existed in any version — "CTXBENCH" in caps, agents following instructions "almost to a fault" — circulate as quotes. The verification habit this repo enforces (verbatim quote or table transcription, per version, from the primary source) is not bureaucracy; it is the only thing standing between a reader and a citation that was already wrong three retellings ago.

## 5. The mechanism is obedience, and obedience is content-dependent

All three experiments independently measured the same thing: **agents do what the file says** — Gloaguen's own phrasing, "instructions in context files are well followed." Gloaguen: more tests, more grep, more repo-specific tooling (`uv` used 1.6×/instance when mentioned, <0.01× when not), more reasoning tokens — "the absence of improvements with context files is not due to a lack of instruction-following." Lulla: less exploration when structure is described upfront. Khatri: fewer blind full-suite runs on the one repo whose file warned the suite was slow — and *depressed* correctness on one probe task.

Which yields the only design rule the evidence actually supports:

> A context file is a lever on agent behavior, not a source of agent skill. It moves behavior in the direction its content points, it costs steps and tokens to be obeyed, and it cannot supply capability the model lacks (Khatri's probe: "context can narrowly depress correctness but never manufactured a pass"). Write what is expensive to rediscover (slow suites, non-obvious conventions, the two commands that actually work) and delete what the model already knows (repository overviews — Gloaguen's ablation: present in 95–100% of generated files, worth nothing).

Gloaguen's ablations sharpen the cost side: removing the *testing* section from a generated file cut cost significantly (p=0.023/0.0035) without hurting accuracy. The most expensive section is often the one doing the least.

## 6. What the evidence base is missing

- **No study measures security or performance outcomes** — while the census shows ~85% of files never mention either. The guardrail gap is unmeasured on both ends.
- **No non-Python evidence.** All three experiments are Python-only; Gloaguen flags the confound explicitly (models may already know Python tooling from training data, "nullifying the effect").
- **No long-horizon or multi-session evidence.** Everything here is single-task PR reconstruction.
- **No purpose-built files.** Every study tests either real-world developer files or generated ones; Khatri names task-specific context as open future work.
- **No file-length dose-response.** Word counts are described (mean 641, range 24–2003) but never varied as an experimental axis.

A study that fills any of these rows is a genuine contribution; a study that re-runs Python PR reconstruction with a fifth agent is not.

## 7. If you must act today

1. Keep the file short, specific, and about *this repo's* traps. The evidence supports "minimal requirements" (Gloaguen's own conclusion) and nothing broader.
2. Do not generate it with an LLM and ship it unreviewed — every generated-file result in this set is ≤ the no-file baseline.
3. Put the expensive-to-rediscover facts in it (slow test suites, the real build command, the convention that will silently break PRs). Delete the architecture overview.
4. If you claim a benefit, measure it on your own tasks. The published effect sizes (±2–3pp) are below the resolution of everything in this grid; your repo's file may genuinely help or hurt, and only a paired local experiment will tell you which.
5. When citing any number from this space, cite the version. See §4.

---

*Related Orvii repos: [harness-atlas](https://github.com/Orvii/harness-atlas) (what each harness promises, per-cell evidence) · [convention-map](https://github.com/Orvii/convention-map) (which file each harness actually reads) · [bench-notes](https://github.com/Orvii/bench-notes) (measurement failure modes, incl. median-over-mean) · [retractions](https://github.com/Orvii/retractions) (things we believed and disproved).*
