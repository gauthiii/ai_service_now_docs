# Create an AI agent

_Source pages: 59–120 | Depth: 1_

---

<!-- page 59 -->
Note: The enforcement applies only to the freshly reset instances. Any instances that
aren't reset aren't affected by this configuration change.
Scope and applicability
The deny-by-default ACL configuration applies under the following conditions:
•The instance is a freshly reset instance.
•The ACL type is one of the five agentic types.
•The existing ACL record uses a wildcard (*) pattern.
Security benefits
Enforcing deny-by-default ACLs for agentic types provides the following security benefits:
•Reduces the risk of unauthorized access to AI agents and agentic workflows resulting from
permissive wildcard ACLs.
•Verifies that records without explicit ACL entries aren't inadvertently exposed.
•Aligns the platform with secure-by-default principles for AI agentic components.
•Provides a clear, auditable ACL model for agentic workflows and AI agents.
Create an AI agent
Create an AI agent in AI Agent Studio to solve problems for your users and coordinate with other
AI agents while executing the agentic workflows.
Before you begin
Role required: sn_aia.admin
About this task
In the ServiceNow agentic ecosystem, an AI agent is a set of large language model (LLM)
instructions and tools that can perform specific tasks.
An AI agent can collaborate with other agents to achieve better results by using fewer LLM calls.
AI agents can also reach out to the user if they need any help or information.
Procedure
1.Navigate to All > AI Agent Studio > Create and manage > AI agents.
2. From the Add drop-down menu, select one of the following agent creation options:Chat or
External.
a.Chat: Select the Chat option to create AI agents in the AI Agent Studio to connect with
internal AI agents within the ServiceNow AI Platform to execute agentic workflows.
The following instructions are for Chat AI agents. See the following links for guides to create
other types of AI agents.
b.Voice: Select the Voice option to create an AI voice agent.
See Deploy AI agents for voice for more information on setting up and creating AI voice
agents.

<!-- page 60 -->
c.External: Select the External option to create external AI agents in the AI Agent Studio to
connect the ServiceNow AI Platform with the third-party agentic AI providers.
For more information about creating external AI agents in the AI Agent Studio, see Create an
external AI agent.
3. Define the AI agent's specialty.
4.Define the AI agent security controls.
5. Optional: Add a trigger to automatically invoke your AI agent if a specified event occurs..
(Optional) If you want your AI agent to be used only in chats, you don’t need to add a trigger.
6.Determine the chat assistants to access your AI agent, set the processing messages, and
activate your AI agent..
7.Select Save and test to complete the configuration steps or review a previous step by
selecting Back.
Selecting Save and test leads you to the AI agent testing page, where you can test the AI agent
that you created. For more information, see Manually test the execution of an AI agent.
To test the AI agent, you must have the sn_aia.admin role and any roles the ACLs configured
for the AI agent and its tools require, if applicable.
Result
You can see the AI agent that you created in the Manage agentic workflows and AI agents
page.
If you selected Users with specific roles for your ACL, you can change roles at any point. Return
to the guided setup and double-click the pills to make changes. All other security changes must
be done on the ACL [sys_security_acl] table by a user with elevated permissions.
Find AI agents
Find available AI agents in AI Agent Studio to explore your options when creating agentic
workflows.
Before you begin
Role required: sn_aia_viewer.
About this task
AI agents are autonomous systems that interact with their environment to gather data, make
decisions, and complete tasks that would otherwise need to be done by a human.
Procedure
1.View the available AI agents in AI Agent Studio.
Current location Navigation option
Select the Explore all button in the Ready-
AI Agent Studio Overview page made agentic workflow and AI agents section,
and then select the AI agents tab.
View the Recent agentic workflows and AI
AI Agent Studio Overview page
agents activity section on the AI agents tab

<!-- page 61 -->
Current location Navigation option
to see the most recently added or changed
agents.
Note: You see a list of the AI agents on­
ly when there's recent activity of the AI
agents on your instance.
Navigate to All > AI Agent Studio > Create
Anywhere else and manage, and then select the AI agents
tab.
2. View all AI agents, including those AI agents that were installed with Now Assist applications
by navigating to the AI agents tab.
Result
Navigating through any of the preceding options directs you to the AI agents that are available on
your AI Agent Studio instance.
Define the specialty of an AI agent
In the guided setup for an AI agent, write a clear description defining your agent and its role. You
can also configure supported LLMs, enable third-party access, and manage long-term memory.
Before you begin
Role required: sn_aia.admin
About this task
The first step of the guided setup enables you to define the fundamentals of the AI agent. The
description, AI agent role, and list of steps fields are used by the LLM to understand how to use
the AI agent, by itself or as part of an agentic workflow. Descriptions, AI agent roles, and list
of steps should be clear and well-defined. For guidelines for writing these fields, see Writing
effectively for agentic AI. For an example AI agent, see Example AI agent.

<!-- page 62 -->
Note: If you have the Off Glide Conversation Server plugin (com.glide.cs.offglide) installed
on your ServiceNow instance, then the Premium Chat experience may differ from the
standard experience. If you plan to use an AI agent in the Premium Chat mode, make sure
to test so it works as expected.
Procedure
1.Enter a name for the AI agent.
2. Craft an AI agent description.
The description should clarify the purpose of the AI agent, including its inputs, outputs, and
context.
3. Craft the AI agent role.

<!-- page 63 -->
The difference between the description and the agent role is that the agent role provides more
detail about the function that the AI agent serves within a greater context. The greater context
may be as part of an agentic workflow, or it could be the specific function it serves in another
type of work process.
4.Craft a list of steps.
You can also use an old version of a list of steps. Select View versions for a full list of previous
versions of the field. See Version control for more information.
5. Determine unsupported model providers.
You may find that some models use your AI agent better than others. If you want to avoid
users from having a less optimal experience with a certain model, you can mark a model as
unsupported. If an administrator changes the instance-level settings to an unsupported model,
your AI agent won't be available to users.
6.Determine if the AI agent can be accessed by third parties.
Make your AI agent discoverable by turning on the Allow third-party to access this AI agent
toggle button that enables you to use your ServiceNow AI agent on other platforms. You can
still use it on your ServiceNow instances as well.
See ServiceNow agents as secondary agents for more information about configuring agents to
use on other AI platforms.
7.Configure long-term memory options.
Long-term memory for AI agents enables agents to access data outside of the specific
conversation or trigger that executes it. For example, you can select the Device and
Software category to give the AI agent access to user information about the kinds of
hardware devices and software that are available to the invoking user. The AI agent can
remember this information in later conversations.
◦For more information about creating LTM categories, see Create long-term memory category.
◦For more information about selecting the categories to map them to you AI agent, see Map
long-term memory category.
8.Configure AI agent learning.
You can enable the AI agent to learn from past interactions with the user. For example, if the
user encounters a similar issue, enabling this feature could help the AI agent understand what
didn't work previously, so it can recommend other options.
Note: When the agent learning capability is inactive at the AI Agent Studio level, the
option to enable at the AI agent level is also inactive. To enable agent learning at the AI
Agent Studio level, see Set up long-term memory.
Result
You have defined the basics of your AI agent.
What to do next
Select Save and continue to move to the next step, Add tools and information.
Add tools and information to an AI agent
Add a tool to an AI agent to enable different functionalities and help your AI agents achieve their
objectives.

<!-- page 64 -->
Tool overview
Tools provide your AI agents with the capabilities necessary to complete their tasks. When
adding tools, consider how the AI agent uses them to achieve its objectives as well as how those
tools interact with each other. Providing your AI agents with the appropriate tools help promote
the robustness and quality of their performance.
Some additional guidelines for adding and creating tools are the following:
•Design tools to work together. Your AI agent should solve a specific, discrete task, and the tools
should give the AI agent the capabilities necessary to achieve its goal.
•Write detailed tool descriptions. Tool descriptions are used by the AI agent to determine a
tool's function. Thorough descriptions about what the tools are and how they work give the AI
agent the best chance to succeed.
•Consider the outputs of tools when creating them. Use the tool description or output
transformation strategy fields to describe how to process the tool outputs. For example, if you
have a tool that gathers records from a large number of tables, provide the tool with plans for
how to handle the large number of records.
Note: If you select Google as your web search tool provider, the web search tool leverages
Grounding with Google Search , offered under a Global Standard deployment. Because
grounding isn’t data resident , Google's global infrastructure routes traffic to a global
datacenter for each web search request. This processing may be different than your data
processing location chosen for your ServiceNow instance. Consider your organization's
data policies before enabling AI agents that use Google web search tools.
Once you have added the tools to your AI agent, you can select Save and continue to move to
the next step in the guided setup.
Knowledge graphs
In this step, you can also add Knowledge graphs. Knowledge graphs give the AI agent
information to understand the relationships between real-world entities to improve its outputs.
For example, you could add a Knowledge Graph to an approval AI agent that maps users to
their location, company, and department to help the AI agent understand the specific approval
process to apply.
Supervised execution mode for AI agents
You can minimize the potential negative impact of an AI agent not executing as expected by
configuring AI agents' tools to run in supervised mode. Running in supervised mode means that
the tools use human oversight when executing actions. You can use the Supervised mode to
enhance security for agents with the capability to perform sensitive or critical actions.

<!-- page 65 -->
You can set the supervised execution mode when creating a tool in the AI agent guided setup.
For example, choose Supervised as the Execution mode when adding a catalog item tool. For
reference, see Add a catalog item to an AI agent.
Add a catalog item to an AI agent
Add a Service Catalog to an AI agent in AI Agent Studio so that your users can access
conversational catalog items.
Before you begin
Role required: sn_aia.admin
Procedure
1.Navigate to All > AI Agent Studio > Create and manage > AI agents.
2. Open the AI agent that you want to add a catalog item to and navigate to the Add tools and
information section.
3. In the Add tool drop-down list, select Catalog item.
4.On the form, fill in the fields.
Add a catalog item form
Fields Description
Name
Name that you want to specify for your
catalog item.
Description Description of the catalog item and what it’s
going to do to assist your AI agent.
Note: This description is sent to the
large language model (LLM).
Select catalog item Catalog item that you want to add.
If there is a tool used by an AI agent for the
same catalog item, the rest of the form will
populate the fields based on the other tool.
You can make any changes specific to the
current AI agent to suit your needs, and it will
not affect the tool of the existing AI agent.
Execution mode Mode of execution for your selected catalog
item:
◦Supervised: Inputs from your human agent
are required during the execution of this
catalog item while the AI agent runs.
◦Autonomous: Doesn't require any input
from your live agent during the execution of
this catalog item while the AI agent runs.
Display output Permission to display the output of the
execution in the Now Assist panel or in Virtual
Agent:

