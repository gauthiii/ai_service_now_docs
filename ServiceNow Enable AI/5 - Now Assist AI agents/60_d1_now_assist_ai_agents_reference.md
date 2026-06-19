# Now Assist AI agents reference

_Source pages: 233–262 | Depth: 1_

---

<!-- page 233 -->
Before you begin
Role required: none
Procedure
1.Navigate to All > Incidents > Assigned to you and open an incident that you would like to
resolve.
When you open an incident, the Now Assist application checks if a plan is available by using
AI agents and displays the Now Assist has a plan for solving INCXXXXXXX.
Open Now Assist Panel to view the plan. message in a banner.
Note: You can select the banner and directly go to the conversation on the Now Assist
panel to complete the task.
2. Open the Now Assist panel by using the Now Assist icon.
Now Assist provides the resolution steps for the incident.
3. On the Now Assist panel, enter Yes.
When the live agent enters Yes, they can proceed with the execution plan that is proposed by
the Now Assist AI agents. The live agent checks the conversation and adds further inputs, if
needed, to resolve the incident.
Review and update tickets with the Ticket Status AI agent
Review the status of your tickets and take standard ticket actions, such as adding comments,
using the Ticket Status AI agent in Now Assist in Virtual Agent.
Before you begin
Role required: By default, any authenticated user with access to the portal the Ticket Status AI
agent is enabled for can access the AI agent. There may be additional roles required depending
on the configuration by your administrator.
Procedure
1.Navigate to your Service Portal and open Virtual Agent to start a new conversation.
Depending on the configuration, you may also be able to access this AI agent in the Now Assist
panel or Microsoft Teams with myBot.
2. Enter one of the following utterances:
◦Can you list all open tickets I've created?
◦What's the current status of my incident INC001?
◦Add comment to INC001 "I need your help in fixing this request ASAP. Please prioritize this."
◦Can you check the latest progress on my most recent request?
3. Answer any follow-up questions.
Result
The Ticket Status AI agent used various tools to check and update your tickets.
Now Assist AI agents reference
Find more information about user roles, tables, and the different properties that are installed in
Now Assist AI agents.

<!-- page 234 -->
Now Assist AI agents roles
The following roles are installed with Now Assist AI agents with a compatible Now Assist
application.
Roles required to configure or monitor AI agents
Role Description
AI Agent admin [sn_aia.admin] Administrator of the application. A user with
the sn_aia_admin role can create, read,
update, and delete records.
AI Agent Viewer [sn_aia.viewer] Read-only access to the application. A user
with the sn_aia_viewer role has read and
report access on all tables.
agent_role_config_admin With this role, user can access and modify
Agent role configurations with AI Agent admin
[sn_aia_admin] being the parent role.
agent_role_config_viewer Can view the Agent role configurations with AI
Agent Viewer [sn_aia_viewer] being the parent
role.
Note: The roles can be assigned manually through the user record directly. For the
assigned roles to take effect, logout and login back to the application.
Now Assist AI agents system properties
The following are system properties that define default values and behavior.
System properties to use for configuring AI agents
Property Description
glide.ai_record_activity.validation.feature.enabledEnables UI validation for agentic AI and skills
at the instance level. If this feature is enabled,
then any UI validation, such as required
fields, must be met before the AI process is
completed.
The following properties are context-specific
gates that determine where validation is done
when the feature is enabled:
•glide.ai_record_activity.ai_detection.nap.enabled:
Now Assist panel executions
•glide.ai_record_activity.ai_detection.skill.enabled:
Now Assist skill execution with UI actions or
in Virtual Agent
•glide.ai_record_activity.ai_agent.validation.enabled:
agentic AI-initiated record updates with UI
actions or in Virtual Agent
If you want to enable these gates of the UI
validation feature, you must create the system

<!-- page 235 -->
System properties to use for configuring AI agents (continued)
Property Description
property and set the value to true. You don't
need to enable this feature for individual skills
or agentic AI assets.
sn_aia.agent_llm_provider Defines the (large language model) LLM
service provider for AI agents.
Default value: azure_openai.
sn_aia.agent_tool_supported_data_types Defines a comma-separated list of supported
data types for tools that are used by agents
for IntegrationHub spoke. Each value
corresponds to the name field of records in
the Field classes table [sys_glide_object].
sn_aia.analytics_dashboard_sysid Provides the sys_id for the AI Agents Analytics
dashboard.
read_roles: sn_aia.admin and sn_aia.viewer
sn_aia.continuous_communicator_output_limit Defines the maximum number of continuous
outputs that the AI Agent Orchestrator can
trigger to show to users.
Default value: 3
sn_aia.continuous_tool_execution_limit Defines the maximum consecutive number of
uses for the same tool.
Default value: 7
sn_aia.enable_usecase_tool_execution_mode_oEvenrarbidlees running agentic workflows fully
autonomously, overriding any non-automated
tools in the agentic workflow.
Default value: false
sn_aia.ltm.category.auto_create Enables AI-generated categories if no
matching categories exist.
Default value: false
sn_aia.ltm.enable_long_term_memory Enables long-term memory for AI agents. All
previous user interactions are used as context
for the LLM.
Default value: false
sn_aia.maximum_agent_tools Defines the maximum number of tools that can
be assigned to an AI agent.
Default value: 20
sn_aia.max_scheduled_trigger_query Defines how many records are processed
when a scheduled trigger is detected.

