### Platform Agentic Workflows


About this task
Agentic workflows can perform work on certain records, and you can track their progress or
provide input in the AI Workflows panel available for forms and workspaces. See In-product
agentic AI for more details about the functions and features of the AI Workflows panel.
The following task describes the process for enabling the system property that
allows you to see the AI Workflows panel and see UI actions for agentic workflows:
com.glide.agentic_processes_view.enabled.
To enable users to access agentic workflows with UI actions, you can open the agentic workflow
in AI Agent Studio and navigate to the Select channels and access step. You can select a UI
action as a possible way to access the workflow. See Select channels and access for agentic
workflows for more information.
Procedure
1.Navigate to All > System Properties > All Properties.
2. Select New.
3. In the Name field, enter com.glide.agentic_processes_view.enabled.
4.In the Value field, enter true.
Result
The In-product agentic experience, including the AI Workflows panel, is available.
What to do next
Monitor agentic workflow execution on forms in the Core UI and workspaces, or create UI actions
to grant users access.
Platform agentic workflows
You can use the available Now Assist AI agents Platform agentic workflows to achieve business
outcomes with self-executing autonomous AI agents.
Use the following agentic workflows that are available with ServiceNow AI Platform.
Available agentic workflows for Platform
Agentic
workflow Description Available AI agents
name
Analyze Detects recurring patterns, predicts disruptions, and enables Issue trend
task trends proactive resolutions with actionable recommendations. analysis AI Agent
Classify Triages tasks by updating fields, evaluating sentiment, and Record field value
tasks summarizing. prediction AI agent
Generate Provides a personalized work plan based on current work Prioritize work AI
my work and historical data of previous work. agent
plan
© 2026 ServiceNow, Inc. All rights reserved. 77
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **Agentic workflow name** | **Description** | **Available AI agents** |
|---|---|---|
| Analyze task trends | Detects recurring patterns, predicts disruptions, and enables proactive resolutions with actionable recommendations. |  |
| Classify tasks | Triages tasks by updating fields, evaluating sentiment, and summarizing. |  |

Available agentic workflows for Platform
(continued)
Agentic
workflow Description Available AI agents
name
•Next best action
Generate Analyzes tasks, generates resolution summaries, and
recommendation
resolution updates comments or work notes.
AI agent
plan
•Resolution
Action AI Agent
Help Identifies backlog items, evaluates team member Work Allocator AI
optimize performance on previous assignments, and allocates work Agent
team based on similarity to those previous assignments.
productivity
Identify Analyzes feedback, trends, and metrics and provides Survey Analysis AI
ways to recommendations to help optimize processes. agent
improve
service
Investigate Provides insights from incident or problem details. Problem
problems investigation AI
agent
•Image Processor
Process Processes images and converts them to tasks.
Agent
images for
tasks •Document and
visual insights AI
agent
•Survey response
Propose Suggests answers for survey questions.
suggestion AI
survey
agent
responses
•Survey filling
data collection
AI agent
© 2026 ServiceNow, Inc. All rights reserved. 78
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **Agentic workflow name** | **Description** | **Available AI agents** |
|---|---|---|
| Generate resolution plan | Analyzes tasks, generates resolution summaries, and updates comments or work notes. |  |
| Help optimize team productivity | Identifies backlog items, evaluates team member performance on previous assignments, and allocates work based on similarity to those previous assignments. |  |
| Identify ways to improve service | Analyzes feedback, trends, and metrics and provides recommendations to help optimize processes. |  |
| Investigate problems | Provides insights from incident or problem details. |  |
| Process images for tasks | Processes images and converts them to tasks. |  |

Important: By default, all agentic workflows and AI agent records are read only.
To run the AI agents autonomously, you must either activate the agentic workflow template
or duplicate the agentic workflow, and then proceed with the following steps:
•Activate the agentic workflow.
•Activate all agents within the agentic workflow.
•Activate the trigger to invoke the agentic workflow automatically. If you prefer to invoke it
manually, activating the trigger isn’t necessary.
Tools mapped to AI agents in agentic workflows
To find the tools mapped to AI agents used in the agentic workflows, you can perform the
following steps:
1.Navigate to All > AI Agent Studio > Create and manage
2. In the Agentic workflows tab, select the agentic workflow.
3. In the Describe and connect step of the guided setup, select the AI agent you want to see the
tools for.
4.Go to the Add tools and information step.
5. Review the tools mapped to the AI agent.
6.Repeat for all AI agents in the agentic workflow.
Agentic workflows and UI actions
To enable users to access agentic workflows with UI actions, you can open the agentic workflow
in AI Agent Studio and navigate to the Select channels and access step. You can select a UI
action as a possible way to access the workflow
If you don't see your UI actions after configuring it in AI Agent Studio, ensure that the property
com.glide.agentic_processes_view.enabled is set to true.
Looking for an AI agent?
•There might be AI agents installed with the Now Assist application that are not used in agentic
workflows. To learn how to see all agents that are available on your instance, see Find AI
agents.
•To find agents that might not be installed on your instance, visit the AI Agent Marketplace on
the ServiceNow Store.
Platform Analyze task trends agentic workflow
Use the Platform Analyze task trends agentic workflow to detect recurring task patterns of closed
tickets so that you can understand the root cause and get recommendations to prevent them
from happening in future.
Analyze task trends overview
The Analyze task trends agentic workflow enhances task management by detecting recurring
patterns, predicting disruptions, and suggesting proactive resolution to reduce downtime and
improve reliability. Tasks are grouped and analyzed by AI to analyze common recurring issues
and root causes. The LLM then generates resolution recommendations based on the analysis
and displays it to you. After the analysis is generated, you can continue the conversation to do
the following:
© 2026 ServiceNow, Inc. All rights reserved. 79
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

