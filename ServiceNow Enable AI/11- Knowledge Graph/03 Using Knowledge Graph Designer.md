# Using Knowledge Graph Designer

_Source: ServiceNow Now Assist documentation, pages 994-1005._

## Overview

Use Knowledge Graph Designer to create customized Knowledge Graph schemas that consist of nodes and edges. Knowledge Graph schemas are the customized Knowledge graphs that consist of nodes and edges.

Like tables, nodes also denote and store details about entities such as user, location, and department. You can add nodes to the Knowledge Graph schema so that the system can reach out to all the relevant tables to fetch the data. You can also edit node properties such as data source, start node, end node, and connected nodes. Knowledge Graph enables you to select the node columns that can be queried.

The relationship or connections between these nodes are referred to as edges. You can select and edit the connecting edges and available edges for each node.

With Knowledge Graph Designer, you can create, edit, duplicate, or delete a Knowledge Graph schema. Apart from ServiceNow tables, you can also create a Knowledge Graph schema using Workflow Data Fabric tables to retrieve data from different systems in real time without moving it. There's also an option to test a Knowledge Graph schema by generating and running a query.

This subtopic covers viewing schemas, creating a schema, editing a schema, managing nodes, adding or deleting edges, testing a schema, analyzing logs for debugging, and copying a schema.

## Features

- Create, edit, duplicate (copy), or delete a Knowledge Graph schema.
- Add and edit nodes (entities/tables), including node synonyms and node descriptions.
- Select the node columns that can be queried.
- Add table filters to control which records appear in query results, with optional condition sets and the ability to apply filters to child tables.
- Add, edit, or delete edges (relationships) that connect nodes, including connecting edges and available edges.
- Create schemas from ServiceNow tables or external Workflow Data Fabric tables (if integrated).
- Test a Knowledge Graph schema by generating and running a query against a selected LLM.
- Analyze Knowledge Graph logs and history for debugging.
- Copy a prebuilt or existing schema for further customization.

## Functionalities

### View Knowledge Graph schemas

By default, ServiceNow-published Knowledge Graph schemas are available with the product. You can view the prebuilt schemas provided by ServiceNow, or the schemas created by your organization admin. There are currently two prebuilt schemas available that are read-only but can be cloned and edited:

1. User profile schema
2. Employee schema

### Create a Knowledge Graph schema — Edit Knowledge Graph Schema details form

| Field | Description |
|---|---|
| Display Name | Display name for the Knowledge Graph schema. |
| Name | Optional name for the Knowledge Graph schema. |
| Scope | Scope used when creating the Knowledge Graph schema. This field is read-only. |
| Description | Knowledge Graph schema overview to provide additional information to users. |

When creating a schema you can use ServiceNow tables or external Workflow Data Fabric tables. After creating, you add the following details in the navigation pane:

- **Node details section:** Add node synonym, Node description.
- **Table filters section:** Add filters to set rules that control which records are shown in query results. Provide Field, Operator, Value; optionally Add Condition set (alternative filter condition); and optionally check **Apply filters to child tables** to add the same filter conditions for the child table of the selected table in the graph.
- **Columns that can be queried section:** Search for and select the desired columns.
- **Related nodes section:** Add, delete, or edit edges.

### Edit a Knowledge Graph schema — Edit Knowledge Graph Schema details form

| Field | Description |
|---|---|
| Display Name | Display name of the Knowledge Graph schema. |
| Name | Name of the Knowledge Graph schema. |
| Scope | Scope used to create the Knowledge Graph schema. |
| Description | Knowledge Graph schema overview for users. |

### Edges (Related nodes section)

Each related node displays a list of **connecting edges** and **available edges**. To establish a connection, select the plus icon against an available edge to move it to Connecting edges. Selecting an edge shows its parent node and grandparent nodes in the hierarchy. To reconfigure a connecting edge, use the edit icon and update the **Edge type** and **Edge description**. To delete an edge, use the remove edge control.

### Test a Knowledge Graph schema — options

LLM model options when testing:

- NowLLM
- Claude
- Gemini
- GPT

Optional test settings:

