# Define security controls for an agentic workflow

_Source pages: 123–124 | Depth: 2_

---

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