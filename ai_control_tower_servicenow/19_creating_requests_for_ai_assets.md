# Creating Requests for AI Assets
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Role: AI Risk & Compliance Officer Reference

---

## What Is This?

Once an AI asset is deployed and managed, its governance does not end. Two types of post-deployment requests manage the ongoing lifecycle of deployed AI assets:

1. **Change requests** — to modify the relationships between a deployed AI asset and its related assets (models, prompts, datasets, tools)
2. **Offboarding requests** — to retire deployed AI assets that are no longer needed

Both request types follow a formal approval workflow involving the asset owner (initiator) and the AI steward (reviewer/approver). This ensures that even post-deployment changes and retirements go through a governed process with a documented audit trail.

---

## Change Requests for AI Assets

### Purpose

> "Create a change request to modify the relationships between a deployed AI asset and its related assets."

A change request is triggered when you need to:
- Change which AI model an AI system uses
- Update the datasets linked to a model
- Add or remove tools from an agentic AI system
- Update sub AI systems linked to a system
- Update prompts associated with a system
- Update evaluation or training datasets

**What change requests do NOT cover:** Changes to the asset's core metadata (name, description, use & purpose fields). Those would require the asset to go through a new review cycle.

### Eligible Asset Types for Change Requests

- AI systems (Classic, Generative, and Agentic)
- AI models
- Datasets

**Note:** Prompts and MCP servers are not listed as eligible for change requests in the documented procedure.

### Roles Involved

| Role | Action |
|---|---|
| AI asset owner (`sn_ai_asset_mgmt.ai_asset_owner`) | Creates and submits the change request |
| AI steward (`sn_ai_governance_ai_steward`) | Reviews, assigns, and approves or rejects the request |

### Initiating a Change Request (Asset Owner)

Three navigation paths to create a change request:

**Path 1: From the AI Control Tower Home view**
- `Home view > Create request drop-down > Create a change request`

**Path 2: From the Change requests list**
- `AI assets view > Requests > Change requests > Create change request`

**Path 3: From the AI asset record (most contextual)**
- `AI assets view > AI asset inventory - Managed > [asset type subsection]`
- OR: `Lifecycle > Deploy`
- Select the AI asset meeting ALL THREE criteria:
  - State = Deployed
  - Lifecycle phase = Deploy
  - Lifecycle status = Deployed
- `Create a request drop-down > Create a change request`

> **Risk Officer Note:** The three-criteria check (State = Deployed, Lifecycle phase = Deploy, Lifecycle status = Deployed) ensures change requests can only be created for assets that have completed the full governance lifecycle. An asset in "In review" or "Build and test" status cannot have a change request raised against it — it must first complete deployment. This prevents circular governance gaps.

### Change Request Form Fields

**Change details section:**

| Field | Description |
|---|---|
| Asset in review | The AI asset to modify (auto-populated if initiated from asset record) |
| Version | Updated version number of the AI asset |
| Due date | When the request must be completed |
| Justification | Reason for creating the change request |

**Conditional sections (appear based on asset type):**

| Section | Appears For | What It Updates |
|---|---|---|
| Sub AI systems | AI systems (Generative AI or Agentic AI only) | Related AI components or subsystems |
| AI models | AI systems only | Related AI models |
| AI prompts | AI systems only | Related prompts |
| Evaluation datasets | AI systems and AI models | Related evaluation datasets |
| Tools | Agentic AI systems only | Related tools |
| Training datasets | AI models only | Related training datasets |
| Source | Datasets only | Related data source |
| Base datasets | Datasets only | Related base dataset |
| Dataset card | Datasets only | Related dataset card |

> **Risk Officer Note:** The conditional sections mean the change request form is asset-type aware. When you raise a change request for an Agentic AI system, you see tools and sub AI systems. When you raise it for a dataset, you see source and base datasets. This scoping ensures the right relationship changes are documented for each asset type. Review all conditional sections carefully — for an agentic AI system, an unnoticed tool change can significantly alter the system's risk profile.

### Submitting and Approving a Change Request

**Asset owner submits:**
1. Fill in change details form
2. Select `Submit for review`
3. In the Submit change request dialog box, select `Submit request`
4. Automatically redirected to the new change request record

