# AI Control Tower Dashboard
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Role: AI Risk & Compliance Officer Reference

---

## What Is This?

The AI Control Tower dashboard is the primary operational interface for governing AI across the enterprise. It provides a comprehensive overview of AI status, AI inventory, and AI-related metrics across multiple specialized tabs. Each tab is a distinct monitoring surface with drill-down capability.

---

## Dashboard Architecture

The dashboard home page (`Workspaces > AI Control Tower`) features:
- **Top action bar** — displays task statuses, pending asset reviews, and newly added AI systems
- **Tab navigation** — eight specialized tabs covering different governance dimensions

Dashboard data is **transactional** (not historical by default). Data only populates once assessments are completed. On first installation, all widgets are empty.

**Two scheduled jobs** drive trend data:
- `AI Control Tower Core Monthly Data Collection` — runs monthly, displayed quarterly
- `AI Control Tower Core Historical Data Collection` — must be run manually to backfill past data

---

## Tab 1: Overview

**Role required:** AI steward

The Overview tab is the executive summary of the AI estate. It shows the **State of AI** across the enterprise.

### Widgets on the Overview Tab

| Widget | What It Shows |
|---|---|
| **All AI systems** | Count of AI systems by lifecycle stage: New, Assess, Build and test, Deploy |
| **AI systems by type** | Breakdown by Agentic AI, Generative AI, Classic AI |
| **Risk classification** | AI systems classified as High, Medium, Low, Unacceptable risk |
| **AI systems by provider** | Count of AI systems by provider (donut chart; note: Other category hidden if >5 providers) |
| **Compliance** | Compliance effectiveness % for active controls on Authority documents and Policies |
| **AI cases by priority** | Total AI cases with breakdown by priority rating |
| **AI systems trend** | Historical trend of AI system additions and deployments (quarterly, driven by scheduled jobs) |

> **Risk Officer Note:** The Overview tab is your governance dashboard at a glance. The Risk classification widget is the first signal of portfolio risk. The Compliance widget tells you how many controls are passing vs. failing against authority documents (EU AI Act, GDPR, etc.). Monitor these two together — high unacceptable risk + low compliance posture = immediate escalation trigger.

---

## Tab 2: AI Strategy

**Prerequisite:** Strategic Portfolio Management (SPM) Professional license required

The AI Strategy tab connects AI governance to strategic portfolio planning. It shows:

### Sections

**Strategy**
- AI strategies and goals linked to the AI Control Tower workspace
- Goals classified as Artificial Intelligence from Goal Framework or Strategic Planning Workspace

**Costs**
- Tracks AI planning items (projects, epics, demands) comparing:
  - Planned cost vs. Budgeted cost vs. Actual cost
- Planning items must have `Investment type = Artificial Intelligence` in Strategic Planning Workspace

**Prioritized AI work**
- Shows projects, epics, and demands in `Prioritized` state with `Investment type = Artificial Intelligence`
- Tracks what AI work is being planned and executed

**AI RIDAC**
- Risks, Issues, Decisions, Actions, Changes at the project level
- Appears for projects with:
  - `Investment type = Artificial Intelligence` in PPM Standard
  - Primary goal category = `Artificial Intelligence` in Goal Framework or Strategic Planning
  - Strategic priority type = `Artificial Intelligence`

> **Risk Officer Note:** AI RIDAC is one of the most valuable features for a Risk Officer. It bridges strategic risk (project-level) with operational AI governance. If a project carrying an AI investment also has open risks or issues in RIDAC, those should be reflected in the AI asset's risk register in AIRC. This integration closes the gap between program risk management and AI asset governance.

---

## Tab 3: AI Asset Inventory

**Role required:** AI steward

The AI asset inventory tab catalogs all AI-related assets used by the organization.

### Widgets

| Widget | What It Shows |
|---|---|
| **AI systems by provider** | Donut chart of systems by provider |
| **AI systems by type** | Agentic AI, Generative AI, Classic AI |
| **All AI systems (by lifecycle status)** | Steward review, Approved for development, Ready for deployment, Deploy |
| **AI asset inventory by department** | Bar graph of systems by Providers and Components per department |

### Asset Counts Tracked

- AI systems
- AI models
- Prompts
- Datasets
- MCP servers

---

## Tab 4: Value

**Role required:** AI steward

The Value tab measures the business return from AI systems. It is organized into four sub-sections.

