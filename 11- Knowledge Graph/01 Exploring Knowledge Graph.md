# Exploring Knowledge Graph

_Source: ServiceNow Now Assist documentation, pages 973-990._

## Overview

The Knowledge Graph application uses the structured and unstructured data from ServiceNow records, knowledge bases, and external sources to enhance the performance of Now Assist Virtual Agent, AI agents, and generative AI skills.

Knowledge Graph provides a connected representation of data that maps entities and their relationships, adding context and meaning to information to enable intelligent search, insights, and AI-driven experiences. The ServiceNow Knowledge Graph application enhances the Now Platform by creating a semantic layer that connects data, relationships, and context across the enterprise. It structures information as a graph of entities and connections, bringing context and meaning to the available raw data. By leveraging AI, it powers personalized and intelligent experiences across the Now Assist ecosystem including NAVA (Now Assist Virtual Agent), AI Agents, and AI Search to deliver more relevant insights and automation.

By linking data and embedding semantic meaning, ServiceNow Knowledge Graph transforms raw data into actionable knowledge, fueling faster resolutions, richer insights, and more personalized AI-powered experiences.

This subtopic covers the Knowledge Graph overview, its components, the Knowledge Graph Designer, prebuilt integrations, users, benefits, how to access the Knowledge Graph schema, prebuilt integration with Now Assist Virtual Agent, Now Assist Panel and AI agents, natural language query use cases and examples, Workflow Data Fabric integration, and configuration item (CI) relationship support.

## Features

ServiceNow Knowledge Graph application provides the following capabilities:

- **Natural language queries:** Allow users to query structured ServiceNow data conversationally — for example, "Who is my manager?", "What's the status of my incident?", or "What assets are assigned to me."
- **User context:** Provide Now Assist Virtual Agent and AI Agents with contextual information such as role, department, or location to deliver personalized and relevant responses.
- **Slot-filling:** Simplify user interactions by automatically populating known information in forms or chat requests, reducing effort and friction.
- **Smarter AI Agents:** Empower agents to retrieve insights, facts, and relationships directly from the knowledge graph to automate actions and improve accuracy.
- **Integration with Workflow Data Fabric:** Use an integrated data layer that gives real-time, secure, and unified access to data from any source without duplicating it, enabling faster, data-rich workflows across the platform.

### Knowledge Graph benefits

| Benefit | Feature | Users |
|---|---|---|
| Enhance user experience (with prebuilt integration for downstream products like Now Assist Virtual Agent and Agentic AI) | Provides accurate data with minimal user effort. | Requester |
| Simple and easy to use | Creates a complex data model called Knowledge Graph schema with numerous entities and their relation within a few steps. | kg_admin |
| Easy to manage | Editing Knowledge Graph schemas to add new nodes or edges is simple. | kg_admin |
| Customizable Knowledge Graph schema | Provides an option to copy the ServiceNow Knowledge Graph schemas for customization. | kg_admin |
| Test a Knowledge Graph schema | Provides an option to test a Knowledge Graph schema by running a query. | kg_admin |
| Use Workflow Data Fabric to retrieve information without saving or copying them from the source entity. This ensures efficiency and security. | Leverage Workflow Data Fabric tables in Knowledge Graph to retrieve data. | Requester |
| Create a Knowledge Graph schema with Workflow Data Fabric tables. | To create and manage Workflow Data Fabric tables, see "Managing data fabric tables in Workflow Data Fabric Hub." | kg_admin |

## Functionalities

### Knowledge Graph components

ServiceNow Knowledge Graph is a graphical representation of real-world entities (tables) and their relationships, stored in a database. Each graphical representation is called a **Knowledge Graph Schema** that consists of relevant entities called **nodes**. The relationship between each entity is called an **edge**.

To create, edit, and manage Knowledge Graph schemas for specific use cases, ServiceNow Knowledge Graph has introduced the **Knowledge Graph Designer**.

Users can use these schemas to customize and extend Knowledge Graph integrations with Now Assist Virtual Agent, AI agents, and Now Assist Panel. ServiceNow also provides some prebuilt integrations that connect the Knowledge Graph with Now Assist Virtual Agent, AI agents, and other ServiceNow applications, enabling seamless AI-powered workflows and personalized experiences.

### Knowledge Graph Designer

Knowledge Graph Designer is a dedicated, no-code UI where Knowledge Graph administrators (kg_admins) can effortlessly:

