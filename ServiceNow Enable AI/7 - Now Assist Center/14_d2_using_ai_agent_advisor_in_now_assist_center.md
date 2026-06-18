## Using AI Agent Advisor in Now Assist Center

> **Source document:** Now Assist Center  
> **Pages:** 28–35


4.Select the Instance health assessment card to view information about your instance status.
5. Select View assessment in the card of an individual assessment.
The View Assessment tab opens showing the detailed results of a readiness assessment for
the specified area of your instance. It shows the summary results of the checks performed and
lists the important tasks to achieve AI implementation readiness.
6.Optional: Filter the list of tasks as needed.
  - Select the category box and choose a category to filter by category.
  - Select any combination of the filter option buttons to filter by readiness status and task type.
7.Select the caret-down-outline icon ( ) to view the task details.

### What to do next

Resolve the reported issues to improve AI implementation readiness.

### Using AI Agent Advisor in Now Assist Center

Use AI Agent Advisor to automatically discover automation opportunities in your instance and
deploy AI agents to implement the automations.

AI Agent Advisor analyzes your instance data to identify where AI can improve outcomes and
efficiency. For each identified opportunity, it proposes AI agents that can automate the solution,
and generates new agents when no existing match is available.
Perform the following activities to use AI Agent Advisor in Now Assist Center.

### View your automation opportunities

Review the automation opportunities that AI Agent Advisor has identified for your instance.

### Before you begin

Automation discovery must be set up and an analysis run must be completed. For more
information, see Set up automation opportunity discovery for AI Agent Advisor.
Role required: sn_na_center.nac_admin

### About this task

After AI Agent Advisor completes an analysis, it produces a prioritized list of automation
opportunities based on your instance data. Follow these steps to review the identified
opportunities and assess which ones to act on.

### Procedure

1.Navigate to All > Now Assist Center or Workspaces > Now Assist Center.
2. Review the Automation opportunities section of the home page to see the top automation
opportunities.
Each card displays the estimated time and cost savings.

### Automation opportunities

3. Do one of the following:
a.Select Review opportunity in a card to view its details.
The Resolution Steps tab opens showing the opportunity details.

> **[Screenshot: Automation Opportunities Section with Six Example Cards]**
>
> The "Automation opportunities" section of the Now Assist Center home page. Above the section a dark hero card shows "Incident summarization" use case with "+ Activate" / "Dismiss" buttons. The AI Agent Advisor section shows heading "Automation opportunities" with subtitle about evaluating volume, costs, and time savings. Two control buttons: "Change advisor settings" (pencil) and "View all (181)". Six opportunity cards in a 3×2 grid each showing: title, source type badge (Interaction or Incident icon), "Est. cost savings per year" and "Est. time saved per year" in two columns, and "Review opportunity >" link. Cards: "Mac admin access via self-service or remote session" ($9,235,744 / 9,851,460 hrs), "ServiceNow SSO token failures and authentication escalation" ($7,003,772 / 7,470,690 hrs), "Active Directory password reset and account unlock procedures" ($4,540,907 / 4,843,634 hrs), "Travel request access resolved via correct form submission" ($4,463,943 / 4,761,539 hrs), "Account lockouts in ServiceNow and Okta due to access issues" ($4,079,120 / 4,351,061 hrs), "MDM and Entitlement Data Sync and Mapping Errors" (Incident, $4,050,000 / 4,320,000 hrs).


Opportunity details example
b.Select View all to view the complete list of automation opportunities.
The Automation opportunities tab opens showing a summary and a searchable list of all
automation opportunities.
Use the search field or the filter and sort controls adjust the list.
Automation opportunities list
c.Optional: Select a combination of sort, filter, and display options to refine the list.
▪Type in the search box and select the Submit search icon ( ) to filter by search criteria.
▪Select the filter button ( ), choose one or more filters, and select Apply.

