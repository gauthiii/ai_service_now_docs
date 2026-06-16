# Definitions of AI Asset Inventory
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Role: AI Risk & Compliance Officer Reference

---

## What Is This?

The AI asset inventory is the foundational **registry of all AI components** in an organization. It is the single source of truth for what AI exists, what it does, what it is made of, and how it relates to other AI components. Every governance, risk, compliance, and security activity in AI Control Tower depends on this inventory being complete and accurate.

This section defines the four core asset types and explains why their inter-dependencies matter for governance.

---

## AI Asset Inventory Overview

> *"The AI Asset Inventory provides a record of all components and their connections that contribute to an AI experience."*

Organizations may choose to manage one or more of these asset types as part of their overall AI governance strategy. The inventory covers:

- **AI systems** — the deployable AI applications and agents
- **AI models** — the trained ML/AI engines powering systems
- **Datasets** — the data used to train and evaluate models
- **Prompts** — the instructions guiding model outputs

> **Risk Officer Note:** "May opt to manage one or more" is intentionally flexible, but from a governance standpoint, managing all four is the only way to achieve complete risk traceability. A risk assessment on an AI system that doesn't account for the model it uses or the dataset it was trained on is an incomplete assessment. The inventory is only as good as its coverage.

---

## Asset Type 1: AI Systems

### Definition
> *"An AI system is a type of computer program designed for performing tasks that typically require human intelligence, such as learning the language, deciding, or recognizing images. Unlike traditional software that operates based on set rules, AI systems learn from data, adapt their actions, and can decide on their own."*

### Key Characteristics
- **Adaptive** — learns from data rather than following fixed rules
- **Autonomous** — can make decisions without explicit human instruction at runtime
- **Consequential** — outputs or behaviors aren't always predetermined by the developer or user
- Can operate with **different levels of autonomy**, from fully human-directed to fully autonomous

### Hierarchical AI Systems
AI systems can be interconnected:
- One system may depend on the outputs of another → called a **sub AI system**
- This creates **parent-child relationships** in the inventory
- Recognizing these connections is critical for monitoring usage and clarifying accountability

**Example hierarchy:**
```
AI Issue Resolution Agent (parent)
├── Issue Summarization (sub AI system)
└── Owner Mapping (sub AI system)
```

### What About Tools?
Tools are **attributes** of an AI system or sub AI system — NOT separate AI assets.

| Tools Are | Tools Are NOT |
|---|---|
| Attributes of AI systems | Separate tracked AI assets |
| Relevant for agentic AI use cases | Subject to their own lifecycle in AICT |
| Linked during discovery from cloud platforms | Governed independently |

Tools are discovered and linked to AI systems via cloud platforms (Azure Foundry, AWS) or internal discovery processes. They appear in the inventory as attributes, not as standalone governed entities.

> **Risk Officer Note:** The distinction between AI systems and tools is governance-critical. In agentic AI architectures (like CareAtlas agents), an agent may use 10+ tools. Those tools are not individually governed — only the agent (AI system) is. This means your risk assessment on an agent must account for **all the tools it can invoke**, even though those tools don't have their own lifecycle records. Failure to document tool-level capabilities in the AI system record creates a governance blind spot.

### Examples of AI Systems
| AI System | Function |
|---|---|
| Spam filter in Gmail | Determines whether emails are spam |
| Netflix recommendation engine | Suggests shows based on viewing patterns |
| Self-driving car software | Makes driving decisions |
| ChatGPT-style chatbot | Responds to questions |
| AI Issue Resolution Agent | Orchestrates sub-agents for issue summarization and owner mapping |

### Real-World Governance Example (Banking/Finance)
The documentation uses a **credit scoring system** as the canonical governance example:
- An AI system generates credit scores for loan approvals
- It is fed data from multiple LLMs: Now LLM (financial info, payment history), OpenAI (bankruptcy filings, court judgments), Azure OpenAI (spending/saving patterns)
- AICT + AIRC together ensure compliance and responsible usage at creation, build, and deployment stages

