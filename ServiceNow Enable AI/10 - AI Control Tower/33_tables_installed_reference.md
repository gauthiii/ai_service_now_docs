# Tables Installed with AI Control Tower — Reference
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Topic 33 of 35 | Role: AI Risk & Compliance Officer Reference

---

## What Is This?

This is the complete, standalone database table reference for AI Control Tower and the Evaluation dashboard — every table installed by the AICT core plugin and the Evaluation framework, with field names, data types, and governance usage context.

For broader governance reporting guidance and table usage examples, see Topic 29 (Tables Installed with AI Control Tower). This document is the pure technical reference.

---

## AI Control Tower Core Tables

Installed with: `sn_ai_governance` (AI Control Tower Core)

### Table: AI Control Tower Details

| Field Label | Field Name | Type |
|---|---|---|
| Asset | `ai_asset` | Reference |
| Risk classification | `risk_score` | Choice |
| Status | `approval_status` | Choice |

---

### Table: AI Asset Assessment Request

| Field Label | Field Name | Type |
|---|---|---|
| Sys ID | `sys_id` | SYS_ID |
| AI asset | `asset` | Reference |
| Parent Task | `parent_task` | Reference (`ai_gov_review_task`) |
| State | `state` | — |
| Type | `type` | Choice |
| Close Notes | `close_note` | — |

---

### Table: AI Asset Governance Task

| Field Label | Field Name | Type |
|---|---|---|
| Sys ID | `sys_id` | SYS_ID |
| Parent Task | `parent_task` | Reference |
| Approval | `approval` | Reference (`sysapproval`) |
| State | `state` | — |
| Type | `type` | Choice |

---

## AI Asset Inventory Tables

### Digital Asset Tables (Governance Layer)

| Table Name | Asset Type |
|---|---|
| `alm_ai_system_digital_asset` | AI System — primary governance record |
| `alm_ai_model_digital_asset` | AI Model governance record |
| `alm_ai_dataset_digital_asset` | AI Dataset governance record |
| `alm_ai_prompt_digital_asset` | AI Prompt governance record |

### CMDB Product Model Tables (Configuration Layer)

| Table Name | Asset Type |
|---|---|
| `cmdb_ai_system_product_model` | AI System CMDB CI |
| `cmdb_ai_model_product_model` | AI Model CMDB CI |
| `cmdb_ai_dataset_product_model` | AI Dataset CMDB CI |
| `cmdb_ai_prompt_product_model` | AI Prompt CMDB CI |

### AI Governance State Table

| Table Name | What It Stores |
|---|---|
| `sn_ai_governance_asset_governance_details` | Lifecycle phase, lifecycle status, management status (Managed/Unmanaged) per asset |

### AI Tools and Relationships

| Table Name | What It Stores |
|---|---|
| `sn_ent_ai_tool` | AI Tool records (attributes of AI systems) |
| `sn_ent_ai_system_subcomponent_m2m` | M2M relationships: agent↔tool, agent↔sub-agent, usecase↔agent |

### AI Discovery

| Table Name | What It Stores |
|---|---|
| `sn_ai_disc_ai_usage` | Usage and execution data for discovered AI agents |
| `cmdb_ci_function_ai` | AI Function CI class (used by GCP and LangGraph connectors) |

### Source Tables (Now Assist Sync Sources)

| Table Name | Syncs To |
|---|---|
| `sn_nowassist_skill_config` | `alm_ai_system_digital_asset` (AI Systems) |
| `sys_generative_ai_model_config` | `alm_ai_model_digital_asset` (AI Models) |
| `sys_one_extend_test_dataset` | `alm_ai_dataset_digital_asset` (AI Datasets) |
| `sys_generative_ai_config` | `alm_ai_prompt_digital_asset` (AI Prompts) |
| `sn_aia_agent` | `alm_ai_system_digital_asset` (AI Agents) |
| `sn_aia_tool` | `sn_ent_ai_tool` (AI Tools) |
| `sn_aia_agent_tool_m2m` | `sn_ent_ai_system_subcomponent_m2m` (Agent-Tool relationships) |
| `sn_aia_usecase` | `alm_ai_system_digital_asset` (AI Use Cases) |
| `sn_aia_team_member` | `sn_ent_ai_system_subcomponent_m2m` (Usecase-Agent relationships) |

---

## Enterprise AI Discovery Staging Tables

Staging tables are intermediate tables used during SGC import. Query the target tables above for final data.

### AWS Staging Tables

