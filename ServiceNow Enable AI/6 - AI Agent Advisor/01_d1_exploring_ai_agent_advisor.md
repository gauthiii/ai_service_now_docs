# Exploring AI Agent Advisor

> **Source document:** AI Agent Advisor  
> **Pages:** 2–4


application has been fully trained or tested for your use case. To mitigate these issues, it is your responsibility to test and evaluate your use of this application for
accuracy, harm, and appropriateness for your use case, employ human oversight of output, and refrain from relying solely on AI-generated outputs for decision-
making purposes. This is especially important if you choose to deploy this application in areas with consequential impacts such as healthcare, finance, legal,
employment, security, or infrastructure. You agree to abide by ServiceNow’s AI Acceptable Use Policy , which may be updated by ServiceNow.

### Data processing

This application requires data to be transferred from ServiceNow customers' individual instances to a centralized ServiceNow environment, which may be located
in a different data center region from the one where your instance is, and potentially to a third-party cloud provider, such as Microsoft Azure. This data is handled
per ServiceNow's internal policies and procedures, including our policies available through our CORE Compliance Portal .

### Data collection

ServiceNow collects and uses the inputs, outputs, and edits to outputs of this application to develop and improve ServiceNow technologies including ServiceNow
models and AI products. In addition, this application will collect information extracted from documents. Customers can opt out of future data collection at any
time, as described in the Now Assist Opt-Out page.
For more information, see the Now Assist documentation.

### Exploring AI Agent Advisor

AI Agent Advisor automatically discovers automation opportunities in your instance and helps
you to deploy AI agents to implement them.

### AI Agent Advisor overview

AI Agent Advisor analyzes your instance data to identify the most frequent and impactful
opportunities for efficiency gains in your workflows. For each identified opportunity, it proposes
AI agents that can automate the solution, and generates new agents when no existing match is
available.
This gives the Now Assist administrator a data-driven starting point for AI adoption, eliminating
the guesswork of deciding where to apply automation.

### AI Agent Advisor users

The following table lists the primary users of AI Agent Advisor.

### Users

User Description
Now Assist Administrators
Now Assist administrators responsible
for organization-wide AI deployment and
management
Platform administrators
Platform administrators overseeing enterprise
AI governance
AI builders and practitioners
AI practitioners building and deploying custom
AI solutions across ServiceNow workflows

### AI Agent Advisor workflow

The following diagram shows the AI Agent Advisor workflow.

| User | Description |
| --- | --- |
| Now Assist Administrators | Now Assist administrators responsible for organization-wide AI deployment and management |
| Platform administrators | Platform administrators overseeing enterprise AI governance |
| AI builders and practitioners | AI practitioners building and deploying custom AI solutions across ServiceNow workflows |


### AI Agent Advisor workflow

AI Agent Advisor operates through three sequential phases:
Mine
The system analyzes the records in your instance (for example, incident and case
records) on a scheduled basis to identify recurring problems that are candidates for
automation.

> **[Diagram: AI Agent Advisor Workflow]**
>
> A vertical flowchart on a white background illustrating the three sequential phases of the AI Agent Advisor process. A legend at the top shows two node styles: solid blue rounded rectangles labelled "AI Agent Advisor action" and dashed green rounded rectangles labelled "User action". Large bold black phase labels appear on the left margin.
>
> **MINE phase (top section):**
> - Central blue box: "Analyze instance data" → branches right to two pale-blue sub-step boxes: "Select sample records" and "Analyze records to extract issues"
> - Downward arrow to blue box: "Identify automation opportunities" → branches right to four pale-blue sub-step boxes: "Identify common issues", "Cluster records by issue", "Refine, rank, and label clusters", "Generate resolution steps"
>
> **MATCH phase (middle section):**
> - Blue box: "Find available AI agents and tools" → branches right to two pale-blue sub-steps: "Examine resolution steps", "Search for matching AI assets"
> - Downward arrow to blue box: "Map AI assets to resolution steps" → branches right to three pale-blue sub-steps: "Identify strong matches for steps", "Identify partial matches for steps", "Identify steps with no matches"
>
> **MAKE phase (lower section):**
> - Blue box: "Create AI agents" → branches right to four pale-blue sub-steps: "Define objectives for new AI agent", "Generate AI agent", "Add tools to the agent", "Submit new AI agent for review"
> - Downward arrow to green box: "Implement automation opportunities" → branches right to three dashed-green user-action boxes: "Review automation opportunities", "Select automation opportunity", "Deploy AI agents"


You can configure the data sources, filters, and schedule to target the most relevant
records for your organization.
Match
For each identified opportunity, the system maps the resolution steps to existing AI
agents, tools, and agentic workflows already available on your platform.
Make
When no existing agent is a strong match for a resolution step, the system
generates a new AI agent tailored to that specific problem.
The result is a prioritized list of automation opportunities. Each opportunity displays the
estimated time and cost savings, number of records analyzed, and available AI assets. AI Agent
Advisor generates the resolution steps using the data from existing records on your instance. You
can use this list to decide which opportunities to act on first.

### AI Agent Advisor benefits

AI Agent Advisor provides the following benefits.

### Benefits of AI Agent Advisor

Benefit Feature User
Quickly discover automation Automation discovery with AI
opportunities for your Agent Advisor Now Assist administrator
instance. AI Agent Advisor
analyzes actual instance data
to identify and propose AI
automations that provide the
greatest efficiency gains.
Matches identified automation AI agent matching and
opportunities to existing AI automated deployment Now Assist administrator
agents on the platform and
AI developer
supports automated creation
and deployment of new
agents, shortening the path
from insight to action.

### What to explore next

To learn more about configuring and using AI Agent Advisor, see:
-Configuring AI Agent Advisor
-Using AI Agent Advisor
-AI Agent Advisor reference

### Supporting information for AI Agent Advisor

Get a quick overview of the important information that is related to the AI Agent Advisor
application.

### Supported versions

AI Agent Advisor v1.0 is supported starting with Australia general availability (Patch 2).

| Benefit | Feature | User |
| --- | --- | --- |
| Quickly discover automation opportunities for your instance. AI Agent Advisor analyzes actual instance data to identify and propose AI automations that provide the greatest efficiency gains. | Automation discovery with AI Agent Advisor | Now Assist administrator |
| Matches identified automation opportunities to existing AI agents on the platform and supports automated creation and deployment of new agents, shortening the path from insight to action. | AI agent matching and automated deployment | Now Assist administrator AI developer |
