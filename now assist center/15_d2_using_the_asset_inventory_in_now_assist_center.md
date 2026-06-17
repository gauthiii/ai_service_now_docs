## Using the asset inventory in Now Assist Center

> **Source document:** Now Assist Center  
> **Pages:** 36–44


AI Agents tab on the resolution steps page
4.Select an AI agent to open it in Agent guided setup tab.
The Agent guided setup tab opens showing the AI agent details.
Agent guided setup tab
5. Edit the AI agent in the Agent guided setup tab using AI Agent Studio capabilities.
Select Save and continue to progress through the forms.
For more details on the guided setup forms, see Create an AI agent.

### Using the asset inventory in Now Assist Center

The asset inventory lists the AI assets in your instance.
These assets include Now Assist AI capabilities such as AI skills, AI agents, and AI agentic
workflows. They also include conversational components that you can use to build an LLM
conversation such as topics, subflows, actions, and virtual assistants. You can also view your
datasets, knowledge graphs, and catalog items in the asset inventory.

> **[Screenshot: AI Agents Tab on the Resolution Steps Page]**
>
> The AI Agents sub-tab of the Resolution Steps page for "Account access restoration after password changes." Metrics: Records analyzed=28, $2,155,007 cost savings/year, 2,298,674 hrs/year. The AI Agents tab label is active. Description: "These AI Agents were created from this automation opportunity and can be managed in AI Agent Studio." Table shows one row: AI Agent="Account Access Restoration Agent - from AAA" (hyperlink), Short description (text about automating end-to-end process), Status=Inactive, Agent type=Chat. A "Continue in AI Agent Studio" teal button appears at bottom-right.
>
> **[Screenshot: Agent Guided Setup Tab — Same Agent After Selecting]**
>
> The same "Account Access Restoration Agent - from AAA" agent opened in the Agent guided setup tab. Layout identical to page 35 screenshot with Define the specialty panel active.


Asset inventory

### View your AI assets in the asset inventory

Use the asset library to view the AI assets in your instance.

### Before you begin

Role required: sn_na_center.nac_admin

### About this task

Follow these steps to view the AI assets on your instance. AI assets include agents, agentic
workflows, skills, subflows, actions, virtual assistants, and topics. They also include datasets,
knowledge graphs, and catalog items.
For more information, see Now Assist AI assets.

### Procedure

1.Navigate to All > Now Assist Center or Workspaces > Now Assist Center.
2. Select Asset inventory ( ) in the side navigation bar.
The Asset inventory tab opens showing tabs for the various asset types.

> **[Screenshot: Asset Inventory — Overview Tab]**
>
> The "Asset inventory" workspace tab with a sub-tab bar: Overview (active), AI agents, Agentic workflows, Skills, Subflows, Actions, More ▾ (dropdown showing: Virtual assistants, Topics, Data assets, Catalog items, Knowledge graphs). A "Create asset" button in the top-right. The "Assets summary" section shows count cards: AI agents=129 (70 Active / 49 Inactive), Agentic workflows=36 (36 Active), Subflows=2 (2 Inactive), Actions=6 (6 Inactive), Virtual assistants=5 (3 Active / 2 Inactive), Topics=368 (330 Active / 38 Inactive), Data assets=3 (3 Published), Catalog items=105 (105 Active), Knowledge graphs=6 (2 Enterprise tag / 4 Graph schema). "Available assets 669" section below with filter tabs "All", "Recently created", "New from ServiceNow" and a Search box. Table columns: Asset name, Status, Asset type, Last updated, Description.


Asset inventory
3. Select the tab to view your AI assets for that type.
Select More to view and select additional tabs.
The asset inventory contains the following tabs.
Asset inventory tabs
Tab Description
Overview
Displays the total number of each asset type
and a full list of all assets in your instance.
Select the Recently created or New from
ServiceNow filters in the Discover assets
section to see new AI assets.

### Agents

Displays a list of all AI agents.
An AI agent is an autonomous digital worker
that uses LLMs, tools, and workflows to
complete tasks on behalf of users. They
can reason, plan, and act independently or
collaboratively.
Agentic workflows
Displays a list of all agentic workflows.
An agentic workflow is a structured sequence
of tasks executed by one or more AI agents

| Tab | Description |
| --- | --- |
| Overview | Displays the total number of each asset type and a full list of all assets in your instance. Select the Recently created or New from ServiceNow filters in the Discover assets section to see new AI assets. |
| Agents | Displays a list of all AI agents. An AI agent is an autonomous digital worker that uses LLMs, tools, and workflows to complete tasks on behalf of users. They can reason, plan, and act independently or collaboratively. |

