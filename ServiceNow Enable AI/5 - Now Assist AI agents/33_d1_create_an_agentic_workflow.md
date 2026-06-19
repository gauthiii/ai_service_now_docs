# Create an agentic workflow

_Source pages: 121–136 | Depth: 1_

---

<!-- page 121 -->
3. If the endpoint requires a scheme prefix on the value (for example, Bearer for Google
A2A), include the prefix directly in the API Key (api_key) field value — for example, change
AIza... to Bearer AIza....
Note: The API Key Prefix field is not currently applied by the A2A flow action; embed
the scheme in the API Key value instead.
4.Save the record and re-test the external agent end-to-end.
Wizard-created credential records
The wizard creates a working API Key credential record for most A2A endpoints. Only edit the
credential record manually if your remote endpoint has specific requirements that the default
credential does not satisfy.
•Custom header name (for example, x-api-key): Set the API Key Header
(api_key_header_name) field to the header name the endpoint expects.
•Scheme prefix on the value (for example, Bearer for Google A2A): Include the prefix directly
in the API Key field value — for example, Bearer <your-key>. Don't use the API Key
Prefix field; it is not applied by the A2A flow action.
Create an agentic workflow
Create an agentic workflow in AI Agent Studio so that AI agents can coordinate to solve complex
problems.
Before you begin
Role required: sn_aia.admin
About this task
Agentic workflows solve business problems by automating processes with agentic AI. In AI Agent
Studio, you must define an agentic workflow and connect it with an AI agent to execute complex
goals. These goals can involve variable data or other factors that traditional automation can
struggle with.
Procedure
1.Navigate to All > AI Agent Studio > Create and manage > Agentic workflows and select New.
2. Define your key requirements.
3. Define the agentic workflow security controls.
4.Optional: Add a trigger to automatically invoke your agentic workflow if a specified event
occurs..
(Optional) If you want your agentic workflow to be used only in chats, you don’t need to add a
trigger.
5. Determine the channels to invoke your agentic workflow..
Result
An agentic workflow is created and can be seen in the agentic workflow list in the Create and
manage page.

<!-- page 122 -->
What to do next
•Move to the Testing playground to test your new agentic workflow using example utterances.
•Review the Platform agentic workflows.
Define key requirements for an agentic workflow
In the guided setup for an agentic workflow, write a clear description of what the agentic workflow
is, add AI agents, and select unsupported AI model providers.
Before you begin
Role required: sn_aia.admin
About this task
The first step of the guided setup includes defining the fundamentals of the agentic workflow.
The description and list of steps fields are used by the large language model (LLM) to achieve
its objectives. Descriptions and list of steps should be clear and well-defined. For guidelines for
writing these fields, see Writing effectively for agentic AI. For an example agentic workflow, see
an example agentic workflow.
You also assign the AI agents that the agentic workflow has access to in this step. The AI agents
should be clearly defined and referred to in your list of steps so that the LLM knows how to use
them. You can use existing AI agents installed with Now Assist applications or create your own.
See Create an AI agent for the steps to create your own custom AI agents.
Procedure
1.Enter a name for the workflow.
2. Craft a workflow description.
3. Craft a list of steps.
You can also use an old version of a list of steps. Select View versions for a full list of previous
versions of the field. See Version control for more information.

<!-- page 123 -->
4.Add AI agents to perform the tasks described in the list of steps.
You can use Now Assist to generate a list of AI agents for you.
5. Determine unsupported model providers.
You may find that some models use your AI agent better than others. If you want to avoid
users from having a less optimal experience with a certain model, you can mark a model as
unsupported. If an administrator changes the instance-level settings to an unsupported model,
your AI agent isn't available to users.
Result
You have written instructions for the LLM to determine how to use the agentic workflow, assigned
AI agents, and determined LLM provider support.
What to do next
Select Save and continue to move to the next step, Define security controls.
Define security controls for an agentic workflow
In the guided setup for an agentic workflow, define security controls for who can access the
agentic workflow and what data the agentic workflow has access to.
Before you begin
Role required: sn_aia.admin
About this task
The Define security controls step is divided into two parts: Define user access and Define data
access. The former creates an ACL (ACL) that determines which users can discover or invoke
the agentic workflow. The latter defines the data that the agentic workflow has access to once it’s
invoked.
See Security for AI agents for more information about creating ACLs and user identities for
security for agentic workflows.

