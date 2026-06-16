# Inter-dependencies of AI Assets
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Role: AI Risk & Compliance Officer Reference

---

## What Is This?

Inter-dependencies describes the structural relationships between the four AI asset types — AI systems, AI models, and datasets (with prompts as a modifying layer) — and why those relationships are not optional governance artifacts. They are the backbone of complete AI risk assessment, meaningful audits, and regulatory compliance. Overlooking even one element in the chain creates governance blind spots that cannot be patched retroactively.

---

## The Core Principle

> *"An AI system operates as part of a larger framework, closely connected to the AI model powering its capabilities and the datasets that shape its behavior. While these elements are interrelated, each plays a unique role and should be clearly identified to confirm effective governance."*

> *"Overlooking any aspect, such as the training dataset or the model supporting an AI feature, can result in incomplete risk assessments, audit challenges, or compliance issues."*

These two statements define the governance mandate. Inter-dependency mapping is not optional — it is the prerequisite for meaningful risk management.

---

## The Dependency Chain

```
Dataset(s)
    |
    v trains
AI Model(s)
    |
    v powers
AI System (deployed agent/application)
    |
    v guided by
Prompts (system + user)
    |
    v uses
Tools (attributes of the system — NOT separate governed assets)
```

Each element in this chain plays a distinct and non-interchangeable role:

| Element | Role in the Chain | Primary Risk Dimension |
|---|---|---|
| **Dataset** | Shapes model behavior by providing training signal | Bias, privacy, provenance, consent, quality |
| **AI Model** | The computational "brain" — makes predictions, generates outputs | Accuracy, fairness, drift, security vulnerabilities |
| **AI System** | The deployed application that uses the model | Autonomy level, scope of decision-making, consequences |
| **Prompts** | Instructions that guide model outputs at runtime | Prompt injection, policy drift, version control |
| **Tools** | Functions the system can call to take actions | Scope creep, least-privilege violations, attack surface |

---

## Three Mandatory Governance Actions

The documentation states three required actions for comprehensive responsible AI governance:

1. **Inventory for each AI system** — every deployed AI system must be registered in AICT
2. **Identify the associated AI model** — which model powers this system? Link it explicitly.
3. **Document the dataset** — what data trained and evaluates this model? Record provenance.

> **Risk Officer Note:** These three actions are minimum governance standards. An AI system in AICT with no linked model and no linked dataset is an incomplete record — it cannot be meaningfully assessed for risk because the origin of its behavior is unknown. Treat unlinked AI system records as open governance findings.

---

## Canonical Example: Credit Scoring (Applicable to Healthcare)

The documentation uses a credit scoring AI system to illustrate the dependency chain. This maps directly to healthcare AI like CareAtlas:

**Credit scoring context:**
- AI System: Loan Approval Decision System
  - Now LLM: financial info, payment history
  - OpenAI: bankruptcy filings, court judgments
  - Azure OpenAI: spending and saving patterns

**Healthcare equivalent (CareAtlas):**
- AI System: Patient Risk Stratification Agent
  - Clinical NLP Model: patient notes, diagnosis history
  - Lab Results Model: lab values, trends
  - Medication Model: prescriptions, adherence patterns

In both cases: the AI system makes consequential decisions affecting real people, multiple models and data sources feed into the decision, and each model-data combination introduces independent risks that must be assessed.

---

## Risk Propagation Through the Chain

| Upstream Event | How Risk Propagates | Downstream Impact |
|---|---|---|
| Biased or unrepresentative training data | Model learns discriminatory patterns | AI system makes biased decisions |
| PII/PHI in training dataset without proper handling | Model memorizes sensitive data | AI system can leak patient or customer information via outputs |
| Non-consented data used for training | Regulatory violation at dataset level | Entire model and all dependent systems are non-compliant |
| Model accuracy degrades (drift) | System outputs increasingly unreliable predictions | Consequential wrong decisions at scale |
| System prompt modified without governance review | AI system behavior changes without change management | Uncontrolled, untested behavior in production |
| Tool with excessive permissions linked to system | AI agent can take actions beyond intended scope | Unauthorized access, data exfiltration, unintended side effects |

> **Risk Officer Note:** When a dataset is flagged for a privacy issue, the first action is not just to quarantine the dataset — it is to identify every model trained on that dataset and every AI system using those models. AICT's M2M relationship tables (`sn_ent_ai_system_subcomponent_m2m`) are the technical mechanism for this impact analysis. They must be populated for this analysis to be possible.

