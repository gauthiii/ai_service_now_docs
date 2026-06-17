# Domain separation and Now Assist AI Agent Studio

_Source pages: 244–245 | Depth: 2_

---

<!-- page 244 -->
Tables used for configuring AI agents (continued)
Table Description
If two large language model (LLM) calls are
made to the sn_aia_execution_task, then the
sn_aia_gen_ai_m2m table has two records.
Report metrics [sn_aia_report_metric] List of the report metrics.
Agent Access Role Configurations List of agent access roles. You can also create
[sys_agent_access_role_configuration] agent access roles from this table.
generative AI Configurations Record that points to the actual model.
[sys_generative_ai_config]
Invocation Sources Functions as a registry of entry points and
[sn_aia_invocation_source] helps track and define the different contexts
or surfaces from which an AI agent can be
invoked or triggered.
Tables used for Group Action Framework
See Group Action Framework for more information.
Table Description
GAF record group [sn_gaf_record_group] Stores the output of the grouping skill. Each
record represents a cluster of related records.
You can open each record group record to
discover which records were included within
the cluster.
GAF record group detail Contains the individual records that belong
[sn_gaf_record_group_detail] to each group GAF record group. You can
also find if a record is marked to act as a
representative of the cluster on these records.
GAF action strategy result Holds the results of the Action Strategy skill,
[sn_gaf_action_strategy_result] which selects representative records from
each group for downstream processing.
GAF action mapper results Stores the output of the Mapper skill, which
[sn_gaf_action_mapper_result] maps new records to existing clusters.
GAF action reducer results Stores the result of the Action Reducer skill.
[sn_gaf_action_reducer_result] The results include insights for entire clusters.
For example, how to resolve incidents similar
to those gathered in a cluster.
Domain separation and Now Assist AI Agent Studio
Domain separation is supported for Now AssistAI Agent Studio. Domain separation enables you
to separate data, processes, and administrative tasks into logical groupings called domains. You
can control several aspects of this separation, including which users can see and access data.

<!-- page 245 -->
Domain Separation Overview
Now Assist AI agents use basic domain separation capabilities to help protect your users' data.
Domain separation support for AI agents is applied at design time and run time.
Design-time support
Refers to creating or updating agentic workflows, agents, tools, trigger
configurations, and so on. AI agent configurations can be made domain-specific
for individual agents and the actual agentic workflows. Administrators can apply
specific domains to those records. Similar to other basic domain separations,
records in the AI agents tables are accessible if the user belongs to the same or a
higher domain than those records.
Run-time support
Refers to the agentic conversation on the Now Assist panel, web client, or any
conversational channel. In the agentic conversations, the user that the agent
impersonates functions as an agent with any AI agents who initiate the conversation
on demand. For example, if the conversation is happening via a trigger mentioned
on the Run as field on the Trigger form of an agentic workflow. If the user that the
agent impersonates belongs to the same or a higher domain, that agent can access
and use configurations that are associated with that domain.
The domain visibility for an agentic workflow is resolved during run time based
on the Run as attribute in the agentic workflow trigger condition. For more
information, see defining a trigger for an agentic workflow.
When an agentic conversation is triggered on demand, the domain visibility is applied to the
particular agent in action. When an agentic conversation is initiated through a trigger, the domain
visibility is applied to the user who resolves the caller (in an incident record where the Run as
attribute is set to Caller), when the conversation runs against the incident record.
Note: The sys_domain field is added to all AI agent tables to achieve domain separation
in Now Assist AI agents. The sys_domain_path, which is available for domain separation, is
enabled on your instance.
To understand more about the ServiceNow domain separation, see Exploring domain
separation .
How domain separation works in Now Assist AI Agent Studio
Process separation is enabled through the use of the sys_overrides column in domain-aware
tables. Any table that contains both the sys_domain and the sys_overrides fields can be
configured to have different processes from the parent domain.
AI Agents support only configuration tables to be process separated. Below are the list of tables
that are process separated:
•sn_aia_agent_config
•sn_aia_usecase_config_override
Domain separation in Now Assist AI agents supports:
•Agentic workflow discovery.
•AI agent and its tools can be active in the X domain and inactive in the Y domain.
•Memory category can be active in the X domain and inactive in the Y domain.