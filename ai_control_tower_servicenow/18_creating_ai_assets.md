# Creating AI Assets
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Role: AI Risk & Compliance Officer Reference

---

## What Is This?

Creating AI assets is the manual pathway for registering AI systems, AI models, prompts, and datasets into the AICT inventory. While Now Assist Asset Discovery handles automatic sync of ServiceNow-native assets and Enterprise AI Discovery handles third-party cloud assets, manual creation is required for: assets that are not auto-discoverable, assets being created for the first time before deployment, and assets being registered from outside the Now Platform.

Every manually created asset enters the **Onboard stage** of the AI asset lifecycle immediately upon submission, with a Lifecycle status of **AI steward review** — triggering the governance workflow.

---

## Common Rules Across All Asset Types

| Rule | Description |
|---|---|
| **Roles required** | `sn_ai_governance_ai_steward` OR `sn_ai_asset_mgmt.ai_asset_owner` for creation |
| **Managed by field** | Auto-set to the creating user. Editable only by AI stewards — read-only for asset owners |
| **State options** | Draft (not yet submitted) or Deployed |
| **Save vs. Submit** | Save: stores the record without triggering governance. Submit for review: enters the lifecycle and triggers AI steward review |
| **Post-submission navigation** | Unsubmitted (saved) assets accessible via `AI assets > Lifecycle > Onboard` |
| **Result of submission** | Asset enters Onboard stage, Lifecycle status = AI steward review |
| **Default management** | All assets created through AICT are automatically designated as Managed |

---

## Asset Type 1: Create AI System Assets

**Navigation:** `Workspaces > AI Control Tower > AI assets view > AI asset inventory - Managed > AI Systems` OR `AI asset inventory - Unmanaged > AI Systems > Add AI system`

### Section 1: Details

| Field | Description | Risk Governance Relevance |
|---|---|---|
| Name | Name of the AI system | Unique identifier in the inventory |
| Provider | People or organization that developed the AI system | Vendor identification for third-party risk |
| Version | Version of the AI system | Change tracking; version used at time of approval |
| Description | Brief description | Human-readable governance context |
| Documentation | Additional information (evaluation methodology, technical specs) | Supporting documentation for the risk assessment |
| Managed by | User assigned to manage the AI system | Accountability assignment |
| State | Draft or Deployed | Operational state |
| License details | License in use | IP and vendor obligation tracking |
| Asset type | Agentic AI / Classic AI / Generative AI | Determines which related asset sections appear |
| Department | Department that owns the AI system | Organizational accountability |
| Supported locations | Locations where the AI system is supported | Geographic compliance scoping |

> **Risk Officer Note on Asset Type:** The Asset type field is not just a label — it controls which related asset sections appear in the next step. Selecting "Agentic AI" enables the Sub AI systems and Tools sections. Selecting "Agentic AI" or "Generative AI" enables the Sub AI systems section. Setting this incorrectly at creation will hide governance-relevant relationship fields.

### Section 2: Related Assets

Associate the AI system with its dependent assets. Available association types by asset type:

| Related Asset Section | Available For | What It Links |
|---|---|---|
| **Sub AI systems** | Agentic AI and Generative AI only | Sub-systems and components the parent system depends on |
| **AI models** | All types | AI models that power this system |
| **Evaluation datasets** | All types | Datasets used to test integrated AI models |
| **Prompts** | All types | Prompts provided to integrated AI models |
| **Tools** | Agentic AI only | AI tools integrated with this system |

**Two ways to link related assets:**
- **Add from inventory** — select from existing assets already in the inventory
- **Create** — create a new related asset inline (not available for AI tools)

> **Risk Officer Note:** The Related Assets section is the dependency chain. Completing it is what makes risk traceability possible. An AI system record with no linked models, datasets, or prompts is an incomplete record — it passes the "asset exists" check but fails the "governance is complete" check. Never submit an AI system for review with empty related asset sections if those dependencies exist.

### Section 3: Use & Purpose

This section is the richest source of risk-relevant metadata in the entire asset creation form. All fields should be treated as risk inputs.

**Intended outcome of the AI system:**

| Option | Risk Implication |
|---|---|
| Not Applicable | Review appropriateness of this selection |
| Efficiency Boost | Low direct risk unless efficiency is safety-critical |
| Quality Enhancement | Medium risk if quality judgments affect people |
| Decision Guidance | High risk — AI influences human decisions |
| Automation of Tasks | High risk — tasks may affect people without review |
| Customer Experience Upgrade | Medium risk — customer-facing, reputation risk |
| Insight Generation | Medium risk — insights may drive consequential decisions |

**Interaction type with end users:**

| Option | Risk Implication |
|---|---|
| No Direct Interaction | Background processing — still has risk but less visible |
| Background Support | Agent-level, no user-facing output |
| Notifications & Prompts | Moderate — influences user behavior |
| User-Facing Recommendations | High — direct influence on user decisions |
| Chat-Based Interaction | High — open-ended, harder to control scope |
| Interactive Experience | Highest — user and AI jointly navigate workflow |

