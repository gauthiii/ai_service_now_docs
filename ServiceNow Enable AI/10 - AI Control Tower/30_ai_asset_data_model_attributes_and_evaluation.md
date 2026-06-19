# AI Asset Data Model Attributes & Evaluation Dashboard References
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Role: AI Risk & Compliance Officer Reference

---

## What Is This?

This document covers the final two reference sub-sections of the AI Control Tower documentation:

1. **AI asset data model attributes** — the extended attribute set for each AI asset type in the CMDB product model and digital asset tables. This is the schema specification that tells you exactly what fields exist on each asset record, what they mean, and where they map in the database.

2. **Evaluation dashboard references** — the complete technical reference for the evaluation framework including metrics definitions, score calculation methodology, the evaluation execution flow logic, and the batch evaluation flow.

---

## Part 1: AI Asset Data Model Attributes

### Overview

The AI asset data model is organized into two layers:

**CMDB Product Model layer** — stores product/configuration information in the CMDB (these are the CI records)
**Digital Asset layer** — stores the governance and operational record (these are the AICT-managed records)

Each asset type has both a product model record and a digital asset record. The attributes below are organized by this structure.

---

### AI Model Product Model (`cmdb_ai_model_product_model`)

> "Product Information for the AI model that is used by the AI system to generate responses without human intervention."

| Attribute | Description |
|---|---|
| **Model parameters info** | Number of parameters for the model |
| **Supported languages** | Languages supported by the model |
| **Model size** | Size of the model in MB — mostly applicable for models developed and deployed within the organization |
| **Deployment guidelines** | Instructions applicable for models developed and deployed within the organization |
| **Source** | Links or details of source of the model — examples: Hugging Face, Microsoft |
| **Training procedure** | Type of training used. Options: Decision Trees, Deep Neural Networks, Linear Regression, Logistic Regression, Random Forest, Supervised Learning, Unsupervised Learning, Reinforcement Learning, Transfer Learning, Semi-Supervised Learning, Instruction Finetuning, Supervised Finetuning |
| **Context window** | Size of input sequences the model can handle (number of tokens) |

> **Risk Officer Note:** The **Training procedure** field is governance-critical. The type of training used has direct implications for bias and explainability. Decision Trees and Linear Regression are relatively explainable; Deep Neural Networks and Reinforcement Learning are less so. For high-stakes AI systems (clinical decision support, credit scoring), explainability requirements from regulations like the EU AI Act may constrain which training procedures are acceptable. Document this field for all models and use it as an input to risk assessment.

---

### AI Dataset Product Model (`cmdb_ai_dataset_product_model`)

> "Product Information for the collection of data that is used to train and test AI models."

| Attribute | Description |
|---|---|
| **Data type** | Type of data in the dataset. Examples: Text, Image, Video, Table |
| **Source** | Links or details of data source. Examples: Customer, Wikipedia, Hugging Face, Crowd sourced |
| **Acceptable usage** | Acceptable usage of the data according to license/contract. Examples: Training, Evaluation |

> **Risk Officer Note:** The **Acceptable usage** field on the Dataset product model is a contractual and compliance constraint. A dataset licensed for "Evaluation" only cannot legally be used for training without violating the data provider's terms. A dataset sourced from "Customer" data carries consent obligations. These are governance boundaries that must be enforced operationally: when a model is linked to a dataset during asset creation, verify that the intended use matches the dataset's Acceptable usage declaration.

---

### AI Prompt Product Model (`cmdb_ai_prompt_product_model`)

> "Product Information for instructions given to AI models to get a response for AI system."

| Attribute | Description |
|---|---|
| **Documentation** | Links and information about requirements, design, and related information |

> **Risk Officer Note:** The Prompt product model has minimal attributes at the CMDB layer — this reflects that prompts are versioned artifacts rather than complex technical configurations. The governance weight of prompts sits at the Digital Asset layer (prompt information field) and in the version control discipline applied to system prompts. The Documentation attribute should link to the design rationale and requirements document for the prompt.

---

### AI System Product Model (`cmdb_ai_system_product_model`)

> "Product Information for software that provides ML/AI capability to generate outputs, such as decisions, recommendations, content, or predictions."

| Attribute | Description |
|---|---|
| **Documentation** | Links and information about requirements, design, and related information |

