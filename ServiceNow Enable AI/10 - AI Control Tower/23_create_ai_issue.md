# Create an AI Issue in the AI Control Tower
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Role: AI Risk & Compliance Officer Reference

---

## What Is This?

An AI issue is a **subordinate record linked to an AI case** that identifies and manages specific problems within the impacted areas of the reported AI case. While the AI case is the top-level incident record, issues are the granular, actionable findings that emerge from the case investigation — each with its own type classification, priority, assignment, action plan, and resolution timeline.

Think of it this way: an AI case says "there was a problem with our patient triage AI." An AI issue says "the specific problem is: the control for detecting biased recommendations doesn't exist" (Issue type: Control doesn't exist). Multiple issues can be linked to a single case.

---

## Roles Required

- `sn_grc_ai_gov.ai_risk_and_compliance_analyst`
- `sn_grc_ai_gov.ai_risk_and_compliance_manager`

Note: These are **AIRC roles**, not the AICT case management roles — indicating that AI issues are formally part of the AI Risk and Compliance governance framework, not just the case management module.

---

## Procedure

1. Navigate to `All > AI Control Tower`
2. Go to the **AI cases dashboard**
3. On the AI cases tab, select **Create issue**
4. Fill in the form fields (see full reference below)
5. Select **Save**

---

## Complete AI Issue Form — Field Reference

### Identification Section

| Field | Description | Notes |
|---|---|---|
| **Number** | Auto-generated issue number | System-assigned |
| **Name** | Name of the issue | Example: "Cyber Attack on Acme" or "Bias in patient risk model" |
| **Issue source** | Source of the issue | Auto-set to "AI case" when created from the AI cases dashboard |

### Issue Type

The Issue type field is the most governance-significant classification in the entire form. It determines the nature of the finding and drives remediation approach:

| Issue Type | Description | Governance Implication |
|---|---|---|
| **Control design effectiveness failure** | Control was poorly designed and cannot prevent/detect intended risk | Requires control redesign |
| **Control operative effectiveness failure** | Control was well-designed but failed during execution or wasn't followed | Requires process improvement or training |
| **Control doesn't meet requirement** | Control is in place but doesn't satisfy regulatory, policy, or business requirements | Requires control enhancement |
| **Control doesn't exist** | No control present to address a known risk or requirement | Requires new control implementation |
| **Non-compliance to a regulation** | A law or regulation was not followed, potentially exposing the organization to penalties | Immediate regulatory response required |
| **Non-compliance to a policy** | An internal policy was not adhered to | Policy enforcement action required |
| **Improvement or suggestion to an existing policy** | Recommendation to enhance an existing policy | Governance improvement track |
| **Recommendation for a new policy** | Proposal to create a new policy to address a gap | Policy development track |
| **Process optimization or improvement** | Opportunity to improve efficiency, accuracy, or effectiveness | Continuous improvement track |
| **Observation** | General finding that may warrant attention but is not yet a confirmed issue | Watch list item |
| **Data breach** | Unauthorized access, disclosure, or loss of sensitive or personal data | Immediate breach response + regulatory notification |
| **Fraud** | Intentional deception for personal or organizational gain | Legal and security response required |
| **Misstatement** | Errors or omissions in financial or operational reporting | Audit and correction required |
| **Training** | Gaps or needs in knowledge or skills | Training and awareness program required |
| **Documentation** | Missing, outdated, or inaccurate documentation | Documentation update required |
| **Risk issue** | Broad risk-related concern not fitting other categories | Standard risk management response |
| **Other** | Any issue not fitting above types | General tracking |

> **Risk Officer Note:** The four control-related issue types (design failure, operative failure, doesn't meet requirement, doesn't exist) directly correspond to the control assessment outputs in GRC. When an AI control attestation identifies a failure, that failure should be captured as an AI issue with one of these types. This creates the linkage between your control assurance program and your case management system. A pattern of "Control doesn't exist" issues across multiple AI cases signals a systemic governance gap requiring a new control framework, not just individual remediation.

### Classification

| Classification | When to Use |
|---|---|
| **Compliance** | Issue relates to regulatory or policy compliance requirements |
| **Risk** | Issue relates to a risk management concern |
| **Audit** | Issue was identified through an audit finding |
| **Vendor Risk** | Issue relates to a third-party AI provider or vendor |

### Workflow State

| State | Description |
|---|---|
| New | Issue created |
| Analyze | Under analysis — root cause being determined |
| Respond | Response/remediation being implemented |
| Review | Under review for closure approval |
| Closed Complete | Issue resolved and closed |
| Closed Incomplete | Issue closed without full resolution |

**Note:** State is auto-set to **Review** when an issue is created from an AI case (the issue source being the case triggers the Review state as the initial state for analyst-reviewed issues).

### Priority

| Priority | Meaning |
|---|---|
| Critical | Immediate threat; requires same-day response |
| High | Significant urgency; requires response within SLA |
| Moderate | Standard urgency; can be addressed in normal workflow |
| Low | Minor; can be backlogged |
| Planning | Anticipated future concern |

**Note:** Priority is auto-set to **Review** (same as State) when created from an AI case — meaning the initial triage is considered part of the Review state workflow.

### Issue Rating

Separate from priority, Issue rating assesses the **severity or magnitude** of the issue:

| Rating | Description |
|---|---|
| Very High | Maximum severity |
| High | Significant severity |
| Moderate | Moderate severity |
| Low | Minor severity |
| Very Low | Minimal severity |

> **Risk Officer Note:** Priority and Issue rating are distinct: Priority drives response urgency; Issue rating assesses magnitude. A low-priority issue can still have a Very High rating if it is severe but not time-sensitive. Use both dimensions together: a Critical + Very High issue is a P1 emergency; a Low + Very Low issue can be scheduled for routine remediation. Document the rationale for both ratings in the Description field.

### Description

| Field | Notes |
|---|---|
| **Description** | Detailed description of the issue. Example: "ACME experienced a cyber attack that resulted in unauthorized access to internal systems." For AI issues, include: what the specific issue is, how it manifests in the AI system, which controls are affected, and the potential regulatory impact. |

### Assignment

| Field | Description |
|---|---|
| **Assignment group** | Group assigned to the issue (e.g., "Risk Managers") |
| **Assigned to** | Specific user assigned |
| **Issue manager group** | Manager group: Compliance Managers, IT Risk Managers, or Risk Managers |
| **Issue manager** | Specific manager assigned |
| **Watch list** | Persons who must be informed |

### Schedule Section

| Field | Description |
|---|---|
| Due date | When the issue must be resolved |
| Confirmed date | Auto-filled confirmation date |
| Created | Auto-set to current date and time |
| Closed | Date issue is closed |
| Planned start date | Planned start of issue remediation |
| Planned end date | Planned end of issue remediation |
| Duration | Duration in days, hours, minutes, seconds |
| Actual start date | Actual start of remediation |
| Actual end date | Actual end of remediation |
| Actual duration | Actual time taken |

> **Risk Officer Note:** The planned vs. actual dates create the remediation efficiency record. Regulators reviewing your AI governance program will ask: "When you find a control failure, how long does it take to remediate?" The gap between planned and actual end dates answers this. Track this as a governance KPI: average days from issue creation to closure, by issue type and classification.

### Issue Grouping

| Field | Description |
|---|---|
| **Issue group rule** | Group rule for the issue — auto-filled |
| **Parent issue** | Parent issue this issue is associated with (for hierarchical issue tracking) |

### Action Plan Section

| Field | Description | Notes |
|---|---|---|
| **Recommendation** | Recommendation for the issue | Example: "Enhance cybersecurity measures and provide regular security training" |
| **Action plan** | Specific actions to address the issue | Example: "Upgrade the firewall to the latest version and implement multi-factor authentication for all administrative accounts" |

> **Risk Officer Note:** The Recommendation and Action plan fields are what regulators look for in a post-incident review. A completed AI issue record with no action plan is a compliance gap in itself. Every closed issue should have: (1) a specific, measurable recommendation, (2) a specific, time-bound action plan, and (3) documented evidence that the action was completed (in work notes or as an attachment). "Enhance controls" is not an action plan — "Implement PII output screening on Patient Data Agent by [date], assigned to [person], verified by [person]" is.

### Activity Section

| Field | Description |
|---|---|
| **Work notes (Private)** | Internal notes — not visible to external parties |
| **Additional comments (Customer visible)** | Notes visible to customers |

### Settings Section

| Field | Description |
|---|---|
| **Functional domain** | Functional domain the issue belongs to (e.g., AI Risk and Compliance domain) |

---

## Substate Field

The **Substate** field is auto-filled based on the issue's current State. It provides additional granularity within each State. The documentation notes it is auto-filled — the specific substate values are determined by the issue workflow configuration.

---

## AI Case → AI Issue Relationship

```
AI Case (top-level)
  └── AI Issue 1: Control doesn't exist (Classification: Compliance)
  └── AI Issue 2: Data breach (Classification: Risk)
  └── AI Issue 3: Non-compliance to regulation (Classification: Compliance)
```

- One case can have multiple issues
- Each issue is independently assigned, tracked, and resolved
- Issues contribute to the case's overall resolution — the case may not close until all linked issues are resolved or closed incomplete

---

## Key Takeaways for AI Risk & Compliance Officers

1. **AI issues are GRC-role governed** — only AI R&C analysts and managers can create issues; this is a GRC function, not just a case management function.
2. **Issue type drives remediation strategy** — the four control-related types map directly to your control assurance framework; use them consistently to create linkage between case findings and control management.
3. **A pattern of "Control doesn't exist" issues = systemic gap** — if this type recurs across multiple cases and AI systems, it signals that your control framework for AI is fundamentally incomplete.
4. **Priority ≠ Issue rating** — use both dimensions; they answer different questions (when to respond vs. how severe is it).
5. **Action plan fields are regulatory evidence** — specific, time-bound action plans with named owners and verification steps are what auditors and regulators look for in post-incident reviews.
6. **State is auto-set to Review** when created from an AI case — this pre-positions the issue for analyst review immediately.
7. **Planned vs. actual dates create your remediation efficiency record** — track average days to closure by issue type as a governance KPI.
8. **Functional domain field** connects the issue to the AI Risk and Compliance domain for cross-module traceability.

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 855–858*