<!-- page 66 -->
Fields Description
◦Yes
◦No
If you want the AI agent to work in Off Glide
architecture with Premium Chat experience,
you must turn-on the Display output toggle.
When the toggle is turned-on, you can add
widgets that can be used in assistants built
with Premium Chat experiences. The widget
configuration includes:
◦Widget: Defines the display output
to render the content in a better user
experience. You can select the widget from
the drop-down.
◦Require widget transformation: An
additional LLM call is required to transform
the raw tool. If you choose to skip this
transformation step, the tool output will be
directly mapped to the widget.
▪Yes
▪No
◦Display refined widget message: Refines
the widget message when configured.
▪Yes
▪No
Note: The display output as a
toggle is exclusively available for the
Premium Chat experience when the
Off Glide Conversation Server plugin
(com.glide.cs.offglide) is installed. If the
plugin is not installed, you will continue
to access the standard display output
options.
Advanced settings
Select an output transformation format Style for the LLM to present the results as
it passes information between tools and to
other agents. Out transformation formats:
◦None
◦Concise
◦Paragraph
◦Summary
◦Custom
Write processing messages for users Message to display to users during tool
execution.

<!-- page 67 -->
Fields Description
◦In-progress message: Write an in-progress
message to be displayed to end-users
while the tool is running.
◦Completion message: Write a completion
message to be displayed to end-users
once the tool finishes running.
5. Select Add.
A catalog item is added in the Catalog items list on the Add tools and information page.
Add a conversational topic to an AI agent
Add a Virtual Agent topic to an AI agent in AI Agent Studio so that you can use conversations to
get additional information from the user. For example, a conversational topic could be used to let
a user select a date range for surveys.
Before you begin
Role required: sn_aia.admin
Procedure
1.Navigate to All > AI Agent Studio > Create and manage > AI agents.
2. Open the AI agent that you want to add a conversational topic to and navigate to the Add tools
and information section.
3. In the Add tool drop-down list, select Conversational topic.
4.On the form, fill in the fields.
Add a conversational topic form
Fields Description
Name
Name that you want to specify for your
conversational topic.
Description Description of the conversational topic and
what it’s going to do to assist your AI agent.
Note: This description is sent to the
large language model (LLM).
Select topic The Virtual Agent topic that you want to add.
After it’s selected, the description of the topic
displays underneath the drop-down list.
If there is a tool used by an AI agent for
the same conversational topic, the rest of
the form will populate the fields based on
the other tool. You can make any changes
specific to the current AI agent to suit your
needs, and it will not affect the tool of the
existing AI agent.

<!-- page 68 -->
Fields Description
Note: Only large language model
(LLM) topics can be selected.
Execution mode Mode of execution for your selected
conversational topic:
◦Supervised: Inputs from your human agent
are required during the execution of this
conversational topic while the AI agent
runs.
◦Autonomous: Doesn't require any input
from your live agent during the execution of
this conversational topic while the AI agent
runs.
Display output Permission to display the output of the
execution in the Now Assist panel or in Virtual
Agent:
◦Yes
◦No
If you want the AI agent to work in Off Glide
architecture with Premium Chat experience,
you must turn-on the Display output toggle.
When the toggle is turned-on, you can add
widgets that can be used in assistants built
with Premium Chat experiences. The widget
configuration includes:
◦Widget: Defines the display output
to render the content in a better user
experience. You can select the widget from
the drop-down.
◦Require widget transformation: An
additional LLM call is required to transform
the raw tool. If you choose to skip this
transformation step, the tool output will be
directly mapped to the widget.
▪Yes
▪No
◦Display refined widget message: Refines
the widget message when configured.
▪Yes
▪No

<!-- page 69 -->
Fields Description
Note: The display output as a
toggle is exclusively available for the
Premium Chat experience when the
Off Glide Conversation Server plugin
(com.glide.cs.offglide) is installed. If the
plugin is not installed, you will continue
to access the standard display output
options.
Advanced settings
Select an output transformation format Style for the LLM to present the results as
it passes information between tools and to
other agents. Out transformation formats:
◦None
◦Concise
◦Paragraph
◦Summary
◦Custom
Write processing messages for users Message to display to users during tool
execution.
◦In-progress message: Write an in-progress
message to be displayed to end-users
while the tool is running.
◦Completion message: Write a completion
message to be displayed to end-users
once the tool finishes running.
5. Select Add.
A conversational topic is added in the Conversational topics list on the Add tools and
information page.
Add a defined desktop action tool to an AI agent for desktop and web-based task
Add a desktop action as a tool to an AI agent in AI Agent Studio so that AI agents can execute
defined path desktop actions for repetitive tasks in desktop and web environment.
Before you begin
Familiarize yourself with defined path desktop actions. For more information, see Defined
desktop actions for desktop and web-based tasks and Defined path desktop actions in AI
Desktop Actions.
Role required: sn_aia.admin
About this task
Desktop actions are tools that AI agents use to interact with web and desktop applications.
When you configure an AI agent and select desktop action as a tool, you define whether the
AI agent follows a defined path (fixed steps designed in AI Desktop Actions) or an adaptive
path (high-level goal described in the tool configuration). Unlike adaptive path desktop actions
that dynamically plan execution, defined path desktop actions enable AI agents to execute
preconfigured workflows through a fixed sequence of steps.

<!-- page 70 -->
Defined desktop actions are further categorized into on-screen tasks and background tasks.
•On-screen tasks: These actions help you simulate humans interacting with UI elements
on your thick client applications, legacy systems, or SaaS applications without APIs. These
actions include clicking buttons, typing into text boxes, selecting from drop-down menus, and
more. They encapsulate repeatable UI interactions, such as screens, anchors, and steps. You
can create, manage, and test your desktop actions in AI Desktop Actions.
•Background tasks: These actions include prebuilt connectors that enable your AI agents
to interact with various applications and system components in the background. These
connectors streamline automation by offering actions for common tasks, reducing the need for
complex scripting. Each connector focuses on a specific application or system area, providing
a collection of related methods. You can't create background tasks actions.
Procedure
1.Navigate to All > AI Agent Studio > Create and manage > AI agents.
2. Open the AI agent that you want to add a desktop action to.
For creating an AI agent, see Create an AI agent.
3. Navigate to the Add tools and information step.
4.In the Add tool drop-down list, select Desktop action.
5. Select or create a desktop action.
Existing desktop action New desktop action
a.Select an existing desktop action of type a.On the Add a desktop action modal, select
on-screen task or background task from the the Click here to create a desktop action
Select a desktop action drop-down list. link.
The background task desktop actions are
supported for the following applications:
▪Microsoft Excel
▪Microsoft Outlook
▪Microsoft Word
▪PDF
▪PowerShell Connector

<!-- page 71 -->
Existing desktop action New desktop action
▪SQL b.Select the option Record a fixed sequence
of steps for desktop and web-based tasks.
▪SSH
c.Select Open AI Desktop Actions app.
▪SystemAction
b.Select Continue. Record or manually capture the desktop
action in AI Desktop Actions Windows
application, activate it, and then come
back here to add it as a tool. For more
information, see Defined path desktop
actions in AI Desktop Actions.
The creation process of defined desktop
actions ends here.
6.On the form, fill in the fields.
Add a desktop action form
Fields Description
Desktop action description Read-only. Description of the desktop action
or application that you selected.
Applications Read-only. Applications that this desktop
action interacts with.
Note: This field appears only when
On-screen task desktop action is
selected.
Created by Read-only. User who created the desktop
action.
Note: This field appears only when
On-screen task desktop action is
selected.
Last updated Read-only. Date when this desktop action
was last updated.
Note: This field appears only when
On-screen task desktop action is
selected.
Inputs Read-only. Input parameters associated with
this desktop action.
Note: This field appears when
a desktop action or application is
selected from the list.
Outputs Read-only. Output parameters associated
with this desktop action.

<!-- page 72 -->
Fields Description
Note: This field appears when
a desktop action or application is
selected from the list.
Name Name that you want to specify for your
selected desktop action.
Tool description Description of the desktop action tool and
what it’s going to do to assist your AI agent.
Note: This description is sent to the
large language model (LLM).
Map parameters
Important:
If you update a desktop action after mapping its inputs in AI Agent Studio, the agent
continues to use the previous mapping until you reopen the tool configuration and save
it again.
If you rename an input in the desktop action, the agent treats it as a new input and the
existing mapping for that input is removed. You must remap the renamed input before
the desktop action can be saved.
Step name Read-only. The name of the step that is
configured to use a parameter.
Note: This field appears only when
an On-screen task desktop action with
inputs configured for parameters is
selected.
Description Read-only. The description entered for the
step that is configured to use a parameter.
Note: This field appears only when
an On-screen task desktop action with
inputs configured for parameters is
selected.
Parameter record Select the Desktop action parameter record
that the AI agent must use to retrieve the
value for this step at execution time. Mapping
a parameter record is required for all steps
before the desktop action can be saved.

<!-- page 73 -->
Fields Description
Note: This field appears only when
an On-screen task desktop action with
inputs configured for parameters is
selected.
The same parameter record can be
mapped to multiple steps. Each step
can only be mapped to one parameter
record.
Execution mode Mode of execution for your selected desktop
action:
◦Supervised: Inputs from your live agent
are required during the execution of this
desktop action while the AI agent runs.
◦Autonomous: Doesn't require any input
from your live agent during the execution of
this desktop action while the AI agent runs.
Display output Permission to display the output of the
execution in the Now Assist panel or in Virtual
Agent:
◦Yes
◦No
If you want the AI agent to work in Off Glide
architecture with Premium Chat experience,
you must turn-on the Display output toggle.
When the toggle is turned-on, you can add
widgets that can be used in assistants built
with Premium Chat experiences. The widget
configuration includes:
◦Widget: Defines the display output
to render the content in a better user
experience. You can select the widget from
the drop-down.
◦Require widget transformation: An
additional LLM call is required to transform
the raw tool. If you choose to skip this
transformation step, the tool output will be
directly mapped to the widget.
▪Yes
▪No
◦Display refined widget message: Refines
the widget message when configured.
▪Yes
▪No

<!-- page 74 -->
Fields Description
Note: The display output as a
toggle is exclusively available for the
Premium Chat experience when the
Off Glide Conversation Server plugin
(com.glide.cs.offglide) is installed. If the
plugin is not installed, you will continue
to access the standard display output
options.
Advanced settings
Select an output transformation format Style for the LLM to present the results as
it passes information between tools and to
other agents. Out transformation formats:
◦None
◦Concise
◦Paragraph
◦Summary
◦Custom
Write processing messages for users Message to display to users during tool
execution.
◦In-progress message: Write an in-progress
message to be displayed to end-users
while the tool is running.
◦Completion message: Write a completion
message to be displayed to end-users
once the tool finishes running.
7.Select Add desktop action.
The desktop action is added in the Desktop actions list on the Add tools and information page.
What to do next
For more information about executing desktop actions, see Examples of executing desktop
actions using AI agents.
Add a file upload to an AI agent
Upload files for analysis by an AI agent in AI Agent Studio to grant your AI agent access to
specialized knowledge.
Before you begin
Role required: sn_aia.admin
Procedure
1.Navigate to All > AI Agent Studio > Create and manage > AI agents.
2. Open the AI agent that you want to add a file upload to and navigate to the Add tools and
information section.
3. In the Add tool drop-down list, select File upload.
4.On the form, fill in the fields.