<!-- page 124 -->
Procedure
1.Select which users can access the agentic workflow.
The drop-down menu options are:
◦Users with specified roles
◦Authenticated users
◦Public
If you select Users with specified roles, you can select exactly which roles can
access the agentic workflow. Agentic workflows installed with Now Assist applications and
their AI agents might require you to include specific roles. To learn which roles they need,
consult the documentation for the AI agent or the agentic workflow that uses the AI agent.
2. Select Save and continue to move to the next step.
Saving and moving onto the next step triggers the creation of an ACL for your agentic workflow.
If you want to make changes later, you can return to the guided setup and change the options
here. If you have the correct elevated role, you can also make edits directly on the ACL table.
3. Define the user identity of the agentic workflow to determine what data it has access to.
The two options are Dynamic user and AI user. The dynamic user is the user invoking
the agentic workflow. An AI user is a dedicated user that has its own specified roles that allow
access, which could be more than the dynamic user.
If you don't have an AI user but want to use the AI user identity, you need to create record
on the User table. See Create a user . Select AI user as the identity type.
If you select Dynamic user, you can select the Approved roles that the AI agent runs
with. By default, an AI agent runs as a dynamic user and has the roles of the invoking user.
Select the approved roles to limit the data access that an AI agent could have. Role masking
must be applied for all AI agents and agentic workflows set to run as dynamic users.
To override the role masking requirement for a specific agentic workflow or AI agent, admins
with the correct elevated access can create an approved list of roles for a given agentic
workflow or AI agent. Then, they can access that role masking record in the Agent Access Role
Configurations table [sys_agent_access_role_configuration], and select the “allow all roles”
check box. Taking these steps deactivates the requirement for a role masking approved roles
list in AI Agent Studio, so the AI admin can return to AI Agent Studio and continue to configure
the agentic workflow or AI agent without role masking applied.

<!-- page 125 -->
Note: Role masking should be applied as security general guidelines and adherence
to the principle of least privilege. Overriding the role masking requirement isn’t
recommended.
If you select AI user, the list of roles that the AI user has is displayed.
Result
You have created an ACL that determines who can discover and access your agentic workflow,
and you have assigned a user identity (and role masking, if relevant) to the agentic workflow to
determine what data it can access.
What to do next
Select Save and continue to move to the next step, Adding a trigger. Adding a trigger is optional.
You can also skip to the final step, Select channels and access.
Add a trigger to an agentic workflow
In the guided setup for an agentic workflow, add triggers to run the agentic workflow
automatically when certain conditions are met.
Before you begin
Role required: sn_aia.admin
About this task
Adding a trigger is optional. If you want your agentic workflow to be used only in chats such as
in Now Assist for Virtual Agent or Now Assist panel, you don't need to add a trigger. Only add a
trigger if you want to invoke the agentic workflow automatically when some event occurs.
Note: Triggers contain instance-specific information. If you are moving AI agents or
agentic workflows between instances using Update Sets, you must set the triggers to
inactive before adding them to the update sets and then activate them on the new instance.
If you don't want to add a trigger, skip to the final step, Select channels and access.
Procedure
1.Select Add trigger.
2. On the form, fill in the fields.

<!-- page 126 -->
Create a new trigger
Fields Description
Select trigger List of triggers that are available in the
instance.
Name Name of the trigger.
Trigger objective Additional user statements or sample
utterances that help guide when to trigger
this agentic workflow.
Define when this trigger occurs
Fields Description
Table Name of the applicable table for your agentic
workflow.
Conditions Conditions that you can add to control the
trigger configuration. You must have at least
one condition.
Select + Add condition set to add conditions
to your agentic workflow trigger.
Active trigger toggle Only enable the trigger once you’re confident
in the execution of your agentic workflow.
Try testing the agentic workflow execution
and user access first. To review overall trends
over many executions, try an automated
evaluation.

<!-- page 127 -->
Select where to show this launch
Fields Description
Channel
Medium for the agentic workflow output: Now
Assist panel or Virtual Agent.
Note: To view the output from a
triggered agentic workflow in the
Now Assist panel, you need the
now_assist_panel_user role.
Show an alert to users Alerts appear in the selected channel.

