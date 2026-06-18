# Connecting to an MCP Server from an MCP Client

_Source: ServiceNow Now Assist documentation, pages 1044-1049._

## Overview

Connect to a Model Context Protocol (MCP) server from an MCP client by creating an OAuth inbound integration and configuring the client with the server details.

With the Quickstart Server or after creating a server, you can complete the following steps to connect to a server from a client:

1. Create an OAuth inbound integration for an MCP client.
2. Configure an MCP client to connect to an MCP server.

The process to configure a client to connect to a server depends on the client used. For more information, refer to the documentation for your AI application and client.

## Features

- Secures access to MCP servers on an instance with OAuth inbound integrations (one per client).
- Supports any standards-conforming MCP client (such as Microsoft Copilot or Claude).
- Provides a complete set of server connection details (URLs, scope, identity provider, client ID/secret) for client configuration.
- Supports cross-instance connections using the ServiceNow Model Context Protocol Client (an AI agent on one instance accessing a server on another instance).
- Returns tool results to the client as JSON data, which the client presents as formatted text.

## Functionalities

### Roles required

- **Create an OAuth inbound integration:** `oauth_admin`, `mi_admin`, `admin`
- **Configure an MCP client to connect to an MCP server:** none
- **Example (cross-instance with ServiceNow Model Context Protocol Client):** `sn_mcp_client.admin`

### Inbound integration form (OAuth - Authorization code grant)

| Field | Value |
| --- | --- |
| **Details section** | |
| Name | Enter a name for the OAuth integration. |
| Redirect URLs | Enter the redirect URL for a client. The authorization code is sent to this URL after authentication. To get the redirect URL, refer to the documentation for your AI application and client. To connect to the ServiceNow MCP client on another instance, use the following redirect URL: `https://<client-instance>.service-now.com/oauth_redirect.do`. For more information, see the Model Context Protocol Client documentation. |
| **Auth scope section** | |
| Allow access only to APIs in selected scope | Clear the check box to make the OAuth integration broadly scoped. |
| **Advanced options section** | |
| Token Format | Select **JWT**. |

After saving, the OAuth inbound integration is created as broadly scoped with a **client ID** and **client secret** that you use when configuring the client to connect to servers on the instance.

### Server details for MCP client configuration

| Server details | Value |
| --- | --- |
| Server URL | `https://<server-instance>.service-now.com/sncapps/mcp-server/mcp/<server-name>`. To connect to the preconfigured Quickstart Server, use `https://<server-instance>.service-now.com/sncapps/mcp-server/mcp/sn_mcp_server_default`. |
| Host | `<server-instance>.service-now.com` |
| Base URL | `/sncapps/mcp-server` |
| Scope | `mcp_server` |
| Authentication type | OAuth 2.0 |
| Identity Provider | Generic OAuth 2 |
| Authorization URL | `https://<server-instance>.service-now.com/oauth_auth.do` |
| Token URL | `https://<server-instance>.service-now.com/oauth_token.do` |
| Token Revocation URL | `https://<server-instance>.service-now.com/oauth_revoke.do` |
| Refresh URL | `https://<server-instance>.service-now.com/oauth_auth.do` |
| Redirect URL | `https://<server-instance>.service-now.com/oauth/callback` |
| Client ID | The client ID from the OAuth inbound integration on the server instance. |
| Client secret | The client secret from the OAuth inbound integration on the server instance. |

After configuring these details, the client calls the server with the `Authorization: Bearer <token>` header. If the token is validated by the server, the client receives the list of tools available for use.

### Add MCP server form (ServiceNow Model Context Protocol Client — first page)

| Field | Value |
| --- | --- |
| Name | Quickstart Server |
| Authentication Type | OAuth 2.1 |
| MCP server URL | `https://<server-instance>.service-now.com/sncapps/mcp-server/mcp/sn_mcp_server_default` |

### Add MCP server form (ServiceNow Model Context Protocol Client — second page)