- Design and manage Knowledge Graph schemas, and configure the related nodes (tables), properties (columns), and their relationships.
- Analyze results of the Knowledge Graph APIs integrated in downstream products by auditing the schema using natural language queries and achieved responses.

The Knowledge Graph Designer streamlines the entire process, from schema creation and data ingestion to performance monitoring and results analysis. The new approach confirms a scalable, flexible, and intuitive way for Knowledge modeling.

### Prebuilt Integrations

By unifying Knowledge across platforms and integrating with Now Assist, AI Search, AI agents, and skill kit, the prebuilt integrations of Knowledge Graph help the customer drive productivity, enhance decision-making, and unlock the full potential of enterprise data, while maintaining robust data governance and permission controls.

In this release, the available prebuilt integrations are:

1. **Integration with Now Assist Virtual Agent, Now Assist Panel and AI agents for User Context:** Helps users with personalized responses.
2. **Integration with Now Assist Virtual Agent and Now Assist Panel for Slot filling:** Helps pre-fill the slots for Virtual Agent topics using the Natural Language Querying feature of Knowledge Graph.
3. **Integration with Now Assist Virtual Agent and Now Assist Panel for Employee schema:** Helps requesters and fulfillers with personalized responses on people queries and Natural Language queries. Also supports people citation card. By default the user NLQ graph is connected which is used for people queries, but you also have sample graph schema for other employee queries. To see more sample graphs for employee queries refer to the KB article.
4. **Integration with AI agents as a tool:** Used to retrieve results in Natural Language and perform follow up tasks that are assigned to the AI agents.

### Knowledge Graph users

| User role | KG Functionality | Description |
|---|---|---|
| Knowledge Graph Admin (kg_admin) | Knowledge Graph Designer | The Knowledge Graph Admin can create and manage Knowledge Graph schemas. |
| Requester | Prebuilt integration with Virtual Agent and Agentic AI | Helps requesters with personalized answers, natural language queries, and fewer conversation turns with pre-filled slots for LLM topics and skills. |
| Fulfiller | Prebuilt integration with Now Assist Panel and Agentic AI | Helps fulfillers with personalized answers, natural language queries, and fewer conversation turns with pre-filled slots for LLM topics and skills. |

### Access Knowledge Graph Schema

Use Knowledge Graph Designer to create, edit, and manage Knowledge Graph schema.

The Knowledge Graph Designer landing page displays a list of all the Knowledge Graph schemas available for users.

ServiceNow provides prebuilt schemas that are non-editable. Currently, the following prebuilt schemas are available:

- **User graph schema:** Used to provide the logged-in user's details to Virtual Agent for personalized response. The profile section is used by AI agents for additional user context.
- **Natural Language Query Schema:** Helps the requester with personalized responses on people queries and Natural Language queries. Also supports people citation card. By default the user NLQ graph is connected which is used for people queries, but you also have sample graph schema for other employee queries. For more details on other prebuilt schema, see the KB article.

ServiceNow has also introduced **Enterprise Graph**, a pre-configured Knowledge Graph schema that maps all instance tables and their connections, enabling natural language queries from data across all tables.

Along with Enterprise Graph, you can also create, edit, and manage **tags** with Knowledge Graph Designer. You can use these tags to mark the key tables that are important for answering natural language questions for specific use cases.

Knowledge Graph supports Admin to create a Knowledge Graph schema with Workflow Data Fabric tables. This helps access data from different systems in real time without moving it. You can create a Knowledge Graph schema from the landing page.

### Prebuilt integration with Now Assist Virtual Agent and Now Assist Panel

The prebuilt integrations of Knowledge Graph can help ServiceNow users to drive productivity, enhance decision-making, and unlock the full potential of enterprise data — while maintaining robust data governance and permission controls.

Available prebuilt integrations with Now Assist Virtual Agent and Now Assist Panel:

1. **Integration with Now Assist for User Context:** Helps requesters and fulfillers with personalized responses.
2. **Integration with Now Assist for Slot filling:** Helps requesters and fulfillers in pre-filling the slots for LLM topics and skills execution using Natural Language Querying of Knowledge Graph.
3. **Integration with Now Assist for Natural Language Query graph:** Helps requesters and fulfillers with personalized responses on people queries and Natural Language queries. Also supports people citation card.

> **Note:** To enable Knowledge Graph for Now Assist Virtual Agent, ensure that the `sn_vad_genai.knowledge_graph.enabled` and `sn_ais_assist.enable_knowledge_graph_nlq` system properties are set to true. See "Add a Knowledge Graph schema to a chat assistant."