> **[Screenshot: Asset Inventory — Overview Tab (second view same page)]**
>
> Same asset inventory screenshot as above, showing the same summary counts and the "Available assets" table structure.


Tab Description
with minimal human intervention to fulfill a
business objective.
Skills
Displays a list of all Now Assist skills.
A Now Assist skill is a capability that uses
generative AI to perform tasks such as
generating summaries, resolution notes, and
so on. You can have base system skills or
custom skills created in Now Assist Skill Kit.
Subflows
Displays a list of all subflows.
A subflow is an automated process that is
part of a larger automated process. It consists
of reusable actions and flow logic, data
inputs, and outputs.
Actions
Displays a list of all actions.
An action is a single step or task performed
by a an AI agent, a workflow, or a subflow.
Virtual assistants
Displays a list of all virtual assistants.
A virtual assistant is the container for the
end-to-end administrative configuration for a
chat or voice conversation.
Topics
Displays a list of all topics.
A conversational topic is used to structure
back-and-forth conversations between the
virtual agent and the end user.
Data assets
Displays a list of all datasets.
A custom dataset and data collection in Now
Assist Data Kit is used for evaluations in Now
Assist Skill Kit.
Catalog items
Displays a list of all catalog items.
A catalog item is used to publish a service to
users in the Service Catalog.
Knowledge graphs
Displays a list of all knowledge graphs.
A knowledge graph is a graphical
representation of real-world entities (tables)
and their relationships. It is used add context

| Tab | Description |
| --- | --- |
|  | with minimal human intervention to fulfill a business objective. |
| Skills | Displays a list of all Now Assist skills. A Now Assist skill is a capability that uses generative AI to perform tasks such as generating summaries, resolution notes, and so on. You can have base system skills or custom skills created in Now Assist Skill Kit. |
| Subflows | Displays a list of all subflows. A subflow is an automated process that is part of a larger automated process. It consists of reusable actions and flow logic, data inputs, and outputs. |
| Actions | Displays a list of all actions. An action is a single step or task performed by a an AI agent, a workflow, or a subflow. |
| Virtual assistants | Displays a list of all virtual assistants. A virtual assistant is the container for the end-to-end administrative configuration for a chat or voice conversation. |
| Topics | Displays a list of all topics. A conversational topic is used to structure back-and-forth conversations between the virtual agent and the end user. |
| Data assets | Displays a list of all datasets. A custom dataset and data collection in Now Assist Data Kit is used for evaluations in Now Assist Skill Kit. |
| Catalog items | Displays a list of all catalog items. A catalog item is used to publish a service to users in the Service Catalog. |

Tab Description
and meaning to information to enable
intelligent search, insights, and AI-driven
experiences.
4.Optional: Select a combination of sort and filter options to refine the list.
(Optional) The filters vary depending on the asset tab selected.
Filter and sorting controls
  - Select the Sort by button ( ) and select a sorting order.
  - Select a filter button.
  - Select an option from a filter menu.
  - Type in the search box and select the Submit search icon ( ) to filter by search criteria.
5. Optional: Change the columns that appear in the list table.
a.Select the Personalize columns button ( ).
(Optional) The Select columns to display box opens.
Select columns to display
b.Customize the columns as needed.

| Tab | Description |
| --- | --- |
|  | and meaning to information to enable intelligent search, insights, and AI-driven experiences. |

> **[Screenshot: Filter and Sorting Controls in Asset Inventory]**
>
> A narrow filter bar for the Skills tab of the asset inventory. Pill/badge filters: "All (143)", "Active (96)", "Inactive (3)", "Not configured (44)". Then a Search box. Dropdown menus: "All workflows ▾", "All products ▾", "All features ▾". Sort button (↕) and column-personaliser (⊞) icons on the right.
>
> **[Screenshot: Select Columns to Display Modal]**
>
> A modal dialog "Select columns to display" with subtitle "Customize your view by selecting columns and arranging them in your preferred order." Left pane "Available columns (9)" with a search box and checkboxes: Skill (✓), Status (✓), Workflow (✓), Product (✓), Feature (✓), Skill type (✓), LLM provider (✓), Last updated (✓), Description (unchecked). Right pane "Selected columns (8)" shows draggable rows: Skill ×, Status ×, Workflow ×, Product ×, Feature ×, Skill type × (partial list). Buttons at bottom: "Reset to defaults", "Cancel", "Apply".


