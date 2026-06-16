# Enterprise AI Discovery: Unlock Visibility, Governance & Value
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Role: AI Risk & Compliance Officer Reference

---

## What Is This?

Enterprise AI Discovery is the mechanism for finding, cataloging, and governing AI assets that exist **outside** the ServiceNow platform — in cloud hyperscalers (AWS, GCP, Azure), agentic AI frameworks (LangGraph, n8n, Salesforce), and other external AI ecosystems. It uses **Service Graph Connectors (SGC)** to pull AI asset metadata from third-party APIs into AICT's AI Asset Inventory and the ServiceNow CMDB.

While Now Assist AI Asset Discovery handles ServiceNow-internal assets, Enterprise AI Discovery handles the rest of your AI footprint — the shadow AI and the cloud-native AI you don't fully see yet.

---

## Why Enterprise AI Discovery Exists

> *"Fragmented AI ecosystems create governance and compliance risks. Enterprises need real-time visibility into AI usage including shadow AI to ensure security, compliance, and operational efficiency."*

The documentation identifies the core problem directly: most enterprises have AI deployed across multiple cloud platforms, built with multiple frameworks, managed by multiple teams. Without a unified discovery mechanism, these assets are invisible to governance — they exist, they run, they make decisions, but no risk assessment has been done, no compliance mapping has been created, and no lifecycle exists for them.

Enterprise AI Discovery is the answer to shadow AI governance at scale.

---

## Key Benefits

| Benefit | Description |
|---|---|
| **Eliminate Blind Spots** | Aggregate fragmented AI assets from all platforms into a single unified view |
| **Accelerate Governance** | Centralize compliance, security, and operational efficiency across all AI |
| **Drive Innovation** | Enable responsible, scalable, and auditable AI ecosystems where governance and innovation coexist |

---

## How It Works — Service Graph Connectors (SGC)

Service Graph Connectors are ServiceNow's mechanism for importing and integrating third-party data into CMDB and non-CMDB tables.

**Data flow:**
```
Third-party API (AWS, Azure, GCP, etc.)
    |
    v returns JSON data
Staging Tables (import set tables)
    |
    v transform maps convert JSON to ServiceNow format
Target Tables (CMDB CI classes + AICT digital asset tables)
    |
    v visible in
AI Asset Inventory in AICT
```

**Benefits of SGC approach:**
- Gains trust in CMDB data (verified import process)
- Minimizes operational risk
- Minimizes custom integrations (pre-built connectors)
- Accelerates time to value

**Note:** Assets and CIs are identified using their unique source IDs — e.g., ARN (Amazon Resource Names) for AWS. Product Models are identified by the associated asset.

---

## Required Plugins

The AI connections page appears ONLY when these plugins are installed:
- `com.sn_ai_disc` — AI Discovery plugin
- `sn_sgc_central` — SGC Central

**Important:** Uninstall the AWS AI Discovery plugin BEFORE installing the AI Discovery plugin (`sn_ai_disc`) to use the AI connections.

---

## Required Roles (All Connectors)

| Role | Purpose |
|---|---|
| `sn_ai_disc.discovery_admin` | Discovery administration for AI connections |
| `sn_cmdb_int_util.sgc_admin` | Service Graph Connector administration |

---

## AI Connections Page

**Navigation:** `AI Control Tower > Configurations > AI connections`

The AI connections page is the management hub for all enterprise AI discovery connections. Features:
- List all data sources in columns
- Create new AI connections
- Manage existing connections
- Activate/deactivate connections via State column (AI steward action)
- Manually trigger discovery or usage data collection
- Adjust run frequency via connection alias (admin action)

**Two types of scheduled jobs per connection:**
- **Discovery:** Discovers AI assets from hyperscalers, AI apps, and agentic frameworks
- **Execution:** Processes usage data; data visible in Performance analytics for each discovered agent

**Critical requirement:** Confirm the **AI discovery daily data collection job is active** — this is the key element in collecting usage data.

Existing connections appear under the **Legacy connections** section.

---

## Available Service Graph Connectors (as of March 2026)