### Productivity Indicators

| Metric | Description | Data Source |
|---|---|---|
| Total productivity gained | Estimated productivity gains in hours from AI systems including third-party | ServiceNow + third-party AI |
| Average AI users | Average unique users of ServiceNow AI systems in date range | ServiceNow only |
| Top 5 AI systems by value (hrs) | Top 5 systems delivering most value | ServiceNow + third-party |
| Task closure efficiency gain | % improvement in task completion time using AI vs. manual | ServiceNow only |
| Top 10 AI systems consuming assists | Highest consumption of assists | ServiceNow only |
| AI systems with no usage | Deployed AI systems with no usage in selected period | ServiceNow + third-party |
| System summary | All AI systems with user count and productivity details | ServiceNow + third-party |

### Engagement Indicators

| Metric | Description |
|---|---|
| Total AI actions | Total LLM-related actions across all skills | ServiceNow + third-party |
| Usage by department | Top 5 departments by AI system usage; "Others" = users with empty department | ServiceNow + third-party |
| Countries with highest AI adoption | Top 5 countries by AI system usage | ServiceNow + third-party |
| Countries with lowest AI adoption | Top 5 countries with least AI system usage | ServiceNow + third-party |
| AI actions comparison by user department | # and type of AI actions by up to 5 departments | ServiceNow + third-party |

### Quality Indicators

| Metric | Description |
|---|---|
| Positive feedback | Summary of positive feedback for all AI executions | ServiceNow only |
| % of task closed using AI system | Tasks completed with an associated AI execution plan (incident, problem, change, case, request) | ServiceNow only |
| Success rate | % of successful AI executions across all AI systems | ServiceNow only |
| Success rate summary | All AI systems with successful executions and details | ServiceNow only |

### Creator Skills Indicators

| Metric | Description |
|---|---|
| Highest instance usage | Highest % of instance usage | ServiceNow only |
| Highest skill usage | Highest % of assists by one skill | ServiceNow only |
| Total creator calls | Total calls for creator skills across the instance | ServiceNow only |
| Accepted creator calls | Total accepted creator calls | ServiceNow only |
| Skill satisfaction | Skill satisfaction by usage and approvals | ServiceNow only |
| Designation with highest creator calls | Designation with highest creator skill usage | ServiceNow only |
| Creator calls by skill | # creator calls by skills | ServiceNow only |
| Creator calls by instance name | # creator calls by instance names | ServiceNow only |
| Creator calls by code environment | # creator calls by code environments | ServiceNow only |
| Creator call by title/designation | # creator calls by designation | ServiceNow only |

> **Risk Officer Note:** Value metrics matter for risk governance for two reasons. First, high-value AI systems that perform poorly or have quality issues represent **compounded risk** — failure of a high-impact system has outsized consequence. Second, "AI systems with no usage" is a **security and governance risk** — deployed but unused systems still carry permissions, data access, and attack surface. Dormant systems should be reviewed for decommissioning or suspension.

---

## Tab 5: Health

The Health tab monitors guardrail performance through **Now Assist Guardian**.

### What It Monitors
- Average latency added by active offensive content and prompt injection guardrails
- Count and percentage of offensive content and prompt injection occurrences
- Skills where occurrences were detected

> **Note:** The Health tab does NOT use historical data. It reflects the current period only.

### Content Guardrail Effectiveness

| Metric | Description |
|---|---|
| Number of content items flagged | Offensive content + prompt injection occurrences in selected date range |
| % of content items flagged of total use | % of LLM requests/responses flagged for offensiveness or prompt injection |

### Offensive Content Visualizations

| Metric | Description |
|---|---|
| Guardrail-added latency | Average latency from active offensive content guardrail per skill/date range |
| Percentage flagged as offensive | % of LLM requests/responses flagged for offensive content |
| Total offensive content occurrences | Total occurrences for selected skills and date range |
| Categories of offensive content | Breakdown by category (note: multi-category content counts toward each category) |
| Offensive content occurrences by skill | Occurrences over time by skill |

### Prompt Injection Visualizations

| Metric | Description |
|---|---|
| Guardrail-added latency | Average latency from active prompt injection guardrail |
| Percentage flagged as prompt injection | % of LLM requests/responses flagged |
| Total prompt injection occurrences | Total occurrences |
| Prompt injection occurrences by skill | Over time by skill |