---

## The M2M Relationship Tables

AICT tracks inter-dependencies through many-to-many (M2M) relationship tables:

| Relationship | Table | What It Links |
|---|---|---|
| Agent to Tool | `sn_ent_ai_system_subcomponent_m2m` | Which tools an agent/system uses |
| Agent to Sub-agent | `sn_ent_ai_system_subcomponent_m2m` | Parent-child AI system hierarchy |
| Use case to Agent | `sn_ent_ai_system_subcomponent_m2m` | Which use cases deploy which agents |
| System to Model | Via `cmdb_ai_system_product_model` | Which model powers which system |
| Model to Dataset | Via `cmdb_ai_model_product_model` | Which dataset trained which model |

> **Risk Officer Note:** These tables are auto-populated by the Now Assist sync for ServiceNow-native assets. For third-party assets discovered via Service Graph Connectors, relationship population depends on what the connector retrieves. Always verify relationship completeness after a discovery run — empty relationships on a complex AI system are a data quality gap.

---

## Hierarchical AI Systems: Sub-System Dependencies

AI systems can be nested — a parent AI system uses sub AI systems as components:

```
Parent: AI Issue Resolution Agent
  Sub-system: Issue Summarization (receives incident, returns summary)
  Sub-system: Owner Mapping (takes summary, identifies responsible owner)
```

**Governance implications of hierarchy:**
- Each sub-system is a separately governed AI asset with its own lifecycle and risk classification
- The parent system's risk assessment must account for the combined risk of all sub-systems
- If a sub-system is retired or replaced, the parent system must be re-assessed
- Access controls on the parent do not automatically apply to sub-systems

> **Risk Officer Note:** A CareAtlas orchestrator agent that calls five sub-agents is five separate AI systems plus the orchestrator — six governance records, potentially six risk assessments, six lifecycle records. An orchestrator assessed in isolation, without assessing its sub-agents, produces a meaningless risk score.

---

## Tools: The Invisible Governance Gap

Tools occupy a unique and governance-challenging position:

- Tools are functions an AI agent can invoke (search, write, delete, call APIs)
- Tracked in AICT as attributes of the AI system (`sn_ent_ai_tool`)
- NOT separately governed assets — no independent lifecycle
- Do NOT go through the AI asset lifecycle (Assess → Build & Test → Deploy)
- Do NOT have their own risk classification
- ARE captured in the inventory during discovery

**The governance risk:** An AI agent record may show "Low" risk — but if that agent has a tool that can delete patient records, the effective risk is "High." The risk classification is only as good as the tool-level risk consideration embedded in the AI system's risk assessment.

> **Risk Officer Note:** Your risk assessment questionnaire for AI systems must explicitly enumerate all tools the system can invoke and assess the risk of each tool at the system level. This is the most common governance gap in agentic AI assessments.

---

## Practical Governance Checklist for Inter-Dependencies

**For every AI System:**
- [ ] Is there at least one linked AI Model?
- [ ] Is there at least one linked Dataset for each model?
- [ ] Are all tools enumerated in the system record?
- [ ] Are sub-systems identified and separately registered?
- [ ] Are M2M relationship records populated?
- [ ] Has the risk assessment accounted for all models, datasets, and tool capabilities?

**For every AI Model:**
- [ ] Is the model linked to the AI systems that use it?
- [ ] Is the training dataset linked?
- [ ] Has the model been assessed for bias, drift, and accuracy?

**For every Dataset:**
- [ ] Is the dataset linked to the models trained on it?
- [ ] Is data provenance documented (source, collection date, collection method)?
- [ ] Is consent status documented?
- [ ] Is data classification (PII, PHI, confidential) documented?
- [ ] Is a data retention and deletion policy documented?

---

## Key Takeaways for AI Risk & Compliance Officers

1. **Inter-dependencies are not optional metadata** — they are the audit trail and impact analysis foundation.
2. **Risk propagates upstream to downstream** — a compromised dataset compromises its models and all systems using those models.
3. **Unlinked assets = incomplete records = invalid risk assessments** — treat broken relationships as open findings.
4. **Hierarchical systems require hierarchical governance** — every sub-system is a separate governance subject.
5. **Tools carry undisclosed risk at the system level** — the tool list must be part of every AI system risk assessment.
6. **M2M tables are the technical backbone** — verify they are populated after every discovery run and every manual asset creation.

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 776–778*
