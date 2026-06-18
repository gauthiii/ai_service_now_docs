# Implement access control in Now Assist AI agents

_Source pages: 50–58 | Depth: 2_

---

<!-- page 50 -->
You can select Exclude delegates if you don't want delegated users to receive the notification.
By default, delegates will receive notifications.
6.Update or save the record.
Result
The specified users or groups can now receive notifications for a specific triggered condition of
AI agent or agentic workflow executions.
What to do next
Repeat for any other AI agent alert notifications you want to configure.
Implement access control in Now Assist AI agents
Implement security controls for AI agents and agentic workflows through access control lists
(ACLs), user identities, and role masking to implement the access control-based security
measures in the agentic system.
Security for AI agents overview
Access controls for agentic AI on the ServiceNow AI Platform comprises the major aspects:
determining which users can access agentic AI resources, and what access each of those
resources has once invoked. These aspects are controlled through three main components:
access control lists (ACLs), user identities and role masking. The interaction between these
components at the agentic workflow, AI agent, and tool levels within the AI Agent Studio
influences their overall security and functionality.
Access control lists
The access control lists (ACLs) in Now Assist AI agents determine which role(s) a user must have
to be allowed to invoke an agentic workflow or an AI agent. ACLs must be configured individually
for each agentic workflow, AI agent, and certain AI agent tools.
The ACLs added to an AI agent and agentic workflow are available in the respective related lists
for reference.
Important: ACLs configured in AI Agent Studio only determine the roles required for
users to invoke an agentic workflow or an AI agent. They don't determine the access that
the agentic workflow or an AI agent has once it’s invoked.
User identity
The user identity determines which user the AI agent or an agentic workflow operates as during
execution, and therefore the data it can access and the actions it can take, depending on the
roles assigned to the user identity.
After configuring the access control lists (ACLs), you must configure the User identity (also called
as Run as) which the AI agent or agentic workflow will run as during execution.
Note: Each agentic workflow and AI agent has its own user identity configuration.
There are two possible user configurations to select from:
•Dynamic user: The user identity of the person or resource (automated trigger/agentic
workflow/parent agent) invokes the execution of an AI agent or an agentic workflow. The
roles assigned to the agentic workflow or AI agent will change dynamically depending on the
identity of the invoking user.

<!-- page 51 -->
Note: Dynamic user is the default user identity, and you can use the dynamic user
unless there's a specific need that justifies an AI user.
•AI user: A dedicated user identity that the AI agent or an agentic workflow runs as during
execution, which has assigned roles that remain consistent regardless of who or how the
execution is invoked. For example, an AI agent or an agentic workflow may need to be run with
elevated privileges that the dynamic user might not have. If configured as a dynamic user, the
execution would fail. However, if the AI agent or agentic workflow is configured to run as an AI
user that has the elevated roles assigned to it, the execution will succeed even when invoked
by a user with lower privileges.
If you don't have a suitable AI user but want to use the AI user identity, you must create a
record on the User [sys_user] table. See Create a user and select AI user as the identity
type.
Note:
•Role masking limits which roles an AI agent can use during execution. It only applies
when the agent runs as a dynamic user — not when it runs as an AI user. The key
difference: AI users determine the identity the agent runs as and role masking narrows
the roles available to an agent that run as a dynamic user.
◦For more information about user identity in an AI agent, refer to Define security controls
for an AI agent.
◦For more information about user identity in an agentic workflow, refer to Define security
controls for an agentic workflow.
•For each component’s execution, the ACL is checked against the invoking user identity,
and if passed, the component’s run as user identity is applied. Any downstream
components’ ACLs are checked in comparison to the run as user identity of component
directly before it in the agentic hierarchy, and their run as user identities are passed down
to the next downstream component’s ACLs.
Note:
◦Now Assist Skills and other tools of AI agents always run as Dynamic Users.
◦This flow applies to user-invoked agents. Agents with automated triggers operate
without a conversational user; role masking still applies, but the invoking context
is a system session rather than an individual user.
Supervised execution mode for AI agents
Configuring AI agents' tools to run in supervised mode is another way to minimize the potential
negative impact of an AI agent that is not executing as expected. This will require human
approval for the tool's actions before it executes. You can use the Supervised mode to enhance
security for agents with the capability to perform sensitive or critical actions.
You can set the supervised execution mode when creating a tool in the AI agent guided setup.
For example, choose Supervised as the Execution mode when adding a catalog item tool. For
reference, see Add a catalog item to an AI agent.
Role masking in Now Assist AI agents
Role masking for AI agents and agentic workflows helps users enhance security by enabling
them to limit their roles during tool execution and verify that AI agents run with least-access
privileges.

