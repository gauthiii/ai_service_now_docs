# Using Enterprise Graph Schema

_Source: ServiceNow Now Assist documentation, pages 1006-1028._

## Overview

Use Enterprise Graph for accurate natural language query responses, across the entire database. Enterprise Graph is a pre-configured Knowledge Graph schema that maps all instance tables and their connections, enabling natural language queries for data across all tables.

Enterprise Graph schema simplifies Knowledge Graph setup by providing a preconfigured schema, eliminating the need for custom schema creation in Knowledge Graph designer. Admins can choose Enterprise Graph as the Knowledge Graph schema when using AI agents, NA Virtual Agent, or NA Panel and add tags to enhance accuracy.

By mapping all tables, the Enterprise Graph schema expands query capabilities to cover the entire database, whereas a custom or out-of-the-box (OOTB) schema limits queries to only the tables included in its specific schema.

This subtopic covers the benefits of Enterprise Graph on prebuilt integration, the two modes of Enterprise Graph, tags in Knowledge Graph (tagging, creating, and managing tags, AI instructions, synonyms, data filters, and hidden columns), setting up Enterprise Graph in sub-production and production instances, and accessing, viewing, managing, selecting tables for, and testing the Enterprise Graph schema.

## Features

- A pre-configured schema that maps all instance tables and their connections.
- Two modes: Enterprise Graph (regular mode) and Enterprise Graph (Small).
- Tags to mark key tables important for answering natural language questions for specific use cases, including prebuilt tags (Virtual Agent Default Tag, Now Assist Panel Default Tag).
- AI instructions at node, property, and edge levels (with an optional **Always Include** flag).
- Support for synonyms, data filters, and hidden columns.
- Manual setup of Enterprise Graph in sub-production instances; automatic configuration in production with the ability to import generated descriptions from sub-production.
- Access, view, and manage the Enterprise Graph schema; select multiple tables (up to 200 nodes); test the schema with selectable LLM models and Enterprise Graph modes.
- Contribute synonyms to the Enterprise Graph schema to improve accuracy.

### Benefits of Enterprise Graph on Prebuilt integration

- **Now Assist Virtual Agent:** With Enterprise Graph integration, Now Assist Virtual Agents can respond to a wide range of questions about their enterprise data from requesters, helping to deflect queries.
- **Now Assist Panel:** With Enterprise Graph enabled, Now Assist Panel allows fulfillers to obtain insights from the structured data in the instance by asking natural language questions, which boosts their productivity.
- **AI agents:** With Enterprise Graph enabled, AI agents can access relevant information from structured data in the ServiceNow instance directly from the Knowledge Graph, giving them essential context for tasks.

## Functionalities

### Modes of Enterprise Graph

Enterprise Graph has two modes:

- **Enterprise Graph — regular mode:** Used for use cases with a large number of tables (more than 50 tables). Searches across all tables, but gives more priority to tables which are included in the tag added at the time of configuring Enterprise Graph in the consuming app (AI agent or VA). Useful for scenarios where an answer is expected from a large number of tables.
- **Enterprise Graph (Small):** A version of Enterprise Graph that limits the search to only the tables tagged with specific labels. This means it can only answer queries related to those tables. Searches only within tables included in the tag added at the time of configuring Enterprise Graph (Small) in the consuming app (AI agent or VA). Tagging is mandatory in this mode. Useful for latency-sensitive use cases with a limit of 50 tables.

### Tags in Knowledge Graph

Tags are lists of key tables that are important for answering natural language questions in a specific use case. They are required to be used with Enterprise Graph and Enterprise Graph (Small). Use Knowledge Graph Designer to create and edit tags from the **Enterprise Graph Tags** section.

| Name | Description |
|---|---|
| Enterprise Graph — regular mode | Provides a hint to Enterprise Graph on which tables to prioritize when retrieving information, to improve the accuracy of results. It is recommended to only tag up to 30 tables for regular mode as hints to prioritize while searching. |
| Enterprise Graph (Small) | Provides a list of tables to run the search operation. Enterprise Graph (Small) will only search on the tables provided by tags. It is mandatory to add a tag when Enterprise Graph (Small) is used with any of the prebuilt integration with AI agent, Virtual Agent, or Now Assist Panel. You can tag a maximum of 50 tables. To enable querying on columns of a table which are references to another table, also include the referenced table in tags. |

