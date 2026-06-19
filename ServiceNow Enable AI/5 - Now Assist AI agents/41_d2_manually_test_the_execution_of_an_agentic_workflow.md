# Manually test the execution of an agentic workflow

_Source pages: 133–134 | Depth: 2_

---

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