**AI steward reviews and decides:**
1. Open the change request record (from Change requests list or from the AI asset record's Requests tab → Change requests)
2. On the Details tab, set the Assigned to field (can assign to self or any AI steward)
3. The assigned user approves or rejects:
   - **Approve:** Status → Approved; State → In progress

**After approval — what happens automatically:**
> "The AI Control Tower application then generates a change task for each asset that is impacted by the request. These change tasks appear on the Change tasks tab and specify the actions that must be taken on the impacted assets."

- Change tasks are assigned to users with the AI asset owner role
- AI stewards can create additional change tasks manually for further clarification
- After all change tasks are completed: AICT **automatically creates a new AI asset record** for the changed asset
- State of the request changes to Completed

**After rejection:**
- Status → Rejected; State → Completed

**Important constraint:** The Change tasks tab is NOT available if the change request was created for a dataset.

> **Risk Officer Note:** The automatic creation of a new AI asset record after a change request is completed is the governance mechanism for tracking asset evolution. Each significant relationship change results in a new asset version record. This creates a version history of the asset's governance — critical for audit trails and for understanding which version of an asset was deployed at any given time. Ensure change request justifications are substantive: they explain WHY the change was made, not just what changed.

---

## Offboarding Requests for AI Assets

### Purpose

> "Create an offboarding request to retire AI assets that are no longer needed."

The offboarding request is the formal retirement mechanism. Without it, assets remain in "Deployed" status indefinitely — continuing to appear in the AI inventory, consuming governance attention, and potentially retaining access and permissions even though they are no longer used.

**Automation note:**
> "We have automated the ServiceNow AI model to initiate the offboarding workflows when a deprecation date is present."

This means that if a model has a deprecation date recorded, offboarding is triggered automatically.

### Eligible Asset Types for Offboarding Requests

- AI systems (Classic, Generative, and Agentic)
- AI models
- Datasets
- **MCP servers** (note: this type is included for offboarding but NOT for change requests)

### Roles Involved

| Role | Action |
|---|---|
| AI asset owner (`sn_ai_asset_mgmt.ai_asset_owner`) | Creates and submits the offboarding request |
| AI steward (`sn_ai_governance_ai_steward`) | Reviews and approves the request |

### Initiating an Offboarding Request (Asset Owner)

Three navigation paths (parallel to change request):

**Path 1: From the AI Control Tower Home view**
- `Home view > Create request drop-down > Create an offboarding request`

**Path 2: From the Offboarding requests list**
- `AI assets view > Requests > Offboarding requests > Create offboarding request`

**Path 3: From the AI asset record**
- Same criteria as change requests: State = Deployed, Lifecycle phase = Deploy, Lifecycle status = Deployed
- `Create a request drop-down > Create an offboarding request`

### Offboarding Request Form Fields

| Field | Description |
|---|---|
| Asset in review | The AI asset to retire (auto-populated if initiated from asset record) |
| Due date | When the offboarding must be completed |
| Justification | Reason for retiring the asset |

### Submitting an Offboarding Request

1. Fill in the form
2. Select `Save` and then `Submit for review`
3. In the Submit offboarding request dialog box, select `Submit request`
4. The offboarding workflow is initiated
5. Two additional tabs appear on the request record:
   - **Impacted assets** — lists all related assets affected by the retirement
   - **Offboarding workflow** — shows the workflow steps

### What the Offboarding Workflow Does

After AI steward approval:
- Assigns tasks to **all impacted asset owners** for each impacted asset
- Updates the Status of the AI asset record to **Retired** upon completion

**Impacted assets:** When an AI system is retired, the models, datasets, and prompts linked to it may be impacted. The offboarding workflow surfaces these impacts so owners can handle them appropriately (e.g., a dataset that was only used by the retiring system may also be eligible for retirement).

> **Risk Officer Note:** The "Impacted assets" tab is the offboarding equivalent of the dependency chain. Before approving an offboarding request, review all impacted assets: (1) Are any of the linked models or datasets used by OTHER AI systems? If so, retiring the parent system should not cascade to them. (2) Are there any active sessions, API connections, or integrations that need to be terminated as part of the offboarding? (3) For MCP servers specifically: are there registered clients that will lose access? These clients need to be notified and their configurations updated.

---

## The Full Request Lifecycle (Summary)

```
CHANGE REQUEST:
Asset owner initiates → AI steward reviews → Approve/Reject
    → If Approved: Change tasks auto-generated → Asset owners complete tasks
        → New AI asset record auto-created → Request Completed

OFFBOARDING REQUEST:
Asset owner initiates → AI steward reviews → Approve
    → Offboarding workflow triggered → Tasks assigned to impacted asset owners
        → All tasks completed → Asset Status = Retired → Request Completed
```

---

## Key Takeaways for AI Risk & Compliance Officers

1. **Change requests govern post-deployment relationship changes** — any update to a deployed asset's linked models, datasets, prompts, or tools must go through a change request.
2. **Offboarding requests govern retirement** — deployed assets cannot be informally decommissioned; the offboarding workflow is required to set status to Retired.
3. **Three-criteria check (Deployed + Deploy + Deployed) enforces change control on deployed assets only** — governance applies to the full deployed lifecycle, not just initial approval.
4. **Change request approval auto-creates a new asset record** — this is the version history mechanism; each approved change creates a new versioned governance record.
5. **Offboarding workflow surfaces impacted assets** — before approving retirement, review all downstream assets that may be affected.
6. **MCP servers can be offboarded** — they are explicitly listed as eligible for offboarding requests, enabling governed retirement of MCP server connections.
7. **Deprecation date automation** — setting a deprecation date on a model triggers offboarding automatically; use this to enforce planned decommissioning timelines.
8. **Justification fields are governance evidence** — substantive justifications for both change and offboarding requests are part of the audit trail.

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 835–840*