> **Note:**
> - To enable Knowledge Graph functionality in the Now Assist Virtual Agent and conversational catalog, make sure to fill the Slot Filling Schema.
> - To use Knowledge Graph for Question Answering from VA, fill out the Natural Language Query Schema in the Now Assist Panel.
> - You can only have one active Knowledge Graph schema at a time for either Slot Filling or Natural Language Query. Multiple active Knowledge Graph schemas are not supported.

#### Integration with Now Assist for User Context

For the users of Now Assist, Knowledge Graph integrates the context from the prebuilt User Profile Schemas that provide personalized responses. By leveraging relationships between users, teams, and content, products like AI Search and Now Assist can provide relevant, permission-aware answers instead of generic results.

Responses are dynamically tailored based on:

- **Who the user is:** Role, department, and location
- **Who they collaborate with:** Manager, reportee
- **What assets they have**

**Example use case:**

- An employee uses Now Assist Virtual Agent for information on parental leave policy. They enter the query in the Virtual Agent window: *What is my parental leave policy?*
- Virtual Agent receives the user information — the employee is based in country: USA, state: California, City: Santa Clara — from the Knowledge Graph User Profile Schema.
- This additional user profile context is used to personalize the synthesized response to the exact location of the employee.
- Instead of getting a link to the parental leave policy document or a generic response, the employee gets a tailored, contextualized answer describing the company's California parental leave policy (24 weeks paid as of January 2022, up from 18), plus California state-law protections such as the California Family Rights Act (CFRA) offering up to 12 weeks of unpaid job-protected leave, and the Pregnancy Disability Leave (PDL) law providing up to four months of unpaid job-protected leave.

#### Integration with Now Assist for Slot filling

Knowledge Graph enhances the Now Assist user experience and makes the process seamless and efficient by reducing the slot-filling questions asked during conversations.

**Example use case:** An employee uses Virtual Agent to request a laptop replacement. Virtual Agent uses the assigned Knowledge Graph schema to find information and resolve the query with minimal user inputs.

1. The user uses Virtual Agent to query *Need assistance in laptop replacement.*
2. Virtual Agent processes the query and generates the following prompts required for this request:
   - Topic: New laptop request
   - Name
   - Location
   - Department
   - Laptop model
   - Address
3. Virtual Agent first tries to gather this information using Knowledge Graph.
4. The Knowledge Graph schema leverages the LLM to retrieve the data from all the relevant entities (nodes) using the relationship between these nodes (edges) and provides the following output:
   - Topic: New laptop request
   - Name: John Doe
   - Location: Santa Clara
   - Department: Marketing
   - Badge Template: User input needed
   - Address: 123 Street, CA, USA
5. Virtual Agent requests verification of the output and adds details for the missing fields.
6. The user can edit and verify the provided information before confirming. Once confirmed, the request is processed with minimal effort from the user.
7. Virtual Agent processes the user input and completes the user query.

Knowledge Graph leverages the existing information available in the internal databases and auto-populates it to reduce the efforts while making the entire experience seamless.

#### Integration with Now Assist for people queries

Now Assist can provide users with information about people in your organization. If you ask Virtual Agent about a person, the information about that person appears in the synthesized response, along with an inline people citation.

Inline citations appear at the end of the relevant synthesized response sentence. Selecting an inline citation results in a popover containing either a link to an article or source, or a description and action to start the action.

> **Note:** Shared files only appear if the Knowledge Graph admin has activated the `sn_kg_conn_user_shared_files` record in the Knowledge Graph related data map [`sn_kg_related_data_map_list`] table. To activate it, set the **Active** field to True.

Selecting the person's name presents a popover. The information in the popover can include:

- Manager
- Location
- Email
- Teams
- Phone
- Shared files

> **Important:**
> - Shared Microsoft SharePoint files between you and the person found appear only on the people popover.
> - The shared files only appear after you have completed the prompt to Log in and signed in successfully. If you do not have a valid token, you will be prompted to sign in and re-directed to the Microsoft login page.
> - If you have not configured Microsoft OneDrive application, see "Configure Microsoft OneDrive application for Knowledge Graph."

#### Integration with AI Search

Knowledge Graph is also integrated with AI Search. You can enable Now Assist Multi-Content Response Genius Results to get answers from Knowledge Graph on AI Search. Ensure that you have already configured Knowledge Graph with an assistant before enabling it on AI Search. To configure and enable the AI Search, see "Now Assist Q&A Genius Results."