•Get a summary of each group analysis. You have to specify which group you would like to get a
summary of.
•Download the analysis as a PDF or Word document.
•Get more information by asking follow-up questions. For example, you can ask why certain
suggestions were generated.
•Analyze the next ten groups. Each analysis is done for ten groups at a time. You can continue
analyzing more groups with the same filters within the same conversation, but the other
actions for the previous group are no longer available.
The exact options for follow-up actions available can be configured.
The default input fields considered for analysis are the following:
•Short Description
•Description
•Resolution Notes
•Resolution Code
•Subcategory
•Category
You can con figure additional input fields using a Now Assist Skill Config Var Set
[sn_nowassist_skill_config_var_set]. See the Additional configuration section for more
information.
The agents, tools, and triggers associated with the Analyze task trends agentic workflow are
provided by Now Assist applications. You can activate the agentic workflow template by making
triggers active and setting the display settings to include the Now Assist panel. If you want to
change this agentic workflow's instructions, you must duplicate it, adjust the settings to suit your
specific needs, and activate the duplicated version instead.
Prerequisites and setup
To access this workflow, you must have Now Assist for Platform installed on your instance. You
can get this by installing any other Now Assist application, such as Now Assist for IT Service
Management (ITSM).
For this agentic workflow to behave as expected, you should have at least 500 records on your
task table.
You must also configure Group Action Framework (GAF). See Group Action Framework for more
information on what GAF is and how to set it up. The Incident, Case and HR Case tables use the
default GAF records, but you can configure GAF for other task tables.
GAF is set up for certain Now Assist applications for you. If you want the agentic workflow to have
its own system of categorization different from the main application, you can clone an existing
action strategy skill and use the clone in the var set described below. This enables you to train
the groupings differently for different agentic resources.
Note: If you create a clone of an action strategy skill, ensure that Optimized
prediction is enabled to use AI Search as your fallback. You can leave it unchecked if
you do not use AI Search on your instance.
© 2026 ServiceNow, Inc. All rights reserved. 80
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

Role masking
Required role: sn_uxc_gen_ai.platform_ai_analyze_trnds.
Role masking enables users to limit the roles and privileges of agentic workflows during tool
execution. Agentic workflows and their AI agents that get installed with Now Assist applications
are assigned pre-defined roles. If you select Users with specific roles for user
access, you must configure the security controls to include these roles. Data access settings
must also include these roles. For the instructions to change the security controls, see Define
security controls for an agentic workflow.
In the data access settings, you must also add the necessary roles to enable reading of the
tables for the records you want to access for trend analysis. For example, you can add the itil role
to the agentic workflow's list of approved roles so that it can access Incident records.
Additional configuration
You can change different settings related to the agentic workflow by changing values for the Now
Assist Skill Config Var Set. To access the variable set and make changes, do the following while
in the Platform AI Agents and Skills scope:
•Go to the Now Assist Skill Config [sn_nowassist_skill_config] table.
•Open the record named Analyze Task Trends.
•In the Now Assist Skill Config Var Set related list, select Task Trends Input Config.
•Edit the variable values.
•Save or update the record.
Time is a required filter specification in the user utterance. If you want users to be able to filter
tasks by fields other than time, you can configure a Task Table Config var set. One for the
Task table is provided as part of the application. If you want to create one for a specific table,
you can create a Now Assist Skill Config Var Set [sn_nowassist_skill_config_var_set]. The Skill
Config is Analyze Task Trends, and the Config Type is Prompt Parameter
Configuration.
Task Trends Input Config configuration
Config
Description Default value
field
•Get a
Post List of possible follow-up actions a user can take before the agentic
summary
Analysis workflow completes.
Actions •Get more
info
•Analyze
next 10
groups
•Download
analysis
© 2026 ServiceNow, Inc. All rights reserved. 81
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **Config field** | **Description** | **Default value** |
|---|---|---|

Task Trends Input Config configuration (continued)
Config
Description Default value
field
Analysis Range of time, in months, for the trends analyzer to look at records 3
Time to identify trends. You can specify smaller ranges when running the
Frame agentic workflow, but this value defines the maximum limit.
GAF Number of records analyzed per GAF record grouping. See the previous 8
Record Prerequisites and setup section.
Limit
Prompt parameter configuration
Config field Description Default value
Input Table that these potential filter conditions Task
Table belong to
Input Additional fields that the agentic None
Fields workflow can consider as context for its
analysis
•Assignment group.Name
Filter Fields that users can include when
Fields invoking the agentic workflow •Service.Name
If you want to add new fields, use the •Configuration item.Name
dot-walked display-label format like the
default values.
Group The Group Action Framework grouping No default
Skill ID skill dedicated to arranging records into
categories
Action The Group Action Framework action skill No default
Skill ID dedicated to selecting and mapping
representative records for each group
and summarizing them
See Group Action Framework for
information about setting up GAF.
Auto When the grouping and action skills run No default
Classify again to incorporate new records for
Frequency analysis
© 2026 ServiceNow, Inc. All rights reserved. 82
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **Config field** | **Description** | **Default value** |
|---|---|---|
| Analysis Time Frame | Range of time, in months, for the trends analyzer to look at records to identify trends. You can specify smaller ranges when running the agentic workflow, but this value defines the maximum limit. |  |

| **Config field** | **Description** | **Default value** |
|---|---|---|
| Input Table | Table that these potential filter conditions belong to |  |
| Input Fields | Additional fields that the agentic workflow can consider as context for its analysis |  |
| Filter Fields | Fields that users can include when invoking the agentic workflow If you want to add new fields, use the dot-walked display-label format like the default values. |  |
| Group Skill ID | The Group Action Framework grouping skill dedicated to arranging records into categories |  |
| Action Skill ID | The Group Action Framework action skill dedicated to selecting and mapping representative records for each group and summarizing them See Group Action Framework for information about setting up GAF. |  |

