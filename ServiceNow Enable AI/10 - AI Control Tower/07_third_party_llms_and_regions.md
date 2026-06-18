# Explore the Third-Party LLMs and Regions
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Role: AI Risk & Compliance Officer Reference

---

## What Is This?

This section covers how AICT manages the configuration of Large Language Models (LLMs) and Small Language Models (SLMs) from third-party providers, including data routing, provider allowlists, fallback/spillover mechanisms, and configuration audit logs. For a Risk & Compliance Officer, this is the critical control point governing **which AI models are permitted, in which regions, and under what data residency constraints**.

---

## Configuration Scenarios by Region

| Scenario | Data Routing | Provider List | Editable? |
|---|---|---|---|
| **APJC, AMS & EMEA regions** | Regional routing (no global option available) | All allowed providers visible | Yes |
| **Regulated markets** | Data routing configuration NOT available | Limited provider list only | Read-only |

> **Risk Officer Note:** Regulated market instances (FedRAMP, NSC DOD IL5, Australia IRAP-Protected) have locked, read-only provider lists. Verify your environment classification before planning any AI capability roadmap.

---

## Data Routing

Data routing directs LLM/SLM requests to the most suitable datacenter to optimize traffic, reduce latency, and speed up response time.

### Two Types

| Type | Description | Compliance Implication |
|---|---|---|
| **Regional** | Requests route to datacenters within your region | Safer default for data residency compliance; may be government-mandated |
| **Global** | Requests route to the globally best datacenter | Higher risk — data may cross international borders |

**Configuration path:** `AI Control Tower > Configurations > Controls > AI model providers > Data routing`

> **Risk Officer Note:** Global data routing means LLM prompt content may cross international borders. Before enabling it, verify it is permissible under your DPAs, GDPR obligations, and applicable data localization laws.

---

## AI Model Providers

Two categories are tracked:

**1. AI Model Providers Supported by ServiceNow**
- Now LLM Service
- Now LLM-LTS Model (see below)
- AWS Claude
- Other ServiceNow-validated providers

**2. AI Model Providers Configured by Your Organization**
- Perplexity, IBM Watson, and other custom third-party providers

### Now LLM Service — LTS (Long Term Stable) Model

> *"Supports regulated industries, such as financial institutions, with stronger AI lifecycle management, governance, transparency, and compliance tools."*

The LTS model provides: predictable behavior (fewer unannounced model updates), stronger compliance guarantees, governance-friendly transparency, and enhanced lifecycle management.

> **Risk Officer Note:** For healthcare deployments with regulatory obligations (HIPAA, FDA SaMD), the LTS model's stability and compliance orientation may be required. It is the model choice for risk-averse, regulated-industry deployments.

---

## Fallback and Spillover

### Fallback

**Default: Active.**

If active AI systems use providers NOT in your allowed list, fallback allows those systems to continue operating on their default providers. If deactivated, those systems must be deactivated.

| Fallback Setting | What Happens | Governance Implication |
|---|---|---|
| **Active (default)** | Systems on non-allowed providers continue via default providers | Systems may run on providers not explicitly reviewed — governance gap |
| **Inactive** | Systems on non-allowed providers are deactivated | Forces explicit provider approval for all production systems — stricter governance |

> **Risk Officer Note:** Fallback OFF is the more conservative governance posture — every production AI system is explicitly tied to an approved provider. Fallback ON is operationally easier but may allow systems to run on providers that have not been through vendor risk assessment.

### Spillover

Only applies to **Azure OpenAI**. When regional Azure OpenAI capacity is limited, requests spill over to additional capacity. Spillover activates automatically when Azure OpenAI is selected as a provider.

> **Risk Officer Note:** Spillover may route your AI requests to Azure capacity in a different region when your home region is saturated. Confirm cross-region spillover is permissible under your Azure DPA and data sovereignty requirements.

---

## Impact Summary (Preview Tool)

The **Preview impact** button shows the consequences of your provider and fallback choices BEFORE you save. Always use this before any provider configuration change.

### Fallback OFF — What the Impact Summary Shows

| Column | Meaning |
|---|---|
| Total AI systems | All systems supported by allowed providers |
| AI systems supported by allowed providers | Systems whose skill sets are fully supported |
| **AI systems require deactivation** | **Active systems with NO supported provider — WILL GO OFFLINE** |
| AI systems can't be activated | Inactive systems with no provider support |

### Fallback ON — What the Impact Summary Shows

| Column | Meaning |
|---|---|
| Total AI systems | All systems supported by allowed providers |
| AI systems supported by allowed providers | Systems supported by your chosen providers |
| AI systems supported by fallback providers | Systems running on fallback — shown as non-compliant |

> **Risk Officer Note:** The "AI systems require deactivation" column is operationally critical. Review it with both governance and operations teams before committing any provider change in production.

### Support Matrix

After previewing, select an entry to open the Support Matrix — a table of all AI systems with their respective model providers, showing: AI system name, type, activation status, and selected model provider.

---

## Approval Controls

Located at: `Configurations > Controls > Approvals`

| Control | Default | Effect When Activated |
|---|---|---|
| **AI systems approval** | Inactive | All AI skills and agents require steward approval before deployment |
| **MCP servers approval** | Inactive | Unapproved MCP servers blocked in AI Agent Studio (error: "Approval is needed to display tools") |
| **AI models approval** | Inactive | All AI models require steward approval before deployment |
| **Automatically trigger playbooks** | Inactive | Auto-triggers approval workflows on asset submission (recommended for production) |