---

### Information Asset Attributes

This layer adds data classification to AI assets:

| Attribute | Description |
|---|---|
| **Data classification** | Classification according to organization's data classification model. Examples: Public, Confidential, Customer Confidential |

> **Risk Officer Note:** The Data classification attribute at the Information Asset level is the bridge between the AI governance framework and the broader enterprise data classification scheme. For healthcare, the classification values should align with your information security classification model — adding "PHI" or "Clinical" classifications if they are not already present. Every AI asset that processes Protected Health Information should have Data classification = PHI (or your organization's equivalent). This field enables data-classification-aware governance reporting: "How many deployed AI systems process Confidential or Customer Confidential data?"

---

### AI Digital Asset Attributes (Shared Across All Asset Types)

These attributes apply to the base AI digital asset (`ai_asset`) and are therefore shared across all four AI asset types:

| Attribute | Description |
|---|---|
| **ServiceNow record reference** | Reference to Now Assist record |
| **ServiceNow table** | Now Assist table |

---

### AI System Digital Asset (`alm_ai_system_digital_asset`)

| Attribute | Description | Notes |
|---|---|---|
| **AI models** | Reference to one or more associated models | M2M relationship — links to model digital asset records |
| **Evaluation Dataset** | Reference to one or more associated datasets used for evaluation | M2M relationship |
| **Evaluation Metrics Report** | Details of evaluation results | Documentation link or text field |

---

### AI Model Digital Asset (`alm_ai_model_digital_asset`)

| Attribute | Description | Governance Relevance |
|---|---|---|
| **Base model** | This AI model version was derived from an internal model developed within the organization | Provenance tracking — inherited risks from base model |
| **Model weights info** | Additional model information if available — mostly applicable for models developed within the organization | Technical documentation for internal models |
| **Required infrastructure** | Documentation of infrastructure requirements for model deployment — primarily for models deployed within the organization | Operational dependency documentation |
| **Training dataset** | Reference to one or more associated datasets used for training the model — mostly applicable for models developed within the organization | Bias and fairness traceability |
| **Evaluation dataset** | Reference to one or more associated datasets used for evaluating the model | Performance validation traceability |
| **Evaluation metrics report** | Links or details of evaluation results | Evidence of performance assessment |
| **License details** | Link or detail to applicable licenses applied to the model | IP and usage obligation tracking |
| **Model card** | Links to shareable model card (internal and external) | Primary transparency document |

> **Risk Officer Note:** The **Model card** attribute is the single most important transparency artifact for an AI model. A model card should contain: what the model was designed for, what data it was trained on, known limitations and failure modes, performance metrics across demographic groups (bias evaluation), and appropriate use cases. For any AI model used in patient-facing applications in CareAtlas, a model card is not optional — it is the evidence base for the entire risk assessment. If a vendor does not provide a model card, that is a vendor risk finding.

---

### AI Dataset Digital Asset (`alm_ai_dataset_digital_asset`)

| Attribute | Description | Governance Relevance |
|---|---|---|
| **Base datasets** | This version of the AI dataset was derived from the previous version | Provenance chain for derived datasets |
| **Dataset card** | Information on number of records, distribution; documentation for data quality and known risks and limitations | Primary transparency document for the dataset |
| **License details** | Link or detail to applicable licenses applied to the dataset. Examples: CommonCore, Apache 2.0 | Legal use boundary enforcement |

> **Risk Officer Note:** The **Dataset card** attribute should contain: total record count, data distribution (demographic breakdown if applicable), known biases or representation gaps, data collection methodology, annotation methodology (if labeled), and known limitations. For healthcare datasets, the card should also include: patient consent status, de-identification methodology, and data retention policy. A dataset without a card cannot be meaningfully assessed for bias risk.

---

### AI Prompt Digital Asset (`alm_ai_prompt_digital_asset`)

| Attribute | Description |
|---|---|
| **Prompt information** | Details of the prompt (the actual prompt text or instructions) |
| **AI model** | Reference to the AI model for which the prompt is created |

---

## Complete Attribute Summary by Asset Type

| Attribute | AI System | AI Model | AI Dataset | AI Prompt |
|---|---|---|---|---|
| Associated models (M2M) | ✓ | — | — | — |
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
| Data classification | ✓ | ✓ | ✓ | ✓ |
| SN record reference | ✓ | ✓ | ✓ | ✓ |

---

## Part 2: Evaluation Dashboard References

### Evaluation Metrics

The evaluation framework assesses virtual agent / Now Assist conversations across nine metrics. All metrics are rated on a scale of 3 or 5, then scaled to 5:

| Metric | Description |
|---|---|
| **Request Completion** | Measures the virtual agent's ability to complete user requests by accurately identifying the user's intent and gathering all required information (slot filling). Calculated as the lowest score between Slot Filling and Intent Accuracy. |
| **Intent Accuracy** | Shows the virtual agent's ability to comprehend user requests, resulting in relevant responses |
| **Slot Filling** | Shows the virtual agent's capability to interpret user responses and extract structured answers to required questions |
| **Smooth Flowing Conversation (Deadlock avoidance)** | Checks if the virtual agent responds dynamically, successfully moving the conversation forward without repetition |
| **Context Retention** | Shows if the virtual agent retains and uses information provided during the conversation, including request interpretation and slot filling |
| **Truthfulness (Hallucination Prevention)** | Shows if the virtual agent generates genuine responses grounded in the conversation, excluding fabrication or memory and comprehension failures |
| **Conciseness (Redundancy Avoidance)** | Checks the virtual agent's ability to avoid superfluous or verbose responses that don't contribute to the core intent |
| **Coherence** | Checks for clear logical flow, structure, and organization of virtual agent responses |
| **User Satisfaction** | Weighted average of all other metrics on which the conversation was evaluated |

> **Risk Officer Note:** From a governance perspective, **Truthfulness (Hallucination Prevention)** and **Intent Accuracy** are the highest-risk metrics for healthcare AI. A virtual agent that fabricates medical information (low Truthfulness) or misunderstands patient queries (low Intent Accuracy) can cause patient harm. Establish minimum acceptable thresholds for these two metrics on any patient-facing conversational AI. Any conversation with a Truthfulness score below threshold should be flagged for human review.

---

### Score Calculation Methodology

#### Deviation Calculations

To align auto-evaluation scores with human judgment over time, deviations are calculated from a rolling 6-month window of human-labeled scores:

**Upper Deviation:**
- Condition: Number of human-labeled scores HIGHER than auto-evaluated scores in the last 6 months > 30
- Calculation: Top 90% of these cases → average the delta (human score − auto score) = Upper Deviation

**Lower Deviation:**
- Condition: Number of human-labeled scores LOWER than auto-evaluated scores in the last 6 months > 30
- Calculation: Top 90% of these cases → average the delta = Lower Deviation

**Adjusted Score:**
- If ≥30 distinct evaluations of BOTH upper and lower deviations are labeled:
  - Error band = SUM(Avg labeling score − LLM score) / Distinct evaluations
  - Adjusted Score = Auto-Eval Score + Error Band
- If neither deviation meets the 30-record threshold: Adjusted Score = Auto-Eval Score

> **Minimum records required for deviation calculation:** 30 (controlled by `sn_na_conv_eval.errorBandMinRecords`)

#### User Satisfaction Score Calculations

**Auto eval user satisfaction score:**
SUM(metric score × metric weight) / SUM(metric weights) for all LLM-generated metric scores in the evaluation

**Human user satisfaction score:**
- Only calculated if at least one metric has been human-labeled
- For each metric: use labeled score if labeled, else use LLM score
- SUM(metric score × metric weight) / SUM(metric weights)

**Gap:** Human user satisfaction score − Auto eval satisfaction score

**Upper Deviation (evaluation level):** If Gap is positive and there are >30 records → error band at top 90% = SUM(Positive Gap) / Distinct evaluations

**Lower Deviation (evaluation level):** If Gap is negative and there are >30 records → error band at top 90% = SUM(Negative Gap) / Distinct evaluations

**Adjusted user satisfaction score:** SUM(Gap) / Distinct evaluations

---

### Important Calculation Notes

1. **The evaluator provides an aggregated score per chat** — even if multiple different requests are made by the user within one conversation, there is one score per conversation

2. **Performance Analytics indicators calculate the average score over time** — if you run batch jobs on historical data, these evaluations are counted on the **evaluation date** in aggregated scores, NOT on the actual chat date. Historical batch evaluations will not backfill scores for the original chat dates.

---

### Evaluation Flow Logic (Single Conversation)

The Execute Evaluation flow runs when a conversation's state changes to Complete:

1. **Count check:** If today's evaluation count ≥ max evaluations per day (`sn_na_conv_eval.maxEvaluateCount`, default 200) → stop
2. **Random sampling:** Generate random number 1–100; proceed only if ≤10 (10% random sampling rate)
3. **Conditional branch:** If sampled → continue; if not → stop
4. **Interaction table lookup:** Match conversation channel metadata with interaction table
5. **Application scope filter:** If interaction scope includes `hr` → skip (HR conversations excluded)
6. **Transcript construction (buildTranscript):**
   - Tag messages as `[User]:` and `[Virtual Agent]:`
   - Replace genius results with full Knowledge article body (tagged and delimited)
   - Skip if KB article is HR-scoped or inaccessible
   - Truncate articles >10,000 words
   - For catalog items: extract name, short description, description
   - Skip if first message routes to live agent, or live agent invoked within first 120 words
7. **Chat classifier:** Validate evaluation eligibility, extract Topic and Category (IT/HR)
8. **Create evaluation record** in `sn_na_conv_eval_evaluation` with State = Processing
9. **For each evaluation skill:** invokeApiDefinition → LLM skill invoked asynchronously → results parsed (Score, Reason, Examples) → written to `sn_na_conv_eval_evaluation_metrics`
10. **Wait 7 seconds** between each skill invocation (rate limit management)

**Skills invoked for evaluation:**
- Coherence Chat Evaluation
- Conciseness Chat Eval
- Context Retention
- Inadequate Slot Filling Chat Eval
- Intent Accuracy Chat Eval
- Smooth Flowing Conversation Chat Eval
- Truthfulness Hallucination Chat Eval

**Exclusion rules:**
- HR conversations: Always excluded
- Short conversations: First live agent invoked within 120 words → excluded
- Direct live agent routing: First message to live agent → excluded
- Inaccessible KB articles: Conversation references inaccessible/empty KB → excluded
- Already evaluated conversations: Skip in batch flow

### Request Completion Score Logic

The Request Completion metric is NOT independently scored by an evaluation skill. It is computed as:

```
IF (Slot Filling score > Intent Accuracy score):
    Request Completion score = Intent Accuracy score
    Request Completion reason = Intent Accuracy reason
ELIF (Slot Filling score < Intent Accuracy score):
    Request Completion score = Slot Filling score
    Request Completion reason = Slot Filling reason
ELSE (tied):
    Request Completion score = both scores (tied)
    Request Completion reason = both reasons
```

This logic reflects the principle that a request is only complete if both intent was understood AND all required slots were filled — so the score is bounded by the lower of the two.

---

## Key Takeaways for AI Risk & Compliance Officers

1. **Model card is the most important transparency artifact** — missing model cards should block assessment completion; they are the evidence base for risk scoring.
2. **Dataset card must document distribution and known biases** — without this, bias risk assessment on the model trained from the dataset is impossible.
3. **Data classification attribute bridges AI governance and enterprise data governance** — use it to flag PHI/Confidential data across all four AI asset types.
4. **Training procedure field determines explainability** — Neural Network and Reinforcement Learning models have lower explainability; factor this into regulatory risk classification, especially for EU AI Act high-risk systems.
5. **Acceptable usage on datasets is contractual** — license violations occur when datasets are used beyond their declared scope; enforce this during model creation workflows.
6. **Evaluation metrics are sampled at 10%** — evaluation scores are statistically representative, not exhaustive; understand this when interpreting quality metrics.
7. **Adjusted scores require 30+ human labels** — early in deployment, before 30 human-labeled evaluations exist, scores are raw auto-eval scores; they become calibrated over time.
8. **HR conversations are always excluded from evaluation** — if your AI system serves HR use cases, evaluation metrics will not cover those interactions; plan alternative quality assessment.
9. **Batch evaluation does not backfill to original chat dates** — historical batch runs show scores on the evaluation date, not the conversation date; account for this in trend analysis.

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 869–883*