**Creating tags.** Tags are created by kg_admins using the Knowledge Graph Tags section and must be linked to a schema when selecting Enterprise Graph or Enterprise Graph (Small) as the Knowledge Graph schema for your use case in Virtual Agent, Now Assist Panel, or AI agent.

Knowledge Graph ships the following prebuilt tags:

1. **VIRTUAL AGENT DEFAULT TAG:** A prebuilt tag listing common core, ITSM, and HR tables for integrating Enterprise Graph with the Virtual Agent on the employee portal. Admins can edit this tag to include additional tables relevant for answering Virtual Agent queries.
2. **NOW ASSIST PANEL DEFAULT TAG:** A prebuilt tag listing common core, ITSM, and HR tables which can be leveraged as a general tag on Now Assist Panel. Admins can edit this tag to add additional important tables for answering questions on Now Assist Panel.

**Steps to create or edit tags:**

- Go to the Knowledge Graph Designer to view the existing tags and their associated tables. You can use an existing tag, edit one to fit your needs, or create a new tag for your particular use case.
- Navigate to the admin center for consuming apps:
  - For the Now Assist Virtual Agent or Now Assist Panel, go to your virtual agent's setup, select **Information Sources**, and open the Knowledge Graph.
  - For AI agent, proceed to its setup and open the Knowledge Graph tool for the AI agent.
- Select **Enterprise Graph** or **Enterprise Graph (Small)** as the KG schema and select the required tag from the **Tag** drop-down to link it to the graph schema.

> **Note:** In this release, the Enterprise Graph option is hidden by default for Now Assist Virtual Agent and Now Assist Panel, and only Enterprise Graph (Small) can be selected as the schema option. To use Enterprise Graph, Admins can enable it as a schema option by setting the property `sn_kg.va.enable_global_graph_all_modes` to true. The role required is Admin.

**Recommended tables for different use cases:**

- **Now Assist Virtual Agent:** Include the tables necessary to answer the expected user queries. For example, if you want to deploy a new virtual agent on the employee center portal, add a tag having tables relevant for answering employee questions.
- **Now Assist Panel:** Operates as a unified assistant across multiple workspaces, so it is essential to tag tables as follows:
  - An individual tag for each workspace that encompasses key tables relevant to that workspace. This ensures the Now Assist panel can deliver responses specific to queries related to the workspace tables when accessed within each workspace.
  - Create a general tag that includes the most important tables required to answer users' questions on Now Assist Panel, allowing the Now Assist panel to provide relevant answers when used outside of any workspace.
  - For more information on adding workspace tags in Now Assist Panel, see "Add a Knowledge Graph schema to a chat assistant."
- **AI agent:** Include key tables relevant to the agent's purpose. For example, for asset manager agents, User, Asset, and other crucial tables should be included in the tag. For more information, see "Add a Knowledge Graph to an AI agent."

### Improving Natural Language Queries with Tag configuration

AI instructions add more business context to natural language queries. They guide users and promote responses that more closely align with their needs and expectations.

**AI instructions.** AI instructions help clarify how the knowledge graph interprets user queries and accesses data. When a user submits a query, relevant instructions at all applicable levels — node, property, and edge — are considered. Referencing data within tables directly in instructions is not a general guideline. Instead, instructions should be generalized and context-driven. You can add instructions at three levels:

- Node (entity/table)
- Property (column/attribute)
- Edge (relationship) level

**The Always Include flag.** The option to set an **Always include** flag enables users to indicate that a particular instruction should be considered unconditionally. This is useful for enforcing critical business filters, such as always excluding certain asset statuses unless requested otherwise.

- Use **Always include** for business-critical filters that must apply regardless of user query phrasing.
- Omit **Always include** for context-sensitive instructions that should only apply when relevant.
- Verify that flagged instructions do not conflict with each other or produce duplicate results.

**Examples of Good AI Instructions:**

