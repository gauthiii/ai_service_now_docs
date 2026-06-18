# Monitoring in Now Assist Center

> **Source document:** Now Assist Center  
> **Pages:** 53–69


Guardrail Description
Select Offensiveness to open the Offensive­
ness tab.
For more information on how to configure this
guardrail, see Activate offensiveness protec­
tion for generative AI.
This guardrail filters subjects not suited for
AI responses, such as workplace safety or
employee compensation. It applies to Virtual
Agent conversational skills only (available for
HR Service Delivery and Customer Service
Sensitive topic filters Management).
Select Sensitive Filters to open the Filters
tab.
For more information on how to configure this
guardrail, see Configure sensitive topic filters.

### Monitoring in Now Assist Center

Monitor AI readiness, usage, and performance using Now Assist Center.

### Monitor your recently activated Now Assist solution in Now Assist Center

View performance metrics on your most recently activated AI solutions on the Now Assist Center
home page.

### Before you begin

Role required: sn_na_center.nac_admin

### Procedure

1.Navigate to All > Now Assist Center or Workspaces > Now Assist Center.
2. Select Home ( ) in the side navigation bar.
3. Review the Recently activated AI section of the home page to see the performance metrics on
your most recently activated AI solutions.
Recently activated AI section of the home page
4.Select View all analytics to see a complete list of performance metrics on the Analytics tab.

| Guardrail | Description |
| --- | --- |

> **[Screenshot: Recently Activated AI Section on Now Assist Center Home Page]**
>
> The "Recently Activated AI" section card. A "View all analytics" button top-right. One card: "KB generation for" with a teal line chart. X-axis dates Feb 27–Mar 26; Y-axis 0–50. Line fluctuates with peak around Mar 14. Legend: "Gen AI Actions per day."


The Analytics page opens.
For more information, see View AI assets usage and performance in Now Assist Center.

### View AI assets usage and performance in Now Assist Center

Use Now Assist Center to view dashboards showing the usage and performance of your AI
assets.

### Before you begin

Role required: sn_na_center.nac_admin

### Procedure

1.Navigate to All > Now Assist Center or Workspaces > Now Assist Center.
2. Select Monitor ( ) in the side navigation bar.
The Analytics page opens showing tabs for the different dashboards.
Dashboards and data visualizations are derived from various Now Assist features and are
grouped by asset type.
3. Select the tab for the dashboard you want to view.
Some tabs contain another set of tabs for viewing the various usage, performance, and
governance properties of the asset type.
4.Select the tab for the data visualizations you want to view.
The Overview tab displays a summary of AI asset activation, adoption, and usage across
your organization. Use the dashboard to monitor the state of your AI assets and track user
engagement across departments. For more information, see Now Assist Center Overview
dashboard.

> **[Screenshot: Analytics Page — Overview Dashboard with Activation, Adoption, and Usage Sections]**
>
> The Monitor analytics page tab bar: Overview (active), Performance Explorer, Skills, AI Agents, Assistants, Business Value. Date filter: "Last 3 months." Three main sections:
>
> **Activation section**: Four metric cards in a row — "Active skills" (108, large number), "Active assistants" (5), "Active AI agents" (112), "Active asset trends" (line chart with three coloured lines for Skills/Assistants/AI Agents, Jan–Apr, Y-axis 0–100, Skills line is highest at ~108).
>
> **Adoption section**: Four bar/trend charts — "Number of users using skills" (horizontal bar, Finance dept highlighted in teal), "Number of users using assistants" (horizontal bars by dept: Product Manage., Sales, Customer Support, Finance, HR, IT), "Number of users using AI agents" (Customer Support, Finance, HR, IT, Sales), "Users by asset type" (multi-line trend Jan–Apr, three coloured lines).
>
> **Usage section** (partially visible): "Total number of skill executions" (bar chart, Finance), "Total assistant executions" (bars by dept), "Total AI agent executions" (HR, Customer Support, Finance, IT, Sales), "Total executions by asset type" (trend line Jan–Apr, Y-axis 0–400).


