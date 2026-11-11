# Glossary

Definitions are practical and specific to this repository. They are not legal definitions.

**Adequacy decision / adequacy regulations.** A formal finding by the European Commission (EU) or the UK Government (UK) that a country or framework gives personal data protection judged sufficient, so transfers can proceed without additional safeguards. Can be amended or withdrawn.

**ADR (architecture decision record).** A short document recording one significant decision: context, options, the choice and its consequences. This repository uses the MADR format.

**Agent.** Software that uses a model to plan and take multi-step actions, usually by calling tools. See *tool gateway*.

**AI gateway.** An internal service through which applications reach models, applying routing, quotas, redaction and logging. The main control for swapping models.

**AI governance gate.** A review step that a new AI use case passes before production, with evidence proportionate to risk.

**Annex I, Annex III (EU AI Act).** Annex I lists EU product-safety legislation under which AI components can make a system high-risk. Annex III lists use-case areas (for example employment, education, access to essential services) that are high-risk.

**Break-glass account.** An emergency administrative account that does not depend on normal sign-in infrastructure, stored securely, monitored, and used only when other access fails.

**CLOUD Act.** US law (Clarifying Lawful Overseas Use of Data Act, 2018) that includes provisions on US legal process applying to providers in respect of data in their possession, custody or control, wherever stored.

**Confidential computing.** Hardware-based techniques that protect data while it is being processed. Useful in some cases, with their own assumptions and limits.

**Crypto-shredding.** Making data unreadable by destroying or revoking the keys that protect it. Works only if every copy, including backups, uses keys covered by the action.

**Customer-managed key (CMK) / bring your own key (BYOK).** A model in which the customer controls encryption keys, typically in the provider's key management service. Differs from *hold your own key*.

**Data Act (EU).** Regulation (EU) 2023/2854 on fair access to and use of data, including rules on switching between data processing services.

**Data bridge (UK-US).** Common name for the UK Extension to the EU-US Data Privacy Framework, which allows transfers from the UK to certified US organisations that opted in.

**Data protection test.** The standard in the UK's international transfer framework, as amended by the Data (Use and Access) Act 2025: protection "not materially lower" than under UK law.

**Data residency.** Where data is stored and processed. Different from *jurisdiction exposure*.

**DPIA (data protection impact assessment).** A structured assessment of risks to individuals from processing, required in certain circumstances under UK and EU GDPR.

**DUAA.** Data (Use and Access) Act 2025, which amends the UK GDPR and Data Protection Act 2018.

**Egress.** Data leaving a provider's network, or the network traffic that carries it. May be charged.

**Embedding.** A numeric representation of content (text, images) used for semantic search. See *vector store*.

**Envelope encryption.** A design in which data is encrypted with data keys, and the data keys are encrypted with a master key held in a key management service.

**Exit plan.** A written plan for leaving a platform: scope, target, sequence, dependencies, time and cost.

**GPAI (general-purpose AI) model.** A model, such as a large language model, capable of serving many tasks. The EU AI Act sets duties on its providers.

**Hold your own key (HYOK).** A model in which the provider calls a key service operated outside its control. Strongest separation, most availability risk.

**IDTA.** International Data Transfer Agreement, the ICO's standard transfer contract for restricted transfers from the UK.

**Identity provider (IdP).** The service that authenticates users and issues identity assertions to applications.

**Jurisdiction exposure.** The extent to which legal systems can compel access to data or services, based on where the supplier and its group are established and where data and operations sit.

**KMS (key management service).** A service that creates, stores and controls the use of cryptographic keys.

**Lock-in.** The cost, time or risk of leaving a supplier or technology. Present to some degree in every choice. The aim is to know its size, not to eliminate it.

**MADR.** Markdown Architectural Decision Records, a lightweight ADR format.

**Model registry.** A record of models and prompts with versions, owners, licences, evaluation results and deprecation dates.

**Open-weight model.** A model whose trained parameters are published for download. Licence terms vary and may restrict use. Not necessarily open source.

**OpenTelemetry.** A vendor-neutral standard and toolset for collecting traces, metrics and logs.

**Outbox pattern.** A design in which a service writes events to a table in the same transaction as its data change and a separate process publishes them, avoiding lost or duplicated events without a streaming platform.

**Portability test.** A scheduled exercise that exports data from a platform, loads it elsewhere and checks that it is complete and usable.

**Prompt injection.** Manipulating a model through instructions hidden in content it reads, to make it ignore its intended behaviour.

**Proportionality.** Applying controls in line with the risk and impact, rather than uniformly.

**RAG (retrieval-augmented generation).** Supplying a model with retrieved content from your own sources to ground its answers.

**SCIM.** System for Cross-domain Identity Management, a standard for provisioning users and groups across systems.

**SCCs (standard contractual clauses).** Standard EU contract terms for transfers of personal data. UK organisations use the UK Addendum or the IDTA.

**Sovereignty (as used here).** The degree of control an organisation retains over its digital capabilities, considered through data location, operational control, legal jurisdiction exposure and portability. A spectrum with trade-offs, not a state.

**Sub-processor.** A third party engaged by a processor to process personal data on behalf of the controller.

**Tool gateway.** A control point that mediates every tool call an agent makes, with allow-lists, scopes and validation.

**Transfer risk assessment.** An assessment of whether a transfer to a particular destination, under a particular mechanism, gives adequate protection in practice.

**UK Extension.** See *data bridge*.

**UK GDPR.** The UK's retained and amended version of the EU General Data Protection Regulation, which operates alongside the Data Protection Act 2018.

**Vector store.** A database or index that stores embeddings and supports similarity search.

**Workload identity.** An identity issued to software (a service, pipeline or agent) rather than a person, ideally with short-lived credentials.