- "Always add WHERE alm_asset.install_status <> 7 to filter out retired assets by default." This instruction respects business context automatically. Retired assets are excluded unless the user explicitly requests them.
- "When generating a query involving sc_cat_item, don't include state='published' unless explicitly mentioned." This avoids unintended filtering caused by ambiguous instructions.
- "For life-cycle-related queries, use sam_sw_product_lifecycle_report as the primary/default table." This aligns query logic with performance and business requirements.

| Good Instruction | Bad Instruction |
|---|---|
| Consider normalized_company only when user asks for normalised manufacturer. | Check company (no indication of which property or relationship to use). |
| Always add WHERE alm_asset.install_status <> 7 to filter out retired assets by default. | Filter by manufacturer (no column or condition specified). |

Poor instructions may result in hallucinations. The AI generates incorrect data or misinterprets the query intent. This can occur due to:

- Missing context or incomplete references.
- Ambiguous column or table names.
- Contradictory guidelines across instruction levels.

AI instructions must adhere to the same basic guidelines as user queries. Reference structured elements, avoid unsupported query types, and follow prescribed business logic. What applies to good queries also applies to effective AI instructions.

**Examples of how to use AI instructions effectively:**

| No. | Instruction Pattern | Example Query | Behavior without AI instruction | Sample AI instructions | Behavior with AI instruction |
|---|---|---|---|---|---|
| 1 | Preventing incorrect traversal paths | Which companies are located in New York? | When no instructions are added, the query goes from core_company to cmn_location table and filters on the city field by default. But if your use case requires querying location from the city field of core_company table, you need to write an AI instruction to guide the system on the traversal path. | Table Instruction on core_company table: "For company-city queries, always use core_company.city directly. Do NOT traverse through cmn_location." This instruction avoids the system from using the cmn_location path for city-based company queries. | When the instruction is added, the query matches the city field in core_company and then filters city = New York and returns all companies. |
| 2 | Providing column specific context | Who hosted BBS0000013 brown bag session? | When there is no AI instruction, the system will return sys_id without traversing to host_s. You need to add an instruction on the host_s column to provide business context to use this column when the query is about host. | Column Instruction on host_s of x_snc_brown_bags_sessions table: "Use s.host_s or :host_s relationship for the host of a brown bag session, NOT s.sys_created_by." | When instructions are added, the query correctly returns the name from the host_s column. |
| 3 | Providing column specific context | What is Kelsey Rodriguez's tenure in current role (months)? | When there is no AI instruction, the system may not give an accurate result as it may provide incorrect information for the tenure column. You need to add an instruction to guide the system to refer to the right column for such queries. | Column instruction on time_in_current_role column: "Prioritize this column when query contains 'tenure in current role'." | When instructions are added, the query correctly returns the time from the time_in_current_role column. |
| 4 | Providing context on what to prioritize in case of similar tables | Give me name of Allison Hill's reports having goals pastdue >0? | When there is no AI instruction, the LLM will directly refer to "sys_user" table to fetch user details instead of traversing to the WDF table where this information is stored. We need to add an instruction to guide the LLM to refer to the right table when there are similar tables. | Table instruction on WDF table — "x_snc_wdf_user": "Always give more priority to 'x_snc_wdf_user' over sys_user and other glide tables." | When instructions are added, the query correctly refers to the WDF table and returns results. |
| 5 | Providing context on what to prioritize in case of similar tables | What is your job title? | When there is no AI instruction, the LLM will directly refer to "sn_hr_core_job" table to fetch job details instead of traversing to "sn_hr_core_profile" table where this information is stored. We need to add an instruction to guide the LLM to refer to the right table when there are similar tables. | Table instruction on table — "sn_hr_core_profile": "Always give more priority to 'sn_hr_core_profile' over 'sn_hr_core_job' when user specifically asks about job titles." | When instructions are added, the query correctly refers to "sn_hr_core_profile" table and returns results. |
| 6 | Disambiguate among multiple similar and confusing choice values | What are the hardware models that are in normalized state? | When there is no AI instruction, the LLM will refer to "normalized" choice value of "normalization status" column which could confuse the LLM whether to use other choice values or not, as the "normalization status" field has 5 choice values (normalized, manufacturer normalized, manually normalized, partially normalized, match not found). We need to add an instruction to guide the LLM on which all choices to include in normalization status. | Column instruction on "Column-normalization status": "Always consider normalization status as normalized when choice values is any of the following choices: 'normalized, manufacturer normalized, manually normalized'." | When instructions are added, the query correctly considers all 3 choices ("normalized, manufacturer normalized, manually normalized") as normalized state and returns results. |