The Performance Explorer tab displays execution-level details for assistants and AI agents.
Use the dashboard to investigate individual executions, analyze performance For more
information, see Now Assist Center Performance Explorer dashboard.
The Business Value dashboard displays a consolidated view of the business value generated
by AI assets across your organization. Use the dashboard to monitor total executions, time
saved, and cost saved across skills, AI agents, and agentic workflows. For more information,
see Now Assist Center Business Value dashboard.
The Skills tab provides dashboards showing usage and performance metrics for Now Assist
skills. The dashboards are featured in the Performance section of the Now Assist Admin
console. For more information, see Analyzing Now Assist performance.
Dashboards under the Skills tab
Tab Description
Usage Summary
The Usage summary dashboard page
includes indicators on total and daily
Now Assist actions, skill distribution and
engagement trend, and daily unique users
who have engaged with Now Assist.
For more information, see Usage and
adoption.
Offensiveness
The Offensive content dashboard page helps
you monitor and evaluate the effectiveness
of Now Assist Guardian guardrails in tracking
and analyzing requests sent to large
language models (LLM) and their responses.
For more information, see Now Assist
Guardian analytics.
Context Menu
The Now Assist context menu dashboard
page helps you to evaluate the effectiveness
of context menu actions in assisting agents
with summarizing, creating, and editing
emails and chat replies.
For more information, see Now Assist context
menu analytics.

### Adoption

The Adoption dashboard page tracks the
departments with the highest Now Assist
usage, comparison of actions by department,
and feedback and error details.
For more information, see Usage and
adoption.

| Tab | Description |
| --- | --- |
| Usage Summary | The Usage summary dashboard page includes indicators on total and daily Now Assist actions, skill distribution and engagement trend, and daily unique users who have engaged with Now Assist. For more information, see Usage and adoption. |
| Offensiveness | The Offensive content dashboard page helps you monitor and evaluate the effectiveness of Now Assist Guardian guardrails in tracking and analyzing requests sent to large language models (LLM) and their responses. For more information, see Now Assist Guardian analytics. |
| Context Menu | The Now Assist context menu dashboard page helps you to evaluate the effectiveness of context menu actions in assisting agents with summarizing, creating, and editing emails and chat replies. For more information, see Now Assist context menu analytics. |
| Adoption | The Adoption dashboard page tracks the departments with the highest Now Assist usage, comparison of actions by department, and feedback and error details. For more information, see Usage and adoption. |

Tab Description
Skill Performance
The Skills performance dashboard page
contains indicators that help you analyze the
usage and performance of active skills.
For more information, see Skills performance.
Prompt Injection
The Prompt Injection dashboard page helps
you monitor and evaluate the effectiveness
of Now Assist Guardian guardrails in tracking
and analyzing requests sent to large
language models (LLM) and their responses.
For more information, see Now Assist
Guardian analytics.
User Search Analyser
The User search analyzer dashboard page
contains indicators that help you understand
the effectiveness of search in enhancing the
self-service experience.
For more information, see User search
analyzer.
The AI Agents tab provides dashboards showing usage and performance metrics for AI agents.
The dashboards are featured on the AI Agent Analytics page of the AI Agent Studio. For more
information, see AI Agent Analytics dashboard.
Dashboards under the AI Agents tab
Tab Description
Overview
The Overview dashboard page provides
summary indicators for the usage,
performance, and efficiency of AI agents.
Status
The Status dashboard page provides an
operational view of the AI agent deployment
on the instance. It displays the current
activation state of agentic workflows and AI
agents and gives you a quick health check
without having to navigate to individual asset
records.
Insights
The Insights dashboard page shows deeper
analytical findings about how AI agents are
being used in practice. It helps you spot
recurring problems by tracking errors over
time and identify patterns in agent behavior.

| Tab | Description |
| --- | --- |
| Skill Performance | The Skills performance dashboard page contains indicators that help you analyze the usage and performance of active skills. For more information, see Skills performance. |
| Prompt Injection | The Prompt Injection dashboard page helps you monitor and evaluate the effectiveness of Now Assist Guardian guardrails in tracking and analyzing requests sent to large language models (LLM) and their responses. For more information, see Now Assist Guardian analytics. |
| User Search Analyser | The User search analyzer dashboard page contains indicators that help you understand the effectiveness of search in enhancing the self-service experience. For more information, see User search analyzer. |

| Tab | Description |
| --- | --- |
| Overview | The Overview dashboard page provides summary indicators for the usage, performance, and efficiency of AI agents. |
| Status | The Status dashboard page provides an operational view of the AI agent deployment on the instance. It displays the current activation state of agentic workflows and AI agents and gives you a quick health check without having to navigate to individual asset records. |
| Insights | The Insights dashboard page shows deeper analytical findings about how AI agents are being used in practice. It helps you spot recurring problems by tracking errors over time and identify patterns in agent behavior. |

