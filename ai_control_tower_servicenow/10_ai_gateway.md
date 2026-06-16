# AI Gateway
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Role: AI Risk & Compliance Officer Reference

---

## What Is This?

AI Gateway is AICT's governance, observability, and security layer specifically for **MCP (Model Context Protocol) transactions**. It acts as a controlled proxy between AI agents and external MCP servers, ensuring that all cross-platform AI tool usage is authenticated, governed, audited, and observable.

In plain terms: when a ServiceNow AI agent (or any external AI agent) wants to use a tool that lives on an external MCP server, that request goes through the AI Gateway. The Gateway enforces access controls, logs the transaction, and makes it visible to the AI steward.

---

## Model Context Protocol (MCP) — Foundation

> *"The Model Context Protocol (MCP) is a standardized client-server protocol that enables AI applications to discover and interact seamlessly with external tools, data sources, and systems."*

**MCP Architecture:**
```
AI Host Application (AI Agent Studio)
    |
    v contains
MCP Client (embedded in host)
    |
    v connects to via AI Gateway
MCP Server(s) (expose specific capabilities as tools)
```

MCP facilitates communication between:
- **AI host application** — the agent builder environment (AI Agent Studio in ServiceNow)
- **MCP Client** — embedded in the host; makes requests to MCP servers
- **MCP Server** — exposes specific capabilities (tools, data sources, APIs)

---

## AI Gateway Overview

> *"AI Gateway enables governance, observability, and security for your MCP transactions. AI Gateway is designed to be platform agnostic, delivering the above-mentioned benefits both within ServiceNow (AI Agent Studio) and in external agentic studios and hosts."*

**Platform agnostic** means AI Gateway works not just for ServiceNow agents, but for any MCP-compatible AI agent from any platform — including Microsoft Copilot Studio, Postman, and other tool builder platforms.

### What AI Gateway Offers

| Capability | Description |
|---|---|
| **Lifecycle management** | MCP servers go through the full AICT lifecycle (Assess → Build & Test → Deploy) |
| **Asset registry** | Every MCP server is an AI asset in the AICT inventory |
| **Identity and access management** | Controls which agents/clients can connect to which MCP servers |
| **Secure authentication** | OAuth 2.1 with Dynamic Client Registration |
| **Observability** | Transaction metrics (total requests, success rate, latency) per server and tool |

### Business Value

> *"With the increasing need of interoperability across different AI solutions across enterprises, AI Gateway provides a way for interoperability governance, observability & security."*

- Enables tight governance and control of cross-platform MCP server resources
- Securely connects agents to remote MCP servers — works for any agent/server combination
- Provides visibility into production metrics: usage and latency

---

## Installation and Prerequisites

### Applications Required

| Application | Note |
|---|---|
| **Now Assist subscription** | Required |
| **AI Control Tower for Now Assist – Pro Plus license** | Auto-installs `sn_awh_config` |
| **AI Agent Studio** | Required for MCP server intake in AI Gateway for AI Control Tower (1.0.5) |

### Plugins Required

| Plugin | Minimum Version |
|---|---|
| `sn_ai_governance` | 5.0.6 or higher |
| `sn_telemetry_data` | 1.1.10 or higher |

### Roles Required

| Role | Purpose |
|---|---|
| `sn_ai_governance.ai_steward` | Approval workflows and policy management |
| `sn_aia.admin` (AI Agent admin) | Configuring MCP servers as tools in AI Agent Studio |

**Auto-install:** AI Gateway is automatically installed for customers using AI Control Tower for Now Assist. If you use any generative AI features, you already have AI Gateway access (included with all Pro Plus licenses). Requires both AI Agent Studio AND AI Control Tower to be available.

**AI Steward role inheritance:** The `sn_ai_governance.ai_steward` role automatically inherits:
- `sn_aia.admin` (AI admin)
- `aig_admin` (AIG admin)
- `sn_mcp_client.admin` (MCP Client admin)

---

## Complete Process Flow for MCP Servers Via AI Gateway

The process has three phases that must be completed in order:

```
Phase 1: Add MCP Server
    |
    v
Phase 2: MCP Server Approval Workflow (Assess → Build & Test → Deploy)
    |
    v
Phase 3: AI Gateway Setup and Client Registration
```

**Role required throughout:** `sn_ai_governance.ai_steward`

---

## Phase 1: Adding an MCP Server (Three Methods)

### Method A: From ServiceNow AI Agent Studio

**Navigate to:** `Workspaces > AI Agent Studio > Settings > Manage MCP servers > New`

**Steps:**
1. Enter the server Name
2. Select Authentication type: **OAuth 2.1** (AI Gateway supports OAuth 2.1 only)
3. Select Next
4. Select Client registration type: **Dynamic Client Registration** (AI Gateway registration in Agent Studio supports this)
   - If server allows dynamic client registration: details auto-retrieved
   - If not: enter details manually