- **Include conversation history** check box — adds any previous chats.
- **Group response by table** — sorts the results.
- **Show column properties in response** — view the associated properties.

### Analyze Knowledge Graph logs for debugging

The `sn_kg.log.level` system property controls logging. The default value is **Err**, but you can use any of the following values: emerg, alert, crit, err, warning, notice, info, debug. After setting, the logs are added to syslog.

### Create a copy of a Knowledge Graph schema — form

| Field | Value |
|---|---|
| Display Name | Existing name of the Knowledge Graph schema. |
| Name | Name of the cloned Knowledge Graph schema. |
| Scope | Scope under which you want to create the Knowledge Graph schema. |
| Description | Knowledge Graph schema overview for users. |

## Instructions / Procedures

### Create a Knowledge Graph schema

Create a customized Knowledge Graph schema that will be used by Virtual Agent, AI Agents, and Now Assist Panel.

**Before you begin** — Role required: `kg_admin`

**Procedure:**

1. Navigate to **All > Knowledge Graph > Knowledge Graph Designer**. The UI displays a list of all the Knowledge Graph schemas on the landing page.
2. Start creating a Knowledge Graph schema by selecting **Create New**.

   > **Note:** You can create a Knowledge Graph schema using ServiceNow tables or the external Workflow Data Fabric tables.
3. On the form, fill in the fields (Display Name, Name, Scope [read-only], Description).
4. Select **Create**. The "Add nodes to the Knowledge graph schema" window is displayed.
5. Enter or search for the nodes that you want to add to the Knowledge Graph schema and select **Add**. (You can search and select the Workflow Data Fabric tables, if integrated.) The Knowledge Graph schema is created and displayed on the Knowledge Graph canvas.
6. In the navigation pane, add the required details.
7. In the **Node details** section, you can add or edit the following fields:
   - Add node synonym
   - Node description
8. In the **Table filters** section, view and add filters to set rules that control which records are shown in query results. To add table filters, provide the following information:
   - Field
   - Operator
   - Value
   - Add Condition set: optional field to add an alternative filter condition.
   - Apply filters to child tables: optional check box to add the same filter conditions for the child table of the selected table in the graph.
9. In the **Columns that can be queried** section, search for and select the desired columns and select **Save**.
10. Add, delete, or edit edges in the **Related nodes** section and select **Save**.

### Edit a Knowledge Graph schema

**Before you begin** — Role required: `kg_admin`

**Procedure:**

1. Navigate to **All > Knowledge Graph > Knowledge Graph Designer**. The UI displays a list of all the Knowledge Graph schemas on the landing page.
2. From the list of existing Knowledge Graph schemas, select a Knowledge Graph schema to edit. The Knowledge Graph schema opens in the Knowledge Graph canvas.
3. Select the edit icon.
4. On the form, fill in the fields (Display Name, Name, Scope, Description).
5. To save the changes, select **Save**.
6. Delete all the changes made to the Knowledge Graph schema by selecting **Discard**.

### Manage nodes in a Knowledge Graph schema

Add or delete a node from an existing Knowledge Graph schema.

**Before you begin** — Role required: `kg_admin`

**Procedure:**

1. Navigate to **All > Knowledge Graph > Knowledge Graph Designer**. The UI displays a list of all the Knowledge Graph schemas on the landing page.
2. Select a Knowledge Graph schema from the list. The Knowledge graph schema opens in the Knowledge Graph canvas page.
3. From the toolbar, select the **Add nodes** option. The Edit Knowledge Graph Schema details form is displayed.
4. In the "Add nodes to Knowledge graph schema" window, enter or search for the nodes that you want to add to the Knowledge Graph schema. (You can search and select the Workflow Data Fabric tables, if integrated.)
5. Select **Add**. The nodes are added to the Knowledge Graph schema and displayed on the Knowledge Graph canvas.
6. Select the node to update the node details in the side navigation pane.
7. Select **Save** to save your changes.
8. Select **Remove node** to delete a node from the schema.

### Add or delete edges to a Knowledge Graph schema

Add, edit, or delete edges that connect the nodes to customize a Knowledge Graph schema.

**Before you begin** — Role required: `kg_admin`

**Procedure:**

