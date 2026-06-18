# Create an AI Case in the AI Control Tower
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Role: AI Risk & Compliance Officer Reference

---

## What Is This?

An AI case is the formal record for documenting, investigating, tracking, and resolving **incidents, risks, or compliance concerns related to AI systems**. It is the escalation mechanism that turns an AI governance concern into a structured, time-tracked, accountable workflow with a documented audit trail.

For a Risk & Compliance Officer, AI cases are the operational evidence of your organization's ability to detect and respond to AI failures, compliance violations, and adversarial events. They are the incident management layer of AI governance — and the records that would be produced in response to a regulatory inquiry or audit.

---

## When to Create an AI Case

AI cases should be created when:
- An AI system produces incorrect, biased, or harmful outputs
- An adversarial attack (prompt injection, model manipulation) is suspected or detected
- A data breach involving AI-processed data is discovered
- A regulatory violation involving an AI system is identified
- A compliance concern about an AI asset requires formal investigation
- A stakeholder reports a governance concern about an AI deployment

---

## Role Required

- `sn_ai_case_mgmt.ai_case_analyst` — can create and work on AI cases
- `sn_ai_case_mgmt.ai_case_manager` — can manage all AI cases and inquiries

---

## Procedure

1. Navigate to `All > AI Control Tower`
2. Go to the **AI cases dashboard**
3. On the AI cases tab, select **Create AI case**
4. Fill in the form fields (see full reference below)
5. Select **Save**

> "After you submit this form, the AI case team will provide the insights and support you need."

---

## Complete AI Case Form — Field Reference

### Identification Section

| Field | Description | Notes |
|---|---|---|
| **Number** | Auto-generated case number | System-assigned; immutable |
| **Name** | Name of the AI case | Example: "Incorrect AI recommendation in patient triage" |
| **Description** | Detailed description of the case | Include: expected behavior, actual behavior, context, impact, steps to reproduce. Especially important for "Incorrect AI Recommendation" type cases |
| **Type** | Case type | Auto-set to "AI case" |
| **Sub-type** | Category of the case | See sub-type reference below |
| **State** | Workflow state | Auto-set to "New" |

### Priority

| Priority Level | Meaning |
|---|---|
| **Critical** | Immediate threat to operations, compliance, or patient safety |
| **High** | Significant impact requiring urgent attention |
| **Moderate** | Meaningful impact but not immediately critical |
| **Low** | Minor concern that can be addressed in normal workflow |
| **Planning** | Anticipated future concern being tracked proactively |

### People Section

| Field | Description |
|---|---|
| **Requester** | Person who raised the case |
| **Requested on behalf of** | Person the case was created for (if different from requester) |
| **Primary entity** | Entity impacted by the AI case — only entities identified in impacted areas are selectable |
| **Entity owner** | Auto-set based on entity selected in Impacted areas related list |
| **Assignment group** | Group assigned to the case — preconfigured to request type during setup |
| **Case analyst** | Analyst who will analyze and work on the case — part of the Assignment group |
| **Watch list** | Persons who must be informed about the case |
| **Accountable executive** | Person accountable for case resolution |

### Primary Origin Section

| Field | Description |
|---|---|
| **Location** | Location where the AI case occurred (e.g., Japan, Phoenix) |
| **Sub-location** | Sub-location detail (e.g., Tokyo, Phoenix AZ) |
| **Impacted business unit** | Business unit affected (e.g., Finance, Clinical Operations) |
| **Impacted department** | Department affected (e.g., Customer Support, Patient Services) |
| **Source** | Auto-set to "Manual" (manual creation) or "Employee Center" (if reported through Employee Center) |
| **Additional source** | Reporting mode when Source = Manual. Options: Email, Phone |

### Schedule Section

| Field | Description | Governance Importance |
|---|---|---|
| **Date of occurrence** | When the AI case event occurred | Start of the incident timeline |
| **Date of discovery** | When the case was discovered | Gap between occurrence and discovery = detection latency KPI |
| **Reported date** | Date the case is formally reported | Regulatory reporting timeline starts here |
| **Case closure SLA** | Expected date of case closure | SLA management |
| **Investigation planned start** | Planned start of investigation | Planning timeline |
| **Investigation actual start** | Actual start of investigation | Variance from planned = response efficiency metric |
| **Investigation planned end** | Planned end of investigation | — |
| **Investigation actual end** | Actual end of investigation | — |
| **Remediation planned start** | Planned start of remediation | — |
| **Remediation actual start** | Actual start of remediation | — |
| **Remediation planned end** | Planned end of remediation | — |
| **Remediation actual end** | Actual end of remediation | — |