**Level of human involvement:**

| Option | Risk Implication |
|---|---|
| Full User Control | Lowest risk — human always in command |
| User-Guided with AI Support | Low-medium risk |
| Shared Control | Medium risk — shared accountability |
| AI-Initiated with User Approval | Medium-high — AI leads, human approves |
| Full Automated Workflow | Highest risk — no human in the loop |

**System autonomy level:**

| Option | Risk Implication |
|---|---|
| None | No AI autonomy — safe |
| Assistive (AI suggests) | Low risk |
| Semi-Automated (acts with confirmation) | Medium risk |
| Condition-Based Automation | Medium-high — automation triggered by conditions |
| Event-Triggered Automation | High — automated responses to events |
| Fully Automated Execution | Highest risk — no human in the loop |

**Type of output produced:**
- Automated Decisions, Generated Content, Insight & Summaries, Ranking & Scores, Recommendations, Simple Alerts, System Actions

**Area where the AI system is used:**
- Customer services, External Partner Ecosystem, Finance & Accounting, HR & Workforce, Internal Operations, IT & Security, Sales & Marketing, Supply Chain

**People affected by the AI system:**
- External Partners, General Customer Base, Internal Team, Public or Large Audiences, Specific Customer Groups

**Data used by the system:**
- Behavioral or Usage Data, Business Operational Data, Customer Interaction Data, Profile or Account Data, Public or General Info, Sensitive Business Data

**Additional use and purpose details:** Free text for additional context.

> **Risk Officer Note:** The Use & purpose fields collectively describe the risk profile of the AI system before any formal assessment is run. For a Risk & Compliance Officer, these fields answer: *How autonomous is it? Who does it affect? What data does it use? What outputs does it produce?* An AI system that answers: Full Automated Workflow + Specific Customer Groups + Customer Interaction Data + Automated Decisions is a maximum-risk system before a single assessment question has been asked. Use these fields to triage which assets need the most rigorous evaluation workflows.

> **Additional note from the docs:** "For more information on classifying AI systems based on regulatory risk at intake by applying a configured Risk Assessment Methodology (RAM), see Assessment templates and risk assessment methodologies." This means the Use & purpose fields can feed into automated regulatory risk classification using configured RAMs — this is the bridge between intake and the AIRC risk assessment module.

### Submission

- Select **Submit for review** → Asset enters Onboard stage, Lifecycle status = AI steward review
- Select **Save** → Asset stored as Draft; edit and submit later via `AI assets > Lifecycle > Onboard`

---

## Asset Type 2: Create AI Model Assets

**Navigation:** `AI asset inventory - Managed > AI Models` OR `AI asset inventory - Unmanaged > AI Models > Add AI model`

### Details Fields

| Field | Description | Risk Governance Relevance |
|---|---|---|
| Name | Name of the AI model | — |
| Provider | Developer of the AI model | Third-party risk identification |
| Version | Model version | Tracks which version was approved |
| Supported languages | Languages the model supports | Scope of use; localization risk |
| Deployment guidelines | Instructions for deployment | Standard operating procedure reference |
| Training procedure | Method used to train the model | Bias and fairness assessment input |
| Context window | Max tokens the model can process and recall | Operational limit; affects data exposure risk |
| Model size in MB | Size of the model | Infrastructure sizing reference |
| Model parameters info | Internal variables learned during training | Technical governance detail |
| Description | Brief description | — |
| Managed by | Managing user | Accountability |
| State | Draft or Deployed | — |
| License details | License in use | Compliance obligation tracking |
| **Base model** | **Foundation model this model was built from** | **Provenance tracking — critical for inherited risks** |
| Department | Owning department | Organizational accountability |
| Supported locations | Locations supported | Geographic compliance scoping |
| **Model card** | **Document describing context, intended use, training data, limitations** | **Key governance document for model transparency** |
| Model weights info | Numerical parameters defining learning | Technical reference |
| Required infrastructure | Software and hardware requirements | Operational dependency |
| **Evaluation metrics report** | **Data for metrics evaluating model effectiveness** | **Performance evidence for risk assessment** |

> **Risk Officer Note:** Three fields stand out for governance: (1) **Base model** — if this model was built on a foundation model (e.g., GPT-4, Llama), the risks of the foundation model are inherited. Document this explicitly. (2) **Model card** — this is the primary transparency document for the model; it should exist before the model is submitted for review; a missing model card should block submission. (3) **Evaluation metrics report** — the performance evidence; without this, you cannot assess accuracy, bias, or drift risk.

### Related Assets

Associate the AI model with datasets:
- **Evaluation datasets** — datasets that help TEST the model
- **Training datasets** — datasets that helped TRAIN the model

Both types are governance-critical: training datasets are the source of bias risk; evaluation datasets are the evidence of performance assessment.

---

## Asset Type 3: Create Prompt Assets

**Navigation:** `AI asset inventory - Managed > Prompts` OR `AI asset inventory - Unmanaged > Prompts > Add prompt`