> **Risk Officer Note:** Prompt injection is a top-tier AI security risk. High prompt injection rates against specific skills indicate those skills are being targeted. Offensive content violations in agent outputs indicate either guardrail misconfiguration or model drift. Both require incident response. High guardrail latency could mean guardrails are over-triggered and need tuning.

---

## Tab 6: Risk & Compliance

The Risk & Compliance tab displays risk posture and compliance status across the AI asset inventory.

### Compliance Overview Section

**Regulatory risk classification**
- Donut charts showing risk classification of AI systems, AI models, and Datasets
- Classifications: High, Medium, Low, Unacceptable

**Compliance by authority documents and policies**
- Shows compliance effectiveness against selected authority documents (EU AI Act, GDPR, etc.) and policies
- Filterable by specific authority document or policy
- Drill-down into issues requiring immediate attention and AI cases by authority document/policy

> **Important legal disclaimer from the documentation:** *"The authority documents are provided solely for informational and guidance purposes to assist with the initial setup of AI Risk and Compliance frameworks. It does not constitute legal advice or assurance of regulatory compliance. You are solely responsible for ensuring that all use of the content complies with applicable laws, regulations, directives, and industry standards in their jurisdictions."*

### Risk Overview Section

**AI systems by aggregated risk score**
- Classification of AI systems by aggregated risk score (High/Low)

**Risk heatmap**
- Visualization of all identified risks within AI assets
- Default filter: residual risk
- Can be toggled to inherent risk

> **Risk Officer Note:** The Risk & Compliance tab is your primary operational dashboard. Configure which authority documents appear here via system properties (`Set up properties for compliance posture`). In a CareAtlas / healthcare context, HIPAA, EU AI Act (if applicable), and NIST AI RMF should all be configured as visible authority documents. The risk heatmap gives you an instant read on whether risks are being effectively controlled (residual risk low) or not (residual ≈ inherent, meaning controls are ineffective).

---

## Tab 7: AI Cases

Tracks, monitors, and analyzes AI case workflows.

### AI Cases Sub-Tab

| Widget | Description |
|---|---|
| AI cases status by state | Distribution of AI cases by lifecycle/workflow state |
| AI cases status by priority | Cases by priority: Critical, High, Moderate, Low, Planning |
| AI cases (All / Overdue / Due in 7 days / Unassigned) | Filtered views of cases; each card drills to list view |
| Trends — AI cases by subtype | Trend over time by case category |
| Trends — Issues linked to AI cases | Counts by state (New, Review, Responds) and urgency (Overdue, Due in 7 days, Unassigned) |

**Actions from this tab:**
- `Create AI case` button — initiates a new case record for documenting, investigating, or tracking issues, risks, or compliance concerns related to AI models or datasets
- `Create issue` button — creates an issue linked to an AI case

### Inquiries Sub-Tab

| Widget | Description |
|---|---|
| Inquiries status by state | Counts by state: New, Triage, In progress, Approved |
| Inquiries status by priority | Critical, High, Moderate, Low, Planning |
| Inquiries (list) | All AI inquiries; filterable by status, priority, assignment |
| Trends — Inquiries by business unit | Distribution across departments |

Inquiry metadata tracked: Name, Requested by, Assigned to, State, Priority

> **Risk Officer Note:** AI Cases are the escalation mechanism in AICT. When risk assessments find violations, or when the AI steward identifies a concern, a case is the formal record. Inquiries are the pre-case triage mechanism — a stakeholder asks a question or raises a concern, it becomes an inquiry before being escalated to a case. Maintain zero unassigned cases as a governance KPI.

---

## Tab 8: Security & Privacy

Reviews AI asset security metrics and maps agent relationships.

### ServiceNow AI Insights
Requires: `Now Assist AICT security posture summarizer` skill enabled

Provides AI-generated summaries of:
- **Positives** — enabled settings and features improving security posture
- **Areas for Attention** — low-to-medium risk items to resolve
- **High Impact Observations** — high-risk items requiring immediate action
- **Actions** — suggested remediation steps

### Access Map
- Node-graph visualization of relationships between ServiceNow agents, agentic workflows, and tools
- Navigate via: `All > AI Security and Privacy > Access Map` or dashboard link
- Warning icons indicate access issues on specific agents
- Drill into warnings to see: workflow, agent, tool associated with the issue
- In Access issues: User ID = the user who ran the agent

