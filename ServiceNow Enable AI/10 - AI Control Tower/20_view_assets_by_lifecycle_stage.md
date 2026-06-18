# View AI Assets by Life-Cycle Stage / Enable or Disable Management / Complete AI Asset Lifecycle
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Role: AI Risk & Compliance Officer Reference

---

## What Is This?

This topic covers three closely related operational functions that together provide the governance view and control over AI assets in motion through the lifecycle:

1. **View AI assets by life-cycle stage** — the monitoring function; see which assets are at which governance stage
2. **Enable or disable the management of an AI asset** — the control function; move assets between Managed and Unmanaged states
3. **Complete AI asset lifecycle** — the execution function; how the AI steward works through the formal Assess → Build and Test → Deploy lifecycle stages

These three functions are the day-to-day operational governance activities of the AI Steward role, and the monitoring surface for the Risk & Compliance Officer.

---

## Part 1: View AI Assets by Life-Cycle Stage

### Purpose

To monitor which AI assets are currently in each stage of the governance lifecycle, and to determine which assets require immediate attention.

### Role Required

`sn_ai_governance.ai_steward` OR `sn_ai_asset_mgmt.ai_asset_owner`

### Navigation

`Workspaces > AI Control Tower > AI assets view > Lifecycle section` (left navigation menu)

### The Four Lifecycle Stages (as Navigation Subsections)

| Lifecycle Stage | What You See | Governance Meaning |
|---|---|---|
| **New** | Assets recently submitted or auto-synced; no review started | These need AI steward attention to start the review process |
| **Assess** | Assets currently in the assessment phase | Active governance in progress; tasks assigned and being evaluated |
| **Build and test** | Assets in development and testing phase | Pre-deployment testing and validation underway |
| **Deploy** | Assets approved and deployed | Live in production; change requests or offboarding applies |

**Additional option:** Select `Cancel` to cancel an AI asset from any lifecycle stage.

### What You Can Do From the Lifecycle View

After selecting an asset from any lifecycle subsection:

| Action | How to Access | What It Does |
|---|---|---|
| Start lifecycle review | Select `Start review` | Initiates the lifecycle review process from New |
| Continue review in progress | `Lifecycle tab > follow Complete AI asset lifecycle steps` | Resumes a review already started |
| View / modify general details | `Details tab > Details > Details` | Edits the asset's core metadata |
| View / modify use and purpose | `Details tab > Details > Use & purpose` | Edits the intended use and purpose (AI systems only) |
| View / modify / add related assets | `Details tab > Related assets section > [subsection]` | Manages linked models, datasets, prompts, tools |
| View evaluation metrics | `KPIs & metrics tab` | Performance metrics (AI systems and AI models only) |
| View / modify value templates | `Value template tab` | Productivity value calculation templates (AI systems only) |
| View associated requests | `Requests tab` | Onboarding, change, and offboarding requests |
| View evaluation templates | `Evaluation template tab` | Enabled evaluations (AI systems only) |

> **Risk Officer Note:** The lifecycle view is your governance monitoring dashboard at the asset level. From a compliance standpoint, the most important subsection is **New** — assets that have been in "New" status for more than a defined period (e.g., 5 business days) represent governance backlog. Assets sitting in New stage are technically in the inventory but have received no formal governance review. Establish a KPI: zero assets in New stage beyond your defined review SLA.

### Adding Related Assets from the Lifecycle View

When viewing a lifecycle asset and navigating to the Related assets section, two options are available:
- **Add from inventory** — link an existing asset from the inventory
- **Create** — create a new related asset inline

The Create option is NOT available for related AI tools.

---

## Part 2: Enable or Disable Management of an AI Asset

### Purpose

To control whether a specific AI asset is governed by AICT (Managed) or merely visible in the inventory (Unmanaged).

### Role Required

`sn_ai_governance.ai_steward` (only)

**Default:** All assets created through the AI Control Tower application are **automatically designated as Managed**.

Assets discovered via auto-sync (Now Assist, Enterprise AI Discovery) are **Unmanaged by default** until explicitly moved to Managed.