| Staging Table | Target |
|---|---|
| `sn_ai_disc_aws_sgc_bedrock_ai_asset` | Routes to other staging tables |
| `sn_ai_disc_aws_sgc_bedrock_ai_system` | `alm_ai_system_digital_asset` |
| `sn_ai_disc_aws_sgc_bedrock_ai_model` | `alm_ai_model_digital_asset` |
| `sn_ai_disc_aws_sgc_bedrock_ai_tool` | `sn_ent_ai_tool` |
| `sn_ai_disc_aws_sgc_bedrock_ai_prompt` | `alm_ai_prompt_digital_asset` |
| `sn_ai_disc_aws_sgc_bedrock_sbcomp_m2m` | `sn_ent_ai_system_subcomponent_m2m` |
| `sn_ai_disc_aws_sgc_bedrock_ai_usage` | `sn_ai_disc_ai_usage` |
| `sn_ai_disc_aws_sgc_agentcore_ai_system` | `alm_ai_system_digital_asset` |
| `sn_ai_disc_aws_sgc_agentcore_ai_tool` | `sn_ent_ai_tool` |
| `sn_ai_disc_aws_sgc_agentcore_ai_usage` | `sn_ai_disc_ai_usage` |
| `sn_ai_disc_aws_sgc_sg_awssagemaker_model` | `alm_ai_model_digital_asset` |

### GCP Staging Tables

| Staging Table | Target |
|---|---|
| `sn_ai_disc_gcp_sgc_sg_gcp_execution` | `sn_ai_disc_ai_usage` |
| `sn_ai_disc_gcp_sgc_sg_gcp_ai_system` | `alm_ai_system_digital_asset`, `cmdb_ci_function_ai` |
| `sn_ai_disc_gcp_sgc_sg_gcp_ai_model` | `alm_ai_model_digital_asset` |
| `sn_ai_disc_gcp_sgc_sg_gcp_ai_tool` | `sn_ent_ai_tool` |
| `sn_ai_disc_gcp_sgc_sg_gcp_ai_prompt` | `alm_ai_prompt_digital_asset` |
| `sn_ai_disc_gcp_sgc_sg_gcp_ai_system_subcomponent_m2m` | `sn_ent_ai_system_subcomponent_m2m` |

### LangGraph Staging Tables

| Staging Table | Target |
|---|---|
| `sn_langgraph_integ_agents` | `alm_ai_system_digital_asset`, `alm_ai_prompt_digital_asset`, `cmdb_ci_function_ai` |
| `sn_langgraph_integ_usage` | `alm_ai_model_digital_asset`, `sn_ai_disc_ai_usage` |

---

## Evaluation Dashboard Tables

Installed with the Evaluation framework.

### Core Tables

| Label | Table Name | Description |
|---|---|---|
| Evaluation | `sn_na_conv_eval_evaluation` | One record per evaluated conversation |
| Evaluation configurations | `sn_na_conv_eval_evaluation_configurations` | Framework configuration settings |
| Evaluation Metrics | `sn_na_conv_eval_evaluation_metrics` | Individual metric scores per evaluation |
| Evaluation Set | `sn_na_conv_eval_evaluation_set` | Batch evaluation sets |
| Evaluation Value Aggregates | `sn_na_conv_eval_evaluation_value_aggregates` | Aggregated value calculations by chat size |

### Remote Tables (Computed, Not Physical)

| Table Name | Computes |
|---|---|
| `sn_na_conv_eval_st_value_calcs` | Time savings and efficiency % for small/medium/large chats; Knowledge article and catalog item invocation value |
| `sn_na_conv_eval_weekly_cals` | Same calculations broken down by week of the selected date range |

### Conversation Source Table

| Table Name | Role |
|---|---|
| `sys_cs_conversation` | Source of all virtual agent conversations — trigger source for Execute Evaluation flow |
| `sys_cs_message` | Individual messages within conversations — used by buildTranscript |

---

## Governance Reporting Quick Reference

| Report Needed | Primary Table | Join / Filter |
|---|---|---|
| All managed AI systems with risk classification | `alm_ai_system_digital_asset` | Join `sn_ai_governance_asset_governance_details` on asset sys_id |
| Current lifecycle status of all assets | `sn_ai_governance_asset_governance_details` | Filter by management_status = Managed |
| Open governance tasks by asset | AI asset governance task table | Filter state != Completed |
| Completed assessments by asset | AI asset assessment request table | Filter state = Completed |
| AI agent usage from discovery | `sn_ai_disc_ai_usage` | — |
| Tools linked to each agent | `sn_ent_ai_tool` + `sn_ent_ai_system_subcomponent_m2m` | Join on agent sys_id |
| Evaluation scores by conversation | `sn_na_conv_eval_evaluation` + `sn_na_conv_eval_evaluation_metrics` | Join on evaluation sys_id |
| Weekly value aggregates | `sn_na_conv_eval_weekly_cals` | Remote table — query with date range |

---

## Key Takeaways for AI Risk & Compliance Officers

1. **`alm_ai_system_digital_asset` is your primary governance table** — every governed AI system record lives here
2. **`sn_ai_governance_asset_governance_details` holds lifecycle state** — this is where Managed/Unmanaged and lifecycle phase are stored
3. **Staging tables are temporary transit** — query target tables, not staging tables, for authoritative data
4. **`sn_ent_ai_system_subcomponent_m2m` is the dependency chain** — empty M2M records mean broken traceability
5. **`sn_na_conv_eval_evaluation` + `sn_na_conv_eval_evaluation_metrics`** — the two tables you need for evaluation quality reporting
6. **Remote tables (`st_value_calcs`, `weekly_cals`) are computed on demand** — they do not store data permanently; query them with a date range filter

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 868–874*
