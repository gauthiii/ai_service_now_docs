# Configure Model Context Protocol Client

_Source pages: 264–278 | Depth: 2_

---

<!-- page 264 -->
making purposes. This is especially important if you choose to deploy this application in areas with consequential impacts such as healthcare, finance, legal,
employment, security, or infrastructure. You agree to abide by ServiceNow’s AI Acceptable Use Policy , which may be updated by ServiceNow.
Data processing
This application requires data to be transferred from ServiceNow customers' individual instances to a centralized ServiceNow environment, which may be located
in a different data center region from the one where your instance is, and potentially to a third-party cloud provider, such as Microsoft Azure. This data is handled
per ServiceNow's internal policies and procedures, including our policies available through our CORE Compliance Portal .
Data collection
ServiceNow collects and uses the inputs, outputs, and edits to outputs of this application to develop and improve ServiceNow technologies including ServiceNow
models and AI products. Customers can opt out of future data collection at any time, as described in the Now Assist Opt-Out page.
For more information, see the Now Assist documentation.
Explore Model Context Protocol Client
The Model Context Protocol (MCP) client in ServiceNow is a framework that allows AI agents,
such as large language models (LLMs), to interact with and manage ServiceNow instances. This
interaction takes place within a server-client architecture.
Model Context Protocol Client terminology
MCP host
The AI application environment where the tasks are initiated.
MCP client
Manages communication between the host and the MCP servers, handling the
requests and responses.
The MCP Client architecture enables AI agents to extend their capabilities by
invoking external systems dynamically, which enables tasks like accessing APIs,
databases, or file systems in a standardized way.
MCP server
Provides external functionalities by exposing tools for AI agents to use.
MCP tools
The external tools exposed by the MCP servers to be used by AI agents.
Why use MCP tools
MCP tools enable seamless integration to:
•Connect your AI agent with a wide variety of external tools with minimal setup.
•Add multiple MCP tools to an AI agent to perform a broader range of tasks.
•Review and edit tool input parameters as needed before saving.
Configure Model Context Protocol Client
Configure the MCP Client to execute agentic workflows with AI agents and mapped tools.
Configuring MCP Client enables you to:
•Incorporate external tools in AI agents built on ServiceNow.
•Access tools offered on external MCP servers.
•Integrate MCP Client with the AI Agent Studio.

<!-- page 265 -->
By setting up MCP servers, AI agents in your environment can leverage external tools efficiently,
enhancing their ability to perform complex tasks with up-to-date information.
Important: The Model Context Protocol Client application supports the latest Model
Context Protocol version, which is 2025-06-18. However, the latest version does not include
the support for PRM and Elicitation.
Install Model Context Protocol Client
Install the MCP Client application on your ServiceNow instance to enable using the tools from
the MCP server in AI agents.
Before you begin
The following must be completed:
•The Generative AI Controller plugin [com.sn.generative.ai] is installed.
Note: Installing the Generative AI Controller plugin enables AI Agent Studio and the
MCP Client on your instance.
•The latest version of the Now Assist AI Agents plugin [sn_aia].
•The sn_aia.enable_mcp_tool system property is set to true to enable the MCP tool
experience.
Note: ServiceNow AI Platform supports Protocol version 2025-06-18 of the MCP servers
for MCP Client.
Role required: sn_mcp_client.admin
Procedure
1.Navigate to All > System Definition > Plugins.
2. Search for the Model Context Protocol Client plugin [sn_mcp_client].
Add an MCP server in AI Agent Studio
An MCP server hosts the APIs and tools required by an AI application to receive and process
calls from MCP clients. The MCP server governs ingress traffic and promotes secure and efficient
access to tools. Adding an MCP server in the AI Agent Studio helps you to leverage the Model
Context Protocol as a tool for an AI agent.
Connecting an MCP server with the AI Agent Studio simplifies the integration process, making
it easier to discover and invoke services. This connection enhances security and governance,
providing a streamlined setup experience for administrators.
Note: To connect MCP servers with AI Agent Studio, you must have installed the Now
Assist AI Agents plugin [sn_aia] as a prerequisite.
Adding an MCP server requires you to add an MCP server in the AI Agent Studio. You can add an
MCPserver with one of the following authentication options:

