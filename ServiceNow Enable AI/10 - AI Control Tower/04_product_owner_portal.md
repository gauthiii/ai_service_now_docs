# Product Owner Portal
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Role: AI Risk & Compliance Officer Reference

---

## What Is This?

The Product Owner portal is a **scoped, role-specific view** within AI Control Tower designed for AI asset owners and workspace users. Unlike the AI Steward view — which sees the entire AI estate — the Product Owner view is deliberately limited to the assets a person manages or owns. It also includes an AI portfolio view for workspace users who need visibility across all AI assets without the governance permissions of a steward.

Understanding this portal is important for Risk & Compliance Officers because:
1. Product owners are responsible for submitting assets for governance review — they are the first link in the governance chain.
2. The portal surfaces tasks and cases assigned to owners — tracking these is part of oversight accountability.
3. The AI portfolio tab gives workspace users (including compliance observers) a structured view of all AI assets and their lifecycle/risk status.

---

## Who Uses This Portal

| Persona | Tab Access |
|---|---|
| **AI asset owner** | My overview, Value, Adoption tabs |
| **AI Control Tower workspace user** | AI portfolio tab |

---

## My Overview Tab

**Purpose:** Displays all active assets to the asset owner and AI stewards for the assets they manage or own.

### Widgets on My Overview

**Assets**
Displays all assets owned by the asset owner, organized by category:
- Generative AI
- Agentic AI
- AI prompt
- AI dataset
- AI model

**Assets by lifecycle status**
Shows the lifecycle status of the owner's assets:

| Lifecycle Status | Meaning |
|---|---|
| Deployed | Asset is live in production |
| In review | Asset is currently under AI steward review |
| AI steward review | Awaiting steward action |
| Ready for deployment | Passed review; pending deployment |
| Rejected | Steward rejected the asset |
| Cancelled | Review process was cancelled |

**AI cases by state**
- Shows active cases categorized as: **New** and **Triage**
- Only cases associated with the owner's assets are shown

### Create an AI Asset Button

The `Create an AI asset` button is available directly from the My overview home page. This is the primary mechanism for asset owners to submit new AI systems, models, prompts, or datasets into the governance workflow.

> **Risk Officer Note:** The "Create an AI asset" action is where the governance lifecycle begins. An asset that is created but not submitted for review is in an unmanaged, ungoverned state. A key compliance control is ensuring that **no AI asset is deployed without first passing through the AICT lifecycle** — this starts here, with the product owner submitting via this button.

---

## Tasks and Cases List

The My overview tab includes two lists that are central to governance accountability.

### Tasks List
Shows all active tasks assigned to the product owner by default.

| Column | Description |
|---|---|
| Number | Task identifier |
| Priority | Task priority |
| Short description | Task summary |
| Assigned to | Who the task is assigned to |
| State | Current task state |
| Due date | When the task is due |
| Asset in review | Which AI asset this task relates to |

### Cases List
Shows active AI cases associated with the owner's assets.

| Column | Description |
|---|---|
| Name | Case name |
| Number | Case identifier |
| Case analyst | Assigned analyst |
| Assignment group | Team responsible |
| State | Case state |
| Priority | Case priority |

> **Risk Officer Note:** These task and case lists are the product owner's accountability view. From a Risk & Compliance standpoint, overdue tasks and unresolved cases on an asset are governance findings. Monitoring the average age of open tasks per asset owner, and flagging assets with overdue tasks, should be a standard oversight metric. An AI asset with open, overdue Impact Assessment tasks should not be allowed to remain in a deployed state without documented exception.

---

## AI Portfolio Tab

**Who sees this:** AI Control Tower workspace users

**Purpose:** Provides a read-only, comprehensive view of **all AI assets** (active, inactive, and completed) across the organization — regardless of who owns them.

### Assets Shown

The AI portfolio tab shows all active AI assets in four categories:
- AI systems
- AI model
- Datasets
- Prompts

### Lifecycle Status Categories