| Field | Value |
| --- | --- |
| Client registration type | Manual Registration |
| Grant type | Authorization Code |
| Token authentication method | Client Secret Post |
| Client ID | The client ID from the OAuth inbound integration for the Model Context Protocol Client on the server instance. |
| Client secret | The client secret from the OAuth inbound integration for the Model Context Protocol Client on the server instance. |
| Authorization URL | `https://<server-instance>.service-now.com/oauth_auth.do` |
| Token URL | `https://<server-instance>.service-now.com/oauth_token.do` |
| Token Revocation URL | `https://<server-instance>.service-now.com/oauth_revoke.do` |

### Add a Model Context Protocol Tool form (AI agent)

| Field | Value |
| --- | --- |
| Select Model Context Protocol server | Quickstart Server |
| Select tool | Select the tools from the Quickstart Server that you want to use with this AI agent. |

## Instructions / Procedures

### Create an OAuth inbound integration for an MCP client

**Role required:** `oauth_admin`, `mi_admin`, `admin`

**About this task:** For each client that you want to access servers on an instance, create an OAuth inbound integration in Machine Identity Console. To create the OAuth integration, you need a redirect URL from the client. For more information, refer to the documentation for your AI application and client.

**Procedure:**

1. Navigate to **All > MCP Server Console**.
2. From the **Configuration** tab, select **Servers**.
3. From the **OAuth setup required** banner, select **Set up OAuth**. Alternatively, you can navigate to **All > Machine Identity Console** and select the **Inbound integrations** tab.

   > **Note:** In the list of existing inbound integrations, you might see integrations created with the same names as servers (including underscores). These are integrations for monitoring servers from AI Control Tower and shouldn't be used to integrate with clients.
4. Select **New integration**.
5. Select **OAuth - Authorization code grant**.
6. On the form, fill in the required fields (see Inbound integration form above). For more information about this form, see *Configure an OAuth authorization code grant*.
7. Select **Save**. The OAuth inbound integration is created as broadly scoped with a client ID and client secret that you use when configuring the client to connect to servers on the instance.

**What to do next:** Configure the client to use the client ID and client secret to authenticate with servers on the instance.

### Configure an MCP client to connect to an MCP server

**Role required:** none

**About this task:** The process to configure a client to connect to a server depends on the client used. The following procedure is a high-level overview of the workflow to configure a client to call a server. For more information, refer to the documentation for your AI application and client.

**Procedure:**

1. Configure a client with the required server details as determined by the client (see Server details for MCP client configuration above).

   After configuring these details, the client calls the server with the `Authorization: Bearer <token>` header. If the token is validated by the server, the client receives the list of tools available for use.
2. From the client, you can view the list of tools available to determine how to prompt the server.
3. Enter a prompt for the information you need or for the tool to perform an action on the instance.

   For example, if the **Look up Incident Records** tool is available, you could enter "Get all open incidents." With the **Case summarization** tool, you could enter "Summarize all cases closed this week." The server runs the relevant tools and returns the result to the client as JSON data. The client presents the response as formatted text.

### Example: Connecting to an MCP server from ServiceNow Model Context Protocol Client

This example demonstrates how to connect to a server from an AI agent on another instance using the ServiceNow Model Context Protocol Client. First, you configure the client to call the preconfigured Quickstart Server. From an AI agent, you access the Quickstart Server's list of tools and add individual tools to the agent. Lastly, you test the agent in AI Agent Studio by providing a prompt and seeing the agent's response. For more information, see the Model Context Protocol Client documentation.

**Role required:** `sn_mcp_client.admin`

1. On the server instance, create an OAuth inbound integration for the ServiceNow Model Context Protocol Client. For more information, see *Create an OAuth inbound integration for an MCP client*.
2. On the client instance, navigate to **All > AI Agent Studio > Settings**.
3. Select **Manage MCP Servers**.
4. Select **New**.
5. Add the Quickstart Server. For more information about this step, see *Add an MCP server with OAuth 2.1*.
   - a. On the **Add MCP server** form, fill in the fields (first-page form above: Name = Quickstart Server, Authentication Type = OAuth 2.1, MCP server URL = the Quickstart Server URL).
   - b. Select **Next**.
   - c. On the form, fill in the fields (second-page form above: Client registration type = Manual Registration, Grant type = Authorization Code, Token authentication method = Client Secret Post, Client ID, Client secret, Authorization URL, Token URL, Token Revocation URL).
   - d. Select **Save**.