Prompt parameter configuration (continued)
Config field Description Default value
Note: If you provide a Group
Skill ID and an Action Skill ID but
leave the Auto Classify Frequency
empty, it will default to 24 hours.
Accessing the Analyze task trends agentic workflow
To access the agentic workflow:
1.Navigate to All > AI Agent Studio > Create and manage.
2. Select Analyze task trends.
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
Testing the Analyze task trends agentic workflow
You can manually test an agentic workflow execution or access on the Testing page of AI Agent
Studio if you have the sn.aia_admin role and all other roles configured in the security controls.
Start a manual test, select a test type and the name of the workflow, and use utterances in the
Task field like the following samples. See Test an agentic workflow execution.
If you want to evaluate the agentic workflow over many different execution logs, run an
automated evaluation.
Sample utterance
After the workflow has been activated in AI Agent Studio, use similar queries to the following
to run the agentic workflow in the Now Assist panel. You can also run this workflow on
the Testing page of AI Agent Studio with the same utterance in the Task field if you have the
sn.aia_admin role.
Each utterance must include the name of the table and the time frame to analyze. If the utterance
doesn't include these things, the agentic workflow prompts you for more information.
© 2026 ServiceNow, Inc. All rights reserved. 83
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **Config field** | **Description** | **Default value** | **** |
|---|---|---|---|
|  |  |  | Note: If you provide a Group Skill ID and an Action Skill ID but leave the Auto Classify Frequency empty, it will default to 24 hours. |

The time frame specified by the user can't exceed the maximum value set by the Analysis time
frame configuration.
When invoking the agentic workflow, if you want to use additional filters, such as assignment
group, use the name of the field in the utterance. For example, "Analyze incident trends assigned
to the Hardware group" is more likely to analyze the correct records than "Analyze Hardware
incident trends."
•Analyze incident trends related to payment issues within the last two months
•Analyze case trends within the last month
•Analyze HR case trends with High Priority within the last two years
•Analyze incident and problem trends within the last two weeks
Troubleshooting
When running this agentic workflow, it's possible to see an error that states "I couldn't analyze as
I didn't have the required resources." This error occurs when GAF isn't configured for the table
you want to analyze. See Configure Group Action Framework for steps to configure GAF for the
table. If you're still having issues after GAF is configured, reach out to Now Support.
AI agents used in the Analyze task trends agentic workflow
The following table lists the agents that are used in the Analyze task trends agentic workflow.
Important: In the Select channels and status step of each AI agent's guided setup, make
sure that the Status toggle is enabled to activate the AI agent.
AI agents names and descriptions in the Analyze task trends agentic workflow
AI agent
AI agent description Role required
name
Issue Analyzes grouped task data to sn_uxc_gen_ai.platform_ai_analyze_trnds
trend identify recurring issues and root
analysis causes. Provides detailed, actionable
AI recommendations using structured
agent analysis.
Other Platform agentic workflows
For more information on other agentic workflows that are associated with the Platform workflow,
see Platform agentic workflows.
Platform Classify tasks agentic workflow
Use the Platform Classify tasks AI agents agentic workflow to gather relevant information about
tasks automatically and make decisions about priorities and assignments.
Classify tasks overview
The Classify tasks agentic workflow can help improve efficiency and accuracy by automatically
gathering information, prioritizing tasks, assigning teams, detecting sentiment, and generating
task summaries.
The agents, tools, and triggers that are associated with the Classify tasks agentic workflow are
provided by Now Assist applications. You can activate the agentic workflow template by making
© 2026 ServiceNow, Inc. All rights reserved. 84
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **AI agent name** | **AI agent description** | **Role required** |
|---|---|---|
| Issue trend analysis AI agent | Analyzes grouped task data to identify recurring issues and root causes. Provides detailed, actionable recommendations using structured analysis. | sn_uxc_gen_ai.platform_ai_analyze_trnds |

triggers active and setting the display settings to include the Now Assist panel. If you want to
change this agentic workflow's instructions, you must duplicate it, adjust the settings to suit your
specific needs, and activate the duplicated version of the agentic workflow instead.
Prerequisites and setup
To access this workflow, you must have Now Assist for Platform installed on your instance, which
you can get if you install any other Now Assist application, such as Now Assist for IT Service
Management (ITSM).
For this agentic workflow to behave as expected, you must also configure Group Action
Framework (GAF). See Set up AI Search for Group Action Framework and Configure Group Action
Framework for more information on getting started with GAF.
Role masking
Required role: sn_uxc_gen_ai.platform_ai_classify_tasks
Role masking enables users to limit the roles and privileges of agentic workflows during tool
execution. Agentic workflows and their AI agents that get installed with Now Assist applications
are assigned pre-defined roles. If you select Users with specific roles for user
access, you must configure the security controls to include these roles. Data access settings
must also include these roles. For the instructions to change the security controls, see Define
security controls for an agentic workflow.
In the data access settings, you must also add the necessary roles to enable reading of the
tables for the records you want to classify. For example, you can add the itil role to the agentic
workflow's list of approved roles so that it can access Incident records.
Additional configuration
You can change different settings related to the agentic workflow by changing values for the Now
Assist Skill Config Var Set. To access the variable set and make changes, do the following while
in the Platform AI Agents and Skills scope:
•Go to the Now Assist Skill Config [sn_nowassist_skill_config] table.
•Open the record named Task Classify Tasks Skill Config.
•In the Now Assist Skill Config Var Set related list, select Field Predictor.
•Edit the variable values.
•Save or update the record.
The Classify tasks configuration variable set includes the following variables. You can configure
either the AIS fields or the GAF field for determining how the agentic workflow gathers what work
the user has. If you configure both, GAF takes priority when running the agentic workflow. For
more information about GAF, see Group Action Framework.
Classify tasks configuration
Config field Description
Search Options include Keyword, Semantic, or Hybrid. Keyword-based searches look
Mode at individual phrases, while semantic-based searches rely on the phrasing of
utterances as well. Hybrid utilizes both strategies.
© 2026 ServiceNow, Inc. All rights reserved. 85
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **Config field** | **Description** |
|---|---|