### Prebuilt integration with AI agents

The prebuilt integrations of Knowledge Graph can improve live agent productivity by assisting AI agents in performing tasks and answering user queries.

Available prebuilt integrations with AI agents:

1. **Integration with Now Assist AI agents for User Context:** Helps users with personalized responses.
2. **Integration with AI agents as a tool:** Used to perform specific tasks that are assigned to the AI agents.

#### Integration with AI agents for User Context

For the users of Now Assist, AI agents integrate the context from the prebuilt User Profile schema to fetch relevant data and provide personalized responses. By leveraging relationships between users, teams, and content, Now Assist AI agents can fetch relevant, permission-aware user information and provide answers to reduce slot-filling requirement.

**Example use case:**

- A user needs assistance in writing their resume, so they use a ServiceNow AI agent called Resume builder.
- The user adds their task: *Build my resume.*
- AI agents use Knowledge Graph to fetch the following information from the user profile schema: First name, Last name, Location, Email ID, Phone number, Occupation.
- AI agents revert with the available information and request the missing information to proceed building the resume.
- Once the agent has all the required information, it provides the user with output.

#### Integration with AI agents as a tool

Knowledge Graph can be used as a tool within AI agents. Users can choose Knowledge Graph to perform tasks while creating an Agent. You can define the flow action to use Knowledge Graph as a reusable operation in automating the ServiceNow AI Platform features without writing code. See "Add a Knowledge Graph to an AI agent" to add Knowledge Graph to AI agents in AI Agent Studio.

**Example use case:**

- A user wants to view and retire all the assets assigned to another user. To execute this task, the user uses the Asset Manager agent.
- Asset Manager uses Knowledge Graph to fetch the asset information related to the user.
- After processing the query, the agent provides output listing the user's assets, email address, and username.
- The user then proceeds with the task of retiring the assets: *Proceed with retiring the assets associated with Username1.*
- The next tool used to execute this task takes the table name and sysId displayed in Knowledge Graph output and proceeds with the task.

**Example: Knowledge Graph API output in AI agents.** When a user asks *What is my Manager's name?*, AI agents reach out to Knowledge Graph to fetch this information. Example output:

```json
{
  "Manager": [
    {
      "sys_user": {
        "user_name": {
          "value": "abel.tuter",
          "displayValue": "abel.tuter"
        },
        "sysId": "62826bf03710200044e0bfc8bcbe5df1",
        "name": {
          "value": "Abel Tuter",
          "displayValue": "Abel Tuter"
        },
        "first_name": {
          "value": "Abel",
          "displayValue": "Abel"
        },
        "last_name": {
          "value": "Tuter",
          "displayValue": "Tuter"
        }
      }
    }
  ]
}
```

In this example, the table that is called is `sys_user` and the column referred to is `user_name`. The output also displays the SysId, for example: `"sysId": "62826bf03710200044e0bfc8bcbe5df1"`.

### Natural language queries use cases and examples

Natural Language Query support in Knowledge Graph and Enterprise Graph allows users to interact with structured data using human-like language. This feature enhances the user experience by enabling more intuitive and flexible search capabilities within the ServiceNow platform.

**Supported Queries.** Knowledge Graph and Enterprise Graph understand and process queries that reference specific tables, columns, choice values, and conditions. They also handle queries involving system-generated identifiers (sys-ids), person names, dates, and contextual pronouns. Additionally, they support aggregate and sorting queries, enabling users to perform simple statistical analysis and order results.

#### Queries with specific reference

Queries having reference to all table names, column names, or choice values and conditions required are supported. Ensure that the conditions are specified exactly.

| Example | Description |
|---|---|
| Show all stories which are ready for acceptance. | Stories refers to the stories table and ready for acceptance refers to a choice. |
| Find details of CI associated with P1 priority incident. | CI refers to the configuration table and finds those CIs which are linked to an incident with priority 1. |
| List all change requests with high risk. | Change request refers to the change_request table, risk refers to a column, and high refers to a choice. |
| Give details of CI named "AppleMacBookPro15". | CI refers to the configuration item table and named refers to the name column. The exact name of the CI is also specified. |
| Show all incidents which are open. | Incident refers to the table; "in progress," "new," and "on hold" are choice values in the state column options that correspond to open. |
| Share all case tasks assigned to "Dev – Knowledge Graph" group. | Case task is a reference to a table, group is a reference to the assignment group column, and the exact condition to look for is specified exactly. |
| Find Configuration items where manufacturer = Lenovo. | Configuration item is a reference to the cmdb_ci table, manufacturer is a column, and the exact name of the manufacturer is specified. |
| Show me assets assigned to \<Person Name>. | Assets refer to the asset table, assigned to is a column, and the person name is well specified. |
| Find details of CI associated with P1 priority incident. | CI refers to the configuration table and P1 indicates the choice value of the priority column. |

