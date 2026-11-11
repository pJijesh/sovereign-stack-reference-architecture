# Weighted decision matrix template

Use this when comparing candidate options for a layer (for example three vector stores or two identity approaches). It is deliberately simple. Its main value is making criteria, weights and assumptions explicit so that they can be challenged, not producing a "correct" number.

## Steps

1. **State the decision** and the options in a sentence each. Aim for two to five options.
2. **Set must-have gates.** These are pass or fail, and are applied before any scoring. An option that fails a gate is excluded, however well it scores elsewhere. Examples: supports the required region; exports data in a documented format; meets the mandatory criteria in the relevant decision record.
3. **Choose criteria** (six to ten is usually enough) and give each a **weight**. Weights add up to 100. Agree the weights **before** scoring, with the people who own the outcome, so that they are not tuned to favour a preferred answer.
4. **Score each option** against each criterion from 0 to 5 using the anchors below. Write one line of evidence for each score.
5. **Calculate** the weighted score: sum of (weight x score) for all criteria, divided by 100. The result is on the same 0 to 5 scale.
6. **Test sensitivity.** Change the two or three weights you are least sure about and see whether the ranking changes. If it does, the decision is close and you should discuss the underlying trade-off, not the number.
7. **Record the outcome** in a decision record, including the runners-up and the reasons.

## Scoring anchors (0 to 5)

| Score | Meaning |
|---|---|
| 0 | Does not meet the need, or no evidence available |
| 1 | Poor: meets the need only with significant workarounds |
| 2 | Weak: meets part of the need |
| 3 | Adequate: meets the need with known limitations |
| 4 | Good: meets the need well, minor limitations |
| 5 | Strong: meets or exceeds the need, with evidence |

## Suggested criteria

Pick and weight what matters for the decision. Starting set:

- Data location and residency controls
- Exit and portability (formats, export, contract terms, tested)
- Security and key control
- Operational fit and skills available
- Total cost of ownership over a stated period (including exit and egress)
- Capability fit (functional and performance needs)
- Supplier viability and support
- Auditability (logs, evidence, certifications relevant to you)
- Licence and governance of the software (for open-source options)

## Template

**Decision:** ________________________________  **Date:** __________  **Owner:** __________

**Must-have gates**

| Gate | Option A | Option B | Option C |
|---|---|---|---|
| Gate 1: ________________ | Pass / Fail | Pass / Fail | Pass / Fail |
| Gate 2: ________________ | Pass / Fail | Pass / Fail | Pass / Fail |

**Weighted criteria** (weights must total 100)

| Criterion | Weight | A score | B score | C score | Evidence notes |
|---|---:|---:|---:|---:|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| **Total** | **100** | | | | |
| **Weighted score (0 to 5)** | | | | | |

**Sensitivity check:** which weights did you vary, and did the ranking change?

**Outcome and reasons:**

**Residual risks accepted, and by whom:**

In a spreadsheet, the weighted score for option A is `=SUMPRODUCT(weights, A_scores)/100`.

## Worked example (illustrative, fictional)

The numbers below are invented to show the mechanics. They do not describe any real product, and they are not a recommendation.

**Decision:** choose a hosting approach for a new internal service. Options are labelled A, B and C only.

| Criterion | Weight | A | B | C |
|---|---:|---:|---:|---:|
| Data location and residency controls | 20 | 4 | 3 | 5 |
| Exit and portability | 20 | 2 | 4 | 5 |
| Security and key control | 15 | 3 | 4 | 4 |
| Operational fit and skills | 15 | 5 | 3 | 2 |
| Total cost of ownership | 15 | 4 | 3 | 2 |
| Capability fit | 10 | 4 | 3 | 3 |
| Supplier viability and support | 5 | 4 | 3 | 3 |
| **Weighted score** | **100** | **3.60** | **3.35** | **3.65** |

C narrowly leads, A is close behind, and B trails. Now suppose the group is less sure about two weights and tries exit and portability at 30 and operational fit at 5 (other weights unchanged, total still 100):

| | A | B | C |
|---|---:|---:|---:|
| Weighted score | 3.30 | 3.45 | 3.95 |

C still leads, but B now overtakes A. The first ranking was therefore sensitive to those two weights, and the real discussion should be about how much the organisation values portability against operational ease, and whether it has the skills for C.

## Cautions

- A matrix can create false precision. Do not treat a difference of a few tenths as meaningful without looking at sensitivity.
- Cost and capability are easy to quantify, and exit and jurisdiction exposure are not. Be careful that the measurable criteria do not dominate by default.
- Use gates for things that must not be traded off.