Classify tasks configuration (continued)
Config field Description
Default: Keyword
AIS Fields used by AI Search operations to find similar records for improved prediction
Search context
Fields
Capability OneExtend capability for enhanced field prediction functionality. See Generative AI
Controller reference for more details.
GAF Skill configuration for Group AI Framework (GAF).
Config
AIS Fields used by AI Search to determine what work a user has
Search
Fields
AIS Fields returned by AI Search to the agentic workflow to base decisions on
Return
Fields
GAF Group Action Framework grouping configuration record, which is a collection of
Config groups of records to make searching easier
AIS Profile for AI search, such as Now Assist in Virtual Agent.
Search
Profile
Capability Server-side script to generate custom payloads for OneExtend capability
Payload integration
AIS Table used if GAF is not configured
Fallback
Table
Return Field values returned from identified relevant records
Fields
Check Uses the information provided by the Issue Readiness AI agent
for Issue
Readiness Warning: Only enable if the Issue Readiness AI agent is active on your
instance. Otherwise, the agentic workflow will not execute.
© 2026 ServiceNow, Inc. All rights reserved. 86
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **Config field** | **Description** |
|---|---|
|  |  |
| AIS Search Fields |  |
| Capability |  |
| GAF Config |  |
| AIS Search Fields |  |
| AIS Return Fields |  |
| GAF Config |  |
| AIS Search Profile |  |
| Capability Payload |  |
| AIS Fallback Table |  |
| Return Fields |  |

Classify tasks configuration (continued)
Config field Description
Fields Field values to predict and update
Table Table where you want to execute the agentic workflow on
Search Options include Record-based and Utterance-based. Record-based derives search
Term terms for generating context from the record itself. Utterance-based relies on the
Source user-submitted utterance for search term options.
Default: Record-based
Accessing the Classify tasks agentic workflow
To access the agentic workflow:
1.Navigate to All > AI Agent Studio > Create and manage.
2. Select Classify tasks.
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
Testing the Classify tasks agentic workflow
You can manually test an agentic workflow execution or access on the Testing page of AI Agent
Studio if you have the sn.aia_admin role and all other roles configured in the security controls.
Start a manual test, select a test type and the name of the workflow, and use utterances in the
Task field like the following samples. See Test an agentic workflow execution.
If you want to evaluate the agentic workflow over many different execution logs, run an
automated evaluation.
© 2026 ServiceNow, Inc. All rights reserved. 87
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **Config field** | **Description** |
|---|---|
| Fields |  |
| Table |  |

Sample utterance
After the workflow has been activated in AI Agent Studio, enter these or similar phrases in the
Now Assist panel to trigger the workflow. You must have the sn.now_assist_panel_user role to run
the workflow. You can also run this workflow on the Testing page of AI Agent Studio with the same
utterance in the Task field if you have the sn.aia_admin role.
•Populate the priority and assignment group for INC0001
•Populate the empty fields on INC0001
•Find the priority for INC001
AI agents used in the Classify tasks agentic workflow
The following table lists the agents that are used in the Classify tasks agentic workflow.
Important: In the Define availability step of each AI agent's guided setup, make sure that
the Status toggle is enabled to activate the AI agent.
AI agents names and descriptions in the Classify tasks agentic workflow
AI agent
AI agent description Role required
name
Record Fetches, predicts, creates, and sn_uxc_gen_ai.platform_ai_field_predictor
field value updates records with the provided
prediction details. Provides summary and
AI agent justification for recommendations.
Other Platform agentic workflows
For more information on other agentic workflows that are associated with the Platform workflow,
see Platform agentic workflows.
Platform Generate my work plan agentic workflow
Use the Platform Generate my work plan agentic workflow to create personalized work plans for
currently assigned work.
Generate my work plan overview
The Generate my work plan agentic workflow creates personalized work plans based on current
assigned work. This reduces manual effort and guesswork in work planning. The AI agents
identify and retrieve all work assigned to the user, predict effort required to complete work, and
generate an actionable work plan. Effort is estimated based on historical records related to the
open work items. Generated work plans emphasize the highest priority work by examining the
following information and can result in faster resolution and fewer missed SLAs.
•User sentiment
•Short description
•Priority
•Description
•Due date
•Escalation
•State
© 2026 ServiceNow, Inc. All rights reserved. 88
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **AI agent name** | **AI agent description** | **Role required** |
|---|---|---|
| Record field value prediction AI agent | Fetches, predicts, creates, and updates records with the provided details. Provides summary and justification for recommendations. | sn_uxc_gen_ai.platform_ai_field_predictor |