<!-- page 266 -->
•OAuth 2.1: Add an MCP server with an authentication code. For more information, see Add an
MCP server with OAuth 2.1.
Note: You can configure an MID Server to connect with MCP Client by adding it as an
MCP server through OAuth 2.1 configuration and selecting the Use MID server check
box on the respective server's Connection and Credentials Aliases record. For more
information about connecting MCP Client with an MID Server through Connection and
Credentials Aliases, see Set up OAuth integration via MID Server .
•API Key: Add an MCP server with an API Key.
•Others: Add an MCP server manually by selecting a Connection and Credential Alias record.
Note: You must authenticate the users with the MCP server to add the MCP tool to an AI
agent. Without prior authentication, you can’t add the MCP servers.
Add an MCP server with OAuth 2.1
Add an MCP server with OAuth 2.1 in the AI Agent Studio.
Before you begin
Role required: sn_mcp_client.admin
About this task
OAuth is the standard method to authenticate MCP servers. If your MCP server supports it,
choose OAuth 2.1 as the authentication method.
Procedure
1.Navigate to All > AI Agent Studio > Settings.
2. Navigate to Manage MCP Servers and select New.
3. On the Add MCP server form, enter a name and the web address for your MCP server.
4.In the Authentication Type field, select OAuth 2.1.
5. Select Next.
The form extends with the registration details.
6.On the form, fill in the fields.
The Dynamic Client Registration form auto-populates the field data.

<!-- page 267 -->
Note: If dynamic registration is supported by the MCP server, you're prompted to
confirm the grant type and other inputs. If dynamic registration isn’t supported, you can
continue to the Manual Registration method.
Dynamic Client Registration form
Field Description
Grant Type How you want to obtain an access token
when accessing protected resources.
The following options are available:
◦Authorization Code: A system-generated
code used for granting access to an
application or resource.
◦Client Credentials: An access token
provided by the administrator to access the
application directly.
Token Authentication Method Method using which the client credentials
are sent when requesting tokens from the
Authorization server.
Auth Scopes Specific permissions for an application.
Note: The Auth scopes must be
comma-separated values.
Authentication Token for Client Registration Authentication token used to verify the
identity of the client and grant it permission
to register with an authorization token.
Provide the following values:
◦Header: Authorization header.
◦Value: Authentication password.
Authorization URL Web address of your server to direct
authorization.
Token URL Web address containing the token.
Token Revocation URL Web address to revoke the previously
provided token in the Authentication Token
for Client Registration field.

<!-- page 268 -->
The MCP server with dynamic client registration is added as a simple connection and
credential alias.
7.On the form, fill in the fields.
Note:
◦If your MCP server doesn’t support dynamic client registration, then you can register
the OAuth client for AI agents in your MCP server manually and update those client
details in AI Agent Studio.
◦The manual registration doesn’t auto-populate the field data and must be manually
provided.

<!-- page 269 -->
Manual Registration form
Field Description
Grant Type How you want to obtain an access token
when accessing protected resources.
The following options are available:
◦Authorization Code: A system-generated
code used for granting access to an
application or resource.
◦Client Credentials: An access token
provided by the administrator to access the
application directly.
Token Authentication Method Method using which the client credentials
are sent when requesting tokens from the
Authorization server.
Client ID Unique ID for authentication and
authorization purposes.
Client Secret Unique credentials used for authentication.
Auth Scopes Specific permissions for an application.
Note: The Auth scopes must be
comma-separated values.
Authentication Token for Client Registration Authentication token used to verify the
identity of the client and grant it permission
to register with an authorization token.
Provide the following values:
◦Header: Authorization header.
◦Value: Authentication password.
Authorization URL Web address of your server to direct
authorization.
Token URL Web address containing the token.
Token Revocation URL Web address to revoke the previously
provided token.

<!-- page 270 -->
8.Select Add.
You're redirected to the MCP Server record to authenticate the MCP server for adding an MCP
tool to an AI agent.
9.Select Authenticate.