<!-- page 52 -->
Role masking overview
Role masking lets AI admins in the AI Agent Studio to limit permissions of agentic workflows or AI
agents set to run as dynamic users by defining an allow-list of roles they can inherit from invoking
users, enforcing least-privilege access.
Use role masking to:
•Empower users to follow least-access principles when an agentic workflow or AI agent
executes on behalf of a dynamic user.
•Limit roles that agentic workflows, AI agents, and skills inherit from users and can be applied
when a user invokes them.
For more information about configuring skills, see Now Assist Skill Kit.
•Reduce the risk of AI solutions accessing the resources that they shouldn't, therefore helping
prevent agentic overreach into sensitive data or capabilities beyond what the user is allowed.
•Expand the security configurations to increase functionality of agentic products while reducing
security risks by enforcing governance for elevated or scoped roles.
Prerequisites
To configure role masking on your ServiceNow instance, you must have:
•Now Assist for Platform version 10.0.2-SS.
•The sn_aia.admin privileges.
Role masking behavior
Role masking behavior in agentic workflows, AI agents, and tools controls which of the invoking
user's roles are available to AI agents and tools during workflow execution. The roles are applied
sequentially across layers in the agentic workflow, AI agent, and Tool sequence to verify that
tools execute with minimum required privileges.
Role masking rules
1.Role masking limits the roles with which an agentic workflow, AI agent or Skill can execute to
the intersection between the roles assigned to the invoking user and the roles included in the
role masking approved roles list.
2. AI user vs Role mask:
The AI admin can choose for the component to run as either an AI user or a dynamic user. If
set to run as a dynamic user, the AI admin can configure role masking for the component. Role
masking cannot be configured for agentic workflows or AI agents set to run as AI users.
◦If an AI user is selected, all roles assigned to the AI user are available to the agentic workflow
or AI agent. This can be used to provide elevated access to the agentic workflow AI agent.
Note: Tools always run as dynamic users.
◦If Role masking is applied to an agentic workflow, AI agent, or tool running as a dynamic user,
the component runs with roles with roles limited to the intersection of the current invoking
user's roles and the roles included in the role masking approved roles list.
3. Multiple role masks can be configured and applied in the agentic workflow - AI agent - tool
sequence, but each mask still follows the intersection rule.

<!-- page 53 -->
4.Role masking only restricts roles that components can execute with, but never grants
components roles which exceed those of the invoking user. Thus, if the invoking user has
a role that is not included in the approved roles list, the component will not be allowed to
execute with that role. And, if the approved roles list includes a role that is not assigned to the
invoking user, the component will not be able to execute with that role again.
5. When a workflow running as an AI user invokes an AI agent running as a dynamic user with
role masking configured, then the roles available to the AI agent will be the intersection of the
role masking configuration of the AI agent and the roles assigned to the AI user of the agentic
workflow. The same holds true for an AI agent running as an AI user that then invokes a skill
with role masking configured.
Configuration
•To configure role masking for an AI agent, see Define security controls for an AI agent.
•To configure role masking for an AI agent, see Define security controls for an agentic workflow.
ACLs, role masking, and user identities in AI Agent Studio
Access control lists (ACLs) and role masking serve distinct security functions in AI Agent Studio.
The difference between these two mechanisms helps you configure agents with the correct
permissions and access boundaries.
ACLs: controlling access to the agent
ACLs define who can access an AI agent. They determine which users, groups, or roles are
permitted to interact with or invoke the agent. ACLs don't govern what the agent is allowed to do
once it is running.
ACLs control who can access an AI agent. The user identities and role masking control what
the agent can do. Using them together verifies that agents operate within defined security
boundaries. An ACL determines which roles a user must have to be allowed to invoke an AI
agent. If a user is not permitted by the ACL, they can't reach the agent at all.
User identities and role masking determine what the agent can do once it is invoked (that
is, e once the invoking user has passed the ACL check). User identities restrict the agent’s
permissions to the roles of the user identity with which the agent is executing. Role masking is
a configuration for agents set to run as Dynamic Users, which further reduces the scope of roles
the agent is permitted to run with by allowing the agent to execute only with the subset of the
invoking user’s roles which are also on the permitted roles list of the agent. Together, the user
identity and role masking restrict the agent's effective permissions at runtime — limiting which
records it can read or write and which operations it can perform. The agent can't exceed the
permissions defined by its masked role, even if the invoking user has broader access. Therefore,
both user identity and role masking mechanisms are required for complete agent security.
Role masking: controlling what the agent can do
Role masking defines is a means of further restricting what data and actions an AI agent
can access and perform when configured to run as a Dynamic user. Like user identities, role
masking controls the agent's permissions at runtime — which records it can read or write, which
operations it can execute, and which resources it can access on behalf of a user.
Role masking works by restricting the agent's roles to a subset of the permissions available to the
invoking user. Even if the invoking user has broader access, the agent operates only within the
permissions defined by its masked role. This is a way to verify that even when invoked by users
with high privileges, Dynamic User AI agents run only with the roles that are pertinent to their task
and cannot access unrelated data or take high privileged actions.

