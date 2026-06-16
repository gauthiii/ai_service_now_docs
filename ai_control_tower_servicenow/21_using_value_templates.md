# Using Value Templates
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Role: AI Risk & Compliance Officer Reference

---

## What Is This?

Value templates are the structured framework in AICT for **defining, calculating, and tracking the productivity value delivered by AI assets**. They answer the question every executive asks: "What is this AI system actually worth?" By building formula-based, persona-specific value calculations into governance, AICT makes AI ROI measurable, transparent, and consistent across the enterprise.

For a Risk & Compliance Officer, value templates are relevant because: (1) they are reviewed and validated as part of the Assess lifecycle stage — making value justification a governance artifact, not just a finance exercise; (2) they reveal which AI systems are delivering value vs. sitting idle (dormant systems are a security risk); and (3) the value data feeds the executive-level Value dashboard that justifies the AI governance program itself.

---

## What Value Templates Are

> "Value templates introduce a unified and structured framework for defining, calculating, and tracking the value delivered by your AI assets. You can define value based on personas and formulas using customizable templates."

**Benefits:**
- **Transparency:** Visibility into how value is determined for an AI asset
- **Customization:** Supports various persona-driven and formula-based definitions

**Supported asset types:** Skills, AI agents, and AI use cases. Value templates are **not currently supported** for AI models, datasets, or prompts.

**Trigger for template assignment:** A value template is assigned to an asset when a skill, AI agent, or AI use case is **activated and deployed** as an asset in the system.

---

## State Behavior When Toggling Managed/Unmanaged

| Transition | Value Template State Change |
|---|---|
| Managed → Unmanaged | Published → Unmanaged; Draft → Retired |
| Unmanaged → Managed again | Only Unmanaged mappings revert to Published (Draft-turned-Retired does NOT revert) |

**Important:** Existing value template mappings remain the same, but the AI asset is **excluded from value calculations** while Unmanaged.

---

## Default Value Templates

AICT ships with default value templates for each supported asset type. These auto-apply when an asset is deployed:

| AI Asset Type | Default Formula |
|---|---|
| **ServiceNow skill** | Daily skill executions (Usage) × average time per execution (Time) × 50% (Acceptance rate) |
| **ServiceNow AI agent** | Daily AI agent executions (Usage) × average time per execution (Time) × 50% (Acceptance rate) |
| **AWS and Microsoft AI agents** | Daily AI agent invocations (Usage) × **15 mins** (Time, fixed) × 50% (Acceptance rate) |
| **ServiceNow AI use case** | Daily AI use case invocations (Usage) × average time per invocation (Time) × 50% (Acceptance rate) |

**Example — ServiceNow skill (Incident Summarization):**
- Daily executions: 1,500
- Average time per execution: 0.2 minutes
- Acceptance rate: 90%
- Value = 1,500 × 0.2 × (90/100) = **270 minutes/day**

**Example — ServiceNow AI agent (Problem Investigator):**
- Daily executions: 1,000
- Average time per execution: 1.5 minutes
- Acceptance rate: 50%
- Value = 1,000 × 1.5 × (50/100) = **750 minutes/day**

> **Risk Officer Note:** The 50% acceptance rate default is intentionally conservative — it assumes only half the AI outputs are accepted/acted upon. If your actual acceptance rate data is higher, the default template will understate value. If it is lower, the template will overstate value. The Value Template Review task in the Assess stage exists precisely to validate that the acceptance rate and time assumptions are realistic for each specific asset. Unrealistic assumptions in value templates can mislead executive decisions about which AI systems to invest in or retire.

---

## The Add Value Template Form — Field Reference

When creating a new value template, the form has four sections:

### Calculation Builder

| Field | Description | Notes |
|---|---|---|
| **Persona** | User role for whom value is calculated | Options: Agent, Developer, Other, Requestor. Default: Other. Value calculations apply to the selected persona only |
| **Usage** | Daily usage metric of the AI asset | Must be a daily usage indicator; can be a custom metric |
| **Time value type** | Type of time metric | Constant (fixed minutes) or Indicator (dynamic metric) |
| **Time constant** | Fixed time value in minutes as baseline | Used when Time value type = Constant |
| **Time indicator** | Average time saved per invocation (in minutes) | Used when Time value type = Indicator; derived from custom indicator |
| **Acceptance rate type** | Type of acceptance rate | Constant (fixed %) or Indicator (dynamic metric) |
| **Acceptance rate constant** | Fixed percentage representing acceptance rate | Value between 1 and 100 |
| **Acceptance rate indicator** | Dynamic acceptance rate from custom indicator | Daily indicator; value between 1 and 100 |

### Attributes

| Field | Description |
|---|---|
| **Template name** | Unique descriptive name; appears in the templates list |
| **Value template category** | Use case categorization: Productivity, Efficiency, Accuracy (helps organize and filter templates) |
| **Department** | Business unit associated with this template |
| **Description** | What the template does and how it measures value |

### Calculation Output

| Field | Description |
|---|---|
| **Instance** | Instance where the template is applied (useful for multi-instance management) |

**Testing note:** Validate formulas in non-production before publishing to production. After initiating testing: same-instance testing may take up to 10 minutes; cross-instance testing may take up to 30 minutes. During this period, you cannot edit or resend the template, but can work on other templates.

---

## Create a New Value Template

**Roles required:** AI steward (`sn_ai_governance_ai_steward`) AND AI asset owner (`sn_ai_asset_mgmt.ai_asset_owner`)

**Navigation:** `Workspaces > AI Control Tower > AI assets view > Productivity > Value templates > New template`

### Three-Step Process

**Step 1: Formula**
- Build the calculation using the Calculation Builder fields
- Select **Add metrics** to use a custom metric for calculations
- Select **Next**