<!-- page 236 -->
System properties to use for configuring AI agents (continued)
Property Description
Default value: 10
Write_role: admin
sn_aia.mid_skill_switch_enabled Enables mid-skill switching.
Default value: false
sn_aia.react_failure_retry_max_limit Defines the maximum number of retries in
case of an execution failure.
Default value: 3
sn_nowassist_va.router_redirect_va_agentic Determines AI agent discovery in Virtual
Agent. If set to NEVER, Virtual Agent continues
Q&A without any agentic AI.
Default: ROUTER_DECISION
com.glide.cs.dynamic.capability.timeout Defines the Timeout for AIA Proficiency
Descriptor.
Default value: 180.
Write_role: admin.
sn_aia.enable_follow_up Enables users to continue the conversation
with follow-ups after the agentic workflow
execution is complete.
Default value: true.
sn_aia.follow_up_message Defines a follow-up message sent after
execution is completed.
Default Value: How otherwise can I help you?
sn_aia.allow_context_sharing Enables the sharing of short-term memory,
allowing context to persist across execution
within the same conversation.
Default Value: true
sn_aia.agent_strategy_choice_enabled Enables to show the LLM reasoning strategy in
the agent setup screen.
Default Value: false
sn_aia.context_sharing_strategy This property defines the strategy to use for
storing short-term memory for an execution.
Default Value: summarise
sn_aia.enable_agent_tool_input_value_overridesEnables you to override the agent tool
description.

<!-- page 237 -->
System properties to use for configuring AI agents (continued)
Property Description
Default Value: true.
sn_aia.follow_up_qna_failure_limit Defines the limit to exit execution if the
number of consecutive questions and
answers aren’t available in the follow-up.
Default value: 1.
sn_aia.ltm.use_memory_for_ai_agent Enables long-term memory for AI agent
interactions. When enabled, stored user
memories are utilized in AI agent interactions.
Default value: true.
sn_aia.quick_mode_failure_retry_max_limit Defines maximum limit for retries in case of a
failure in Quick Mode execution.
Default value: 3.
sn_aia.user_context_data Defines a comma-separated list of user
context data to be used with AI Agents.
The list is used to pick the data available from
knowledge graph API: getUserContext.
List of available user information:
•profile
•manager
•reportees
•assets
The user information can also be customized
by overriding the method getUserContext
via UserContextUtil.
If customized, the property must define the
comma separated list of keys generated by the
customized getUserContext method.
Default value: profile.
sn_aia.external_agents.enabled
Set to true to enable external agent features
sn_aia.external_agents.parallel_conversations.enabled
Enables or disables multiple simultaneous
conversations per user
sn_mcp_client.cursor.max_iterations
Specifies the maximum number of cursor-
based pagination iterations to perform when

<!-- page 238 -->
System properties to use for configuring AI agents (continued)
Property Description
fetching MCP tools. Helps prevent excessive
looping or API calls during data retrieval.
Note: Set this value to 0 to disable
pagination iteration limits.
mcp_guardian_check Enables guardian check for MCP Client when
the value is set to true.
The default value is false.
Note: To enable guardian check for
MCP Client, verify that you enable Now
Assist guardian on AI Agent Studio >
Settings page.
com.glide.agentic_processes_view.enabled Enables the in-product experience for agentic
workflows in the AI Workflows panel. Verify
that this is set to true if you plan on using UI
actions to run agentic workflows.
sys_generative_ai_prompt_config References a config record via the generative
AI Config field.
Global properties used for episodic memory or agent learning
System property Description
sn_aia.enable_episodic_memory Enables episodic memory. When enabled,
episodic memories from past interactions are
collected and stored in sn_aia_memory and
utilized in future interactions to enhance the
overall experience
Default value: true.
.
sn_aia.enable_memory_limit Maximum number of episodic memories to
inject into prompt when an agent is invoked.
Note: The maximum number of values
allowed is less than or equal to 5.
sn_aia.use_episodic_memory_for_ai_agent Enables episodic memory injection for AI
agent interactions. When enabled, stored user
memories are utilized in AI agent interactions.
Default value: true.
Properties on the Agent Properties table
The following properties are on the Agent Properties [sn_aia_property] table. These properties
affect different AI agent behaviors.