> **Risk Officer Note:** This example is directly applicable to healthcare AI. Replace "credit scoring" with "patient risk stratification" or "clinical decision support" and the governance requirements are analogous — multiple data sources, consequential decisions, regulatory oversight requirements, and need for bias and fairness controls.

---

## Asset Type 2: AI Models

### Definition
> *"An AI model acts as the 'brain' of an AI system. It learns from previous data and applies that knowledge to make predictions, respond to questions, or identify patterns."*

### Training Techniques Tracked
Models are developed using:
- **Supervised learning** — trained on labeled data
- **Unsupervised learning** — identifies patterns without labels
- **Reinforcement learning** — learns through trial and reward

### Why Models Matter for Governance
> *"Learning which models power your AI systems is important for monitoring their accuracy, fairness, and potential risks."*

A model is the source of:
- **Accuracy risks** — model may produce incorrect predictions
- **Fairness/bias risks** — training data or algorithm may embed bias
- **Privacy risks** — model may memorize and leak training data
- **Drift risks** — model performance degrades over time as data distribution shifts

### Examples of AI Models
| Model | Function |
|---|---|
| Spam detection model | Flags emails as spam |
| Language model (ChatGPT) | Generates text responses |
| Image recognition model | Recognizes objects in photos |
| Credit scoring model | Predicts likelihood of loan default |

> **Risk Officer Note:** In AICT, models are tracked in `alm_ai_model_digital_asset` and `cmdb_ai_model_product_model`. When a model is updated or replaced, the linked AI systems should be re-assessed for risk, because the model change may alter behavior, accuracy, or fairness characteristics. Establish a change control process: any model update triggers a new risk assessment on all dependent AI systems.

---

## Asset Type 3: Prompts

### Definition
> *"A prompt is a question or instruction provided to an AI system, indicating what you want it to accomplish."*

More formally (from the asset inventory definition):
> "Any data, including text or images, that is used to guide, instruct, or influence an AI model's output."

### Types of Prompts
1. **User prompts** — input from end users at runtime
2. **System prompts** — pre-configured instructions embedded in the AI system design
3. **Structural prompts** — elements in a process requiring user input before output

### Why Prompts Matter for Governance
> *"Certain AI systems, such as GenAI systems, require user prompts to function. Monitoring prompts can help analyze user interactions with the AI and the types of outputs produced."*

Prompts are:
- **Security-sensitive** — prompt injection attacks manipulate prompts to override intended behavior
- **Compliance-relevant** — system prompts may contain policy constraints that must be version-controlled
- **Privacy-relevant** — user prompts may contain PII that must be detected and handled

### Examples of Prompts
| Prompt | Output |
|---|---|
| "Write a poem about the moon" | AI-generated poem |
| "Translate 'hello' into Spanish" | "Hola" |
| "Show red dresses under $50" | Filtered e-commerce results |
| "Summarize this email" | Short summary |

### Sync Logic for Prompts
Prompts are tracked from source table `sys_generative_ai_config`:
- Target tables: `alm_ai_prompt_digital_asset`, `cmdb_ai_prompt_product_model`
- Fields tracked: `active`, `prompt`, `model`, `name`, `version`
- Records included: Active prompts with active model and linked skill

> **Risk Officer Note:** System prompts are your primary prompt governance asset. They define what the AI is allowed and instructed to do. They should be treated like policy documents: version-controlled, reviewed by the compliance team, and audited for changes. A change to a system prompt without governance review is equivalent to changing a business rule without change management — it creates uncontrolled behavior.

---

## Asset Type 4: Datasets

### Definition
> *"A dataset is a collection of data used to train or evaluate an AI model. You can think of it as a large spreadsheet with rows representing examples and columns for features or labels. Datasets can also come in other formats, such as images, audio, or video."*