1. Navigate to **All > Knowledge Graph > Knowledge Graph Designer**. The UI displays a list of all the Knowledge Graph schemas on the landing page.
2. Select a Knowledge Graph schema from the list. The Knowledge Graph schema opens in the canvas.
3. From the Knowledge Graph schema, select a node to edit.
4. In the side navigation pane, select **Related nodes**. Each related node displays a list of connecting edges and available edges.
5. To establish a connection to an available edge, select the plus icon against the edge. The available edge is moved to **Connecting edges**. Select an edge to see its parent node and grandparent nodes in the hierarchy.
6. To reconfigure a connecting edge, select the edit icon and update the following:
   - Edge type
   - Edge description
7. To delete an edge and move it to available edges, select the remove edge control.
8. To delete the edge, select **Remove edge** when prompted.
9. To save your changes, select **Save**, or to undo all your changes, select **Discard**.

### Test a Knowledge Graph schema

Promote functionality by entering a query and testing the Knowledge Graph schema.

**Before you begin** — Role required: `kg_admin`

**Procedure:**

1. Navigate to **All > Knowledge Graph > Knowledge Graph Designer**. The UI displays a list of all the Knowledge Graph schema on the landing page.
2. From the list of Knowledge Graph schemas, select the Knowledge Graph that you want to test. The Knowledge Graph schema opens in the canvas.
3. From the toolbar, select **Test**.
4. In the **Query** section of the Test Knowledge Graph Schema window, enter your question.
5. Select an LLM model from the following:
   - NowLLM
   - Claude
   - Gemini
   - GPT
6. Optional: Select the **Include conversation history** check box to add any previous chats.
7. Optional: Select **Group response by table** to sort the results.
8. Optional: Select **Show column properties in response** to view the associated properties.
9. Select **Run Query**.

### Analyze Knowledge Graph logs for debugging

Review Knowledge Graph logs and history to analyze performance and diagnose issues.

**Before you begin** — Ensure that you do not make any changes to the production instance. Role required: `admin`.

**Procedure:**

1. Navigate to **All > sys_properties.list > sn_kg.log.level** or **All > System Properties > All Properties > sn_kg.log.level**.
2. Open `sn_kg.log.level` and in the value field add `debug`. The default value is **Err**, but you can use any of the following values:
   - emerg
   - alert
   - crit
   - err
   - warning
   - notice
   - info
   - debug
3. Select **Update**. The logs will now be added to syslog.

### Create a copy of a Knowledge Graph schema

Create a copy of a Knowledge Graph schema and duplicate it for further customization.

**Before you begin** — Verify that you have not selected a ServiceNow prebuilt Knowledge Graph schema that is non-editable. Verify that the scope selected when creating a Knowledge Graph schema is the same as the scope of the existing Knowledge Graph schema. Role required: `kg_admin`.

**Procedure:**

1. Navigate to **All > Knowledge Graph > Knowledge Graph Designer**. The UI displays a list of all the Knowledge Graph schemas on the landing page.
2. Select a Knowledge Graph schema.
3. Select the more icon.
4. Select **Copy Graph**. Verify that the scope of the existing Knowledge Graph schema is the same as the new schema.
5. On the form, fill in the fields (Display Name, Name, Scope, Description).
6. Select **Create**.

## Figures, Diagrams & Screenshots

**Figure (p.996):** Screenshot of the **User Graph** read-only Knowledge Graph schema open in the Knowledge Graph canvas. The top platform bar shows tabs (All, Favorites, History, Workspaces, Admin) with "Knowledge Graph" selected and a Search box. A breadcrumb reads "Home > User Graph," with **Test Schema** and **Copy Graph** buttons at the top right. An information banner states: "This is a read-only Knowledge graph schema, published by ServiceNow." The canvas is a node-edge graph centered on a highlighted **User** node, connected by dashed directional edges labeled with relationship names to surrounding nodes: **Asset** (edge "Assigned to"), **Location** (edge "Location"), **Company** (edge "Company"), **Department** (edge "Department"), and **Manager** (edge "Manager"). A right-side panel for **User** lists collapsible sections: Node details, Table filters, Columns that can be queried, and Related nodes. A zoom control reads 88%. This illustrates the canvas layout and how node properties are edited in the side pane (Step 6-7).