| Connector | Discovers | Supported SN Versions |
|---|---|---|
| **AWS (Bedrock + AgentCore + SageMaker)** | AI systems, agents, models, tools, prompts, usage | Australia, Zurich patch 7, Yokohama patch 11 |
| **GCP Vertex AI** | AI systems, models, prompts, tools, usage | Australia, Zurich patch 7, Yokohama patch 11 |
| **LangGraph** | AI systems, agents, models, tools, prompts, usage | Australia, Zurich patch 7, Yokohama patch 11 |
| **Microsoft (Azure Foundry + Copilot Studio)** | AI systems, models, prompts, tools, usage | Australia, Zurich patch 7, Yokohama patch 11 |
| **n8n** | AI systems, models, prompts, tools, usage | Australia, Zurich patch 7, Yokohama patch 11 |
| **Salesforce** | AI systems (agents), models, tools, prompts, usage | Australia, Zurich patch 7, Yokohama patch 11 |

---

## Connector Deep Dives

### 1. AWS (Amazon Bedrock, AgentCore, SageMaker)

**Download:** ServiceNow Store — AI Service Graph Connector for Amazon

**AWS Prerequisites:**
- Active AWS account
- IAM Credentials: Access Key ID + Secret Access Key with read permissions
- API access enabled for: Amazon Bedrock, Amazon SageMaker, Amazon CloudWatch, Amazon Bedrock AgentCore

**Required IAM Permissions:**
- Amazon Bedrock: `bedrock:List*`, `bedrock:Get*`
- Amazon SageMaker: `sagemaker:List*`, `sagemaker:Describe*`
- Amazon CloudWatch: `logs:DescribeLogGroups`, `logs:DescribeLogStreams`, `cloudwatch:GetMetricData`
- Amazon Bedrock AgentCore: `bedrock:ListAgents`, `bedrock:GetAgent`

**Data Mapping (Source → Staging → Target):**

| Data Source | Staging Table | Target Table |
|---|---|---|
| Bedrock AI Asset | `sn_ai_disc_aws_sgc_bedrock_ai_asset` | Routes to other staging tables |
| Bedrock AI System | `sn_ai_disc_aws_sgc_bedrock_ai_system` | `alm_ai_system_digital_asset` |
| Bedrock AI Model | `sn_ai_disc_aws_sgc_bedrock_ai_model` | `alm_ai_model_digital_asset` |
| Bedrock AI Tool | `sn_ai_disc_aws_sgc_bedrock_ai_tool` | `sn_ent_ai_tool` |
| Bedrock AI Prompt | `sn_ai_disc_aws_sgc_bedrock_ai_prompt` | `alm_ai_prompt_digital_asset` |
| Bedrock Subcomponent M2M | `sn_ai_disc_aws_sgc_bedrock_sbcomp_m2m` | `sn_ent_ai_system_subcomponent_m2m` |
| Bedrock Usage | `sn_ai_disc_aws_sgc_bedrock_ai_usage` | `sn_ai_disc_ai_usage` |
| AgentCore Runtime | `sn_ai_disc_aws_sgc_agentcore_ai_system` | `alm_ai_system_digital_asset` |
| AgentCore Tool | `sn_ai_disc_aws_sgc_agentcore_ai_tool` | `sn_ent_ai_tool` |
| AgentCore Usage | `sn_ai_disc_aws_sgc_agentcore_ai_usage` | `sn_ai_disc_ai_usage` |
| SageMaker Model | `sn_ai_disc_aws_sgc_sg_awssagemaker_model` | `alm_ai_model_digital_asset` |

**Setup steps (high-level):**
1. Navigate to `AI Control Tower > Configurations > AI connections > Add > AWS > Create connection`
2. Select source systems: Amazon Bedrock, Amazon Bedrock AgentCore, Amazon SageMaker
3. Configure Bedrock: Connection Name, Access Key ID, Secret Access Key, AWS Region → Update and test
4. Configure Bedrock import schedule: activate parent schedule, set run frequency, optionally Execute now
5. Configure CloudWatch logs for Bedrock: Connection Name, Access Key, Secret Key, AWS Region, Log Group Names → Create and test
6. Configure CloudWatch import schedule for Bedrock
7. Configure SageMaker: Connection Name, Access Key ID, Secret Access Key, AWS Region → Create and test
8. Configure SageMaker import schedule
9. Configure CloudWatch monitoring for SageMaker
10. Configure CloudWatch monitoring import schedules for SageMaker

---

### 2. GCP Vertex AI

**Download:** ServiceNow Store — AI Service Graph Connector for GCP Vertex AI