### Why Datasets Matter for Governance
> *"Mapping datasets within the AI Control Tower is important for tracking data sources, ownership, and other key details, making it a vital part of the organization's AI governance program."*

Datasets are the **origin point of AI risk**:
- **Bias** — if training data is unrepresentative, the model inherits the bias
- **Privacy** — training data may contain PII, PHI, or confidential information
- **Provenance** — knowing where data came from is required for regulatory compliance
- **Consent** — data used for training may have consent requirements
- **Quality** — poor quality training data produces poor model performance

### Examples of Datasets
| Dataset | Use Case |
|---|---|
| Labeled images (dogs, cats) | Training image recognition model |
| Articles and books | Training a language model |
| Customer purchase history | Training recommendation engine |
| Medical records | Training clinical diagnosis tools |

### Sync Logic for Datasets
Datasets tracked from source table `sys_one_extend_test_dataset`:
- Target tables: `alm_ai_dataset_digital_asset`, `cmdb_ai_dataset_product_model`
- Fields tracked: `status`, `parent`, `name`, `description`
- Records included: Published datasets where `eval_run = true`

> **Risk Officer Note:** Medical record datasets (as in CareAtlas) are among the highest-risk datasets in any organization. They are subject to HIPAA, and potentially GDPR if patients are EU residents. Before any dataset is linked to a model or system in AICT, confirm: (1) data classification level, (2) consent status, (3) data residency, (4) anonymization/de-identification status, (5) retention policy. These should be documented as dataset attributes in AICT.

---

## Inter-Dependencies: Why They Matter

> *"An AI system operates as part of a larger framework, closely connected to the AI model powering its capabilities and the datasets that shape its behavior. While these elements are interrelated, each plays a unique role and should be clearly identified to confirm effective governance."*

> *"Overlooking any aspect, such as the training dataset or the model supporting an AI feature can result in incomplete risk assessments, audit challenges, or compliance issues."*

### The Governance Chain
```
Dataset → (trains) → Model → (powers) → AI System → (uses) → Prompt
```

Each link in this chain must be:
- **Inventoried** in AICT
- **Assessed for risk** independently
- **Linked** to show the dependency
- **Traceable** for audit purposes

### Required Governance Actions per Inter-Dependency
> "Comprehensive responsible AI governance requires attention to all these components:
> - Inventory for each AI system
> - Identify the associated AI model
> - Document the dataset"

### Risk Propagation Through the Chain
| Upstream Issue | Downstream Impact |
|---|---|
| Biased training dataset | Biased model → biased AI system decisions |
| Non-consented data in dataset | Privacy violation propagated to model and system |
| Model accuracy degradation | AI system makes poor decisions |
| Model security vulnerability | AI system is exploitable |
| Prompt injection in user prompt | AI system behaves contrary to intended policy |

> **Risk Officer Note:** The inter-dependency chain means risk assessments must be **chain-aware**. When assessing a deployed AI system, you must also assess the model it uses and the dataset that trained the model. If any link in the chain has an unacceptable risk, the entire chain is at risk. AICT's relationship mapping (the M2M tables) is what makes this chain-aware assessment possible — but only if the relationships are actually populated.

---

## Now Assist AI Asset Discovery — Auto-Sync

AICT automatically synchronizes ServiceNow-native AI assets into the inventory. Understanding this sync is critical for knowing what is automatically in your inventory vs. what requires manual entry.

### Sync Logic for AI Systems (Skills)
Source: `sn_nowassist_skill_config`
Targets: `alm_ai_system_digital_asset`, `cmdb_ai_system_product_model`

**Inclusion rules:**
- Default skills: included if Active
- Custom skills: included if Active, OR if state = Published

**State mapping:**

| Source State (Now Assist skill) | Target State (AI System in AICT) |
|---|---|
| Active | Deployed |
| Published or Draft | In Development |
| Retired | Retired |
| Deleted | No update made |

### Complete Asset Sync Mapping Table