•Updated
•Number
•Impact
•SLA
Along with the plan itself, the agentic workflow also provides reasoning behind its decisions for
creating the plan.
The agents, tools, and triggers associated with the Generate my work plan agentic workflow are
provided by Now Assist applications. You can activate the agentic workflow template by adding
triggers and setting the display settings to include the Now Assist panel. To change this agentic
workflow's instructions, duplicate it, adjust the settings to suit your specific needs, and activate
the duplicated version instead.
Prerequisites and setup
To access this workflow, you must have Now Assist for Platform installed on your instance. You
can get this by installing any other Now Assist application, such as Now Assist for IT Service
Management (ITSM).
Now LLM is not a supported LLM provider for the Generate my work plan agentic workflow.
Role masking
Required role: sn_uxc_gen_ai.platform_ai_work_planner.
Role masking enables users to limit the roles and privileges of agentic workflows during tool
execution. Agentic workflows and their AI agents that get installed with Now Assist applications
are assigned pre-defined roles. If you select Users with specific roles for user
access, you must configure the security controls to include these roles. Data access settings
must also include these roles. For the instructions to change the security controls, see Define
security controls for an agentic workflow.
In the data access settings, add the necessary roles to enable reading of the tables for the
records you want to access for potential work plans. For example, add the itil role to the agentic
workflow's list of approved roles so that it can access Incident records.
Additional configuration
Change different settings related to the agentic workflow by changing values for the Now Assist
Skill Config Var Set. To access the variable set and make changes, do the following while in the
Platform AI Agents and Skills scope:
•Go to the Now Assist Skill Config [sn_nowassist_skill_config] table.
•Open the record named Generate my work plan config.
•In the Now Assist Skill Config Var Set related list, select New.
•Enter a name for your Config Var Set.
•Set Config Type to be either User schedule or Generate my work plan.
•Save the Var Set record.
•Set the variables for the config type.
•Save the Var Set.
The work plan config var set includes general variables for running the agentic workflow.
© 2026 ServiceNow, Inc. All rights reserved. 89
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

Work plan config type configurations
Config
Description
field
Schedule Creates a scheduled job that automatically runs, allowing users to see updated
job prioritization suggestions after making progress in their work. Default: Unselected.
Schedule How long after a record in the original work plan is updated for the agentic workflow
job to run again. Default: 30 minutes
frequency
Predict Predict estimated time to complete work per record.
estimates
Exclude By default, certain fields are used for prioritizing work on the Task table. You can
task table configure what fields to use on individual tables, such as the Incident table. Enable
this to only plan for tables configured and not other records which are task or
extension of task tables.
Max tasks The maximum number of tasks that can be recommended to a user for their work
plan. Default: 30 tasks
The Incident config var set includes the following variables. Configure either the AIS fields or
the GAF field for determining how the agentic workflow gathers what work the user has. If you
configure GAF, it takes priority when running the agentic workflow. For more information about
GAF, see Group Action Framework.
Use this config var set as a template to change any values for other tables, such as the Case or
HR Case tables.
Note: If you select Exclude task table in the work plan config var set, only the
tables that have these var sets configured are included for work in the suggested work plan.
Incident table config type configuration
Config field Description
Table Table for record types that someone can work on
Conditions Filter criteria for determining eligible tasks
Record Fields passed to the workflow for analysis
fields
Time Custom or edited field for specifying time worked. By default, the agentic workflow
worked uses the Time worked field.
© 2026 ServiceNow, Inc. All rights reserved. 90
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **Config field** | **Description** |
|---|---|
| Schedule job |  |
| Schedule job frequency |  |
| Predict estimates |  |
| Exclude task table |  |

| **Config field** | **Description** |
|---|---|
| Table |  |
| Conditions |  |
| Record fields |  |

Incident table config type configuration (continued)
Config field Description
AIS Search Specific AI Search profile
Profile
AIS Search Fields AI Search looks at for determining similarity
Fields
AIS Return Fields returned by AI Search to the agentic workflow to base decisions on
Fields
GAF Config Group Action Framework grouping configuration record, which is a collection of
groups of records to make searching easier.
Assigned The field for the user who works on the record. By default, the agentic workflow
to field uses the assigned_to field.
Order by JSON object array containing the ordering information for how work records are
prioritized.
Default is as follows. Any direction other than “DESC” is considered ascending in
order.
[
{ column: 'priority', direction: ''},
{ column: 'due_date', direction: ''},
{ column: 'escalation', direction: 'DESC' },
{ column: 'sys_created', direction: 'DESC' }
]
By default, the Generate my work plan agentic workflow relies on the User [sys_user] record's
Schedule field. If there is no schedule defined on the User record, the workflow consults the
Schedule [chm_schedule] table for the user. If neither are present, the assumed schedule is a
weekday schedule from 8:00 a.m. to 5:00 p.m.
Change what tables and fields to look for schedule information with the User schedule
config type.
Generate my work plan User schedule configuration
Config field Description
Table Table where user schedule information is stored
Conditions (Optional) Conditions to determine what user schedule to associate with the
user.
© 2026 ServiceNow, Inc. All rights reserved. 91
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **Config field** | **Description** |
|---|---|
| AIS Search Profile |  |
| AIS Search Fields |  |
| AIS Return Fields |  |
| GAF Config |  |
| Assigned to field |  |

| **[** |
|---|
| { column: 'priority', direction: ''}, |
| { column: 'due_date', direction: ''}, |
| { column: 'escalation', direction: 'DESC' }, |
| { column: 'sys_created', direction: 'DESC' } |
| ] |

| **Config field** | **Description** |
|---|---|
| Table |  |