**Best practices for AI instructions:**

- Write clear, unambiguous, and actionable instructions tied to business logic. Always reference the correct tables (nodes), columns (properties), and relationships (edges). Use flags like **Always include** only when enforcing true default business behavior.
- Avoid vague or contradictory instructions. Instructions that do not align with the underlying data model can confuse the system and lead to incorrect results. For example, an instruction like "Filter by manufacturer" without specifying the column or condition is ambiguous.
- Use conditions to control when logic applies. Clearly state when an instruction should be applied (for example, only when the user asks for host information), rather than applying logic universally.
- Keep instructions focused and generalized. Instructions should guide intent interpretation across similar queries, not solve a single one-off case.
- Do not duplicate logic already handled elsewhere. Avoid restating filters or constraints that are already enforced through data filters to avoid conflict.

### Support for Synonyms, Data Filters and hidden columns

**Synonyms.** Knowledge Graph supports configuring synonyms for tables, columns, edges, and reverse edges to enhance flexibility and user-friendliness. Synonyms enable users to define alternate names for these entities, accommodating different terminologies.

- Each entity can have up to five synonyms.
- Synonyms promote broad coverage for commonly used alternate terms.
- Maintaining a manageable synonym set reduces ambiguity in query resolution.

**Data Filters.** Data filters are applied deterministically as post-processing rules to refine query results. After initial Cypher generation, filters are systematically applied to promote consistency and reliability of outcomes.

- Filters are applied after Cypher generation, not during.
- Dynamic filters enable real-time adaptation based on user context.
- Improves precision and relevance of returned data. Does not modify the core graph query.

**Hidden columns.** Hidden columns cannot be queried and do not appear in the result. For example, add Employee number as a hidden column for the sys_user table to hide the employee number from query results.

## Instructions / Procedures

### Create Knowledge Graph tag

Create Knowledge Graph tags for Now Assist Virtual Agent, AI agent, or Now Assist panel Enterprise Graph using Knowledge Graph Designer to improve accuracy of natural language queries.

**Before you begin** — Role required: `admin`

**Procedure:**

1. Navigate to **All > Knowledge Graph Designer > Enterprise Graph Tags > New tag**. You are navigated to the Create New Tag record page.
2. On the Create New Tag record page, add the following information:
   - **Tag name:** Name for the tag.
   - **Description**
   - **Scope:** The default selection is Global. Read-only field.
   - **Select Tables:** The tables or nodes that you want to add to the tag.
3. Select **Next** to go to the Configure tables page. The details added to the Configure tables page will help to further improve the accuracy of the natural language queries. The selected tables will be displayed on the left pane of the Configure tables page.
4. Select a table from the left pane to add the following — column and edge configurations, data filters, and hidden columns:
   - **Tables configurations:** Synonyms and AI instructions
   - **Column and edge configurations:** Synonyms and AI instructions
   - **Data filters**
   - **Hidden columns**

   AI Instructions inject business context directly into the Knowledge Graph natural language query engine, shaping how the system interprets and traverses data. Instructions can be configured at three levels: Node (entity/table), Property (column/attribute), Edge (relationship). Each instruction can optionally be marked as **Always Include**, ensuring critical business logic applies unconditionally across all queries. For best results, write instructions as generalized, context-driven guidance rather than hard-coded references to specific table values.
5. Add alternative names in the **Table synonyms** field and select **Add**.
   - Use the commonly used table names as synonyms to help AI recognize them in natural language queries.
   - Example: you can add Tickets as a synonym for the Incident table.
   - You can add up to five synonyms only.
6. To delete a synonym, select the icon next to the synonym.
7. Add AI Instructions in the Table Configurations section and select **Add**.

   > **Note:** Add up to 5 table-specific business context in the AI Instructions field.