Tab Description
Assist Consumption
The Assist Consumption dashboard page
displays indicators for assist consumption
and consumption trends on agentic
executions so you can track spend against
entitlements.
Performance
The Performance dashboard page helps
you identify which agents, tools, or workflow
steps are introducing delays, and supports
the optimization of multi-step agentic
processes.
Troubleshooting
The Troubleshooting dashboard page
provides diagnostics for failed or degraded
AI agent executions. It shows error counts,
failed tool calls, and failed agent calls across
the instance, and helps you identify the
scope and pattern of failures.
Security
The Security dashboard page displays
metrics and status information related to
security controls for AI agents and agentic
workflows.
The Assistants tab provides dashboards showing usage and performance metrics for AI
assistants. The dashboards are featured on the Analytics feature of the Assistant Designer. For
more information, see Analyzing assistants .
Dashboards under the Assistants tab
Tab Description
Overview
The Overview dashboard page provides
high-level summary of assistant activity,
assist usage, user engagement and overall
customer satisfaction (CSAT) score.
For more information, see Overview page in
Assistant analytics .

### Usage

The Usage dashboard page aggregates
key metrics related to assistant usage,
including the total number of conversations
by assistant, conversations by channel,
citations associated with the results, and the
flow of conversation states.
For more information, see Usage page in
Assistant analytics .

| Tab | Description |
| --- | --- |
| Assist Consumption | The Assist Consumption dashboard page displays indicators for assist consumption and consumption trends on agentic executions so you can track spend against entitlements. |
| Performance | The Performance dashboard page helps you identify which agents, tools, or workflow steps are introducing delays, and supports the optimization of multi-step agentic processes. |
| Troubleshooting | The Troubleshooting dashboard page provides diagnostics for failed or degraded AI agent executions. It shows error counts, failed tool calls, and failed agent calls across the instance, and helps you identify the scope and pattern of failures. |
| Security | The Security dashboard page displays metrics and status information related to security controls for AI agents and agentic workflows. |

| Tab | Description |
| --- | --- |
| Overview | The Overview dashboard page provides high-level summary of assistant activity, assist usage, user engagement and overall customer satisfaction (CSAT) score. For more information, see Overview page in Assistant analytics . |
| Usage | The Usage dashboard page aggregates key metrics related to assistant usage, including the total number of conversations by assistant, conversations by channel, citations associated with the results, and the flow of conversation states. For more information, see Usage page in Assistant analytics . |

Tab Description
Adoption & Engagement
The Adoption & Engagement dashboard
page aggregates metrics related to user
adoption and engagement, including average
active users, new user growth, conversation
volume trends, assist-to-execution trend, and
channel distribution.
For more information, see Adoption and
Engagement page in Assistant analytics .
Self Solved
The Self-Solve Performance dashboard page
aggregates metrics related to self-solved
events (instances where assistants resolved
user queries), deflection rates, live agent
transfers, and user effort.
For more information, see Self-Solve
Performance page in Assistant analytics .
Sentiment
The Sentiment dashboard page aggregates
metrics related to user satisfaction, emotional
feedback, empathy levels, and conversation
outcomes. These metrics enable you to
monitor inferred CSAT, track transfers and
escalations, analyze empathy distribution,
and review negative emotion trends.
For more information, see Sentiment page in
Assistant analytics .
Assists
The Assists dashboard page aggregates
metrics related to conversational assists,
including total assists consumed, usage
breakdown by assistant, usage trends, and
features which used the most number of
assists.
For more information, see Assists page in
Assistant analytics .

### Now Assist Center Overview dashboard

Use the Now Assist Center Overview dashboard to monitor key metrics for AI asset activation,
adoption, and usage across your organization.

### Now Assist Center Overview dashboard

The Now Assist Center Overview dashboard displays a summary of AI asset activation, adoption,
and usage across your organization. Use the dashboard to monitor the state of your AI assets
and track user engagement across departments.