> **[Screenshot: Opportunity Details Page — Account Lockouts]**
>
> The "Resolution Steps" workspace tab for "Account lockouts in ServiceNow and Okta due to access issues." Header shows: Type=Interaction, Updated=May 20, 2026. Description paragraph explains end-user account lockouts. Key metrics row: Records analyzed=53, Estimated cost saving per year=$4,079,120, Estimated time saved per year=4,351,061 hrs. "Learn how to" sidebar (right) with 3 numbered steps: 1. Review the following list of steps to plan for your AI agent, 2. Assess each AI tool for this plan, 3. Start building AI Agent in AI Agent Studio. Three tabs: "Resolution steps (18)", "Example records", "AI Agents (3)". Resolution steps panel shows a step: "Step 1: Agent verifies the user's account status in ServiceNow and/or Okta administration tools" with "Matched AI tool" label and confidence "High" badge. Tool card shows: "All tool / Chat" tabs, "Look up User Account Details by User ID" tool name, About/Why this is a match/Used in AI Agent descriptions, and a note "To enable this tool for your AI agent, install it from the ServiceNow Store. Install Now." A "Continue in AI Agent Studio" teal button appears bottom-right.
>
> **[Screenshot: Automation Opportunities List View]**
>
> The "Automation opportunities" full-list tab. Shows summary row: Opportunities=181, Records=3087, Estimated cost saving per year=$239,588,244, Estimated time saved per year=260,001,756 hrs. Below: a searchable sortable table. Columns: Name (hyperlink), Est. savings per year, Est. time saved per year, AI tools, Records analyzed, Type, AI agents created, Updated on. Rows include the same six opportunities listed above plus additional ones. Sort dropdown shows "Savings highest to lowest."


▪Select an option from a sort menu.
▪Select the List layout ( ) to display the opportunities in a list or Grid layout ( ) to show
them as stacked cards.

### What to do next

Implement an automation opportunity. For more information, see Implement an automation
opportunity from Now Assist Center.

### Implement an automation opportunity from Now Assist Center

Deploy a matched AI agent or a new agent to automate a resolution for an identified automation
opportunity.

### Before you begin

Role required: sn_na_center.nac_admin

### About this task

Follow these steps to implement an automation opportunity with AI Agent Advisor.
Each automation opportunity includes a set of recommended resolution steps that describe how
to automate the identified opportunity. AI Agent Advisor also maps each resolution step to an
existing AI agent on your platform when a match is available. Review the details of an opportunity
before deciding whether to deploy an agent for it.

### Procedure

1.Navigate to All > Now Assist Center or Workspaces > Now Assist Center.
2. In the Automation opportunities section of the home page or in the automation opportunities
list tab, select an automation opportunity to view its details.
The Resolution Steps tab opens showing the opportunity details.
The page displays summary information for the opportunity, a Resolution steps tab with
editable implementation steps, and an Example records tab with example records from the
data source. It also displays an AI Agents tab showing the agents created from the automation
opportunity.

Opportunity details page
For more information on finding an automation opportunity, see View your automation
opportunities.
3. Optional: Select the Example Records tab to review records from the source table.
(Optional) Select a record number to open the record and view its details.
4.Optional: Select the AI Agents tab to view AI agents created from the automation opportunity.
5. In the Resolution Steps tab, review the steps for accuracy and completeness in planning your
AI agent.
The Resolution Steps tab shows the implementation steps and the matched AI agents for
each step.
6.Optional: Adjust the steps as needed.
Option Description
Add a step
a.Select Add new step under the steps.
b.Enter the text and select Save.
Edit a step
a.Select the Edit icon ( ).
b.Change the text as needed and select
Save.
Delete a step
a.1. Select the Delete icon ( ).
b.2. Select Delete to confirm.

| Option | Description |
| --- | --- |
| Add a step | a.Select Add new step under the steps. b.Enter the text and select Save. |
| Edit a step | a.Select the Edit icon ( ). b.Change the text as needed and select Save. |
| Delete a step | a.1. Select the Delete icon ( ). b.2. Select Delete to confirm. |