▪Select an option in the Available columns panel to add the column to your list. Deselect
an option to remove it.
▪Select the Remove items icon ( ) on an item in the Selected columns panel to remove it
from your list.
▪Drag one or more columns to a different location in the Selected columns panel to change
the order in which they appear in your list.
Columns ordered from top to bottom in the panel appear from left to right in the list table.
▪Select Reset to defaults to restore the column configuration before your changes.
c.Select Apply.
6.Optional: In the Overview tab, use the Available assets section to find the new AI assets on
your instance.
  - Select the Recently created filter to see all AI assets you created in the last 30 days.
  - Select the New from ServiceNow filter to see all base system assets provided by
ServiceNow within the last 90 days.
7.Optional: Select the asset name in the list to view the asset details.
(Optional) The asset details page may open on a separate workspace tab if the selected asset
is managed using an application that is fully integrated in Now Assist Center. If it is managed in
another application, the application opens to the asset details page.

### Create an AI asset in the asset inventory

Use the asset library to create AI assets in your instance.

### Before you begin

Role required: sn_na_center.nac_admin

### About this task

Follow these steps to create an AI asset.
From the asset inventory, asset types are created by opening their respective application.
- Create agents and agentic workflows with AI Agent Studio.
For more information, see AI Agent Studio.
- Create Virtual Agent assets with Virtual Agent Assistant Designer, including topics, virtual
assistants, subflows, and actions.
For more information, see Assistant Designer .
- Create custom skills with Now Assist Skill Kit.
For more information, see Now Assist Skill Kit.
- Create datasets with Now Assist Data Kit.
For more information, see Now Assist Data Kit.
- Create catalog items with Catalog Builder.
For more information, see Catalog Builder .

- Create knowledge graphs with Knowledge Graph Designer.
For more information, see Knowledge Graph.

### Procedure

1.Navigate to All > Now Assist Center or Workspaces > Now Assist Center.
2. Select Asset inventory ( ) in the side navigation bar.
The Asset inventory tab opens.
3. Select the Create asset button.
The Create asset box opens showing the following options for the asset type.
Options in the Create asset box
Asset type Description
AI agent
Opens the New AI Agent form in AI Agent
Studio.
An AI agent is an autonomous digital worker
that uses LLMs, tools, and workflows to
complete tasks on behalf of users. They
can reason, plan, and act independently or
collaboratively.
For more information on creating an AI agent
in AI Agent Studio, see Create an AI agent.

| Asset type | Description |
| --- | --- |
| AI agent | Opens the New AI Agent form in AI Agent Studio. An AI agent is an autonomous digital worker that uses LLMs, tools, and workflows to complete tasks on behalf of users. They can reason, plan, and act independently or collaboratively. For more information on creating an AI agent in AI Agent Studio, see Create an AI agent. |

> **[Screenshot: Create Asset Modal Dialog]**
>
> A "Create asset" modal with × close button. Four option rows each with an icon, asset type name (bold), description, and a contextual badge:
> - **AI agent** (robot/gear icon) "Uses prompts to LLMs to independently form thoughts and take actions on its own." Badge: "AI Agent Studio ↗". Examples: "Categorize incidents | Notify users via Twilio | Generate post-incident reviews"
> - **Agentic workflow** (circular arrow icon) "Uses a group of AI agents that work together to independently solve problems." Badge: "AI Agent Studio ↗". Examples: "Resolve a major incident | Generate resolution plans | Automate document Q&A"
> - **Custom skill** (crossed-scissors/wand icon) "Uses prompts to large language models (LLMs) to interpret the language in users' requests and provide outputs when requested." Badge: "Now Assist Skill Kit ↗". Examples: "Summarize documents | Generate change request plans | Update ticket statuses"
> - **Subflow** (branch/node icon) "Used for a limited set of steps that are part of a larger automated process." (no badge). Examples: "Delegate roles | Verify user identity | Capture incident details"