| Tab | Description |
| --- | --- |
| Adoption & Engagement | The Adoption & Engagement dashboard page aggregates metrics related to user adoption and engagement, including average active users, new user growth, conversation volume trends, assist-to-execution trend, and channel distribution. For more information, see Adoption and Engagement page in Assistant analytics . |
| Self Solved | The Self-Solve Performance dashboard page aggregates metrics related to self-solved events (instances where assistants resolved user queries), deflection rates, live agent transfers, and user effort. For more information, see Self-Solve Performance page in Assistant analytics . |
| Sentiment | The Sentiment dashboard page aggregates metrics related to user satisfaction, emotional feedback, empathy levels, and conversation outcomes. These metrics enable you to monitor inferred CSAT, track transfers and escalations, analyze empathy distribution, and review negative emotion trends. For more information, see Sentiment page in Assistant analytics . |
| Assists | The Assists dashboard page aggregates metrics related to conversational assists, including total assists consumed, usage breakdown by assistant, usage trends, and features which used the most number of assists. For more information, see Assists page in Assistant analytics . |

Use the Date filter at the top of the Overview dashboard to set the time range for all metrics on
the page. The default time range is Last 3 months.

### Now Assist Center Overview dashboard


### Activation

The Activation section displays the current number of active AI assets and their trends over the
selected time range.
Activation section of the Now Assist Center Overview dashboard
Active skills
This area of the dashboard displays the total number of skills that are currently
active in your instance. Use this count to understand the scale of your deployed skill
library.
Active assistants

> **[Screenshot: Now Assist Center Overview Dashboard — Full Layout]**
>
> A full screenshot of the "Now Assist Center : Ov..." tab showing the complete Overview dashboard. Navigation sub-tabs: Overview (active), Performance Explorer, Skills, AI Agents, Assistants, Business Value. Date picker: "Last 3 months."
>
> **Activation row**: Active skills=108, Active assistants=5, Active AI agents=107, Active asset trends (line chart, Jan–Apr, three lines for Skills/Assistants/AI Agents).
>
> **Adoption row**: Four charts — "Number of users using skills" (bar, Finance only), "Number of users using assistants" (multi-bar, Product Manage./Sales/Customer Support/Finance/HR/IT coloured by dept), "Number of users using AI agents" (Customer Support/Finance/HR/IT/Sales), "Users by asset type" (multi-line trend Jun–Apr).
>
> **Usage row**: "Total number of skill executions" (bar, Finance), "Total assistant executions" (bar, same depts), "Total AI agent executions" (bar, HR/Customer Support/Finance/IT/Sales), "Total executions by asset type" (line chart Jan–Apr, Y-axis 0–400).
>
> **[Screenshot: Activation Section Close-Up]**
>
> Close-up of just the Activation row: same four metrics as above with the trend chart clearly showing Skills (highest, flat ~108), Assistants (low, ~5), AI Agents (rising from ~50 to ~107) over Jan–Apr.


This area of the dashboard displays the total number of assistants that are currently
active in your instance. Use this count to track the scale of your deployed assistant
configurations.
Active AI agents
This area of the dashboard displays the total number of AI agents that are currently
active in your instance. Use this count to understand the scope of your active AI
agent deployments.
Active asset trends
This area of the dashboard displays a trend line chart showing the count of active
skills, assistants, and AI agents over the selected time range. Use the trend lines to
monitor how your active asset inventory has changed over time and identify periods
of growth or reduction across asset types.

### Adoption

The Adoption section shows how users across departments are engaging with AI assets over
the selected time range.
Adoption section of the Now Assist Center Overview dashboard
Number of users using skills
This area of the dashboard displays the number of users who used skills in the
selected time range, grouped by department. Use this visualization to identify which
departments have the highest skill adoption and which may benefit from further
enablement.
Number of users using assistants
This area of the dashboard displays the number of users who used assistants in
the selected time range, grouped by department. Use this visualization to compare
assistant adoption levels across departments and identify engagement patterns.
Number of users using AI agents
This area of the dashboard displays the number of users who used AI agents in the
selected time range, grouped by department. Use this visualization to track AI agent
adoption across your organization and identify departments with strong or limited
engagement.
Users by asset type
This area of the dashboard displays a trend line chart showing the number of users
per asset type (skills, assistants, and AI agents) over the selected time range. Use
the trend lines to compare adoption levels across asset types and identify shifts in
user preferences over time.

### Usage

The Usage section displays the total number of executions for each AI asset type, grouped by
department and asset type, over the selected time range.