<!-- page 128 -->
If you choose a scheduled trigger, additional options are available, such as the day of the week
and time when you want the trigger to run.
Note: When running a scheduled trigger, not every record is included in the execution.
By default, the value is 10. If you want to change this number, you must set the
sn_aia.max_scheduled_trigger_query system property to a different value.
If you choose an email trigger, the target emails must exist on the Reply [sys_reply] table.
New emails aren’t available as triggers.
3. Select Add.
4.Repeat the preceding steps for additional triggers.
Result
You have added triggers to your agentic workflow to run it automatically under the specified
conditions.
What to do next
Select Save and continue to move to the final step, Select channels and access.
Select channels and access for an agentic workflow
In the guided setup for an agentic workflow, activate the agentic workflow to use in the Now
Assist panel or UI actions in the Core UI and workspaces.
Before you begin
Role required: sn_aia.admin
About this task
The final step of the agentic workflow guided setup includes options for where a user can invoke
the agentic workflow. The Now Assist panel is available to users with the correct role. You can
specify the exact conditions when a UI action is available to users on a table.

<!-- page 129 -->
Procedure
1.Select whether you want users to use the Now Assist panel to invoke the agentic workflow.
2. Optional: Add a UI action to your agentic workflow.
a.Select Add UI action.
b.Enter the UI action label.
(Optional) The UI action label is the text that the user sees in the button on the table.
c.Select a table where the UI action can be used.
(Optional) Users who are accessing a record on the selected table can view the UI action
in the Core UI and workspaces. See In-product agentic AI for more information about the AI
Workflows panel.
d. Specify conditions for the UI action to appear and select Add.
(Optional) For example, you could only show a UI action for a Generate resolution plan
agentic workflow if the record state is Active.
Note: The display for a new UI action is turned on by default.
(Optional)
3. Select Save and test.
Result
You have completed the guided setup for creating an agentic workflow. Your new agentic
workflow can be edited at any time using AI Agent Studio.

<!-- page 130 -->
If you added a UI action for your agentic workflow in this guided setup,
but the UI action is not appearing on forms, ensure that the property
com.glide.agentic_processes_view.enabled is set to true.
What to do next
Move to the Testing playground to test an agentic workflow execution using example utterances
or to test user access.
Duplicate an agentic workflow
Duplicate an existing agentic workflow in AI Agent Studio to save time by not having to manually
configure or create agentic workflows.
Before you begin
Role required: sn_aia.admin
About this task
Duplicate the agentic workflows to do the following tasks:
•Duplicate the record.
•Disallow any agentic workflows with existing names.
Custom columns, such as the Tools and Knowledge sources, Status, and a column with the
Duplicate icon ( ) are available for agentic workflows list.
Note: Selecting the Duplicate icon duplicates the selected agentic workflow.
Procedure
1.Navigate to All > AI Agent Studio > Create and manage > Agentic workflows and open the AI
agents list in AI Agent Studio.
2. Duplicate the agentic workflow from either the Manage agentic workflows and AI agents page
or the AI agent form.
Current location Navigation option
On the agentic workflows list, select the dupli­
Manage agentic workflows and AI agents
cate icon ( ) for the agentic workflow that
page
you would like to duplicate.
Open the agentic workflow that you want to
duplicate, select the menu icon ( ) next to
AI agent form
Exit on the Describe and instruct form, and se­
lect Duplicate.
You see a confirmation message in a pop-up window.

<!-- page 131 -->
3. Create a copy of the agentic workflow with the same information from the original agentic
workflow's record by selecting Duplicate.
Note:
◦The agentic workflow is duplicated with the original agentic workflow's name but it’s
appended with the suffix (Copy) to help you identify the duplicated agentic workflow
from the original agentic workflow. For example, Steps for Issue Resolution
(Copy). You can rename it and also edit the other information that is duplicated.
◦All the AI agents that were connected to the original agentic workflow are also added to
the duplicated agentic workflow. You can edit these AI agents and add more agents for
your own requirements.
4.After editing the details in the Describe and instruct section, select Save and continue.
5. In the Define Trigger section, activate any triggers that are duplicated from the original agentic
workflow if you need them and select Save and continue.
Note: The triggers that you see in the duplicated agentic workflows are from the original
agentic workflow. They aren’t active by default but you can activate them if necessary.
6.In the Toggle display section, turn on the Display toggle for the duplicated agentic workflow to
be visible in the Now Assist panel and select Save and test.
Result
You’re redirected to the AI Agent Studio home page. In the Manage and configure AI agents to
solve agentic workflow section on the Agentic workflows tab, you see the duplicated agentic
workflow.
Activate an agentic workflow template
Activate an agentic workflow that come installed with Now Assist applications in AI Agent Studio.
Before you begin
Role required: sn_aia.admin

