# Tables Installed with AI Control Tower
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Role: AI Risk & Compliance Officer Reference

---

## What Is This?

This is the complete database table reference for AI Control Tower and the Evaluation dashboard. It documents every table installed with the AICT core plugin and the Evaluation framework — the tables that store all governance data, assessment records, task records, and evaluation metrics.

For a Risk & Compliance Officer, knowing the table structure is essential for: writing custom reports, building audit queries, designing integrations, troubleshooting data issues, and verifying that governance data is being stored where expected.

---

## AI Control Tower Core Tables

These tables are installed with the activation of the AI Control Tower core plugin (`sn_ai_governance`).

### AI Control Tower Details Table

This table extends the base AI asset record with AICT-specific governance fields.

| Label | Field Name | Data Type | Description |
|---|---|---|---|
| Asset | `ai_asset` | Reference | Reference to the AI asset record |
| Risk classification | `risk_score` | Choice | The risk classification value (High/Medium/Low/Unacceptable) |
| Status | `approval_status` | Choice | Current approval/governance status of the asset |

---

### AI Asset Assessment Request Table

Stores assessment request records linked to AI assets during the governance lifecycle.

| Label | Field Name | Data Type |
|---|---|---|
| Sys ID | `sys_id` | SYS_ID |
| AI asset | `asset` | Reference |
| Parent Task | `parent_task` | Reference (to `ai_gov_review_task`) |
| State | `state` | — |
| Type | `type` | Choice |
| Close Notes | `close_note` | — |

---

### AI Asset Governance Task Table

Stores the governance tasks created during lifecycle phases (Assess, Build and test, Deploy).

| Label | Field Name | Data Type |
|---|---|---|
| Sys ID | `sys_id` | SYS_ID |
| Parent Task | `parent_task` | Reference |
| Approval | `approval` | Reference (to `sysapproval`) |
| State | `state` | — |
| Type | `type` | Choice |

---

## Key AICT Tables by Function

Beyond the tables explicitly listed in the reference section, the following tables are central to AICT operations and referenced throughout the documentation:

### AI Asset Inventory Tables (Digital Asset Layer)

| Table Name | What It Stores |
|---|---|
| `alm_ai_system_digital_asset` | AI System digital asset records — the primary governance record for every AI system |
| `alm_ai_model_digital_asset` | AI Model digital asset records |
| `alm_ai_dataset_digital_asset` | AI Dataset digital asset records |
| `alm_ai_prompt_digital_asset` | AI Prompt digital asset records |

### CMDB Product Model Tables (Configuration Management Layer)

| Table Name | What It Stores |
|---|---|
| `cmdb_ai_system_product_model` | AI System product model (CMDB CI class) |
| `cmdb_ai_model_product_model` | AI Model product model |
| `cmdb_ai_dataset_product_model` | AI Dataset product model |
| `cmdb_ai_prompt_product_model` | AI Prompt product model |

### AI Governance Details Table

| Table Name | What It Stores |
|---|---|
| `sn_ai_governance_asset_governance_details` | Lifecycle phase, lifecycle status, management status per asset — the governance state record |

### AI Discovery Usage Table

| Table Name | What It Stores |
|---|---|
| `sn_ai_disc_ai_usage` | Usage and execution data for discovered AI agents (from Enterprise AI discovery) |

### AI Tools and Relationships Tables

| Table Name | What It Stores |
|---|---|
| `sn_ent_ai_tool` | AI Tool records (attributes of AI systems, not separate governed assets) |
| `sn_ent_ai_system_subcomponent_m2m` | Many-to-many relationships between AI systems and their sub-components (sub-agents, tools, use cases) |

### CMDB CI Function AI Table

| Table Name | What It Stores |
|---|---|
| `cmdb_ci_function_ai` | AI Function CI class — used by GCP Vertex AI and LangGraph connectors for function-level AI entities |

### Staging Tables for Enterprise AI Discovery

These tables are used as intermediate storage during the Service Graph Connector import process:

| Connector | Example Staging Tables |
|---|---|
| AWS Bedrock | `sn_ai_disc_aws_sgc_bedrock_ai_system`, `sn_ai_disc_aws_sgc_bedrock_ai_model`, `sn_ai_disc_aws_sgc_bedrock_ai_tool`, `sn_ai_disc_aws_sgc_bedrock_ai_usage` |
| AWS AgentCore | `sn_ai_disc_aws_sgc_agentcore_ai_system`, `sn_ai_disc_aws_sgc_agentcore_ai_tool` |
| AWS SageMaker | `sn_ai_disc_aws_sgc_sg_awssagemaker_model` |
| GCP Vertex AI | `sn_ai_disc_gcp_sgc_sg_gcp_ai_system`, `sn_ai_disc_gcp_sgc_sg_gcp_ai_model`, `sn_ai_disc_gcp_sgc_sg_gcp_ai_tool` |
| LangGraph | `sn_langgraph_integ_agents`, `sn_langgraph_integ_usage` |

---

## Evaluation Dashboard Tables

These tables are installed with the Evaluation framework for the Virtual Agent / Now Assist evaluation capability.

### Core Evaluation Tables

| Label | Table Name | Description |
|---|---|---|
| Evaluation | `sn_na_conv_eval_evaluation` | Primary evaluation records — one per evaluated conversation |
| Evaluation configurations | `sn_na_conv_eval_evaluation_configurations` | Configuration settings for the evaluation framework |
| Evaluation Metrics | `sn_na_conv_eval_evaluation_metrics` | Individual metric scores per evaluation (Intent Accuracy, Slot Filling, etc.) |
| Evaluation Set | `sn_na_conv_eval_evaluation_set` | Batch evaluation sets — used for Execute Batch Evaluation flow |
| Evaluation Value Aggregates | `sn_na_conv_eval_evaluation_value_aggregates` | Aggregated value calculations (time savings, efficiency %) by chat size category |

### Remote Tables (Calculation Tables)

Remote tables are not physical storage tables — they define remote queries whose results are computed on demand:

| Table Name | What It Calculates |
|---|---|
| `sn_na_conv_eval_st_value_calcs` (Conversation Evaluator Value Calculations) | For a given query: time savings and efficiency % for small, medium, and large chats; also returns time savings when a Knowledge article or catalog item was invoked |
| `sn_na_conv_eval_weekly_cals` (Conversation weekly calculations) | Same calculations as above but broken down by week of the selected date range — supports the weekly efficiency trend charts |

### Evaluation Scheduled Jobs

| Job Name | Schedule | Description |
|---|---|---|
| **CE Populate Value Aggregates Chats – Daily** | Daily | Randomly selects 1,000 conversations from yesterday. Extracts chat duration and classifies as small/medium/large. Classifies conversations where a Knowledge article or catalog item was invoked. For evaluated chats, populates data into the Evaluation Value Aggregates table |
| **Evaluation Value Calculation – Runs Only Once After Install** | Once | Deletes all records in Evaluation Value Aggregates, runs calculations again, stores aggregated values from the first evaluation date onward |

### Evaluation System Properties

| Property | Default | Description |
|---|---|---|
| `sn_na_conv_eval.errorBandMinRecords` | 30 | Minimum number of records required to calculate the error band for upper/lower deviation |
| `sn_na_conv_eval.evalWeights` | — | Weights for each evaluation metric used in computing composite/total scores |
| `sn_na_conv_eval.maxEvaluateCount` | 200 | Maximum number of records to evaluate per day |
| `sn_na_conv_eval.total_sampled_conv_count` | 1,000 | Total number of conversations that can be sampled for value calculations |
| `sn_na_conv_eval.value_chat_classifier` | 4, 10 | Defines small/medium/large conversation boundaries based on inbound message count: ≤4 = small; 5–10 = medium; >10 = large |
| `sn_na_conv_eval.ce_value_calculation_weights` | — | Value calculation weight values for each type of evaluated chat |
| `sn_na_conv_eval.eval_value_rerun_status` | — | Status of the Conversation Evaluator Value Rerun; changes to false after the post-install run completes |

> **Risk Officer Note on Conversation Size Classification:** The `value_chat_classifier` property (default: 4, 10) determines how conversations are classified for value calculations. Small conversations (≤4 inbound messages) contribute little to no savings because they are too brief to represent meaningful AI-assisted work. The time savings calculation only counts quality interactions as delivering value. Understand these thresholds when reviewing Value dashboard data — a sudden drop in reported value may reflect a change in conversation complexity (more short conversations), not a drop in AI performance.

### Evaluation Business Rules

