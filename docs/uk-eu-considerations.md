# UK and EU considerations

> **Not legal advice.** This is a briefing note that summarises public sources as they stood on **4 November 2026**. Law, adequacy decisions and guidance change, and the application of any rule depends on facts specific to your organisation. Take advice from a qualified adviser before relying on anything here. Where a point could not be verified against a primary source, this document says so.

## 1. How to read this note

The reference architecture is designed so that technical choices can respond to legal change without redesign: regional placement, key custody, logging, AI gating and exit paths are all adjustable. The purpose of this note is to say which legal developments those choices relate to, and what was and was not verified.

**Verification approach.** Facts below were checked against a mix of primary sources (for example legislation.gov.uk, the European Commission's AI Act Service Desk, the ICO) and secondary sources (law-firm and trade commentary) where the primary text could not be retrieved. Each section names which kind of source supports the claim. Full links are in [references](references.md).

## 2. UK data protection framework

- The UK regime is the **UK GDPR** (the retained and amended version of the EU GDPR) together with the **Data Protection Act 2018** (DPA 2018).
- The **Data (Use and Access) Act 2025** (DUAA) received Royal Assent on 19 June 2025 and amends the UK GDPR and DPA 2018. Its provisions commence in stages. Examples named in government guidance include a new "recognised legitimate interests" lawful basis, a more permissive framework for solely automated decisions with required safeguards (information, representations, challenge and human intervention), and a requirement to handle data protection complaints through a defined process. Source: [GOV.UK guidance on the DUAA](https://www.gov.uk/guidance/data-use-and-access-act-2025-data-protection-and-privacy-changes).
- The DUAA's Schedule 7 changes the UK's international transfer framework. The new **data protection test** is met where protection in the destination is "**not materially lower**" than under UK law, assessed as a whole. The Secretary of State applies it when approving transfers by regulations, and controllers and processors apply it, acting reasonably and proportionately, when relying on appropriate safeguards. Source: [DUAA Schedule 7 on legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2025/18/schedule/7).
- A secondary source reports that Commencement No. 6 Regulations 2026 brought a set of DUAA provisions into force on 5 February 2026 and describes them as including cross-border data transfer provisions. **Not verified:** the regulations themselves were not read, so confirm which transfer provisions are in force before relying on them. Source: [Digital Policy Alert summary](https://digitalpolicyalert.org/event/37518-data-use-and-access-act-2025-commencement-no-6-and-transitional-and-saving-provisions-regulations-2026-including-cross-border-data-transfer-regulation-enter-into-force).

**Architecture touchpoints:** data location register and classification ([ADR-0002](adr/0002-data-residency-approach.md)); log minimisation and retention ([ADR-0008](adr/0008-logging-and-retention.md)); complaints, DSAR and erasure capability in the data and AI layers; the AI governance gate ([ADR-0010](adr/0010-ai-governance-gate.md)) for automated decision-making.

## 3. EU GDPR, and when it matters to a UK business

A UK organisation can be subject to the **EU GDPR** directly, for example where it offers goods or services to people in the EU or monitors their behaviour (Article 3), and may then need to consider an EU representative (Article 27). Whether this applies is a question of fact for each organisation. Text: [EU GDPR on EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj).

## 4. International transfers

### 4.1 EU to UK (UK adequacy)

- The European Commission renewed its adequacy decisions for the UK. Secondary reporting dates the announcement to **19 December 2025** and gives the new expiry as **27 December 2031**, covering both the GDPR decision and the Law Enforcement Directive decision. The renewed decisions are time-limited, and the European Data Protection Board asked the Commission to monitor how the DUAA is implemented. Sources: [Shepherd and Wedderburn](https://shepwedd.com/knowledge/european-commission-approves-extension-of-uk-adequacy-decisions/), [Hunton](https://hunton.com/privacy-and-information-security-law/european-commission-renews-uk-data-adequacy-decisions), [RPC](https://www.rpclegal.com/snapshots/data-protection/spring-2026/eu-commission-renews-adequacy-decision-for-the-uks-data-protection-regime/). **Verification note:** the Commission press release page could not be read directly (the PDF returned only a language selector), so the dates rest on secondary sources that agree with each other.
- **Practical effect:** personal data can flow from the EU/EEA to the UK without additional transfer mechanisms while the decision stands. **Risk:** an adequacy decision can be amended or withdrawn. Keep fallback mechanisms (for example standard contractual clauses) in mind for critical flows, and treat the expiry date as a planning input.

### 4.2 UK to EU/EEA

- The ICO keeps a list of current UK adequacy regulations and explains the other transfer routes. Check its list for the EEA and for any other destination. **Not verified:** this note did not confirm the EEA entry on the ICO page, which describes adequacy regulations but, in the version read, did not state the EEA position in the text retrieved. Source: [ICO international transfers guidance](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/).

### 4.3 UK to the US: the UK Extension to the Data Privacy Framework ("data bridge")

- The UK-US data bridge, formally the UK Extension to the EU-US Data Privacy Framework (DPF), allows restricted transfers from the UK to US organisations that have **self-certified to the DPF and opted in to the UK Extension**. Secondary sources date its start to 12 October 2023. Sources: [ICO guidance](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/adequacy-regulations/how-does-the-uk-extension-to-the-eu-us-data-privacy-framework-work), [GOV.UK supporting documents](https://www.gov.uk/government/publications/uk-us-data-bridge-supporting-documents), [Schofield Sweeney](https://www.schofieldsweeney.co.uk/knowledge/data-protection-uk-us-data-bridge-comes-into-force).
- Per ICO guidance, before relying on it you should check that the recipient has an **active** DPF listing, has opted in to the UK Extension, and is registered for the **type of data** you send (HR and/or non-HR). Only US businesses regulated by the FTC or the Department of Transportation can participate, so many sectors are excluded. Additional steps apply to some sensitive categories (for example genetic data, biometric data for unique identification, data about sexual orientation, and criminal offence data), because the DPF's definition of sensitive data is narrower than the UK's special category definition. Periodic re-checks are needed because listings lapse.
- **Legal challenge risk (EU side):** the EU General Court dismissed Philippe Latombe's challenge to the EU-US DPF adequacy decision on 3 September 2025, and he appealed to the Court of Justice on 31 October 2025. Commentary describes the first ruling as short-term reassurance and recommends monitoring and keeping alternative mechanisms available. Source: [WilmerHale](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20251201-european-court-of-justice-to-review-challenge-to-eu-us-data-privacy-framework). **Not verified:** whether the appeal has progressed or been decided after the source date. Check before relying on this section.
- The UK bridge is a separate UK instrument that builds on the EU-US framework, so a change to the EU framework does not automatically change UK law, but the legal and political context is linked. Treat that as a risk to monitor, not a prediction.

### 4.4 Other destinations and tools

- Where no adequacy decision or regulation applies, the usual UK tools are the ICO's International Data Transfer Agreement (IDTA) or the UK Addendum to the EU standard contractual clauses, plus a transfer risk assessment. Source: [ICO IDTA guidance](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/appropriate-safeguards/what-are-standard-data-protection-clauses-the-uk-idta-and-the-addendum). From the EU side, see the Commission's [standard contractual clauses page](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/standard-contractual-clauses-scc_en).
- The new UK data protection test (section 2) changes how the assessment is framed. Check the ICO's updated guidance for current expectations.

### 4.5 Residency is not the same as jurisdiction exposure

Keeping data in a UK or EU region reduces some risks. It does not decide which laws can reach the data or the supplier. For example, US legislation (the CLOUD Act, [18 U.S.C. 2713](https://www.law.cornell.edu/uscode/text/18/2713)) provides for US legal process to apply to providers within US jurisdiction in respect of data in their possession, custody or control, wherever stored. Whether and how that affects your arrangements is a legal and contractual question. The architecture response is to record the exposure, minimise what is exposed (classification, encryption and key custody under [ADR-0003](adr/0003-bring-your-own-key-and-key-custody.md)), and keep an exit path ([ADR-0009](adr/0009-exit-strategy-and-portability-tests.md)).

## 5. EU Data Act and switching between providers

The EU Data Act applies since 12 September 2025 and includes rules on switching between data processing services (cloud, and other services in scope). The Commission describes a transition period for switching charges, after which, from **12 January 2027**, providers can no longer charge for the operations needed to switch or for data egress in the cases covered. Source: [European Commission, Data Act explained](https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained). **Not verified here:** the detailed notice periods, scope and any UK-specific relevance. The Act is aimed at services offered to customers in the EU, so UK-only customers may not be covered. Use it as a source of contract negotiating points and as a benchmark for [ADR-0009](adr/0009-exit-strategy-and-portability-tests.md), and confirm applicability.

## 6. EU AI Act touchpoints

The EU AI Act is Regulation (EU) 2024/1689 ([EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)). It can apply to organisations outside the EU, for example providers that place systems on the EU market and providers or deployers whose AI output is used in the EU. Scope is fact-specific.

### 6.1 Key dates (as verified)

The dates below were checked against the European Commission's AI Act Service Desk timeline page and against several law-firm commentaries that agree with it. The amending regulation, **Regulation (EU) 2026/1744 (the "Digital Omnibus on AI")**, is recorded on EUR-Lex as dated 8 July 2026 and entering into force on 27 July 2026, and secondary sources report publication in the Official Journal on 24 July 2026. **Verification note:** the operative text of Regulation 2026/1744 was not read by the author of this document. Only its EUR-Lex metadata page and secondary sources were consulted. Confirm dates against the text before acting.

| Date | What applies | Notes |
|---|---|---|
| 2 February 2025 | General provisions and **prohibited practices** apply; AI literacy provision applies | Commission Service Desk timeline |
| 2 August 2025 | **General-purpose AI (GPAI) model** obligations apply; governance bodies and national authority designation | Commission Service Desk timeline |
| 2 August 2026 | **Article 50 transparency obligations** apply (for example informing people they are interacting with an AI system); enforcement begins for GPAI models, prohibitions, transparency rules and AI literacy | Under the Omnibus, a transitional deadline to **2 December 2026** applies to Article 50(2) marking of synthetic content for systems already on the market before 2 August 2026 |
| 2 December 2026 | New prohibition on AI systems generating non-consensual sexual deepfakes and child sexual abuse material; Article 50(2) transitional deadline for existing systems | Added by the Omnibus, per the Service Desk |
| 2 August 2027 | Each Member State should have at least one operational AI regulatory sandbox | Commission Service Desk timeline |
| 2 December 2027 | **Annex III high-risk** AI systems rules apply | Moved from 2 August 2026 by the Omnibus |
| 2 August 2028 | **Annex I** high-risk (AI in products covered by EU harmonised product legislation) rules apply | Final milestone |

Sources: [AI Act Service Desk timeline](https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act); [Regulation (EU) 2026/1744 on EUR-Lex](https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng); commentary from [Lewis Silkin](https://www.lewissilkin.com/en/insights/2026/07/27/the-digital-omnibus-on-ai-enters-into-force-today-102nedo), [Garrigues](https://www.garrigues.com/en_GB/garrigues-digital/ai-digital-omnibus-regulation-has-been-published-redefining-deadlines-and) and [iubenda](https://www.iubenda.com/en/blog/ai-omnibus-adopted-august-2-obligations-july-2026/).

**Changes to the position during drafting.** Earlier commentary (mid-2026) described the Omnibus as adopted by Parliament but awaiting Council and publication, and some sources said transparency marking would move wholesale to 2 December 2026. The later and more specific position, supported by the Commission's page and three commentaries, is that Article 50 applies from 2 August 2026 with a transitional deadline of 2 December 2026 only for Article 50(2) marking by systems already on the market. This illustrates why dates need re-checking.

**AI literacy.** The Article 4 provision was amended by the Omnibus. One source shows its current wording as providers and deployers taking measures to support the development of AI literacy. Check the current text. Source: [artificialintelligenceact.eu, Article 4](https://artificialintelligenceact.eu/article/4/).

### 6.2 Where the architecture connects

| AI Act theme | Where it shows up here |
|---|---|
| Prohibited practices | Intake questions at the [AI governance gate](adr/0010-ai-governance-gate.md) |
| Transparency to users (Article 50) | Design of user-facing AI features; AI gateway can add disclosures and content marking hooks |
| High-risk systems: risk management, data governance, logging, human oversight, accuracy | Gate tier 3 evidence; [logging ADR](adr/0008-logging-and-retention.md); [agent autonomy ADR](adr/0012-agent-autonomy-and-tool-permissions.md) |
| Deployer log retention (Article 26(6)): logs under the deployer's control kept at least six months unless other law provides otherwise | Log class "AI gateway" in ADR-0008. Source: [Article 26](https://artificialintelligenceact.eu/article/26/) |
| GPAI model provider duties | Mostly fall on model providers; as a user, record model provider documentation and licence terms in the model registry |
| Inventory and classification | AI use case register at the gate |

Whether any of your systems is high-risk depends on Annex III categories (for example employment and worker management, education, access to essential services) and on how the system is used. Seek advice on classification.

## 7. UK position on AI regulation

**Not verified.** To the author's knowledge, at the time of writing the UK has relied on existing regulators and general law (including data protection law and ICO guidance) rather than a single horizontal AI statute. Search results around the drafting date included material on UK AI bills, but the status of any bill could not be confirmed from a reliable primary source. Check current government and parliamentary sources. For data protection aspects of AI, see the [ICO's AI guidance](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/).

## 8. What would change the recommended defaults

| Development | Possible architecture response |
|---|---|
| UK-EU adequacy withdrawn or amended | Activate fallback transfer mechanisms; review which UK-EU flows are critical |
| EU-US DPF invalidated on appeal, and consequent changes to the UK bridge | Move affected flows to alternative mechanisms; increase use of EU or UK regions and key custody |
| New UK transfer test in force and ICO guidance updated | Update transfer risk assessment template |
| New high-risk classification guidance from the Commission | Revisit gate tiering |
| Data Act switching charges removed (12 January 2027) | Revisit exit-cost assumptions for in-scope services |

## 9. Limits of this note

It covers only data protection, transfers, the Data Act switching rules and the AI Act at summary level. It does not cover sector regulation (for example financial services, health), cyber security legislation, employment law, intellectual property in AI outputs, consumer law or competition law. It is a point-in-time summary and may be out of date by the time you read it.