### AI Asset Security Score
A composite health score for all AI assets calculated from:
- Access issues (privileged AI agents)
- Dormant AI systems
- Sensitive information disclosure risk

**Score detail view:** Select `See details` in the Security & privacy tab.

**AI assets impacting your score** — table columns:

| Column | Description |
|---|---|
| AI system | Name of the AI asset |
| Category | Issue type: Dormant AI system, Privileged AI agent, Access issue, Sensitive information disclosure |
| Provider | ServiceNow or external |
| Score impact | % impact to the AI asset security score |
| Date | Date the issue occurred |

**Actions from this view:**
- `Mute` an asset — excludes it from score calculation (e.g., if remediation would be a risky change)
- `Create AI task` — creates a tracked security remediation task

**Score bands:**
- **Good (80–100%)** — Low risk; configurations align with ServiceNow guidelines; ideal for production
- **Fair (50–79%)** — Moderate risk; typical for non-production or staged rollouts
- **Bad (<50%)** — High risk; requires immediate hardening and vulnerability remediation

**Privileged AI Agents**
- Area chart showing agents with elevated permissions (admin, security admin)
- AWS Bedrock agent metrics available if AWS account configured + `Now Assist AiSP AWS IAM privileged policy checker` skill enabled
- Create AI task directly from list view

**Dormant AI Systems**
- Area chart showing AI agents not active for over 90 days
- Auto-creates an AI asset security task assigned to the agent's owner when a system goes dormant
- Tasks over 180 days old are archived (archival window configurable in system properties)

### MCP Server Access Metrics

| Metric | Description |
|---|---|
| Authorized access attempts to MCP servers | Successful access from MCP clients through AI Gateway |
| Failed access attempts to MCP servers | Unsuccessful access attempts through AI Gateway |

### Guardrails Section

| Section | Data Source |
|---|---|
| Prompt injection | Now Assist Guardian analytics |
| Offensive content | Now Assist Guardian analytics |
| Sensitive data detected | Sensitive data identified in user responses to Now Assist prompts |
| Sensitive data anonymized | Prompt data that matched configured PII patterns and was anonymized |

### Agentic Output Injection Detection
- Detects when agents' LLM output contains known security-vulnerable patterns
- Patterns monitored: `Eval-Function-Audit`, `Html-Tag-injection`, `Non-printable-class`, `Script-Tag-injection`, `SQL-query-injection`, `Terminal-RCE`
- Source table: `sn_data_discovery_data_pattern` in AI Security and Privacy application
- Analysis is deterministic (rule-based, not probabilistic)

> **Risk Officer Note:** The Security & Privacy tab is where AI security governance meets AI compliance governance. For a healthcare context like CareAtlas: SQL injection and HTML tag injection in agent outputs are critical findings that require immediate incident response. Dormant agents with patient data access are a HIPAA risk. The Access Map is your tool for understanding which agents have access to which systems — equivalent to a network topology map but for AI agents. Review it before every new agent deployment.

---

## Tab 9: AI Gateway

**Role required:** AI steward

Shows metrics at the MCP (Model Context Protocol) server level:
- Lists all connected MCP servers
- Total number of transactions per server
- Success rate per server

This is the observability surface for AI agent interoperability across platforms.

---

## Dashboard Configuration Notes

- **Compliance display:** Configure which authority documents and policies appear via `Set up properties for compliance posture` (system properties)
- **Archival:** Resolved AI asset security tasks over 180 days are archived; configurable in system properties
- **Data freshness:** Trend data driven by monthly scheduled job; run Historical job after install for backfill

---

## Key Takeaways for AI Risk & Compliance Officers

1. The dashboard has **8 specialized tabs** — each addresses a distinct governance dimension; know which tab answers which question.
2. **Overview + Risk & Compliance** are your daily monitoring tabs.
3. **Health tab** is your real-time security signal for guardrail effectiveness.
4. **Security & Privacy tab** is your AI security posture — treat the security score as a KPI with a minimum threshold (e.g., maintain >80% Good).
5. **AI Cases tab** is your incident and compliance case management surface — zero unassigned cases is a governance standard to aim for.
6. **AI Strategy tab** (if SPM licensed) bridges strategic risk with operational AI governance.
7. **Value tab** helps you identify high-value/high-risk combinations and dormant systems.
8. Dashboard data requires **scheduled jobs to be active** — verify this immediately after installation.

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 694–732*
