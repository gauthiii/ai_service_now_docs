# Manually test the execution of an AI agent

_Source pages: 108–109 | Depth: 2_

---

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

> **[Screenshot: Manual test setup form in AI Agent Studio]**
> Test setup page at breadcrumb "Home > Test Details > Manual Test". Title "Test one example of behavior" with subtitle "Test how an AI agent or agentic workflow completes a task or if it allows users permission to access it." Form fields: "Choose a test type *" — "AI agent or workflow" selected in dropdown. "Choose a testing mode *" — radio buttons: "Premium Chat" (selected) and "Standard". "Name of the AI agent or agentic workflow *" — search/autocomplete field containing "Q Demo Next Best Action Agent". "Version *" — "1 – V1 (Active)" dropdown. "Task * ⓘ" with "Instruction for LLM" link — text area containing "Give me next steps for INC0012345." Footer: "Cancel" button and "Continue to test chat response" teal button.