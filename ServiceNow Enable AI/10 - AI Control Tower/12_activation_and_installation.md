# Activation and Installation of AI Control Tower
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Role: AI Risk & Compliance Officer Reference

---

## What Is This?

This section covers the complete installation architecture of AI Control Tower — the ordered list of applications and plugins that must be installed, their inter-dependencies, and the constraints that govern what capabilities are available in what editions. Understanding the installation stack is critical for Risk & Compliance Officers because the capabilities available to you depend entirely on which plugins are active.

---

## Installation Principle

The dependent plug-ins **install automatically** when the generative AI Controller is installed — they are NOT installed individually. This means:

- For **Pro Plus licensed customers**: AI Control Tower for Now Assist 1.01 is auto-installed with generative AI Controller (`sn_generative.ai 11.0.9`). Installation of the Now Assist plugin auto-installs relevant AI Control Tower plugins. No additional plugins needed.
- For all other deployments: follow the ordered installation sequence below, then download the AI Control Tower application from the ServiceNow Store once dependent plugins are active.

---

## The Installation Order

AICT installs seven components in a specific dependency sequence:

### 1. AI Control Tower Core (`sn_ai_governance`)

> "Combines AI assets and controls in a central hub, ensuring comprehensive governance and management."

**What it provides:**
- The foundational AI asset inventory
- Core governance controls
- The central hub that all other AICT components build on

**Dependent plugin:**
- Data Foundation Model (`sn_cmdb_foundation:1.1.0`)

---

### 2. AI Asset Management (`sn_ai_asset_mgmt:2.0.0`)

> "The ability to collect information, track changes and manage the lifecycle of AI artifacts like AI systems, models, datasets, and prompts."

**What it provides:**
- Lifecycle management for all four AI asset types
- Asset record creation, update, and retirement workflows
- Change tracking for AI artifacts

---

### 3. AI Risk and Compliance Management (`sn_grc_ai_gov:21.0.1`)

> "A comprehensive framework that facilitates end-to-end lifecycle management of AI risks. It supports activities such as risk classification of AI assets, mapping to regulatory authority documents, continuous monitoring, and policy conformance to promote responsible and accountable AI usage."

**What it provides:**
- Risk classification for AI assets
- Mapping to regulatory authority documents (EU AI Act, GDPR, NIST, etc.)
- Continuous monitoring frameworks
- Policy conformance management

**Dependent plugins (all required):**
- AI Control Tower Core (`sn_ai_governance:4.0.2`)
- GRC feature roles (`sn_grc_ftr_role:21.0.1`)
- GRC: Common workspace elements (`sn_grc_workspace:21.0.4`)
- GRC: Policy and Conformance management (`sn_compliance:21.0.2`)
- Post assessment actions for Smart assessments (`sn_smart_imp_auto:20.1.0`)
- GRC: Risk management (`sn_risk:21.0.2`)
- Regulatory agency library (`sn_reg_body_mgmt:21.0.0`)
- Smart assessment core (`sn_smart_asmt:21.0.1`)
- Smart assessment connected (`sn_smart_asmt_conn:21.0.1`)
- Smart assessment designer (`sn_smart_asmt_desg:21.0.3`)

> **Risk Officer Note:** The AI Risk and Compliance Management component is the most dependency-heavy in the stack. It requires nine separate GRC plugins, all of which must be at their minimum versions. In a fresh deployment, these typically install together. In an environment where GRC is already deployed, version conflicts are the most common installation issue. Run a plugin version audit before installation.

---

### 4. AI Case Management (`sn_ai_case_mgmt:21.0.1`)

> "Enables tracking, triaging, and resolution of incidents or inquiries related to AI systems. It provides a structured case handling mechanism for AI stewards, conformance officers, and stakeholders to manage AI-related exceptions, investigations, and operational events efficiently."

**What it provides:**
- Formal case records for AI violations, compliance concerns, and incidents
- Inquiry management workflow
- Assignment, prioritization, and escalation of AI-related cases

---

### 5. AI Risk and Compliance Integration with Control Tower (`sn_grc_ai_irm_intg:21.0.1`)

> "Establishes a seamless connection between AI Risk and Compliance and the AI Control Tower workspace. This integration ensures unified visibility into AI governance activities, enabling users to monitor risk postures, conformance statuses, and case workflows directly within the Control Tower interface for a centralized oversight experience."

