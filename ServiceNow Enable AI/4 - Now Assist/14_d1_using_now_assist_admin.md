# Using Now Assist Admin

_Source pages: 156–178 | Depth: 1_

---

<!-- page 156 -->
◦To create a new granular feedback selection, select New.
◦To change an existing granular feedback option, select the option.
12. Enter or change the fields: Description, Message, Message Key, Bundle Id, Application, Active,
Order.
13.Select Submit.
14.To access the stored feedback data, in the filter navigator field, enter
sys_ci_analytics.list to display the CI Analytics table.
15.Select the appropriate entry to view the feedback data.
Configure processing messages
For Now Assist panel premium chat, configure processing messages to control the status
updates that appear in the chat interface while Now Assist works on a request. You can
customize the text of processing messages to better reflect your organization's terminology or
the specific actions your AI agents perform.
Before you begin
Role required: admin
Procedure
1.In the filter navigator field, enter sys_properties.list.
2. In the selection fields, select Name from the drop-down list and enter
processing_messages in the Search field.
3. If you have Now Assist panel premium chat, configure
sn_aia.og_ao.enable_processing_messages to enable or disable processing messages.
Using Now Assist Admin
Use Now Assist Admin to explore the various Now Assist plugins, skills and associated
Generative AI application features you are entitled to.
Now Assist skill details
Explore details of Now Assist skills, security and usage data.
Explore details about various skills within a workflow. This page contains information about skill,
usage and consumption information, and a summary of security and governance data.
Note: The minimum version required to access the skill details page is Zurich patch 10
and Australia patch 3.

<!-- page 157 -->
The View details option displays skill details under these tabs:
•Overview: General description of the skill
•Usage: Details about the skill usage, adoption and AI assist consumption. The report on total
execution, active users and executions across channels can be exported in .csv or excel
format.
◦Total executions: Count of the number of times the selected skill is executed
◦Active users: Total number of unique users who have utilized this skill

<!-- page 158 -->
◦Executions by channel: Distribution of skill execution across diverse channels
◦Assist consumption: The total number of AI assists utilized throughout the executions of this
skill in a given date range
•Security and governance- Manage various security and governance aspects of skill details like
model provider, ACLs, guardrails and other data privacy policies, as illustrated in the example.
Activate a Now Assist skill
Configure the triggers, settings, and display locations for Now Assist skills to enable GenAI
capabilities across the ServiceNow AI Platform.
Before you begin
Role required: sn_generative_ai.nsa_admin
About this task
Activate the skills that are most relevant to your use cases and business needs. For a full list
of available skills, see Now Assist skills. After the skills have been activated, they’re accessible
across the ServiceNow AI Platform based on the availability and display settings you choose.
Procedure
1.Navigate to All > Now Assist Admin Console > Features.
If you’re already in the Now Assist Admin console, select the Now Assist Features tab.
2. On the navigation panel, select a workflow, such as Technology.
Each workflow contains feature sets.
3. On the feature card that is associated with the skill you'd like to activate, select View details.
4.In the All available skills section, select Activate Skill.
5. In the first step of the skill configuration, determine which inputs or triggers that you want to
associate with the skill.
Each skill configuration has steps that are shown in the guided setup. The exact steps vary
from skill to skill. A symbol next to each step indicates whether the step is completed, partially
completed, or not completed. After configuring a step, select Save and continue to go to the
next step. Return to a previous step by selecting Back.

<!-- page 159 -->
Note: Some configuration options are read only.
6.After you've configured the current step, select Save and continue to go to the next step.
7.Optional: For some skills, the next step is to define the availability.
(Optional) You can select Skill is always available if you do not want to place any restrictions
on when the skill is available for use. If you want to add conditions, select Customize skill
availability. Selecting this option opens up a condition builder for you to select fields and
values that determines whether someone can use the skill.
8.In the next step of the skill configuration, select where you'd like to display the skill.
Options vary from skill to skill. Some options are only available for certain skills.

