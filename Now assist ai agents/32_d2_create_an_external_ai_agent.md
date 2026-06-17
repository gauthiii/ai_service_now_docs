# Create an external AI agent

_Source pages: 112–120 | Depth: 2_

---

<!-- page 112 -->
Delete an AI agent
Delete an AI agent from AI Agent Studio if you no longer need it.
Before you begin
Role required: sn_aia_admin
About this task
You must assign appropriate permissions by using the access control lists (ACLs) to delete AI
agents on AI Agent Studio.
Note: You can't delete the AI agents that come installed with Now Assist applications.
Procedure
1.Navigate to All > AI Agent Studio > Create and manage > AI agents.
2. Select the check box of the AI agent that you want to delete and select Delete.
You can also delete multiple AI agents by selecting multiple AI agent records at a time.
Note: Some AI agents installed with Now Assist applications can't be deleted.
3. In the confirmation pop-up window, select Delete.
Result
The selected AI agents are deleted from the AI agents list in AI Agent Studio.
Create an external AI agent
Create external AI agents in AI Agent Studio to connect the ServiceNow AI Platform with third-
party agentic AI providers as primary agents.
Integrating external AI agents
Integrate and configure external agents with the ServiceNow agentic AI system using
Agent2Agent (A2A) protocol integration to use in agentic workflows created in the AI Agent
Studio.
External agent discovery on the ServiceNow AI Platform
You can enable external AI agents on the AI Agent Studio via the Settings
page. Navigate to AI Agent Studio > Settings > External AI agents >
Discoverability.

<!-- page 113 -->
•Allow ServiceNow to access External AI agents: Turn on the toggle to enable external AI
agents integration with the ServiceNow agentic AI system using the A2A protocol.
•Allow third-party to access ServiceNow AI agents: Turn on the toggle to enables integrating
ServiceNow AI agents into external agentic AI systems.
When creating a new external AI agent in AI Agent Studio, you can connect your agent to the
ServiceNow agentic AI system using the Agent2Agent (A2A) protocol integration. To do this, you
must have a Connection & Credential alias record that connects to your agentic AI provider.
After connecting to the external AI agent, you can add details about its role and instructions to
provide context for the AI Agent Orchestrator. Additional context helps differentiate your AI agent
from other AI agents so that the AI Agent Orchestrator can decide about which agent to use.
Contextual data access for external agents on the ServiceNow AI Platform
Enable contextual data access for external agents to improve AI agent response during
execution.
•Short-term memory: Turn on the toggle to enable external AI agents remember your
preferences or facts from the current interaction only.
•Long-term memory: Turn on the toggle to enable external AI agents remember your
preferences or facts from previous interaction.
•Knowledge graph for external AI agent interactions: Turn on the toggle to enable external AI
agents to use structured and unstructured data from different records across the ServiceNow
AI Platform.
Agent2Agent protocol overview
Agent2Agent (A2A) is an open standard that enables AI agents across different platforms to
communicate with each other. The standard relies on every AI agent having an Agent Card
associated with it that provides basic information for providers like the ServiceNow AI Platform,
Azure, and Google to use them.
Version 0.3 of A2A is supported.
An AI agent's Agent Card uses standardized JSON to help different providers understand its
capabilities. The Agent Card is accessed by a specific type of endpoint from a provider's server.
Execution plans are communicated through an execution endpoint so that both the provider's
server and the ServiceNow AI Platform can track what the external AI agent is doing.

<!-- page 114 -->
See Create an external AI agent with the Agent2Agent protocol for instructions for using this
protocol to create an AI agent.
Configuring A2A authentication
A2A connections require authorization from the source platform to execute on the ServiceNow
AI Platform. Authentication is established by creating two Connection & Credential Alias and
Connection records, one with an Agent Card endpoint and one with an execution endpoint.
Configuration Properties
The following properties configure different aspects of how your agents can interact with the
ServiceNow AI Platform.
External AI agent properties
Name Description
sn_aia.external_agents.enabled Set to true to enable external agent
features
sn_aia.external_agents.parallel_conversations.enabled Enables or disables multiple
simultaneous conversations per user
ServiceNow AI agents as secondary agents
Integrate ServiceNow AI agents into other agentic AI systems, such as Google Cloud or Azure
OpenAI.
Enabling discovery of ServiceNow mobile agents
In AI Agent Studio, on the Settings page, under External AI Agents > Discoverability, you can
enable the discovery of ServiceNow AI agents to use on other AI platforms. To do so, toggle
Allow third party to access ServiceNow AI Agents.
You can also choose between Synchronous and Asynchronous communication between your
external AI agent and the agentic AI provider.

