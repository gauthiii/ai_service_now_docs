# Find AI agents

_Source pages: 60–60 | Depth: 2_

---

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