<!-- page 160 -->
◦In-product desktop: When selected, Now Assist skills are displayed on forms and
workspaces.
◦Now Assist panel: When selected, Now Assist skills are available in the Now Assist panel. If
you don't see this option, you must activate the Now Assist panel. For more information, see
Activate the Now Assist panel standard chat.
◦Core UI: When selected, the Now Assist skill will display as a UI action in the Core UI.
Select the down arrow next to the Display toggle to select the roles that can use the skill. Roles
can be added by entering the name of the role in the User roles field. Existing roles can be
removed by selecting the X icon in the role bubble. You must have at least one role specified,
but you can add as many as you like.
9.Review your choices and select Activate to complete the configuration.
What to do next
Use the Now Assist applications and skills that you've activated.
Configure chat summarization and chat reply recommendation skills in the Now Assist Admin
console
Define the triggers, inputs, and display location for chat summarization and chat reply
recommendation by using the guided setup in the Now Assist Admin console. The activation
steps are conceptually same for both the skills.
Before you begin
Role required: sn_generative_ai.nsa_admin

<!-- page 161 -->
Procedure
1.Navigate to All > Now Assist Admin Console > Features.
If you’re already in the Now Assist Admin console, select the Now Assist Features tab.
2. On the navigation panel, select a workflow that has chat recommendation, either Technology
or Customer.
Each workflow contains feature sets.
3. On the Chat feature card, select View details.
4.In the All available Chat skills section of the chat recommendation card, select Activate Skill.
5. Go to Define Trigger, the first step in the guided setup.
By default, many of the options in the setup are configured for the most common use cases.
You might need to select the step in the guided setup navigation to go back and change the
configurations in previous steps. You can also use Back to navigate through the steps.
6.Using the toggles, select the actions trigger the chat recommendation skill.
Define triggers for chat recommendation
7.Using the toggles, select the actions trigger the chat summarization skill.

<!-- page 162 -->
Define triggers for chat summarization
8.Select whether you want the summary to be formatted with bullet points.
By default, the summaries are written with bullet points, but you can turn off this format so that
the generated summary uses paragraphs instead.
9.Go to Define availability, the next step, by selecting Save and continue.
10.Customize when and how the skill capability will exist and be available.
11. Select Customize skill availability if you want to define the skill to be available for a certain
domain.
12. Go to Choose Input, the next step, by selecting Save and continue.
13.Select any additional data sources that you want the Large language model (LLM) to take into
account when generating a recommendation.

<!-- page 163 -->
14.Select a portal for the data source to allow chat summarization/recommendation to be
generated for the conversation occurring on that portal.
This is a mandatory step. The admin must specify a portal and enable a specific channel on
Choose Input page, to enable the skill for chats sent in the selected portal/channel. Else the
agent will receive an error message, "Chat summaries won't appear until your IT administrator
completes all the required steps involved in the setup".
15.Select Save and continue.
16. Go to Select display, the last step, and select where you would like to display the skill.
You can select both in-product, Now Assist panel, or both.
Note: Chat recommendation is not available in the Now Assist panel.
◦In-product desktop: When selected, Now Assist skills are displayed on forms and
workspaces.
◦Now Assist panel: When selected, Now Assist skills are available in the Now Assist panel.
Select the down arrow to identify the roles that can use the skill. Select the arrow next to
toggle, to select roles who can access the skill. You can add roles by entering the name of
the role in the User roles field. You can remove existing roles by selecting the X icon in the
role bubble. You must have at least one role specified, but you can add as many roles as you
like.
Note: You can use different roles for chat recommendation in different workflows. You
can see which workflow you're configuring by checking the label next to the skill name at
the top of the guided setup, such as "ITSM" or "HRSD."

