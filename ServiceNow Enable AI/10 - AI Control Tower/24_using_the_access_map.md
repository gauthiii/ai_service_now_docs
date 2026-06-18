# Using the Access Map
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Role: AI Risk & Compliance Officer Reference

---

## What Is This?

The Access map is a **node-graph visualization** of the relationships between your ServiceNow AI agents, agentic workflows, and tools — with a specific focus on surfacing access issues. It is the security topology map for your AI agent ecosystem, equivalent to a network diagram but for AI agent access rather than network traffic.

The Access map answers: "Which agent has access to what? Who built it? What tables did it touch last month? Are there any access violations?"

---

## Where to Find It

Two navigation paths:

1. **From the Security & privacy dashboard:** Select the **access map** link in the header of the Security and privacy tab
2. **Direct navigation:** `All > AI Security and Privacy > Access Map`

**Role required:** AI steward (`sn_ai_governance_ai_steward`)

---

## What the Map Shows

The access map is a **node-graph** — each node represents an AI agent, agentic workflow, or tool. Connections between nodes represent relationships (which workflow invokes which agent; which agent uses which tool).

**Nodes that have access issues are highlighted with a warning icon.** This is the primary visual governance signal — a warned node requires investigation.

---

## Navigating the Map

**Step 1:** Open the Access map (via Security & privacy tab or direct navigation)

**Step 2:** Select an AI agent or agentic workflow using:
- Clicking directly on the map
- Using the **Search by agent or workflow** field
- Using **AI agents** and **Agentic workflows** filters to refine the view

Agents with access issues display with a warning icon on the map.

**Step 3:** Select a node in the node map to view its connections

**Step 4:** Select a node to get further details and configure settings

---

## Node Detail Reference

When you select a node, a detail panel opens. The content varies by node type:

### Agentic Workflow Node

| Detail | Description |
|---|---|
| **Description** | A brief description of the workflow |
| **Domain** | The domain scope of the workflow |
| **Execution mode** | How the workflow is executed: Autonomous or Manual |
| **Created by** | The creator of the workflow |

### Agent Node

| Detail | Description | Notes |
|---|---|---|
| **Description** | A brief description of the agent | — |
| **Domain** | The domain scope of the agent | — |
| **Created by** | The creator of the agent | — |
| **Tables accessed** | Review the table accesses of the agent over the last month | Select **Operation** to filter specific access operations |
| **Access issues** | Details the resources and operations causing the access issues | Only displays for agents WITH access issues |
| **Resource** | The resource the agent is having issues accessing | Part of Access issues panel |
| **Operation** | The operation the agent attempted (e.g., read, write, delete) | Part of Access issues panel |
| **Count** | The number of times the agent encountered the issue | Part of Access issues panel |

> **Risk Officer Note:** The "Tables accessed" detail is the most important governance information on the Agent node. It shows what the agent actually accessed over the last month — not what it was configured to access, but what it actually did. Compare this against the agent's intended scope: if a patient appointment scheduling agent accessed the `sys_user_password` table, that is an unauthorized access event. Tables accessed is your observed access audit trail; intended scope is your designed access model. Any gap is a security finding.

### Tool Node

| Detail | Description |
|---|---|
| **Description** | The description of the tool |
| **Domain** | The domain scope of the tool |
| **Execution mode** | The execution mode of the tool: Supervised or Autonomous |
| **Type** | The type of tool |
| **Target record** | The record the tool modifies |
| **Created by** | The creator of the tool |

**Additional action:** Select **Open tool record** to view full tool details beyond what appears in the detail panel.

> **Risk Officer Note:** The Tool node's **Execution mode** (Supervised or Autonomous) is a critical governance detail. A Supervised tool requires human approval before executing. An Autonomous tool executes without human review. For healthcare AI agents in CareAtlas, tools that modify patient records, send notifications to clinical staff, or trigger appointments should be Supervised — not Autonomous. Any tool in Autonomous mode that can write to clinical systems is a compliance risk that should be flagged and reviewed.

---

## Access Issues: What They Mean

Access issues appear when an agent has attempted to access a resource it is not authorized for. The Access map surfaces these visually through the warning icon.

**Why access issues occur:**
- Agent has been granted permissions beyond its intended scope (Privileged AI Agent — security score penalty)
- Agent's scope was not properly configured at design time
- Agent is attempting to access resources in workflows outside its intended purpose (Agent goal deviation)
- A tool used by the agent has broader permissions than the agent should have