5. Select the Grant type
6. Select Add — server is added and details displayed
7. Select Authenticate to authenticate with your credentials
8. Select Save to create the MCP server record

**Important notes:**
- In the Create and manage tab of AI Agent Studio, you can only add MCP servers that have been approved in AICT
- A scheduled job named **"AI Agent Studio to AICT-MCP server sync"** runs **every 15 minutes** to synchronize MCP servers from AI Agent Studio to AI Control Tower
- After synchronizing, the MCP server appears in AI asset inventory with Status = In review, Lifecycle phase = New
- Once an MCP server is added to AICT, it cannot be added again; AI Agent Studio will not discover a server already added

**Note regarding unapproved servers (AWH for AI Control Tower 2.0.0):** Unapproved MCP servers appear in the Agent Studio list but tools cannot be fetched until the server is approved in AI Control Tower.

### Method B: From the MCP Catalog

**Navigate to:** `AI assets > AI asset inventory > MCP servers > Add > Choose from MCP Catalog`

**Steps:**
1. Search for a server or browse available MCP servers (displayed as cards with icons, descriptions, versions)
2. Verify the server details: MCP server URL, Transport type, Available tools and capabilities
3. Select the server → Import it by selecting Select
4. System auto-fills: Name, MCP server URL, Authentication type, Transport type
5. Confirm server and endpoint selections → OK
6. Add any additional details
7. Select Submit — server submitted to AI steward for review

**Notes:**
- Only one MCP server can be added at a time from the catalog
- Status becomes In review; synced to AI Agent Studio within 15 minutes

### Method C: Directly from AI Control Tower

**Navigate to:** `AI assets > AI asset inventory > MCP servers > Add`

**Steps:**
1. Enter the Name (Server name)
2. Enter the MCP server URL
3. Select Next
4. Select Client registration type:
   - **Dynamic Client Registration**: AICT automatically receives Client ID and Client Secret
   - **Manual registration**: Client must be created externally on the MCP provider side; enter Client ID and Secret manually
5. Review Grant type, Token authentication method
6. Review three URL sections:
   - **Authorization URL** — where the user authenticates and grants the access token
   - **Token URL** — where the system exchanges an authorization code for an access token
   - **Token revocation URL** — used to invalidate issued tokens (if supported)
7. Select Submit

**Result:** Newly added MCP server registered in AI asset inventory MCP servers list and available for approval workflow.

---

## Phase 2: MCP Server Approval Workflow

**Navigate to:** `AI Control Tower > AI assets > Approvals`

**Steps:**
1. Select the MCP server from the asset type filter OR navigate to Lifecycle and filter by current state = New
2. Select the MCP Server record with status = New
3. Select **Start Review**

**During review:** Within AI Agent Studio, the MCP Server shows status = "AI Steward review." Product Owners can select "View approval record" in Agent Studio to go directly to the MCP Server record in AICT.

4. A playbook is triggered with three phases:

**Assess phase:**
- Includes: Architecture review, Risk Assessment, Stakeholder review
- Select **Mark as Complete** for the Assess phase when done

**Build and Test phase:**
- Out-of-application testing and validation activities
- Example: Run a test AI agent using the MCP Server as a tool, validate the output
- Select **Mark as Complete** for Build and Test phase

**Deploy phase:**
- Final step to deploy and enable the MCP Server for usage
- Select **Mark as Complete** for Deploy phase

5. Select Save

**Critical note:** The AI Gateway setup tab appears **ONLY** after an MCP server request is approved. Before approval, this tab is not visible.

### Workaround for AI Control Tower Pro License (Known Behavior)

With the AI Control Tower Pro license (not Pro Plus), after synchronization the Start Review button may not appear. The Lifecycle status shows as "None."

**Workaround — run this script manually:**
```javascript
var assetGovernanceRecord = new GlideRecord('sn_ai_governance_asset_governance_details');

if (assetGovernanceRecord.get('<sys_id of asset governance record>')) {
    assetGovernanceRecord.setValue('status', 5);
    assetGovernanceRecord.setDisplayValue('lifecycle_phase', 'New');
    assetGovernanceRecord.update();
}
```
This sets the lifecycle phase to New and triggers the approval process.

> **Risk Officer Note:** The three-phase approval (Assess → Build & Test → Deploy) for MCP servers is a full governance lifecycle. The Assess phase must include a **Risk Assessment** — this is the point at which the MCP server's capabilities, data access, and security posture should be evaluated before any agent is permitted to use it. This assessment should be documented in the AI steward's close notes and, ideally, linked to a formal assessment record.

---

## Phase 3: AI Gateway Setup and Client Registration

**Navigate to:** `AI assets > AI asset inventory > MCP servers > [Approved MCP server] > AI Gateway setup tab`