> **[Screenshot: Adoption Section of Now Assist Center Overview Dashboard]**
>
> Close-up of the "Adoption" section. Four visualisations:
> - "Number of users using skills" — horizontal bar chart, Finance (teal bar, ~1 user).
> - "Number of users using assistants" — stacked horizontal bars by dept (Product Manage., Sales, Customer Support, Finance, HR, IT) with coloured segments (green Product Manage., purple Sales, teal Customer Support, orange Finance).
> - "Number of users using AI agents" — horizontal bars (Customer Support largest in green, then Finance, HR, IT, Sales).
> - "Users by asset type" — multi-line trend chart Jun–Apr: three lines (Users using Skills, Users using Assistants, Users using AI Agents). Values ~25 peak with fluctuations.


Usage section of the Now Assist Center Overview dashboard
Total number of skill executions
This area of the dashboard displays the total number of times skills were executed
in the selected time range, grouped by department. Use this visualization to
understand which departments are driving the most skill usage and identify high-
volume execution patterns.
Total assistant executions
This area of the dashboard displays the total number of assistant executions in
the selected time range, grouped by department. Use this visualization to identify
departments with the highest assistant usage and compare execution volumes
across your organization.
Total AI agent executions
This area of the dashboard displays the total number of AI agent executions in the
selected time range, grouped by department. Use this visualization to track AI agent
usage patterns across departments and identify areas of high or low engagement.
Total executions by asset type
This area of the dashboard displays a trend line chart showing the total executions
for skills, assistants, and AI agents over the selected time range. Use the trend lines
to compare usage volumes across asset types and monitor changes in execution
patterns over time.

### Now Assist Center Performance Explorer dashboard

Use the Now Assist Center Performance Explorer dashboard to review and analyze the execution
details of assistants and AI agents across your organization.

### Now Assist Center Performance Explorer dashboard

The Now Assist Center Performance Explorer dashboard displays execution-level details for
assistants and AI agents. Use the dashboard to investigate individual executions, analyze
performance metrics, and identify patterns across your AI asset deployments.
The Performance Explorer dashboard includes two sub-tabs: Assistants and Agents. Each sub-
tab displays a table of individual executions for the selected asset type.

### Assistants

The Assistants tab displays a list of individual assistant executions. Use the Date, Assistant
Name, Result Type Offered, Conversation End State, Deflection Outcome, and Deflection
State filters to narrow results. Select Reset Filters to clear all applied filters.

> **[Screenshot: Usage Section of Now Assist Center Overview Dashboard]**
>
> Close-up of the "Usage" section. Four visualisations:
> - "Total number of skill executions" — horizontal bar, Finance (~3 executions, teal).
> - "Total assistant executions" — bars by dept (Product Manage. tallest at ~5, then Sales, Customer Support, Finance, HR, IT).
> - "Total AI agent executions" — bars (HR ~4, Customer Support ~3, Finance ~2, IT ~1, Sales ~1).
> - "Total executions by asset type" — line chart Jan–Apr, Y-axis 0–400, three lines. Skill Executions (highest, ~400), Assistant Executions (~50), AI Agent executions (~10).


Assistants tab of the Now Assist Center Performance Explorer dashboard
Assistant Name
The name of the assistant that was executed. Select the assistant name to view the
full execution record.
Executed On
The date on which the assistant execution occurred.
Result type Offered
The type of result that the assistant offered during the execution, such as an answer,
a deflection, or a transfer.
Conversation End State
The state of the conversation at the end of the execution, such as Open or Faulted.
Inferred CSAT
The inferred customer satisfaction score for the execution, calculated based on
conversation signals.
Transfers and escalation
Indicates whether the conversation was transferred or escalated to a live agent
during the execution.
Assist
The number of assist actions performed by the assistant during the execution.
Deflection Outcome
The outcome of the deflection attempt, indicating whether the conversation was
successfully deflected.
Deflection State
The state of the deflection for the execution, such as deflected or not deflected.
Effort Score
A score reflecting the level of effort required by the user to complete the interaction,
based on conversation signals.

> **[Screenshot: Performance Explorer — Assistants Tab]**
>
> The "Performance Explorer" sub-tab with "Assistants" and "Agents" sub-tabs; Assistants is active. Filter row: Date (2026-05-26 – 2026-06-02), Assistant Name (All ▾), Result Type Offered (All ▾), Conversation End State (All ▾), Deflection Outcome (All ▾), Deflection State (All ▾), Reset Filters button. Table columns: Assistant Name, Executed On, Result type Offered, Conversation End State, Inferred CSAT, Transfers and escalation, Assist, Deflection Outcome, Deflection State, Effort Score. Rows visible: "Now Assist in Virtual Agent (default)" (2026-06-02, Faulted, 0 Assist, No Response), "Now Assist Panel – Platform (default)" (multiple rows, 2026-05-28 to 2026-06-02, mixed Faulted/Open). Pagination: 1-10 of 12.