| Asset Type | Source Table | Target Tables | Key Fields Tracked | Inclusion Criteria |
|---|---|---|---|---|
| **Models** | `sys_generative_ai_model_config` | `alm_ai_model_digital_asset`, `cmdb_ai_model_product_model` | active, max_tokens, model, supported_languages, domain_id | Active = true |
| **Datasets** | `sys_one_extend_test_dataset` | `alm_ai_dataset_digital_asset`, `cmdb_ai_dataset_product_model` | status, parent, name, description | Published = true, eval_run datasets |
| **Skills** | `sn_nowassist_skill_config` | `alm_ai_system_digital_asset`, `cmdb_ai_system_product_model` | active, datasets, prompts, model, sys_created_by, domain_id, name, description | Active or Published (custom); non-platform skills only |
| **Prompts** | `sys_generative_ai_config` | `alm_ai_prompt_digital_asset`, `cmdb_ai_prompt_product_model` | active, prompt, model, name, version | Active prompts with active model and linked skill |
| **Tools** | `sn_aia_tool` | `sn_ent_ai_tool` | name, description, type, active, sys_created_by, domain_id | All |
| **AI Agents** | `sn_aia_agent` | `alm_ai_system_digital_asset`, `cmdb_ai_system_product_model` | name, description, role, instructions, sys_created_by, domain_id | Active = true |
| **Agent Tool Mapping** | `sn_aia_agent_tool_m2m` | `sn_ent_ai_system_subcomponent_m2m` | agent-tool mapping | All agent-tool mappings |
| **Agent Use Cases** | `sn_aia_usecase` | `alm_ai_system_digital_asset`, `cmdb_ai_system_product_model` | name, description, sys_created_by, domain_id | Active = true |
| **Usecase-Agent Mapping** | `sn_aia_team_member` | `sn_ent_ai_system_subcomponent_m2m` | usecase-agent mapping | All usecase-agent mappings |

> **Risk Officer Note:** The auto-sync means your AI inventory self-populates from the Now Platform. However, **"Deleted" skills do not update** — if a skill is deleted from Now Assist without being retired first, the AICT record becomes stale. Establish a decommissioning policy: always retire before deleting. Also note that third-party AI systems (non-ServiceNow) are NOT auto-synced — they require Enterprise AI discovery (Service Graph Connectors) or manual entry.

---

## View AI Asset Details — Field Reference

When viewing an AI asset record in AICT (`Workspaces > AI Control Tower > AI assets`), the following key fields are tracked:

| Field | Description |
|---|---|
| Version | Version number of the asset |
| Type | Asset type (AI system, model, dataset, prompt) |
| Provider | Who built the asset |
| Vendor | Who sold the asset |
| Department | Department where asset is allocated |
| Managed by | Asset owner |
| License details | License information |
| Supported locations | Locations where this asset is authorized for use |
| Lifecycle phase | New / Assess / Build and test / Deploy / Offboarding |
| Lifecycle status | Current governance status |

---

## Key Takeaways for AI Risk & Compliance Officers

1. The **four asset types** (systems, models, datasets, prompts) are all required for complete governance — partial coverage means incomplete risk assessments.
2. **Tools are attributes, not assets** — but they still represent attack surface and capability scope; document them at the AI system level.
3. **Hierarchical AI systems** (parent-child) require the dependency chain to be mapped; a risk in a sub-system propagates to the parent.
4. **Inter-dependencies are governance-critical** — a biased dataset propagates bias through the model to the system; risk tracing requires all three to be inventoried and linked.
5. **Auto-sync covers ServiceNow-native assets** — third-party assets require Enterprise AI discovery or manual entry; know the gap between your auto-synced inventory and your actual AI footprint.
6. **Deleted skills ≠ retired assets** — establish a retirement-before-deletion policy to maintain inventory accuracy.
7. **Dataset governance in healthcare** is highest-risk — document data classification, consent, residency, and anonymization status as mandatory dataset attributes.

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 774–780*
