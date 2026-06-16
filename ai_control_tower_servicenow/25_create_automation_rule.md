# Create an Automation Rule
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Role: AI Risk & Compliance Officer Reference

---

## What Is This?

Automation rules in AI Control Tower define the conditions under which AI assets are **automatically designated as managed**. They are the scalability mechanism for governance — instead of having an AI steward manually review and move each of the potentially hundreds or thousands of unmanaged assets one by one, automation rules identify assets that meet defined criteria and automatically promote them to Managed status.

For a Risk & Compliance Officer, automation rules are both a governance accelerator and a governance risk. Used correctly, they ensure that certain categories of AI assets enter the governance lifecycle without delay. Used incorrectly, they can create a false impression of governance coverage by bulk-promoting assets to Managed status without meaningful human review.

---

## Core Concept

> "The Automation rules define how AI assets are set to be under managed assets."

> "If an asset is qualified for a rule, it will be automatically moved under managed assets."

The rule evaluates each AI asset against defined conditions. Assets that match the conditions are automatically moved from the Unmanaged inventory to the Managed inventory — which triggers:
- Lifecycle review process initiation
- Risk classification process initiation
- Value template calculation initiation
- Evaluations initiation

This is a significant state change with real governance consequences. The rule is the authorization for all of these processes to begin on an asset that has not had individual human review.

---

## Roles and Permissions

| Action | Role Required |
|---|---|
| Create, modify, or delete automation rules | AI steward |
| View automation rules | AI steward |
| Trigger immediate rule execution | AI steward |

---

## Rule Execution Logic

| Aspect | Detail |
|---|---|
| **Scheduled execution** | The scheduled job **"Run AI Asset Management Rules"** executes **every 6 hours** |
| **Active rules only** | Only active rules are evaluated during scheduled runs — inactive rules are skipped |
| **Immediate execution** | AI stewards can trigger immediate execution on any active rule using the **"Run Now"** action |
| **Qualification** | If an asset qualifies for a rule, it is automatically moved to managed assets |
| **Deletion** | Rules no longer needed can be deleted |

---

## Rule Limits (System Properties)

Administrators can configure system-enforced limits on automation rules:

| System Property | Description | Recommended Default |
|---|---|---|
| `sn_ai_governance.management_rule.max_active_rules` | Maximum number of active rules allowed at any time | 5 |
| `sn_ai_governance.management_rule.max_total_rules` | Maximum total rules in the system (active + inactive) | 10 |

These limits exist to prevent rule proliferation that could:
- Create conflicting governance signals (multiple rules matching the same asset)
- Cause performance issues from overly complex rule evaluations
- Lead to accidental mass-promotion of assets

> **Risk Officer Note:** The default maximum of 5 active rules is deliberately conservative. It forces governance teams to be intentional about which categories of assets deserve automatic management promotion, rather than creating rules for every conceivable scenario. Before creating a new automation rule, document the business justification: what class of assets does this rule target, why is automated promotion appropriate for this class, and how will the AI steward validate that automatically-managed assets still receive meaningful governance review?

---

## Procedure: Create an Automation Rule

**Role required:** AI steward

**Navigation:** `AI Control Tower > Configuration > Controls > Automation rules`

**Steps:**
1. Select **+Create new**
2. Enter the rule name in the **Rule name** field
3. Enter the description of the rule in the **Description** field
4. Select the **Asset** type this rule applies to and define the **conditions**
5. Select the **Activate the rule** check box

**Result:** An automation rule is created for AI assets.

---

## Rule Components

### Rule Name
A unique, descriptive name that clearly identifies what the rule does. Good naming convention: `[Asset Type] - [Condition] - [Action]`

Examples:
- "AI Agents - Provider: ServiceNow - Auto-manage"
- "AI Skills - Active and Published - Auto-manage"
- "Third-party Models - Any - Auto-manage for review"

### Description
Document the business justification for this rule:
- What asset category does it target?
- Why is automatic management promotion appropriate for this category?
- What governance review is still expected after automatic promotion?
- Who approved this rule's creation?

### Asset Selection
Specifies which asset type the rule applies to:
- AI systems
- AI models
- Datasets
- Prompts
- MCP servers

### Conditions
The conditional logic that determines whether a specific asset qualifies for the rule. Conditions can be based on asset attributes such as:
- Provider (e.g., "Provider = ServiceNow")
- Asset type (e.g., "Asset type = Agentic AI")
- State (e.g., "State = Deployed")
- Department
- Custom fields

