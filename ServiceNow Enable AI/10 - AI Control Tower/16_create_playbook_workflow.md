# Create an AI Control Tower Playbook Workflow
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Role: AI Risk & Compliance Officer Reference

---

## What Is This?

The AI Control Tower Playbook Workflow is the structured, step-by-step governance process that an AI steward follows to review, evaluate, and approve or reject an AI asset. It is the operational heart of AICT governance — the mechanism that takes an asset from "submitted for review" to "approved for deployment" through a documented, auditable sequence.

Understanding this topic is essential for Risk & Compliance Officers because the playbook workflow is where governance decisions are made and recorded. Every risk score, every close note, every task assignment in the Assess stage is captured here and becomes the permanent audit trail for that asset.

---

## Critical Prerequisite: Automatic Triggering

> **Important:** The AI Control Tower Approval Playbook for the Now Assist approval is NOT created manually. It is automatically triggered when an approval request is created while the approval mandate is enabled.

**Requirement:** The "Automatically trigger playbooks" feature must be activated under `Configurations > Controls`.

Without this setting active, no playbook is created when an asset is submitted. The AI steward would have to manually initiate approval requests — creating governance gaps where assets can be submitted without triggering any workflow.

---

## Accessing the Playbook Workflow

**Role required:** `sn_ai_governance_ai_steward`

**Navigation:**
1. `Workspaces > AI Control Tower`
2. Open the AI assets view
3. Navigate to **Now Assist Approvals** in the navigation menu
4. Open an Approval request record
5. Select the **Playbook tab** to see the Now Assist Approvals workflow

---

## The Three Playbook Stages

### Stage 1: Review Asset

**What happens:**
- The AI steward can view ALL details of the asset under review
- Full asset record is visible: name, provider, type, use & purpose fields, related assets (models, datasets, prompts, tools)
- This is a read-only assessment of what has been submitted

**Action to advance:**
- Select **Next**
- The approval status changes when the Review asset step is marked as complete

**What to look for during Review:**
- Is the asset description complete and accurate?
- Are all related assets (models, datasets, prompts) correctly linked?
- Is the Use & purpose section filled in — intended outcome, autonomy level, type of output, data used, people affected?
- Are there any obvious red flags before deeper evaluation begins?

> **Risk Officer Note:** The Review Asset stage is the first gate. An incomplete asset record should stop here — do not advance to Evaluate if the asset description is inadequate. The steward should send it back for completion rather than proceed with incomplete information. A risk score based on incomplete data is worse than no risk score because it creates false assurance.

---

### Stage 2: Evaluate Asset

**What happens:**
- AI stewards can create and assign **approval tasks** to other individual AI stewards to evaluate the asset
- Tasks can be for any review type: Legal review, Security review, Data review, Privacy review, etc.
- Each task is assigned to a specific person with a due date
- Task list management: tasks can be Copied, Deleted, or created via **New** in the Approval tasks list

**Action to advance:**
- Complete all assigned evaluation tasks
- Each evaluating steward marks their task as complete with close notes

**What evaluation tasks should cover (for a Risk & Compliance context):**

| Task Type | What It Reviews |
|---|---|
| Legal review | Regulatory compliance, terms of service, liability |
| Security review | Authentication, access controls, data security, vulnerability assessment |
| Data review | Data sources, data quality, PII handling, consent, retention |
| Privacy review | HIPAA/GDPR compliance, data subject rights, data flows |
| Ethics review | Bias, fairness, transparency, explainability |
| Architecture review | System design, scalability, integration risks |
| Stakeholder review | Business approval, impacted stakeholder sign-off |

> **Risk Officer Note:** The evaluation task system is how cross-functional review is operationalized within AICT. For CareAtlas (healthcare), at minimum every AI system affecting patient data should have: (1) a Data Privacy review task, (2) a Security review task, and (3) a Legal/Regulatory review task that explicitly confirms HIPAA compliance. These are not optional — they are the governance evidence that an asset was properly evaluated before deployment. Create these tasks as standard for every patient-facing AI system.

---

### Stage 3: Approve or Reject

**What happens:**
- The AI steward reviews all evaluation task outcomes
- Selects a **Risk score** from the drop-down menu
- Enters **Close notes** documenting the rationale for the decision
- Selects either **Approve asset** or **Reject asset**

**Critical constraint:**
> "The Risk score and Close notes can't be modified after the Approve/Reject step is marked as complete."

This is a data integrity control — once the decision is made and recorded, it is permanent and auditable. The risk score and close notes become immutable governance records.

**Risk score selection:**
The risk score assigned here becomes the asset's Risk classification in AICT. This is one of two paths to risk classification:
1. **Manual selection** — the AI steward picks the risk score at this stage based on evaluation task outcomes
2. **Assessment-driven** — if the AIRC content pack is installed and an Impact Assessment questionnaire was run, the score can be auto-calculated from questionnaire responses and pre-populated as a recommendation

> **Risk Officer Note:** The permanence of risk score and close notes after approval is both a governance strength and a governance obligation. Before clicking Approve or Reject, the AI steward must be confident in the risk score because it cannot be corrected afterward — only a new review cycle (via a change request) can update it. Establish a standard that close notes must include: (1) summary of evaluation task outcomes, (2) basis for the risk score selected, (3) any conditions or constraints on the approval (e.g., "approved for internal use only, not patient-facing").

---

## What Happens After Approval

> "If you need to activate any skill from Now Assist Admin, an approval request is now required. The AI Control Tower approvals are integrated with both the builder team on the Skill Kit and Now Assist Admin. You may only use models, skills, or AI systems that have been approved."

Post-approval, AICT enforces the approval:
- Skills cannot be activated in Now Assist Admin without a completed approval record
- Integration with Skill Kit means the builder team cannot publish without governance clearance
- MCP servers cannot be used in AI Agent Studio until approved (when MCP server approval control is active)

This makes the playbook workflow not just a documentation exercise — it is an **enforcement mechanism** that blocks deployment of unapproved assets.

---

## Cancel Option

At any step in the playbook, the AI steward can select **Cancel approval request** to cancel the workflow. This stops the process and records the cancellation in the approval record. This should be used when:
- An asset is found to be duplicating an existing approved asset
- The asset owner withdraws the submission
- The asset fails a preliminary review check and needs to be resubmitted from scratch

---

## Playbook Customization

The pre-built Now Assist Approval playbook can be customized:
- Number of steps can be increased or rearranged
- Different security policies can be applied at different steps
- Custom steps (e.g., HIPAA compliance validation, data privacy review) can be added

Any customization of the playbook template should go through change management — the playbook defines the governance controls applied to every asset.

---

## Key Takeaways for AI Risk & Compliance Officers

1. **Playbooks are auto-triggered, not manually created** — "Automatically trigger playbooks" must be active in Configurations or no governance workflow fires.
2. **Three stages: Review → Evaluate → Approve/Reject** — each stage is a distinct governance gate.
3. **Evaluation tasks are the cross-functional review mechanism** — use them to assign Legal, Security, Data Privacy, and Ethics reviews as standard for patient-facing AI assets.
4. **Risk score and close notes are permanent after approval** — treat them as formal legal and governance records; they cannot be corrected post-approval.
5. **The playbook workflow is an enforcement mechanism** — approved AI assets cannot be deployed via Now Assist Admin or Skill Kit without completing this workflow.
6. **Cancellation is an option** — use it cleanly rather than abandoning incomplete workflows; cancelled approvals are still audit trail entries.

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 822–823*