Asset type Description
Agentic workflow
Opens the New agentic workflow form in AI
Agent Studio.
An agentic workflow is a structured sequence
of tasks executed by one or more AI agents
with minimal human intervention to fulfill a
business objective.
For more information on AI Agent Studio, see
Create an agentic workflow.
Custom skill
Opens the Now Assist Skill Kit home page.
A skill is a self-contained unit of generative
AI functionality that runs a prompt against
a large language model (LLM) and returns a
response.
For more information, see Create a skill.
Subflow
Opens the New Subflow form in Assistant
Designer.
A subflow is an automated process that is
part of a larger automated process. It consists
of reusable actions and flow logic, data
inputs, and outputs.
For more information on creating an asset in
Virtual Agent Designer, see Getting started
with Virtual Agent Designer .
Action
Opens the New Action form in Assistant
Designer.
An action is a single step or task performed
by a an AI agent, a workflow, or a subflow.
For more information on creating an asset in
Virtual Agent Designer, see Getting started
with Virtual Agent Designer .
Virtual assistant
Opens the Create an assistant page in
Assistant Designer.
A virtual assistant is the container for the
end-to-end administrative configuration for a
chat or voice conversation.
For more information on creating a virtual
assistant in Assistant Designer, see
Configuring assistants overview .

| Asset type | Description |
| --- | --- |
| Agentic workflow | Opens the New agentic workflow form in AI Agent Studio. An agentic workflow is a structured sequence of tasks executed by one or more AI agents with minimal human intervention to fulfill a business objective. For more information on AI Agent Studio, see Create an agentic workflow. |
| Custom skill | Opens the Now Assist Skill Kit home page. A skill is a self-contained unit of generative AI functionality that runs a prompt against a large language model (LLM) and returns a response. For more information, see Create a skill. |
| Subflow | Opens the New Subflow form in Assistant Designer. A subflow is an automated process that is part of a larger automated process. It consists of reusable actions and flow logic, data inputs, and outputs. For more information on creating an asset in Virtual Agent Designer, see Getting started with Virtual Agent Designer . |
| Action | Opens the New Action form in Assistant Designer. An action is a single step or task performed by a an AI agent, a workflow, or a subflow. For more information on creating an asset in Virtual Agent Designer, see Getting started with Virtual Agent Designer . |
| Virtual assistant | Opens the Create an assistant page in Assistant Designer. A virtual assistant is the container for the end-to-end administrative configuration for a chat or voice conversation. For more information on creating a virtual assistant in Assistant Designer, see Configuring assistants overview . |

Asset type Description
Topic
Opens the Create a topic form in Assistant
Designer.
A conversational topic is used to structure
back-and-forth conversations between the
virtual agent and the end user.
For more information on creating an asset in
Virtual Agent Designer, see Getting started
with Virtual Agent Designer .
Catalog item
Opens the Catalog Builder.
A catalog item is used to publish a service to
users in the Service Catalog.
For more information on creating a catalog
item in Catalog Builder, see Catalog Builder .
Data asset
Opens a Create data asset box.
Choose one of the following options.
  - Import and create data
Opens the Create dataset form in Now
Assist Data Kit.
  - Generate synthetic data
Opens the Now Assist Data Kit home page.
A custom dataset and data collection in Now
Assist Data Kit is used for evaluations in Now
Assist Skill Kit.
For more information on creating a dataset
in Now Assist Data Kit, see Using Now Assist
Data Kit.
Knowledge Graph
Opens Knowledge Graph Designer home
page.
A knowledge graph is a graphical
representation of real-world entities (tables)
and their relationships. It is used add context
and meaning to information to enable
intelligent search, insights, and AI-driven
experiences.
For more information on creating a
knowledge graph in Knowledge Graph
Designer, see Using Knowledge Graph
Designer.

| Asset type | Description |
| --- | --- |
| Topic | Opens the Create a topic form in Assistant Designer. A conversational topic is used to structure back-and-forth conversations between the virtual agent and the end user. For more information on creating an asset in Virtual Agent Designer, see Getting started with Virtual Agent Designer . |
| Catalog item | Opens the Catalog Builder. A catalog item is used to publish a service to users in the Service Catalog. For more information on creating a catalog item in Catalog Builder, see Catalog Builder |
| Data asset | Opens a Create data asset box. Choose one of the following options. ◦Import and create data Opens the Create dataset form in Now Assist Data Kit. ◦Generate synthetic data Opens the Now Assist Data Kit home page. A custom dataset and data collection in Now Assist Data Kit is used for evaluations in Now Assist Skill Kit. For more information on creating a dataset in Now Assist Data Kit, see Using Now Assist Data Kit. |
| Knowledge Graph | Opens Knowledge Graph Designer home page. A knowledge graph is a graphical representation of real-world entities (tables) and their relationships. It is used add context and meaning to information to enable intelligent search, insights, and AI-driven experiences. For more information on creating a knowledge graph in Knowledge Graph Designer, see Using Knowledge Graph Designer. |