#### Queries with Sys-IDs, Person Names, and Date References

Queries having person names or references to dates such as yesterday, last month, and contextual pronouns to the right person. Queries using system-generated identifiers (sys-ids) also work and can identify the table based on sys-ids.

| Example | Description |
|---|---|
| Find details of request items linked to REQ0010144. | The request item refers to the sc_req_item table and the REQ sys-id refers to the sc_request table. |
| Show details for INC0000044. | INC as sys-id refers to the Incident table. |
| Get status for CHG000567. | CHG as sys-id refers to the change request table and the status refers to the status column for that record. |
| Find department for person who requested RITM0010144. | The RITM sys-id refers to sc_request_item and department refers to the department column from cmn_department, which is linked to the person who requested RITM0010144. |
| Find details of problem linked to INC0000047. | This query requests the details of the problem record linked to incident INC0000047. |
| Show incidents assigned to Fred Luddy. | Finds the Incident table with the user in the assigned to column. |
| List tasks created by Beth Anglin. | Task refers to the task table and the user name refers to the created by column. |
| Find approvals pending for Joe's reportees. | Find approvals from the sysapproval_approver table for approvals that are pending for the user's reportees. |
| Display incidents created more than 3 days ago and are not resolved yet. | Uses the Incident table, created date, and state column to fetch the details. |
| Find certificates expiring in the next 30 days. | Certificates refer to the table name; the next 30 days reference can be converted to a date-related condition and can be understood from the date reference in the query. |
| Find case task created in last 30 minutes. | Case task refers to a table, created refers to the created column, and the time-related condition can be understood from the time reference in the query. |
| What are the Problems open with my group? | Problem refers to the problem table, group refers to a column, and the 'my' reference is resolved to the person asking the query. |
| Show my open incidents. | Uses the Incident table and 'my' reference is the person asking the query. |
| What is the status of my request? | Uses the request table and 'my' reference is the person asking the query. |
| What are their pending approvals? | Uses the sysapproval_approver table and 'their' reference is the person referred to in the previous turn of conversation. |

#### Aggregate or Sorting Queries

These queries let users perform simple statistics and sorting directly in the Virtual Agent or Now Assist panel.

| Example | Description |
|---|---|
| Count of incidents grouped by priority. | Counts the records in the incident table grouped by the priority column. |
| Count of problems grouped by stage. | Counts the records in the problem table grouped by the stage column. |
| Count case task assigned to group "Dev - Knowledge Graph". | Counts the records in the case task table that are assigned to assignment group = Dev – Knowledge Graph. |
| List in progress hr cases by ordered by created date. | Lists the HR cases from the HR cases table ordered by the created date field. |
| Show top 5 users by number of incident assigned to them. | Lists the top 5 users by number of incidents from the incident table assigned to them. |

#### Unsupported Query Categories

Knowledge Graph does not support the following types of queries:

**Queries Missing References or with Misspellings.** Queries that lack references to table, columns, choice values, or conditions, or contain misspellings, are not supported.

| Example | Rephrase to: |
|---|---|
| Find incidents about SAP login issue. | Find incidents where short description = SAP login issue. |
| Find CI where manufacturer is Orrange. (Incorrect spelling) | Find CI where manufacturer is Orange. |
| Find CI in SanDiego city. | Find CI in San Diego city. |
| Locate changes related to patch upgrade. | Locate change request where description contains patch upgrade. |
| Change request for Abel Tuter. | Change request assigned to Abel Tuter or Change request opened by Abel Tuter. |
| Problem by Mark Andrew. | Problem updated by Mark Andrew or Problem closed by Mark Andrew. |

**Queries on Journal Fields or Document IDs.** Queries involving journal entries, document IDs, or glidelist references are not supported. Examples of unsupported queries:

- Show latest comments added to INC0000044.
- What comments or work notes were added in the approval of change request CHG0000046.
- Show tasks with 'urgent' in comments.
- Find incident where Joe commented about email resolution steps.

**Keyword Queries or Queries Requiring KB Resolution.** Keyword-based queries or those requiring resolution from the Knowledge Base (KB) are handled by AI Search, not the Knowledge Graph. Examples of unsupported queries:

- VPN issue
- Password reset
- Incident SLA
- How can I request a windsurf license?
- How to install global protect for PC?

### CMDB query support

Knowledge Graph supports CI Relationship (Rel CI) queries, enabling natural language questions about CMDB configuration item dependencies and infrastructure topology.

### Workflow Data Fabric integration with Knowledge Graph

Knowledge Graph supports Workflow Data Fabric to fetch third-party information securely without copying the data. The integration of Workflow Data Fabric (WDF) with the Knowledge Graph allows organizations to seamlessly connect external and internal data sources. This integration extends the functionalities of the Knowledge Graph to external data, ensuring real-time access and enabling advanced insights, workflow automation, and personalization using external data.

**Key features of Workflow Data Fabric integration with Knowledge Graph:**

- **Real-Time Access:** Zero Copy connectors from WDF and the semantic layer of the Knowledge Graph ensure that external data is accessible in real-time.
- **Deep Data Connection:** WDF tables are automatically included in the Enterprise Graph, enhancing the connectivity and utility of external data within the ServiceNow platform.
- **Natural Language Query Support:** Users can ask natural language queries (NLQ) in Virtual Agent and AI Agents, leveraging both external (WDF) and internal data.

**Benefits of using Workflow Data Fabric integration in Knowledge Graph:**

- **Requestors and Fulfillers:** Can ask NLQ questions and receive insights from external (WDF) tables integrated with the KG schema.
- **Admins:** Can create a KG schema with WDF tables and link it to the Now Assist panel, AI Agents, or Now Assist in Virtual Agent.

Admins can add WDF tables to the Knowledge Graph just like any other internal table. However, only WDF tables configured with a primary key are supported.

**Integration best practices:**

- **Primary Key Requirement:** Always add a primary key to your WDF table during configuration. This is mandatory for supporting WDF tables in the Knowledge Graph.
- **Meaningful Naming:** Use clear and meaningful names when creating WDF tables. Add synonyms to your tables in the Knowledge Graph schema as needed to improve the accuracy of natural language queries.

**Example use case:** **Snowflake and Google BigQuery Integration** — WDF tables sourced from Snowflake and Google BigQuery can be added to the Knowledge Graph schema, allowing users to query and analyze data from these external sources within ServiceNow.

### Configuration item relationships and Knowledge Graph

Configuration item (CI) Relationships enable Knowledge Graph to answer natural language questions about service dependencies and infrastructure topology by storing typed parent-child relationships between CMDB configuration items.

The `CMDB_REL_CI` table stores relationships between configuration items (CIs) in the ServiceNow CMDB. Each relationship connects a parent CI to a child CI through a defined relationship type, enabling the Knowledge Graph to understand and traverse the topology of your IT environment. CI relationship support in Knowledge Graph allows users to ask natural language questions about how services, servers, databases, and other CIs relate to one another without writing queries or navigating CMDB tables directly.

#### Enabling CI relationship for Knowledge Graph

CI relationship support for the Knowledge Graph is inactive by default. Set both of the following system properties to true to enable it:

| System Property | Purpose |
|---|---|
| `sn_kg.description_generation.enable_cmdb_rel_ci` | Enables description generation for CI relationship data |
| `sn_kg.query.enable_cmdb_rel_ci` | Enables Knowledge Graph querying against CI relationship data |

> **Note:** After enabling both properties, allow time for CI relationship data to be fully indexed before running queries. Results may be incomplete until indexing is complete.

#### How CI relationship data is stored

Each record in the CI relationship table represents a bi-directional relationship between two CIs. Relationships are described by a relationship type that consists of a parent-to-child relationship and a child-to-parent relationship, separated by double colons:

```
<parent descriptor>::<child descriptor>
```

This means every relationship can be read in two directions:

- **Parent → child:** read using the parent-to-child relationship (parent descriptor)
- **Child → parent:** read using the child-to-parent relationship (child descriptor)

For example, a record in the CI relationship table has **Bond Trading** (cmdb_ci_service) as the parent, **lnux100** (cmdb_ci_linux_server) as the child, and a relationship type of **Depends on::Used by**. This relationship is read as:

- Bond Trading depends on lnux100
- lnux100 is used by Bond Trading

> **Note:** The direction of the relationship affects how you phrase queries to the Knowledge Graph. Parent-to-child queries (for example, "depends on") return more reliable results than child-to-parent queries (for example, "used by").