**What it provides:**
- The integration bridge between AICT (governance hub) and AIRC (GRC module)
- Makes risk posture, compliance status, and case data visible in the AICT dashboard
- The Risk & Compliance tab in AICT depends on this integration

**Dependent plugins:**
- AI Case Management (`sn_ai_case_mgmt:21.0.1`)
- AI Risk and Compliance management (`sn_grc_ai_gov:21.0.1`)
- GRC: Advanced Risk (`sn_risk_advanced:21.0.2`)

> **Risk Officer Note:** Without this integration plugin, the Risk & Compliance tab in AICT will not display data. This is the "glue" that makes AICT a unified governance view rather than just an asset inventory. If your Risk & Compliance tab is empty even after configuring AIRC, verify this integration plugin is installed and active.

---

### 6. AI Risk and Compliance Content (Optional)

> "Provides customers to promote conformance with the applicable laws, regulations, directives and/or standards and that any content provided in the product is accurate and up to date."

**What it provides:**
- Pre-built authority documents (EU AI Act, GDPR, NIST AI RMF, etc.)
- Pre-built risk statements mapped to regulatory frameworks
- Pre-built controls aligned to authority document requirements
- Assessment templates for regulatory compliance evaluation

**Critical legal disclaimer from the documentation:**
> "When the customer acknowledges that the content provided with the product is easy to use, then it's that customer's responsibility to replace the content with the applicable laws, regulations, directives and, or standards at its own discretion."

**What this means:** The content pack is a starting point, not a compliance guarantee. ServiceNow provides it to help you get started, but you are responsible for ensuring it reflects the actual current text of applicable regulations. Regulations change; the content pack may not update in sync.

> **Risk Officer Note:** Install the content pack — it saves enormous time in initial setup. But treat all pre-built authority documents and controls as **templates requiring validation**, not as authoritative compliance content. Before relying on any pre-built control mapping for actual regulatory compliance evidence, have your legal/compliance team verify it against the current version of the regulation. The EU AI Act, for example, has ongoing implementing acts and technical standards that may not yet be reflected in the content pack.

---

### 7. AI Control Tower (`sn_aict`) — The Final Application

> "Provides a single, consolidated view of all enterprise AI assets and their relationships, empowering organizations with enhanced integration, governance, and operational efficiency."

**What it provides:**
- The unified AICT workspace and dashboard
- Integration of all the above components into one interface

**Dependent plugins:**
- AI Asset Management (`sn_ai_asset_mgmt:2.0.0`)
- AI Control Tower Core (`sn_ai_governance:4.0.2`)
- AI Risk and Compliance integration with Control Tower (`sn_grc_ai_irm_intg:21.0.1`)
- Engagement dashboard for AI Control Tower (`sn_ai_engagement:2.1.6`)
- Value dashboard for AI Control Tower (`sn_ai_value:2.1.6`)
- Health for AI Control Tower (`sn_ai_health:2.5.14`)
- AI Discovery (`sn_ai_disc:1.0.4`)

**Health plugin note:** The Health tab (`sn_ai_health:2.5.14`) in AICT is available from the Zurich (September) release onwards. It installs **after** the Value dashboard for AI Control Tower is installed.

---

## Complete Plugin Dependency Map

```
sn_cmdb_foundation:1.1.0
    └── sn_ai_governance:4.0.2 (AI Control Tower Core)
            └── sn_ai_asset_mgmt:2.0.0 (AI Asset Management)
            └── sn_grc_ftr_role:21.0.1
            └── sn_grc_workspace:21.0.4
            └── sn_compliance:21.0.2
            └── sn_smart_imp_auto:20.1.0
            └── sn_risk:21.0.2
            └── sn_reg_body_mgmt:21.0.0
            └── sn_smart_asmt:21.0.1
            └── sn_smart_asmt_conn:21.0.1
            └── sn_smart_asmt_desg:21.0.3
                    └── sn_grc_ai_gov:21.0.1 (AI Risk & Compliance Mgmt)
                    └── sn_ai_case_mgmt:21.0.1 (AI Case Management)
                    └── sn_risk_advanced:21.0.2
                            └── sn_grc_ai_irm_intg:21.0.1 (Integration)
                                    └── sn_aict (AI Control Tower — final)
                                        ├── sn_ai_engagement:2.1.6
                                        ├── sn_ai_value:2.1.6
                                        ├── sn_ai_health:2.5.14
                                        └── sn_ai_disc:1.0.4
```