<!-- page 75 -->
Add file upload form
Fields Description
Name
Name that you want to specify for your file
upload.
Description Description of the file upload and what it’s
going to do to assist your AI agent.
Note: This description is sent to the
large language model (LLM).
Execution mode Mode of execution for your selected file
upload:
◦Supervised: Inputs from your human agent
are required during the execution of this
uploaded file while the AI agent runs.
◦Autonomous: Doesn't require any input
from your live agent during the execution of
this uploaded file while the AI agent runs.
Display output Permission to display the output of the
execution in the Now Assist panel or in Virtual
Agent:
◦Yes
◦No
If you want the AI agent to work in Off Glide
architecture with Premium Chat experience,
you must turn-on the Display output toggle.
When the toggle is turned-on, you can add
widgets that can be used in assistants built
with Premium Chat experiences. The widget
configuration includes:
◦Widget: Defines the display output
to render the content in a better user
experience. You can select the widget from
the drop-down.
◦Require widget transformation: An
additional LLM call is required to transform
the raw tool. If you choose to skip this
transformation step, the tool output will be
directly mapped to the widget.
▪Yes
▪No
◦Display refined widget message: Refines
the widget message when configured.
▪Yes
▪No

<!-- page 76 -->
Fields Description
Note: The display output as a
toggle is exclusively available for the
Premium Chat experience when the
Off Glide Conversation Server plugin
(com.glide.cs.offglide) is installed. If the
plugin is not installed, you will continue
to access the standard display output
options.
Attachments For analysis by an AI agent, attach up to
5 files with a maximum size of 5 MB each
in these file formats: PDF, DOCX, or TXT
formats.
Note: A user who interacts with the AI
agent with the file upload tool can see
the information contained within the
files.
Advanced settings
Select an output transformation format Style for the LLM to present the results as
it passes information between tools and to
other agents. Out transformation formats:
◦None
◦Concise
◦Paragraph
◦Summary
◦Custom
Write processing messages for users Message to display to users during tool
execution.
◦In-progress message: Write an in-progress
message to be displayed to end-users
while the tool is running.
◦Completion message: Write a completion
message to be displayed to end-users
once the tool finishes running.
5. Select Add.
A file upload is added to the AI agent.
Add a flow action to an AI agent
Add a flow action to an AI agent in AI Agent Studio. Define the flow action to use it as a reusable
operation in automating the ServiceNow AI Platform features without having to write code.
Before you begin
When an AI agent uses a flow action tool, the user the AI agent is running as must pass the ACL
of the flow action. Ensure that the security configurations for the flow action are met by the AI
agent and agentic workflow. For more information, see Security for AI agents.

<!-- page 77 -->
Role required: sn_aia.admin
Procedure
1.Navigate to All > AI Agent Studio > Create and manage > AI agents.
2. Open the AI agent that you want to add a flow action to and navigate to the Add tools and
information section.
3. In the Add tool drop-down list, select Flow action.
4.On the form, fill in the fields.
Add a flow action form
Fields Description
Name
Name that you want to specify for your
selected flow action.
Tool description Description of the flow action and what it’s
going to do to assist your AI agent.
Note: This description is sent to the
large language model (LLM).
Select flow action Existing automated process to be selected
from the list.
If there is a tool used by an AI agent for the
same flow action, the rest of the form will
populate the fields based on the other tool.
You can make any changes specific to the
current AI agent to suit your needs, and it will
not affect the tool of the existing AI agent.
Inputs Flow action inputs. The values are filled in by
the LLM at runtime unless you specify a value
override.
Note: If the agent uses multiple tools,
you can choose to use another tool's
output as an input value override. Select
the data picker icon ( ) to review the
available options.
Execution mode Mode of execution for your selected flow
action:
◦Supervised: Inputs from your human agent
are required during the execution of this
flow action while the AI agent runs.
◦Autonomous: Doesn't require any input
from your live agent during the execution of
this flow action while the AI agent runs.

<!-- page 78 -->
Fields Description
Display output Permission to display the output of the
execution in the Now Assist panel or in Virtual
Agent:
◦Yes
◦No
If you want the AI agent to work in Off Glide
architecture with Premium Chat experience,
you must turn-on the Display output toggle.
When the toggle is turned-on, you can add
widgets that can be used in assistants built
with Premium Chat experiences. The widget
configuration includes:
◦Widget: Defines the display output
to render the content in a better user
experience. You can select the widget from
the drop-down.
◦Require widget transformation: An
additional LLM call is required to transform
the raw tool. If you choose to skip this
transformation step, the tool output will be
directly mapped to the widget.
▪Yes
▪No
◦Display refined widget message: Refines
the widget message when configured.
▪Yes
▪No
Note: The display output as a
toggle is exclusively available for the
Premium Chat experience when the
Off Glide Conversation Server plugin
(com.glide.cs.offglide) is installed. If the
plugin is not installed, you will continue
to access the standard display output
options.
Advanced settings
Select an output transformation format Style for the LLM to present the results as
it passes information between tools and to
other agents. Out transformation formats:
◦None
◦Concise
◦Paragraph
◦Summary
◦Custom

<!-- page 79 -->
Fields Description
Write processing messages for users Message to display to users during tool
execution.
◦In-progress message: Write an in-progress
message to be displayed to end-users
while the tool is running.
◦Completion message: Write a completion
message to be displayed to end-users
once the tool finishes running.
5. Select Add.
A flow action is added in the Flow actions list on the Add tools and information page.
Add a Knowledge Graph to an AI agent
Add a Knowledge Graph to an AI agent in AI Agent Studio that uses the structured and
unstructured data from different ServiceNow records to enhance the performance of AI agents.
Before you begin
Role required: sn_aia.admin
Procedure
1.Navigate to All > AI Agent Studio > Create and manage > AI agents.
2. Select New or open the AI agent that you want to add a Knowledge Graph to and navigate to
the Add tools and information section.
3. In the Add tool drop-down list, select Knowledge graph.
You may have to scroll down.
4.On the form, fill in the fields.
Add a Knowledge Graph form
Fields Description
Name
Name that you want to specify for your
selected Knowledge Graph.
Description Description of the Knowledge Graph and
what it’s going to do to assist your AI agent.
Note: This description is sent to the
large language model (LLM).
Select Knowledge Graph Existing Knowledge Graph to be added to the
AI agent.
If there is a tool used by an AI agent for the
same Knowledge Graph, the rest of the form
will populate the fields based on the other
tool. You can make any changes specific to
the current AI agent to suit your needs, and it
will not affect the tool of the existing AI agent.

<!-- page 80 -->
Fields Description
You can utilize Enterprise Graph and
Enterprise Graph (Small) as Knowledge
Graph resources while creating the
Knowledge Graph tool.
Query instruction The search query. Translate your request into
a search query, including a verb.
The query instruction is passed on to the LLM
to generate a structured query for the Graph
from the inputs selected in the tool form.
Conversation history When enabled, the last 5 conversation turns
are passed to the Knowledge Graph tool,
allowing users to ask follow-up questions on
the previously returned results. Turn off the
toggle if each query should be treated as a
standalone lookup.
Note: The knowledge graph tools
added previously to your AI agents will
have the Conversation history turned off
by default.
Execution mode Mode of execution for your selected
Knowledge Graph:
◦Supervised: Inputs from your human agent
are required during the execution of this
Knowledge Graph while the AI agent runs.
◦Autonomous: Doesn't require any input
from your live agent during the execution
of this Knowledge Graph while the AI agent
runs.
Display output Permission to display the output of the
execution in the Now Assist panel or in Virtual
Agent:
◦Yes
◦No
If you want the AI agent to work in Off Glide
architecture with Premium Chat experience,
you must turn-on the Display output toggle.
When the toggle is turned-on, you can add
widgets that can be used in assistants built
with Premium Chat experiences. The widget
configuration includes:
◦Widget: Defines the display output
to render the content in a better user
experience. You can select the widget from
the drop-down.
◦Require widget transformation: An
additional LLM call is required to transform

<!-- page 81 -->
Fields Description
the raw tool. If you choose to skip this
transformation step, the tool output will be
directly mapped to the widget.
▪Yes
▪No
◦Display refined widget message: Refines
the widget message when configured.
▪Yes
▪No
Note: The display output as a
toggle is exclusively available for the
Premium Chat experience when the
Off Glide Conversation Server plugin
(com.glide.cs.offglide) is installed. If the
plugin is not installed, you will continue
to access the standard display output
options.
Advanced settings
Select an output transformation format Style for the LLM to present the results as
it passes information between tools and to
other agents. Out transformation formats:
◦None
◦Concise
◦Paragraph
◦Summary
◦Custom
Write processing messages for users Message to display to users during tool
execution.
◦In-progress message: Write an in-progress
message to be displayed to end-users
while the tool is running.
◦Completion message: Write a completion
message to be displayed to end-users
once the tool finishes running.
5. Select Add.
The Knowledge Graph tool is added to the AI agent.
Add a Now Assist skill to an AI agent
Add a generative AI skill to an AI agent in AI Agent Studio. You can customize the skills to meet
the needs of your users in different workflows.
Before you begin
If you want to add a custom skill to an AI agent, the skill must be published and activated on the
Now Assist Admin console. For more information on deploying custom skills, see Finalize and
publish a custom skill and Activate a custom skill.

<!-- page 82 -->
When an AI agent uses a skill as a tool, the user the AI agent is running as must pass the ACL of
the skill. Ensure that the security configurations for the skill are met by the AI agent and agentic
workflow. For more information on setting skill-level ACLs, see Configure access control lists for a
skill.
Role required: sn_aia.admin
Procedure
1.Navigate to All > AI Agent Studio > Create and manage > AI agents.
2. Open the AI agent that you want to add a skill to and navigate to the Add tools and information
section.
3. In the Add tool drop-down list, select Now Assist skill.
4.On the form, fill in the fields.
Add a Now Assist skill form
Fields Description
Name
Name that you want to specify for your skill.
Description Description of the skill and what it's going to
do to assist your AI agent.
Note: This description is sent to the
large language model (LLM).
Select skill Existing skill to be selected from the list.
If there is a tool used by an AI agent for the
same skill, the rest of the form will populate
the fields based on the other tool. You can
make any changes specific to the current AI
agent to suit your needs, and it will not affect
the tool of the existing AI agent.
Inputs Skill inputs. The values are filled in by the
LLM at runtime unless you specify a value
override.
Note: If the agent uses multiple tools,
you can choose to use another tool's
output as an input value override. Select
the data picker icon ( ) to review the
available options.
Execution mode Mode of execution for your skill:
◦Supervised: Inputs from your human agent
are required during the execution of this
tool while the AI agent runs.
◦Autonomous: Doesn't require any input
from your live agent during the execution of
this tool while the AI agent runs.