<!-- page 115 -->
ServiceNow AI agents as secondary agents overview
You can connect your ServiceNow agent to other agentic AI model providers using the
Agent2Agent protocol.
After creating your AI agent in AI Agent Studio, you can direct to the Agent Card URL that is
displayed for secondary agents for easy access so the admins can view, copy, and consume the
URL.
The endpoint to direct to the actual execution of the AI agent is in the format
{{instance}}.service-now.com/api/sn_aia/a2a/v2/agent/id/{{agent-
id}}.
You can use the same OAuth or API key for authenticating the agent discovery and the agent
execution.
To verify that your AI agent is running from the ServiceNow side, during a conversation with the AI
agent, you can go to the Execution Plan [sn_aia_execution_plan] table. From the
Execution Plan table, you can identify the execution plan based on the Objective field that
contains the prompt from the conversation on the other platform.
For more information about sample payloads for Google A2A with ServiceNow AI agent as
Secondary agent, see Sample payloads for Google A2A .
For more information about setting up instructions for your ServiceNow AI agents as secondary
agents (acting as A2A server), refer to Authentication for Google A2A - ServiceNow as Secondary
Agent .
Asynchronous connection
Asynchronous connection involves communication where the sender and receiver don't have to
be active simultaneously unlike the synchronous communication mode.
To establish asynchronous connection, you must obtain a callback URL for push notifications to
function.
Once you have obtained a callback URL, you must create a record on the External Agent
Callback Registries [sn_aia_external_agent_callback_registry] table. Go to the table, select New,
and enter the callback URL. Save the record.
Once you save the record, a Connection & Credential Alias [sys_alias] record is created for you.
To add authentication, you can open the Connection record associated with the sys_alias record
and add a credential to the Credential field.
When the record is created, you can go back to the External Agent Callback Registry record you
created and select Verify URL to test the connection works as expected.
Create an external AI agent with the Agent2Agent protocol
Create external AI agents in AI Agent Studio to connect the ServiceNow AI Platform with third-
party agentic AI providers.
Before you begin
If you don’t see the option to create an external agent, confirm that your administrator has
selected Allow ServiceNow to access External AI Agents. This option is available on the
Settings page in AI Agent Studio, under External AI Agents > Discoverability.
Your instance must be at least on Zurich patch 4.
Role required: sn_aia.admin

<!-- page 116 -->
About this task
You can integrate third-party AI providers into the ServiceNow AI Platform by creating an external
AI agent in AI Agent Studio.
Procedure
1.Navigate to All > AI Agent Studio > Create and manage > AI agents.
2. Select New > External.
3. In the Discover and activate step, select the AI agent provider for your external agent and
discover your agent.
Select Save and continue to navigate to the next step.
a.Select an existing provider or add a provider.
If you select Add new provider, you must fill out the fields and then select Save.
Add provider form fields
Name Description
Name Name of the agentic AI provider.
Agent card URL The URL that points to the external AI agent's Agent Card. The
URL should include well_known/agent_json.
Under Advanced Credentials to access your external AI agent's Agent Card. You
settings, Connection & can select an existing alias or create one.
Credential alias
Under Advanced Subflow that establishes Agent2Agent protocol. The default
settings, Select subflow subflow should handle the majority of cases, but you can also
create your own.
b.Select Discover external AI agent to validate the connection to your external agent.
If discovery is successful, the name of your agent and the version number are added to the
page previous the Discover external AI agent button.

<!-- page 117 -->
c.Select the name of the agent to verify that the Name, Version, Description, and
Skills fields are populated correctly, then select Selected.
The Agent card tab shows the entire JSON for the agent.
4.In the Review skills and capabilities step, verify that the skill names are correct.
5. In the Define the specialty step, add details for how the external agent fits in the ServiceNow
agentic system.
a.Review your AI agent description.
You can leave your AI agent description as it is, or you can add a longer description to help
differentiate the agent from other AI agents. This helps enable the AI Agent Orchestrator to
use your external AI agent more effectively. For suggestions for writing AI agent descriptions,
see General guidelines for creating AI agents and agentic workflows.
b.Set your communication mode to either Synchronous or Asynchronous.

