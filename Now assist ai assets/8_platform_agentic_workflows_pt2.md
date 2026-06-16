# Platform Agentic Workflows (part 2)

*Source: document pages 101–110 (PDF chunk pages 1–10)*

*Covers: Platform Identify ways to improve service, Investigate problems, Process images for new tasks, Propose survey responses, Platform AI agents intro.*

---



<!-- doc page 101 -->

Prerequisites and setup
To access this workflow, you must have Now Assist for Platform installed on your instance. You
can get this by installing any other Now Assist application, such as Now Assist for IT Service
Management (ITSM).
Because this agentic workflow relies on survey data, you must have Assessment records
associated with task tables to analyze.
Role masking
Required role: sn_uxc_gen_ai.platform_ai_improve_services.
Role masking enables users to limit the roles and privileges of agentic workflows during tool
execution. Agentic workflows and their AI agents that get installed with Now Assist applications
are assigned pre-defined roles. If you select Users with specific roles for user
access, you must configure the security controls to include these roles. Data access settings
must also include these roles. For the instructions to change the security controls, see Define
security controls for an agentic workflow.
In the data access settings, add the necessary roles to enable reading of the Assessment table
and other required tables. For example, add the itil role to the agentic workflow's list of approved
roles so it can access Incident records.
Additional configuration
You can change agentic workflow settings by changing values for the Now Assist Skill Config
Var Set. To access the variable set and make changes, do the following while in the Platform AI
Agents and Skills scope:
•Go to the Now Assist Skill Config [sn_nowassist_skill_config] table.
•Open the record named Identify ways to improve service.
•In the Now Assist Skill Config Var Set related list, select Survey analysis input
config.
•Edit the variable values.
•Save or update the record.
Survey analysis input configuration
Config
Description Default value
field
Maximum Maximum number of records included in analysis 500
number
of
records
Analysis Time range, in months, for the survey analyzer to examine records to 3
Time identify trends. Users can specify smaller ranges when running the
Frame agentic workflow, but this value defines the maximum limit.

ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| Config field | Description | Default value |
| --- | --- | --- |
| Maximum number of records | Maximum number of records included in analysis |  |



<!-- doc page 102 -->

Survey analysis input configuration (continued)
Config
Description Default value
field
•Download
Post List of possible follow-up actions a user can take before the agentic
analysis
Analysis workflow completes.
Actions •Get more
info
Survey Filter configuration
Config
Description Default value
field
Table Table that the filter applies to Assessment Instance
name [asmt_assessment_instance]
Fields Fields that the user can add when invoking the Metric type.Name
agentic workflow
Task Filter configuration
The following is the default configuration for the Task table. You can make
additional Skill Config Var Sets for other tables, such as Incident or Case.
Config
Description Default value
field
Table Table that the filter applies to Task [task]
name
•Assignment
Fields Fields that the user can add when invoking the agentic
group.Name
workflow
•Service.Name
•Configuration
item.Name
Accessing the Identify ways to improve service agentic workflow
To access the agentic workflow:
1.Navigate to All > AI Agent Studio > Create and manage.
2. Select Identify ways to improve service.

ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| Config field | Description | Default value |
| --- | --- | --- |
| Table name | Table that the filter applies to |  |


| Config field | Description | Default value |
| --- | --- | --- |
| Table name | Table that the filter applies to |  |



<!-- doc page 103 -->