6. Verify the OAuth configuration.
   - a. Select **Authenticate**.
   - b. Select **Allow** to allow the client to connect to the server.
7. Add tools from the Quickstart Server to an AI agent. For more information about this step, see *Add an MCP server tool to an AI agent*.
   - a. In AI Agent Studio, select the **Create and manage** tab.
   - b. From the **AI agents** tab, select an existing agent or create one. For information about creating an agent, see *Create an AI agent*.
   - c. Select **Add tools and information**.
   - d. Select **Add tool > MCP server tool**.
   - e. On the form, fill in the fields (Add a Model Context Protocol Tool form above: Select Model Context Protocol server = Quickstart Server, Select tool = the tools you want to use).
   - f. Select **Add**.
   - g. Select **Save and continue**.
8. Test the AI agent. For more information about this step, see *Test an AI agent*.
   - a. In AI Agent Studio, select the **Testing** tab.
   - b. Select **Start manual test**.
   - c. In the **Choose a test type** field, select **AI agent or workflow**.
   - d. Select the AI agent you configured and its version.
   - e. In the **Task** field, enter a prompt to get information or to perform an action on the instance. The prompt should be based on which tools are available. For example, if you added the **Look up Case Records** and **Case summarization** tools, you can enter "Summarize all cases closed this week."
   - f. Select **Continue to Test Chat Response**.

   The AI agent calls the server, and the server runs the tools requested based on the prompt. The server returns the information to the agent as JSON data, and the agent presents it as formatted text. In this example, the agent returns summaries of the cases closed by Abel Tuter in the past week.

## Figures, Diagrams & Screenshots

**Figure (p.1044):** Two visuals.
1. Top: screenshot of the **Create a tool from a Now Assist skill** form (carried over from the previous topic) showing a top banner, the Basic information section (Category, Now Assist skill selector, Label, Description), and the "Add your tool to the existing MCP server" section with an Active toggle.
2. Below: the start of the "Connecting to an MCP server from an MCP client" topic text (no screenshot).

**Figure (p.1045):** Topic page for "Create an OAuth inbound integration for an MCP client." Contains the numbered procedure and the beginning of the **Inbound integration form** field table (Details section: Name, Redirect URLs; Auth scope section; Advanced options section: Token Format). No application screenshot on this page (text and table only).

**Figure (p.1046):** Screenshot of the completed **OAuth - Authorization code grant** inbound integration form in Machine Identity Console. The form header includes **Cancel**, **Save**, and additional controls. Visible fields/sections include a **Name** field, **Auth Type**, an **Application** field, **Redirect URLs**, and an **Active** toggle. This illustrates step 6-7 (filling in and saving the OAuth integration). Below the screenshot the page continues into "Configure an MCP client to connect to an MCP server" and the start of the **Server details for MCP client configuration** table.

**Figure (p.1047):** Continuation of the **Server details for MCP client configuration** table (Base URL, Scope, Authentication type, Identity Provider, Authorization URL, Token URL, Token Revocation URL, Refresh URL, Redirect URL, Client ID, Client secret) followed by the start of the "Example: Connecting to an MCP server from ServiceNow Model Context Protocol Client" section. No application screenshot; reference table and body text.

**Figure (p.1048):** Topic page showing the example procedure steps 2-6, including the two **Add MCP server form** tables (first page: Name, Authentication Type, MCP server URL; second page: Client registration type, Grant type, Token authentication method, Client ID, Client secret, Authorization URL, Token URL, Token Revocation URL). No application screenshot; numbered steps and tables.

**Figure (p.1049):** Two visuals.
1. Top: continuation of the example (steps a-d and the **Add a Model Context Protocol Tool** form table: Select Model Context Protocol server = Quickstart Server, Select tool).
2. Middle: screenshot of the **Add a Model Context Protocol Tool** modal in AI Agent Studio. It includes the text "An AI agent uses a MCP server tool to interact with external data sources and external tools." Below, a **Select Model Context Protocol server** dropdown shows "Quickstart Server," and a **Select tool** dropdown is expanded showing a searchable list of Quickstart Server tools — `case_summarization`, `incident_summarization`, `look_up_case_records`, and `look_up_incident_records` — each with a short description and an "in production" status indicator. This illustrates selecting MCP server tools to add to an AI agent.