<!-- page 118 -->
Some agents don’t support asynchronous communication.
Under Advanced settings, you can use the default subflow, an existing subflow, or create a
subflow. The default subflow should work for the majority of cases.
c.Select your AI agent's execution Connection & Credential alias for authentication.
Choose which credentials access your external AI agent's execution endpoint. You can
select an existing alias or create one. If you create one, a modal fdisplays with options for
configuring an OAuth or API Key authentication.
Note: For more information about the API Key credential, see A2A API Key credential
behavior.
d. Configure access control lists (ACLs) for the AI agent.
Note: The ACLs determine who has access to discover and execute the AI agent.
To learn more about the ACLs you can create in AI Agent Studio and how to add more
advanced security configurations, see Implement access control in Now Assist AI
agents.
This is a required step. If you have previously configured an AI agent without creating an
ACL, you must generate an ACL before you can make other modifications.
Define who can access the AI agent
Field Description
User access The type of users whose access for the AI
agent is defined by the following options:
▪Any authenticated user: Any user who is
logged in can access the AI agent.
▪Users with specific roles: Users that have
at least one of the roles assigned to them
can access the AI agent. This option is the
default.

<!-- page 119 -->
Field Description
Note: If a user doesn't have access
to an AI agent or if the user doesn't
have access to at least one of the
AI agents in the respective agentic
workflow execution, then the whole
execution aborts before the first AI
agent is initiated.
▪Public: Any user can access the AI agent
even without logging in. Use this option
only when you want guests to be able to
access the AI agent.
Role Assign one or more specific roles from the
drop-down menu.
Note: Selecting the role is possible
only when you chose the Users with
specific roles user access.
6.In the Select a display step, choose where you want the AI agent to appear and what message
users see when the AI agent is running.
a.Select your AI agent's availability.
Set the Status to active if you want the AI agent to be available to users with the correct
role.
b.Select a display channel.
You can choose to use a Virtual Agent and specify which assistant you want to access the AI
agent. If you want to test the AI agent first, you don’t need to select a display channel yet.
c.Choose processing messages to display to the user when the AI agent is executing.
For example, Initiating AI agent or Processing record details, or An AI
agent is looking into the request.
d. Activate the AI agent.
Select the toggle to activate the AI agent if you want the AI agent to be discoverable. If you
want to test your AI agent first, wait until after you have tested it before activating it.
If you don't see this option, you may need to scroll.

<!-- page 120 -->
7.Select Save and test to save the AI agent details and go to the Testing page of AI Agent Studio.
Result
Your external AI agent is connected to ServiceNow.
What to do next
You can test an execution of your AI agent or its data access. You can also add it to a new or
existing agentic workflow. See Create an agentic workflow for the steps to create or configure an
agentic workflow.
A2A API Key credential behavior
Starting in Now Assist AI Agents 7.1.x, the header included in each A2A request is driven by the
API Key credential record and it is not injected automatically by the flow action.
Starting in Now Assist AI Agents 7.1.x, A2A flow actions no longer inject an Authorization:
Bearer header automatically. The header included in each request is now driven entirely by the
API Key credential record bound to the external agent's Connection & Credential Alias.
OAuth-based external agents, and API Key endpoints whose existing credential record already
aligns with the endpoint's expectations, are unaffected. You only need to act if your remote A2A
endpoint requires a specific header name or a scheme prefix.
Resolve 401 or 403 errors after upgrade
If your A2A endpoint returns a 401 or 403 after upgrading, update the API Key credential record
bound to your external agent.
1.Open the api_key_credentials record bound to your A2A external agent. Navigate to
the record via the Connection & Credential Alias on the external-agent provider.
2. If the endpoint requires a specific header name (for example, x-api-key instead of
Authorization), set the API Key Header (api_key_header_name) field to the header
name the endpoint expects.

> **[Screenshot: External AI agents – Data access settings for contextual data]**
> AI Agent Studio Settings page, Settings > External AI agents > Data access breadcrumb. Left sidebar shows: Now Assist Guardian, Long-term memory, External AI agents (expanded showing Discoverability, Data access (highlighted), Manage MCP servers, Model provider). Main content title "Contextual data". Description: "External AI agents can use different types of contextual data to improve their responses." Three toggle rows, all currently ON (blue): "Short-term memory ON" – "External AI agents can remember a user's preferences or facts from the current interaction only." "Long-term memory ON" – "External AI agents can remember a user's preferences or facts from previous interactions." "Knowledge graph for external AI agent interactions ON" – "External AI agents can use structured and unstructured data from different ServiceNow records."