**Prerequisites:** Create service account, assign roles, bind roles to service account, enable APIs, create JKS file, register in ServiceNow instance. See KB2731256 for full setup instructions.

**Data Mapping:**

| Data Source | Staging Table | Target Tables |
|---|---|---|
| GCP Execution | `sn_ai_disc_gcp_sgc_sg_gcp_execution` | `sn_ai_disc_ai_usage` |
| GCP AI System | `sn_ai_disc_gcp_sgc_sg_gcp_ai_system` | `cmdb_ai_system_component_product_model`, `alm_ai_system_digital_asset`, `cmdb_ci_function_ai`, `cmdb_rel_asset_ci` |
| GCP AI Model | `sn_ai_disc_gcp_sgc_sg_gcp_ai_model` | `cmdb_ai_model_product_model`, `alm_ai_model_digital_asset` |
| GCP AI Tool | `sn_ai_disc_gcp_sgc_sg_gcp_ai_tool` | `sn_ent_ai_tool` |
| GCP AI Prompt | `sn_ai_disc_gcp_sgc_sg_gcp_ai_prompt` | `cmdb_ai_prompt_product_model`, `alm_ai_prompt_digital_asset` |
| GCP System Subcomponent M2M | `sn_ai_disc_gcp_sgc_sg_gcp_ai_system_subcomponent_m2m` | `sn_ent_ai_system_subcomponent_m2m` |

**Setup steps (high-level):**
1. Navigate to `AI Control Tower workspace > Configuration > AI connections > Add > GCP Vertex AI > Create connection`
2. Read and confirm setup instructions, create X.509 certificate using JKS file
3. Create and test connection: Connection Name, Cloud region, Service Account Email, Keystore, Keystore Password, Organization ID (optional — only if service account has org-level access)
4. Configure import schedule: activate both Discovery and Execution jobs (shipped inactive); execute Discovery first; set run frequency

---

### 3. LangGraph

**Download:** ServiceNow Store — AI Service Graph Connector for LangGraph

**Prerequisites:** Create an API key in your LangGraph/LangSmith instance (Settings > n8n API > Create API Key — same pattern; for LangGraph: Settings > API Keys).

**APIs Used by LangGraph Connector:**

| API | Endpoint | What It Does |
|---|---|---|
| List Workspaces | `https://api.smith.langchain.com/api/v1/workspaces/` | Lists all workspaces for the API key |
| List Deployments | `https://api.host.langchain.com/v2/deployments` | Lists all agent deployments per workspace |
| List Tracer Sessions | `https://api.smith.langchain.com/api/v1/sessions` | Lists all tracer sessions per workspace |
| Get Run Stats | `https://api.smith.langchain.com/api/v1/runs/stats` | Gets LLM invocation stats per run |
| Search Assistants | `{{endpoint_url}}/assistants/search` | Lists all assistants per deployment |
| Search Threads | `{{endpoint_url}}/threads/search` | Lists all threads per deployment |

**Data Mapping:**

| Data Source | Staging Table | Target Tables |
|---|---|---|
| LangGraph Agents | `sn_langgraph_integ_agents` | `alm_ai_system_digital_asset`, `alm_ai_prompt_digital_asset`, `cmdb_ci_function_ai` |
| LangGraph Usage | `sn_langgraph_integ_usage` | `alm_ai_model_digital_asset`, `sn_ai_disc_ai_usage` |

**Main target tables for LangGraph:**
- `alm_ai_system_digital_asset` — AI System digital assets
- `alm_ai_prompt_digital_asset` — AI Prompt digital assets
- `alm_ai_model_digital_asset` — AI Model digital assets
- `sn_ai_disc_ai_usage` — AI Usage/Execution data
- `cmdb_ci_function_ai` — AI Function (Agent) CI table

**Setup steps:** Navigate to AI connections > Add > LangGraph > Create connection; enter Connection Name, LangSmith API URL, LangSmith Rest API URL, API Key; optionally use MID Server; Create and test; activate both scheduled jobs (Discovery first).

---

### 4. Microsoft (Azure Foundry + Copilot Studio)

**Download:** ServiceNow Store — AI Service Graph Connector for Microsoft

**Three Azure service variants supported:**