| Status | Description |
|---|---|
| In review | Currently under governance review |
| Approved | Approved by AI steward |
| Rejected | Rejected during review |
| Deployed | Live in production |
| Retired | Decommissioned |

### Columns in the AI Assets List

| Column | Description |
|---|---|
| Display name | Asset name |
| Provider | Who built the asset |
| Vendor | Who sold the asset |
| Managed by | Asset owner |
| Lifecycle phase | New, Assess, Build and test, Deploy, Offboarding |
| Install status | Whether the asset is installed |
| Lifecycle status | Current governance status |
| Risk classification | High, Medium, Low, Unacceptable, To be determined |

> **Risk Officer Note:** The AI portfolio tab is the closest thing to a **full AI registry** that a workspace user or compliance observer can access. Key things to monitor here: (1) Any asset in `Deployed` status with `Risk classification = To be determined` — these are ungoverned deployed assets, a critical gap. (2) `Retired` assets should be reviewed for proper decommissioning — access revoked, data purged. (3) Assets with no `Managed by` value are orphaned — a governance risk.

---

## Automation Rules (Related to Product Owner Context)

Product owners' assets can be automatically moved from Unmanaged to Managed via **Automation Rules**. These rules run every 6 hours via the `Run AI Asset Management Rules` scheduled job. AI stewards can also trigger immediate execution via `Run Now`.

**Important:** If an asset qualifies for a rule, it is automatically moved to managed assets — without any manual action from the product owner. This means assets can enter the governance lifecycle without the owner initiating it. Product owners should be aware of this.

**System properties governing rules:**

| Property | Description |
|---|---|
| `sn_ai_governance.management_rule.max_active_rules` | Maximum number of active rules allowed |
| `sn_ai_governance.management_rule.max_total_rules` | Maximum total rules allowed |

---

## Managed vs. Unmanaged Status (Critical Context)

Starting with the March 2026 release, assets are designated as either **managed** or **unmanaged** directly from the list:

- **Default:** All assets in AICT start as **Unmanaged**
- **Unmanaged:** Not governed or monitored; no lifecycle, no risk classification, no security scoring
- **Managed:** Full AICT capabilities enabled — governance, lifecycle management, value assessment, risk classification, security, and privacy

**Important trigger:** Initiating a steward review for an unmanaged asset automatically transitions it to managed state.

If a managed asset is switched back to unmanaged, it **loses all AICT governance capabilities**. This action should be audited and controlled.

> **Risk Officer Note:** The Managed/Unmanaged distinction is your primary shadow AI control point. An asset that is Deployed but Unmanaged is a deployed AI system with no governance — equivalent to shadow IT for AI. The governance objective is to reduce the Unmanaged count toward zero over time. Track `Unmanaged + Deployed` assets as a critical risk indicator — these are live systems with no oversight.

---

## Value Tab (Product Owner View)

The Value tab in the product owner view shows productivity and engagement metrics **scoped to the owner's assets only**. The metrics are the same as the AI Steward's Value tab but filtered to owned assets.

**Important note from the documentation (March 2026 release):**
> "AI systems that were initially managed and later marked as unmanaged will continue to appear in the Value dashboard. Their value and usage will be accounted for only up to the date they were marked as unmanaged."

This means historical value data is preserved when an asset is moved back to unmanaged — important for audit trail integrity.

---

## Key Takeaways for AI Risk & Compliance Officers

1. The Product Owner portal is the **entry point for governance** — assets are submitted for review here. Gaps here = ungoverned assets in production.
2. **Tasks and cases** on the My overview tab are accountability artifacts — overdue tasks are governance findings.
3. The **AI portfolio tab** is the closest to a full AI asset registry for workspace users — monitor for Deployed + Risk classification = "To be determined" as a priority gap.
4. **Automation Rules** can move assets to managed automatically — product owners may not always initiate the lifecycle. Ensure they are aware of this.
5. **Managed vs. Unmanaged** is the foundational governance control — track `Deployed + Unmanaged` assets as a top governance KPI.
6. **Orphaned assets** (no `Managed by`) are a governance risk — establish a process for identifying and assigning them.

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 771–773*