> **Risk Officer Note:** All three approval controls should be activated in production. In their default inactive state, AI systems, MCP servers, and AI models can be deployed without steward review — a significant governance gap. "Automatically trigger playbooks" must also be active in production to ensure no asset bypasses governance.

---

## Data Sharing

**Default: Active** (opt-in by default).

ServiceNow collects and uses instance data (inputs, outputs, edits) to improve AI products. Customers can opt out at any time.

**Opt-out path:** `Configurations > Data > Data sharing > Opt out`

> **Risk Officer Note:** In healthcare, sharing patient-interaction data with a vendor — even in aggregated form — may require HIPAA BAA review. Decide and document this opt-in/opt-out decision before go-live.

---

## Data Overflow Processing

**Default: Inactive.**

When Active: traffic spikes redirect to **Microsoft Azure datacenters** to maintain performance.

Note: Data sharing and data overflow processing features are available for sub-prod instances in **read-only mode** when Multi-instance setup is configured.

> **Risk Officer Note:** Data overflow to Azure is a cross-border data transfer consideration. Keep inactive in regulated environments unless Azure overflow is explicitly covered by your DPAs.

---

## Security & Privacy Guardrail Configuration

Located at: `Configurations > Data > Security & Privacy`

These four settings govern LLM output monitoring and are directly relevant to compliance:

### 1. Data Integrity Incident Detection (Default: Inactive)

Tracks when a model's output fails to match expected behavior categories.
- **Categories:** Based on OWASP Top 10 Risk & Mitigations for LLMs + OpenAI model specification
- **Sampling rate:** % of transactions evaluated (100% = most accurate)
- **Max skill calls per execution:** Min 10, Default 1,000
- **Analysis mode:** Single LLM or Multiple LLMs (3+ with majority vote; must be odd number)
- If deactivated: past data visible for 90 days

### 2. Agent Goal Deviation (Default: Inactive)

Detects when AI agents deviate from their intended role or objective (unauthorized actions, prompt injection).
- Same sampling rate and max skill calls settings as above
- Same single vs. multiple analysis options
- Note: Due to probabilistic nature, not all occurrences may be identified
- If deactivated: past data visible for 90 days

### 3. Output Screening (Default: configurable)

Monitors AI agent output for PII and security-vulnerable patterns.

| Sub-setting | What It Monitors |
|---|---|
| Output Security Vulnerability | Agentic output injection: HTML tag injection, SQL injection, XSS, Terminal RCE, non-printable characters |
| Output Extended PII | Additional PII patterns: U.S. CA driver's license, U.S. passport number, vehicle ID number |
| Output PII Violation | Standard PII from Data Privacy config: U.S. phone number, credit card number |

If deactivated: past data visible for 90 days.

### 4. Sensitive Data Input and Anonymization

Shows data patterns from Data Privacy enabled for detecting and anonymizing PII in LLM prompts.
- Requires Data privacy plugin
- Use as quick reference when troubleshooting Sensitive data detected and Sensitive data anonymized charts
- Governed by the User data usage policy for Now Assist

### Score Weight Configuration

Controls how LLM guardrail categories are weighted in the AI Asset Security Score.
- Default weights can be changed
- Categories can be deactivated to remove from scoring
- Formula: average across all managed AI assets

> **Risk Officer Note:** In healthcare, Output PII Violation and Output Extended PII must be Active. An agent that outputs PHI in LLM responses without detection is a HIPAA breach. All four guardrail settings should be active in production with sampling rates as close to 100% as performance allows.

---

## Audit Logs

All configuration changes to Data, Approvals, and AI model providers are captured and available via `View audit logs` (top right of the Configurations page).

| Field | Description |
|---|---|
| Timestamp | When the change was made |
| User | Who made the change |
| Changed category | Data / Approvals / AI model providers |
| Changed setting | The specific setting modified |
| After change | New value |
| Before change | Previous value |

**Filter:** Date range starting with last 90 days.

**Multi-instance note:** When a sub-prod instance is added/removed from syncing, audit logs first show all instances removed, then a record of the instance being added/removed.

> **Risk Officer Note:** Audit logs are your governance evidence trail for provider and approval configuration changes. Every change must be tied to a change request. The 90-day default view means logs must be exported regularly if your audit retention requirements exceed 90 days.

---

## Key Takeaways for AI Risk & Compliance Officers

1. **Regional data routing is the safer default** — global routing creates data sovereignty risk.
2. **Regulated market instances have locked provider lists** — verify environment classification before planning.
3. **Fallback ON (default) creates a governance gap** — consider deactivating in production for stricter control.
4. **Always use Preview impact before changing providers** — the deactivation column is critical operational intelligence.
5. **All three approval controls should be Active in production** — AI systems, MCP servers, and AI models all require steward review.
6. **Data sharing and data overflow are DPA/legal decisions** — decide before go-live.
7. **All four guardrail settings should be Active in healthcare** — especially Output PII Violation and Output Extended PII.
8. **Audit log retention is 90 days default** — export proactively if your compliance requires longer retention.

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 758–766, 86*
