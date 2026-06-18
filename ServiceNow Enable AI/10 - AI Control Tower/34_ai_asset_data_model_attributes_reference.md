# AI Asset Data Model Attributes — Reference
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Topic 34 of 35 | Role: AI Risk & Compliance Officer Reference

---

## What Is This?

This is the complete, standalone reference for the AI asset data model attributes — the extended attribute set for each of the four AI asset types across both the CMDB product model layer and the digital asset layer. These attributes define what information AICT can store about each asset type, forming the governance data schema for the entire AI inventory.

For how these attributes are populated during asset creation, see Topic 18 (Creating AI Assets). For the table names where these attributes are stored, see Topic 33 (Tables Installed).

---

## Data Model Architecture

Each AI asset type has two record layers:

```
CMDB Product Model Layer (cmdb_ai_*_product_model)
    └── Configuration / product information about the asset
    └── Used for CMDB impact analysis and ITOM integration

Digital Asset Layer (alm_ai_*_digital_asset)
    └── Governance, lifecycle, and operational record
    └── This is the AICT-managed record you work with in the workspace

Shared Layer (Information Asset)
    └── Data classification — applies to all asset types
```

---

## AI Model Attributes

### CMDB Product Model (`cmdb_ai_model_product_model`)

> "Product Information for the AI model that is used by the AI system to generate responses without human intervention."

| Attribute | Description | Governance Relevance |
|---|---|---|
| **Model parameters info** | Number of parameters for the model | Scale indicator — larger models have greater capability and risk surface |
| **Supported languages** | Languages the model supports | Scope of use; localization risk; out-of-scope language use is a governance gap |
| **Model size** | Size of the model in MB — primarily for internally developed/deployed models | Infrastructure planning and operational dependency documentation |
| **Deployment guidelines** | Instructions for deployment — primarily for internally developed/deployed models | Standard operating procedure reference for operations teams |
| **Source** | Links or details of the model source — examples: Hugging Face, Microsoft | Provenance tracking; vendor identification for third-party risk |
| **Training procedure** | Type of training used | See training procedure options below |
| **Context window** | Size of input sequences the model can handle (number of tokens) | Operational limit; affects data exposure risk (more context = more data per call) |

**Training procedure options (all values):**
- Decision Trees
- Deep Neural Networks
- Linear Regression
- Logistic Regression
- Random Forest
- Supervised Learning
- Unsupervised Learning
- Reinforcement Learning
- Transfer Learning
- Semi-Supervised Learning
- Instruction Finetuning
- Supervised Finetuning

> **Risk Officer Note — Training Procedure and Explainability:** The training procedure directly determines explainability. Decision Trees and Linear/Logistic Regression produce inherently interpretable models. Deep Neural Networks, Reinforcement Learning, and Transfer Learning are opaque — they produce accurate outputs but cannot easily explain why. The EU AI Act's requirements for transparency and human oversight are harder to meet for opaque models. For high-risk AI systems (clinical decision support, credit decisions, employment AI), document the training procedure and assess whether the explainability level is sufficient for the regulatory context.

---

### Digital Asset (`alm_ai_model_digital_asset`)

| Attribute | Description | Governance Relevance |
|---|---|---|
| **Base model** | This AI model was derived from an internal model developed within the organization | Provenance chain — risks of base model propagate to derived models |
| **Model weights info** | Additional model information if available — primarily for internally developed models | Technical documentation for internal model governance |
| **Required infrastructure** | Documentation of infrastructure requirements for deployment — primarily for internal models | Operational dependency documentation |
| **Training dataset** | Reference to one or more datasets used to train the model — primarily for internally developed models | Bias and fairness traceability; the origin point of model behavior |
| **Evaluation dataset** | Reference to one or more datasets used to evaluate the model | Performance validation evidence |
| **Evaluation metrics report** | Links or details of evaluation results | Documented evidence of accuracy, bias, and performance assessment |
| **License details** | Link or detail to applicable licenses | IP and usage obligation tracking; open-source license compliance |
| **Model card** | Links to shareable model card — internal and external | Primary transparency document for the model |