---

## Additional Capability-Specific Plugins

### For AI Risk and Asset Management with Now Assist

Required: `sn_aict_irm_aiam` (AI Risk and Asset Management for Now Assist), which depends on:
- `sn_grc_ai_irm_intg` (AI Risk and Compliance Integration with Control Tower)
- `sn_ai_asset_mgmt` (AI Asset Management)

### For AI Strategy Tab (SPM Integration)

**The AI Strategy tab in AI Control Tower is available ONLY with the SPM Professional license.** This is an additional licensed feature, not a plugin that can be installed independently.

### For Employee Portal Intake Forms (New IRM Deployment)

When AI Control Tower Core is used with AI Risk and Compliance in a new IRM deployment:
- Required: `sn_irm_std` (IRM Standard)
- Purpose: Makes AI intake request forms available in the Employee Portal
- Scope: Only required for intake forms — not for AI cases, inquiries, or Anonymous Reporting Center

---

## AI Gateway Installation

AI Gateway is automatically installed for customers who use AI Control Tower for Now Assist.

Required plugins for AI Gateway:
- `sn_ai_governance:5.0.6` or higher
- `sn_telemetry_data:1.1.10` or higher

The AI Gateway is included with all types of Pro Plus licenses. If you use any generative AI features, you already have AI Gateway access.

---

## Post-Installation Verification Checklist

After installation, verify the following before proceeding to configuration:

**Core functionality:**
- [ ] AI Control Tower workspace is accessible at `Workspaces > AI Control Tower`
- [ ] Left navigation shows: Home, AI assets, Configurations
- [ ] All eight dashboard tabs are visible (Overview, AI Strategy [if SPM], AI Asset Inventory, Value, Health, Risk & Compliance, AI Cases, Security & Privacy, AI Gateway)

**Plugin verification:**
- [ ] `sn_ai_governance` active (Core)
- [ ] `sn_ai_asset_mgmt` active (Asset Management)
- [ ] `sn_grc_ai_gov` active (Risk & Compliance Management)
- [ ] `sn_ai_case_mgmt` active (Case Management)
- [ ] `sn_grc_ai_irm_intg` active (Integration)
- [ ] `sn_ai_disc` active (AI Discovery)
- [ ] `sn_ai_health` active (Health tab)

**Risk & Compliance integration:**
- [ ] Risk & Compliance tab on AICT dashboard shows data (not "No data available" with configuration error)
- [ ] AI Risk and Compliance module accessible from All menu

**Content pack (if installed):**
- [ ] Authority documents visible in Risk & Compliance configuration
- [ ] Pre-built assessment templates available
- [ ] Pre-built controls and risks available

> **Risk Officer Note:** The Risk & Compliance tab showing "No data available" after installation is expected — it requires assessments to be run first. However, if the tab itself is missing or shows a configuration error (not just no data), check whether `sn_grc_ai_irm_intg` is active. This plugin is the most common missing piece when the Risk & Compliance integration is not working.

---

## Key Takeaways for AI Risk & Compliance Officers

1. **Seven components install in sequence** — each depends on the ones before it; do not attempt out-of-order installation.
2. **Pro Plus customers get auto-installation** — no manual plugin work needed if you are a Pro Plus Now Assist customer.
3. **AI Risk and Compliance Management has nine GRC plugin dependencies** — verify all are at minimum required versions before installation, especially in existing GRC environments.
4. **The integration plugin (`sn_grc_ai_irm_intg`) is the bridge** — without it, the Risk & Compliance tab in AICT will not work regardless of what else is installed.
5. **The content pack is optional but strongly recommended** — it provides pre-built authority documents, risks, controls, and templates that save weeks of setup; treat it as a validated starting point, not a compliance guarantee.
6. **AI Strategy tab requires SPM Professional license** — plan this into licensing if strategic AI portfolio tracking is needed.
7. **IRM Standard plugin required for intake forms in new IRM deployments** — without it, the Employee Portal pathway for asset registration is unavailable.
8. **Health tab requires Zurich release and installs after Value dashboard** — check if your instance is post-Zurich if Health tab is missing.

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 817–819*