### Managed vs. Unmanaged — What Each State Means

**Managed — You CAN:**
- Perform all lifecycle management processes
- Create requests (onboarding, change, offboarding)
- Determine risk classification
- Calculate value metrics
- Run quality assessments
- Apply safety controls and evaluations

**Unmanaged — You CANNOT:**
- Perform any of the above
- The asset is visible in the inventory but has no governance applied

**Important consequence of moving Managed → Unmanaged:**
> "The life-cycle review process, risk classification, value template calculations, and evaluations for the asset are automatically canceled."

And for value templates:
> "When you change an AI asset state from Managed to Unmanaged, the associated value template state automatically changes from Published to Unmanaged and Draft to Retired. Existing value template mappings remain same, but the AI asset is excluded from value calculations. When you again change the AI asset to Managed state, the value template state (only Unmanaged mappings) automatically reverts to Published."

This means governance can be restored — but the cancellation of the lifecycle review, risk classification, and evaluations must be deliberate and documented.

### Enabling Management (Unmanaged → Managed)

1. Navigate to `AI assets view > AI asset inventory - Unmanaged > [asset type subsection]`
2. Select the checkbox for the asset(s) to manage (multiple assets can be selected at once)
3. Select **Move to Managed**
4. In the dialog box, confirm by selecting **Move to Managed**

**Result:** The asset:
- Moves to the corresponding Managed subsection
- Lifecycle review process automatically initiates
- Risk classification process automatically initiates
- Value template calculations automatically initiate
- Evaluations automatically initiate

### Disabling Management (Managed → Unmanaged)

1. Navigate to `AI assets view > AI asset inventory - Managed > [asset type subsection]`
2. Select the checkbox for the asset(s) to unmanage
3. Select **Unmanage**
4. In the dialog box, confirm by selecting **Unmanage**

**Result:** The asset:
- Moves to the corresponding Unmanaged subsection
- Lifecycle review process automatically canceled
- Risk classification automatically canceled
- Value template calculations automatically canceled
- Evaluations automatically canceled

> **Risk Officer Note:** Moving a Managed asset back to Unmanaged is a governance regression — it removes all controls from a previously governed asset. This action should require documented justification and, in a mature governance program, AI steward approval from a second steward (four-eyes principle). Establish a governance policy: (1) Unmanage actions must be documented with business justification, (2) Unmanage of a Deployed (production) asset requires senior AI steward or CISO approval, (3) All Unmanage actions are logged in the audit trail and reviewed in monthly governance reports.

---

## Part 3: Complete AI Asset Lifecycle

### Purpose

The step-by-step execution of the formal lifecycle review process — from the initial assessment through to deployment. This is the AI steward's primary governance workflow activity.

### Role Required

`sn_ai_governance.ai_steward` OR `sn_ai_asset_mgmt.ai_asset_owner`

### Full Lifecycle Procedure

**Navigation:** `Workspaces > AI Control Tower > AI assets view > locate and open an asset with Lifecycle status = AI steward review`

**Step 1: Initiate the lifecycle**
- Select **Start review** from the asset record view
- This formally begins the lifecycle process

**Step 2: Assess stage — create and complete tasks**

Navigate to the `Lifecycle tab > Assess`

> "The AI steward can manually create tasks under Lifecycle > Assess and assign them to an asset owner. The asset owner or the AI steward can mark this task as complete and move on to the next stage."

**Tasks in the Assess stage include:**
- **Value Template review and approval task** (auto-created) — verify the correct value template is mapped and calculations are valid
- **Impact assessment task** (auto-created when AIRC content pack is installed) — the risk questionnaire that drives automatic risk score calculation
- Additional custom tasks created by the AI steward

**How Assess tasks work:**
- AI steward creates tasks and assigns them (to self, to asset owner, or to other stewards)
- Task assignees complete their reviews and mark tasks Complete
- Complete button marks the individual task as done
- When all tasks in Assess are complete, the stage advances