Generate my work plan User schedule configuration (continued)
Config field Description
Schedule Field where specific schedule information is stored
column
Accessing the Generate my work plan agentic workflow
To access the agentic workflow:
1.Navigate to All > AI Agent Studio > Create and manage.
2. Select Generate my work plan.
The first step of the guided setup includes a complete list of included AI agents. Selecting the
name of an AI agent opens it in AI Agent Studio, where you can see the full description, role, list
of steps, and tools. Tools are displayed in the second step of the AI agent guided setup, Add
tools and information.
In-product agentic AI and UI actions
Access agentic workflows in the Core UI and in workspaces in the AI Activity panel. From there,
track their progress, provide or review input, and see the results of the work performed. For more
information, see In-product agentic AI for more details about the AI Activity panel.
To enable users to access agentic workflows with UI actions, open the agentic workflow in AI
Agent Studio and navigate to the Select channels and access step. Select a UI action as a
possible way to access the workflow.
If you don't see your UI actions after configuring it in AI Agent Studio, verify that the property
com.glide.agentic_processes_view.enabled is set to true. See Enable the in-
product experience for agentic workflows.
Testing the Generate my work plan agentic workflow
Manually test an agentic workflow execution or access on the Testing page of AI Agent Studio
if you have the sn.aia_admin role and all other roles configured in the security controls. Start a
manual test, select a test type and the name of the workflow, and use utterances in the Task field
like the following samples. See Test an agentic workflow execution.
To evaluate the agentic workflow over many different execution logs, run an automated
evaluation.
Sample utterance
After the workflow is activated in AI Agent Studio, enter What should I work on
today? or similar phrases in the Now Assist panel to trigger the workflow. You must have the
sn.now_assist_panel_user role to run the workflow. Also run this workflow on the Testing page of
AI Agent Studio with the same utterance in the Task field if you have the sn.aia_admin role.
Users must have the sn_uxc_gen_ai.platform_ai_work_planner role to execute the agentic
workflow.
© 2026 ServiceNow, Inc. All rights reserved. 92
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **Config field** | **Description** |
|---|---|

AI agents used in the Generate my work plan agentic workflow
The following table lists the agents used in the Generate my work plan agentic workflow.
Important: In the Select channels and status step of each AI agent's guided setup, verify
that the Status toggle is enabled to activate the AI agent.
AI agents names and descriptions in the Generate my work plan agentic workflow
AI agent
AI agent description Role required
name
Prioritize Dynamically orders tasks based on sn_uxc_gen_ai.platform_ai_work_planner
work AI parameters like urgency, priority, SLAs,
Agent​ sentiment, and impact.
Other Platform agentic workflows
For more information on other agentic workflows associated with the Platform workflow, see
Platform agentic workflows.
Platform Generate resolution plan agentic workflow
Use the Platform Generate resolution plan AI agents agentic workflow to fetch task record details,
generate resolution summary steps, and update comments or work notes.
Generate resolution plan overview
The Generate resolution plan agentic workflow can help resolve tasks by collecting record
details and generating resolution summaries that can be added to comments or work notes.
Due to the dynamic nature of AI agents, this agentic workflow can be used for tasks that require
complex logic even when provided with minimal details.
The agents, tools, and triggers that are associated with the Generate resolution plan agentic
workflow are provided by Now Assist applications. You can activate the agentic workflow
template by making triggers active and setting the display settings to include the Now Assist
panel. If you want to change this agentic workflow's instructions, you must duplicate it, adjust the
settings to suit your specific needs, and activate the duplicated version of the agentic workflow
instead.
Prerequisites and setup
To access this workflow, you must have Now Assist for Platform installed on your instance, which
you can get if you install any other Now Assist application, such as Now Assist for IT Service
Management (ITSM).
For this agentic workflow to behave as expected, you must also configure Group Action
Framework (GAF). See Set up AI Search for Group Action Framework and Configure Group Action
Framework for more information on getting started with GAF.
Role masking
Required role: sn_uxc_gen_ai.platform_ai_grp_workflow.
Role masking enables users to limit the roles and privileges of agentic workflows during tool
execution. Agentic workflows and their AI agents that get installed with Now Assist applications
are assigned pre-defined roles. If you select Users with specific roles for user
© 2026 ServiceNow, Inc. All rights reserved. 93
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **AI agent name** | **AI agent description** | **Role required** |
|---|---|---|
| Prioritize work AI Agent​ | Dynamically orders tasks based on parameters like urgency, priority, SLAs, sentiment, and impact. | sn_uxc_gen_ai.platform_ai_work_planner |

access, you must configure the security controls to include these roles. Data access settings
must also include these roles. For the instructions to change the security controls, see Define
security controls for an agentic workflow.
In the data access settings, you must also add the necessary roles to enable reading of the
tables for the records you want to access for potential resolution plans. For example, you can add
the itil role to the agentic workflow's list of approved roles so that it can access Incident records.
Additional configuration
You can change different settings related to the agentic workflow by changing values for the Now
Assist Skill Config Var Set. To access the variable set and make changes, do the following while
in the Platform AI Agents and Skills scope:
•Go to the Now Assist Skill Config [sn_nowassist_skill_config] table.
•Open the record named Generate Resolution Plans Skill Config.
•In the Now Assist Skill Config Var Set related list, select the configuration variable set you want
to edit.
•Set the variables for the configuration type.
•Save the Var Set.
The Generate resolution plan configuration variable set includes the following variables. You can
configure either the AIS fields or the GAF field for determining how the agentic workflow gathers
what work the user has. If you configure both, GAF takes priority when running the agentic
workflow. For more information about GAF, see Group Action Framework.
Review button params configuration
Config field Description Default value
Show button Display a UI action for reviewing a generated resolution plan Enabled
Button label Label for the UI action button to review a generated resolution plan Review
Next Best Action Recommender configuration
Config field Description
Search Mode Options include Keyword, Semantic, or Hybrid. Keyword-based searches look
at individual phrases, while semantic-based searches rely on the phrasing of
utterances as well. Hybrid utilizes both strategies.
Default: Keyword
Include Determines whether the Decomposition Agent, one of the agents in the
Decomposition workflow, is used. If this is unselected, the Next best action recommendation
Agent in the AI agent still runs.
workflow
© 2026 ServiceNow, Inc. All rights reserved. 94
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **Config field** | **Description** | **Default value** |
|---|---|---|
| Show button | Display a UI action for reviewing a generated resolution plan |  |