<!-- page 239 -->
General properties on the Agent Properties table
Name Description Default value
alert.assist_spike_hours_to_check Time 3
interval,
in hours,
between
running the
scheduled
job that
checks for
spikes in
assist usage
alert.assist_spike_usage_percentage_threshold Percentage 0.5 (50%)
increase
required
from
previous
job results
to trigger
the spike in
assist usage
notification
alert.assist_spike_usage_threshold Minimum 5000
number of
assists to
trigger the
spike in
assist usage
notification
alert.consecutive_error_count Consecutive 3
number
of latency
errors to
trigger the
latency
notification
alert.llm_latency_threshold Time taken, 10
in seconds,
for the LLM
to respond
before
sending a
latency error
alert.tool_latency_threshold Time taken, 300
in seconds,
for a tool
to finish
executing
before

<!-- page 240 -->
General properties on the Agent Properties table (continued)
Name Description Default value
sending a
latency error
enable_agent_tool_input_value_overrides Determines false
whether tool
input values
can be
overriden
by the AI
agent or
other tools
for use by
another tool
execution_task.latency_thresholds Determines
{
thresholds
"llm": {
on LLM
and tool
"timeBoundaries": [
execution
5000,
times and
10000
response
],
tokens/
"tokenLimit":
character
counts for
},
tool calling
"tool": {
"timeBoundaries": [
200000,
300000
],
"outputCharLimit":
10000
}
}
follow_up_behaviour Actions no_followup_close_conversation
to take by
the agentic
workflow
after it has
finished
executing.
Each record
applies to
only one
agentic
workflow.
mcp_guardian_check Determines false
whether
Now Assist

<!-- page 241 -->
General properties on the Agent Properties table (continued)
Name Description Default value
Guardian
runs on
MCP tool
executions
show_citations Determines false
whether
agentic AI-
generated
responses
in Now
Assist
panel or
Now Assist
in Virtual
Agent add
citations for
their output
kill_switch.mode Controls warn_only
how the
feature Other values include:
responds to
•off
a detected
•enforce
breach
kill_switch.consecutive_windows_duration The total 4320
look back
span.
kill_switch.max_fires_per_window Fires per 5
record that
mark it as
breaching.
kill_switch.min_distinct_records Breaching 25
records
needed for
the window
to count as
runaway.
kill_switch.window_size Length 1440
of one
observation
window.
The following properties are used to detect and avoid infinite recursion or execution loops. If
you reach the max executions that match the query within the time window, any new executions
matching the query will abort. You can adjust these values if you want to lower the threshold for
detecting recursion.

<!-- page 242 -->
Recursive check properties on the Agent Properties table
recursive_check.create_max_executions Maximum 50
number of
matching
executions
creating
records
recursive_check.create_time_window Time 15
window, in
minutes,
for
checking
for
matching
executions
creating
records
recursive_check.query_for_create_record Query objective={objective}^agent={agent}^ORusecase={usecase}
for the
fields of
execution
plans to
create
records to
check if
executions
are
repeating
recursive_check.query_for_update_record Query related_task_record={related_task_record}^objective={objective}^agent={agent}^ORusecase={usecase}
for the
fields of
execution
plans to
update
records to
check if
executions
are
repeating
recursive_check.update_max_executions Maximum 5
number of
matching
executions
updating a
record
recursive_check.update_time_window 15
Time
window, in
minutes,
for
checking

<!-- page 243 -->
Recursive check properties on the Agent Properties table
(continued)
for
matching
execution
updates
Now Assist AI agents tables installed
The following tables are installed so Now Assist AI agents works as expected:
Tables used for configuring AI agents
Table Description
Agentic workflows [sn_aia_usecase] List of configured agentic workflows.
AI Agents [sn_aia_agent] List of configured AI agents.
Tools [sn_aia_tool] List of tools used by an AI agent.
Strategies [sn_aia_strategy] List of strategies used by an AI agent.
Teams [sn_aia_team] Team that is a group of listed agents.
Team members [sn_aia_team_member] List of teams mapped to an agent.
Agent Tools [sn_aia_agent_tool_m2m] List of tools mapped to an AI agent.
AIA Trigger Configurations List of triggers created for an agentic workflow.
[sn_aia_trigger_configuration]
Execution Tasks [sn_aia_execution_task] List of tasks by execution plan ID.
Messages [/sn_aia_message] List of messages recorded in AI agent
conversations to and from the human users.
Tools Executions [sn_aia_tools_execution] List of tools executed by the plan ID.
Note: The records in the Tools
Executions table expire and is set to
unavailable after a period of 13 months.
Execution Plans [sn_aia_execution_plan] List of plan executions by conversation ID.
Agent Tools [sn_aia_agent_tool_m2m] List of tools and maximum automatic
executions.
AI Agent configs [sn_aia_agent_config] List of active AI agents configured for the
proficiency that they’ll be used in.
Agent properties [sn_aia_property] Various properties that affect AI agent
behavior.
Gen AI Metadata M2M [sn_aia_gen_ai_m2m] List of Gen AI metadata and the maximum
automatic executions.Maintains the mapping
between sn_aia_execution_task and Gen AI
log metadata.

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