| Rule Name | Trigger | Conditions | Purpose |
|---|---|---|---|
| Add info message for Evaluation set | After insert/update | State changes to In Progress; evaluation_type = conversation | Adds informational message to evaluation set |
| Scale Up labeling metric | Before insert/update | metric_type = Labeling; metric_name includes 'hel...' | Scales up labeling metric scores |
| updateLabelingScoresOnEvaluation | After insert/update | metric_type = Labeling; raw_score value changes | Updates labeling scores on evaluation records |
| Update deviation scores | Before insert/update | metric_type = LLM Generated; score value changes | Updates deviation scores when LLM scores change |
| getAutoEvalCompositeScore | After update | State changes to Complete; total_score in... | Calculates composite auto-evaluation score on completion |

### Evaluation Flows

| Flow Name | Description | Default State |
|---|---|---|
| **Execute Evaluation** | Performs evaluations when conversations are completed. Trigger: Conversation table state = Complete | **Deactivated by default** — use nightly scheduled job instead |
| **Execute Batch Evaluation** | Performs batch evaluations of up to 100 completed virtual agent conversations. Trigger: Evaluation set created/updated with Evaluation Type = Conversation | Available for manual batch runs |

> **Risk Officer Note:** The Execute Evaluation flow is deactivated by default because activating it means every conversation completion triggers an evaluation in real-time — this can create performance load. Instead, the nightly scheduled job "Execute Evaluations" evaluates chats in batch. If you need real-time evaluation data, activate the flow, but test the performance impact in a non-production environment first.

### Evaluation Flow Actions

| Action | Description |
|---|---|
| **Randomize conversations** | Performs randomization and returns 100 conversations randomly from a given query |
| **invokeApiDefinition** | Invokes OneExtend Capability in the LLM — the core skill invocation action |
| **Chat Classifier Eval** | Returns title, category, and whether evaluation should be executed |
| **buildTranscript** | Builds the full conversation transcript with proper tagging |
| **evalExecuteCondition** | Checks if the transcript is good enough to be evaluated |

### Evaluation Script Includes

| Script Include | Description |
|---|---|
| `evalExecuteCondition` | Use this script include to update the evaluation condition |
| `evalUtils` | Primary utility function for the Evaluator |

---

## Table Usage Guide for Governance Reporting

For common governance reporting needs, here are the key tables to query:

| Governance Report Needed | Primary Table(s) |
|---|---|
| All managed AI systems with risk classification | `alm_ai_system_digital_asset` joined with `sn_ai_governance_asset_governance_details` |
| Lifecycle status of all assets | `sn_ai_governance_asset_governance_details` |
| Open governance tasks by asset | AI asset governance task table |
| Assessment requests by asset | AI asset assessment request table |
| AI usage data from discovery | `sn_ai_disc_ai_usage` |
| AI tools linked to agents | `sn_ent_ai_tool` + `sn_ent_ai_system_subcomponent_m2m` |
| Evaluation scores by conversation | `sn_na_conv_eval_evaluation` + `sn_na_conv_eval_evaluation_metrics` |
| Conversation value aggregates | `sn_na_conv_eval_evaluation_value_aggregates` |

---

## Key Takeaways for AI Risk & Compliance Officers

1. **`alm_ai_system_digital_asset` is the primary AI asset table** — every governed AI system has a record here; this is the foundation for all governance reporting.
2. **`sn_ai_governance_asset_governance_details` holds lifecycle state** — query this for current lifecycle phase and status of all assets.
3. **Staging tables are temporary** — Enterprise AI discovery data flows through staging tables to target tables; query target tables for final, transformed data.
4. **The Evaluation daily job samples 1,000 conversations** — evaluation metrics are not from 100% of conversations; understand the sampling for accurate interpretation.
5. **Execute Evaluation flow is OFF by default** — if evaluation data is stale or missing, check whether the nightly job is active; activating the real-time flow has performance implications.
6. **Conversation size thresholds affect value calculations** — the 4/10 inbound message classifier determines whether a conversation contributes to value metrics; conversations below the small threshold contribute minimally.
7. **`sn_na_conv_eval.errorBandMinRecords = 30`** — adjusted scores (which correct for human-AI score differences) require at least 30 human-labeled records per metric; below this, raw auto-eval scores are used.

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 868–874*