<!-- page 164 -->
17. Review your choices and complete the configuration by selecting Activate.
Result
Chat recommendation or reply recommendation for the workflow is active on the instance.
What to do next
Analyze your skill performance and usage on the Now Assist Admin console to help determine
the success of the skill. Learn more about tracking your Now Assist usage at Monitoring Now
Assist usage in Subscription Management .
Configure email reply recommendation in the Now Assist Admin console
Configure the email recommendation Now Assist skill to enable agents to draft email replies
based on contextual information.
Before you begin
Role required: sn_generative_ai.nsa_admin
About this task
The email recommendation skill is available in multiple workflows. The exact steps and the order
in which they appear for the guided setup for the skill vary depending on the workflow.

<!-- page 165 -->
Procedure
1.Navigate to All > Now Assist Admin > Now Assist Features.
If you’re already in the Now Assist Admin console, select the Now Assist Features tab.
2. On the navigation panel, select a workflow, such as Technology.
Each workflow contains feature sets. The available workflows for email recommendation are
Customer (CSM) and Employee (HRSD).
3. On the feature card that is associated with the skill you'd like to activate, select View details.
4.In the All available skills section, select Activate Skill.
If you have already activated the skill and want to edit the configuration, in the Active skills
section, select the more options menu item ( ). Then select Edit.
5. In the Write with Now Assist step, choose whether you want the Now Assist context menu to
be active and then select the actions you want to be available.
After each step, select Save and continue. For more information about these choices, see Skill
inputs and triggers for Now Assist for HRSD .
6.Choose when you want the skill to be available.
You can select Skill is always available if you don’t want to place any restrictions on when
the skill is available for use. If you want to add conditions, select Customize skill availability.
Selecting this option opens up a condition builder for you to select fields and values that
determine whether someone can use the skill.
7.Choose the inputs or email parameters, including input data and whether you want to display
template suggestions.
Some options may be read-only in certain workflows.
Additional context can improve the quality of the email recommendation. In the Additional
input fields field, you can choose any fields not already selected in the Default input fields.
You can include Knowledge articles by selecting the check box. You can choose a field from

<!-- page 166 -->
related records, such as resolution notes, in the Related record field. If there’s no value for the
related record field or you don’t select one, you can also opt to include activity from related
records.
If you select Show template recommendations, then agents see a list of template suggestions
generated by Now Assist when they go to select a template.
8.In the next step of the skill configuration, select where you'd like to display the skill.
You can select both in-product, Now Assist panel, or both.
◦In-product: When selected, Now Assist skills are displayed on forms and workspaces.
For the skills that appear in-product, select the down arrow to identify the roles that can use
the skill.
◦Now Assist panel: When selected, Now Assist skills are available in the Now Assist panel. If
you don't see this option, you must activate the Now Assist panel. For more information, see
Activate the Now Assist panel standard chat.
For the skills that appear in the Now Assist panel, select the down arrow to identify the roles
that can use the skill.
Roles can be added by entering the name of the role in the User roles field. Existing roles
can be removed by selecting the X icon in the role bubble. You must have at least one role
specified, but you can add as many as you like.
9.Review your choices and select Activate to complete the configuration.
Result
Agents can generate email drafts with generative AI.
Edit a Now Assist skill
Edit the configuration of a Now Assist skill to choose the inputs or triggers and the display
location of the skill output.
Before you begin
Role required: sn_generative_ai.nsa_admin

<!-- page 167 -->
Procedure
1.Navigate to All > Now Assist Admin > Features.
If you’re already in the Now Assist Admin console, select the Now Assist Admin Features tab.
2. Select a workflow on the navigation panel, such as Technology.
Each workflow contains feature sets.
3. On the feature card associated with the skill you'd like to edit, select View details.
4.Under Active skills, select the more options icon next to the skill that you want to configure,
then select Edit.
The first step in the guided setup for the skill is displayed.
Each skill configuration has a number of steps shown in the guided setup. The exact steps vary
from skill to skill. A symbol next to each step indicates whether the step is completed, partially
completed, or not completed.
Note: Some configuration options are read-only.