<!-- page 246 -->
•sn_aia_property can be overridden in a different domain.
•Triggers can be overridden in different domain.
Note: AI agent and agentic workflow details can’t be overridden in the different domains.
Related topics
Domain separation for service providers
AI Agent Analytics dashboard
Track the AI agent use and efficiency gain on your instance through the AI Agent Analytics
dashboard. The dashboard can reveal trends in how AI agents are used to improve the time to
resolution and the number of tasks closed.
Required ServiceNow AI Platform roles
To use the AI Agent Analytics dashboard, you must have either the sn_aia.viewer or the
sn_aia.admin role.
If you want to change the dashboard, you must duplicate it and apply changes to the copy.
You can redirect the Analytics page in AI Agent Studio to the new dashboard by replacing the
dashboard sys_id in the system property sn_aia.analytics_dashboard_sysid.
Accessing the AI Agent Analytics dashboard
To open the dashboard, navigate to All > AI Agent Studio > Analytics.
You can also access the dashboard from the AI Agent Studio overview page. Go to the Recent
agentic workflows and AI agents activity section and select the View analytics link.
Indicators
Most indicators are updated daily. The latency indicators are updated every 15 minutes.
Once you have installed Now Assist AI Agents, you can collect initial data by running the [Now
Assist AI Agents] Historical Data Collection job. The other data collection jobs, [Now Assist AI
Agents] Daily Data Collection and [Now Assist AI Agents] Periodic Data Collection, update the
indicators.
Automated indicators for AI agents
Name Description
Agentic workflow latency Time taken for an agentic workflow to complete.
AI agent execution plan P90 Time taken for 90% of AI agent execution plans in a system
latency to be processed.
AI agent execution plan P95 Time taken for 95% of AI agent executions plans in a
latency system to be processed.

<!-- page 247 -->
Automated indicators for AI agents
(continued)
Name Description
AI agent execution plan P99 Time taken for 99% of AI agent execution plans in a system
latency to be processed.
AI agent latency Time taken for an AI agent in a system to be processed.
All agentic workflows Total number of agentic workflows created before today.
All AI agents Total number of AI agents created before today.
All tools Total number of tools created before today.
LLM P90 latency Time taken for 90% of LLM requests in a system to be
processed.
LLM P95 latency Time taken for 95% of LLM requests in a system to be
processed.
LLM P99 latency Time taken for 99% of LLM requests in a system to be
processed.
Number of closed tasks Total number of tasks closed.
Number of closed tasks with AI Total number of tasks closed today that were closed with
agent assist agentic workflows or AI agents.
Summed duration of closed tasks Total time taken to close tasks.
Summed duration of closed tasks Total time taken to close tasks today that were closed with
with AI agent assist agentic workflows or AI agents.
Tool execution P90 latency Time taken for 90% of tool executions in a system to be
processed.
Tool execution P95 latency Time taken for 95% of tool executions in a system to be
processed.
Tool execution P99 latency Time taken for 99% of tool executions in a system to be
processed.

<!-- page 248 -->
Automated indicators for AI agents
(continued)
Name Description
Tool latency Time taken for a tool in a system to be processed.
Total number of CS conversations Total number of conversations in Now Assist panel or
Virtual Agent.
Total number of execution plans Total number of execution plans created by agentic
workflows and AI agents today.
Total number of execution tasks Total number of tasks executed by agentic workflows and
AI agents today.
Total number of tool executions Total number of tool executions in agentic workflows and
AI agents today.
Use case execution plan P90 Time taken for 90% of agentic workflows in a system to be
latency processed.
Use case execution plan P95 Time taken for 95% of agentic workflows in a system to be
latency processed.
Use case execution plan P99 Time taken for 99% of agentic workflows in a system to be
latency processed.
Formula indicators for AI agents
Name Description
% of conversations with Number of conversations in Now Assist panel or Virtual Agent
an AI agent or agentic with a defined AI agentic or agentic workflow divided by the total
workflow defined number of conversations.
Average time to close a Average time taken for a task to go from creation to closure.
task
Average time to close a Average time taken for a task to go from creation to closure with an
task with AI agent assist agentic workflow or AI agent involved.