8. Select **Always include** to allow adding an instruction as a default business logic. For example, always include an instruction to skip retired assets from the results unless the user explicitly requests it.
9. Select **Add Column** and choose the columns and edges that you want to add synonyms to.
   - Add commonly used column and edge names as synonyms to help the AI match user terms to this field.
   - Example: you can add Opened On as a synonym for Created Date.
   - You can add up to five synonyms only.
   - The selected columns and edges are added to the **Column / Edge configurations** section.
10. To delete a column from the section, select the icon next to the column.
11. Add AI Instructions in the Column/Edge Configurations section and select **Add**.

    > **Note:** Add up to 5 instructions per entity in the AI Instructions field.
12. Select the **Add filter** option to add data filters for managing which records appear in the query results and add the following details:
    - Field
    - Operator
    - Value

    Examples:
    - To exclude inactive users from search results, apply Active = True filter.
    - To include only active incidents in response, add a data filter to consider state in (in progress, on hold).
13. Select the **Apply filters to child tables** check box if you want to add the same filter conditions for the child table of the selected table in the tag. If enabled, these filters will also apply to child tables that inherit data from this table.
14. Select irrelevant or insensitive columns from the **Hidden column** drop-down to exclude them from queries. Hidden columns cannot be queried and do not appear in the result. For example, add Employee number as a hidden column for the sys_user table to hide the employee number from query results.
15. Select **Create tag** and repeat the same process for each of the selected columns.

### Managing Knowledge Graph tags

Edit or delete Knowledge Graph tags for Now Assist Virtual Agent, AI agent, or Now Assist Panel Enterprise Graph use case.

**Before you begin** — Role required: `admin`

**Procedure:**

1. To edit an existing tag, go to **All > Knowledge Graph Designer > Enterprise Graph Tags**.
2. Select a tag to open it in the Knowledge Graph canvas. You can see all the tables that are part of the tag on the Knowledge Graph canvas.
3. Select the **Edit tag** option to open the Edit Tags window or select a node to edit. If you select a node you will see the Tag configuration section on the right pane.
4. You can also select the **Edit tag configuration** icon from the Tag configuration section to open the Edit Tags window.
5. To delete a tag, select the icon next to a tag on the Enterprise Graph tags section on the home page.
6. Select **Delete** from the drop-down. You can also select the edit option here, to go to the Edit tags window.
7. When prompted, confirm the deletion process.

### Setting up Enterprise graph in sub-production instance

Use these steps to set up Enterprise Graph in a sub-production instance manually.

**Before you begin** — Unlike production instances, the Enterprise Graph setup does not start automatically in the sub-production instance. You have to manually enable the system property: `sn_kg.description_generation.enable.non_production_envs`. When you enable this system property, the Enterprise Graph setup starts in the sub-production instances and can take several days to complete. Until this setup is finished, the Enterprise Graph schema won't work effectively for answering queries. This step creates the necessary descriptions for the Enterprise Graph to respond to queries. Role required: `kg_admin`.

### Initial setup for Enterprise Graph schema in production instance

Set up and use Enterprise Graph Schema, a unified knowledge graph schema that captures all the ServiceNow and third-party tables and their connections.

**Before you begin** — When you install Enterprise Graph, it automatically begins configuring instance tables. This may take several days, and until the setup is complete, the schema won't respond effectively to queries. If you have already completed the setup in a sub-production instance, you can import the generated descriptions to the production instance to speed up the process.

Assuming that you have completed the setup in a sub-production instance, do the following to complete the initial setup in the production instance:

- Create an integration user in the sub-production instance. For more information, see "Create a user."
- Verify if the descriptions are generated in the sub-production instance.
- Use the following procedure to import the data into production and run the associated Transform Maps.
- Remove tracker records from the production instance.

Role required: `admin`

**Procedure:**

1. Navigate to **All > Connections & Credentials > Connection & Credential Aliases**.
2. Open the record with the name **Description_Connector**.
3. Select **Create New Connection & Credential** from the related links section.
4. Enter the required details in the **Create Connection & Credential** form.
5. Add the user name and password that was used while creating the new user. See "Create a user" for more information.
6. Navigate to **All > System Import Sets > Administration > Data Sources**.
7. In the name field search bar, enter **KG** to view the related tables. The following tables are displayed:
   - KG Choice Picker Description.
   - KG Column Picker Description.
   - KG Table Picker Description.
   - KG Triplet Picker Description.