<!-- page 168 -->
Chat summarization skill configuration panel
5. Proceed to the next step when you've finished configuring the current step by selecting Save
and continue.
You can return to a previous step by selecting Back.
6.Apply the new settings after reviewing your changes by selecting Done.
Result
The skill is activated with your preferred settings. You can now install other plugins or activate
other skills.
Make a copy of a Now Assist skill
The 'Make a copy' feature enables you to create a copy of a Now Assist skill so that you can
experiment with skill settings and configure the skill to fit your business needs.
Before you begin
Role required: sn_generative_ai.nsa_admin
About this task
The skills that come with the Now Assist applications have default configurations that are
optimized to serve the most common use cases. If you want to change the skill settings, you can
edit a skill with the Now Assist Admin console or you can create a copy of the skill. Creating a
copy leaves the original skill configuration intact in case you want to use it later or want to create
another copy from the original. You can activate and configure the copies of the skills by using
the same guided setup as the default skills.
Note: The 'Make a copy' feature is not available for all Now Assist skills.

<!-- page 169 -->
Note: In a default scenario, only one version of a skill can be active at a time. If you create
and activate a copy of the skill, any previously activated version of the skill is deactivated.
Procedure
1.Navigate to All > Now Assist Admin > Features.
If you’re already in the Now Assist Admin console, select the Now Assist Features tab.
2. In the navigation pane, select the workflow of the skill that you want to copy, such as
Technology or Customer.
3. On the feature card that contains the default skill, select View details.
4.In the All available skills or Active skills section, select the more options icon next to the
skill that you want to make a copy of and select Make a copy.
Note: Only one version of a skill can be active at a time. If you create and activate a
copy of the skill, any previously activated version of the skill is deactivated.
5. In the modal, select Make a copy.
Result
A copy of the skill is generated and you're taken to the guided setup.
What to do next
Continue the steps in the guided setup to activate the skill. For more information, see Activate a
Now Assist skill.
If you're making a copy of the case or incident summarization skill and would like to learn more
about your options, see the documentation for configuring record summarization.
Configure case or incident summarization in the Now Assist Admin console
Configure case or incident summarization by using the guided setup in the Now Assist Admin
console. You can choose the input tables and fields as well as customize the prompt output for
copies of the record summarization skills.
https://player.vimeo.com/video/996395898?
h=e609c55303&badge=0&autopause=0&player_id=0&app_id=58479
Before you begin
You can only customize the input data and prompt output for a copy of a record summarization
skill. To learn more about making a skill copy, see Make a copy of a Now Assist skill. After you
create a skill copy, you can learn the steps to complete the skill setup here.
Role required: nsa_admin
About this task
By default, many settings for Now Assist record summarization are optimized for general use
cases. Review your goals for incorporating generative AI on your instance to determine whether
you want to make changes and what those changes are. After you have made a plan, you can
create a copy of a skill and modify the input sources and prompt output.

<!-- page 170 -->
Procedure
1.In the Name of the skill field, enter the skill name.
The default name adds (copy) to the end of the original skill name. For example, Case
summarization (copy). Changing the name to be more specific makes it easier to identify later if
you want to make changes.
2. Optional: Add a description for the skill.
3. Go to the next step by selecting Save and continue.
4.Choose the input fields and data sources for each input template.
The default options are selected for you. Some options are read only. After you make any
changes to the input template, you can save your work by selecting Save template.
a.Select an input template.
The three default input templates are for new records, records that are in progress, and
closed records.
b.Add the base input table fields by selecting New base input field, choosing a field, and
entering a field description.
Each base input table field requires a description. The description informs the large
language model (LLM) what the field is for and how the information should be interpreted.
The more information that you put in the description means that the model has more context
for the data.
c.Add or modify the rule conditions for the base table.
The rule conditions determine when the input template is used. Record summarization is
only available to the records that match the rule conditions of an input template.