**Figure (p.997):** Screenshot of the **Department** node detail side panel. It shows a trash/delete icon, the **Node details** section expanded with: Source node = `cmn_department`, Display name = Department, an "Add node synonym" field ("Enter synonym," Characters left: 40) with a tag chip "Department," and a "Node description" field containing `cmn_department` (Characters left: 3986). Collapsed sections "Columns that can be que..." and "Related nodes" appear below. This illustrates the Node details fields (Step 7) — adding node synonyms and node descriptions.

**Figure (p.998):** Screenshot of the **User** node side panel focused on the **Table filters** section (expanded, with an edit pencil icon). It shows a "Filters" area containing the condition `active=true`. Collapsed "Columns that can be queried" and "Related nodes" sections appear below; a "Node details" header shows an "Enter a label" tooltip. This illustrates the Table filters section (Step 8) used to control which records appear in query results.

**Figure (p.999):** Screenshot of the **Department** node side panel focused on the **Columns that can be queried** section (highlighted/expanded). It shows a "Search for columns" box and a checkbox list of columns, several marked with an "E..." (edge) tag: Business unit, Company, Cost center, Department head, **Description** (checked, with edit pencil), **Head count** (checked, edit pencil), **ID** (checked, edit pencil), Name, Parent (tagged "Edge"), Parent HP1, Primary contact, and sys_created_by (partially visible). This illustrates selecting which columns can be queried (Step 9).

**Figure (p.1000):** Screenshot of the **Related nodes** section (expanded) showing two related-node cards. The first card, **Fast Fact Mg2 DF**, lists "Connecting edges (1)" with an edge "Manager employee number" (with link and trash icons) and "Available edges (0)." The second card, **User**, lists "Connecting edges (1)" with an edge "Employee number" and "Available edges (0)." This illustrates the Related nodes / edges section (Step 10) where edges are added, deleted, or edited.

**Figure (p.1001):** Screenshot of the **Discard changes** confirmation dialog overlaid on the Edit Knowledge Graph Schema details form. The dialog reads: "By clicking on discard, all changes made to this graph schema will be discarded. Are you sure you want to discard all changes? This action cannot be reversed," with **Cancel** and **Discard** buttons. This illustrates Step 6 of editing a schema (discarding changes).

**Figure (p.1002, top):** Screenshot of the **Add nodes to Knowledge graph schema** window. It shows a search field "Search for tables available within ServiceNow system" with two selected table chips — "User (sys_user)" and "Incident (incident)" — and an **Add** button. This illustrates Step 4 of managing nodes (searching/selecting nodes to add).

**Figure (p.1002, bottom):** Screenshot of the **Remove node** confirmation dialog. It reads: "By removing the node, both the node and their associated edges will be removed from the schema. Are you sure you want to continue?" with **Cancel** and **Remove Node** buttons. This illustrates Step 8 of managing nodes (deleting a node).

**Figure (p.1003):** Screenshot of the **Related nodes** section (same layout as p.1000) showing the **Fast Fact Mg2 DF** card with Connecting edges (1) "Manager employee number" and Available edges (0), and the **User** card with Connecting edges (1) "Employee number" and Available edges (0). This illustrates establishing, reconfiguring, and removing edges (Steps 5-7 of adding/deleting edges), referencing the plus, edit, and remove-edge icons.

**Figure (p.1004):** Screenshot of the **Test Knowledge Graph Schema** window/page within the Knowledge Graph Designer. The left pane shows the query/configuration controls — a query input field, an LLM model selector, and check-box options such as "Include conversation history," "Group response by table," and "Show column properties in response," with a Run Query action. The right pane displays the query response output as structured/JSON-like results. This illustrates the schema-testing workflow (Steps 4-9).

**Figure (p.1005):** No standalone screenshot. The page is largely text — it lists the remaining `sn_kg.log.level` values (emerg, alert, crit, err, warning, notice, info, debug) and the Create a copy of a Knowledge Graph schema form table (Display Name, Name, Scope, Description). Only the decorative ServiceNow header logo appears as a graphic.
