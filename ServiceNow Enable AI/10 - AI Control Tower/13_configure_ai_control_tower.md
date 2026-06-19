# Configure AI Control Tower
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Role: AI Risk & Compliance Officer Reference

---

## What Is This?

"Configure AI Control Tower" is Step 2 of the three-step setup sequence. Once AICT is installed, it must be configured before it can function as a governance tool. This section covers the configuration procedure and, critically, the configuration options that directly determine how AICT behaves as a governance platform — data sharing, approval controls, playbooks, AI model providers, AI Gateway, and value templates.

---

## Base Configuration Procedure

**Role required:** AI steward (`sn_ai_governance_ai_steward`)

**Navigation:** `Workspaces > AI Control Tower > Configurations`

**Note:** Custom widget support is NOT included in the AI Control Tower overview for AI stewards.

### The Two Mandatory Configuration Steps

**Step 1: Data Sharing**
1. Navigate to Configurations view
2. Expand **Data** and select **Opt in** under Data sharing
   - Requirement: Confirm that the generative AI Controller plugin is installed to view the Data section
   - The Opt in option is enabled by default
   - **Important:** Opting OUT of data sharing can only be enabled by your Account Executive or the Now Support team — it is NOT toggle-able in the UI by the AI steward. The opt-out is inactive by default.

> **Risk Officer Note:** This is a significant governance constraint. While the documentation says you "can opt out," the UI does not allow the AI steward to do this directly — it requires escalation to your Account Executive or Now Support. If your organization has a policy to opt out of vendor data sharing (common in healthcare and financial services), initiate this request with your ServiceNow Account Executive BEFORE go-live, not after. Waiting creates a window where data is being shared without organizational consent.

**Step 2: Enable Automatically Trigger Playbooks**
1. Select **Controls**
2. Locate the **"Automatically trigger playbooks"** option
3. Activate it (it is inactive by default)

**Why this is critical:**
> "Enabling the Automatically trigger playbooks and adding an AI asset to this environment automatically triggers approval requests."

Without this: approval requests are NOT generated automatically. Only the AI steward can initiate them manually. This means assets can enter the AICT inventory without triggering any governance workflow.

**Recommendation from ServiceNow:**
> "Verify to have the Automatically trigger playbooks option enabled in your production environment."

---

## Complete Configurations Page Reference

The Configurations page is the control center for AICT governance settings. It is organized into five sections:

### Section 1: Data

**Data sharing**
- Default: Active (opted in)
- Opt-out requires Account Executive or Now Support engagement
- Sub-prod instances show this in read-only mode when Multi-instance is configured

**Data overflow processing**
- Default: Inactive
- When active: traffic spikes redirect to Microsoft Azure datacenters
- Sub-prod read-only when Multi-instance configured

**Security & privacy**
Four configurable guardrail features:

| Feature | Default | Governs |
|---|---|---|
| Data integrity incident detection | Inactive | LLM output policy violations |
| Agent goal deviation | Inactive | Agent behavior deviation from intended role |
| Output screening | Configurable | PII and security-vulnerable patterns in LLM output |
| Sensitive data input and anonymization | Configured via Data Privacy | PII in LLM prompts |

**Score weight**
- Controls how LLM guardrail categories are weighted in the AI Asset Security Score
- Can change default weights or deactivate categories from scoring

### Section 2: Controls

**Approvals (three sub-controls):**

| Control | Default | Effect When Activated |
|---|---|---|
| AI systems | Inactive | All AI skills and agents require AI steward approval before deployment |
| MCP servers | Inactive | AI stewards can block unapproved MCP servers from being used in AI Agent Studio |
| AI models | Inactive | All AI models require AI steward approval before deployment |

**Automatically trigger playbooks:**
- Default: Inactive
- Recommendation: Activate in production environment
- Effect: Auto-generates approval requests when AI assets are submitted

**AI model providers (sub-section):**
- Configure data routing (Regional / Global)
- Select Allowed model providers
- Manage Fallback and Spillover settings
- Access Impact Summary via Preview impact

**Value templates (sub-section):**
- View and manage default template mappings
- Assign default templates by persona, asset type, skill type, and vendor