<!-- page 171 -->
d. Optional: Add additional input data sources by selecting New data source and choosing
either Related Table or Activity: Email.
(Optional) Each related table is configured with input fields and descriptions. More specific
descriptions for related tables help provide more context to the LLM. Activity fields, such as
Email, don't have input fields that you can configure.
e. Optional: Add a filter condition to the related table.
(Optional) You can add more rule conditions to the related table. These rule conditions
determine whether the data from the additional data source is incorporated into the

<!-- page 172 -->
summary. You can generate summaries on cases that don't match additional data source
rule conditions as long as the base table rule conditions are met.
5. Select Save and continue.
6.Choose prompt output sections to appear in summaries by moving a prompt section in the
Available prompt sections list to the Final prompt sections list.
You can reorder sections by dragging the boxes in the Final prompt sections list. Some input
templates have sections that are marked with the lock icon ( ). These sections must appear
in the final summary, but you can still reorder them with any sections you have added.
7.In the Test response panel, select a record from the Choose a record field.
8.Generate a summary for the chosen record by selecting Run Test.

<!-- page 173 -->
Important: Each time that you test your prompt output, the operation counts as an
assist that is tracked by your Now Assist subscription. To track your Now Assist usage,
Monitoring Now Assist usage in Subscription Management .
Running multiple tests with different records can help ensure that you're satisfied with the
results.
9.Select Save and continue.
10.Choose when the skill is available by selecting either Skill is always available or Customize
skill availability.
If you choose Customize skill availability, you can use the condition builder to add conditions
that restrict when the skill is available. For example, you could make the skill only available for
certain assignment groups.
11. Select Save and continue.
12. Choose where you want record summarization to be available by selecting the toggle next to
your preferred display option.
You can select both in-product, Now Assist panel, or both.
◦In-product: When selected, Now Assist skills are displayed on forms and workspaces.
For the skills that appear in-product, select the down arrow to identify the roles that can use
the skill.
◦Now Assist panel: When selected, Now Assist skills are available in the Now Assist panel. If
you don't see this option, you must activate the Now Assist panel. For more information, see
Activate the Now Assist panel standard chat.
For the skills that appear in the Now Assist panel, select the down arrow to identify the roles
that can use the skill.
You can add roles by entering the name of the role in the User roles field. You can remove
existing roles by selecting the X icon in the role bubble. You must specify at least one role, but
you can add as many roles as you like.
13.Select Save and continue.
14.Review your choices and select Activate to complete the configuration.
Result
Your customized version of case or incident summarization is active on the instance.
What to do next
Analyze your skill performance on the Now Assist Admin console to help determine the success
of the new version of the skill. Learn more about tracking Now Assist usage at Monitoring Now
Assist usage in Subscription Management .
Archive a Now Assist skill
The 'Archive' option in the navigation pane within Now Assist Admin allows you to archive copies
and custom Now Assist skills.
Before you begin
Role required: sn_generative_ai.nsa_admin

<!-- page 174 -->
Procedure
1.Navigate to All > Now Assist Admin > Features.
If you’re already in the Now Assist Admin console, select the Now Assist Features tab.
2. In the navigation pane, select a workflow you would like a archive a skill from.
3. Select a skill you would like to archive.
You can archive custom skills and copies of skills, only.
4.Confirm your selection in the modal.
5. In the navigation pane, select Archive.
6.Find the skills you have archived.
7.Restore an archived skill you would like to activate.

<!-- page 175 -->
8.Select Restore to find the skill in your instance.
9.Select Activate.
You may find specific skills within Archive for which Activate option is unavailable. These are
business unit skills that are deprecated. You will find these in your instance like:
Analyzing Now Assist usage
Use the Now Assist analytics and monitoring tools in the Overview page to review the summaries,
skill usage information, and issues that need your attention.
Now Assist Admin Overview page
After you activate and begin using the skills, you can measure their usage over time with graphs
that display important metrics. The console Overview page contains the information about skill
performance, including the task completion over time, and a summary of which skills are active
or available.
The following example shows the Now Assist Admin Overview page.