<!-- page 249 -->
Formula indicators for AI agents
(continued)
Name Description
Efficiency gain Percentage efficiency gain comparing average time taken to close
a task with AI agent assist against a task closed without AI agent
assist.
Percentage of tasks closed Number of tasks closed using AI agents and agentic workflows
using AI agents divided by the total number of tasks.
Breakdowns
Different breakdowns enable you to divide the data differently to track specific aspects of the AI
agent usage. Not all breakdowns are available for all indicators.
•Agentic workflow
•AI agent
•AI agent execution status
•Latency metric
•Tool
•Tool latency metric
Filters
You can filter data to review a subset of trends. The following table lists the available filters on the
AI Agent Analytics dashboard.
Filters on the AI Agent Analytics dashboard pages
Page Available filters
Status Time created
•Time created
Insights
•Agentic workflow
•AI agent
•AI Agent Type
•Time created
Assist consumption
•Agentic workflow
•AI agent
•AI Agent Type

<!-- page 250 -->
Filters on the AI Agent Analytics dashboard pages (continued)
Page Available filters
•Time created
Performance
•Agentic workflow
•AI agent
•AI Agent Type
•Tool
Troubleshooting Time created
Data visualizations
Visualizations are graphic elements that can be used to see data trends, percentages, and
scores. The AI Agent Analytics dashboard includes the following visualizations.
Data visualizations on the AI Agent Analytics dashboard overview page
Title Type Description
Average Score AI-generated score estimating what a customer would rate the AI
inferred CSAT card response. 1 being the user is extremely dissatisfied and 5 being the
for AI agents user is extremely satisfied with the interaction.
in last 7 days
Execution Pie Execution tasks divided by status (Success, Ongoing, Cancelled,
tasks in last 7 chart Queued).
days
AI Agent Line Number of errors seen by AI agents within the last 90 days broken down
errors in last graph by week.
90 days
AI agent tool Pie Tools divided by type. Example: Script, Flow action, Subflow, and so on.
type chart
AI agent tool Pie Tools divided by either autonomous or supervised execution mode.
execution chart
mode
Execution Pie Execution plans divided by status (Completed, Terminated, Wrap Up, or
plans in last 7 chart In Progress)
days

<!-- page 251 -->
Data visualizations on the AI Agent Analytics dashboard overview page (continued)
Title Type Description
AI agent List List of AI agent executions. The list is broken down by AI agent and AI
executions agent execution status. Columns span for multiple weeks, and there are
change percentages and trend lines comparing the current against the
previous week.
Number Trend Total number of agentic workflows. The agentic workflows created in the
of agentic line last day and a trend line are shown.
workflows
Number of AI Trend Total number of AI agents. The AI agents created in the last day and a
agents line trend line are shown.
Number of Trend Total number of tools. The tools created in the last day and a trend line
tools line are shown.
AI agent List List of AI agent execution plans. The list is broken down by agentic
execution workflow. Columns span for multiple weeks, and there are change
plans percentages and trend lines comparing the current against the previous
week.
Data visualizations on the AI Agent Analytics dashboard status page
Title Type Description
AI agent Score Four score cards, one for each execution plan status (Ready, In progress
execution cards right now, Completed, and Terminated).
plans
AI agent Score Four score cards, one for each execution plan status (In progress right now,
executions cards Completed, Successful, and Errors/Cancelled).
AI agent/ List List of AI agent and tool executions. The list is broken down by AI agent and
tool tool, and there are columns for each status (Cancelled, Ongoing, Queued,
executions and Success).
Data visualizations on the AI Agent Analytics dashboard insights page
Title Type Description
Tasks closed Trend Percentage of tasks closed using AI agents. Trend line is shown.
using AI agents line

<!-- page 252 -->
Data visualizations on the AI Agent Analytics dashboard insights page (continued)
Title Type Description
Task closure Trend Percentage efficiency gained with agentic workflows and AI agents.
efficiency gain line Trend line is shown.
using AI agents
Average close Trend Average time taken for a task to go from creation to closure with the
time assisted line involvement of an AI agent or agentic workflow. Trend line is shown.
by AI agents
Inferred CSAT Score Estimated CSAT score calculated using AI based on the subjective
of AI agents card quality of the AI agents' responses. 1 being the user is extremely
dissatisfied and 5 being the user is extremely satisfied with the
interaction.
Inferred Score Estimated CSAT score calculated using AI based on the overall session
Session CSAT card interactions of a user. 1 being the user is extremely dissatisfied and 5
being the user is extremely satisfied with the interaction.
Top user Bar Most common user intents as interpreted by the LLM. Intents are
intents when chart grouped by Group Action Framework.
using agentic
solutions
Average AI Bar Average CSAT score for each user intent interpreted by the LLM.
agent CSAT by chart Intents are grouped by Group Action Framework.
intent
Transfers and Bar An estimated score using AI that indicates whether the user requested
escalations chart an escalation or there was a transfer to another AI agent or human.
using AI agents
User effort Bar Counts of AI-generated scores that measure the time and energy users
required with chart had to put in during their interaction with an AI agent. Values are on a
AI agents 3-point scale of low, medium, and high.
AI agent Bar Counts of AI-generated scores that indicate whether the AI agent
recommended chart recapped the outcome and provided clear instructions or guidance
next steps on what the customer should do next, if applicable. Values are on a 3-
point scale of low, medium, and high.
AI agent Score An AI-generated score that indicates whether the AI agent resolved
resolved the card the user's request. Values can be yes, no or unknown.
users request

