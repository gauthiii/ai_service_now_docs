# Create a Now Assist Approval Task
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Role: AI Risk & Compliance Officer Reference

---

## What Is This?

A Now Assist Approval Task is a **sub-task of an approval request** created during the Evaluate Asset stage of the playbook workflow. It is the mechanism for delegating specific review activities — Legal, Security, Data Privacy, Ethics, Architecture — to individual reviewers across the organization. Each task produces a documented outcome that feeds into the AI steward's final Approve/Reject decision.

---

## Purpose and Context

> "The Now Assist approval task is a sub task of an approval request where you will need approvals from other organizations or entities like Legal review, Security review, Data review, Privacy review etc."

**Where it fits in the workflow:**
```
Playbook Stage 2: Evaluate Asset
    └── Create new task (one per review type)
        ├── Legal review task → assigned to Legal team
        ├── Security review task → assigned to Security team
        ├── Data review task → assigned to Data team
        └── Privacy review task → assigned to Privacy/DPO team
```

Each task is independent — it can be assigned to a different person, have a different due date, and be completed at different times. The Evaluate Asset stage is not complete until all assigned tasks are marked complete.

---

## Prerequisites

**Prerequisite:** The **Review asset** step in the Playbook must be marked as complete before creating evaluation tasks. You cannot create evaluation tasks while the Review Asset stage is still open.

**Role required:** `admin`

---

## Procedure

**Navigation:** `Now Assist Approvals > open an Approval record > Playbook section`

1. Confirm the **Review asset step is marked as complete**
2. Select **Create new task** under Evaluate asset
3. A new approval task is created — **task number and task type fields are auto-populated**
4. Fill in the following fields:

| Field | Description | Notes |
|---|---|---|
| Short description | Brief description of the review task | e.g., "Legal review for Patient Data Agent" |
| Description | Detailed description of what the reviewer should evaluate | Include specific questions or criteria |
| Due date | When the review must be completed | Set realistic timelines; this drives overdue tracking |
| Close notes | Summary of findings after review is complete | Completed by the assigned reviewer |
| Priority | Urgency of this specific review | Critical / High / Moderate / Low / Planning |
| State | Current state of the task | Open → In Progress → Completed |
| Status | Approval status outcome | Not yet requested → Requested → Approved → Rejected |
| Assigned to | Individual responsible for completing this review | Search and select the reviewer |
| Parent approval record | Links this task to the parent approval | **Auto-populated; read-only** |

5. Select **Save**

**Result:** A Now Assist Approval task is created and linked to the parent approval request.

---

## Task Management Options

From the Approval tasks list within the Evaluate Asset stage, you can:
- **Copy** a task — useful for creating similar tasks across multiple reviewers (e.g., two Legal reviewers)
- **Delete** a task — remove tasks that were created in error
- **New** — create additional tasks during the evaluation phase

---

## Review Task Design for Healthcare AI (CareAtlas)

For a healthcare context, standard evaluation task types and their reviewer assignments should be:

| Task Type | Suggested Assignee | What the Review Covers |
|---|---|---|
| **Legal & Regulatory Review** | Legal / Compliance Officer | HIPAA applicability, BAA requirements, FDA SaMD classification if applicable, state privacy laws |
| **Data Privacy Review** | Data Protection Officer / Privacy team | Data types used (PHI, PII), consent mechanisms, data flows, retention and deletion controls |
| **Security Review** | Information Security / CISO team | Authentication, authorization, encryption, vulnerability assessment, OWASP AI Top 10 review |
| **Clinical Safety Review** | Chief Medical Officer / Clinical team | Patient safety implications if AI output is acted upon clinically, error rate tolerance |
| **Architecture Review** | Enterprise Architecture team | Integration design, dependency risks, scalability, failure modes |
| **Ethical AI Review** | AI Ethics committee / Risk team | Bias assessment, fairness across patient populations, transparency and explainability |
| **Vendor Risk Review** | Vendor Management / Procurement | Third-party provider assessment, data processing agreements, SLA review |

> **Risk Officer Note:** The task design above represents the minimum review standard for patient-facing AI systems in a healthcare environment. Create a standard set of task templates for each AI system category (Agentic AI, Generative AI, Classic AI) to ensure consistent evaluation coverage across all assets. Document these templates in your AI governance policy so the playbook is consistently applied regardless of which AI steward is running the review.

---

## What Happens When Tasks Are Completed

Each reviewer:
1. Opens their assigned task
2. Performs their domain-specific review
3. Enters their findings in **Close notes**
4. Sets **Status** to Approved or Rejected based on their review outcome
5. Changes **State** to Completed

After all tasks across the Evaluate Asset stage are completed, the AI steward reviews all outcomes in aggregate and proceeds to the final Approve/Reject decision in Stage 3.

> **Risk Officer Note:** A single Rejected evaluation task does not automatically block approval — the AI steward makes the final call. However, if a Legal or Security evaluation task is Rejected (e.g., "This system requires a BAA that is not yet in place"), the AI steward should NOT approve the asset until the blocking issue is resolved. Establish a governance policy that defines which task types are **hard blockers** (approval cannot proceed until resolved) vs. **advisory findings** (documented risk accepted). For healthcare: Legal, Data Privacy, and Security reviews are hard blockers; Architecture and Vendor reviews are advisory unless they identify critical findings.

---

## Relationship to the Value Template Review Task

During the Assess stage (the first lifecycle stage, distinct from the approval playbook), a **Value Template review and approval task** is also auto-created. This is not the same as an evaluation task in the approval workflow.

| Task Type | Stage | Purpose | Creator |
|---|---|---|---|
| Value Template review and approval | Assess (lifecycle stage) | Verify that the correct value template is mapped to the asset | Auto-created by AICT |
| Now Assist Approval task | Evaluate Asset (approval playbook) | Domain-specific review (Legal, Security, Privacy, etc.) | Manually created by AI steward |

Both types of tasks must be completed for the full governance workflow to be satisfied.

---

## Audit Trail from Tasks

Every approval task creates the following audit evidence:
- Task number (system-generated, immutable)
- Assigned reviewer identity
- Creation date and due date
- Close notes (reviewer's documented findings)
- Completion date
- Status outcome (Approved / Rejected)
- Parent approval record linkage

This audit trail is retrievable from:
- The parent approval record → Evaluate asset section → task list
- The AI steward's task queue
- The individual asset record → Requests tab

> **Risk Officer Note:** The audit trail from evaluation tasks is your primary governance evidence in the event of a regulatory inquiry. Ensure that: (1) every evaluation task has substantive close notes, not just "reviewed and approved" — regulators want to see what was reviewed and what was found; (2) task due dates are realistic and overdue tasks are escalated; (3) the person assigned to each task has the competence and authority to make that domain judgment.

---

## Key Takeaways for AI Risk & Compliance Officers

1. **Approval tasks are the cross-functional review mechanism** — they are how Legal, Security, Privacy, and Ethics reviews are formally documented within AICT's governance record.
2. **Review Asset must be complete before creating evaluation tasks** — you cannot skip the Review stage.
3. **Role required is admin** — the AI steward (or admin) creates tasks; the reviewers can have any appropriate role.
4. **Parent approval record auto-populates** — the task is automatically linked to its parent; no manual linkage needed.
5. **Close notes are the substantive governance evidence** — they must be specific and findings-based, not generic sign-offs.
6. **Define hard-blocker vs. advisory task types in policy** — without this definition, a Rejected security task may be overridden, creating liability.
7. **Task audit trail is permanent** — all task records, outcomes, and notes are retained as part of the approval record.

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 823–824*