### Agents

The Agents tab displays a list of individual AI agent executions. Use the Date, State, and E2E
Latency (S) filters, or the Search Agent field, to narrow results. Select Reset Filters to clear all
applied filters.
Agents tab of the Now Assist Center Performance Explorer dashboard
Agent Name
The name of the AI agent that was executed.
Executed On
The date on which the AI agent execution occurred.
State
The state of the AI agent execution, such as Completed or Terminated.
Tool Calls
The total number of tool calls made by the AI agent during the execution.
LLM Calls
The total number of large language model (LLM) calls made by the AI agent during
the execution.
E2E Latency (S)
The end-to-end latency of the execution, in seconds, measured from the start to the
completion of the AI agent run.
Tool Latency
The cumulative latency contributed by tool calls during the execution.
LLM Latency
The cumulative latency contributed by LLM calls during the execution.
Assists Consumed
The number of assist credits consumed by the AI agent during the execution.
Inferred CSAT
The inferred customer satisfaction score for the execution, calculated based on
interaction signals. See Exploring Conversation Insights for more information.

> **[Screenshot: Performance Explorer — Agents Tab]**
>
> The "Agents" sub-tab is active. Filter row: Date (2026-04-15 – 2026-04-22), State (All States ▾), E2E Latency (S) (All ▾), Search Agent field. Reset Filters button. Table columns: Agent Name, Executed On, State, Tool Calls, LLM Calls, E2E Latency (S), Tool Latency, LLM Latency, Assists Consumed, Inferred CS[AT]. One row: "KB content creation AI agent" (2026-04-22, Completed, Tool Calls=2, LLM Calls=5, E2E Latency=107.1s, Tool Latency=4.3s, LLM Latency=4.8s, Assists Consumed=0, Inferred CSAT=★2). Pagination: 1-3 of 3.



### Now Assist Center Business Value dashboard

Use the Now Assist Center Business Value dashboard to monitor the business value generated
by AI assets across your organization, including total executions, time saved, and cost saved.

### Now Assist Center Business Value dashboard

The Now Assist Center Business Value dashboard displays a consolidated view of the business
value generated by AI assets across your organization. Use the dashboard to monitor total
executions, time saved, and cost saved across skills, AI agents, and agentic workflows.
Use the Date filter at the top of the Business Value dashboard to set the time range for all metrics
on the page.


### Now Assist Center Business Value dashboard


> **[Screenshot: Now Assist Center Business Value Dashboard — Full Page]**
>
> Full-page screenshot of the "Business Value" dashboard tab. Navigation sub-tabs: Overview, Performance Explorer, Skills, AI Agents, Assistants, Business Value (active). "Add configuration" and "Take tour" buttons top-right. Date filter: 2025-12-01 – 2026-06-30.
>
> **Summary row (3 KPI cards)**: Total executions=83 (↑83 since May 1–Nov 30, 2025), Total time saved=2.96 Hrs (↑2.96 Hrs), Total cost saved=$1495.83 (↑$1495.83). Each card has a small trend sparkline below.
>
> **Time saved section**: "Time saved – Monthly trend" line chart (Dec 2025–Jun 2026, Y-axis 0–1.00 Hrs, three lines: Skill/AI Agent/Agentic Workflow; the Skill line is highest). Three horizontal bar charts: "Time saved by skill (Hrs)" (AI agents bar ~1.00 Hrs, AI Filter Assist ~0.00), "Time saved by AI Agent (Hrs)" (Document and vi... bar ~1.00 Hrs, KB content creat..., KB content cons..., Search Q&A Agent ~0.00), "Time saved by Agentic Workflow (Hrs)" (Identify ways to l... ~6.35 Hrs, Process emails fo... ~5.01 Hrs, Investigate probl... ~3.34 Hrs).
>
> **Cost saved section**: "Cost saved – Monthly trend" line chart (same period, Y-axis $0–$400, Skill line peaks around Feb 2026). Three bar charts: "Cost saved by skill" (AI agents ~$1000), "Cost saved by AI Agent" (Document and vi... ~$100), "Cost saved by Agentic Workflow" (Identify ways l... ~$8.35, Process emails... ~$6.68, Investigate probl... ~$5.01).
>
> **Executions section**: "Executions – Monthly trend" line chart (Y-axis 0–25, peaking Feb 2026). Three bar charts: "Executions by skill" (AI agents ~50), "Executions by AI Agent" (Document and vi... ~1, KB content ~3, others ~1–2), "Executions by Agentic Workflow" (Identify ways ~10, Process emails ~6, Investigate probl ~2).



