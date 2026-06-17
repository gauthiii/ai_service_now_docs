# Add tools and information to an AI agent

_Source pages: 63–96 | Depth: 2_

---

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

> **[Screenshot: Knowledge graph configuration in Add tools and information step]**
> A knowledge graph configuration card within the AI agent setup. Card header: "Knowledge graph | AI Instruction" with description "An AI agent uses a knowledge graph to understand the relationships between real-world entities to improve its outputs." Table with columns: Name, Execution mode, Display output, Description, Date added, Remove. One row: "Approval User Knowledge Graph" | Autonomous | false | "This tool is designed to retrieve specific requestor details required for approval evaluation and decision-making, such as department, location, company, assets, or other attributes." | 2025-07-14 | trash icon.

> **[Screenshot: Add tool dropdown menu showing all available tool types]**
> A dropdown list triggered by "Add tool ▾" button. The list shows tool type options in a vertical menu: Catalog item, Conversational topic, Desktop action (highlighted/selected), File upload, Flow action (with expand arrow ∨), Knowledge graph (with arrow and "d tools?" partial label), MCP server tool, Now Assist skill, Record operation, Script, Search retrieval (partially visible). A "Build their own bui... ∨" option also visible.
>
> **[Screenshot: Add a desktop action — Existing vs New desktop action choice panel]**
> A two-column reference panel showing two paths: Left column "Existing desktop action" — "a. Select an existing desktop action of type on-screen task or background task from the Select a desktop action drop-down list." Then "The background task desktop actions are supported for the following applications:" with a bulleted list: Microsoft Excel, Microsoft Outlook, Microsoft Word, PDF, PowerShell Connector. Right column "New desktop action" — "a. On the Add a desktop action modal, select the Click here to create a desktop action link." A modal screenshot shows "Add a desktop action" dialog with "Select a desktop action *" dropdown and "Can't find what you are looking for? Click here to create a desktop action" link, then "Cancel" and "Continue" buttons.