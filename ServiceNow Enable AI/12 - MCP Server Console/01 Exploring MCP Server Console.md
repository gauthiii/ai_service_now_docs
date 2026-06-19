# Exploring MCP Server Console

_Source: ServiceNow Now Assist documentation, pages 1030-1032._

## Overview

MCP Server Console enables secure and governed access to functionality on a ServiceNow instance for AI applications with Model Context Protocol (MCP) servers. MCP servers extend ServiceNow AI Platform® functionality into any external MCP client and employee experience over the Model Context Protocol.

The Model Context Protocol defines a standard method of communication between large language models (LLMs) and external systems, such as a ServiceNow instance. AI applications connect to an external system from an MCP client, such as an AI agent, using an MCP server. The server tells the client which external resources it can access and how to access them. Then, from an MCP client, users can request information from the server and automate functionality using the available tools and data that the server returns. For general information about the Model Context Protocol and MCP terminology, see the Model Context Protocol documentation on the modelcontextprotocol.io website.

With MCP Server Console, you can:

- Create MCP servers on an instance and configure the tools that they expose, or use a preconfigured Quickstart Server.
- Define tools that determine which functionality and data a server exposes to clients and the actions that can be performed on an instance by clients.
- Create tools based on existing capabilities, such as Now Assist skills.

Any AI application, such as Microsoft Copilot or Claude, can call a server from a client using OAuth 2.0 authentication and get a list of available tools. With these tools, employees using MCP clients can prompt the server for information from the instance or to perform an action on the instance, such as to summarize a list of recently closed incidents or cases. You can also use the ServiceNow Model Context Protocol Client to let an AI application on one instance access tools from an MCP server on another instance.

The documentation provides a tutorial video (hosted on Vimeo) in which you can learn about the Model Context Protocol and how to create and use MCP servers with MCP Server Console.

## Features

The MCP Server Console landing page (Get started) provides four entry points:

- **Explore** — Learn about MCP Server Console.
- **Configure** — Create an MCP server and configure its tools.
- **Connect** — Call an MCP server from an MCP client.
- **Reference** — Get details about components installed with MCP Server Console.

Key capabilities highlighted on these pages:

- Creation of one or more MCP servers, each exposing different tools for different use cases or clients.
- A preconfigured Quickstart Server to help you get started.
- OAuth 2.0 authentication for secure client connections.
- Tools built on existing capabilities such as Now Assist skills.
- Cross-instance access using the ServiceNow Model Context Protocol Client.

### AI limitations

This application uses artificial intelligence (AI) and machine learning, which are rapidly evolving fields of study that generate predictions based on patterns in data. As a result, this application may not always produce accurate, complete, or appropriate information. There is no guarantee that this application has been fully trained or tested for your use case. To mitigate these issues, it is your responsibility to test and evaluate your use of this application for accuracy, harm, and appropriateness for your use case, employ human oversight of output, and refrain from relying solely on AI-generated outputs for decision-making purposes. This is especially important if you choose to deploy this application in areas with consequential impacts such as healthcare, finance, legal, employment, security, or infrastructure. You agree to abide by ServiceNow's AI Acceptable Use Policy, which may be updated by ServiceNow.

### Data processing

This application requires data to be transferred from ServiceNow customers' individual instances to a centralized ServiceNow environment, which may be located in a different data center region from the one where your instance is, and potentially to a third-party cloud provider, such as Microsoft Azure. This data is handled per ServiceNow's internal policies and procedures, including the policies available through the CORE Compliance Portal.

### Data collection

ServiceNow collects and uses the inputs, outputs, and edits to outputs of this application to develop and improve ServiceNow technologies including ServiceNow models and AI products. Customers can opt out of future data collection at any time, as described in the Now Assist Opt-Out page. For more information, see the Now Assist documentation.

## Functionalities

### MCP Server Console users

| User | Description |
| --- | --- |
| AI administrator | AI administrators can create MCP servers and configure which tools they expose to MCP clients. They also create OAuth inbound integrations on the instance for each client and configure clients with the server and authentication details. |

### Components and concepts referenced