<!-- page 83 -->
Fields Description
Display output Permission to display the output of the tool
execution in the Now Assist panel or in Virtual
Agent:
◦Yes
◦No
If you want the AI agent to work in Off Glide
architecture with Premium Chat experience,
you must turn-on the Display output toggle.
When the toggle is turned-on, you can add
widgets that can be used in assistants built
with Premium Chat experiences. The widget
configuration includes:
◦Widget: Defines the display output
to render the content in a better user
experience. You can select the widget from
the drop-down.
◦Require widget transformation: An
additional LLM call is required to transform
the raw tool. If you choose to skip this
transformation step, the tool output will be
directly mapped to the widget.
▪Yes
▪No
◦Display refined widget message: Refines
the widget message when configured.
▪Yes
▪No
Note: The display output as a
toggle is exclusively available for the
Premium Chat experience when the
Off Glide Conversation Server plugin
(com.glide.cs.offglide) is installed. If the
plugin is not installed, you will continue
to access the standard display output
options.
Advanced settings
Select an output transformation format Style for the LLM to present the results as
it passes information between tools and to
other agents. Out transformation formats:
◦None
◦Concise
◦Paragraph
◦Summary
◦Custom

<!-- page 84 -->
Fields Description
Write processing messages for users Message to display to users during tool
execution.
◦In-progress message: Write an in-progress
message to be displayed to end-users
while the tool is running.
◦Completion message: Write a completion
message to be displayed to end-users
once the tool finishes running.
5. Select Add.
A Now Assist skill tool is added in the Skills section on the Add tools and information page.
Add a record operation to an AI agent
Add a record operation to an AI agent in AI Agent Studio to create, update, look up, or delete
records.
Before you begin
Role required: sn_aia.admin
Procedure
1.Navigate to All > AI Agent Studio > Create and manage > AI agents.
2. Open the AI agent that you want to add a record operation to and navigate to the Add tools
and information section.
3. In the Add tool drop-down list, select Record operation.
4.On the form, fill in the fields.
Add a record operation form
Fields Description
Select a type of record operation to add If you select An existing one, you can select
a record operation tool used by the current
AI agent or any other AI agent. You can make
changes to the settings of that tool to fit the
needs of your specific AI agent.
Name
Name that you want to specify for your record
operation.
Description Description of the record operation and what
it’s going to do to assist your AI agent.
Note: This description is sent to the
large language model (LLM).
Inputs
◦Input name: Name of the input for the LLM
to use.
◦Description: Description of the input to
give the LLM context.

<!-- page 85 -->
Fields Description
◦Value override: Value for the input. If you
leave it blank, generative AI fills in the value
for you.
Note: If the agent uses multiple
tools, you can choose to use another
tool's output as an input value
override. Select the data picker icon
( ) to review the available options.
Table Table that you want to perform the record
operation on.
Select operation
Inputs should be referred to as {{inputname}}.
Camelcase is not supported.
◦Create record: Requires values for fields in
the new record.
◦Delete records: Requires the conditions to
determine which records to delete.
◦Look up records: Requires the conditions
to determine which records to look up,
number of results specified, which fields to
return, the result order, and the result sort
type.
◦Update records: Requires the values for
fields in the updated record and conditions
to determine which records to update.
Execution mode Mode of execution for your selected record
operation:
◦Supervised: Inputs from your human agent
are required during the execution of this
tool while the AI agent runs.
◦Autonomous: Doesn't require any input
from your live agent during the execution of
this tool while the AI agent runs.
Display output Permission to display the output of the
execution in the Now Assist panel or in Virtual
Agent:
◦Yes
◦No
If you want the AI agent to work in Off Glide
architecture with Premium Chat experience,
you must turn-on the Display output toggle.
When the toggle is turned-on, you can add
widgets that can be used in assistants built
with Premium Chat experiences. The widget
configuration includes:

<!-- page 86 -->
Fields Description
◦Widget: Defines the display output
to render the content in a better user
experience. You can select the widget from
the drop-down.
◦Require widget transformation: An
additional LLM call is required to transform
the raw tool. If you choose to skip this
transformation step, the tool output will be
directly mapped to the widget.
▪Yes
▪No
◦Display refined widget message: Refines
the widget message when configured.
▪Yes
▪No
Note: The display output as a
toggle is exclusively available for the
Premium Chat experience when the
Off Glide Conversation Server plugin
(com.glide.cs.offglide) is installed. If the
plugin is not installed, you will continue
to access the standard display output
options.
Advanced settings
Select an output transformation format Style for the LLM to present the results as
it passes information between tools and to
other agents. Out transformation formats:
◦None
◦Concise
◦Paragraph
◦Summary
◦Custom
Write processing messages for users Message to display to users during tool
execution.
◦In-progress message: Write an in-progress
message to be displayed to end-users
while the tool is running.
◦Completion message: Write a completion
message to be displayed to end-users
once the tool finishes running.
5. Select Add.
A record operation is added in the Record operations list on the Add tools and information
page.

<!-- page 87 -->
Add a script to an AI agent
Create a script to add it to an AI agent in AI Agent Studio. With scripts, you can use the scriptable
APIs and back-end integration to support the AI agent.
Before you begin
Role required: sn_aia.admin
Procedure
1.Navigate to All > AI Agent Studio > Create and manage > AI agents.
2. Open the AI agent that you want to add a script to and navigate to the Add tools and
information section.
3. In the Add tool drop-down list, select Script.
4.On the form, fill in the fields.
Add a script form
Fields Description
Select a type of record operation to add If you select An existing one, you can select
a record operation tool used by the current
AI agent or any other AI agent. You can make
changes to the settings of that tool to fit the
needs of your specific AI agent.
Name
Name that you want to specify for your script.
Description Description of the script and what it's going to
do to assist your AI agent.
Note: This description is sent to the large
language model (LLM).
Script inputs Input name and description to use in the
script. The LLM uses the name and description
to determine what value should be used at
runtime.
Example: Input name is
task_record_sys_id and description is
sys_id of the Task Record, this
is mandatory.
Script JavaScript code that includes an object class or
a function for your script.
Note: For improved security, use
GlideRecordSecure instead of
GlideRecord and addUserEncodedQuery()
instead of addEncodedQuery().
Execution mode Mode of execution for your script:

<!-- page 88 -->
Fields Description
◦Supervised: Inputs from your human agent
are required during the execution of this tool
while the AI agent runs.
◦Autonomous: Doesn't require any input from
your live agent during the execution of this
tool while the AI agent runs.
Display output Permission to display the output of the tool
execution in the Now Assist panel or in Virtual
Agent:
◦Yes
◦No
If you want the AI agent to work in Off Glide
architecture with Premium Chat experience,
you must turn-on the Display output toggle.
When the toggle is turned-on, you can add
widgets that can be used in assistants built
with Premium Chat experiences. The widget
configuration includes:
◦Widget: Defines the display output to render
the content in a better user experience. You
can select the widget from the drop-down.
◦Require widget transformation: An
additional LLM call is required to transform
the raw tool. If you choose to skip this
transformation step, the tool output will be
directly mapped to the widget.
▪Yes
▪No
◦Display refined widget message: Refines the
widget message when configured.
▪Yes
▪No
Note: The display output as a
toggle is exclusively available for the
Premium Chat experience when the
Off Glide Conversation Server plugin
(com.glide.cs.offglide) is installed. If the
plugin is not installed, you will continue
to access the standard display output
options.
Advanced settings
Select an output transformation format Style for the LLM to present the results as it
passes information between tools and to other
agents. Out transformation formats:
◦None
◦Concise

<!-- page 89 -->
Fields Description
◦Paragraph
◦Summary
◦Custom
Write processing messages for users Message to display to users during tool
execution.
◦In-progress message: Write an in-progress
message to be displayed to end-users while
the tool is running.
◦Completion message: Write a completion
message to be displayed to end-users once
the tool finishes running.
5. Select Add.
A script tool is added in the Scripts section on the Add tools and information page.
Add a search retrieval to an AI agent
Add a search retrieval to an AI agent in AI Agent Studio. Leveraging the Retrieval-Augmented
Generation (RAG) enables an AI agent to retrieve and incorporate relevant information from an
external source.
Before you begin
Role required: sn_aia.admin
Procedure
1.Navigate to All > AI Agent Studio > Create and manage > AI agents.
2. Open the AI agent that you want to add a search retrieval to and navigate to the Add tools and
information section.
3. In the Add tool drop-down list, select Search retrieval.
4.On the form, fill in the fields.
Add search retrieval form
Fields Description
Select a type of record operation to add If you select An existing one, you can select
a record operation tool used by the current
AI agent or any other AI agent. You can make
changes to the settings of that tool to fit the
needs of your specific AI agent.
Name
Name that you want to specify for your search
retrieval tool.
Description Description of the search retrieval tool and
what it's going to do to assist your AI agent.
Note: This description is sent to the
large language model (LLM).

<!-- page 90 -->
Fields Description
Search profile
Name of the search profile that you want to
add to your RAG-based tool from the list. To
learn more about a search profile, see Search
profiles in AI Search .
Search sources One or multiple sources that you want to add
to your search profile. To learn more about
the search sources, see Search profiles in AI
Search .
Fields returned One or multiple fields that you want your
search profile to return from the search
sources.
Results limit Number of records to be retrieved from the
defined search source. The default value is
10.
Search criteria Type of search that needs to be used:
◦Semantic: This search is carried out with
the logical meaning of the search query.
◦Keyword: This search is carried out with
the defined keywords.
◦Hybrid: This search is a combination of
both keyword and semantic searches.
Semantic indexes Fields on the source table that are indexed
for a semantic search.
Note: Semantic indexed fields are
required if the search criteria are
semantic or hybrid.
Document matching threshold Cosine similarity score between 0 and 1
(exclusive). Default value is 0. The higher the
number, the more variation in search results.
Execution mode Mode of execution for your search retrieval
tool:
◦Supervised: Inputs from your human agent
are required during the execution of this
tool while the AI agent runs.
◦Autonomous: Doesn't require any input
from your live agent during the execution of
this tool while the AI agent runs.
Display output Permission to display the output of the tool
execution in the Now Assist panel or in Virtual
Agent:
◦Yes
◦No

<!-- page 91 -->
Fields Description
If you want the AI agent to work in Off Glide
architecture with Premium Chat experience,
you must turn-on the Display output toggle.
When the toggle is turned-on, you can add
widgets that can be used in assistants built
with Premium Chat experiences. The widget
configuration includes:
◦Widget: Defines the display output
to render the content in a better user
experience. You can select the widget from
the drop-down.
◦Require widget transformation: An
additional LLM call is required to transform
the raw tool. If you choose to skip this
transformation step, the tool output will be
directly mapped to the widget.
▪Yes
▪No
◦Display refined widget message: Refines
the widget message when configured.
▪Yes
▪No
Note: The display output as a
toggle is exclusively available for the
Premium Chat experience when the
Off Glide Conversation Server plugin
(com.glide.cs.offglide) is installed. If the
plugin is not installed, you will continue
to access the standard display output
options.
Advanced settings
Select an output transformation format Style for the LLM to present the results as
it passes information between tools and to
other agents. Out transformation formats:
◦None
◦Concise
◦Paragraph
◦Summary
◦Custom
Write processing messages for users Message to display to users during tool
execution.