Option Description
Reorder steps
(Optional) Select the Up icon ( ) or Down
icon ( ) to move the step in the list.
Restore all
(Optional) Select Revert all to restore the
original steps before changes.
Expand all
(Optional) Select Expand all to see the
available assets for each step.
In each applicable step, the description
provides the tool name, context, confidence
level, and rationale for matching the asset to
the step.
Select Collapse all to hide the details.
7.When the steps are ready to implement, select Continue in AI Agent Studio.
The Continue building AI agent box opens.

| Option | Description |
| --- | --- |
| Reorder steps | (Optional) Select the Up icon ( ) or Down icon ( ) to move the step in the list. |
| Restore all | (Optional) Select Revert all to restore the original steps before changes. |
| Expand all | (Optional) Select Expand all to see the available assets for each step. In each applicable step, the description provides the tool name, context, confidence level, and rationale for matching the asset to the step. Select Collapse all to hide the details. |

Continue building AI agent box
8.Choose whether the AI agent will communicate as a Chat Agent or Voice Agent.
9.Select Continue in AI Agent Studio.
The Agent guided setup tab opens.

> **[Screenshot: Continue Building AI Agent Box]**
>
> A modal dialog titled "Continue building AI Agent" with an × close button. Dark header area shows a circular-arrow/brain icon and "Now, let's build your AI Agent!" An info banner: "Some steps are missing a corresponding AI tool and will need a custom one." Below: "Select how the AI Agent will communicate" — two options: "Chat Agent" (selected, blue border, with chat icon) and "Voice Agent" (microphone icon). Left column "Here is what your AI Agent will include": AI agent description, role and steps (✓); 1 AI tools with strong match (✓); 1 AI tools with medium match (✓); 1 curated dataset for testing (✓). Right column "Recommended next steps": 1. Review your AI Agent's steps and tools; 2. Create 9 required custom AI tools; 3. Test AI Agent with curated data; 4. Deploy your AI Agent to production. Buttons: "Cancel" and teal "Continue in AI Agent Studio."


Agent guided setup tab
10.Complete the development of the new agent in the Agent guided setup tab using AI Agent
Studio capabilities.
The resolution steps are mapped to the set of instructions and added as tools for the new AI
agent.
For more information, see Create an AI agent.

### Edit an AI agent from an automation opportunity

Edit an AI agent that was created for an automation opportunity.

### Before you begin

An AI agent must created for the automation opportunity. For more information, see Implement
an automation opportunity.
Role required: sn_na_center.nac_admin

### Procedure

1.Navigate to All > Now Assist Center or Workspaces > Now Assist Center.
2. In the Automation opportunities section of the home page, do one of the following.
  - Select Review opportunity in a card to view its details.
  - Select View all to view the complete list of automation opportunities and select an
automation opportunity to view its details.
The Resolution Steps tab opens showing the opportunity details.
For more information on finding an automation opportunity, see View your automation
opportunities.
3. Select the AI Agents tab to view AI agents created from the automation opportunity.
The page displays the agents created from the automation opportunity on the AI Agents tab.

> **[Screenshot: Agent Guided Setup Tab in AI Agent Studio]**
>
> The "Agent guided setup" tab opened within Now Assist Center as "Account Access Restoration Agent - from AAA." Left progress sidebar shows steps: Define the specialty (✓ filled), Add tools and information, Define security controls (expanded: Define user access, Define data access), Add triggers, Select channels and status. Main panel "Define the specialty" section: text about writing a unique name and description. Fields shown: AI agent name = "Account Access Restoration Agent - from AAA"; AI agent description (multi-line text area with description about automating end-to-end restoration of user access). Character count: 1730 remaining. Below: "Define the role and required steps" section header with "View versions" button. Right sidebar: FAQs ("How does word choice matter?", "What's an example of a clear name?", "How do I define a role?") and Resources links. A "Save and continue" teal button at bottom-right.