- **MCP server** — Created on an instance; exposes tools to MCP clients.
- **MCP client** — An AI agent or AI application (for example, Microsoft Copilot or Claude) that calls a server.
- **Tools** — Define which functionality and data a server exposes to clients and the actions that can be performed on an instance by clients. Can be created from existing capabilities such as Now Assist skills.
- **Quickstart Server** — A preconfigured MCP server provided with MCP Server Console.
- **OAuth 2.0 authentication** — Used by AI applications to call a server from a client.
- **ServiceNow Model Context Protocol Client** — Lets an AI application on one instance access tools from an MCP server on another instance.

### MCP Server Console workflow

The page **"Managing MCP servers with MCP Server Console"** (p.1032) describes the end-to-end workflow an AI administrator follows:

1. As an AI administrator, you identify which functionality on an instance to access from an external MCP client and employee experience.
2. You can use the preconfigured Quickstart Server or create an MCP server with the appropriate tools to use the desired functionality. You can create one or more servers that expose different tools for different use cases, such as for HR or IT workflows, or for different clients.
3. If needed, you can create additional tools from Now Assist skills and configure which fields are exposed to clients and then add the tools to servers.
4. You create OAuth inbound integrations for each client to secure access to servers on an instance.
5. You configure clients to connect to a server using the server and OAuth inbound integration details. Then the client calls the server, which validates the OAuth token and responds with the list of tools available for use with the server.
6. Employees use clients, such as AI agents, to prompt the server for data from the instance or to perform an action on the instance.

> **Note:** With AI Gateway in AI Control Tower, AI administrators can monitor MCP server access and view metrics for servers and their tools. For more information, see *AI Gateway*.

### MCP Server Console benefits

| Benefit | Feature | Users |
| --- | --- | --- |
| Integrate with any AI application and MCP client using a standard protocol. | Create a Model Context Protocol server | AI administrator |
| Control which tools and fields are exposed to MCP clients. | Create a tool for a Model Context Protocol server | AI administrator |
| Securely access functionality from a ServiceNow instance in any external employee experience. | Configure an MCP client to connect to an MCP server | AI administrator |

## Instructions / Procedures

These overview pages do not contain numbered step-by-step procedures. They direct readers to the following topics for configuration and connection procedures:

- Configuring MCP Server Console
- Configure an MCP client to connect to an MCP server
- MCP Server Console reference

**Related topics:** Model Context Protocol Client.

## Figures, Diagrams & Screenshots

**Figure (p.1030):** "Get started" landing screen for MCP Server Console. Below the introductory text and an embedded Vimeo tutorial video (linked via a player URL), four square tiles are arranged in a 2x2 grid, each with a line-art icon: **Explore** (top left, magnifying-glass/discovery icon, captioned "Learn about MCP Server Console"), **Configure** (top right, gear/settings icon, "Create an MCP server and configure its tools"), **Connect** (bottom left, connection/plug icon, "Call an MCP server from an MCP client"), and **Reference** (bottom right, document/book icon, "Get details about components installed with MCP Server Console"). Below the tiles is the **AI limitations** legal/usage notice in small print, and the ServiceNow logo appears at the top. These tiles are navigational entry points.

**Figure (p.1031):** Continuation of the topic page showing the **Data processing** and **Data collection** notices, followed by the "Exploring MCP Server Console" heading, the "MCP Server Console overview" body text, the **MCP Server Console users** table (single row for AI administrator), and the start of the "MCP Server Console workflow" section. No screenshots; this is body text and one data table.

**Figure (p.1032):** Page titled **"Managing MCP servers with MCP Server Console."** The ServiceNow logo sits top-left and the bold section title is near the top; below a band of whitespace the page presents a **numbered workflow (steps 1-6)** describing the AI administrator end-to-end path (identify functionality to expose, create or use a server and its tools, optionally add Now Assist-based tools, create OAuth inbound integrations per client, configure clients to connect, and have employees use clients to query or act on the instance), followed by a **Note** callout about AI Gateway in AI Control Tower and the **"MCP Server Console benefits"** table (columns Benefit, Feature, Users -- three rows, all for the AI administrator). The full text is reproduced above under "MCP Server Console workflow" and "MCP Server Console benefits." This page was encoded with a malformed content-stream operator that the default PDF extractor (poppler) could not process, so both its text and visual were dropped on the first pass; it was recovered with an alternate render engine (pdfium/MuPDF). There is no separate diagram graphic -- the workflow is the numbered list itself.