**Purpose:** Create MCP Client integrations that allow specific agent builders to connect to this approved MCP server through the AI Gateway.

**Steps:**
1. Under MCP Client integration, select **New**
2. Enter the Name
3. Redirect URL (available after agent is created and configured) is a callback/OAuth endpoint
4. Select Save

**Redirect URLs by platform:**

| Platform | Redirect URL |
|---|---|
| AI Agent Studio | `https://<instance_name>.service-now.com/oauth_redirect.do` |
| Copilot Studio | Unique to the tool/connection created inside the Copilot agent |
| Postman | `https://oauth.pstmn.io/v1/browser-callback` |
| Other platforms | Consult platform's OAuth documentation |

**Result:** Client ID and Client Secret are automatically generated and available in the MCP server record. These credentials authenticate the client when connecting to the AI Gateway.

### Global MCP Clients

Global MCP clients are set up at the configuration level rather than per-server, and are automatically available across ALL approved MCP servers.

**Navigate to:** `AI Control Tower > Configurations > AI Gateway > Global MCP clients > Add`

**Steps:**
1. Enter the Client ID
2. Select Next
3. Select Metadata sync mode (**Live mode preferred**)
4. Adjust Security controls per agent builder requirements
5. Select Submit

**Advantage:** Create once, applies to all MCP servers — no need to create individual client integrations per server.

---

## MCP Server Record — Tabs and Contents

Each MCP server record has five tabs:

### Tab 1: Details
- All asset details including MCP server URL (at bottom of page)

### Tab 2: Approvals
- All approval requests for the MCP server
- Shows the history of approval workflow activities

### Tab 3: KPIs & Metrics
- MCP tools observability metrics for each approved, running server
- Shows: different tools invoked across gateway usage from different hosts, total number of requests sent, success rate, latency observed
- Note: The AI Gateway tab on AICT's landing page also shows server-level total requests/transactions and success rate

### Tab 4: AI Gateway Setup *(appears ONLY after approval)*
- **AI Gateway MCP server details** (all auto-generated, cannot be modified):
  - AI Gateway MCP server URL — the Gateway endpoint that clients connect to
  - Authorization endpoint URL — OAuth authorization endpoint
  - Token endpoint URL — OAuth token exchange endpoint
- **Pause AI Gateway transactions:** If an MCP server is identified as malicious, the AI steward can pause all transactions directed to that server through AI Gateway. Once risk is resolved, transactions can be resumed.
- **MCP Client Integration section:** Registered clients for the server. Each agent builder platform needs its own client registration (generates unique Client ID + Client Secret).
- **Global MCP Clients section:** Displays global clients automatically available across all MCP servers (configured at Configurations level, not per-server)
- Tab accessible to all AI Control Tower workspace users

### Tab 5: Related Variants
- Provides one-to-one mapping of all MCP server entries from AI Agent Studio
- Each entry is visible and trackable in AICT
- Multiple MCP servers of the same variant can exist
- **PII check activation:** AI steward can activate sensitive data protection for any transaction across servers by selecting **"Activate PII check"**. When activated, AI Gateway blocks transactions that involve sharing sensitive information to the MCP server.

---

## Connecting External Platforms Via AI Gateway

### Microsoft Copilot Studio Connection

**Role required:** Workspace user

**Steps (in Copilot Studio):**
1. Log in to `https://copilotstudio.microsoft.com`
2. Create a new agent (Agents > +New agent > Configure tab > enter Name and Description > Create)
3. Open the agent > Tools tab > +Add a tool > Model Context Protocol icon > +New tool > Model Context Protocol
4. In the "Add a Model Context Protocol server" window:
   - Server name, Server description, Server URL (from AI Gateway setup tab)
   - Authentication: OAuth 2.0
   - Type: Manual
   - Client ID and Client Secret (from MCP server record created for Microsoft Copilot Studio)
   - Authorization URL and Token URL (from AI Gateway setup tab)
   - Refresh URL = same as Token URL
   - Click Create → generates Redirect URL
5. Copy Redirect URL → paste into Redirect URL field in MCP server record
6. Click Save on MCP server record
7. Navigate to `ALL > Application registry` → find the Copilot MCP server record
8. **Change "Always use PKCE" and "Public Client" from True to False** (this step only applies to Microsoft Copilot Studio)
9. Save the Copilot MCP server record
10. Navigate back to Copilot Studio > Next > Create new connection > Approve
11. After connecting: Add to agent > Open connection manager > provide authentication > Connect > Submit

### ServiceNow AI Agent Studio Connection

**Role required:** `sn_aia.admin`

**Note:** Product Owners can be restricted to use only approved MCP Servers in AI Agent Studio.