8. Open one of the displayed tables and select **Load All Records** from the Related links section. Ensure the data is loaded.
9. Navigate to **System Import Sets > Advanced > Import Sets**, once the data is loaded. For detailed information, see the import set documentation "Import sets."
10. Open the import set and select **Transform** from the Related links section. For detailed information, see the transform map documentation "Transform maps."
11. Select **Transform** to complete the transformation.
12. Navigate to the selected table and verify if the data is loaded.
13. Repeat the import set and transformation steps for the other three tables.

### Access Enterprise Graph schema

View and manage the Enterprise Graph schema, select tables, and test the schema with Knowledge Graph Designer.

To view and manage the Enterprise Graph schema, go to **All > Knowledge Graph Designer > Open Enterprise Graph**. Use Enterprise Graph to view and test the schema. You can also contribute synonyms to the schema for your use case. Synonyms will help improve the accuracy of Enterprise Graph for answering queries.

On the Enterprise Graph start page, use the search bar to search and select a table you want to view or manage. Alternately, you can use the **Open your last view** or **Start with user tables** to view the user and the related table. The Enterprise Graph start page displays the total number of nodes. You can use the **Select multiple tables** option to select tables that you want to view in the schema. Within the Select multiple tables option, you can select an application, tag, or individual tables. Once you select the node, you will see selected nodes and their associated tables on the schema. You can also use the **Test Enterprise Graph** option to run a query on the Enterprise Graph schema.

### View and manage Enterprise Graph schema

Use Knowledge Graph Designer to view and manage the Enterprise Graph schema.

**Before you begin** — Role required: `admin`

**Procedure:**

1. Navigate to **All > Knowledge Graph > Knowledge Graph Designer > Enterprise Graph**. You are navigated to the Enterprise Graph start page.
2. Do one of the following to go to the Enterprise Graph canvas:
   - Search and select a table from the search bar.
   - Select **Open your last view**.
   - Select **Start with user tables**.
   - Select **Select multiple tables**.

   The Enterprise graph schema opens in the Knowledge Graph canvas page.
3. Optional: You can select a tag from the drop-down next to Enterprise graph to see a specific tag.
4. From the toolbar, select the **Nodes details** option to view details or add a synonym for the node. The other fields are read-only and cannot be edited. In the tag view of Enterprise Graph, you can also see tag configuration when you click on a node.
5. Use the icon in the **Tag configurations** section to go to the Edit tag configurations page and update the following details:
   - Node synonyms
   - Column with synonyms
   - Data filters
   - Hidden columns
6. In the **Columns that can be queried** section, search and view the columns of the tables.
7. From the toolbar, select **Related nodes** to view the related nodes.
8. Select **Save** to save the synonyms that you have added. You can save to the most recent contribution or choose another contribution from the drop-down, to save your changes.
9. Select **Discard** to delete your changes.

### Select multiple tables

Choose one or multiple nodes to view in the Enterprise graph canvas.

**Before you begin** — You can select an entire group or individual tables to view in the Enterprise Graph canvas. All the connected nodes or associated tables also get populated once you select the node. However, you can only choose up to 200 nodes at once. Role required: `admin`.

**Procedure:**

1. Navigate to **All > Knowledge Graph Designer > Open Enterprise Graph > Select multiple tables**. Choose up to 200 nodes to customize your view. Once you select a node, all the related edges will also be selected.
2. Select a group using the **By Tag** or **By Application** search bar. You can search and choose multiple groups and all the associated nodes. The selection will be listed in the Individual selection section.
3. Select an individual node using the **Individual Selection** search bar.
4. Select **Apply** to view these nodes and their related tables on the Enterprise Graph canvas.

### Test an Enterprise Graph schema

Promote functionality by entering a query and testing the Enterprise Graph schema.

**Before you begin** — Role required: `admin`

**Procedure:**