| Variant | Resource Hierarchy |
|---|---|
| ML Services (AI Hub) | Subscriptions → Resource Groups → ML Workspaces → Agents |
| AI Services/Old Foundry (Cognitive Services) | Subscriptions → Resource Groups → Cognitive Services Accounts → Projects → Agents |
| New Foundry | Subscriptions → Resource Groups → Accounts → Projects → Agents → Agent Versions |

**Key distinction:** New Foundry treats each agent version as a distinct entity — the other two variants do not. Support for New Foundry added March 2026.

**Per-agent discovered data:**
- AI Agents (assistants) — primary entity
- AI Models — deployed models (GPT-4o, Llama, Claude, etc.) via deployment enrichment
- AI Prompts — system instructions attached to agents
- AI Tools — with type coverage varying by variant:
  - ML & AI Services: functions, connected_agent, others
  - New Foundry adds: mcp, openapi, a2a_preview
- Sub-component Relationships — M2M links between agents and sub-agents/tools
- Usage/Execution Metrics — aggregated run counts by agent, date, and session

**Azure Foundry Prerequisites:**
- OAuth credentials (refer to Azure documentation)
- 'User.Contributor' role on AI Hub (ML services) API + workspace created
- 'Azure AI User' role on Azure Foundry (Cognitive Services) API + account created
- Enable both Discovery and Execution import schedules

**Copilot Studio Prerequisites:**
- Register app in Microsoft Entra ID to obtain Client ID and Client Secret
- In Power Platform Admin Center: add app user with Basic user + System administrator roles
- Find Organization ID and Tenant ID under Settings > Session details
- Usage tracked only in non-developer environments
- OAuth authentication supported

**Azure Foundry System Properties:**

| Property | Default | Description |
|---|---|---|
| `sn_ai_msft_integ.usage_data_lookback` | 3 | Days to look back for threads before the run collection window |
| `sn_ai_msft_integ.usage_first_run_lookback_days` | 30 | Days to look back on first run (when no last success import time exists) |

**APIs Used (New Azure Foundry):**

| API | What It Does |
|---|---|
| List Projects | Lists all Azure AI Foundry projects in a resource group |
| List Deployments | Lists all model deployments within a Foundry project |
| List Agents | Lists all agents in a Foundry project |
| List Agent Versions | Lists all versions of a specific agent |
| List Conversations | Lists all conversation threads in a Foundry project |
| List Conv Items | Lists all messages within a specific conversation |

**Target tables for Azure and Copilot:**
- `alm_ai_system_digital_asset` — AI System digital assets
- `alm_ai_prompt_digital_asset` — AI Prompt digital assets
- `sn_ent_ai_tool` — AI Tools
- `sn_ent_ai_system_subcomponent_m2m` — AI System Subcomponent M2M relationships
- `sn_ai_disc_ai_usage` — AI Usage/Execution data

**Tool naming convention:** Tool names are suffixed for uniqueness: `tool-name:tenantid:resource-name:project-name`

---

### 5. n8n

**Download:** ServiceNow Store — AI Service Graph Connector for n8n

**Prerequisites:** Create an API key in your n8n instance: `Settings > n8n API > Create an API Key` (set label and expiration time). Role required in n8n: admin.

**System Properties:**

| Property | Description | Max |
|---|---|---|
| `sn_n8n_integ.list_execution_page_size` | Max items per page for execution datastream, passed as query parameter to n8n REST API | 250 (n8n limit) |
| `sn_n8n_integ.list_workflow_page_size` | Max items per page for workflow datastream | 250 (n8n limit) |

**Setup steps:** Navigate to AI connections > Add > n8n > Create connection; enter Connection Name, Connection URL, API Key; Create and test; activate both scheduled jobs (Discovery first); set run frequency.

---

### 6. Salesforce

**Download:** ServiceNow Store — AI Service Graph Connector for Salesforce

**Salesforce Data Mapping:**

**AI Agents → `alm_ai_system_digital_asset`:**

| Required Field | ServiceNow Target | Salesforce Staging |
|---|---|---|
| Agent ID | Product instance identifier | `agent_id` |
| Version | External record reference | `version_id` |
| Status | State (install_status) | `u_status` |
| Asset Type | Model Category | `asset_type` |

**AI Models → `alm_ai_model_digital_asset`:**

