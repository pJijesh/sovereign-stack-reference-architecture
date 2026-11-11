# Maturity model

The model has five levels across the eight layers. It is a tool for conversation and prioritisation. It is **not** an audit, a certification or a benchmark against other organisations, and no external data supports the level names.

## Levels

| Level | Name | In one line |
|---|---|---|
| 1 | **Ad hoc** | Practice depends on individuals. Little is written down, and you could not easily show the position to a third party. |
| 2 | **Defined** | Policies or standards exist and key systems are known, but application is uneven and mostly untested. |
| 3 | **Managed** | Controls are applied consistently, owned by named people, and recorded. Most critical platforms are covered. |
| 4 | **Tested** | Controls and exit paths are exercised on a schedule, results are recorded and gaps are tracked to closure. |
| 5 | **Adaptive** | Controls are largely automated and monitored, tests are routine, and lessons feed back into policy and design. |

**Level 5 is not the goal for every layer or every organisation.** Proportionality is one of the principles. A sensible target for many mid-size organisations is level 3 across the board, and level 4 for the layers that hold your most critical or sensitive assets.

## Descriptors by layer

| Layer | 1 Ad hoc | 2 Defined | 3 Managed | 4 Tested | 5 Adaptive |
|---|---|---|---|---|---|
| **Identity and access** | Shared or local accounts in places; no single directory; leavers handled by memory | Central identity provider for most applications; MFA for some; joiner and leaver process written but inconsistent | SSO and MFA enforced; joiner, mover, leaver process owned; privileged accounts separate; break-glass defined | Access reviews evidenced; privileged access time-bound; export and rebuild of identities tested | Automated lifecycle and continuous access analytics; workload identities short-lived; exit drill routine |
| **Data and storage** | Data locations unknown; unmanaged exports and spreadsheets | Key systems and locations known; some classification; backups exist but are untested | Catalogue with owner, classification, residency and retention; backups tested | Open formats for curated data; residency checked by automation; restore and deletion tested | Lineage and policy as code; multi-engine reads routine; erasure verified end to end |
| **Integration and APIs** | Point-to-point links, undocumented; credentials embedded in scripts | Some APIs documented; ad hoc gateways or brokers | Central API edge; specifications in your repository; named owners | Contract tests and schema registry in use; replacement drill completed for a sample | Consumer-driven contracts; automated deprecation; alternative provider proven |
| **AI and ML platform** | Unregistered use of external AI tools | Acceptable use policy and partial inventory; applications call providers directly | AI gateway; routing by data classification; model and prompt registry; supplier terms filed | Evaluation in the release path; leakage and erasure tests for retrieval; model swap tested | Continuous evaluation and monitoring; model portability routine; incident learning loop |
| **Orchestration and agents** | Scripts and manual steps, or unmanaged agent pilots | Some workflow tooling; agent pilots with broad credentials | Durable orchestration; agents act through a tool gateway with their own identities | Approval thresholds enforced; kill switch tested; red-team exercises | Autonomy levels adjusted by evidence; anomaly detection on agent behaviour |
| **Security and key management** | Provider default keys only; secrets in configuration files | Secrets manager for some systems; key policy drafted | Key custody set by classification; rotation; segmentation and private endpoints | Revocation tested; egress controls enforced; key use monitored | Automated rotation and posture management; crypto-shredding part of exit drills |
| **Observability** | Logs held on individual systems; no retention policy | Central logging for some systems; default retention | Open collection standard; retention by class; redaction at the collector | Archive export tested; alerts triaged with measures; deletion evidenced | Detection engineering lifecycle; automated personal-data scanning in logs |
| **Governance and compliance** | Obligations unmapped; decisions undocumented | Policies exist; risk register started; decision records occasional | Obligation register with owners; decision records; AI gate; supplier review | Controls tested and evidence collected routinely; exit plans tested; management review held | Continuous control monitoring; external assurance; lessons feed policy |

## Scoring guidance

For each of the 24 questions in [`assessment/self-assessment-template.csv`](../assessment/self-assessment-template.csv):

1. Read the question and the descriptor for the layer.
2. Choose the highest level for which you can point to **evidence** (a document, a test result, a configuration, a record). Do not score on intent.
3. If only part of the estate meets a level, score the level that applies to the **critical** part, and say so in the notes.
4. Leave the score blank if you cannot answer yet. Blank answers are excluded from the average and reported as unscored.
5. Record the evidence in the `evidence` column. A score you cannot evidence is a guess.

Ask someone outside the team to challenge the scores. Self-assessment tends to be generous.

## How the tool scores

`tools/assess.py` takes the mean of the answered questions in each layer, then takes the mean of the layer scores for the overall figure, so that a layer with more questions does not carry more weight. It reports the nearest level name, lists the three weakest layers, optionally lists gaps against a target, and draws a text radar chart. See `python tools/assess.py --help`.

```bash
cp assessment/self-assessment-template.csv my-scores.csv
# edit my-scores.csv, then:
python tools/assess.py my-scores.csv --target 3
```

A worked example using fictional sample scores is in [`assessment/example-filled.csv`](../assessment/example-filled.csv). It is illustrative only and does not describe a real organisation.

## Limits

- Averages hide the minimum. A layer scoring 3.0 may contain a question at level 1. The tool reports the lowest score per layer in JSON output, and you should look at it.
- The levels are ordinal, not interval. The difference between 1 and 2 is not the same as between 4 and 5.
- The model does not weigh layers by importance to your business. Use the target option and your own judgement.