1. Navigate to **All > Knowledge Graph > Knowledge Graph Designer > Enterprise Graph**.
2. Select **Open your last view** to load and view the recently opened Enterprise Graph schema. The Enterprise graph schema opens in the Knowledge Graph canvas page.
3. From the toolbar, select **Test**. You are navigated to the Test Knowledge Graph Schema page.
4. In the **Query** section of the Test Knowledge Graph Schema window, enter your question.
5. Select an LLM model from the following:
   - NowLLM
   - Claude
   - NowLLM-LTS
   - Gemini
   - GPT
6. Select an Enterprise Graph mode. The options are:
   - Enterprise Graph
   - Enterprise Graph (Small)
7. Optional: Select the **Include conversation history** check box to add any previous chats.
8. Optional: Select the **Anchor Tables** check box to add the Anchor tables.
9. Optional: Select the **Tags** check box to add the associated tags. In Enterprise Graph (Small) mode, tags are mandatory.
10. Optional: Select **Group response by table** to sort the results.
11. Optional: Select **Show column properties in response** to view the column properties along with associated data.
12. Select **Run Query**.

## Figures, Diagrams & Screenshots

**Figure (p.1006):** Screenshot of the **"Create a copy of this Knowledge Graph Schema"** form (top of page). Fields shown: Display Name ("kg user graph copy"), Name (a name field, "coch"), Scope ("Global"), and Description (a multi-line description box containing text about a graph representing core tables like User, Department, Location, Company, Assets — "This Graph is Out of the Box used by Virtual Agent to answer employee queries in Natural Language"), with a character count and a **Create** button. This illustrates the copy-schema dialog referenced just before the Enterprise Graph topic.

**Figure (p.1014, top):** Screenshot of the **Knowledge Graph Designer** landing page (same overall layout as the designer home), showing the Enterprise Graph panel, a node-graph preview on the right, and listed schemas/tags. This illustrates Step 1 of creating a tag (navigating to the designer).

**Figure (p.1014, bottom):** Screenshot of the **Create New Tag** record page. It shows an "Add tag information" section with fields for Tag name, Description, and Scope, and a "Select Tables" area for choosing the tables/nodes to add to the tag, with a **Next** action. This illustrates Step 2 (entering tag information and selecting tables).

**Figure (p.1015):** Screenshot of the **Configure Tables** page (Step 4) for the **Incident** table. The left pane lists selected tables; the main area shows the Incident (incident) configuration with sections including "Table synonyms" (Add alternate names), "Column / edge configurations," "Data filters," and "Hidden columns." Several large circular **plus (+)** tiles ("No records added yet" / "Add new configuration") appear as empty-state add buttons for adding configurations, data filters, and hidden columns. A **Preview** / next control appears at the bottom right. This illustrates configuring table synonyms, AI instructions, data filters, and hidden columns for a tagged table.

**Figure (p.1017):** Screenshot of the **Edit Tag** view for the **VIRTUAL AGENT DEFAULT TAG**. The top shows "Edit Tag Information" with the tag name and an "Add tag information" section; below is a **Select Tables** section listing the tables that are part of the tag as chips/list, displayed over a Knowledge Graph canvas showing a node-edge graph of the tagged tables. This illustrates Step 2-3 of managing tags (opening a tag in the canvas and editing tag information / tables).

**Figure (p.1019, top):** Screenshot of the ServiceNow platform showing navigation to **All > Connections & Credentials > Connection & Credential Aliases**. The left flyout navigation lists Connection & Credential Aliases and related items; the main area shows a dashboard/home page with metric tiles (for example, "Open request item 91%," "Outstanding compliance," and numeric tiles "1...", "5", "4"). This illustrates Step 1 (navigating to Connection & Credential Aliases).

**Figure (p.1019, bottom):** Screenshot of a record form with **Create New Connection & Credential** available from the Related Links section. This illustrates Step 3 (creating a new connection and credential).

**Figure (p.1020):** Screenshot of the **Create Connection and Credential** form. It has two sections — "Please Enter the Connection Information" with **Connection name** ("Description Connector Connection") and **Instance URL** ("https://<name>.service-now.com") fields, and "Please Enter the Credential Information" with **Credential name** ("Description Connector Credential"), **User Name** ("Username for outbound authentication"), and **Password** ("Password for outbound authentication") fields, plus **Cancel** and **Create** buttons. This illustrates Steps 4-5 (entering connection/credential details and the user name/password).