### Details Fields

| Field | Description | Risk Governance Relevance |
|---|---|---|
| Name | Name of the prompt | — |
| Provider | Developer of the prompt | Authorship accountability |
| Version | Prompt version | Version control for prompt governance |
| Description | Brief description | — |
| Documentation | Additional information (evaluation methodology for accuracy/quality of AI model responses based on the prompt) | Quality assurance documentation |
| Managed by | Managing user | Accountability |
| State | Draft or Deployed | — |
| **Prompt information** | **The actual prompt text/input provided to AI models** | **The governed artifact itself** |

> **Risk Officer Note:** The "Prompt information" field contains the actual prompt text. This is the artifact under governance. System prompts in particular must be version-controlled — a change to a system prompt changes what the AI system does. Changes to prompt text after an asset is approved should trigger a change request, not a silent edit. Treat prompt text like a policy document: versioned, reviewed, and immutable post-approval without a formal change process.

### Related Assets

Associate the prompt with:
- **AI models** — models that will receive this prompt as input

A prompt linked to no AI model has unclear governance scope. Always link prompts to their intended models.

---

## Asset Type 4: Create Dataset Assets

**Navigation:** `AI asset inventory - Managed > Datasets` OR `AI asset inventory - Unmanaged > Datasets > Add dataset`

### Details Fields

| Field | Description | Risk Governance Relevance |
|---|---|---|
| Name | Name of the dataset | — |
| Provider | Developer/source of the dataset | Data provenance; vendor or internal |
| **Acceptable usage** | **Acceptable use for the dataset (multiple values allowed)** | **Constrains how the dataset can be used; governance boundary** |
| Version | Dataset version | Version control for training data |
| **Data type** | **Type of data in the dataset (multiple values allowed)** | **Data classification; PII/PHI flag** |
| **Source** | **Source of the dataset: internal customer data or public data** | **Data provenance; consent chain** |
| Description | Brief description | — |
| Managed by | Managing user | Accountability |
| State | Draft or Deployed | — |
| **Creation type** | **Curated / Derived / Synthetic** | **Data origin; synthetic data has different risk profile than real data** |
| **Base datasets** | **Dataset this was built from** | **Derived/synthetic data provenance** |
| Department | Owning department | Organizational accountability |
| Dataset creation date | Date and time dataset was created | Temporal provenance |
| **Dataset card** | **Document describing context, intended use, limitations, and potential biases** | **Primary transparency document for the dataset** |

> **Risk Officer Note — Four Critical Fields:**

> **Acceptable usage** — this field defines the governance boundary of the dataset. If a dataset's acceptable usage is "model evaluation only," using it for production training is a governance violation. Document this field carefully and enforce it.

> **Data type** — this is where you declare PII, PHI, or sensitive data. In healthcare, a dataset containing patient records must be flagged here. This flag should trigger additional review requirements (HIPAA review task, data privacy review task) automatically in your governance playbook.

> **Creation type** — Curated, Derived, or Synthetic each carry different governance implications. Synthetic data does not have privacy risk from real individuals but may not accurately represent the population. Derived data inherits the risks and consents of the source datasets. Curated data from real sources requires consent documentation.

> **Dataset card** — this is the governance transparency document for the dataset. A missing dataset card means the model trained on this dataset cannot be fully assessed for bias, limitations, or appropriate use scope. Dataset cards should be mandatory for all datasets used in production AI systems.

---

## Asset Creation Process Summary

```
For all asset types:

Step 1: Navigate to correct asset inventory section
Step 2: Select Add [asset type]
Step 3: Fill Details section (name, provider, version, type, etc.)
Step 4: Select Next
Step 5: Fill Related assets section (link models, datasets, prompts, tools)
Step 6: Select Next (for AI systems: fill Use & purpose section)
Step 7: Select Submit for review OR Save

Result on Submit:
- Asset enters AI Asset Inventory
- Asset enters Onboard stage of lifecycle
- Lifecycle status = AI steward review
- If "Automatically trigger playbooks" is active: approval workflow fires
```

---

## Key Takeaways for AI Risk & Compliance Officers

1. **Related asset sections must be complete** — an AI system with no linked models, datasets, or prompts is an incomplete record; treat incomplete related assets as open governance findings.
2. **Use & purpose fields are your pre-assessment risk profile** — Full Automated Workflow + Patient Data + Automated Decisions = maximum risk, maximum scrutiny required.
3. **Model card and Dataset card are mandatory governance documents** — missing cards should block submission.
4. **Base model field traces inherited risk** — foundation model risks propagate to derived models.
5. **Dataset Creation type matters for governance** — Curated (real data), Derived (processed real data), and Synthetic each have distinct risk profiles.
6. **Prompt information field is the governed artifact** — changes to prompt text after approval require a change request, not a silent edit.
7. **Save defers governance; Submit activates it** — teams that habitually Save and never Submit create backlog of ungoverned assets in the Onboard stage.

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 824–834*