<!-- page 92 -->
Fields Description
◦In-progress message: Write an in-progress
message to be displayed to end-users
while the tool is running.
◦Completion message: Write a completion
message to be displayed to end-users
once the tool finishes running.
5. Select Add.
A search retrieval tool is added in the Search retrievals section on the Add tools and
information page.
Add a subflow to an AI agent
Add a subflow to an AI agent in AI Agent Studio. Subflows are reusable sequences of processing
steps that can be called from within a flow.
Before you begin
When an AI agent uses a subflow tool, the user the AI agent is running as must pass the ACL of
the subflow. Ensure that the security configurations for the subflow are met by the AI agent and
agentic workflow. For more information, see Security for AI agents.
Role required: sn_aia.admin
Procedure
1.Navigate to All > AI Agent Studio > Create and manage > AI agents.
2. Open the AI agent that you want to add a subflow to and navigate to the Add tools and
information section.
3. In the Add tool drop-down list, select Subflow.
4.On the form, fill in the fields.
Add a subflow form
Fields Description
Name Name that you want to specify for your
selected subflow.
Description Description of the subflow and what it’s going
to do to assist your AI agent.
Note: This description is sent to the
large language model (LLM).
Select subflow Existing process automation capability you
want to add.
If there is a tool used by an AI agent for
the same subflow, the rest of the form will
populate the fields based on the other tool.
You can make any changes specific to the
current AI agent to suit your needs, and it will
not affect the tool of the existing AI agent.

<!-- page 93 -->
Fields Description
Inputs Subflow inputs. The values are filled in by the
LLM at runtime unless you specify a value
override.
Note: If the agent uses multiple tools,
you can choose to use another tool's
output as an input value override. Select
the data picker icon ( ) to review the
available options.
Execution mode Mode of execution for your selected subflow:
◦Supervised: Inputs from your human agent
are required during the execution of this
tool while the AI agent runs.
◦Autonomous: Doesn't require any input
from your live agent during the execution of
this tool while the AI agent runs.
Display output Permission to display the output of the
execution in the Now Assist panel or in Virtual
Agent:
◦Yes
◦No
If you want the AI agent to work in Off Glide
architecture with Premium Chat experience,
you must turn-on the Display output toggle.
When the toggle is turned-on, you can add
widgets that can be used in assistants built
with Premium Chat experiences. The widget
configuration includes:
◦Widget: Defines the display output
to render the content in a better user
experience. You can select the widget from
the drop-down.
◦Require widget transformation: An
additional LLM call is required to transform
the raw tool. If you choose to skip this
transformation step, the tool output will be
directly mapped to the widget.
▪Yes
▪No
◦Display refined widget message: Refines
the widget message when configured.
▪Yes
▪No

<!-- page 94 -->
Fields Description
Note: The display output as a
toggle is exclusively available for the
Premium Chat experience when the
Off Glide Conversation Server plugin
(com.glide.cs.offglide) is installed. If the
plugin is not installed, you will continue
to access the standard display output
options.
Advanced settings
Select an output transformation format Style for the LLM to present the results as
it passes information between tools and to
other agents. Out transformation formats:
◦None
◦Concise
◦Paragraph
◦Summary
◦Custom
Write processing messages for users Message to display to users during tool
execution.
◦In-progress message: Write an in-progress
message to be displayed to end-users
while the tool is running.
◦Completion message: Write a completion
message to be displayed to end-users
once the tool finishes running.
5. Select Add.
A subflow tool is added in the Subflows section on the Add tools and information page.
Add a web search to an AI agent
Add a web search to an AI agent in AI Agent Studio using a third-party search API such as
Microsoft Bing or Google.
Before you begin
Note: If you select Google as your web search tool provider, the web search tool leverages
Grounding with Google Search , offered under a Global Standard deployment. Because
grounding is not data resident , Google's global infrastructure routes traffic to a global
data center for each web search request. This processing may be different than your
data processing location chosen for your ServiceNow instance. Please consider your
organization's data policies before adding a web search tool with Google as the provider.
Role required: sn_aia.admin

<!-- page 95 -->
Procedure
1.Navigate to All > AI Agent Studio > Create and manage > AI agents.
2. Open the AI agent that you want to add a web search to and navigate to the Add tools and
information section.
3. In the Add tool drop-down list, select Web search.
4.On the form, fill in the fields.
Add a web search
Fields Description
Name
Name that you want to specify for your web
search.
Resource Resource for the web search.
Provider Third-party search API provider.
Note: You can configure the
default provider for the Web
Search API capability on the
OneExtend Definition Config table
[sys_one_extend_definition_config].
Inputs Information for the search API to include
in the web search. You can select value
overrides or leave them blank for generative
AI to fill in the details for you.
◦Country: Country where results come from.
◦Max tokens: Maximum number of tokens to
include in the response.
◦Number of results: Total number of results
acquired.
◦Search query: Value to search for
◦Sites or domains: Websites where you
want to search.
Note: If the agent uses multiple tools,
you can choose to use another tool's
output as an input value override. Select
the data picker icon ( ) to review the
available options.
Execution mode Mode of execution for your selected web
search:

<!-- page 96 -->
Fields Description
◦Supervised: Inputs from your human agent
are required during the execution of this
tool while the AI agent runs.
◦Autonomous: Doesn't require any input
from your live agent during the execution of
this tool while the AI agent runs.
Display output Permission to display the output of the
execution in the Now Assist panel or in Virtual
Agent:
◦Yes
◦No
If you want the AI agent to work in Off Glide
architecture with Premium Chat experience,
you must turn-on the Display output toggle.
When the toggle is turned-on, you can add
widgets that can be used in assistants built
with Premium Chat experiences. The widget
configuration includes:
◦Widget: Defines the display output
to render the content in a better user
experience. You can select the widget from
the drop-down.
◦Require widget transformation: An
additional LLM call is required to transform
the raw tool. If you choose to skip this
transformation step, the tool output will be
directly mapped to the widget.
▪Yes
▪No
◦Display refined widget message: Refines
the widget message when configured.
▪Yes
▪No
Note: The display output as a
toggle is exclusively available for the
Premium Chat experience when the
Off Glide Conversation Server plugin
(com.glide.cs.offglide) is installed. If the
plugin is not installed, you will continue
to access the standard display output
options.
Advanced settings
Select an output transformation format Style for the LLM to present the results as
it passes information between tools and to
other agents. Out transformation formats:

<!-- page 97 -->
Fields Description
◦None
◦Concise
◦Paragraph
◦Summary
◦Custom
Write processing messages for users Message to display to users during tool
execution.
◦In-progress message: Write an in-progress
message to be displayed to end-users
while the tool is running.
◦Completion message: Write a completion
message to be displayed to end-users
once the tool finishes running.
5. Select Add.
A web search is added in the Web search list on the Add tools and information page.
Define security controls for an AI agent
In the guided setup for an AI agent, define security controls for who can access the AI agent and
what data the AI agent has access to.
Before you begin
Role required: sn_aia.admin
About this task
The Define security controls step is divided into two parts: Define user access and Define data
access. The former creates an ACL that determines who can discover or invoke the AI agent. The
latter defines the data that the AI agent has access to once it’s invoked.
See Security for AI agents for more information about creating ACLs and user identities for
security for AI agent.
Procedure
1.Select which users can access the AI agent.
The drop-down menu options are:
◦Users with specified roles
◦Authenticated users
◦Public
If you select Users with specified roles, you can select exactly which roles can
access the AI agent.
AI agents installed with Now Assist applications each require specific roles. To learn which
roles they need, consult the documentation for the AI agent or the agentic workflow that uses
the AI agent.
2. Select Save and continue to move to the next step.

<!-- page 98 -->
Saving and moving onto the next step triggers the creation of an ACL for your AI agent. If you
want to make changes later, you can return to the guided setup and change the options here. If
you have the correct elevated role, you can also make edits directly on the ACL table.
3. Define the user identity of the AI agent to determine what data it has access to.
The two options are Dynamic user and AI user. The dynamic user is the user invoking
the AI agent or the dynamic user of the agentic workflow calling on the AI agent. An AI user is
a dedicated user that has its own specified roles that allow access, which could be more than
the dynamic user.
If you do not have an AI user but want to use the AI user identity, you need to create a new
record on the User table. See Create a user . Select AI user as the identity type.
If you select Dynamic user, you can select the Approved roles that the AI agent runs
with. By default, an AI agent runs as a dynamic user and has the roles of the invoking user.
Select the approved roles to limit the data access that an AI agent could have. Role masking
must be applied for all AI agents and agentic workflows to run as dynamic users.
To override the role masking requirement for a specific agentic workflow or AI agent, admins
with the correct elevated access can create an approved list of roles for a given agentic
workflow or AI agent. Then, they can access that role masking record in the Agent Access Role
Configurations table [sys_agent_access_role_configuration], and select the “allow all roles”
check box. Taking these steps deactivates the requirement for a role masking approved roles
list in AI Agent Studio, so the AI admin can return to AI Agent Studio and continue to configure
the agentic workflow or AI agent without role masking applied.
Note: Role masking should be applied as security best practice and adherence to the
principle of least privilege. Overriding the role masking requirement isn’t recommended.

<!-- page 99 -->
If you select AI user, the list of roles that the AI user has is displayed.
Result
You have created an ACL that determines who can discover and access your AI agent, and you
have assigned a user identity (and role masking, if relevant) to the AI agent to determine what
data it can access.
What to do next
Select Save and continue to move to the next step, Adding a trigger. Adding a trigger is optional.
You can also skip to the final step, Select channels and access.
Add a trigger to an AI agent
In the guided setup for an AI agent, add triggers to run the AI agent automatically when certain
conditions are met.
Before you begin
Role required: sn_aia.admin
About this task
Adding a trigger is optional. If you want your AI agent to be used only in chats, you don't need
to add a trigger. Only add a trigger if you want to invoke the AI agent automatically when some
event occurs.
Note: Triggers contain instance-specific information. If you are moving AI agents or
agentic workflows between instances using Update Sets, you must set the triggers to
inactive before adding them to the update sets and then activate them on the new instance.
If you don't want to add a trigger, skip to the final step, Select channels and access.
Procedure
1.Select Add trigger.
2. On the form, fill in the fields.
Create a new trigger
Fields Description
Select trigger List of triggers that are available in the
instance.
Name Name of the trigger.

<!-- page 100 -->
Fields Description
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
in the execution of your AI agent. Try testing
the AI agent execution and user access. To
review overall trends over many executions,
try an automated evaluation.

