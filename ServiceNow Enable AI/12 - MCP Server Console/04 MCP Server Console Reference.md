# MCP Server Console Reference

_Source: ServiceNow Now Assist documentation, pages 1050-1053._

## Overview

Reference topics for MCP Server Console include information about MCP Server Console roles, tables, supported Now Assist skills, and the procedure to create an AI Access Control List (ACL).

## Features

- A documented subset of Now Assist skills that can be used as MCP tools, plus two preconfigured as tools.
- A defined set of user roles installed with the application (administrator, tools administrator, viewer).
- A set of tables installed with the application for tool definitions and inputs.
- A procedure for creating the AI ACL required for external invocation of components.

## Functionalities

### Now Assist skill support in MCP Server Console

MCP Server Console supports creating tools for MCP servers from a subset of Now Assist skills.

**Preconfigured as tools in MCP Server Console:**

- Case summarization
- Incident summarization

**Additional Now Assist skills** that you can create tools from (or from custom skills created with Now Assist Skill Kit). Only Now Assist skills that don't rely on internal information as inputs, such as `sys_id`s, are available to be created as tools. Some Now Assist skills don't currently meet the criteria required to be used as tools. For more information, contact your ServiceNow representative.

- Analyze the CMDB Search request
- Change request risk explanation
- Code Assist AutoComplete
- Code Assist Edit
- Code Assist Generation
- Common control objective creation
- Correlation insights generation
- Customer Service Summary
- Docs summarization in Collaborative Work Management
- Duration to Days convertor
- EAP doc summarization
- Error resolution recommendation
- Feedback summarization
- Flow generation
- Invoice Inquiry solution generator skill
- Multi feedback summarization
- Playbook Generation
- Playbook generation with images
- Policy Based HR Case Evaluator
- Problem investigator skill
- Project doc summarization
- Recommend preferred solution for VIT
- Refine content
- Regulatory alert impacted citations
- Regulatory alert impacted control objectives
- Regulatory alert impacted controls
- Relevant invoice finder
- Resume Skill Extraction
- Skill keyword extractor
- Spoke Generation
- Subflows and actions
- Supplier recommendation
- Survey Filler Answer Suggestion skill
- Text2Test Sentinel
- Text2Test Skill
- Vulnerable item deduplication

**Related topics:** Create a tool for a Model Context Protocol server; Now Assist skills; Now Assist Skill Kit.

### Components installed with MCP Server Console

Several types of components are installed with activation of the MCP Server Console application, including tables and user roles.

#### Roles installed

| Role | Description | Contains roles |
| --- | --- | --- |
| MCP Server administrator `[sn_mcp_server.admin]` | Performs create, read, update, and delete (CRUD) operations on all MCP Server Console tables. | `sn_mcp_server.tools_admin` |
| MCP Server tools administrator `[sn_mcp_server.tools_admin]` | Performs create, read, update, and delete (CRUD) operations for tools. | `canvas_user`; `sn_nowassist_admin.user`; `web_service_admin` |
| MCP Server viewer `[sn_mcp_server.viewer]` | Invokes tools and views all MCP Server Console tables (read-only access). | `one_extend_viewer`; `canvas_user`; `sn_nowassist_admin.user`; `web_service_admin` |

#### Tables installed

| Table | Description |
| --- | --- |
| AI Skill Tool Definition `[sn_mcp_ai_skill_tool_definition]` | Tools based on Now Assist skills. Extends the Tool Definition table. |
| AI Skill Tool Input `[sn_mcp_ai_skill_tool_input]` | Inputs for tools based on Now Assist skills. Extends the Tool Input table. |
| Provisioned MCP Server `[sn_mcp_server_registry]` | MCP servers deployed on the instance. |
| Scripted REST Tool Definition `[sn_mcp_scripted_rest_tool_definition]` | Tools based on Scripted REST APIs that enable other tools. Extends the Tool Definition table. |
| Scripted REST Tool Input `[sn_mcp_scripted_rest_input]` | Inputs for tools based on Scripted REST APIs. Extends the Tool Input table. |
| Tool Definition `[sn_mcp_tool_definition]` | Tools defined for use by MCP servers. |
| Tool Input `[sn_mcp_tool_input]` | Inputs defined for use by MCP server tools. |

## Instructions / Procedures

### Create AI ACL

Create the necessary AI Access Control List (ACL) for the component to be called externally.

**Before you begin:** Role required: `admin`

> **Note:** An AI ACL is essential for ensuring security compatibility of the component, regardless of data types or execution logic. This approach embraces a proactive deny-by-default model.

**Procedure:**

1. Navigate to the navigation filter and enter **Access Control List**.
2. Select **New**.
3. Set the **type** to `flow_action`.
4. Set the **Operation** to `Invoked from AI`. This is the critical distinction. A standard record ACL will not work.
5. In the **Name**, paste the component's internal name (scope-qualified, e.g., `global.get_flow_description`). You can find this by publishing the component first, then checking the three-dot menu or the staging table.
6. Under **Requires Role**, add `sn_mcp_server.admin` (or the appropriate role for the MCP server user).

## Figures, Diagrams & Screenshots

**Figure (p.1050):** Two visuals.
1. Top: continuation of the AI agent example procedure (steps c-f from "Test the AI agent"), with a screenshot of the **Test an AI agent** configuration panel in AI Agent Studio. Visible fields include **Choose a test type** (set to "AI agent or workflow"), a field to select the AI agent and its version, and a **Task** field containing a sample prompt such as "Summarize all cases closed this week," with a **Continue to Test Chat Response** action.
2. Bottom: a larger screenshot showing the AI agent test result and its reasoning/execution flow. On the left is a chat/response panel with formatted text output (the agent's summaries of cases). On the right is an **AI agent reasoning** graph — a node-and-edge flow diagram depicting the agent's execution: a starting node branching through tool-invocation nodes (representing the MCP server tools being called, such as looking up case records and summarizing them) down to the final response, with status indicators on each node. This illustrates that the agent calls the server, the server runs the requested tools and returns JSON data, and the agent presents formatted text (in this example, summaries of cases closed by Abel Tuter in the past week). Below these visuals begins the "MCP Server Console reference" section text.

**Figure (p.1051):** Topic page for "Now Assist skill support in MCP Server Console." Plain text/bulleted content: the two preconfigured skills (Case summarization, Incident summarization) and a long bulleted list of additional supported Now Assist skills. No application screenshots or diagrams.

**Figure (p.1052):** Reference page continuing the list of supported Now Assist skills, then "Components installed with MCP Server Console." Contains the **Roles installed** table (MCP Server administrator, MCP Server tools administrator, MCP Server viewer with their descriptions and contained roles) and the start of the **Tables installed** table (AI Skill Tool Definition row). No screenshots; data tables and lists.

**Figure (p.1053):** Reference page with the remainder of the **Tables installed** table (AI Skill Tool Input, Provisioned MCP Server, Scripted REST Tool Definition, Scripted REST Tool Input, Tool Definition, Tool Input) followed by the "Create AI ACL" procedure (Before you begin, deny-by-default note, and numbered steps 1-6). No screenshots; tables and numbered text.