#### Knowledge Graph support for CI relationships

The Knowledge Graph can answer questions about CI relationships when the query clearly specifies all three of the following:

- The class of the parent CI (for example, service)
- The relationship direction — either the parent descriptor or child descriptor (for example, depends on)
- The class of the child CI (for example, Linux server)

#### Class hierarchy inheritance

When you define a relationship between two CI classes, the Knowledge Graph automatically extends that relationship to all classes higher up in the CI class hierarchy. This means users can query at a more general class level and still get results across all matching subclasses.

For example, a relationship defined between service and Linux server also applies to server, which is a parent class of Linux server in the hierarchy. Querying for servers rather than Linux servers returns results across all server subclasses — including Linux server, Windows server, UNIX server, and others.

> **Note:** If a query returns fewer results than expected, try using a broader parent class in the hierarchy (for example, "server" instead of "Linux server") to include all inherited CI types.

#### Supported query patterns

| Scenario | Example Query |
|---|---|
| Service that depends on a specific Linux server | Which services depend on 'lnux100' Linux server? |
| Servers that a specific service depends on | 'Bond Trading' service depends on which UNIX server? |
| All server types a service depends on (using hierarchy) | 'Bond Trading' service depends on which server? |
| Computers connected to a database | Which databases are connected by computers? |
| Multi-hop relationship across three CI types | What database runs on UNIX server that connects to 'nc6500-a01' network gear? |

#### Unsupported query patterns

| Limitation | Unsupported Query | Recommended Alternative |
|---|---|---|
| Negation of a relationship | Which business capabilities have no related business applications? | Rephrase to ask for what does exist rather than what does not. |
| Unspecified relationship type | Show me services related to Linux servers. | Show me services depending on Linux servers. |
| Skipping steps in a multi-hop path | Show me servers in New York. | Show me servers in racks present in datacenters located in New York. |

## Instructions / Procedures

### Access Knowledge Graph Schema

**Before you begin** — Role required: `kg_admin`

**Procedure:**

Navigate to **All > Knowledge Graph > Knowledge Graph Designer**.

The Knowledge Graph Designer landing page displays a list of all the Knowledge Graph schemas available for users. You can create a Knowledge Graph schema from the landing page.

### What to explore next

To learn more about configuring and using Knowledge Graph, see:

- Configuring Knowledge Graph
- Using Knowledge Graph Designer
- Reference for Knowledge Graph

## Figures, Diagrams & Screenshots

**Figure (p.973):** A "Get started" navigation panel of six tiles arranged under three column headers — **Explore**, **Configure**, and **Use Knowledge Graph**. Each tile shows a circular green line-art icon above a label. Top row tiles: "Explore Knowledge Graph" (interlocking-rings/atom-like icon), "Configure Knowledge Graph" (gear icon), and "Create and edit Knowledge Graph schema" (monitor/desktop icon). Bottom row tiles: "Using Enterprise Graph queries in Knowledge Graph" / "Learn about the Enterprise Graph schema" (icon resembling a node graph), "Natural Language queries in Knowledge Graph" / "View example use cases of natural language queries in Knowledge graph" (calculator/grid icon), and "Reference" / "Additional information to configure Knowledge Graph" (icon). The page also references an embedded Vimeo video (player.vimeo.com link) introducing Knowledge Graph. This panel is the documentation landing hub directing readers to the Explore, Configure, and Use sections. The top of the page also shows the tail end of an "AI prompt digital asset" table with attributes "Prompt information" (Details of the prompt) and "AI model" (Reference to the AI model for which the prompt is created).

**Figure (p.977):** Screenshot of the **Knowledge Graph Designer** landing page in the ServiceNow platform UI. The top shows the platform navigation/breadcrumb bar. The main content area is split: on the left is an **Enterprise Graph** panel with descriptive text and a table/list of available Knowledge Graph schemas (columns for name, scope, updated, and similar metadata); on the right is a node-graph thumbnail/preview showing several connected circular nodes (an Enterprise Graph visualization) with surrounding control buttons. Below is a **"Pre-built Knowledge Graph Schemas"** list/table showing the prebuilt schemas (such as the user/profile and employee schemas) with their attributes. The screenshot illustrates where users land when they navigate to All > Knowledge Graph > Knowledge Graph Designer and how prebuilt and custom schemas are listed.