<!-- page 101 -->
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

<!-- page 102 -->
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
You have added triggers to your AI agent to run it automatically under the specified conditions.
What to do next
Select Save and continue to move to the final step, Select channels and access.
Kill Switch in Now Assist AI Agents
The kill switch feature detects and stops runaway AI agent triggers that execute repeatedly
against the same records, preventing unnecessary consumption of Now Assist interactions.
Kill Switch Overview
An AI agent trigger can match the same record multiple times within a short period during
executions. When left unchecked, a misconfiguration trigger condition can process the same
incident five or more times per day, across dozens of records, for several consecutive days. Each
trigger activation spawns a conversation and consumes assists, resulting in charges for activity
that provides no customer value.
The kill switch feature detects when the same record is triggering the same agent objective
beyond a threshold in a single day and automatically disables the agent. It monitors trigger

<!-- page 103 -->
activity, issues tiered alert notifications to trigger and agent owners, and optionally disables the
trigger automatically after a configurable breach threshold is reached.
Default detection thresholds
The kill switch evaluates trigger activity against the following default thresholds. All thresholds
are configurable by users through system properties:
•Fires per record per 24-hour window: 5
•Distinct records breaching the threshold: 25
•Consecutive days of breach before action: 3
Five tunable system properties control these thresholds and the feature's operating mode:
•kill_switch.mode: Default value: warn_only. For the different operating modes the
property contains, see Operating modes.
•kill_switch.max_fires_per_window: Fires per record that mark it as breaching.
Default value: 5.
•kill_switch.min_distinct_records: Breaching records needed for the window to
count as runaway. Default value: 25.
•kill_switch.window_size: Length of one observation window. Default value: 1440
min / 24h.
•kill_switch.consecutive_windows_duration: The total look back span. Default
value: 4320 min / 3 days.
Architecture
The kill switch uses two fully decoupled execution paths.
Trigger activation path
Runs on every conversation start. When a trigger matches a record and fires, an
audit row is written to the audit table before the conversation begins. Audit writes
never interrupt or fail the user's conversation.
Evaluator path
A scheduled job runs once daily. It reads the audit table, computes a cycleStart
date, and assigns each active trigger a stage value (K) from 0 to 3 based on the
number of consecutive days the trigger has breached the threshold. If K is 1 or
higher, the evaluator sends a warning email. If K reaches 3 and enforce mode is
active, the evaluator also disables the trigger.
Note:
•Warning emails are sent to the trigger creator and to the creators of any agents or
workflows associated with the trigger. Alerts follow the same notification mechanism used
for all existing Now Assist alert purposes.
•Re-enabling an inactive trigger resets the cycle, so the next evaluator run treats the
trigger as a fresh Day 1.
Operating modes
The kill_switch.mode system property controls how the feature responds to a detected
breach.
off

<!-- page 104 -->
Audit rows are still written, but the evaluator performs no detection, sends no
warnings, and never disables triggers.
warn_only
The evaluator sends a daily warning email for each day the breach pattern is
present. Triggers are never inactive. This is the shipped default.
enforce
The evaluator sends the same tiered warnings on Days 1 and 2. On Day 3, it sends a
final warning and deactivates the trigger configuration, including associated many-
to-many and override rows.
Escalation sequence
In warn_only or enforce mode, the evaluator sends progressively stronger email
notifications as the breach continues.
•Day 1 — Early warning: [1 of 3] Action Recommended — Trigger Firing at Unusual Rate
•Day 2 — Stronger warning: [2 of 3] Action Required — Trigger Has Been Firing at High Volume
for 2 Consecutive Days
•Day 3 — Final warning (enforce mode also disables): [3 of 3] Trigger inactive — High Volume
Detected for 3 Consecutive Days
Each email includes the agent name, trigger name, affected record count, and a direct link to the
trigger configuration.
Select channels and status for an AI agent
In the guided setup for an AI agent, activate the AI agent to use in an assistant in Now Assist for
Virtual Agent, and set the processing messages.
Before you begin
Role required: sn_aia.admin
About this task
The final step of the AI agent guided setup includes options for where you can invoke the agentic
workflow as well as set the processing message. You must select which assistants for Now Assist
in Virtual Agent you want to be able to invoke the AI agent. Your processing messages appear
when the AI agent is running and when the AI agent's task is completed.
Procedure
1.Select whether you want users to use Now Assist in Virtual Agent to invoke the AI agent.
If enabled, you must select which chat assistants have access to the AI agent. You can edit
assistants using Assistant Designer.
2. Optional: Set the processing and completion messages for your AI agent.
(Optional) You can set a processing message, completion message, or both. If you don't want
to use a specific type of message, unselect the toggle next to the message field.
You can also use Now Assist to generate the messages for you by selecting Generate
messages. You can change the messages after they're generated.

<!-- page 105 -->
3. Activate the AI agent.
Select the This AI agent is active toggle to activate the AI agent only when you want users to
be able to use it. If you want to test your AI agent first, wait until after you have tested it before
activating it. You can return to the guided setup later.
If you don't see this option, you may need to scroll.
Note: If you have installed the Off Glide Conversation Server plugin
(com.glide.cs.offglide) on your ServiceNow AI Agent Studio instance, then agent learning
and voice agents won't work if the assistant is in Premium Chat mode.
4.Select Save and test.
Result
You have completed the guided setup for creating an AI agent. Your new AI agent can be edited
at any time using AI Agent Studio.

<!-- page 106 -->
What to do next
Move to the Testing playground to test an AI agent execution using example utterances or to test
user access.
Duplicate an AI agent
Duplicate an existing AI agent in AI Agent Studio so that you can save time by not having to
manually configure or create AI agents.
Before you begin
Role required: sn_aia.admin
About this task
Duplicate the AI agents to do the following tasks:
•Duplicate the record.
•Disallow any AI agents with existing names.
Custom columns, such as the Tools and Knowledge sources, Status, and a column with the
Duplicate icon ( ) are available for the AI agents list.
Note: The duplicated AI Agents use the same tools as the original agent and modifying
the agent tools in the duplicated AI agent affects the agent tools in the original AI agent. To
use the tools in a duplicated AI agent, you can either use the duplicated agent tools without
making changes to them or add a new tool.”
Procedure
1.Navigate to All > AI Agent Studio > Create and manage > AI agents and open the AI agents list
in AI Agent Studio.
2. Duplicate the AI agent from either the Manage agentic workflows and AI agents page or the AI
agent form.
Current location Navigation option
On the AI agents list, select the duplicate icon
Manage agentic workflows and AI agents
( ) for the AI agent that you would like to du­
page
plicate.
Open the AI agent that you want to duplicate,
select the menu icon ( ) next to Exit on the
AI agent form
Describe and instruct form, and select Dupli­
cate.
You see a confirmation message in a pop-up window.

<!-- page 107 -->
3. Create a copy of the AI agent with the same information from the original AI agent's record by
selecting Duplicate.
Note: The name of the duplicated AI agent is appended with the suffix (Copy) so that
you can clearly identify the duplicated AI agent from the original AI agent. For example,
Knowledge Article Agent (Copy). You can rename the duplicated AI agent
and also edit the other information that is duplicated from the original AI agent.
4.After editing the details in the Describe and instruct section, select Save and continue.
5. In the Add tools and information section, edit the details that are from the original AI agent or
add new tools for your requirements and select Save and continue.
6.In the Toggle display section, turn on the Status for the duplicated AI agent and select Save
and continue.
Result
You’re redirected to the AI Agent Studio home page. In the Manage and configure AI Agents to
solve agentic workflow section on the AI Agents tab, you see the duplicated AI agent.
Modify an AI agent
Modify an AI agent in AI Agent Studio to suit your changing business needs.
Before you begin
Role required: sns_aia.admin
Procedure
1.Navigate to All > AI Agent Studio > Create and manage > AI agents
2. Select the AI agent that you want to modify.
3. Modify the fields of the different sections of the Guided Setup, making changes to the fields for
your requirements.
The guided setup is the same as the one for creating an AI agent:
◦Define the AI agent's specialty.
◦Define the AI agent security controls.

<!-- page 108 -->
◦(Optional) Add a trigger to automatically invoke your AI agent if a specified event occurs..
◦Determine whether you want to use the Now Assist in Virtual Agent chat assistants and/or as
UI action, set the processing messages, and activate your AI agent..
Note: Some fields aren't editable if the agent is associated with a Now Assist
application. If you want to make more modifications, duplicate the agentic workflow and
make changes to the duplicate.
◦For the List of steps field in the Define specialty step, you can create multiple
versions of the same AI agent without losing previous versions. Creating versions enables
you to test different instructions to evaluate performance. See Version control for AI agents
and agentic workflows for more information.
◦For more guidance on creating effective instructions, see the general guidelines for creating
AI agents and agentic workflows.
◦For the access control lists (ACLs), you can edit the security fields and define who can
access the AI agent and edit the entity to run the AI agent as a dynamic user or an AI user.
For more information, see Implement access control in Now Assist AI agents.
You can navigate through the steps of the Guided Setup with the Continue and Back buttons.
4.Navigate to the last step and select Test to save your changes and begin testing your modified
agent.
Result
Your agent is modified and ready to test.
What to do next
You can test an execution of your AI agent manually or test the user access. Once you've
determined that the AI agent has the basic functionality you expect, you can evaluate the AI
agent using automated tests.
Manually test the execution of an AI agent
Analyze the execution of an AI agent so you can see that it functions the way that you defined it.
Before you begin
Role required: sn_aia_admin and either admin or at least one role required by the ACL of the AI
agent being testing and each of the ACLs of its downstream components
About this task
After you create an AI agent, test it to see that it functions the way that you defined it. You can
choose to run a manual test with a single instruction to test its basic functioning, or you can
evaluate the AI agent's performance across multiple executions.
If you want to test multiple executions using execution logs, you can run an automated test. If you
select Start automated evaluation, the agentic evaluation guided setup opens in a new browser
tab. See Evaluate an AI agent for more details about running a new automated evaluation.
When manually testing performance, you can see how the AI agent interacts with the AI Agent
Orchestrator and the Communicator AI agent. The Orchestration is an agent that directs different
AI agents, and the Communicator AI agent facilitates the communication between the user and
other AI agents.

<!-- page 109 -->
Procedure
1.Navigate to All > AI Agent Studio > Testing.
2. Select Start manual test.
If you want to start an automated test, see Evaluate an AI agent for more details on that
process.
3. In the Choose a test type drop-down menu, select AI agent or workflow.
If you want to test user access security controls, see Test AI agent user access.
4.Under Choose a testing mode, select the testing mode either as Premium Chat or
Standard.
Note: The Premium Chat testing mode is exclusively accessible when the Off Glide
Conversation Server plugin (com.glide.cs.offglide) is installed. If the plugin is not installed,
you will continue to access the standard testing playground.
5. Select an agentic workflow or AI agent that you want to test by searching the name of a
workflow or choosing from the drop-down menu.
6.In the Version drop-down list, select the version of the AI agent you want to test.
See Version control for AI agents and agentic workflows for more information about creating
and changing versions.
7.In the Task field, provide a concise summary of the task to be achieved.
Note: In the task summary, include a reference number or specific record for better
results during your testing.
8.Select Continue to Test Chat Response.
Result
When testing an AI agent, you can see the AI agent Orchestrator and Communicator working
together to organize and manage the AI agents like a team. The AI agent Orchestrator assigns
the individual, specialized agents to complete the subtasks. The AI agent Communicator lets the
AI agent Orchestrator know the status of each agent.