The first step of the guided setup includes a complete list of included AI agents. Selecting an
AI agent name opens it in a new browser tab, where you can see the full description, role, list of
steps, and tools. Tools are displayed in the second step of the AI agent guided setup, Add tools
and information.
In-product agentic AI and UI actions
You can access agentic workflows in the Core UI and in workspaces in the AI Activity panel.
From there, you can track their progress, provide or review input, and see the results of the work
performed. For more information, see In-product agentic AI for more details about the AI Activity
panel.
To enable users to access agentic workflows with UI actions, open the agentic workflow in AI
Agent Studio and navigate to the Select channels and access step. You can select a UI action as
a possible way to access the workflow
If you don't see your UI actions after configuring it in AI Agent Studio, verify that the property
com.glide.agentic_processes_view.enabled is set to true. See Enable the in-
product experience for agentic workflows.
Testing the Identify ways to improve service agentic workflow
You can manually test an agentic workflow execution or access on the Testing page of AI Agent
Studio if you have the sn.aia_admin role and all other roles configured in the security controls.
Start a manual test, select a test type and the workflow name, and use utterances in the Task field
like the following samples. See Test an agentic workflow execution.
To evaluate the agentic workflow over many different execution logs, run an automated
evaluation.
Sample utterance
After the workflow is activated in AI Agent Studio, enter similar phrases to the following in the
Now Assist panel to trigger the workflow. You can also run this workflow on the Testing page of AI
Agent Studio with the same utterance in the Task field if you have the sn.aia_admin role.
When invoking the agentic workflow, if you want to use additional filters, such as metric name
or category, use the name of the field in the utterance. For example, "Identify ways to improve
services for the Hardware category" is more likely to analyze the correct records than "Identify
ways to improve Hardware."
•Make suggestions for continuous service improvement based on surveys within the last 3
months
•Summarize surveys to improve Hardware services based on survey results within the last 2
years
•Give ideas for improving case resolution based on Post-Case metric type survey results over
the last month
AI agents used in the Identify ways to improve service agentic workflow
The following table lists the agents used in the Identify ways to improve service agentic workflow.
Important: In the Select channels and access of each AI agent's guided setup, verify
that the Status toggle is enabled to activate the AI agent.

ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.


<!-- doc page 104 -->

AI agents names and descriptions in the Identify ways to improve service agentic workflow
AI agent
AI agent description Role required
name
Survey Acquires survey data within the sn_uxc_gen_ai.platform_ai_improve_services
Analysis specified time range and analyzes it
AI agent for ways to improve services
Other Platform agentic workflows
For more information on other agentic workflows associated with the Platform workflow, see
Platform agentic workflows.
Platform Investigate problems agentic workflow
Use the Platform Investigate problems AI agents agentic workflow to perform root cause and risk
assessments so that you can create an actionable resolution plan for a problem.
Investigate problems overview
The Investigate problems agentic workflow can help to assist agents and subject matter experts
(SMEs) in investigating problems in their IT landscape. A problem can be associated with many
incidents, and any investigator must be aware of a large number of details when looking at a
problem. The agentic workflow can help provide insights from the incident and problem details
and suggest plans or possible solutions.
The agents, tools, and triggers that are associated with the investigate problems agentic
workflow are provided by Now Assist applications. You can activate the agentic workflow
template by making triggers active and setting the display settings to include the Now Assist
panel. If you want to change this agentic workflow's instructions, you must duplicate it, adjust the
settings to suit your specific needs, and activate the duplicated version of the agentic workflow
instead.
Prerequisites and setup
To access this workflow, you must have Now Assist for Platform installed on your instance, which
you can get if you install any other Now Assist application, such as Now Assist for IT Service
Management (ITSM).
Because this agentic workflow analyzes problems and incidents related to those problems, you
must have records on the Problem and Incident table.
Role masking
Required role: sn_uxc_gen_ai.platform_ai_problem_investigator.
Role masking enables users to limit the roles and privileges of agentic workflows during tool
execution. Agentic workflows and their AI agents that get installed with Now Assist applications
are assigned pre-defined roles. If you select Users with specific roles for user
access, you must configure the security controls to include these roles. Data access settings
must also include these roles. For the instructions to change the security controls, see Define
security controls for an agentic workflow.
In the data access settings, you must also add the necessary roles to enable reading of the
tables for Problems and related records. For example, you can add the itil role to the agentic
workflow's list of approved roles so that it can access Incident records.

ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| AI agent name | AI agent description | Role required |
| --- | --- | --- |
| Survey Analysis AI agent | Acquires survey data within the specified time range and analyzes it for ways to improve services | sn_uxc_gen_ai.platform_ai_improve_services |



<!-- doc page 105 -->