> **Risk Officer Note:** The gap between **Date of occurrence** and **Date of discovery** is one of the most important metrics in AI incident governance. Regulatory frameworks like GDPR require breach notification within 72 hours of discovery (not occurrence). A large occurrence-to-discovery gap indicates inadequate monitoring — your AI guardrails are not detecting issues in time. Track this metric across all AI cases as a governance KPI.

### Breach Analysis Section

| Field | Options | Description |
|---|---|---|
| **Breach status** | To be determined (default), Breach detected, Future potential, Not a breach | Whether a data breach occurred |
| **Breach start** | Date | Only appears when Breach detected or Future potential selected |
| **Breach end** | Date | Only appears when Breach detected or Future potential selected |
| **Breach significance identified** | Date | When the breach significance was identified — triggers regulatory notification timelines |
| **Reporting status** | To be determined (default), Reportable | Auto-set based on reporting status of associated regulations. **If any one associated regulation is reportable, the entire case is set to Reportable** |

> **Risk Officer Note:** The Reporting status field is critical for regulatory compliance. It is automatically determined by the regulations associated with the case. If GDPR, HIPAA, or EU AI Act is linked to the case and any one of them triggers a reportable threshold, the case status becomes "Reportable." This should immediately trigger your regulatory notification process. Do not wait for the case to be fully resolved before notifying regulators — the notification deadline runs from Breach significance identified, not from case closure.

### Root Cause Analysis Section

| Field | Description |
|---|---|
| **Primary cause** | Auto-set to the primary cause selected in the Cause and consequences related list |
| **Primary consequence** | Consequences of the primary cause |
| **Overall observations** | Observations made regarding the AI case |
| **Remediation taken** | Yes / No — whether remediation measures have been taken |
| **Overall preventive measures** | Preventive measures taken toward the case |

### Activity Section

| Field | Description |
|---|---|
| **Work notes (Private)** | Internal notes — not visible to external parties |
| **Additional comments (Customer visible)** | Notes visible to customers/reporters |

---

## AI Case Sub-Types Reference

The Sub-type field categorizes the nature of the AI case. Select the most accurate sub-type for proper triage and reporting:

The documentation example cites: **Adversarial attacks** (Deliberate manipulation of AI models to produce incorrect results).

Other relevant sub-types for healthcare AI contexts include:
- **Incorrect AI recommendation** — documented as a primary example in the form
- **Data breach** — referenced in Issue types (unauthorized access, disclosure, or loss of sensitive/personal data)
- **Non-compliance to a regulation** — regulatory violation involving an AI system
- **Bias or fairness concern** — discriminatory outputs from an AI system
- **Model drift** — AI system performance degradation over time
- **Unauthorized access** — AI agent accessed resources beyond its permissions

> **Risk Officer Note:** Sub-type selection drives downstream routing (assignment group) and reporting categorization. Adversarial attack cases should route to your cybersecurity incident response team. Data breach cases should simultaneously trigger your HIPAA breach response plan. Bias/fairness cases should route to your AI ethics function. Establish sub-type-to-team routing rules in your AICT configuration before go-live so cases are automatically assigned to the right team on creation.

---

## AI Case Workflow States

| State | Meaning |
|---|---|
| New | Just created; not yet triaged |
| Triage | Under initial assessment |
| In progress | Investigation/remediation underway |
| Resolved | Issue resolved; pending closure |
| Closed | Case formally closed |

---

## Relationship to AI Issues

AI cases and AI issues are distinct but linked:
- **AI case** — the top-level record for the incident/concern (creates with `Create AI case`)
- **AI issue** — a subordinate record linked to an AI case that identifies and manages specific issues within the impacted areas (creates with `Create issue` from the AI cases dashboard)

The AI cases dashboard has both a `Create AI case` button and a `Create issue` button — they create different but related records. An AI case may generate multiple linked AI issues.

---

## Key Takeaways for AI Risk & Compliance Officers

1. **AI cases are your incident management records** — they are the evidence that your organization detected, investigated, and remediated AI failures; maintain them as formal legal and regulatory records.
2. **Date of occurrence vs. Date of discovery gap = detection latency KPI** — track this across all cases; large gaps indicate inadequate monitoring.
3. **Reporting status is auto-determined by linked regulations** — any linked reportable regulation makes the entire case Reportable; this triggers your regulatory notification SLA.
4. **Sub-type drives routing** — configure sub-type-to-assignment-group routing rules before go-live to ensure adversarial attacks, data breaches, and compliance violations each route to the correct response team.
5. **Breach significance identified date starts regulatory clock** — for GDPR: 72-hour notification requirement begins here; for HIPAA: 60-day notification begins here.
6. **Cases from Employee Center** show Source = Employee Center — this enables you to track how cases are being reported (manual, email, phone, self-service portal).
7. **Root cause analysis fields drive preventive governance** — document primary causes and preventive measures rigorously; these are what regulators ask for in post-incident reviews.

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 851–854*