<!-- page 176 -->
Performance and analytics on the Now Assist Admin Overview page
Now Assist Summary section
The Now Assist Summary section displays information about the status of your skills and plugins
in a graphical format.
Plugin status
Displays a pie chart that shows the number of plugins that are installed and the
number of uninstalled plugins that are available. Select the Review now link to
review and install additional plugins.
Skills status
Displays a donut chart that shows your skills according to the state of their
configuration: active, inactive, draft, or not configured.
The following diagram shows the plugin status that displays as a pie chart, and the Skills status
that displays as a donut chart.

<!-- page 177 -->
Skills usage section
The Skills usage section displays the metrics on your installed active skills. Select the info icon
to see the information about what each card's metrics represents, or select the option icon
to refresh the card.
Use the configuration controls to configure the charts.
All skills
View all skills, or select one or more skills individually to change the view.
Date range
Change the date range for the analytics.
The following diagram shows the skills usage graphs and controls, which include the number of
actions, average unique users per day, and the number of actions over time.
Data is collected once a day and uses Performance Analytics and Reporting (PAR) for data
collection and visualization.
For more detailed information about performance, see Now Assist Analytics and

<!-- page 178 -->
Skills usage graphs and controls
Now Assist journey checklist
The Now Assist journey checklist provides you with a guide of the Now Assist workflow. If you are
confused as to what your next step should be when implementing Now Assist on your instance,
access the checklist at any time by selecting View checklist.
Additional resources on the Overview page
The Helpful resources and FAQs sections provide links to documentation and answer common
questions.
The Needs Attention section displays a count of items that need your attention. Below the count
are categorized links to those items.

> **[Screenshot: Now Assist skill detail card for Incident sentiment analysis]**
> A skill detail card showing the "Incident sentiment analysis" skill with status badges "Not started", "Out-of-box", "Now LLM Service". Description: "View requester's sentiment corresponding to the Incident. View trend and reason for the sentiment to take informed decisions…" Last updated by admin, Jul 18 2025. A teal "View details for Incident sentiment analysis" link appears. Two large buttons at the bottom: "View details" and "Activate skill".
>
> **[Screenshot: Skill detail – Overview tab for Incident assist]**
> The skill detail page for "Incident assist" (status: Not started) showing three tabs: Overview, Usage, Security and governance. Overview tab content: Description "Resolve incidents faster and easier by asking questions in the Now Assist panel." Metadata fields: Workflow: Technology, Product: ITSM, Feature: Incident, Skill type: Out-of-box, Available display locations: – (none), Last updated: 2025-07-21 14:18:02, Last updated by: admin. An "Activate skill" button appears top-right.
>
> **[Screenshot: Skill detail – Usage tab for Incident assist]**
> Same skill (Incident assist) on the Usage tab. Date filter "Date: 2026-05-18 – 2026-05-25". "Usage and adoption" section with three KPI tiles: "Total executions: 0 — 0 (0.0%) since previous period May 11 – M…", "Active users: 0 — same trend text", "Executions by channels: No data available." Below those tiles: "Assist consumption" section header.

> **[Screenshot: Skill detail – Security and governance tab for Incident assist]**
> The Incident assist skill detail on the "Security and governance" tab. Four governance sections each with a status badge: 1) "AI model" – Provider (blank), Fallback Off, AICT Compliant No – status badge "⚠ Risk". 2) "Access control" – ACL added: Yes, Last updated Jul 31 2025 – status badge "✓ OK". 3) "Guardrails" – "0 of 2 active at instance level" – status badge "⚠ Risk". 4) "Data privacy" – "3 Instance level policies active" – status badge "✓ OK".

> **[Screenshot: Now Assist Admin Analytics navigation and dashboard overview]**
> The Now Assist Admin console showing the Analytics section selected in the top navigation. Left sidebar shows: Usage and Adoption, Self-Service Performance, Skill Performance, Now Assist Guardian, User Search Analyser, Now Assist Context Menu, Value Insights.