Accessing the Investigate problems agentic workflow
To access the agentic workflow:
1.Navigate to All > AI Agent Studio > Create and manage.
2. Select Investigate problems.
The first step of the guided setup includes a complete list of included AI agents. Selecting the
name of an AI agent opens it in a new browser tab, where you can see the full description, role,
list of steps, and tools. Tools are displayed in the second step of the AI agent guided setup, Add
tools and information.
In-product agentic AI and UI actions
Agentic workflows can be accessed in the Core UI and in workspaces in the AI Activity panel.
From there, you can track their progress, provide or review input, and see the results of the work
performed. For more information, see In-product agentic AI for more details about the AI Activity
panel.
To enable users to access agentic workflows with UI actions, you can open the agentic workflow
in AI Agent Studio and navigate to the Select channels and access step. You can select a UI
action as a possible way to access the workflow
If you don't see your UI actions after configuring it in AI Agent Studio, ensure that the property
com.glide.agentic_processes_view.enabled is set to true. See Enable the in-
product experience for agentic workflows.
Testing the Investigate problems agentic workflow
You can manually test an agentic workflow execution or access on the Testing page of AI Agent
Studio if you have the sn.aia_admin role and all other roles configured in the security controls.
Start a manual test, select a test type and the name of the workflow, and use utterances in the
Task field like the following samples. See Test an agentic workflow execution.
If you want to evaluate the agentic workflow over many different execution logs, run an
automated evaluation.
Sample utterance
After the workflow has been activated in AI Agent Studio, enter investigate the problem
PRB001 or similar phrases in the Now Assist panel to trigger the workflow. You can also run this
workflow on the Testing page of AI Agent Studio with the same utterance in the Task field if you
have the sn.aia_admin role.
Troubleshooting
If a Problem has a large number of related incidents, you may run into an error that states "This
model's maximum context length is 128000 tokens. However, your messages resulted in [X]
tokens. Please reduce the length of the messages." This maximum token count is in place for all
Now Assist skills, so there is currently no way to work around this error. You can try the agentic
workflow again using a different Problem.
AI agents used in the Investigate problems agentic workflow
The following table lists the agents that are used in the Investigate problems agentic workflow.

ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.


<!-- doc page 106 -->

Important: In the Define availability step of each AI agent's guided setup, make sure that
the Status toggle is enabled to activate the AI agent.
AI agents names and descriptions in the Investigate problems agentic workflow
AI agent name AI agent description
Problem investigation AI agent Identifies the root causes, performs an impact
assessment, and plans resolutions.
Other Platform agentic workflows
For more information on other agentic workflows associated with the Platform workflow, see
Platform agentic workflows.
Platform Process images for new tasks agentic workflow
Use the Platform Process images for new tasks agentic workflow to convert images to actionable
tasks.
Process images for new tasks overview
The process images for new tasks agentic workflow can help decrease manual data entry
and improve task organization by automatically converting images into task records. First, the
agentic workflow extracts information from the image, such as error messages, and presents
the analysis to the user. Then, the user is presented with the details of the task, such as short
description, category, and priority, before it is submitted so that they can make any changes.
Once the information is confirmed, the agentic workflow creates an incident record and attaches
the image.
The agents, tools, and triggers that are associated with the process images for new tasks
agentic workflow are provided by Now Assist applications. You can activate the agentic workflow
template and set the display settings to include the Now Assist panel. If you want to change
this agentic workflow's instructions, you must duplicate it to create a custom agentic workflow,
adjust the settings to suit your specific needs, and activate the duplicated version of the agentic
workflow instead.
Prerequisites and setup
To access this workflow, you must have Now Assist for Platform installed on your instance, which
you can get if you install any other Now Assist application, such as Now Assist for IT Service
Management (ITSM).
Users must have the sn_uxc_gen_ai.platform_ai_image_processor role to invoke
the agentic workflow.
If you want the ability for users to create tasks from images using Now Assist for Virtual Agent,
you must activate the Image Processor Agent, Record management AI agent, and Document and
visual insights AI agent and set the display to include Virtual Agent. This agentic workflow cannot
be discovered in Virtual Agent, so you must enable the individual AI agents that comprise it.
Role masking
Required role: sn_uxc_gen_ai.platform_ai_image_processor.
Role masking enables users to limit the roles and privileges of agentic workflows during tool
execution. Agentic workflows and their AI agents that get installed with Now Assist applications
are assigned pre-defined roles. If you select Users with specific roles for user

ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| AI agent name | AI agent description |
| --- | --- |
| Problem investigation AI agent | Identifies the root causes, performs an impact assessment, and plans resolutions. |



<!-- doc page 107 -->