| **Config field** | **Description** |
|---|---|
| Search Mode |  |

Next Best Action Recommender configuration (continued)
Config field Description
use_websearch Enables the agentic workflow to use web searches to help collect relevant
information for generating the resolution plan
AIS Semantic ???A
Indexed Names
script_to_run Optional script to run when the Next best action recommendation AI agent
executes
save_activity Determines whether a tool creates an activity record on the
sys_aia_agent_execution_activity table when saving resolution notes
AIS Search Profile for AI search, such as Now Assist in Virtual Agent.
Profile
Return Fields Field values returned from identified relevant records
GAF Config Group Action Framework grouping configuration record, which is a collection
of groups of records to make searching easier
AIS Search Fields used by AI Search to determine what work a user has
Fields
AI Search Threshold value for whether AI Search considers a record to be related and
Matching relevant
Threshold
Table Table which has the records you want to generate resolution plans for
Related List Tables which contain related records that you want the AI agent to explore
Tables before generating resolution plans
Decomposition Agent configuration
Config field Description
agent Name of the AI agent to use for generating resolution actions
tablesinfo Table information for providing context for generated action steps
© 2026 ServiceNow, Inc. All rights reserved. 95
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **Config field** | **Description** |
|---|---|
| use_websearch |  |
| AIS Semantic Indexed Names |  |
| script_to_run |  |
| save_activity |  |
| AIS Search Profile |  |
| Return Fields |  |
| GAF Config |  |
| AIS Search Fields |  |
| AI Search Matching Threshold |  |
| Table |  |

| **Config field** | **Description** |
|---|---|
| agent |  |

Accessing the Generate resolution plan agentic workflow
To access the agentic workflow:
1.Navigate to All > AI Agent Studio > Create and manage.
2. Select Generate Resolution Plan.
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
Testing the Generate Resolution Plan agentic workflow
You can manually test an agentic workflow execution or access on the Testing page of AI Agent
Studio if you have the sn.aia_admin role and all other roles configured in the security controls.
Start a manual test, select a test type and the name of the workflow, and use utterances in the
Task field like the following samples. See Test an agentic workflow execution.
If you want to evaluate the agentic workflow over many different execution logs, run an
automated evaluation.
Sample utterance
After the workflow has been activated in AI Agent Studio, enter these or similar phrases in the
Now Assist panel to trigger the workflow. You must have the sn.now_assist_panel_user role to run
the workflow. You can also run this workflow on the Testing page of AI Agent Studio with the same
utterance in the Task field if you have the sn.aia_admin role.
•Generate resolution plan for INC0001
•Create detailed resolution steps for INC0001
•Resolve INC0001
AI agents used in the Generate resolution plan agentic workflow
The following table lists the agents that are used in the Generate resolution plan agentic
workflow.
Important: In the Select channels and status step of each AI agent's guided setup, make
sure that the Status toggle is enabled to activate the AI agent.
© 2026 ServiceNow, Inc. All rights reserved. 96
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

AI agents names and descriptions in the Generate resolution plan agentic workflow
AI agent name AI agent description Role required
Next best action Identifies the steps sn_uxc_gen_ai.platform_ai_next_best_action
recommendation for resolving tasks
AI agent by referencing the
similar task details
and reviewing
knowledge articles.
Decomposition Analyzes and sn_uxc_gen_ai.platform_ai_resolution_action_ai_agent
Agent breaks down
each previous
resolution step into
smaller, actionable
substeps, then
creates records
Other Platform agentic workflows
For more information on other agentic workflows associated with the Platform workflow, see
Platform agentic workflows.
Platform Help optimize team productivity agentic workflow
Use the Platform Help optimize team productivity AI agents agentic workflow to gather relevant
information about tasks automatically and make decisions about priorities and assignments.
Help optimize team productivity overview
The Help optimize team productivity agentic workflow offers multiple capabilities that can
enhance your team's performance. Improving assignments based on previous work and
balancing workloads, the agentic workflow can address problems that traditional work
assignment rules may have.
The agentic workflow performs the following tasks:
•Analyzes historical performance of team members
•Calculates workloads relative to each team member's typical capacity
•Enables proactive team management with data-driven insights
The agents, tools, and triggers that are associated with the Help optimize team productivity
agentic workflow are provided by Now Assist applications. You can activate the agentic workflow
template by making triggers active and setting the display settings to include the Now Assist
panel. If you want to change this agentic workflow's instructions, you must duplicate it, adjust the
settings to suit your specific needs, and activate the duplicated version of the agentic workflow
instead.
Prerequisites and setup
To access this workflow, you must have Now Assist for Platform installed on your instance, which
you can get if you install any other Now Assist application, such as Now Assist for IT Service
Management (ITSM).
© 2026 ServiceNow, Inc. All rights reserved. 97
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **AI agent name** | **AI agent description** | **Role required** |
|---|---|---|
| Next best action recommendation AI agent | Identifies the steps for resolving tasks by referencing the similar task details and reviewing knowledge articles. | sn_uxc_gen_ai.platform_ai_next_best_action |
| Decomposition Agent | Analyzes and breaks down each previous resolution step into smaller, actionable substeps, then creates records | sn_uxc_gen_ai.platform_ai_resolution_action_ai_agent |

