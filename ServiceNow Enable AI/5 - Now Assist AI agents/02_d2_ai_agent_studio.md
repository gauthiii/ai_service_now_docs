# AI Agent Studio

_Source pages: 6–10 | Depth: 2_

---

<!-- page 6 -->
panel. To learn more about an AI agent Orchestrator is, see the Understand the Now Assist AI
agents.
AI Agent Studio
Create, manage, or test AI agents and agentic workflows so that you can create self-executing
workflows to help you achieve your business goals.
https://player.vimeo.com/video/1096896405?
h=81ff7b3861&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479
AI Agent Studio overview
With the AI Agent Studio application, you can create, manage, or test AI agents and agentic
workflows all in one place. To enable the agentic AI experience, you must first install Now Assist
AI agents. For more information, see Install Now Assist AI agents.
The Overview page has three sections where you can find the information that you must
understand, begin, and continue developing AI agents and agentic workflows. When you first go
to the AI Agent Studio, tour points are available to guide you through the experience.
In the Ready-made agentic workflows and AI agents section, you can find the templates and
ready-made AI agents and agentic workflows that you can incorporate as-is or in custom
workflows that you create. You can even explore more templates to find the ones that best fit your
needs.
In the Recent agentic workflows and AI agents activity section, you can find the agentic
workflows or AI agents that have been created or configured most recently. On both List views,
you can create, duplicate, or delete agentic workflows or AI agents. The tab also includes a
link to the AI Agents Dashboard where you can review the details about AI agent usage and
performance.
The third section is a card to open a modal with a journey checklist that describes the steps to
incorporate the AI agents into your workflows successfully and a video that provides an overview
of the AI agents and workflows to get you started. Select View steps to open this section.
The following example shows the Overview page of AI Agent Studio.

<!-- page 7 -->
AI Agent Studio overview page
Managing agentic workflows and AI agents
From the AI Agent Studio Create and manage page, you can create, duplicate, or manage the
existing agentic workflows and AI agents. This page has two tabs, one for agentic workflows
and one for AI agents. You can edit the columns of the List view to change what information is
displayed. You can also search or filter the Lists to find the agentic workflows and AI agents that
you're looking for quickly. By selecting the name of the agentic workflow or AI agent, you can
open Guided Setup to configure or reconfigure the agentic workflow or AI agent.
The following example shows the AI Agent Studio create and manage page after several Now
Assist applications are installed.
AI Agent Studio Create and manage page
Agentic AI activity
The activity page contains execution logs for both agentic workflows and AI agents. The list
allows you to filter based on various fields, including the version. For more information on
creating multiple versions of the List of steps field, see Version control for AI agents and
agentic workflows.

<!-- page 8 -->
The following example shows several execution logs in AI Agent Studio.
AI Agent Studio activity page
Testing agentic AI
From the AI Agent Studio testing page, you can review the different tests for your AI agents and
agentic workflows, both manual and automated. You can test the performance of your agentic
AI by simulating a single execution manually, or you can use automated agentic evaluations for
testing multiple executions. Single tests are best for evaluating whether the AI agent or agentic
workflow does what you expect it to. Agentic evaluations are better at finding underlying patterns
and trends that may not be noticeable one execution at a time.
Note: The testing feature does not support the Now Assist panel assistance for live
agent interactions. To connect to a live agent, use Now Assist in Virtual Agent instead.
Otherwise, during live agent chat sessions, requester and agent users may be logged out
unexpectedly due to sessions expiring prematurely.
There are two types of manual tests you can do: AI agent or agentic workflow to
test execution or Test access to test security controls. You can view your executed tests in
the two tabs of the testing page. For manual execution tests, you can select the reply button to
repeat the test. You can open the full details page of an automated test by selecting the test's
name in the list in the Automated tab.
The following example shows the inputs for a Generate Resolution Plan agentic workflow testing
setup of AI Agent Studio.

<!-- page 9 -->
AI Agent Studio testing page
AI Agent Studio testing execution
AI Agent Studio settings
From the AI Agent Studio Settings page, you can enable Now Assist Guardian for your AI agents.
By using Now Assist Guardian, you can configure:
•Offensiveness detection
•Prompt injection attempt decision
•Long-term memory for AI agents
The following image shows the AI Agent Studio settings.

<!-- page 10 -->
AI Agent Studio settings page
AI Agent Analytics dashboard
From the AI Agent Analytics dashboard, you can review the vital statistics about your AI agents
and agentic workflows. You can see the data about the number of agents and agentic workflows
used, time-to-resolution efficiency gain, and the number of executions.
The following example shows the overview page for the AI Agent Analytics dashboard.

> **[Screenshot: AI Agent Studio overview page]**
> Full-width screenshot of the AI Agent Studio overview page. Navigation bar shows "servicenow" logo, All, Favorites, History, Workspaces, Admin, and centred "AI Agent Studio ★" badge with search bar and icons. Secondary tab bar: Overview (active underlined), Create and manage, Testing, Settings. Top-right button: "Manage evaluation runs ↗".
>
> Page title "AI Agent Studio" with subtitle "Create, manage, and monitor agentic workflows and the AI agents working across your organization." An animated graphic with nodes/connections appears at top right. A "Preview" badge with "Introduction to agentic AI" video thumbnail and "Take tour / View steps" buttons appear on the right.
>
> "Ready-made agentic workflows and AI agents" section with "Explore all" button. Two visible AI agent cards: "Problem Investigator" – "The Problem Investigator Agent specializes in root cause identification, impact assessment, and remediation planning." and "Incident trends analyser" – "Analyses grouped incident data to identify recurring issues and root causes. Provides detailed, actionable recommendations using structured analyses."
>
> "Recent agentic workflows and AI agents activity" section with "View analytics ↗" link. Two tabs: "Agentic workflows" and "AI agents". List table with columns: Name, Description, AI agents, Date created. Four rows: "Investigate IT problems" (1 agent, 2025-02-10), "Suggest survey responses" (2 agents, 2025-02-10), "Analyze incident trends" (1 agent, 2025-02-19), "Analyze and improve services" (2 agents, 2025-02-19). "View all" link bottom-right.
>
> **[Screenshot: AI Agent Studio Create and manage page]**
> The "Create and manage" tab showing "Manage agentic workflows and AI agents" with subtitle and two tabs: "Agentic workflows" (selected with badge "8") and "AI agents". "New" teal button top-right. List columns: Name, Description, AI agents, Created by, Date updated, Date created. Four workflows listed: Investigate IT problems, Suggest survey responses, Analyze incident trends, Analyze and improve services, each with same metadata. Pagination showing "1 – 4 of 4", Records per page: 20.