**Steps:**
1. Navigate to `All > AI Agent Studio`
2. Open existing agent or create new agent
3. Select Edit > Tools > +Add a tool > +New tool > Model Context Protocol
4. Select the MCP server from the drop-down (only approved servers available in AWH 2.0.0+)
5. Select the specific tools from the MCP server that the agent should use
6. Select Save

**Result:** The agent is configured to use the MCP Server through AI Gateway. All requests from the agent to the MCP Server are routed through AI Gateway for governance, security, and observability.

---

## Security Controls Within AI Gateway

### Pausing Transactions (Server-Level)

> *"If an MCP server is identified as malicious for a certain period, the AI stewards can pause all transactions directed to that server through the AI Gateway. Once the risk is resolved, transactions can be resumed."*

**How to pause:** AI Gateway setup tab on the MCP server record → Pause transactions button

**How to resume:** Same location, when risk is resolved

### Pausing Transactions (Gateway-Level)

All transactions across ALL servers can be paused from the AI Gateway page in the Configurations section:
`AI Control Tower > Configurations > AI Gateway > Pause AI Gateway transactions`

This is the "emergency stop" for the entire AI Gateway.

### PII Protection Per Server

Via the Related Variants tab → Activate PII check:
- Blocks transactions that involve sharing sensitive information to the MCP server
- Applied at the server level, not globally

> **Risk Officer Note:** The ability to pause individual MCP servers or the entire gateway is a critical incident response control. This should be part of your AI security incident playbook: if an MCP server is compromised or behaving maliciously, the AI steward can immediately pause it without taking down the entire instance. Document this capability in your AI security incident response plan and ensure the AI steward knows how to execute it.

---

## AI Gateway Observability Metrics

The AI Gateway tab on AICT's home page shows:
- List of all connected MCP servers
- Total transactions per server
- Success rate per server

The KPIs & Metrics tab on each MCP server record shows:
- Tools invoked across gateway usage from different hosts
- Total number of requests sent
- Success rate
- Latency observed

The Security & privacy tab on the AICT home page shows:
- Authorized access attempts to MCP servers (successful)
- Failed access attempts to MCP servers (unsuccessful)
- Both from MCP clients (ServiceNow AI agents + registered third-party MCP clients) through this instance's AI Gateway

> **Risk Officer Note:** The failed access attempts metric is a security signal. Repeated failed access attempts to specific MCP servers may indicate: unauthorized clients attempting access, misconfigured client credentials, or a potential brute-force attack on the OAuth tokens. Monitor this metric and establish alerting thresholds.

---

## Key Governance Touchpoints for Risk Officers

The AI Gateway represents a **governance boundary** for agentic AI. Key touchpoints:

| Governance Moment | What Happens | Risk Officer Action |
|---|---|---|
| **MCP server first added** | Status = In review; lifecycle phase = New | Ensure steward review is initiated promptly |
| **Assess phase of approval** | Architecture review, Risk Assessment, Stakeholder review | Risk Assessment must be documented; link to formal AIRC assessment |
| **Build & Test phase** | Out-of-application testing and validation | Verify test plan covers all tool capabilities and data access |
| **Deploy phase** | MCP server enabled for production use | Final risk acceptance by AI steward |
| **Client registration** | Agent builder platform gets Client ID/Secret | Each client represents a distinct access grant — govern like IAM |
| **PII check activated** | Transactions with PII blocked to this server | Ensure healthcare-relevant PII patterns are configured |
| **Transaction pause (server)** | All traffic to malicious server halted | Incident response — document root cause and remediation |
| **Transaction pause (gateway)** | All MCP traffic halted instance-wide | Emergency stop — highest severity AI security incident response |

---

## Key Takeaways for AI Risk & Compliance Officers

1. **AI Gateway is the access control layer for MCP tools** — every agent-to-external-tool interaction goes through it; without it, tool access is ungoverned.
2. **The three-phase approval (Assess → Build & Test → Deploy) applies to MCP servers** — treat each MCP server as a governed AI asset with the same rigor as any AI system.
3. **The Risk Assessment in the Assess phase is mandatory** — document the MCP server's tool capabilities, data access, and security posture before approval.
4. **Each agent builder gets its own Client ID/Secret** — govern these like IAM credentials; rotate them, track them, revoke them when no longer needed.
5. **Global MCP clients apply to all servers automatically** — use them for trusted internal clients; use per-server clients for more granular control.
6. **PII check at the server level protects sensitive data** — activate it for any MCP server that may receive prompts containing patient data.
7. **The pause capability is an incident response tool** — document it in your AI security incident playbook.
8. **Failed access attempts are a security signal** — establish monitoring and alerting thresholds for the failed access attempts metric.
9. **The 15-minute sync job between AI Agent Studio and AICT** means there is a delay between server creation and governance visibility — plan for this in time-sensitive governance activities.

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 805–816*