**What to do with access issues:**
1. Select the warned agent node on the map
2. Review the **Access issues** panel: Resource, Operation, Count
3. Determine if the access was: (a) within scope but flagged as anomalous, (b) outside scope — an access control failure, or (c) an attempted unauthorized access (potential adversarial activity)
4. Create an **AI task** from the Security & privacy dashboard to track remediation (requires `sn_vsc.task_manager` role)
5. If the access issue represents a security incident, create an **AI case** with sub-type "Adversarial attack" or appropriate type
6. If the issue is due to over-provisioned permissions, revise the agent's role assignments via the agent configuration in AI Agent Studio

---

## Access Map and the Security Score

The Access map feeds directly into the **AI Asset Security Score**:

| Finding Type on Map | Security Score Impact |
|---|---|
| Privileged AI Agent (agent has admin/elevated permissions) | 0.63% score reduction per agent |
| Access issues detected | Contributes to the "Access issues" category in score |
| Sensitive information disclosure | 1.04% score reduction per agent |

Resolving access issues visible on the map → improves the security score.

---

## Access Map vs. AI Asset Security Score Detail View

These are two complementary views of the same underlying security data:

| View | Format | What It Shows | Best Used For |
|---|---|---|---|
| **Access map** | Node-graph visualization | Topology of agent relationships and access flows | Understanding which workflows connect to which agents and tools; investigating specific access issues by node |
| **AI Asset Security Score detail** | Table/list view | Aggregated score impact per AI asset | Prioritizing which assets to remediate first; tracking score improvement over time |

Use the Access map for **investigation and topology understanding**. Use the Security Score detail for **prioritization and progress tracking**.

---

## In Context: Security & Privacy Tab

The Access map is part of the broader Security & privacy dashboard:

```
Security & privacy tab
├── AI Insights (Now Assist summarized security posture)
├── Access map link → [Access Map page]
├── AI Asset Security Score (92/100)
│   ├── Improvements table (AI assets impacting score)
│   └── Muted table
├── Privileged AI Agents (area chart)
├── Dormant AI Systems (area chart)
├── ServiceNow instance access to MCP servers
│   ├── Authorized access attempts
│   └── Failed access attempts
├── Guardrails
│   ├── Prompt injection charts
│   ├── Offensive content charts
│   └── Sensitive data charts
└── Agentic output injection detection
```

The Access map is reached via the dashboard but lives on its own page (`All > AI Security and Privacy > Access Map`), making it accessible without navigating through the full dashboard.

---

## Governance Use Cases for the Access Map

### Use Case 1: Pre-deployment Agent Review

Before approving a new AI agent for production in the AICT playbook workflow:
1. Open the agent in Agent Studio
2. Navigate to the Access map and locate the agent
3. Review: what tables does it access? What tools does it use? Are any tools in Autonomous mode?
4. Compare against the intended scope from the agent's AI system record
5. Document findings in the Build and Test phase task close notes

### Use Case 2: Quarterly Security Review

As part of your quarterly AI governance review:
1. Open the Access map
2. Filter by Agentic workflows to review all agent orchestration patterns
3. Look for agents with warning icons — these are unresolved access issues
4. Check Tables accessed for each critical agent — compare against approved scope
5. Any table access outside approved scope = security finding → create AI task or AI case

### Use Case 3: Incident Investigation

When an AI case is created for suspected adversarial activity:
1. Identify the specific agent mentioned in the case
2. Open the Access map and locate the agent node
3. Review the Access issues panel: Resource, Operation, Count — when did the unusual access occur?
4. Review Tables accessed over the last month — what did the agent access leading up to the incident?
5. Map the agent's connections to upstream workflows and downstream tools
6. Document the access map findings in the AI case description and work notes

---

## Key Takeaways for AI Risk & Compliance Officers

1. **The Access map is your AI network topology diagram** — it shows who connects to what and who did what, for AI agents rather than network devices.
2. **Warning icons = immediate investigation required** — every warned node is an unresolved access issue that needs a root cause and remediation plan.
3. **Tables accessed = observed access audit trail** — compare this against intended scope; any gap is a security finding.
4. **Tool execution mode matters** — Autonomous tools that modify critical records (patient data, clinical decisions) are compliance risks; they should be Supervised.
5. **Access issues feed the Security Score** — resolving map-visible access issues directly improves the AI Asset Security Score.
6. **Use map for investigation, score table for prioritization** — these are complementary views, not competing ones.
7. **Include Access map review in the Build and Test lifecycle stage** — before an agent is approved for production, its access topology should be documented and verified.
8. **Access map shows last month of table access** — it is not a full historical audit log; for historical access records, consult the Security & privacy guardrails data and ServiceNow audit tables.

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 858–860*