> **[Screenshot: AI Agent Studio activity page — execution logs]**
> The Activity tab of AI Agent Studio showing "View agentic workflow and AI agent activity" with subtitle. "All executions 189" counter shown. Filter/refresh/settings icons top-right. Table columns: Created, Created by, State, State Reason, Run Type, Agentic workflow, AI Agent, Objective, Version, Replay. Seven rows visible:
> - 2025-06-24 04:14:37 | abel.tuter | Completed | | Testing | Default VA Workflow | (blank) | i want to add notes | V1 | ○
> - 2025-06-24 08:38:40 | admin | Completed | User has requested to end the conversati | Chat | Default VA Workflow | (blank) | incident_details: INC0009005 | (blank) | ○
> - 2025-06-25 09:40:53 | abel.tuter | Terminated | No Activity | Testing | (blank) | IT Ticket Agent | Create IT Ticket | (blank) | ○
> - 2025-06-25 03:42:54 | fred.luddy | Completed | | Testing | (blank) | KB content consolidation AI agent | consolidate article 0000010 try to prefix with KB | (blank) | ○
> - 2025-06-25 04:16:00 | admin | Completed | | Testing | Triage cases | (blank) | table is interaction and recordid is IMS0000002 | V1 | ○
> - 2025-06-25 01:39:28 | beth.anglin | Completed | | Testing | (blank) | Next Best Action Agent | Solve INC0009005 | (blank) | ○
> - 2025-06-25 03:01:15 | beth.anglin | Completed | | Testing | (blank) | IT Ticket Agent | Update incident INC00091021 | V1 | ○

> **[Screenshot: AI Agent Studio testing page]**
> The Testing tab. Title "Test how agentic AI performs." Subtitle "Give AI agents and agentic workflows real tasks to complete and see if they provide the expected results." Two side-by-side option cards: "Manual test" (icon with clock/settings) – bullet points: gain insight, view decision log, Good for: testing a single example. "Start manual test" teal button. "Automated evaluation" (icon with chart/arrows) – bullet points: assess performance at scale, aggregate results for task completion and tool choice accuracy, Good for: testing a pattern of behavior. "Start automated evaluation ↗" button.
>
> "Track test results" section with "Manual tests" and "Automated tests" tabs. Filter and refresh icons. Table columns: Created, Created by, State, State Reason, Agentic workflow, AI Agent. Two rows: 2025-11-13 09:51:14 | abel.tutor | Completed | No Activity | (blank) | Incident Details Agent; 2025-11-13 11:36:04 | abraham.lincoln | Completed | (blank) | (blank) | Skill Details.
>
> **[Screenshot: AI Agent Studio testing execution detail — dual-panel view]**
> Split-screen view of a test execution in progress. Left panel shows breadcrumb "Testing Home > Test Details > Manual Test" and a vertical "steps" list: Created a plan, Started AI Agent 'Next action recommendation AI agent', Used the tool 'Get record details', Optimised results, Checking on remaining steps. A "Processing…" status with gear icon at bottom. Centre panel shows a flow diagram with nodes: Task Start (circle with target icon) → Orchestrator (gear/cog icon) → Next action recommendati… (AI Agent node) → Get record details (Tool node). Panel includes "Find on map ×" button and zoom/fit controls. Right panel shows "AI agent decision logs" with expandable entries: Access verification (Completed), Orchestrator (Completed), Gen AI – AIA ReAct Engine (Completed), Next action recommendation AI agent (Ongoing), Gen AI – AIA ReAct Engine (Completed), Tool – Get record details (Completed), Orchestrator (Queued). Green/amber/grey status badges.

> **[Screenshot: AI Agent Studio settings page — Now Assist Guardian Offensiveness]**
> The Settings tab of AI Agent Studio. Left sidebar navigation shows two sections: "Now Assist Guardian" (expanded, with sub-items: Offensiveness (selected/highlighted in blue), Prompt Injection, Long-term memory) and "External AI agents" (expanded, with sub-items: Discoverability, Data access, Manage MCP servers, Model provider). Main content area breadcrumb: "Settings > Now Assist Guardian: Offensiveness". Page title "Offensiveness". Description: "Detect and monitor content created with generative AI in conversational experiences that may include offensive material, such as toxicity, profanity, or sexism." A toggle row: "Offensiveness ON" with a blue toggle (enabled). Text: "Offensiveness is turned on for all AI Agents." A "Detection Impact" section shows "Log only" (current setting, shown as a dropdown/selector with a "⋮" menu). Right sidebar shows "Helpful resources" with links: Now Assist Guardian ↗, Now LLM Service model cards ↗, ServiceNow AI Forum ↗. FAQs section with three expandable items.