<!-- page 253 -->
Data visualizations on the AI Agent Analytics dashboard insights page (continued)
Title Type Description
User frustration Bar An AI-generated score that indicates whether the user expressed
with AI agents chart frustration at any point in the conversation.
AI agent Score An AI-generated score that indicates whether the AI agent was
empathy card empathetic and friendly. Values are on a 3-point scale of low, medium,
and high.
User or Bar Counts of an AI-generated score that indicates whether the user or AI
AI agent chart agent is confused at any point of the conversation.
confusion
Top 10 agentic Bar Top 10 agentic workflows by highest CSAT score.
workflows chart
with highest
session CSAT
Bottom 10 Bar Bottom 10 agentic workflows by CSAT score.
agentic chart
workflows
with highest
session CSAT
Top 10 AI Bar Top 10 AI agents by highest CSAT score.
agents with chart
highest
session CSAT
Bottom 10 Bar Bottom 10 AI agents by CSAT score.
AI agents chart
with highest
session CSAT
AI agent Trend Total number of AI agent conversations in Now Assist panel or Virtual
conversations line Agent. Trend line is shown.
daily
% of Trend Percentage of AI agent conversations in Now Assist panel or Virtual
conversations line Agent that used agentic workflows or AI agents. Trend line is shown.
using AI agents
Efficiency gain List List of indicators. The list is broken down by indicator. Columns span
supporting across a time span.
indicators

<!-- page 254 -->
Data visualizations on the AI Agent Analytics dashboard assist consumption page
Title Type Description
Sum of AI agent Score Total number of assists used on the instance for both AI agents
assists card and agentic workflows.
Sum of AI agent Pie Totals and percentages of assists divided by tier. An assist is
assists per tier chart marked as small until the number of tool executions exceeds
20.
Count of AI agent Pie Count of assist tiers for both AI agents and agentic workflows.
executions per assist chart An assist is marked as small until the number of tool executions
tier. exceeds 20.
Top 10 agentic Pie Percentages of assists consumed among the top 10 agentic
workflows consuming chart workflows consuming assists.
assists
Sum of AI agents Bar Total number of assists used by AI agents broken down by day.
assists chart
Count of AI agent Bar Count of assists used by AI agents broken down by assist tier
executions per assist chart and day.
tier
Count of AI agent Bar Count of assists used by AI agents broken down by agentic
executions per chart workflow.
agentic workflow
Sum of AI agent Bar Number of assists used by AI agents broken down by AI agent.
assists per AI agent chart
Average tool List Count of tools executed by an agentic workflow broken down by
execution count per agentic workflow and day.
agentic workflow
Average tool List Count of tools executed by an agentic workflow broken down by
execution count per assist tier and day.
assist tier

<!-- page 255 -->
Data visualizations on the AI Agent Analytics dashboard performance page
Title Type Description
P90 Score Time in seconds of 90% of agentic workflows in a system to be processed.
agentic card
workflow
latency
P95 Score Time in seconds of 95% of agentic workflows in a system to be processed.
agentic card
workflow
latency
P99 Score Time in seconds of 99% of agentic workflows in a system to be processed.
agentic card
workflow
latency
Total Bar Visualization of what time of day agentic workflows have been executed by
agentic chart hour.
workflows
executed
per hour
Total Bar Visualization of what time of day agentic workflows have been executed and
agentic chart experienced an error by hour.
workflows
errors per
hour
Agentic Line Agentic workflow latency over time. Uses 3 different indicators: P90 tracks
workflow chart the fastest 90% of executions, P95 tracks the fastest 95% of executions, and
latency P99 tracks the fastest 99% of executions.
Agentic Line Agentic workflow latency over time. Uses 3 different indicators: P90 tracks
workflow chart the fastest 90% of executions, P95 tracks the fastest 95% of executions, and
latency P99 tracks the fastest 99% of executions.
(weekly
average)
Agentic Table Average agentic workflow latency today. Each row is an agentic workflow
workflow and each column is a different latency metric. Uses 3 different indicators:
latency P90 tracks the fastest 90% of executions, P95 tracks the fastest 95% of
(daily executions, and P99 tracks the fastest 99% of executions.
average)