**Figure (p.1021, top):** Screenshot of a **Data Sources** list (KG-related tables) within System Import Sets, showing rows such as KG Choice Picker Description, KG Column Picker Description, KG Table Picker Description, and KG Triplet Picker Description with their attributes (type, format, etc.). This illustrates Steps 6-7 (locating the KG data source tables).

**Figure (p.1021, middle):** Screenshot of a data-source record with the **Load All Records** action available from the Related Links section, used to load the import-set data. This illustrates Step 8.

**Figure (p.1021, bottom):** Screenshot of an **Import Set** record with the **Transform** action available from the Related Links section. This illustrates Steps 9-11 (running the transform).

**Figure (p.1022):** Screenshot of the **Enterprise Graph start page** ("Enterprise Graph — Explore, Test, and Contribute"). It shows a search bar to find/select a table and option tiles/cards such as "Open your last view," "Start with user tables," and "Select multiple tables," over a light background scattered with small connected-node graphics; the total number of nodes is displayed. This illustrates how to land on and navigate the Enterprise Graph start page.

**Figure (p.1023, top):** Screenshot of the **Enterprise Graph start page** (same "Explore, Test, and Contribute" layout as p.1022) with the search bar and the Open your last view / Start with user tables / Select multiple tables options. This illustrates Step 1 of viewing/managing the schema.

**Figure (p.1023, bottom):** Screenshot of the **Enterprise Graph canvas** with a schema loaded, centered on a **Building** node. The canvas shows a node-edge graph of connected tables with dashed/solid directional edges; a right-side panel shows node details/sections (Node details, Table filters, Columns that can be queried, Related nodes) for the selected node. This illustrates Step 2 (the Enterprise graph schema open in the Knowledge Graph canvas).

**Figure (p.1024):** Screenshot of the Enterprise Graph canvas in the **VIRTUAL AGENT DEFAULT TAG** view. A breadcrumb shows "Home > VIRTUAL AGENT DEFAULT TAG" with a tag drop-down. The canvas displays a node-edge graph of the tagged tables, with a right-side panel showing node/tag details. This illustrates the optional Step 3 (selecting a tag from the drop-down to view a specific tag) and node details (Steps 4-5).

**Figure (p.1025):** Screenshot of the **Select multiple tables** dialog/page. It shows a "Group selection" area with **By Tag** and **By Application** search bars, and an "Individual selection" area with an Individual Selection search bar, used to choose nodes (up to 200) to view, with an **Apply** action. This illustrates Steps 1-4 of selecting multiple tables.

**Figure (p.1026):** Screenshot of the **Test Knowledge Graph Schema** page with the **Enterprise Graph** badge. The top platform bar shows tabs (All, Favorites, History, Workspaces, Admin) with "Knowledge Graph" selected and a "Search or ask Now Assist" box. The left pane has a **Test Query** field containing "Who is my manager?", a **Model** drop-down set to **GPT**, an **Enterprise Graph Mode** drop-down set to **Enterprise Graph**, and check boxes: "Include conversation history," "Anchor Tables," "Tags," "Group response by table," and "Show column properties in response," with a blue **Run Query** button. The right pane shows an empty **Output response** area with a "?" icon and the prompt "Enter a query and run it to view response." This illustrates Steps 4-5 (entering a query and selecting the model).

**Figure (p.1027):** Screenshot of the same Test Knowledge Graph Schema page with the **Model** drop-down expanded, listing the LLM options: **NowLLM**, **Claude**, **NowLLM-LTS**, **Gemini**, and **GPT** (GPT is checked/selected). The Test Query "Who is my manager?" is visible above, and a **Run Query** button is below. This illustrates Step 5 (selecting an LLM model).

**Figure (p.1028):** Screenshot of the same Test Knowledge Graph Schema page with the **Enterprise Graph Mode** drop-down expanded, showing two options: **Enterprise Graph** ("Searches across all Tables") and **Enterprise Graph (Small)** ("Searches only within Tables in Tags (Runs faster)"). The "Show column properties in response" check box is visible below, with the **Run Query** button. This illustrates Step 6 (selecting an Enterprise Graph mode).