<!-- page 271 -->
10.In the third-party authorization page, select Authorize.
Note: When OAuth access or refresh tokens aren’t available, you must authenticate the
OAuth configuration on the MCP server record to add it as an AI agent tool.
Add an MCP server with an API key
Add an MCP Server with an API Key in the AI Agent Studio.
Before you begin
Role required: sn_mcp_client.admin
Procedure
1.Navigate to All > AI Agent Studio > Settings.
2. Navigate to Manage MCP Servers and select New.
3. In the Authentication Type field, select API Key.
4.On the form, fill in the fields.
Add MCP Server
Field Description
Name Name for your MCP server.
MCP Server URL Web address of your MCP server.
API Key Unique code or password to identify and
authenticate the user or application when
accessing the API.
Note: The API key adds a connection
alias dynamically at runtime and maps
with the MCP server.

<!-- page 272 -->
5. Select Add.
Result
An MCP server with the name you provided appears in the list of MCP servers.
Add an MCP server with a connection and credential alias record
Add an MCP server by selecting a connection and credential alias record.
Before you begin
A connection and credential alias record must be created.
For more information, see Create a Connection & Credential alias .
Role required: sn_mcp_client.admin
About this task
For authentication methods not supported in an MCP server, you can use the connection and
credential alias method to create the alias manually and then update it in the MCP server. To use
the OAuth-based authentication method, create the OAuth entity profile and then create the
connection and credential alias. For other authentication methods like API key, Basic Auth, AWS
Credentials, SSH Credentials, create the connection and credential alias directly.
Procedure
1.Navigate to All > AI Agent Studio > Settings.
2. Navigate to Manage MCP Servers and select New.
3. In the Authentication Type field, select Others.
4.On the form, fill in the fields.

<!-- page 273 -->
Add MCP Server form
Field Description
Name Name for your MCP server.
Connection and credential alias Select a connection and credential alias
record to map with your MCP server.
5. Select Add.
Note: If a message appears that requires you to authenticate the MCP server, follow the
message prompt.
Result
An MCP server with the name you provided appears in the list of MCP servers.
Add an MCP server tool to an AI agent
Add a Model Context Protocol (MCP) tool to an AI agent in the AI Agent Studio so your users can
access the MCP server.
Before you begin
Role required: sn_aia.admin
Procedure
1.Navigate to All > AI Agent Studio > Create and manage > AI agents.
2. Open the AI agent to which you want to add an MCP tool to and navigate to the Add tools and
information section.
3. In the Add tool drop-down list, select MCP server tool.
4.On the form, fill in the fields.

<!-- page 274 -->
Add a Model Context Protocol Tool form
Field Description
Select Model Context Protocol Server The MCP server that you want to add to the
tool.
Note: Verify that the MCP server is
authenticated before adding the MCP
tool to an AI agent. If the MCP server
isn’t authenticated, then you receive an
error message.
Select MCP server tools The tool that you want to add from the MCP
Server.
Select an MCP server tool to view inputs Various inputs for the selected MCP server to
tool.
The following inputs are available and are
subject to change based on the selected
MCP server tool.
◦Query: Represents the search query with
data type as a string.
Note: The search query must not
exceed a maximum of 400characters
or 50 words.
◦Count: Represents the number of results
with data type as numeric.
Note: Results are displayed from 1 to
20 with the default value as 10.
◦Offset: Represents the pagination with
data type as numeric.
Note: The pagination offset must not
exceed a maximum of 9 pages with
the default value as 0.
Name Name of the MCP tool.
Tool and Description Description of the MCP tool and how it can
assist your AI agent.
Note: This description is sent to the
large language model (LLM).
Execution Mode Mode of execution for your selected MCP
tool. Choose from the following options:

<!-- page 275 -->
Field Description
◦Supervised: Requires input from a human
agent are required during the execution of
this MCP tool while the AI agent runs.
◦Autonomous: Doesn't require any input
from a human agent during the execution
of the MCP tool while the AI agent runs.
Display output Option to display the execution output in the
Now Assist panel or in Virtual Agent.
If you want the AI agent to work in Off Glide
architecture with Premium Chat experience,
you must turn-on the Display output toggle.
When the toggle is turned-on, you can add
widgets that can be used in assistants built
with Premium Chat experiences. The widget
configuration includes:
◦Widget: Defines the display output
to render the content in a better user
experience. You can select the widget from
the drop-down.
◦Require widget transformation: An
additional LLM call is required to transform
the raw tool. If you choose to skip this
transformation step, the tool output will be
directly mapped to the widget.
▪Yes
▪No
◦Display refined widget message: Refines
the widget message when configured.
▪Yes
▪No
Note: The display output as a
toggle is exclusively available for the
Premium Chat experience when the
Off Glide Conversation Server plugin
(com.glide.cs.offglide) is installed. If the
plugin is not installed, you will continue
to access the standard display output
options.
Advanced settings
Select an output transformation format Style for the LLM to present the results as
it passes information between tools and to
other agents. Out transformation formats:
◦None
◦Concise
◦Paragraph

