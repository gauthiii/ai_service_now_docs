# Create an AI voice agent

_Source pages: 150–154 | Depth: 2_

---

<!-- page 150 -->
Field Description
Inbound message Select the Static token or Hash message token that you
verification created.
Outbound message Select the Static token or Hash message token that you
creation created.
Outbound service token This field is not supported.
d. Select Submit.
3. Set the channel identity.
a.Navigate to All, and then enter sys_cs_provider_application.list in the
navigation filter.
b.Select the AI Voice Agent Provider Application record to open it.
If you want to use an existing application or create a new provider application, be sure to
update the existing configuration according to the values mentioned in Configuration for
custom AI voice agent provider before proceeding further.
c.In the Provider Channel Identity form, locate the Message auth field and select the message
auth that you set up previously.
d. Select Update.
Create an AI voice agent
Create an AI voice agent in the AI Agent Studio to resolve cases, incidents, or tasks through the
phone channel.
Before you begin
Role required: sn_voice_aia.admin
Procedure
1.Navigate to the New AI Agent page in the Assistant Designer or AI Agent Studio.
To Do this
Navigate in Assistant Designer
a.Go to the Asset Library and select Create
asset.
The Create asset window appears.

<!-- page 151 -->
To Do this
b.Select AI Agent.
You are redirected to the New AI Agent
workflow in the AI Agent Studio.
Navigate in AI Agent Studio
a.Go to All > AI Agent Studio > Create and
manage and select the AI agents tab.
b.In the Add drop-down list, select Voice to
create an AI voice agent.
2. On the Define the specialty page, describe your AI agent and provide instructions on how you
want your AI agent to perform its tasks.
Select Generate details to generate a description and instructions with Now Assist. If you
provide the description of what you want the agent to do, you can select Generate to write the
name, description, AI agent role, and instructions fields for you. You can change those fields
after the text has been generated or try again with new instructions.
Note: The more details that you provide, the more accurately your AI agent can perform.
a.On the form, fill in the fields.
Give a unique name and description form
Field Description
AI agent name
Name of the AI agent. Provide a name
according to the outcome that you want your
AI agent to achieve.
For example: Incident manager.
AI agent description
Brief summary of what your AI agent can do
autonomously. Outline all the activities that
you want your AI agent to perform.
Example for the Incident manager: The
Incident manager AI agent assists users
with existing incidents by gathering
information over the phone, matching it to
records in the system, and sharing relevant
incident details. It can also make limited
updates to the incident using preconfigured
tools.
b.On the form, fill in the fields.

<!-- page 152 -->
Note: The AI agent uses this information as guidance to tailor its responses and
actions.
Define the role and required steps form
Field Description
AI Agent role
Capabilities and responsibilities for your AI
agent. Roles enable your AI agent to perform
its required actions.
Example for the Incident manager: You’re an
AI agent with the purpose of communicating
incident details and making changes to
those incidents for users calling in as long
as they match the caller for those incidents.
You have access to tools that can retrieve
a few fields for incidents, comments, and
escalate the urgency. Only proceed with
gathering information and tool execution
if the user and caller listed on the incident
match.
List of steps
Necessary steps to be followed by the AI
agent while carrying out its role.
Note: The instructions are sent to the
large language model (LLM).
Example for the Incident manager: Incidents
are records for tracking issues and their
resolution updates through a set of journal
entries. Your objective is to act as an
incident manager. If the user provides an
incident number, verify the caller identity
before sharing permitted details. If no
number is given, match incidents using the
short description and confirm with the user.
Allow updates only if the user matches the
caller. Offer live agent transfer if the user is
unsatisfied.
To resolve an incident:
i. Verify the caller number.
ii.Search for incident records associated
with the user.
iii. Consider the context and relationship
between different data points.
iv.If the user provides an incident number,
verify their identity against the caller field
before sharing permitted details. Proceed
with updates or modifications only after
the caller's identity is verified.

<!-- page 153 -->
Field Description
v. If no incident number is given, search
using the short description, list matching
incidents with brief summaries, and
confirm which one the users wants to
explore further.
vi. Only share allowed fields (for example,
incident number, caller, dates, urgency,
state, short description, comments).
Summarize comments if there are more
than five, and notify the user if a field is
empty or restricted.
vii.If the user is unsatisfied, offer to transfer
to a live agent. End the conversation
politely if they’re satisfied or after a
transfer.
Follow these guidelines for writing effective Instructions:
▪Define the AI agent's role:
▪Clearly state the primary function of the AI agent in one or two sentences.
▪Example: The AI agent acts as a customer service assistant.
▪Outline specialties:
▪Specify the key areas or tasks that the AI agent handles.
▪Example: Specializes in handling inquiries and resolving customer issues.
▪Identify the business problem:
▪Articulate the specific business challenge for the AI agent to address.
▪Example: Reducing customer wait times by 50%.
▪Describe the workflow:
▪Provide a brief scenario of how the AI agent is to be used.
▪Example: Automating responses to common queries and escalating complex issues to
human agents.
▪Be concise and clear:
▪Use simple and direct language.
▪Avoid jargon and technical terms.
▪Example: The AI agent helps customers find answers quickly.
▪Provide actionable steps:
▪Include specific instructions on how to set up and use the AI agent.
▪Example: Step 1: Define the types of inquiries the AI agent handles. Step 2: Integrate the
AI agent with the customer service platform.

<!-- page 154 -->
▪Include examples:
▪Provide real-world examples to illustrate how the AI agent should function.
▪Example: For example, the AI agent can automatically respond to questions about the
order status.
▪Focus on outcomes:
▪Emphasize the benefits and outcomes of using the AI agent.
▪Example: Using the AI agent leads to faster resolution times and higher customer
satisfaction scores.
By following these general guidelines, you can create clear and effective prompt instructions
that enable you to use AI agents to their fullest potential. For more information and
examples, see General guidelines for creating AI agents.
c.Optional: Determine if the AI agent can be accessed by third parties.
Making your AI agent discoverable allows you to use your ServiceNow AI agent on other
platforms. You can still use it on your ServiceNow instances as well.
d. Select Save and continue to move to the next step.
3. In the Add tools and information tab, configure additional tools and data sources that provide
capabilities necessary to your AI agent to accomplish its objectives.
Select Recommend Tools for Now Assist to suggest the tools that are required for the AI
agent to carry out the tasks that it's built for. Now Assist suggests tools based on the AI agent
description and instructions given in the previous section.
You can add the tools suggested by Now Assist or manually select the tools from the Add tool
drop-down list. You must add at least one tool to continue setting up your AI agent, but you can
also add more tools to your AI agent. The data input and output type for tools must be string for
optimal voice experience.
The following tools are available for AI voice agents:
◦File upload: Different file types such as PDF, DOCX, or TXT formats that you can add to your
AI agent.
◦Flow action: Custom automated processes in your system that you can add to your AI agent.
Example for the Incident manager agent: Fetch details of the incident.
◦Knowledge Graph: Various Knowledge Graph items that you can add to you AI agent.
◦MCP server tool: An MCP server tool that you can to your AI agent.
◦Record operation: Different record operations that you can add to your AI agent.
◦Script: Editable scripts and APIs that you can add to your AI agent.
◦Search retrieval: Information retrieval processes in your system that you can add to your AI
agent.
Note: Create a dedicated search profile that includes only the KB articles for AI voice
agents to reduce the search scope and minimize latency.
◦Sub flow: Automated flows in your system that you can add to your AI agent.