access, you must configure the security controls to include these roles. Data access settings
must also include these roles. For the instructions to change the security controls, see Define
security controls for an agentic workflow.
In the data access settings, you must also add the necessary roles to enable reading of the
tables for the records you want to be able to make tasks on. For example, you can add the itil role
to the agentic workflow's list of approved roles so that it can access Incident records.
Additional configuration
You can change different settings related to the agentic workflow by changing values for the Now
Assist Skill Config Var Set. To access the variable set and make changes, do the following while
in the Platform AI Agents and Skills scope:
•Go to the Now Assist Skill Config [sn_nowassist_skill_config] table.
•Open the record named Image to task config.
•In the Now Assist Skill Config Var Set related list, select the Tables Mapping configuration
variable set.
•Set the variables for the configuration type.
•Save the Var Set.
Tables Mapping configuration
Config field Description
role_and_table_map When a user triggers this agentic workflow, it checks the role of the
invoking user and uses the map to determine what tables a user can
make a record on. For example, if you map itil to Incident table, then users
with the itil role can make Incident records with images.
get_location_details Determines whether information about the image's location is included in
metadata extraction.
tableslist List of tables where you can make tasks from images
Accessing the Process images for new tasks agentic workflow
To access the agentic workflow:
1.Navigate to All > AI Agent Studio > Create and manage.
2. Select Process images for new tasks.
The first step of the guided setup includes a complete list of included AI agents. Selecting the
name of an AI agent opens it in a new browser tab, where you can see the full description, role,
list of steps, and tools. Tools are displayed in the second step of the AI agent guided setup, Add
tools and information.
In-product agentic AI and UI actions
Agentic workflows can be accessed in the Core UI and in workspaces in the AI Activity panel.
From there, you can track their progress, provide or review input, and see the results of the work

ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| Config field | Description |
| --- | --- |
| role_and_table_map |  |
| get_location_details |  |



<!-- doc page 108 -->

performed. For more information, see In-product agentic AI for more details about the AI Activity
panel.
To enable users to access agentic workflows with UI actions, you can open the agentic workflow
in AI Agent Studio and navigate to the Select channels and access step. You can select a UI
action as a possible way to access the workflow
If you don't see your UI actions after configuring it in AI Agent Studio, ensure that the property
com.glide.agentic_processes_view.enabled is set to true. See Enable the in-
product experience for agentic workflows.
Sample utterance
After the workflow has been activated in AI Agent Studio, enter Convert image to new
task or similar phrases in the Now Assist panel to trigger the workflow. You can also run this
workflow on the Testing page of AI Agent Studio with the same utterance in the Task field if you
have the sn.aia_admin and sn_uxc_gen_ai.platform_ai_image_processor roles.
AI agents used in the Process images for new tasks agentic workflow
The following table lists the agents that are used in the Process images for new tasks agentic
workflow.
Important: In the Define availability step of each AI agent's guided setup, make sure that
the Status toggle is enabled to activate the AI agent.
AI agents names and descriptions in the Process images for new tasks agentic workflow
AI agent name AI agent description Role required
Document and visual insights AI Extracts information from platform_ml_di.creation_agent
agent images.
Other Platform agentic workflows
For more information on other agentic workflows associated with the Platform workflow, see
Platform agentic workflows.
Platform Propose survey responses agentic workflow
Use the Platform Propose survey responses AI agents agentic workflow to assist requesters in
completing surveys.
Propose survey responses overview
The Propose survey responses agentic workflow can help simplify and increase survey
responses. Many callers end up not filling out surveys after requests have been fulfilled, and this
agentic workflow helps them to make informed decisions to answer survey questions quickly.
When this agentic workflow and trigger are activated, the assignee receives an email with AI-
suggested answers to their survey based on the associated Incident or Request. They then have
the option to accept the AI-generated answers with a link at the bottom of the email. They can
also choose to fill out the survey manually.
The agents, tools, and triggers that are associated with the Propose survey responses agentic
workflow are provided by Now Assist applications. You can activate the agentic workflow
template by making the trigger active. If you want to change this agentic workflow's instructions,

ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| AI agent name | AI agent description | Role required |
| --- | --- | --- |
| Document and visual insights AI agent | Extracts information from images. | platform_ml_di.creation_agent |



<!-- doc page 109 -->