### Total executions

This area of the dashboard displays the total number of times AI assets were
executed in the selected time range. Use this count to understand the overall scale
of AI asset usage across your organization.

### Total time saved

This area of the dashboard displays the total amount of time saved by AI asset
executions in the selected time range. Use this metric to quantify the productivity
impact of your AI asset deployments.

### Total cost saved

This area of the dashboard displays the total cost savings generated by AI asset
executions in the selected time range. Use this metric to assess the financial value
delivered by your AI assets.

### Time saved

The Time saved section displays the total time saved by AI asset executions, broken down by
asset type and shown as a monthly trend over the selected time range.
Time saved section of the Now Assist Center Business Value dashboard
Time saved - Monthly trend
This area of the dashboard displays a trend line chart showing the total time saved
by skills, AI agents, and agentic workflows each month over the selected time
range. Use the trend lines to monitor changes in time saved across asset types and
identify periods of higher or lower productivity impact.
Time saved by skill (Hrs)
This area of the dashboard displays a bar chart showing the total time saved by
each skill in the selected time range. Use this visualization to identify which skills are
delivering the greatest time savings in your organization.
Time saved by AI Agent (Hrs)
This area of the dashboard displays a bar chart showing the total time saved by
each AI agent in the selected time range. Use this visualization to compare time
savings across AI agents and identify your highest-impact deployments.
Time saved by Agentic Workflow (Hrs)
This area of the dashboard displays a bar chart showing the total time saved by
each agentic workflow in the selected time range. Use this visualization to evaluate
the time savings delivered by your agentic workflow configurations.

> **[Screenshot: Time Saved Section of Business Value Dashboard]**
>
> Close-up of the "Time saved" section. "Time saved – Monthly trend" line chart from Dec 2025 to Jun 2026, showing three coloured lines for Skill, AI Agent, and Agentic Workflow. The AI Agent line is highest peaking ~1.00 Hrs around Feb–Mar 2026. Three horizontal bar charts below for "Time saved by skill", "Time saved by AI Agent", "Time saved by Agentic Workflow".



### Cost saved

The Cost saved section displays the total cost savings generated by AI asset executions, broken
down by asset type and shown as a monthly trend over the selected time range.
Cost saved section of the Now Assist Center Business Value dashboard
Cost saved - Monthly trend
This area of the dashboard displays a trend line chart showing the total cost saved
by skills, AI agents, and agentic workflows each month over the selected time range.
Use the trend lines to track changes in cost savings over time and identify periods
of higher or lower financial impact.
Cost saved by skill
This area of the dashboard displays a bar chart showing the total cost saved by
each skill in the selected time range. Use this visualization to identify which skills are
generating the greatest cost savings across your organization.
Cost saved by AI Agent
This area of the dashboard displays a bar chart showing the total cost saved by
each AI agent in the selected time range. Use this visualization to compare cost
savings across AI agents and identify your highest-value deployments.
Cost saved by Agentic Workflow
This area of the dashboard displays a bar chart showing the total cost saved by
each agentic workflow in the selected time range. Use this visualization to evaluate
the financial value delivered by your agentic workflow configurations.

### Executions

The Executions section displays the total number of executions for each AI asset type, shown as
a monthly trend and broken down by individual asset over the selected time range.

> **[Screenshot: Cost Saved Section of Business Value Dashboard]**
>
> Close-up of "Cost saved" section with "Cost saved – Monthly trend" line chart (Dec 2025–Jun 2026, $0–$400, Skill line highest peaking ~$300 Jan 2026 then declining). Three bar charts: "Cost saved by skill" (AI agents ~$1000, AI Filter Assist near $0), "Cost saved by AI Agent" (Document ~$100, KB agents ~$50), "Cost saved by Agentic Workflow" (small values $0–$8.35).