**Step 3: Build and test stage**

Navigate to `Lifecycle tab > Build and Test`

> "An AI steward can create tasks in the Development plan and Pre-deployment assessments phases, marking the tasks as complete in both the phases using the Complete button."

**Two sub-phases within Build and Test:**
1. **Development plan** — tasks for development activities
2. **Pre-deployment assessments** — tasks for pre-deployment validation

> **Risk Officer Note:** The Build and Test stage is where security testing, performance benchmarking, and HIPAA compliance validation should occur for healthcare AI assets. For each agentic AI system in CareAtlas, minimum Build and Test tasks should include: (1) Penetration testing / security scan, (2) Performance load testing, (3) HIPAA compliance checklist review, (4) Patient data handling validation, (5) Fail-safe and error handling verification. These are not optional — they are the technical governance gates before deployment.

**Step 4: Deploy stage**

Navigate to `Lifecycle tab > Deploy`

> "To create tasks and complete the AI asset Lifecycle, select Deploy. The asset owner can mark the task as complete."

Deploy tasks may include:
- Final deployment checklist
- Production access provisioning
- Monitoring configuration
- Documentation sign-off

**Step 5: Result**

> "The lifecycle status of an AI asset is deployed and completed."

The asset's:
- Lifecycle phase → Deploy
- Lifecycle status → Deployed
- Risk classification → Set from the Assess stage assessment (or manually assigned during approval)
- State → Deployed

### Visual Reference from Documentation

The documentation references three lifecycle stage screenshots:
- **AI Asset Lifecycle — Assess** — shows task creation and completion in Assess stage
- **AI Asset Lifecycle — Build and Test** — shows Development plan and Pre-deployment assessment sub-phases
- **AI Asset Lifecycle — Deploy** — shows Deploy stage task completion

---

## The Three Functions Together: Governance Flow

```
DISCOVER (via auto-sync or manual creation)
    |
    v
UNMANAGED state (default for discovered assets)
    |
    v [Move to Managed — AI steward decision]
MANAGED state
    |
    v [Start Review]
Lifecycle stage: NEW
    |
    v [View from Lifecycle > New → Start review]
Lifecycle stage: ASSESS
    → Create tasks (value template review, impact assessment, custom tasks)
    → Assign to stewards / asset owners
    → All tasks completed
    |
    v
Lifecycle stage: BUILD AND TEST
    → Create tasks (Development plan + Pre-deployment assessments)
    → Complete all tasks
    |
    v
Lifecycle stage: DEPLOY
    → Create and complete deployment tasks
    |
    v
Lifecycle status: DEPLOYED
    → Asset is live, governed, risk classified, value calculated
    |
    v [Post-deployment governance]
    → Change requests for relationship updates
    → Offboarding requests for retirement
    |
    v [Risk re-assessment]
    → Change request approved → New asset record created → Re-enters lifecycle
```

---

## Key Takeaways for AI Risk & Compliance Officers

1. **New stage = governance backlog** — establish a SLA for reviewing assets in New stage (e.g., 5 business days); overdue New-stage assets are governance findings.
2. **Move to Managed triggers all governance processes automatically** — risk classification, value calculation, and evaluations all start on transition to Managed.
3. **Unmanage cancels all governance** — treat Unmanage of a production asset as a high-severity governance event requiring senior approval and documented justification.
4. **Value template state automatically shifts with Managed/Unmanaged** — Published → Unmanaged → reverts to Published on re-management; understand this before toggling states.
5. **Assess stage drives the risk score** — the Impact Assessment task in Assess is where the automated risk score is generated; this stage must not be rushed.
6. **Build and Test must include security testing** — for healthcare AI, penetration testing and HIPAA compliance validation are non-negotiable Build and Test tasks.
7. **The lifecycle view is your daily governance dashboard** — monitor all four stages; the balance of assets across stages tells you about governance health.
8. **Start review is irreversible within the lifecycle** — once initiated, the lifecycle progresses forward; cancellation is possible but creates an audit record.

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 840–854*