<!-- page 256 -->
Data visualizations on the AI Agent Analytics dashboard performance page (continued)
Title Type Description
P90 AI Score Time in seconds of 90% of AI agent executions in a system to be processed.
agent card
latency
P95 AI Score Time in seconds of 95% of AI agent executions in a system to be processed.
agent card
latency
P99 AI Score Time in seconds of 99% of AI agent executions in a system to be processed.
agent card
latency
Total AI Bar Visualization of what time of day AI agent executions have been executed
agents chart by hour.
executed
per hour
Total AI Bar Visualization of what time of day AI agent executions have been executed
agent chart and experienced an error by hour.
errors per
hour
AI agent Line AI agent latency within the time filter. Uses 3 different indicators: P90 tracks
latency chart the fastest 90% of executions, P95 tracks the fastest 95% of executions, and
P99 tracks the fastest 99% of executions.
AI agent Line AI agent latency over time by week. Uses 3 different indicators: P90 tracks
latency chart the fastest 90% of executions, P95 tracks the fastest 95% of executions, and
(weekly P99 tracks the fastest 99% of executions.
average)
AI agent Table Average AI agent latency today. Each row is an AI agent and each column is
latency a different latency metric. Uses 3 different indicators: P90 tracks the fastest
(daily 90% of executions, P95 tracks the fastest 95% of executions, and P99 tracks
average) the fastest 99% of executions.
P90 tool Score Time in seconds of 90% of tool executions in a system to be processed.
latency card
P95 tool Score Time in seconds of 95% of tool executions in a system to be processed.
latency card

<!-- page 257 -->
Data visualizations on the AI Agent Analytics dashboard performance page (continued)
Title Type Description
P99 tool Score Time in seconds of 99% of tool executions in a system to be processed.
latency card
Total tools Bar Visualization of what time of day tool executions have been executed by
executed chart hour.
per hour
Total tool Bar Visualization of what time of day tool executions have been executed and
errors per chart experienced an error by hour.
hour
Tool Line Tool latency within the time filter. Uses 3 different indicators: P90 tracks the
latency chart fastest 90% of executions, P95 tracks the fastest 95% of executions, and
P99 tracks the fastest 99% of executions.
Tool Line Tool latency over time by week. Uses 3 different indicators: P90 tracks the
latency chart fastest 90% of executions, P95 tracks the fastest 95% of executions, and
(weekly P99 tracks the fastest 99% of executions.
average)
Tool Table Average tool latency today. Each row is a tool and each column is a different
latency latency metric. Uses 3 different indicators: P90 tracks the fastest 90% of
(daily executions, P95 tracks the fastest 95% of executions, and P99 tracks the
average) fastest 99% of executions.
P90 LLM Score Time in seconds of 90% of LLM requests in a system to be processed.
latency card
P95 LLM Score Time in seconds of 95% of LLM requests in a system to be processed.
latency card
P99 LLM Score Time in seconds of 99% of LLM requests in a system to be processed.
latency card
LLM Line Tool latency within the time filter. Uses 3 different indicators: P90 tracks the
latency chart fastest 90% of executions, P95 tracks the fastest 95% of executions, and
P99 tracks the fastest 99% of executions.
LLM Line Tool latency over time by week. Uses 3 different indicators: P90 tracks the
latency chart fastest 90% of executions, P95 tracks the fastest 95% of executions, and
(weekly P99 tracks the fastest 99% of executions.
average)

<!-- page 258 -->
Data visualizations on the AI Agent Analytics dashboard performance page (continued)
Title Type Description
LLM calls Bar Visualization of what time of day LLM calls have been made by hour.
per hour chart
LLM errors Bar Visualization of what time of day LLM calls have been made and
per hour chart experienced an error by hour.
Data visualizations on the AI Agent Analytics dashboard troubleshooting page
Name Type Description
Agentic workflow errors List List of agentic workflow errors.
For more information on security controls for agentic AI, see Security for AI agents.
Data visualizations on the AI Agent Analytics dashboard security page
Name Type Description
Total blocked executions Score Total number of agentic AI executions blocked because of
card security controls.
Total blocked executions List List of executions blocked.
Top agentic workflows with List List of agentic workflows with the most blocked
blocked executions executions.
Top AI agents with blocked List List of AI agents with the most blocked executions.
executions
Agentic Workflows w/o ACL Score Total number of agentic workflows missing an ACL for user
defined card access.
Agentic Workflows ACLs Pie Pie chart displaying the percentage of agentic workflows
chart with and without ACLs for user access.
Agentic Workflows w/o ACL List List of agentic workflows missing an ACL for user access.
defined

<!-- page 259 -->
Data visualizations on the AI Agent Analytics dashboard security page (continued)
Name Type Description
AI agents with no ACLs Score Total number of AI agents missing an ACL for user access.
defined card
AI agent ACLs Pie Pie chart displaying the percentage of AI agents with and
chart without ACLs for user access.
AI agents w/o ACL defined List List of AI agents missing an ACL for user access.
Agentic workflows without Score Total number of agentic workflows without roles identified
role masking card for role masking and data access.
Agentic workflows without List List of agentic workflows without roles identified for role
role masking masking and data access.
AI agents without role Score Total number of AI agents without roles identified for role
masking card masking and data access.
AI agents without role List List of AI agents without roles identified for role masking
masking and data access.
Agentic workflows running Score Total number of agentic workflows running as a dynamic
as dynamic user card user.
Agentic workflows running List List of agentic workflows running as a dynamic user.
as dynamic user
AI agents running as Score Total number of AI agents running as a dynamic user.
dynamic user card
AI agents running as List List of AI agents running as a dynamic user.
dynamic user
Agentic workflows running Score Total number of agentic workflows running as an AI user.
as AI user card
Agentic workflows running List List of agentic workflows running as an AI user.
as AI user
AI agents running as AI user Score Total number of AI agents running as an AI user.
card