<!-- page 110 -->
Note: If you don't have the roles necessary to pass the ACLs of the AI agent and all of
its tools, you’ll be notified that you don't have the necessary access and the test won't
execute.
Your AI agent starts to execute the test autonomously to resolve the task.
Testing an AI agent
•A simulated chat experience begins on the Now Assist panel between your invoking user and
AI agent.
•At the top of the canvas, you can see information about the AI agent you're testing, including
its name, version, and description.
•A diagram shows the tasks and communication of the AI agents that are working together to
solve the case.
•A decision log records the thought process of each AI agent that is involved in solving the
agentic workflow.
Note: You can view the entire decision log by selecting Download logs.
You can restart the entire testing process at any time by selecting Restart.
Test user access to an AI agent
Run a manual test to verify that only the users you want to access the AI agent can do so.
Before you begin
Role required: sn_aia_admin and either admin or at least one role required by the ACL of the AI
agent being testing and each of the ACLs of its downstream components
About this task
You can establish the security settings for an AI agent in the guided setup to establish which
users can access it. See Define security controls for instructions on how to change the user
access settings. When you select Save and continue on that step of the guided setup, an ACL is
created that establishes limitations on which users can access the AI agent.
Once you have created these ACLs, you can verify that they work as intended by using the Test
access test type of a manual test of an AI agent.

<!-- page 111 -->
To see instructions for performing manual tests to evaluate performance, see Test performance
manually. For more information about automated tests, see Evaluate an AI agent.
Procedure
1.Navigate to All > AI Agent Studio > Testing.
2. Select Start manual test.
3. In the Choose a test type drop-down menu, select Test access.
If you want to test the basics of how an AI agent works, select AI agent or worfklow.
The full instructions for that test type can be found in Test performance manually.
4.Search for or select the name of the AI agent you want to test.
5. Select an invoking user.
The invoking user can be the user that triggers the AI agent or it can be the invoking user of
an upstream component, such as an agentic workflow. For more information about how the
invoking user works, see Security for AI agents.
When you select an invoking user, the user roles are populated in the Invoking user
roles field. The field is read-only. If you want to change a user's roles, you must change the
user's User record. See Assign a role to a user .
6.Select Test access.
Result
The results of the access test are opened in the Access Analyzer in a new browser tab.
Access Analyzer identifies all the ACL calls made in the execution of the AI agent, including its
tools, if any are present. You can see the results of each ACL to verify that each one has the
correct user access defined.
What to do next
If the results are different than what you expect or want, you can redefine the security controls of
the AI agent.
You can also test an AI agent's performance with either a manual test or automated evaluations.
See Test performance manually or Evaluate an AI agent.

<!-- page 112 -->
Delete an AI agent
Delete an AI agent from AI Agent Studio if you no longer need it.
Before you begin
Role required: sn_aia_admin
About this task
You must assign appropriate permissions by using the access control lists (ACLs) to delete AI
agents on AI Agent Studio.
Note: You can't delete the AI agents that come installed with Now Assist applications.
Procedure
1.Navigate to All > AI Agent Studio > Create and manage > AI agents.
2. Select the check box of the AI agent that you want to delete and select Delete.
You can also delete multiple AI agents by selecting multiple AI agent records at a time.
Note: Some AI agents installed with Now Assist applications can't be deleted.
3. In the confirmation pop-up window, select Delete.
Result
The selected AI agents are deleted from the AI agents list in AI Agent Studio.
Create an external AI agent
Create external AI agents in AI Agent Studio to connect the ServiceNow AI Platform with third-
party agentic AI providers as primary agents.
Integrating external AI agents
Integrate and configure external agents with the ServiceNow agentic AI system using
Agent2Agent (A2A) protocol integration to use in agentic workflows created in the AI Agent
Studio.
External agent discovery on the ServiceNow AI Platform
You can enable external AI agents on the AI Agent Studio via the Settings
page. Navigate to AI Agent Studio > Settings > External AI agents >
Discoverability.

<!-- page 113 -->
•Allow ServiceNow to access External AI agents: Turn on the toggle to enable external AI
agents integration with the ServiceNow agentic AI system using the A2A protocol.
•Allow third-party to access ServiceNow AI agents: Turn on the toggle to enables integrating
ServiceNow AI agents into external agentic AI systems.
When creating a new external AI agent in AI Agent Studio, you can connect your agent to the
ServiceNow agentic AI system using the Agent2Agent (A2A) protocol integration. To do this, you
must have a Connection & Credential alias record that connects to your agentic AI provider.
After connecting to the external AI agent, you can add details about its role and instructions to
provide context for the AI Agent Orchestrator. Additional context helps differentiate your AI agent
from other AI agents so that the AI Agent Orchestrator can decide about which agent to use.
Contextual data access for external agents on the ServiceNow AI Platform
Enable contextual data access for external agents to improve AI agent response during
execution.
•Short-term memory: Turn on the toggle to enable external AI agents remember your
preferences or facts from the current interaction only.
•Long-term memory: Turn on the toggle to enable external AI agents remember your
preferences or facts from previous interaction.
•Knowledge graph for external AI agent interactions: Turn on the toggle to enable external AI
agents to use structured and unstructured data from different records across the ServiceNow
AI Platform.
Agent2Agent protocol overview
Agent2Agent (A2A) is an open standard that enables AI agents across different platforms to
communicate with each other. The standard relies on every AI agent having an Agent Card
associated with it that provides basic information for providers like the ServiceNow AI Platform,
Azure, and Google to use them.
Version 0.3 of A2A is supported.
An AI agent's Agent Card uses standardized JSON to help different providers understand its
capabilities. The Agent Card is accessed by a specific type of endpoint from a provider's server.
Execution plans are communicated through an execution endpoint so that both the provider's
server and the ServiceNow AI Platform can track what the external AI agent is doing.

<!-- page 114 -->
See Create an external AI agent with the Agent2Agent protocol for instructions for using this
protocol to create an AI agent.
Configuring A2A authentication
A2A connections require authorization from the source platform to execute on the ServiceNow
AI Platform. Authentication is established by creating two Connection & Credential Alias and
Connection records, one with an Agent Card endpoint and one with an execution endpoint.
Configuration Properties
The following properties configure different aspects of how your agents can interact with the
ServiceNow AI Platform.
External AI agent properties
Name Description
sn_aia.external_agents.enabled Set to true to enable external agent
features
sn_aia.external_agents.parallel_conversations.enabled Enables or disables multiple
simultaneous conversations per user
ServiceNow AI agents as secondary agents
Integrate ServiceNow AI agents into other agentic AI systems, such as Google Cloud or Azure
OpenAI.
Enabling discovery of ServiceNow mobile agents
In AI Agent Studio, on the Settings page, under External AI Agents > Discoverability, you can
enable the discovery of ServiceNow AI agents to use on other AI platforms. To do so, toggle
Allow third party to access ServiceNow AI Agents.
You can also choose between Synchronous and Asynchronous communication between your
external AI agent and the agentic AI provider.

<!-- page 115 -->
ServiceNow AI agents as secondary agents overview
You can connect your ServiceNow agent to other agentic AI model providers using the
Agent2Agent protocol.
After creating your AI agent in AI Agent Studio, you can direct to the Agent Card URL that is
displayed for secondary agents for easy access so the admins can view, copy, and consume the
URL.
The endpoint to direct to the actual execution of the AI agent is in the format
{{instance}}.service-now.com/api/sn_aia/a2a/v2/agent/id/{{agent-
id}}.
You can use the same OAuth or API key for authenticating the agent discovery and the agent
execution.
To verify that your AI agent is running from the ServiceNow side, during a conversation with the AI
agent, you can go to the Execution Plan [sn_aia_execution_plan] table. From the
Execution Plan table, you can identify the execution plan based on the Objective field that
contains the prompt from the conversation on the other platform.
For more information about sample payloads for Google A2A with ServiceNow AI agent as
Secondary agent, see Sample payloads for Google A2A .
For more information about setting up instructions for your ServiceNow AI agents as secondary
agents (acting as A2A server), refer to Authentication for Google A2A - ServiceNow as Secondary
Agent .
Asynchronous connection
Asynchronous connection involves communication where the sender and receiver don't have to
be active simultaneously unlike the synchronous communication mode.
To establish asynchronous connection, you must obtain a callback URL for push notifications to
function.
Once you have obtained a callback URL, you must create a record on the External Agent
Callback Registries [sn_aia_external_agent_callback_registry] table. Go to the table, select New,
and enter the callback URL. Save the record.
Once you save the record, a Connection & Credential Alias [sys_alias] record is created for you.
To add authentication, you can open the Connection record associated with the sys_alias record
and add a credential to the Credential field.
When the record is created, you can go back to the External Agent Callback Registry record you
created and select Verify URL to test the connection works as expected.
Create an external AI agent with the Agent2Agent protocol
Create external AI agents in AI Agent Studio to connect the ServiceNow AI Platform with third-
party agentic AI providers.
Before you begin
If you don’t see the option to create an external agent, confirm that your administrator has
selected Allow ServiceNow to access External AI Agents. This option is available on the
Settings page in AI Agent Studio, under External AI Agents > Discoverability.
Your instance must be at least on Zurich patch 4.
Role required: sn_aia.admin

<!-- page 116 -->
About this task
You can integrate third-party AI providers into the ServiceNow AI Platform by creating an external
AI agent in AI Agent Studio.
Procedure
1.Navigate to All > AI Agent Studio > Create and manage > AI agents.
2. Select New > External.
3. In the Discover and activate step, select the AI agent provider for your external agent and
discover your agent.
Select Save and continue to navigate to the next step.
a.Select an existing provider or add a provider.
If you select Add new provider, you must fill out the fields and then select Save.
Add provider form fields
Name Description
Name Name of the agentic AI provider.
Agent card URL The URL that points to the external AI agent's Agent Card. The
URL should include well_known/agent_json.
Under Advanced Credentials to access your external AI agent's Agent Card. You
settings, Connection & can select an existing alias or create one.
Credential alias
Under Advanced Subflow that establishes Agent2Agent protocol. The default
settings, Select subflow subflow should handle the majority of cases, but you can also
create your own.
b.Select Discover external AI agent to validate the connection to your external agent.
If discovery is successful, the name of your agent and the version number are added to the
page previous the Discover external AI agent button.