**Step 2: Map**
- Select the type of AI asset and specific AI assets to map to this template
- You can go back and change selected AI assets
- Select **Next**

**Step 3: Test (Optional)**
- Select the instance and AI assets for real-time value estimation
- Select **Validate and calculate** to preview the output
- This step can be skipped — publish directly after mapping if testing is not needed

**Step 4: Publish**
- Select **Publish template**
- If selected AI assets already have an existing template mapping, a confirmation dialog appears asking whether to publish (replacing the existing template)
- **Constraint:** No AI system can have two templates for its value calculation
- **Scope:** When published, the template is modified across **all instances** and all subsequent calculations use the new template

---

## Edit a Value Template

**Roles required:** AI steward AND AI asset owner

**Navigation:** `Productivity > Value templates > select the template > Duplicate`

**Process:**
1. Select the asset and click **Duplicate** — opens a dialog to select what to duplicate, then opens a tab with same details as original
2. **Duplicating changes the template state to Draft** — this enables editing
3. For a published template: only a limited number of fields can be edited directly; full editing requires duplicating
4. Edit the template per requirements
5. Validate and test: **Validate and calculate output** — can preview calculations from the past 30 days without affecting historical data from the previous version
6. Publish: **Publish template** — calculations across all instances switch to the new template

**Post-publish constraints:**
- Cannot edit basic information after publishing
- Can still add more assets for mapping
- Testing is unavailable for published templates

---

## Create a New Value Template Mapping

Create a direct mapping between a value template and a specific AI asset.

**Role required:** AI steward (`sn_ai_governance_ai_steward`)

**Navigation:** `AI assets view > Productivity > Templates mapping > New record`

**Form fields:**

| Field | Description |
|---|---|
| Template name | Value template to map with the AI asset |
| Persona | Auto-populated based on the selected value template |
| AI system type | Type of AI system the AI asset belongs to |
| Asset name | Name of the AI asset to map |

Select **Create mapping record** → new mapping appears in the Productivity - Templates mapping list.

---

## Assign a Default Template

Assign a template as the default for a category of AI systems — so newly deployed assets in that category automatically use this template without manual mapping.

**Role required:** AI steward (`sn_ai_governance_ai_steward`)

**Navigation:** `Configurations view > Controls > Value templates > Assign default template`

**Form fields:**

| Field | Description | Notes |
|---|---|---|
| Template name | Default template to assign | — |
| Vendors | Software vendor of the AI system | Scopes the default assignment by vendor |
| AI system category | Category of AI system | For AI Skill: specify skill type as Default or Creator |

Select **Assign as default** → if this matches a previous mapping, updates the existing configuration.

---

## Review a Value Template Mapping (Assess Stage Task)

This is the governance activity that validates value templates during the AI asset lifecycle.

**Prerequisites:**
- AI asset State = Deployed
- Asset lifecycle phase = New
- Lifecycle status = In review

**Roles required:** AI steward AND AI asset owner

**What the AI steward validates during this review:**

1. **Accurate productivity metrics:** Hours saved are correctly calculated
2. **Valid assumptions:** Time-saving estimates and acceptance rates are realistic
3. **Complete data:** All inputs, calculations, and expected gains are documented
4. **Proper alignment:** Asset template mappings are updated as needed

**Procedure:**
1. Navigate to `Workspaces > AI Control Tower > AI assets view`
2. Select the AI asset and click **Start review**
3. The AI Asset Lifecycle tab opens; a **Value template review and approval task** is automatically created
4. Select and open the Value Template review and approval task

**Task record fields:**

| Field | Values |
|---|---|
| Short description | "Value Template review and approval" (pre-filled) |
| Description | End-to-end task details (pre-filled) |
| Number | System-generated task number |
| Type | AI governance task |
| Assigned to | User with AI steward role |
| Due date | Due date for the review |
| Parent approval record | Linked approval record number |
| Priority | Priority of the review |
| State | Open → In progress → Completed → Closed skipped |
| Status | Not yet requested → Requested → Approved → Rejected |
| Close notes | Reviewer's findings before closing |

5. Select **Save** and return to the Details tab
6. After reviewing task details and value templates mapped to the AI asset, select **Mark as complete**
7. Result: Assess stage is complete; navigation moves to the next lifecycle stage

> **Risk Officer Note:** The Value Template review task ensures that productivity claims for AI systems are validated before the asset is approved for production. This is governance with a financial dimension: an AI system deployed with an inflated value template creates misleading ROI data that can distort investment decisions. The AI steward's close notes on this task should specifically address whether the usage volumes, time savings, and acceptance rates are evidence-based or assumed. "Acceptance rate 50% assumed — no measurement data available" is a valid close note; "looks good" is not.

---

## Key Takeaways for AI Risk & Compliance Officers

1. **Value templates quantify AI ROI within the governance lifecycle** — value review is not a separate exercise; it is embedded in the Assess stage as a mandatory task.
2. **Default 50% acceptance rate is conservative** — validate against actual data; overstated templates mislead executives; understated templates undermine AI program justification.
3. **Publishing a template updates ALL instances** — template changes have enterprise-wide effect; test in non-production first (10–30 min testing window).
4. **No AI system can have two active templates** — publishing a new template replaces the existing one; verify the replacement is intentional via the confirmation dialog.
5. **Managed→Unmanaged freezes value calculations** — toggling a system Unmanaged excludes it from value metrics, which affects the Value dashboard's completeness.
6. **AWS/Microsoft agents use a fixed 15-minute time value** — this is a platform default, not a measured value; for accurate reporting, replace with a custom indicator based on actual usage data.
7. **Template mappings survive Managed→Unmanaged toggle** — the mapping record is preserved; only the calculation is excluded while Unmanaged.

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 845–850, 861–862*