<!-- page 260 -->
Data visualizations on the AI Agent Analytics dashboard security page (continued)
Name Type Description
AI agents running as AI user List List of AI agents running as an AI user.
Agentic evaluation run results
Learn about agentic evaluation runs and the meaning behind different evaluation scores from
the agentic evaluation results page.
Agentic evaluations overview
Agentic evaluations measure how well AI agents and agentic workflows are accomplishing
their objectives. A Now LLM Service model judges the AI agent or agentic workflow based on
the execution logs. The results page of an evaluation run shows multiple metrics and scores
measuring task completeness and tool use.
If you run an overall task completion evaluation, the results page shows recommended actions
for the AI agent or agentic workflow. Recommended actions give you suggestions for deployment
or improvement to help verify that the agentic workflows that you deploy are performing up to
your standards.
After you've reviewed your evaluation results, you can archive your evaluation or copy it to run
another evaluation with the same parameters and dataset.
You can export the evaluation results as a report. The report is formatted as a .csv file that
includes the individual sys_ids of the execution records and the metric scores for each.
For more information on AI agent usage and other analytics, you can review the AI Agent
Analytics dashboard in the AI Agent Studio.
Evaluation results overview
For each evaluation method that you execute, the results page displays an overall score for the
agentic workflow with a percentage of successful record evaluations and a label of Excellent,
Good, Moderate, or Poor. You can change the metric thresholds for each label by selecting
Customize metric thresholds.
In addition to the overall task completeness results, you can review a summary of the results of
the other metrics.
Overall task completeness evaluation run results
Default
Label Description Recommended action
threshold
Excellent Tasks were consistently performed at a high Proceed with 90%–
standard. The agentic workflow or AI agent is confidence 100%
working well.

<!-- page 261 -->
Overall task completeness evaluation run results (continued)
Default
Label Description Recommended action
threshold
Good Most tasks were performed successfully, but Deploy with caution 70%–
some performance inconsistencies suggest areas 89%
for improvement.
Moderate A significant number of tasks weren't fully Investigate the root 50%–
completed. Performance is below the desired causes of poor task 69%
level. completion
Poor The agentic workflow is consistently failing to Do not deploy 0%–
complete tasks adequately. Major issues are 49%
present.
Individual record metric scores
Evaluations are run against the log tables of agentic workflow executions. Each record is
individually scored for each evaluation plan that you run. Individual record evaluations are
scored according to the following metrics.
Overall task completeness record metric scores
The overall task completeness metric assesses whether an AI agent
successfully completes its assigned task. It evaluates the execution logs of the
agent, ensuring that all required steps were taken and the task was logically
and effectively completed.
Number Score Description
3 Successful The main task was fully completed. All subtasks were resolved, and the
steps followed a logical sequence with no critical errors.
2 Partially The task was partially completed. Some subtasks remain unresolved or
successful inefficiencies affected the process.
1 Unsuccessful The task wasn't completed. Critical subtasks were abandoned or
unresolved or the execution failed entirely.

<!-- page 262 -->
Tool performance record metric scores
The tool performance evaluation metric assesses an AI agent's ability to select
the most appropriate tool for each step while completing a task.
Number Score Description
1 True The right tool was chosen for the action in the plan.
0 False The right tool wasn't chosen.
Tool calling records metric scores
The tool calling evaluation metric assesses whether an AI agent correctly
constructs tool calls by validating the accuracy, completeness, and formatting
of the inputs it provides.
Number Score Description
1 True Input key completeness, input value correctness, and input format correctness
are all successful.
•Input key completeness: 1 - True – All required parameters are
present with exact name matches, and no unexpected parameters are
included.
•Input value correctness: 1 - True – Tool input values are correctly
mapped.
•Input format correctness: 1 - True – Tool inputs are in the correct
format.
0 False One or more of input key completeness, input value completeness, or input
format completeness wasn't successful.
•Input key completeness: 0 - False – A mandatory parameter is either
missing, its name doesn't match exactly, or an unexpected parameter was
found.
•Input value correctness: 0 - False – Tool input values are not
correctly mapped.
•Input format correctness: 0 - False – Tool inputs are not in the
correct format.
Note: The values of the sub-metrics are aggregated using an AND operator. If any one
value is 0, then the entire tool calling records metric score will be 0.