> **Risk Officer Note — Model Card:** A model card is the governance transparency artifact for an AI model. It should contain: intended use cases, out-of-scope uses, training data description, evaluation results across demographic groups, known limitations and failure modes, and ethical considerations. For any model used in patient-facing applications, a model card is not optional — it is the evidence base for the risk assessment. A model without a model card should not be approved for production in a regulated environment.

> **Risk Officer Note — Base Model:** If a model is derived from a base model (e.g., fine-tuned on a foundation model), the risks of the base model are inherited. Document this relationship and include an assessment of inherited risks from the base model when conducting the risk assessment of the derived model.

---

## AI Dataset Attributes

### CMDB Product Model (`cmdb_ai_dataset_product_model`)

> "Product Information for the collection of data that is used to train and test AI models."

| Attribute | Description | Governance Relevance |
|---|---|---|
| **Data type** | Type of data in the dataset — examples: Text, Image, Video, Table | Data classification and processing risk type |
| **Source** | Links or details of the data source — examples: Customer, Wikipedia, Hugging Face, Crowd sourced | Provenance; consent chain; vendor risk |
| **Acceptable usage** | Acceptable usage according to license/contract — examples: Training, Evaluation | **Contractual constraint** — must be honored; using a dataset beyond its declared acceptable usage is a license violation |

> **Risk Officer Note — Acceptable Usage:** This field is a contractual governance boundary. A dataset licensed for "Evaluation" only cannot legally be used for "Training" without violating the data provider's terms. When a model is linked to a dataset during asset creation, the AI steward must verify that the intended use (Training or Evaluation) matches the dataset's Acceptable usage declaration. Misuse = license violation = legal exposure.

---

### Digital Asset (`alm_ai_dataset_digital_asset`)

| Attribute | Description | Governance Relevance |
|---|---|---|
| **Base datasets** | This version of the AI dataset was derived from a previous version | Derived data provenance chain |
| **Dataset card** | Information on record count, distribution; documentation for data quality, known risks and limitations | Primary transparency document for the dataset |
| **License details** | Link or detail to applicable licenses — examples: CommonCore, Apache 2.0 | Open-source and commercial license compliance |

> **Risk Officer Note — Dataset Card:** A dataset card should document: total record count, demographic distribution (critical for bias assessment), data collection methodology, labeling methodology if applicable, known biases or representation gaps, and data quality issues. For healthcare datasets specifically, the card must also include: patient consent status, de-identification methodology applied, applicable regulations (HIPAA, GDPR if EU patients), and data retention policy. A dataset card is the minimum documentation for any dataset used in a production AI system.

---

## AI Prompt Attributes

### CMDB Product Model (`cmdb_ai_prompt_product_model`)

| Attribute | Description |
|---|---|
| **Documentation** | Links and information about requirements, design, and related information |

---

### Digital Asset (`alm_ai_prompt_digital_asset`)

| Attribute | Description | Governance Relevance |
|---|---|---|
| **Prompt information** | Details of the prompt — the actual prompt text or instructions | The governed artifact itself; must be version-controlled |
| **AI model** | Reference to the AI model for which the prompt is created | Scopes the prompt to its intended model |

> **Risk Officer Note — Prompt Information:** The prompt information field contains the actual system prompt or instructions. This is a policy document, not just configuration. Changes to system prompt text change what the AI system does — its behavior, its constraints, its persona. Any change to prompt information after an asset has been approved should trigger a change request workflow. Treat prompt text with the same version control discipline as software code in a regulated environment.

---

## AI System Attributes

### CMDB Product Model (`cmdb_ai_system_product_model`)

> "Product Information for software that provides ML/AI capability to generate outputs, such as decisions, recommendations, content, or predictions."

