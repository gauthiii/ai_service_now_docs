# Explore Model Context Protocol Client

_Source pages: 264–264 | Depth: 2_

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