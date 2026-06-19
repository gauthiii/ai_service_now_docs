# Define security controls for an AI agent

_Source pages: 97–98 | Depth: 2_

---

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

> **[Screenshot: Define user access step — ACL configuration in AI agent guided setup]**
> The guided setup for "Approval Assistance Agent (Chat)" is shown on the "Define user access" sub-step under "Define security controls". Left sidebar stepper shows: Define the specialty (filled), Add tools and information (filled), Define security controls (expanded: Define user access (half-filled/active), Define data access (empty)), Add triggers (empty), Select channels and status (empty). Main content area title: "Define user access". Instruction: "Define which users can access and interact with this AI agent. Once you save your choices, an access control list (ACL) will be automatically generated." Sub-title: "Define who can access this AI agent (ACLs)". A table with columns: Decision type, Roles, User authenticated, Active. One row: "Allow if" | (Roles blank) | true | Active (green badge) | pencil edit icon.