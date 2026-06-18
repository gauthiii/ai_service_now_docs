# AI Agent Analytics dashboard

_Source pages: 246–259 | Depth: 2_

---

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