Conditions can be combined with AND/OR logic to create precise targeting.

### Activate the Rule
The checkbox that makes the rule active. Only active rules are evaluated in scheduled runs.

---

## Relationship to the Automation Rules Overview Page

The Automation Rules page displays all default rules available in AI Control Tower. AI stewards can:
- **Modify existing rules** — adjust conditions or names of existing default or custom rules
- **Create new rules** — per the procedure above
- **Delete rules** — remove rules that are no longer needed

The page shows all rules regardless of active/inactive status, allowing the AI steward to see the full rule set.

---

## Governance Design Considerations

### What Makes a Good Automation Rule

**Good candidates for automation:**
- Assets from known, trusted providers (e.g., ServiceNow-native skills that are already approved through Now Assist deployment processes)
- Assets in specific departments that have a dedicated governance process outside AICT
- Assets that were previously managed and were temporarily moved to Unmanaged for technical reasons
- Assets discovered via Enterprise AI discovery that meet predefined safe-harbor criteria

**Poor candidates for automation:**
- All third-party AI assets regardless of type or risk profile
- Newly created experimental AI systems
- High-risk asset categories (anything with Full Automated Execution, Patient Data, or Automated Decisions in the Use & purpose fields)

### The Governance Gap Automation Creates

When an automation rule promotes an asset to Managed, it initiates the lifecycle review and risk classification processes — but it does not complete them. The asset is Managed with a Lifecycle status of AI steward review until the AI steward actually reviews it. This is correct and expected behavior.

The governance risk is when organizations treat "Managed" as equivalent to "Governed" — it is not. "Managed" means "governance has been triggered." "Governed" means "governance has been completed." Track the backlog of Managed assets that are still in AI steward review status — this is your pending governance queue.

> **Risk Officer Note:** Run a regular report: count of assets with Status = Managed + Lifecycle status = AI steward review + Age > [your SLA, e.g., 5 business days]. This is your automation rule backlog — assets that have been auto-promoted to Managed but have not yet been reviewed by a human steward. A growing backlog indicates that your automation rules are generating more governance work than your team can process. Either add steward capacity, narrow the rule conditions to reduce auto-promotion volume, or increase the max active rules review SLA.

---

## Automation Rules vs. Manual Management

| Aspect | Automation Rule | Manual Management |
|---|---|---|
| **Who initiates** | System (rule match) | AI steward (conscious decision) |
| **Trigger** | Scheduled job every 6 hours | AI steward manually clicks "Move to Managed" |
| **Delay** | Up to 6 hours from qualification | Immediate |
| **Human judgment** | None at promotion moment | Yes — steward evaluates the specific asset before promoting |
| **Auditability** | Rule ID and execution log | AI steward user record and timestamp |
| **Scale** | High — can process hundreds of assets per run | Low — one asset at a time |
| **Risk** | Batch promotion without per-asset review | Individual, intentional governance decision |

---

## Monitoring Automation Rule Execution

To verify that automation rules are working as expected:
1. Check the **AI asset inventory - Managed** section after a scheduled run to see newly promoted assets
2. Check the **Lifecycle > New** subsection — auto-promoted assets appear here waiting for steward review
3. For immediate verification, use the **Run Now** action on an active rule rather than waiting for the scheduled run
4. The audit trail for auto-promotions is available through the standard AICT audit logs

---

## Key Takeaways for AI Risk & Compliance Officers

1. **Automation rules = scalability for governance, not a replacement for it** — rules promote assets to Managed and trigger processes; human review still completes governance.
2. **5 active rules max (default) is intentional** — it forces deliberate rule design; resist the urge to create rules for everything.
3. **"Managed" ≠ "Governed"** — Managed means governance has started; Governed means it has been completed; track the backlog between the two states.
4. **6-hour execution interval creates a governance lag** — assets qualifying for a rule may wait up to 6 hours before being promoted; use Run Now for time-sensitive cases.
5. **Document business justification for every rule** — in the Description field; without it, the rule's intent is not auditable.
6. **High-risk asset categories should NOT be auto-managed** — any asset with patient data, autonomous execution, or external-facing decisions deserves individual steward review, not automated promotion.
7. **Monitor the Lifecycle > New backlog** — this is your automation rule overflow indicator; a growing backlog means rule volume exceeds review capacity.
8. **Rules can be deleted when no longer needed** — don't leave obsolete rules active; they contribute to the max active rules count and may generate unwanted promotions.

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 769–770, 861*
