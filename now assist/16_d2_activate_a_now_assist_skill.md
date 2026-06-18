# Activate a Now Assist skill

_Source pages: 158–165 | Depth: 2_

---

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

> **[Screenshot: Skill detail – Security and governance tab for Incident assist]**
> The Incident assist skill detail on the "Security and governance" tab. Four governance sections each with a status badge: 1) "AI model" – Provider (blank), Fallback Off, AICT Compliant No – status badge "⚠ Risk". 2) "Access control" – ACL added: Yes, Last updated Jul 31 2025 – status badge "✓ OK". 3) "Guardrails" – "0 of 2 active at instance level" – status badge "⚠ Risk". 4) "Data privacy" – "3 Instance level policies active" – status badge "✓ OK".