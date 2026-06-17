# Enable Now Assist Guardian for AI agents

_Source pages: 31–33 | Depth: 2_

---

<!-- page 31 -->
2. Enable Now Assist panel.
a.Navigate to Now Assist admin > Experiences.
b.Turn on the Panel option.
3. Access the AI Agent Studio.
a.Navigate to All > AI Agent Studio > Overview.
b.Review the available default (base system) agentic workflows.
4.Activate the default agentic workflows.
a.Select the agentic workflow that you want to use from the available default workflows.
b.Activate the workflow. The default workflows are set to read only and must be activated
before use.
The default (OOTB) agentic workflows include:
◦Generate resolution plans
◦Analyze incident trends
◦Classify tasks
◦Investigate IT problems
◦Process emails for tasks
5. Configure chat assistants.
a.Navigate to Conversational Interfaces > Assistants.
b.Determine which chat assistants can access your AI agents.
c.Complete the configuration wizards for Now Assist panel (NAP) or Now Assist Virtual Agent
(NAVA).
6.Configure LLM Connections (optional).
If using external LLM providers instead of the default OpenAI GPT-4.1:
a.Navigate to Now Assist admin Console > Settings > Manage Integration.
b.Configure API credentials for your chosen LLM provider.
Note: The default Orchestration layer uses OpenAI GPT-4.1 5.4 on ServiceNow-
managed Azure servers.
7.Test the default AI agents.
a.Navigate to AI Agent Studio > Testing > Test AI reasoning.
b.Verify that the orchestrator canvas displays agent execution properly.
c.Review AI agent decision logs to confirm interactions and thought processes are recorded.
Enable Now Assist Guardian for AI agents
Identify and block offensive messages that are sent by human agents automatically by enabling
Now Assist Guardian in AI agents. With this capability, you can help reduce your agentic workflow
or test from being exposed to harmful content.
Before you begin
Role required: admin

<!-- page 32 -->
About this task
The Now Assist Guardian, which is a ServiceNow AI Platform capability in the Now Assist panel,
is a set of guardrails that are designed to intercept and mitigate offensive, sensitive, or security-
related issues that may arise during interactions with the Now Assist application.
For example, let's say that Now Assist Guardian detects an offensive message in the execution
plan of an agentic workflow. When you try to trigger the plan or test it, Now Assist Guardian can
step in to terminate the plan or test because it detected harmful content at the first step of the
execution plan.
For more information about the different guardrails, see Now Assist Guardian.
Procedure
1.Configure Offensiveness for AI agents.
a.In AI Agent Studio, navigate to the Settings tab.
You’re directed to the Offensiveness page.
b.Turn on the Offensiveness setting for AI agents by using the toggle button.

<!-- page 33 -->
c.Configure the detection impact by selecting the options icon ( ) to enable the detection
impact to use the following options:
▪Edit: Choose the detection impact between logging or both blocking and logging.
Enable the detection impact:
i. Select the Edit option.
ii.On the Detection impact page, select either the Log or Block and log button based on
your requirements.

> **[Screenshot: Now Assist Guardian — execution plan with offensive message detection]**
> A split three-panel screenshot showing: Left panel — the AI Agent Studio guided setup wizard with a description of the use case (Workforce Management and Resource Allocation). The "Describe the use case" step is active. Text areas show a list of steps. One text box is highlighted in amber/orange with label "Offensive message". Centre panel — a simplified flow diagram showing a node labelled "Terminated execution plan due to offensive message detection." with a "Task Start" box and "End" node. Right panel — "AI agent decision logs" panel.
>
> **[Screenshot: AI Agent Studio Settings – Offensiveness page (OFF state)]**
> Settings tab showing breadcrumb "Settings > Now Assist Guardian: Offensiveness". Title "Offensiveness". Description text about detecting offensive material. A toggle row: "Offensiveness OFF" with a grey/disabled toggle. Text: "Offensiveness is turned off." Right sidebar: Helpful resources with three links, FAQs with three expandable items.