you must duplicate it, adjust the settings to suit your needs, and activate the duplicated version
of the agentic workflow instead.
Prerequisites and setup
To access this workflow, you must have Now Assist for Platform installed on your instance, which
you can get if you install any other Now Assist application, such as Now Assist for IT Service
Management (ITSM).
You can use this workflow for any survey triggered on the Incident or Request table. For example,
this agentic workflow can be used by the Short Customer Satisfaction Survey with Smiley Face
when an Incident is closed. You can change existing surveys, and the agentic workflow can still
propose answers. The agentic workflow can also be used for custom surveys triggered by the
Incident or Request table as long as there’s a trigger associated with the survey. See Configure a
trigger condition for a survey for instructions on adding a trigger to a survey.
Propose survey responses isn’t available for Now Assist panel.
Role masking
Required role: sn_uxc_gen_ai.platform_ai_survey_response.
Role masking enables users to limit the roles and privileges of agentic workflows during tool
execution. Agentic workflows and their AI agents that get installed with Now Assist applications
are assigned pre-defined roles. If you select Users with specific roles for user
access, you must configure the security controls to include these roles. Data access settings
must also include these roles. For the instructions to change the security controls, see Define
security controls for an agentic workflow.
In the data access settings, you must also add the necessary roles to enable reading of survey
tables and other related tables.
Accessing the Propose survey responses agentic workflow
To access the agentic workflow:
1.Navigate to All > AI Agent Studio > Create and manage.
2. Select Propose survey responses.
The first step of the guided setup includes a complete list of included AI agents. Selecting the
name of an AI agent opens it in a new browser tab, where you can see the full description, role,
list of steps, and tools. Tools are displayed in the second step of the AI agent guided setup, Add
tools and information.
In-product agentic AI and UI actions
Agentic workflows can be accessed in the Core UI and in workspaces in the AI Activity panel.
From there, you can track their progress, provide or review input, and see the results of the work
performed. For more information, see In-product agentic AI for more details about the AI Activity
panel.
To enable users to access agentic workflows with UI actions, you can open the agentic workflow
in AI Agent Studio and navigate to the Select channels and access step. You can select a UI
action as a possible way to access the workflow
If you don't see your UI actions after configuring it in AI Agent Studio, ensure that the property
com.glide.agentic_processes_view.enabled is set to true. See Enable the in-
product experience for agentic workflows.

ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.


<!-- doc page 110 -->

Sample utterance
After the workflow has been activated in AI Agent Studio, you need to set a trigger for the
workflow to run. This workflow cannot be triggered from the Now Assist panel.
If you want to test the agentic workflow in AI Agent Studio and you have the sn.aia_admin role,
enter the following phrase in the Testing page in the Task field: Help me with survey
AINST00XXXX. List of fields to extract inc/case/req details:
number, short_description, description, calendar_stc, escalation,
reopen_count, close_code, close_notes, state, priority, caller_id.
You must include the list of fields to extract.
AI agents used in the Propose survey responses agentic workflow
The following table lists the agents that are used in the Propose survey responses agentic
workflow.
Important: In the Define availability step of each AI agent's guided setup, make sure that
the Status toggle is enabled to activate the AI agent.
AI agents names and descriptions in the Propose survey responses agentic workflow
AI agent name AI agent description Role required
Survey Suggests answers to questions sn_uxc_gen_ai.platform_ai_survey_response
response based on record details.
suggestion AI
agent
Survey Collects the data related to the sn_uxc_gen_ai.platform_ai_survey_response
filling data record and the survey questions
collection AI to gather feedback.
agent
Other Platform agentic workflows
For more information on other agentic workflows that are associated with the Platform workflow,
see Platform agentic workflows.
Platform AI agents
Explore different AI agents available in platform Now Assist applications.
Looking for an AI agent?
•There might be AI agents installed with the Now Assist application that are not used in agentic
workflows. To learn how to see all agents that are available on your instance, see Find AI
agents.
•To find agents that might not be installed on your instance, visit the AI Agent Marketplace on
the ServiceNow Store.
AI agents are also provided with some of the Integration Hub spokes or plugins that are
preconfigured and are callable from interfaces such as AI Agent Studio and Virtual Agent. For
more information, see Available AI agents for Integration Hub .

ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| AI agent name | AI agent description | Role required |
| --- | --- | --- |
| Survey response suggestion AI agent | Suggests answers to questions based on record details. | sn_uxc_gen_ai.platform_ai_survey_response |
| Survey filling data collection AI agent | Collects the data related to the record and the survey questions to gather feedback. | sn_uxc_gen_ai.platform_ai_survey_response |