<!-- page 54 -->
Key distinction
A common source of confusion is assuming that ACLs define agent actions. They don't! Use the
following summary to distinguish the mechanisms:
Distinguishing ACLS, role masking, and user identities
Feature ACLs Role masking User identities
Controls Who can access the What the agent can do Which identity the agent
agent acts as
Applied to Users, groups, and roles The agent's runtime The dynamic user
that invoke the agent execution context assigned at runtime
Security Restricts agent visibility Restricts agent actions Determines privilege
purpose and invocation and data access scope during execution
Distinguishing AI user and Dynamic user
Feature AI user Dynamic user
Definition A predefined identity the A runtime identity assigned to the agent
agent runs as during execution
Role masking No Yes
applies
Roles used Fixed to the AI user's Scoped down by role masking
assigned roles
Identity source Configured statically Determined dynamically at runtime
ACL and role masking evaluation sequence
The following sequence defines how ACLs and role masks are evaluated across the agentic
workflow, AI agent, and tool execution contexts:
Step 1: Agentic workflow ACL validation
ACLs configured for workflows are evaluated against the invoking user (automated
or conversational) session roles.
Step 2: Agentic workflow role mask application
If the invoking user meets the agentic workflow's ACL criteria (and the agentic
workflow is set to run as a dynamic user with role masking configured), the agentic
workflow role masking is applied to the invoking user's roles (there by restricting
roles from the user session based on the intersection with the configured role
masking).
Step 3: AI agent ACL validation
When an agentic workflow invokes an AI agent, the AI agents' ACLs are validated
against one AI agent ACLs are validated against one of the roles with which the
agentic workflow was approved to execute. Thus:
•If the agentic workflow was set to run as an AI user, the AI agent ACL will validate
against the AI user session configured at the workflow.
•If the agentic workflow was set to run as a dynamic user with role masking, the
AI agent ACL will check whether the effective remaining roles after applying the
workflow role masking meets the ACL criteria.

<!-- page 55 -->
Step 4: AI agent role masking application
Similar to the agentic workflow above, either the AI user or the AI agent role mask is
applied:
•If an AI user is selected, all roles of the AI user are enforced (no masking).
•If role mask is applied, then the roles are limited further based on intersection
with the effective roles after applying the workflow role masking.
Step 5: Tool ACL validation
If a tool uses ACLs, these are checked against the roles that the AI agent—assigned
to the tool—is permitted to use. This means that if role masking is set up, only the
roles left after masking are considered during validation.
Step 6: Tool role masking application
If the tool is a skill and has role mask configured, then the approved roles will be
applied to roles with which the AI agent was approved to run, thereby limiting roles
for the tool's execution.
Summary of ACL and role masking evaluation order:
1.Agentic workflow ACLs → validated with invoking (conversational or automated) user
session's roles.
2. Agentic workflow role masking → applied to the invoking user session.
3. AI agent ACLs → validated with agentic workflow's approved roles (agentic workflow's AI user
OR roles after workflow role masking).
4.AI agent role masking → applied to agentic workflow's approved roles.
5. Tool ACLs → validated with AI agent's approved roles (AI agent's AI user or roles after agent
role masking).
6.Tool role mask (Skills only) → applied to AI agent's approved roles.
Note: When evaluating ACLs and role masks, the admin can identify where and why
execution failed due to either ACL or role mask restrictions.
Why these security mechanisms matter
Using ACLs, role masking, and user identities together provides layered security for AI agents.
ACLs prevent unauthorized users from reaching the agent. Role masking verifies that even
authorized users can't trigger agent actions that exceed defined boundaries. User identities
ensure the agent operates under the correct privilege scope at runtime, preventing escalation
beyond what the assigned dynamic user permits. Configuring only one of these mechanisms
leaves a gap in the agent's security posture.
Deny-by-default ACL configuration
The ServiceNow AI Platform enforces a deny-by-default ACL (Access Control Lists) configuration
for AI agentic types on freshly reset instances, for any AI agents and agentic workflows that don't
have an individual ACL configured to reduce unauthorized access risks.
Configure ACLs in AI Agent Studio
ACLs configured in the AI Agent Studio for AI agents and agentic workflows are role-based and
of the Allow If type:

<!-- page 56 -->
•Allow-If: Grants access to data or resources when any of the specified conditions in the ACL
are met. Allow If ACLs don't prevent other ACLs from granting access to the same resource
even if it that specific ACL itself doesn't grant access.
•Deny-Unless: Grants access only when the invoking user identity meets all the specified
conditions. No other ACLs can override or grant access to that resource once a Deny Unless
ACL is in place. This is available when configuring ACLS in the ACL [sys_security_acl] table and
not in the AI Agent Studio.
There are three possible options for ACLs created in AI Agent Studio:
•Any authenticated user: Grants access to any user who is authenticated on the
instance, regardless of the role.
•Users with specified roles: The default ACL option that requires you to select the
specific roles required to invoke an AI agent or an agentic workflow.
Note: As the ACLs are Allow If ACLs, any user with at least one of the roles will be able
to invoke the AI agent or agentic workflow.
•Public: Grants access to all users, including guests who aren’t signed in.
Each AI agent and agentic workflow must have its own unique ACL.
•To configure an ACL in the AI Agent Studio for an AI agent, see the Define security controls for
an AI agent guided setup.
•To configure an ACL for an agentic workflow, see the Define security controls for an agentic
workflow guided setup.
Note: If there are conflicting security requirements between agentic workflows, AI agents,
and AI agent tools, or if the invoking user meets the criteria for some ACLs but not others,
your agentic AI fails to execute. When configuring these security settings, consider all
aspects of the agentic system- including the agentic workflow, AI agents, and tools.
Security checks on AI Agent Studio
To inform users about security checks on the agentic system, the platform provides the following
notifications in the AI Agent Studio interface:

<!-- page 57 -->
•AI Agent Studio Overview page: The AI Agent Studio overview page displays a warning when
agents or agentic workflows don't have explicit ACLs configured on the instance.
•AI agent guided setup: The AI agent guided setup page displays a warning banner when that
agent doesn't have the required ACLs configured.
Note: To configure access control lists for an AI agent, see Define security controls for
an AI agent.
•Agentic workflow guided setup: The agentic workflow agent guided setup page displays a
warning banner when that agentic workflow doesn't have the required ACLs configured.

<!-- page 58 -->
Note: To configure access control lists for an agentic workflow, see Define security
controls for an agentic workflow.
These warnings indicate that ACLs are missing and should be configured to verify secure and
uninterrupted operation. Users who have already switched to deny-by-default and users who
still use wildcard ACLs will both see these warnings. For wildcard ACL users, the warnings are
informational.
ACL types
The AI access control changes brought in five new ACL types that default to allow access,
expanding the platform attack surface. The ServiceNow AI Platform enforces a deny-by-default
directive for these agentic ACL types on the freshly reset instances. This configuration verifies
that records without explicit ACLs aren't inadvertently exposed, aligning the platform with secure-
by-default best practices for AI agentic components.
The ACL types are:
•gen_ai_agent
•gen_ai_workflow
•gen_ai_skill
•Flow
•flow_action
How deny-by-default enforcement works
The Security Attribute field value for AI Agent and agentic workflow on the Access Controls
table [sys_security_acl] is set to Never, enforcing the deny behavior and leaving the Decision
Type field value as is, that is, Allow If. This configuration verifies that if an AI component already
has a primary ACL in place, access continues to be governed by that ACL. The backup (wild card)
ACLs deny access only when no primary ACL is present. The old wildcard ACLs allow users with
agents that predate the availability of access controls in agentic products to continue to run
their agents, but that general guidelines is to implement deny by default in all instances. The
replacement means that the AI agents and agentic workflows must have explicit ACL entries to
operate. Without explicit ACLs, access is denied by default.