| Attribute | Description |
|---|---|
| **Documentation** | Links and information about requirements, design, and related information |

---

### Digital Asset (`alm_ai_system_digital_asset`)

| Attribute | Description | Governance Relevance |
|---|---|---|
| **AI models** | Reference to one or more associated models | M2M relationship — the model-to-system dependency chain |
| **Evaluation Dataset** | Reference to one or more associated datasets used for evaluation | Evidence that the system was tested with appropriate data |
| **Evaluation Metrics Report** | Details of evaluation results | Performance evidence — the documented output of system testing |

---

## Shared Attributes (All Asset Types)

### Information Asset Layer

| Attribute | Description | Governance Relevance |
|---|---|---|
| **Data classification** | Classification per organization's data classification model — examples: Public, Confidential, Customer Confidential | Bridges AI governance with enterprise data governance |

> **Risk Officer Note — Data Classification:** This field should align with your organization's information classification scheme. For healthcare, add PHI (Protected Health Information) as a classification value if not already present. Every AI asset that processes patient data should be classified at the PHI level. This enables governance reporting filtered by data sensitivity: "How many deployed AI systems process PHI?" is a question you should be able to answer from AICT data alone.

### AI Digital Asset Base Layer

| Attribute | Description |
|---|---|
| **ServiceNow record reference** | Reference to Now Assist record |
| **ServiceNow table** | Now Assist table |

---

## Complete Attribute Coverage Matrix

| Attribute | AI System | AI Model | AI Dataset | AI Prompt |
|---|---|---|---|---|
| Associated models (M2M link) | ✓ | — | — | — |
| Evaluation dataset reference | ✓ | ✓ | — | — |
| Evaluation metrics report | ✓ | ✓ | — | — |
| Training dataset reference | — | ✓ | — | — |
| Base model (provenance) | — | ✓ | — | — |
| Model weights info | — | ✓ | — | — |
| Required infrastructure | — | ✓ | — | — |
| License details | — | ✓ | ✓ | — |
| Model card | — | ✓ | — | — |
| Base datasets (provenance) | — | — | ✓ | — |
| Dataset card | — | — | ✓ | — |
| Prompt information | — | — | — | ✓ |
| AI model reference | — | — | — | ✓ |
| Documentation | — | — | — | ✓ |
| Training procedure | — | ✓ (CMDB) | — | — |
| Supported languages | — | ✓ (CMDB) | — | — |
| Context window | — | ✓ (CMDB) | — | — |
| Source | — | ✓ (CMDB) | ✓ (CMDB) | — |
| Data type | — | — | ✓ (CMDB) | — |
| Acceptable usage | — | — | ✓ (CMDB) | — |
| Data classification | ✓ | ✓ | ✓ | ✓ |
| SN record reference | ✓ | ✓ | ✓ | ✓ |

---

## Minimum Governance Documentation Standards

Based on the data model, the following is the minimum documentation standard for a production-ready AI asset record:

**AI System:**
- [ ] Documentation link (design and requirements doc)
- [ ] Linked AI Models (at least one)
- [ ] Evaluation Dataset linked
- [ ] Evaluation Metrics Report documented
- [ ] Data classification set

**AI Model:**
- [ ] Model card linked (mandatory for production)
- [ ] Training dataset linked
- [ ] Training procedure declared
- [ ] Evaluation dataset linked
- [ ] Evaluation metrics report linked
- [ ] License details documented
- [ ] Base model documented (if derived)
- [ ] Data classification set

**AI Dataset:**
- [ ] Dataset card linked (mandatory for production)
- [ ] Data type declared
- [ ] Source documented
- [ ] Acceptable usage declared
- [ ] License details documented
- [ ] Base datasets documented (if derived)
- [ ] Data classification set

**AI Prompt:**
- [ ] Prompt information field populated (the actual prompt text)
- [ ] AI model linked
- [ ] Documentation link
- [ ] Data classification set

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 869–871*
