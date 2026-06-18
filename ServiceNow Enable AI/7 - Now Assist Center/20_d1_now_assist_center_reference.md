# Now Assist Center reference

> **Source document:** Now Assist Center  
> **Pages:** 70–73



### Procedure

1.Navigate to All > Now Assist Center or Workspaces > Now Assist Center.
2. Select Business Value in the top navigation bar.
3. Select Add configuration.
The Add value configuration modal opens.
4.Select an Asset type.
5. Select an Asset name.
The Execution count (Last 7 days) field is automatically populated based on the selected
asset's execution history and is read-only.
The Currency field displays the currency configured for your instance. To change the currency,
update your instance configuration.
6.Enter a value in Average time saved per execution (min).
7.Enter a value in Average hourly rate.
The Total time saved (hrs) and Total cost saved fields are calculated automatically based on
the execution count, average time saved per execution, and average hourly rate values.
8.Select Add.

### Result

A Benchmark created successfully confirmation banner appears. The value configuration is
added to the Business value configuration table and the Business Value dashboard metrics are
updated to reflect the new configuration.

### Now Assist Center reference

The following topics provide additional information about the features and properties installed
with Now Assist Center.

### Components installed with Now Assist Center

Several components are installed with the Now Assist Center application.

### Roles installed

The following roles are installed with Now Assist Center.
- Now Assist Center admin [sn_na_center.nac_admin]
- Now Assist Center user [sn_na_center.nac_user]
For information on the roles installed with Now Assist Center, see Now Assist Center roles.

### Tables installed

The following tables are installed with Now Assist Center.

Now Assist Center tables
Label Name
AI Tool
nac_aitool
Navigation Item nac_navigation_item
Now Assist Center Promoted Skill nac_promoted_skill
Now Assist Center Promoted Skills State nac_promoted_skill_state

### Domain separation and Now Assist Center

Domain separation is supported for Now Assist Center.
Domain separation allows you to separate data, processes, and administrative tasks into logical
groupings called domains. You can then control several aspects of this separation, including
which users can see and access data.

### Support level: Basic

- Business logic: Ensure data goes into the proper domain for the application’s service provider
(SP) use cases.
- In the application, the user interface, cache keys, reporting, rollups, aggregations, and so on,
all use domain at production run time.
- The owner of the instance must be able to set up the application to function across multiple
tenants.
For more information on support levels, see Application support for domain separation .

### Domain separation uses in Now Assist Center

- The system supports domain separation for skills and instructions.
- Ability to view domain-based skills in the actionable use cases on the home page.
- Ability to duplicate skills for different domains.
- Now Assist Center analytics data contains records from multiple domains.

### Tables

The following Now Assist Center tables contain domain-separated fields:
- nac_promoted_skill
- nac_promoted_skill_state

### Fields

The following domain-separated fields are supported:
- sys_domain
Associates the state record with a specific domain.
- sys_domain_path

| Label | Name |
| --- | --- |
| AI Tool | nac_aitool |
| Navigation Item | nac_navigation_item |
| Now Assist Center Promoted Skill | nac_promoted_skill |
| Now Assist Center Promoted Skills State | nac_promoted_skill_state |

Manages domain hierarchy relationships.
- sys_overrides
Enables child domain state records to override parent domain states.

### Now Assist Center glossary

Before getting started with Now Assist Center, it is important to understand some key concepts
used in the application.
For more helpful terminology, see ServiceNow AI Platform glossary glossary.
agents
An agent, in the context of AI, refers to a software entity that can perceive its environment,
make decisions, and take actions to achieve specific goals. Agents can be simple or
complex, ranging from basic reactive systems to sophisticated entities that learn and adapt
over time. They are often used to automate tasks, interact with users, or manage complex
processes.
agentic system
An agentic system is a type of software or AI that perceives its environment, makes
decisions that are based on that perception, and takes actions to achieve specific goals,
often with minimal human intervention. An agentic system can learn, adapt, and operate
independently to solve problems or perform tasks.
agentic workflow
An agentic workflow is a structured sequence of tasks executed by one or more AI agents
with minimal human intervention to fulfill a business objective. You can create and manage
these workflows in AI Agent Studio by using triggers, tools, and evaluation plans, and
deploy across ITSM, HR, and CSM use cases.
Citation
Small, interactable number next to AI-generated content in the Now Assist panel that cites
the source of the information.
Now Assist
Refers to generative AI experiences on the ServiceNow AI Platform. With Now Assist, you
can improve productivity and efficiency in your organization with better self-service, faster
answers and recommended actions, and empower users to search more effectively.
To learn more about Now Assist, see Exploring Now Assist for Customer Service
Management (CSM) .
Now Assist skill
A predefined capability within Now Assist that uses generative AI to perform tasks such as
generating summaries, resolution notes, and so on.
Orchestrator
The AI agent orchestrator is a specialized agent that plans, coordinates, and manages the
execution of tasks across multiple AI agents. It holds short-term memory, tracks goals, and
ensures agents collaborate effectively. This component is central to Agentic AI architecture
and is configured in AI Agent Studio. The orchestrator conducts the planning and leads a
team of AI agents to address a given agentic workflow.

subflow
An automated process that consists of a sequence of reusable actions and specific
data inputs that allow the process to be started from a flow, subflow, or script. Subflows
automate generic business logic that can be applied to multiple applications or processes.
topic
A blueprint that defines the dialog between Virtual Agent and a user to accomplish a goal.
A topic has topic properties and a topic flow.
virtual agent
A conversational bot platform that provides user assistance through conversations in a
messaging interface.

### Now Assist Center roles

Now Assist Center is installed with these roles.

### Now Assist Center admin [sn_na_center.nac_admin]

Use the Now Assist Center workspace to access and set up Now Assist solutions, perform
administrative tasks, and monitor performance. This role has full access to the Now Assist Center
application, and can access Now Assist Center tables.

### Contains Roles

List of roles contained within the role.
- sn_data_kit.admin
- sn_na_center.nac_user
- sn_agent_miner.app_ui
- sn_aia.admin
- sn_nowassist_admin.nsa_admin

### Groups

None.

### Special considerations

None.

### Now Assist Center user

Perform read actions in Now Assist Center workspace.

### Contains Roles

List of roles contained within the role.
- sn_nowassist_admin.user
- sn_data_kit.analyst
- now_assist_panel_user