### Section 3: Multi-instance Setup

Configures prod-to-sub-prod synchronization. Covered in full in Topic 14.

### Section 4: AI Connections

Manages Service Graph Connector integrations for Enterprise AI Discovery.

The AI connections page displays allowed AI connections in columns:
- Name
- Allowed on AI Gateway
- Last updated by
- Updated

Can be filtered and exported as PDF, JSON, Excel, or CSV.

### Section 5: AI Gateway

Three tabs:

| Tab | Function |
|---|---|
| **Settings** | Pause and resume all AI Gateway transactions (emergency stop) |
| **AI connections** | View list of allowed AI connections on the Gateway |
| **Global MCP clients** | View, add, and manage Global MCP clients (CIMD support — Client ID Metadata Document). Global clients apply across all MCP servers automatically |

**Global MCP clients:** Once created, they apply to ALL MCP servers without needing individual client registrations per server. CIMD = Client ID Metadata Document support.

### Section 6: Playbooks

Displays all playbook templates. Contains three pre-built active templates:

| Template | Purpose |
|---|---|
| AI Asset Onboarding | Full lifecycle: Onboarding → Assess → Build and test → Deploy |
| AI Asset Offboarding | Retirement process |
| Now Assist approval | Approval/rejection workflow for Now Assist skills |

> "You can create your own playbook workflow by customizing the number of steps or rearranging them, as well as applying different security policies."

---

## Audit Logs

The `View audit logs` button (top right of Configurations page) captures all configuration changes across:
- Data settings
- Approval controls
- AI model providers

**Audit log fields:** Timestamp, User, Changed category, Changed setting, After change, Before change

**Filter:** Date range filter; starts with last 90 days.

**Multi-instance audit note:** When a sub-prod instance is added or removed from the sync configuration, audit logs first show all instances being removed, then a record of the instance added/removed.

---

## Recommended Production Configuration State

Based on the documentation's explicit recommendations, a production AICT environment should have:

| Setting | Recommended State | Reason |
|---|---|---|
| Data sharing | Reviewed with legal; opt-out engaged if required | Healthcare data sensitivity |
| Data overflow processing | Decision documented | Cross-border transfer consideration |
| Data integrity incident detection | Active, 100% sampling | Detect LLM policy violations |
| Agent goal deviation | Active, 100% sampling | Detect unauthorized agent behavior |
| Output screening — Output PII Violation | Active | HIPAA: detect PHI in outputs |
| Output screening — Output Security Vulnerability | Active | Detect injection attacks in agent outputs |
| AI systems approval | Active | Block unapproved skills from deploying |
| MCP servers approval | Active | Block unapproved MCP servers from AI Agent Studio |
| AI models approval | Active | Block unapproved models from deploying |
| Automatically trigger playbooks | Active | Auto-generate governance workflows on asset submission |
| Fallback | Decision documented | Governance posture choice |
| Now LLM-LTS | Consider for regulated use cases | Stronger lifecycle and compliance guarantees |

> **Risk Officer Note:** This recommended configuration table represents the governance baseline. During your go-live planning, audit each of these settings against your organization's risk tolerance and regulatory obligations. Settings left at default (inactive) are governance gaps — document them as accepted risks with compensating controls if you choose to leave them inactive.

---

## Key Takeaways for AI Risk & Compliance Officers

1. **Data sharing opt-out requires Account Executive or Now Support** — not UI-toggleable; initiate before go-live if opt-out is required.
2. **"Automatically trigger playbooks" must be ON for governance automation** — without it, the AI steward must manually initiate every governance workflow.
3. **All three approval controls are inactive by default** — this is the most significant default governance gap; activate all three for production.
4. **The Configurations page is the single control plane** for all governance settings — familiarize yourself with all six sections.
5. **Audit logs capture all configuration changes** — treat them as your governance change management trail; export beyond 90 days.
6. **Global MCP clients apply to all servers** — powerful but requires careful access control; global access = global risk.
7. **Playbooks can be customized** — for healthcare, consider adding HIPAA validation and data privacy review steps; all changes require change management.

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 767–770, 820*