**Figure (p.981, top):** Screenshot titled "Example of synthesized response for people on the portal's search results page." It shows a search-results synthesized answer block. The answer reads that a person (Alissa Mountjoy) is a Product Manager on a team, with their location (Frankfurt) and email address shown as a hyperlink, followed by an "Ask a follow-up" prompt and an inline people citation. It illustrates how people information and an inline citation surface on the portal search page.

**Figure (p.981, middle):** Screenshot titled "Example of synthesized response with people inline citations in chat." It depicts the **Now Assist** chat panel. The header bar reads "Now Assist" with icons for New chat, Chats, Support, and Settings. A user has typed "Carol Couglin." The assistant responds: "I found 2 people named Carol Couglin," then lists two people — Carol Couglin, an Account Executive on the Sales team, location Hamburg, with an email hyperlink and an inline citation (person icon + name); and Carol Couglin, a Product Manager on the AI team, location New York City, with an email hyperlink and inline citation. It closes with "If these aren't who you're looking for, tell me more information, like their job title and location, and I can help find the right person." A "Reply..." input box and the disclaimer "Some answers generated by AI. Be sure to check for accuracy." appear at the bottom. This illustrates inline people citations within a Now Assist chat conversation.

**Figure (p.979):** Two-panel comparison diagram showing how Knowledge Graph reduces slot-filling in a Virtual Agent conversation for the use case **"Request for laptop replacement."**
- **Left panel - "Without Knowledge Graph integration"** (Virtual Agent "Processes the query with a set of prompts"): the assistant asks a long series of slot-filling questions one at a time - *What is your name?*, *In what department do you work?*, *What is your office location?*, *What was your hire date?*, *Are you eligible for a new laptop?*, *Do you have the required permission?*, *Choose a laptop model.*, *Select delivery address.*, *Enter delivery date/time.* - and the user must answer each (Jane Doe; Marketing; Santa Clara, CA; May 22, 2021; Yes; Yes; Model A; 123 Main St. CA. USA; November 18, 10:30am PST).
- **Right panel - "With Knowledge Graph integration"** (Virtual Agent "Processes the query leveraging Knowledge Graph schema"): the known details are auto-filled from the graph, so the assistant only asks the user to confirm - *Please confirm your details: Name: Jane Doe, Department: Marketing, Office Location: Santa Clara, CA, Hire date: May 22, 2021* - then *Based on your hire date, you are eligible for a new laptop. Please choose your preference for: Laptop model: Model A; Delivery address: 123 Main St. CA. USA; Delivery date/time: November 18, 10:30am PST.*

The diagram illustrates that Knowledge Graph integration eliminates most of the back-and-forth slot-filling questions by sourcing user and context data from the graph. (This figure is vector artwork that the default PDF renderer dropped; its content was recovered from the PDF text layer via MuPDF.)

**Figure (p.982):** Screenshot of a **people popover card** for "Alissa Mountjoy, Product Manager at AI Search." The card lists fields: **Manager** (Sam Smith), **Location** (Frankfurt, Germany (GMT+1)), **Email** (a hyperlinked address), **Teams** (a team link), and **Phone** (+49 33 12345678), with a "Log in" prompt/link and a circular avatar/initials icon. It illustrates the popover that appears when a user selects a person's name in a synthesized response, including the additional Microsoft SharePoint shared-files context after sign-in.

**Figure (p.983):** Code block showing the beginning of a Knowledge Graph API JSON output for the query "What is my Manager's name?" — an object with a `"Manager"` array opening, leading into a nested `"sys_user"` object (continued on page 984). It illustrates the structured JSON that AI agents receive from Knowledge Graph.

**Figure (p.984):** Continuation code block of the Knowledge Graph API JSON output, showing the `sys_user` object with `user_name` (value/displayValue "abel.tuter"), `sysId` "62826bf03710200044e0bfc8bcbe5df1", `name` ("Abel Tuter"), `first_name` ("Abel"), and `last_name` ("Tuter") fields, each with value and displayValue pairs. It illustrates the full table/column/sys-id structure returned for the Manager query.

**Figure (p.989):** Screenshot of a **Knowledge Graph schema canvas / node-edge graph diagram** illustrating the Snowflake and Google BigQuery (Workflow Data Fabric) integration. The canvas shows multiple labeled circular nodes connected by edges radiating from central "ServiceNow" hub nodes, representing internal ServiceNow tables linked to external WDF tables (Snowflake/BigQuery sources). A side/detail panel with configuration options appears on the right. It illustrates how WDF tables sourced from external data warehouses are mapped as nodes within a Knowledge Graph schema alongside ServiceNow tables.
