# Configuring AI Control Tower Workflow
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Role: AI Risk & Compliance Officer Reference

---

## What Is This?

"Configuring AI Control Tower Workflow" is the umbrella section that defines the three-step setup sequence required to make AICT operational for governance. It establishes the order in which configuration must be done, the dependencies between steps, and the key plugin/capability constraints that shape what is possible in any given environment.

---

## The Three-Step Configuration Sequence

The documentation prescribes a strict sequence:

```
Step 1: Activation and Installation of AI Control Tower
    |
    v
Step 2: Configure AI Control Tower
    |
    v
Step 3: Configure Multi-instance Management for AI Control Tower
```

These steps are sequential — you cannot meaningfully configure AICT before it is installed, and multi-instance management must be set up after the base configuration is complete. The next three sections (Topics 12, 13, 14) each cover one of these steps in detail.

---

## Critical Plugin Dependency Notes

Before any configuration begins, the following plugin and capability constraints must be understood:

### AI Risk and Asset Management Capabilities

AI Risk and Asset Management capabilities in AI Control Tower with Now Assist require the **AI Risk and Asset Management for Now Assist plugin** (`sn_aict_irm_aiam`), which depends on:
- AI Risk and Compliance Integration with Control Tower (`sn_grc_ai_irm_intg`)
- AI Asset Management (`sn_ai_asset_mgmt`)

### Scope Difference: AICT Core vs. AICT with Now Assist

| Edition | Scope |
|---|---|
| **AI Control Tower (Core)** | Governance of BOTH enterprise AI assets AND ServiceNow AI assets |
| **AI Control Tower with Now Assist** | Governance of ServiceNow AI assets ONLY |

> **Risk Officer Note:** If your organization has deployed third-party AI assets (AWS Bedrock, Azure Foundry, etc.) and wants to govern them through AICT, you need the full AI Control Tower (Core) edition — not just the Now Assist variant. The Now Assist variant only sees ServiceNow-native assets.

### IRM Standard Plugin for Intake Forms

When AI Control Tower Core (`sn_ai_governance`) is used with AI Risk and Compliance in a **new IRM deployment**, the `sn_irm_std` (IRM Standard) plugin is required to make **AI intake request forms** available.

**What intake forms do:** Enable submission of requests through the Employee Portal for registering AI systems, AI models, and datasets for governance and risk evaluation.

**What this requirement does NOT apply to:**
- AI cases
- Inquiries
- Anonymous Reporting Center

> **Risk Officer Note:** If you are deploying AICT alongside a new IRM (Integrated Risk Management) deployment and want to use the Employee Portal for AI asset intake requests, verify that IRM Standard is installed. Without it, the intake forms will not be available — and without intake forms, the self-service pathway for asset owners to submit AI systems for governance review is broken.

---

## Playbook Configuration

The Playbook templates list (accessible via `Configurations > Playbooks`) contains the approval and lifecycle templates that govern how AICT workflows operate.

### Pre-built Playbook Templates

| Template | Purpose | Status |
|---|---|---|
| **AI Asset Onboarding** | AI asset lifecycle: Onboarding → Assess → Build and test → Deploy | Active |
| **AI Asset Offboarding** | Retirement process when retiring an asset | Active |
| **Now Assist approval** | Workflow for approving/rejecting Now Assist skill deployments | Active |

**Note:** To retire an asset, the offboarding process must be initiated — assets do not retire automatically.

### Customizing Playbook Workflows

> "You can create your own playbook workflow by customizing the number of steps or rearranging them, as well as applying different security policies."

This means the lifecycle stages (Onboarding → Assess → Build and test → Deploy) can be:
- Reordered
- Extended with additional steps
- Modified to apply different security policies per step

> **Risk Officer Note:** Custom playbooks allow organizations to tailor the governance workflow to their risk appetite. For healthcare (CareAtlas), you might add a dedicated "HIPAA compliance validation" step between Build and Test and Deploy, or insert a "Data Privacy review" step in the Assess phase. However, customization must be governed — changes to playbook templates should go through your change management process, as they define the governance controls applied to every asset that flows through AICT.

---

## Automation Rules

Automation rules define how AI assets are automatically classified as managed assets.

### Overview

The Automation Rules page displays all default rules. AI Stewards can:
- Modify existing rules
- Create new rules based on organizational requirements

### Rule Limits (System Properties)

Administrators can configure system-enforced limits on rules:

| System Property | Description | Recommended Default |
|---|---|---|
| `sn_ai_governance.management_rule.max_active_rules` | Maximum number of active rules | 5 |
| `sn_ai_governance.management_rule.max_total_rules` | Maximum total rules allowed | 10 |

### Rules Execution Logic

- Only **active** rules are evaluated during scheduled runs — inactive rules are skipped
- The scheduled job **"Run AI Asset Management Rules"** executes **every 6 hours**
- AI stewards can trigger immediate execution on any active rule using the **"Run Now"** action
- Rules no longer needed can be deleted
- **If an asset qualifies for a rule, it is automatically moved to managed assets**

> **Risk Officer Note:** Automation Rules are a governance accelerator — they can automatically move the right assets into managed governance without requiring manual AI steward action for each one. However, they are also a governance risk if misconfigured: a rule that is too broad may pull hundreds of unvetted assets into "managed" status, falsely suggesting governance coverage. Review all automation rules before activation, and treat the auto-managed asset list as pending governance review, not completed governance.

---

## Key Takeaways for AI Risk & Compliance Officers

1. **Configuration must follow the three-step sequence** — Installation → Configure → Multi-instance. Steps are dependent on each other.
2. **AI Control Tower Core vs. Now Assist variant have different asset scope** — if you need to govern third-party AI assets, you need Core edition.
3. **IRM Standard plugin required for Employee Portal intake forms** — verify this is installed if new IRM deployment is in scope.
4. **Playbook templates can be customized** — healthcare governance may warrant additional steps (HIPAA validation, data privacy review). All customizations should go through change management.
5. **Automation Rules run every 6 hours** — newly created assets are not instantly governed; plan for the 6-hour delay (or use Run Now for immediate execution).
6. **Auto-managed assets via Automation Rules still need governance review** — the rule moves them to managed; the AI steward must still complete the assessment workflow.

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 769–770, 816*