Role masking
Required role: sn_uxc_gen_ai.platform_ai_help_allocate_work.
Role masking enables users to limit the roles and privileges of agentic workflows during tool
execution. Agentic workflows and their AI agents that get installed with Now Assist applications
are assigned pre-defined roles. If you select Users with specific roles for user
access, you must configure the security controls to include these roles. Data access settings
must also include these roles. For the instructions to change the security controls, see Define
security controls for an agentic workflow.
In the data access settings, you must also add the necessary roles to enable reading of the
tables for records assigned to team members. For example, you can add the itil role to the
agentic workflow's list of approved roles so that it can access Incident records.
Additional configuration
You can change different settings related to the agentic workflow by changing values for the Now
Assist Skill Config Var Set. To access the variable set and make changes, do the following while
in the Platform AI Agents and Skills scope:
•Go to the Now Assist Skill Config [sn_nowassist_skill_config] table.
•Open the record named Optimal Ticket Assignment.
•In the Now Assist Skill Config Var Set related list, select Work Allocator.
•Edit the variable values.
•Save or update the record.
The Help optimize team productivity configuration variable sets include the following variables.
Help optimize team productivity Work Allocator configuration
Config field Description
Tickets per The number of tickets processed by the agentic workflow for evaluation.
batch
Default: 25
Metrics How many days back to include in metric calculations.
Calculation
Window Default: 600
Assignment The assignment group whose tickets are used for evaluation, analysis, and
Group recommendations.
Table for The table used to gather information about the work assigned to team members.
Query
Backlog Filter conditions for determining what counts as "backlog" work for team members
Ticket to complete.
Query
© 2026 ServiceNow, Inc. All rights reserved. 98
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **Config field** | **Description** |
|---|---|
| Tickets per batch |  |
| Metrics Calculation Window |  |
| Assignment Group |  |
| Table for Query |  |

Help optimize team productivity Work Allocator configuration (continued)
Config field Description
Similarity The table used for gathering information about other work that has been
Score Table previously assigned to team members.
Similarity Fields to consider for calculating which tasks are similar to the one that needs
Score assigning. For example, selecting category and subcategory as similarity score
Fields fields includes those fields in calculating whether a team member has worked on
similar assignments within the metric calculation window.
Help optimize team productivity Trigger frequency configuration
Config field Description
Enable Enable the agentic workflow to run on its own using a scheduled job.
scheduled job
Assignment The assignment group whose tickets are used for evaluation, analysis, and
Group recommendations.
Scheduled job The name of the scheduled job that runs to trigger the agentic workflow.
Scheduler How often the scheduled job runs and triggers the agentic workflow.
frequency
Accessing the Help optimize team productivity agentic workflow
To access the agentic workflow:
1.Navigate to All > AI Agent Studio > Create and manage.
2. Select Help optimize team productivity.
The first step of the guided setup includes a complete list of included AI agents. Selecting the
name of an AI agent opens it in a new browser tab, where you can see the full description, role,
list of steps, and tools. Tools are displayed in the second step of the AI agent guided setup, Add
tools and information.
Testing the Help optimize team productivity agentic workflow
You can manually test an agentic workflow execution or access on the Testing page of AI Agent
Studio if you have the sn.aia_admin role and all other roles configured in the security controls.
Start a manual test, select a test type and the name of the workflow, and use utterances in the
Task field like the following samples. See Test an agentic workflow execution.
If you want to evaluate the agentic workflow over many different execution logs, run an
automated evaluation.
© 2026 ServiceNow, Inc. All rights reserved. 99
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **Config field** | **Description** |
|---|---|
| Similarity Score Table |  |

| **Config field** | **Description** |
|---|---|
| Enable scheduled job |  |
| Assignment Group |  |
| Scheduled job |  |

Sample utterance
After the workflow has been activated in AI Agent Studio, enter "Give me optimized assignment
evaluations for the Software assignment group" or similar phrases in the Now Assist panel to
trigger the workflow. You must name the specific assignment group you're allocating work for.
You must have the sn.now_assist_panel_user role to run the workflow. You can also run this
workflow on the Testing page of AI Agent Studio with the same utterance in the Task field if you
have the sn.aia_admin role.
AI agents used in the Help optimize team productivity agentic workflow
The following table lists the agents that are used in the Help optimize team productivity agentic
workflow.
Important: In the Define availability step of each AI agent's guided setup, make sure that
the Status toggle is enabled to activate the AI agent.
AI agents names and descriptions in the Help optimize team productivity agentic workflow
AI agent
AI agent description Role required
name
Work Streamlines ticket management sn_uxc_gen_ai.platform_ai_help_allocate_work
Allocator by automatically fetching backlog
AI Agent tickets, evaluating agent workloads
and performance metrics, and
assigning tickets to agents in a
way that optimizes distribution and
operational efficiency.
Other Platform agentic workflows
For more information on other agentic workflows that are associated with the Platform workflow,
see Platform agentic workflows.
Platform Identify ways to improve service agentic workflow
Use the Platform Identify ways to improve service agentic workflow to analyze feedback,
performance metrics, and historical trends that identify areas for service improvement.
Identify ways to improve service overview
The Identify ways to improve service agentic workflow optimizes service delivery and customer
satisfaction by analyzing feedback, metrics, and trends to provide actionable process
improvement recommendations. After the analysis is generated, you can continue the
conversation to ask follow-up questions or download the analysis as a PDF or Word document.
The Now Assist applications provide the agents, tools, and triggers for the Identify ways to
improve service agentic workflow. You can activate the agentic workflow template by making
triggers active and setting the display settings to include the Now Assist panel. To change this
agentic workflow's instructions, duplicate it, adjust the settings to suit your specific needs, and
activate the duplicated version instead.
© 2026 ServiceNow, Inc. All rights reserved. 100
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **AI agent name** | **AI agent description** | **Role required** |
|---|---|---|
| Work Allocator AI Agent | Streamlines ticket management by automatically fetching backlog tickets, evaluating agent workloads and performance metrics, and assigning tickets to agents in a way that optimizes distribution and operational efficiency. | sn_uxc_gen_ai.platform_ai_help_allocate_work |