<!-- page 117 -->
c.Select the name of the agent to verify that the Name, Version, Description, and
Skills fields are populated correctly, then select Selected.
The Agent card tab shows the entire JSON for the agent.
4.In the Review skills and capabilities step, verify that the skill names are correct.
5. In the Define the specialty step, add details for how the external agent fits in the ServiceNow
agentic system.
a.Review your AI agent description.
You can leave your AI agent description as it is, or you can add a longer description to help
differentiate the agent from other AI agents. This helps enable the AI Agent Orchestrator to
use your external AI agent more effectively. For suggestions for writing AI agent descriptions,
see General guidelines for creating AI agents and agentic workflows.
b.Set your communication mode to either Synchronous or Asynchronous.

<!-- page 118 -->
Some agents don’t support asynchronous communication.
Under Advanced settings, you can use the default subflow, an existing subflow, or create a
subflow. The default subflow should work for the majority of cases.
c.Select your AI agent's execution Connection & Credential alias for authentication.
Choose which credentials access your external AI agent's execution endpoint. You can
select an existing alias or create one. If you create one, a modal fdisplays with options for
configuring an OAuth or API Key authentication.
Note: For more information about the API Key credential, see A2A API Key credential
behavior.
d. Configure access control lists (ACLs) for the AI agent.
Note: The ACLs determine who has access to discover and execute the AI agent.
To learn more about the ACLs you can create in AI Agent Studio and how to add more
advanced security configurations, see Implement access control in Now Assist AI
agents.
This is a required step. If you have previously configured an AI agent without creating an
ACL, you must generate an ACL before you can make other modifications.
Define who can access the AI agent
Field Description
User access The type of users whose access for the AI
agent is defined by the following options:
▪Any authenticated user: Any user who is
logged in can access the AI agent.
▪Users with specific roles: Users that have
at least one of the roles assigned to them
can access the AI agent. This option is the
default.

<!-- page 119 -->
Field Description
Note: If a user doesn't have access
to an AI agent or if the user doesn't
have access to at least one of the
AI agents in the respective agentic
workflow execution, then the whole
execution aborts before the first AI
agent is initiated.
▪Public: Any user can access the AI agent
even without logging in. Use this option
only when you want guests to be able to
access the AI agent.
Role Assign one or more specific roles from the
drop-down menu.
Note: Selecting the role is possible
only when you chose the Users with
specific roles user access.
6.In the Select a display step, choose where you want the AI agent to appear and what message
users see when the AI agent is running.
a.Select your AI agent's availability.
Set the Status to active if you want the AI agent to be available to users with the correct
role.
b.Select a display channel.
You can choose to use a Virtual Agent and specify which assistant you want to access the AI
agent. If you want to test the AI agent first, you don’t need to select a display channel yet.
c.Choose processing messages to display to the user when the AI agent is executing.
For example, Initiating AI agent or Processing record details, or An AI
agent is looking into the request.
d. Activate the AI agent.
Select the toggle to activate the AI agent if you want the AI agent to be discoverable. If you
want to test your AI agent first, wait until after you have tested it before activating it.
If you don't see this option, you may need to scroll.

<!-- page 120 -->
7.Select Save and test to save the AI agent details and go to the Testing page of AI Agent Studio.
Result
Your external AI agent is connected to ServiceNow.
What to do next
You can test an execution of your AI agent or its data access. You can also add it to a new or
existing agentic workflow. See Create an agentic workflow for the steps to create or configure an
agentic workflow.
A2A API Key credential behavior
Starting in Now Assist AI Agents 7.1.x, the header included in each A2A request is driven by the
API Key credential record and it is not injected automatically by the flow action.
Starting in Now Assist AI Agents 7.1.x, A2A flow actions no longer inject an Authorization:
Bearer header automatically. The header included in each request is now driven entirely by the
API Key credential record bound to the external agent's Connection & Credential Alias.
OAuth-based external agents, and API Key endpoints whose existing credential record already
aligns with the endpoint's expectations, are unaffected. You only need to act if your remote A2A
endpoint requires a specific header name or a scheme prefix.
Resolve 401 or 403 errors after upgrade
If your A2A endpoint returns a 401 or 403 after upgrading, update the API Key credential record
bound to your external agent.
1.Open the api_key_credentials record bound to your A2A external agent. Navigate to
the record via the Connection & Credential Alias on the external-agent provider.
2. If the endpoint requires a specific header name (for example, x-api-key instead of
Authorization), set the API Key Header (api_key_header_name) field to the header
name the endpoint expects.

> **[Screenshot: Define the specialty — New AI Agent guided setup wizard]**
> Full-width screenshot of the AI Agent Studio guided setup for a new AI agent (type: Chat). Two warning banners at top (third-party data routing notice and Premium Chat notice). Navigation tab bar: Overview, Create and manage, Testing, Activity, Settings. An "Exit" button top-right.
>
> Left sidebar stepper shows seven steps: 1) Define the specialty (filled/active), 2) Add tools and information (empty circle), 3) Define security controls (expanded showing "Define user access" and "Define data access"), 4) Add triggers (empty), 5) Select channels and status (empty). All steps below current are empty circles.
>
> Main content area titled "Define the specialty". Instruction text: "Using clear, precise language, write the name, description, role, and list of steps this AI agent completes." A "Generate details" teal button and "View writing guidelines" link.
>
> Four form sections: "Give it a unique name and description" — "AI agent name *" field with placeholder "For example, Categorize ITSM Incident AI agent"; "AI agent description * ⓘ" with "Description for LLM" link, a multi-line text area containing sample description "Categorize ITSM Incident AI agent assigns appropriate category, subcategory and configuration item ICD to an incident." Character count: 2000.
>
> "Define the role and required steps" — "View versions ∧" link. "AI agent role * ⓘ" with "Instruction for LLM" link; text area with "You're an expert in analyzing Incidents and are tasked with assigning appropriate category, subcategory and configuration item ICS." Character count: 2000. "List of steps ⓘ" with "Instruction for LLM" link; text area showing "1.a Fetch the details of the given incident…"
>
> "Unsupported model providers" — "List any model providers that this AI agent does not support." LLM providers field with "Select unsupported LLMs" placeholder.
>
> Two toggle rows: "Allow third party to access this AI agent (RP)" – Off toggle; "Allow AI specialists to access this AI agent (RP)" – Off toggle.
>
> "Manage long-term memory" — "Specify categories for memories about user details." Categories field: "Select Categories". "Allow this AI agent to learn from past executions: No" toggle.
>
> Bottom-right: "Save and continue" button.

> **[Screenshot: Knowledge graph configuration in Add tools and information step]**
> A knowledge graph configuration card within the AI agent setup. Card header: "Knowledge graph | AI Instruction" with description "An AI agent uses a knowledge graph to understand the relationships between real-world entities to improve its outputs." Table with columns: Name, Execution mode, Display output, Description, Date added, Remove. One row: "Approval User Knowledge Graph" | Autonomous | false | "This tool is designed to retrieve specific requestor details required for approval evaluation and decision-making, such as department, location, company, assets, or other attributes." | 2025-07-14 | trash icon.

> **[Screenshot: Add tool dropdown menu showing all available tool types]**
> A dropdown list triggered by "Add tool ▾" button. The list shows tool type options in a vertical menu: Catalog item, Conversational topic, Desktop action (highlighted/selected), File upload, Flow action (with expand arrow ∨), Knowledge graph (with arrow and "d tools?" partial label), MCP server tool, Now Assist skill, Record operation, Script, Search retrieval (partially visible). A "Build their own bui... ∨" option also visible.
>
> **[Screenshot: Add a desktop action — Existing vs New desktop action choice panel]**
> A two-column reference panel showing two paths: Left column "Existing desktop action" — "a. Select an existing desktop action of type on-screen task or background task from the Select a desktop action drop-down list." Then "The background task desktop actions are supported for the following applications:" with a bulleted list: Microsoft Excel, Microsoft Outlook, Microsoft Word, PDF, PowerShell Connector. Right column "New desktop action" — "a. On the Add a desktop action modal, select the Click here to create a desktop action link." A modal screenshot shows "Add a desktop action" dialog with "Select a desktop action *" dropdown and "Can't find what you are looking for? Click here to create a desktop action" link, then "Cancel" and "Continue" buttons.

> **[Screenshot: Define user access step — ACL configuration in AI agent guided setup]**
> The guided setup for "Approval Assistance Agent (Chat)" is shown on the "Define user access" sub-step under "Define security controls". Left sidebar stepper shows: Define the specialty (filled), Add tools and information (filled), Define security controls (expanded: Define user access (half-filled/active), Define data access (empty)), Add triggers (empty), Select channels and status (empty). Main content area title: "Define user access". Instruction: "Define which users can access and interact with this AI agent. Once you save your choices, an access control list (ACL) will be automatically generated." Sub-title: "Define who can access this AI agent (ACLs)". A table with columns: Decision type, Roles, User authenticated, Active. One row: "Allow if" | (Roles blank) | true | Active (green badge) | pencil edit icon.

> **[Screenshot: Edit a trigger modal]**
> A modal titled "Edit a trigger" with X close button. Fields: "Select trigger *" dropdown showing "Updated". "Create a new trigger" section (expanded with ∧ chevron): "Name *" field containing "Solution accepted"; "Trigger objective * ⓘ" text area containing "Add a work note to \${number} with, summarized final accepted solution" with a language/settings icon; "Trigger is OFF" toggle (grey/disabled). Footer: "Cancel" and teal "Save" buttons.

> **[Screenshot: Manual test setup form in AI Agent Studio]**
> Test setup page at breadcrumb "Home > Test Details > Manual Test". Title "Test one example of behavior" with subtitle "Test how an AI agent or agentic workflow completes a task or if it allows users permission to access it." Form fields: "Choose a test type *" — "AI agent or workflow" selected in dropdown. "Choose a testing mode *" — radio buttons: "Premium Chat" (selected) and "Standard". "Name of the AI agent or agentic workflow *" — search/autocomplete field containing "Q Demo Next Best Action Agent". "Version *" — "1 – V1 (Active)" dropdown. "Task * ⓘ" with "Instruction for LLM" link — text area containing "Give me next steps for INC0012345." Footer: "Cancel" button and "Continue to test chat response" teal button.

> **[Screenshot: External AI agents – Data access settings for contextual data]**
> AI Agent Studio Settings page, Settings > External AI agents > Data access breadcrumb. Left sidebar shows: Now Assist Guardian, Long-term memory, External AI agents (expanded showing Discoverability, Data access (highlighted), Manage MCP servers, Model provider). Main content title "Contextual data". Description: "External AI agents can use different types of contextual data to improve their responses." Three toggle rows, all currently ON (blue): "Short-term memory ON" – "External AI agents can remember a user's preferences or facts from the current interaction only." "Long-term memory ON" – "External AI agents can remember a user's preferences or facts from previous interactions." "Knowledge graph for external AI agent interactions ON" – "External AI agents can use structured and unstructured data from different ServiceNow records."