<!-- page 132 -->
About this task
Agentic workflows that are installed with Now Assist applications aren’t automatically activated.
You must activate them before they can be used in the Now Assist panel or as a UI action. Some
may come with predefined triggers that must be set to active, too.
These predefined agentic workflows can also be used as templates for your own customized
ones. You can duplicate an agentic workflow and use it as a blueprint for one that better suits
your business needs, such as changing which records are available or providing different
instructions.
Procedure
1.Navigate to All > AI Agent Studio > Create and manage > Agentic workflows.
2. Select the agentic workflow that you want to configure.
3. Select Define trigger to go to that step in Guided Setup.
4.In the Existing triggers section, select the name of an inactive trigger to open the form.
5. Toggle the Active slider so that it’s turned on.
6.Select Save.
7.If there’s more than one trigger, repeat steps 4–6 for each trigger that you want to activate.
8.Select Save and continue.
9.Toggle the display for the Now Assist panel and/or UI action so that it’s turned on.
You have enabled the agentic workflow in the Now Assist panel. If the option isn't available, you
must enable the panel first. For more information, see Turn on the Now Assist panel.
10.Select Save and test.
Result
The agentic workflow runs when the trigger is detected in the Now Assist panel.
What to do next
After completing the steps, you're redirected to test your agentic workflow to be sure it works as
intended. You can test an execution of your agentic workflow manually or test the user access.
Once you've determined that the agentic workflow has the basic functionality you expect, you
can evaluate it using automated tests.
Modify an agentic workflow
Make changes to existing agentic workflows in AI Agent Studio to adjust them to suit your
business needs.
Before you begin
Role required: sns_aia.admin
Procedure
1.Navigate to All > AI Agent Studio > Create and manage > Agentic workflows and open the
agentic workflows list on your AI Agent Studio.
2. Select the agentic workflow that you want to modify.
3. Modify the fields in the different sections of the guided setup, making changes to the fields for
your own requirements.
The guided setup is the same as the one for creating an agentic workflow:

<!-- page 133 -->
◦Define the AI agent's specialty.
◦Define the AI agent security controls.
◦(Optional) Add a trigger to automatically invoke your AI agent if a specified event occurs..
◦Determine the channels to invoke your agentic workflow..
Note: Some fields aren't editable if the agent is associated with a Now Assist
application. If you want to make more modifications, duplicate the agentic workflow and
make changes to the duplicate.
◦For the List of steps field, you can create multiple versions of the same agentic
workflow without losing previous versions. Creating versions enables you to test different
instructions to evaluate performance. See Version control for AI agents and agentic
workflows for more information.
◦For the access control lists (ACLs), you can edit the security fields and define who can
access the agentic workflow and edit the entity to run the agentic workflow as a dynamic
user or an AI user. For more information, see Implement access control in Now Assist AI
agents.
◦For more guidance on creating effective instructions, see the general guidelines for creating
AI agents and agentic workflows.
You can navigate through the steps of the Guided Setup with the Continue and Back buttons.
4.Navigate to the last step and select Save and test to save your changes and begin testing your
modified agentic workflow.
Result
Your agentic workflow is modified and ready to test.
What to do next
You can test an execution of your agentic workflow manually or test the user access. Once you've
determined that the agentic workflow has the basic functionality you expect, you can evaluate it
using automated tests.
Manually test the execution of an agentic workflow
Test your agentic workflow in AI Agent Studio to analyze how it functions while it executes the
instructions that you defined.
Before you begin
Role required: sn_aia.admin and either admin or at least one role required by the ACL of the
agentic workflow being testing and each of the ACLs of its downstream components
About this task
After you create an agentic workflow, test it to see that it functions the way that you defined it. You
can choose to run a manual test with a single instruction to test its basic functioning, or you can
evaluate the AI agent's performance across multiple executions.
If you want to test multiple executions using execution logs, you can run an automated test. If
you select Start automated evaluation, the agentic evaluation guided setup opens in a new
browser tab. See Evaluate an agentic workflow for more details about running a new automated
evaluation.
When manually testing performance, you can see how the agentic workflow and its AI agents
interact with the AI Agent Orchestrator and the Communicator AI agent. The Orchestration

