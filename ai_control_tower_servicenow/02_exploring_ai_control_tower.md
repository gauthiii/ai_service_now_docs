# Exploring AI Control Tower
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Role: AI Risk & Compliance Officer Reference

---

## What Is This Section?

"Exploring AI Control Tower" is the conceptual foundation of AICT. It defines what the platform is, what it governs, how it is architecturally structured, and what value it delivers. Before using or configuring AICT, this is the mental model every practitioner — especially a Risk & Compliance Officer — needs to internalize.

---

## AI Control Tower Overview

> *"AI Control Tower provides enterprises with visibility into their AI footprint, manages the lifecycle of their AI investments, and identifies risks. This AI Control Tower's functionality ensures that their AI models, workflows, and agents are governed, optimized, and aligned with business strategy."*

AICT is structured around **six functional pillars**:

| Pillar | What It Does | Risk & Compliance Relevance |
|---|---|---|
| **AI Strategy & Value** | Tracks how AI improves efficiency, revenue, and cost savings | Links AI investments to business outcomes; supports ROI governance |
| **AI Governance & Compliance** | Ensures AI systems follow company policies and global regulations, focusing on privacy, data governance, and ethical AI | **Primary pillar for Risk Officers** — directly maps to regulatory frameworks |
| **Security, Access & Privacy** | Manages AI agent identities, access controls, and sensitive data | Identity governance for non-human AI agents; PII handling |
| **Lifecycle Management** | Handles the entire lifecycle of AI assets including onboarding, offboarding, skill management, and performance monitoring | Asset lifecycle is the operational backbone of governance |
| **Health & Performance** | Evaluates how reliably and efficiently AI systems operate | Performance degradation can signal risk; monitoring is a control |
| **Enterprise AI Integrations** | Provides a platform to discover and use AI projects, models, and data from within the company and external partners | Third-party AI discovery and shadow AI governance |

---

## AI Asset Data Model

The **AI Asset Data Model** is the foundational taxonomy of everything AICT governs. It catalogs four types of AI assets and manages the relationships between them:

```
AI Asset Inventory
├── AI Systems       (the deployable AI applications and agents)
├── AI Models        (the trained ML/AI models powering systems)
├── Datasets         (training, evaluation, and test data)
└── Prompts          (instructions that guide model outputs)
```

The data model also captures **relationships between assets** — for example, which AI model powers which AI system, or which dataset was used to train which model. This relationship mapping is critical for:
- **Risk traceability** — if a model has a known bias, which systems are affected?
- **Audit trails** — who approved what, when, and under what conditions?
- **Impact analysis** — if a dataset is found to be non-compliant, what downstream assets are affected?

> **Risk Officer Note:** The AI Asset Data Model is the equivalent of a Configuration Management Database (CMDB) for AI. Just as you wouldn't govern IT without a CMDB, you cannot govern AI at scale without this inventory. Populating and maintaining it is a governance prerequisite, not a nice-to-have.

---

## AI Control Tower Benefits

The documentation states four key benefits:

1. **Visibility and management** of enterprise AI across the organization
2. **Lifecycle management** of AI assets (systems, models, prompts, datasets)
3. **Identify risks and set controls** — the direct GRC value proposition
4. **Proactively manage AI risks and compliance** while protecting the business and speeding up AI innovation

The framing is deliberately balanced: governance is positioned not as a brake on innovation but as an enabler of responsible, faster AI deployment.

---

## What AICT Connects To

AICT is not a standalone tool. It is a hub that integrates with other ServiceNow modules and external systems:

| Integration | Purpose |
|---|---|
| **AI Control Tower dashboard** | Unified visibility across all AI assets |
| **Configure AI Control Tower** | Workflow, playbook, and automation setup |
| **AI Risk and Compliance** | Formal GRC module for risk assessments and compliance |
| **Explore Now Assist AI asset discovery** | Discovers ServiceNow-native AI assets automatically |
| **Enterprise AI discovery** | Discovers third-party AI assets via cloud connectors |
| **AI Gateway** | MCP server governance and cross-platform agent interoperability |
| **Using AI Control Tower** | Operational workflows for stewards and owners |
| **AI Control Tower reference** | Roles, tables, and system architecture |

---

## Navigation Structure by Persona

AICT presents different navigation views depending on the user's role:

| Persona | Navigation Access |
|---|---|
| **AI Steward** | Home page, AI assets, Configurations (full access) |
| **Product Owner / Asset Owner** | Home, AI assets (own assets only) |
| **AI Control Tower workspace user** | Home page, AI assets |
| **Risk and Compliance user** | Home page, AI assets |

> **Risk Officer Note:** The AI Steward role is the most powerful governance role in AICT. It has access to the full state of AI across all inventory, value and adoption insights, configurations, and approval workflows. The Risk and Compliance user role has dashboard visibility but is scoped primarily to the Risk & Compliance module. You will typically operate across both roles or coordinate between them.

---

## The AI Strategy Tab (Important Prerequisite)

The **AI Strategy tab** within AICT requires a **Strategic Portfolio Management (SPM) Professional license**. This tab enables:
- Tracking AI costs (planned vs. budgeted vs. actual)
- Monitoring prioritized AI work (projects, epics, demands)
- Tracking AI RIDAC items (Risks, Issues, Decisions, Actions, Changes)

> **Risk Officer Note:** If your organization has SPM Professional, this tab gives you a direct link between AI governance and strategic project tracking. AI RIDAC items in particular are directly relevant — project-level risks that flow from SPM into AICT create an integrated risk picture from strategic planning to operational AI governance.

---

## Scheduled Data Jobs (Critical for Dashboard Accuracy)

AICT dashboard data is not real-time for trend metrics. Two scheduled jobs govern data availability:

| Job | Frequency | Purpose |
|---|---|---|
| **AI Control Tower Core Monthly Data Collection** | Monthly | Collects data going forward; displayed quarterly via aggregation |
| **AI Control Tower Core Historical Data Collection** | Manual / On-demand | Collects historical data from previous months |

**Important:** When AICT is first installed, there is no data. The Historical Data Collection job must be run manually to backfill data. Without it, dashboards will show empty trend charts.

> **Risk Officer Note:** This is a common gotcha during initial setup and demonstrations. Always run the Historical Data Collection job after installation. For ongoing governance, confirm the Monthly job is active and not blocked by maintenance windows.

---

## Key Takeaways for AI Risk & Compliance Officers

1. AICT is structured around **six governance pillars** — understanding which pillar each risk or control maps to helps prioritize governance work.
2. The **AI Asset Data Model** (systems, models, datasets, prompts) is the foundational inventory — it must be complete and accurate for any governance activity to be meaningful.
3. AICT is a **hub, not a silo** — it integrates with Risk & Compliance, AI Gateway, discovery, and SPM modules.
4. **Role-based access** is tightly scoped — the AI Steward role is the governance fulcrum; ensure the right people have it.
5. **Dashboard data requires manual backfill** after first installation — schedule this immediately post-setup.
6. The SPM integration enables **strategic-to-operational risk traceability** — valuable if your organization uses SPM.

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 692–695*