Executions section of the Now Assist Center Business Value dashboard
Executions - Monthly trend
This area of the dashboard displays a trend line chart showing the total number of
executions for skills, AI agents, and agentic workflows each month over the selected
time range. Use the trend lines to monitor changes in execution volume across
asset types over time.
Executions by skill
This area of the dashboard displays a bar chart showing the total number of
executions for each skill in the selected time range. Use this visualization to identify
which skills are used most frequently and understand usage patterns across your
skill library.
Executions by AI Agent
This area of the dashboard displays a bar chart showing the total number of
executions for each AI agent in the selected time range. Use this visualization to
compare execution volumes across AI agents and identify your most actively used
deployments.
Executions by Agentic Workflow
This area of the dashboard displays a bar chart showing the total number
of executions for each agentic workflow in the selected time range. Use this
visualization to track which agentic workflows are running most frequently and
evaluate engagement patterns.

### Business value configuration

The Business value configuration table lists all configured AI assets and the values used to
calculate business value metrics. Use this table to review and manage the configuration for each
asset.

> **[Screenshot: Executions Section of Business Value Dashboard]**
>
> Close-up of "Executions" section. "Executions – Monthly trend" line chart (Dec 2025–Jun 2026, 0–25, peaking ~20 Feb 2026, three coloured lines). Three bar charts: "Executions by skill" (AI agents ~50, AI Filter Assist ~0), "Executions by AI Agent" (Document and vi... ~1, KB content creat... ~3, KB content cons... ~2, Search Q&A Agent ~1), "Executions by Agentic Workflow" (Identify ways ~10, Process emails ~6, Investigate probl ~2).


Business value configuration table in the Now Assist Center Business Value
dashboard
Asset type
The category of the AI asset, such as AI Agent, Skill, or Agentic Workflow.
Asset name
The name of the individual AI asset as configured in your instance.
Status
The current status of the AI asset, such as Active or Inactive.
Execution count
The total number of times the AI asset has been executed.
Average time saved (min)
The average amount of time, in minutes, saved per execution of the AI asset. This
value is used to calculate the total time saved metric.
Average hourly rate
The average hourly rate used to calculate the cost saved by the AI asset. This value
represents the estimated cost of the time saved per execution.
Total time saved (hrs)
The total amount of time saved by all executions of the AI asset, calculated from the
execution count and average time saved values.

### Total cost saved

The total cost saved by all executions of the AI asset, calculated from the total time
saved and average hourly rate values.

### Add a value configuration in the Now Assist Center Business Value dashboard

Add a value configuration to define the business value metrics calculated for an AI asset,
including average time saved per execution and average hourly rate.

### Before you begin

Role required: sn_na_center.nac_admin

### About this task

Value configurations define the data used to calculate business value metrics for each AI asset
on the Business Value dashboard. Each configuration specifies the asset, average time saved
per execution, and average hourly rate, which are used to calculate the total time saved and total
cost saved displayed on the dashboard.

> **[Screenshot: Business Value Configuration Table]**
>
> The "Business value configuration" table with count "10" and filter dropdowns "All asset ▾" and "All Records ▾", plus an "Add configuration" teal button. Columns: Asset type, Asset name, Status, Execution count, Average time saved (min), Average hourly rate (USD), Total time saved (hrs), Total cost saved (USD), and a ⋮ menu. Rows show 10 AI assets:
> - AI Agent | Document and visual insights AI agent | Active | 0 | 16 | 100 | 0 Hrs | $0
> - AI Agent | KB content creation AI agent | Active | 3 | 32.5 | 100 | 1.63 Hrs | $162.5
> - AI Agent | KB content consolidation AI agent | Active | 0 | 67.5 | 0 | 0 Hrs | $0
> - Skill | Incident summarization | Inactive | 14 | 1 | 1 | 0.23 Hrs | $0.23
> - Agentic Workflow | Identify ways to improve service | Active | 0 | 67.5 | 0 | 0 Hrs | $0
> - Agentic Workflow | Process emails for tasks | Active | 0 | 8 | 0 | 0 Hrs | $0
> - Skill | AI agents | Active | 80 | 1 | 1000 | 1.33 Hrs | $1333.33
> - Agentic Workflow | Investigate problems | Active | 0 | 75 | 0 | 0 Hrs | $0
> - Skill | AI Filter Assist | Active | 0 | 12 | 20 | 0 Hrs | $0
> - AI Agent | Search Q&A Agent | Active | 0 | 10 | 0 | 0 Hrs | $0
> Pagination: showing 1-10 of 10.