<!-- page 134 -->
is an agent that directs different AI agents, and the Communicator AI agent facilitates the
communication between the user and other AI agents.
Procedure
1.Navigate to All > AI Agent Studio > Testing.
2. Select Start manual test.
If you want to start an automated test, see Evaluate an agentic workflow for more details on that
process.
3. In the Choose a test type drop-down menu, select AI agent or workflow.
If you want to test user access security controls, see Test agentic workflow user access.
4.Select an agentic workflow that you want to test by entering the name of a workflow or
choosing from the drop-down menu.
5. Under Choose a testing mode, select the testing mode either as Premium Chat or
Standard.
Note: The Premium Chat testing mode is exclusively accessible when the Off Glide
Conversation Server plugin (com.glide.cs.offglide) is installed. If the plugin is not installed,
you will continue to access the standard testing playground.
6.In the Version drop-down list, select the version of the AI agent you want to test.
See Version control for AI agents and agentic workflows for more information about creating
and changing versions.
7.In the Task drop-down list, provide a concise summary of the task to be achieved.
Note: In the task summary, include a reference number for a specific record for better
results during your testing.
8.Select Continue to Test Chat Response.
Result
When testing an agentic workflow, you can see the AI Agent Orchestrator and AI Agent
Communicator working together to organize and manage the AI agents like a team. The AI agent
Orchestrator assigns the individual, specialized agents to complete the subtasks. The AI Agent
Communicator lets the AI Agent Orchestrator know the status of each agent.

<!-- page 135 -->
Note: If you don't have the roles necessary to pass the ACLs of the agentic workflow and
all of its AI agents and tools, you're notified that you don't have the necessary access and
the test won't execute.
Your AI agents start to execute the test autonomously to resolve the agentic workflow by taking
the input from the live agent as required.
Testing an agentic workflow
•A simulated chat experience begins on the Now Assist panel between your invoking user and
AI agent.
•At the top of the canvas, you can see information about the agentic workflow you're testing,
including its name, version, and description.
•A diagram shows the tasks and communication of the AI agents that are working together to
solve the case.
•A decision log records the thought process of each AI agent that is involved in solving the
agentic workflow.
Note: You can view the entire decision log by selecting Download logs.
You can restart the entire testing process at any time by selecting Restart.
Test user access to an agentic workflow
Run a manual test to verify that only the users you want to access the agentic workflow can do so.
Before you begin
Role required: sn_aia_admin and either admin or at least one role required by the ACL of the
agentic workflow being testing and each of the ACLs of its downstream components
About this task
You can establish the security settings for an agentic workflow in the guided setup to establish
which users can access it. See Define security controls for instructions on how to change the
user access settings. When you select Save and continue on that step of the guided setup, an
ACL is created that establishes limitations on which users can access the agentic workflow.
Once you have created these ACLs, you can verify that they work as intended by using the Test
access test type of a manual test of an agentic workflow.

<!-- page 136 -->
To see instructions for performing manual tests to evaluate performance, see Test performance
manually. For more information about automated tests, see Evaluate an agentic workflow.
Procedure
1.Navigate to All > AI Agent Studio > Testing.
2. Select Start manual test.
3. In the Test typeChoose a test type drop down, select Test access.
If you want to test the basics of how an agentic workflow works, select AI agent or
worfklow. The full instructions for that test type can be found in Test performance manually.
4.Search for or select the name of the agentic workflow you want to test.
5. Select an invoking user.
The invoking user can be the user that triggers the agentic workflow or it can be the invoking
user of an upstream component, such as an agentic workflow. For more information about how
the invoking user works, see Security for AI agents.
When you select an invoking user, the user roles are populated in the Invoking user
roles field. The field is read-only. If you want to change a user's roles, you must change the
user's User record. See Assign a role to a user .
6.Select Test access.
Result
The results of the access test are opened in the Access Analyzer in a new browser tab.
Access Analyzer identifies all the ACL calls made in the execution of the agentic workflow,
including its AI agents and tools, if any are present. You can see the results of each ACL to verify
that each one has the correct user access defined.
What to do next
If the results are different than what you expect or want, you can redefine the security controls of
the agentic workflow.
You can also test an agentic workflow's performance with either a manual test or automated
evaluations. See Test performance manually or Evaluate an agentic workflow.