| Required Field | ServiceNow Target | Salesforce Staging |
|---|---|---|
| Foundation Model ID | Base model | `foundation_model_identifier` |
| Model | Model | `base_model` |
| Status | State (install_status) | `u_status` |

**AI Agents Usage → `sn_ai_disc_ai_usage`:**

| Required Field | ServiceNow Target | Salesforce Staging |
|---|---|---|
| Total Invocations | Count | `totalinvocations` |
| Conversion Definition ID | AI system | `conversationdefinitionid` |
| Time | Time | `timestamp` |

**Salesforce APIs Used:**

| API | Endpoint | Description |
|---|---|---|
| Bot Definition/BotVersion | `/services/data/v65.0/query?q=SELECT...FROM BotDefinition` | Lists all Copilot Studio bots (agents) in Dataverse |
| Configured Einstein Models | `/services/data/v65.0/ssot/machine-le...` | Lists configured Einstein AI models |
| GenAiFunctionDefinition | `/services/data/v65.0/query?q=SELECT...FROM GenAiFunctionDefinition` | Lists AI function definitions |
| GenAiPluginDefinition | `/services/data/v65.0/query?q=SELECT...FROM GenAiPluginDefinition` | Lists AI plugin definitions |
| ConversationDefinitionEventLog | `/services/data/v65.0/query?q=SELECT COUNT(Id) TotalInvocations...` | Usage/invocation counts per agent |

**Setup steps:** Navigate to AI connections > Add > Salesforce > Create connection; enter Connection Name, Connection URL, OAuth Client ID, OAuth Token URL; Create and test; activate both scheduled jobs (Discovery first).

---

## AI Connection Record Structure

Each AI connection record has three tabs:

| Tab | Contents |
|---|---|
| **Details** | Connection details of the AI connection |
| **Data sources** | Running units defining what data is fetched from the third-party system |
| **Import schedules** | Parent data import jobs for discovering AI assets and tracking usage |

---

## Common Setup Pattern Across All Connectors

1. Navigate to `AI Control Tower > Configurations > AI connections > Add`
2. Select the connector
3. Review and confirm setup prerequisites
4. Create and test connection (enter credentials/keys)
5. Configure import schedule:
   - **Activate both Discovery and Execution jobs** (all connectors ship with these inactive)
   - **Run Discovery job first** (before Execution)
   - Set run frequency
   - Optional: Execute Now for immediate first run
6. Select View all connections to verify

> **Risk Officer Note:** The most common setup error across all connectors is failing to activate and run the Discovery job first. The Execution job cannot produce usage data for assets that have not yet been discovered. Always sequence: (1) Discovery active and run, then (2) Execution active and running.

---

## Business Impact of Enterprise AI Discovery

> *"AI discovery helps organizations reduce AI deployment risks by automatically finding AI assets and simplifying compliance. This feature improves governance by showing AI deployments across different environments, helping executives make informed decisions with full transparency."*

The business case for discovery is:
- **Risk reduction** — you cannot govern what you cannot see
- **Compliance simplification** — automated cataloging reduces manual audit effort
- **Full transparency** — executives see the actual AI footprint, not just the approved inventory
- **Usage tracking** — discovery also captures usage data, enabling productivity measurement for third-party AI

---

## Key Takeaways for AI Risk & Compliance Officers

1. **Enterprise AI Discovery is your shadow AI governance mechanism** — without it, cloud-hosted AI assets (AWS Bedrock agents, Azure Foundry models, Copilot Studio bots) are invisible to AICT governance.
2. **All connectors require two ServiceNow roles**: `sn_ai_disc.discovery_admin` + `sn_cmdb_int_util.sgc_admin`.
3. **All connectors ship with Discovery and Execution jobs inactive** — you must activate them; Discovery must run before Execution.
4. **The daily data collection job must be active** — this is explicitly called out as the critical element for usage data collection.
5. **Tool name uniqueness** (Azure/Copilot): tools are suffixed with tenant/resource/project info — be aware when cross-referencing with source systems.
6. **New Foundry (Azure) treats each agent version as a distinct entity** — version-level tracking is a governance advantage but increases asset count significantly.
7. **Salesforce usage tracking** links invocations to Conversation Definition IDs — map these to agent records for risk attribution.
8. **SGC data flows through staging tables** — if assets are not appearing in AICT, check staging tables for import errors before checking the connector config.

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 779–805*