<!-- page 276 -->
Field Description
◦Summary
◦Custom
Write processing messages for users Message to display to users during tool
execution.
◦In-progress message: Write an in-progress
message to be displayed to end-users
while the tool is running.
◦Completion message: Write a completion
message to be displayed to end-users
once the tool finishes running.
5. Select Add.
An MCP server tool is added in the Model Context Protocol Tools list on the Add tools and
information page.
Test an AI agent
Analyze the performance of an AI agent that has a Model Context Protocol (MCP) tool added to it
to verify that it functions the way you defined it.
Before you begin
Role required: sn_aia.admin
About this task
After you create an AI agent and add an MCP tool to it, test the AI agent to confirm that it
functions the way you defined it. Search for the AI agent, select the version, and provide a task
with a concise summary and a reference number to begin testing.
Procedure
1.Navigate to All > AI Agent Studio > Testing.
2. In the Test AI reasoning tab, search for and select the AI agent that you want to test.
3. In the Version drop-down list, select a version of the AI agent.
4.In the Task field, provide a concise summary of the task you want to achieve.
Note: In the task summary, include a reference number or specific record to achieve
results pertaining to a task your AI agent can perform.
5. Select Start test.

<!-- page 277 -->
You’re directed to the Chat responses tab, where you can see Now Assist executing
operations to test the AI agent.
6.Complete the testing by selecting Log in and authenticating the MCP server.
Note:
◦The Log in button is visible only if the server isn’t authenticated.
◦Enabling access to the MCP server refreshes the Testing page and resumes testing in
the Chat responses tab.
◦The OAuth token used for the authentication is saved in the OAuth Credentials table
[oauth_credential].
Model Context Protocol Client reference
Find more information about user roles, tables, and the different properties that are installed with
the Model Context Protocol Client application.
MCP Client roles
The following roles are installed with the Model Context Protocol Client plugin [sn_mcp_client].

<!-- page 278 -->
Roles used in MCP Client
Role Description
MCP Client Admin [sn_mcp_client.admin] Administrator of the application.
A user with the sn_mcp-client.admin role can
create, read, update, and delete records.
Note: The sn_aia.admin role contains
the sn_mcp_client.admin role, a role
inheritance on plugin activation.
MCP Client Viewer [sn_mcp_client.viewer] Read-only access to the application.
A user with the sn_mcp_client.viewer role has
read and report access on all tables.
Note: The sn_aia.viewer role contains
the sn_mcp_client.viewer role, a role
inheritance on plugin activation.
MCP Client system properties
The following system properties are installed with the Model Context Protocol Client plugin
[sn_mcp_client].
System properties used for configuring MCP Client
System property Description
sn_aia.enable_mcp_tool Enables access to the MCP Client tool on your
ServiceNow instance.
Default value: false
mcp_guardian_check Detects offensive content on the page, when
the display output of the tool is set to true and
output transformation strategy is null.
Default value: false
MCP Client tables
The following tables are installed by default with the installation of the Model Context Protocol
Client plugin [sn_mcp_client].
Tables used for configuring MCP Client
Table Description
MCP Execution Logs [sn_mcp_execution_logs] Lists the request and response, the method, a
tool call or list call, that was carried out along
with the mapped session.
The execution logs table also helps debug and
shows if there are any errors.

> **[Screenshot: Add MCP Server modal — OAuth 2.1 authentication]**
> A modal dialog titled "Add MCP Server" with X close button. Three form fields: "Name *" = "SNOW OAuth"; "Authentication Type *" = "OAuth 2.1" (dropdown showing value); "MCP Server URL *" = (redacted/blurred URL value) with pencil/edit icon. Footer: "Cancel" and teal "Next" buttons.