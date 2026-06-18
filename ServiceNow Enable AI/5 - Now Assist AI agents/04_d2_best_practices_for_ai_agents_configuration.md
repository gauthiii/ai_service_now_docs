# Best practices for AI agents configuration

_Source pages: 12–20 | Depth: 2_

---

<!-- page 12 -->
managing intricate workflows, facilitating real-time adaptability, and efficient task delegation
among agents.
The role of Orchestrator in AI Agent Studio:
1.Task Coordination & Execution: manages the interaction between multiple AI agents, ensuring
that tasks are executed in the correct sequence.
2. Dynamic Decision-Making: Can invoke AI models dynamically based on the scenario.
3. Seamless Integration with Enterprise Systems: Works with ServiceNow workflows, CMDB, and
third-party APIs to enable end-to-end automation.
4.Handling Multi-Step Workflows: Enables chained execution of AI-driven tasks among multiple
AI Agents.
5. Policy & Governance Enforcement: Enforces governance rules to ensure that AI agents adhere
to compliance and security standards.
The Orchestrator works with ReAct prompt, where the previous reflection prompt has been
merged with the planning prompt for a streamlined execution experience improving the
efficiency and visibility of planner actions. With the ReAct prompt, a scheduling mode called
Route has been introduced that enables asynchronous, parallel tool execution within agents to
reduce latency and improve performance when an agent needs assistance from another agent
during the execution process.
Dynamic Orchestrator for agentic workflows
The dynamic orchestrator helps map the right agents to the user's agentic workflow to provide
better performance and accuracy. When there are more than the ideal 8 to 10 AI agents available
for an agentic workflow, then the dynamic orchestrator helps identify the agents that need to be
considered for executing that agentic workflow in the planning phase.
User impersonation in Now Assist AI agents
The agentic workflow executes tools as the logged-in user in the Now Assist panel. Any
operations that are performed within the tool in this flow are also executed as the logged-in user.
After impersonation is enabled, testing an AI agent uses the instance-level impersonation.
Administrators can see logs with individual AI agent names as a record of who approved the
agentic action in an agentic workflow. The logs help when determining a point of contact if
there’s an issue with the approved agentic action by the AI agent.
With impersonation, the fulfiller in the Now Assist panel and the requester in Virtual Agent can
see the transactions recorded in the name of the AI agent that performed the agentic workflow
execution.
Note: Virtual Agent can be turned on only for AI agents at the Define availability section in
the AI agent guided setup. For more information, see Create an AI agent.
Best practices for AI agents configuration
AI agents can dynamically adjust the actions that are based on the progress and changing
conditions of incidents or cases to help ensure that they stay focused on achieving their
objectives.
AI agents can dynamically adjust the actions that are based on the progress and changing
conditions of incidents or cases to help ensure that they stay focused on achieving their
objectives.

<!-- page 13 -->
•You can create, duplicate, and modify AI agents and agentic workflows. The default AI agents
and agentic workflows are available in read only mode and to utilize them, you are required to
duplicate these resources.
◦For more information about duplicating an AI agent, see Duplicate an AI agent.
◦For more information about duplicating an agentic workflow, see Duplicate an agentic
workflow.
•You can also modify the duplicated AI agent and agentic workflow to meet your requirements.
◦For more information about modifying an AI agent, see Modify an AI agent.
◦For more information about modifying an agentic workflow, see Modify an agentic workflow.
Note: The agentic workflows available by default in the system are inactive and you must
activate them to utilize. For more information about activating an agentic workflow, see
agentic workflow template.
Now Assist AI agents capabilities
Lists the features supported by Now Assist AI agents, including configuration options and
functional capabilities.
Invoke conversations with AI Agent Background Channel
The AI Agent Background Channel helps you to invoke AI Agent or agentic workflow execution
from the Workspace. Use the AI Agent Background Channel associated with the AI Agent
Background Provider to invoke conversations. The AI Agent Background Provider is based on the
Custom Adapter Framework from Virtual Agent. For more information, see Configure a provider
for your custom chat integration .
Create a channel identifier in the Provider Channel Identities table [sys_cs_provider_application]
to add any additional conversational capabilities to your own provider application and get a new
inbound ID that allows for customization. For more information, see Create a channel identifier
for your custom chat integration .
To start a conversation, trigger the flow using the
sn_aia.AiAgentRunttimeUtil().startAiAgentConversation(request) API
in the Script Include (sys_script_include) of the AIAgentBackgroundProvider and select Run
Script. When the Script execution status indicates Success, the conversation begins in the order
of utterances defined in the Script.
Conversations that are invoked for executing an AI agent are logged in the Execution Plans
[sn_aia_execution_plan] table. Open the conversation record to confirm the device type as AI
Agent Background. Open the execution record to see the Execution Tasks, Messages, and the
Tools Executions used to execute the AI agent.
You can also see the entire execution steps on the AI Agent Studio Testing page by copying
the execution plan record's [sys_Id] and testing it. On the Chat responses tab, in the AI agent
decision logs, you can see the AI agent details and the tools it used to resolve the issue.
Interactive and Non-interactive AI agents
The Interactive AI agents reach out to users for information when there is a fallback in the
execution process, and the AI agent re-triggers the flow.
The Non-interactive AI agents do not reach out to the user at any fallback stage in the execution
process. When the AI agent needs user information, it takes the dynamic prompt approach using
the ReAct layer, where the prompt of the ReAct will change based on the execution mode of

<!-- page 14 -->
the AI agent or agentic workflow. Therefore, in the Non-interactive execution, the reach fallback
options do not have to collect input from a user as a fallback option. However, the output of the AI
agent or agentic workflow will still need to be presented to the user, and in any execution failure
scenario, a message in the Now Assist panel or Virtual Agent is shown.
To implement the Non-interactive execution, the Execution Mode field is added in the Execution
Plans [sn_aia_execution_plan] table, where the execution mode can be Interactive or Non
Interactive based on the given runtime parameter.
You can run the AI agents and agentic workflows concurrently in the AI Agent Background
Channel and in Non-interactive mode where the background execution allows AI agents to
operate with any chat panel like Now Assist panel or Virtual Agent.
Multilingual support
You can leverage multilingual support for AI agents across languages for better translation
quality to:
•Tune system prompts for native translations.
•Implement dynamic translation strategies when native support is unavailable.
•Provide extensive testing via automated and manual evaluations.
General guidelines for creating AI agents and agentic workflows
By following some general guidelines for creating AI agents and agentic workflows, you can
create clear and effective instructions that help maximize their efficiency and effectiveness.
https://player.vimeo.com/video/1098393879?
h=d37199a090&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479
Creating AI agents and agentic workflows overview
AI agents and agentic workflows rely on large language models (LLMs), so the language that you
use for their instructions is important. There are many steps that you can take to help improve the
quality and consistency of your agentic AI solutions.
Follow these guidelines when writing AI instructions for an AI agent or agentic workflow.
Clarity
•Use instructions that are concise, clear, and precise. Simple language can help
remove ambiguous situations that could stall or disrupt an agent's progress.
Example: "You're an assistant tasked with helping the caller or requester by
suggesting answers to survey questions." instead of "You help callers with
questions."
•Use specific action verbs. Example: "Analyze" instead of "look at."
•Add explicit conditions when a certain step must be completed. Example: "If
priority = High, then escalate immediately" instead of "escalate urgent issues."
•Clarify boundaries and limitations. Example: "NEVER modify incident status
without supervisor approval."
•Limit technical jargon. Technical jargon can limit applicability because it may not
be accessible or universal.
Context

<!-- page 15 -->
•Embed requirements within context. Specify when certain requirements should
be used within the task. Example: "When generating answers to present to the
user, apply standard quality controls."
•Only include the context that affects decision making. Avoid extraneous
information to help prevent the AI agent or agentic workflow from incorporating
unwanted details.
•Define what good outcomes look like. Include examples. Missing or vague
descriptions of results could cause AI agents or agentic workflows to exit before
the end state is reached. Example: "Present the user with a report that includes a
minimum of 3 relevant graphs pertaining to the list of records."
Constraints
•Denote hard requirements. Use strong language to insist on the importance of
the requirements. While output may not always follow these requirements, being
specific about standards can help reduce deviations.
•Describe preferences that can be adjusted based on context.
•Add conditional restraints. Example: "If more than one record is returned, present
the results to the user in order of creation date. If more than five records are
returned, present the results to the user in order of relevance."
Coherence
•Create steps that flow logically. Each step should build on the results of the
previous step. Example: "Step 1 gathers a list of incident records. Step 2 performs
record operations on those list of records."
•Use consistent terminology throughout.
•Design instructions that serve the overall objective. All of your tools and AI agents
work together to solve problems.
•Break complex goals into individual pieces. Example: "Step 1: Analyze customer
data systematically. Step 2: Check priority and validation permissions. Step 3:
Generate and format comprehensive report."
Structure
•Use consistent formatting. Similar instructions should use similar language
patterns.
•Group related steps together.
•Create a smooth flow from instruction to instruction. Along with grouped
instructions and logical step progression, this provides a systematic and
structured process for the AI agent or agentic workflow to follow.
Guidelines for creating AI agents
The description, AI agent role, and list of steps give the LLM the context and instructions to
perform a task. Together, they form the blueprint that's necessary for the LLM to complete its
role in a complex workflow. Follow these guidelines to improve the accuracy, adaptability, and
optimization of the AI agent:
AI agent description

<!-- page 16 -->
•Specify the key areas or tasks that you want the agent to handle. Example:
"Specializes in handling inquiries and resolving customer issues."
•Use clear, focused language and avoid vague terminology.
•Define the agent's inputs, outputs, and context.
•Differentiate the agent's unique role from other agents. Provide distinct and
detailed descriptions of what that specific agent should do that is different than
other agents.
AI agent role
•Clearly state the primary function of the AI agent in one or two sentences.
Example: "The AI agent acts as a customer service assistant."
•State the specific business challenge that you want the AI agent to address.
Example: "Reducing customer wait times by 50%."
•Provide a brief scenario of how the AI agent is to be used. Example: "Automating
responses to common queries and escalating complex issues to human agents."
AI agent list of steps
•Create a logical progression from step to step.
•Use action-oriented language. Use verbs like the following:
◦Fetch
◦Retrieve
◦Filter
◦Analyze
◦Extract
◦Parse
◦Update
◦Send
◦Notify
◦Generate
◦Validate
•Include outputs for each step to measure the task completion. Example: "Return
the total incident count to other agents or processes that need it."
•Add contingencies to account for unexpected scenarios. Example: "If you
encounter an error while looking up records, try again. If you still get an error,
report that an error occurred."
•Define success and completion. Provide end states so that the AI Agent
Orchestrator can determine whether an AI agent has finished its objective.
•If you have created a tool for your AI agent, refer to the tool by name. However,
verify that the instructions change if the tool is ever renamed. If you don't, then
the AI agent might not complete its task.
Tools

<!-- page 17 -->
•Write detailed tool descriptions to help the AI agent understand what the tool is
and how to use it.
•Create tools that work together. Build your tools around achieving the list of steps
for the AI agent itself.
•Use the output transformation strategy field to define what the output of a tool
should look like. Specifying how a tool should present its output can help the AI
agent use that output when employing other tools or when sharing information
between other agents.
Guidelines for creating agentic workflows
Follow these agentic workflow guidelines to provide the detailed information and the steps
needed to accomplish a task:
Agentic workflow list of steps
•Write each step sequentially and number each step so that there's a logical and
actionable flow.
•Account for as many possibilities as you can to avoid gaps. Provide enough detail
that the agentic workflow can adapt if it encounters an edge case.
•Define the starting conditions, actions, decision points, and end states.
•Refer to end users as "the user."
•Use verbs like "show," "display," or "inform" to describe steps where the user
needs to be shown something but they do not need to provide input.
Additional tips
Associate a maximum of 10 agents per agentic workflow. Adding more agents might
not provide better or faster results. Instead, use small, well-defined scopes.
Note: You can assign up to 100 agents to an agentic workflow. However, not
all 100 agents may be involved in resolving the agentic workflow. The AI Agent
Orchestrator decides which agents should execute the plan. For example, an
incident resolution gets impacted by the size of the agentic workflow and the
number of agents that are assigned to it.
When creating agentic workflows with more than one assigned agent, make sure that you clearly
define the agents with non-overlapping responsibilities. Include explicit limitations in the agents'
roles. For example, one agent could handle user record details while another agent handles the
incident record details.
Common issues
Problem: Agent consistently uses the wrong tool
Potential solutions:
•Create clear, specific instructions with action keywords.
•Write detailed tool descriptions that specify when and why to use each tool.
•Include explicit input and output guidance in tool descriptions.
•Evaluate tool selection logic by testing against various scenarios.
Problem: Inconsistent output quality
Potential solutions:

<!-- page 18 -->
•Embed standards as actionable requirements.
•Use phrases such as "implementing professional standards."
•Add quality verification steps.
Problem: Quality checks or other steps skipped
Potential solutions:
•Convert checklists to actionable steps.
•Use phrases such as "analyze completion against criteria."
•Add conditional progression logic.
Additional resources
For more prompting recommendations, see the Community Now Assist AI Agents prompting
guide .
Example AI agent
Use the example AI agent with clear name, description, AI agent role, and list of steps fields to
use as a guide when creating your own AI agents.
Name
Categorize ITSM incident AI agent
Description
Categorize ITSM incident AI agent assigns the appropriate category, subcategory,
and configuration item (CI) to an incident.
AI agent role
You're an expert in analyzing incidents and are tasked with assigning an appropriate
category, subcategory, and configuration item (CI).
List of steps
Objective: Incidents represent disruptions, unavailability of a service, or issues
faced by a user. The agent's task is to understand the issue and assign the
appropriate:
•Category
•Subcategory
•Configuration Item (CI)
Step 1: Retrieve Incident Details.
•Fetch the details of the given incident.
•DO NOT PROCEED if incident details are missing.
•If no details are found, verify the correctness of the incident number.
•Only proceed when incident details are successfully retrieved.
Step 2: Assign Category, Subcategory, and CI.
Step 2.1: Determine the Category.

<!-- page 19 -->
•Fetch the available categories.
•Recommend a category only if the incident details contain clear, specific,
and meaningful information that directly corresponds to one of the available
categories.
•If the details are too vague, generic, lack context, or do not clearly indicate
a relevant category, then set the category and subcategory to "Not
determined" (field_value = null). Do not edit the subcategory later.
•Do not infer or guess a category based on common or placeholder terms (for
example, "test", "check", "issue") unless they are accompanied by enough context
to confidently justify a match.
•You must be 100% certain that the incident clearly belongs to a category before
assigning it.
Step 2.2: Determine the Subcategory.
•Fetch the list of available subcategories for the chosen category.
•Choose the most appropriate subcategory based on the incident details.
•If no suitable subcategory can be determined or if the category is not determined,
set subcategory to: "Not determined" (field_value = null).
Step 2.3: Determine the Configuration Item (CI).
•Fetch the list of CIs assigned to the caller of the incident.
•Pick the most relevant CI based on
◦Name
◦Manufacturer
◦Asset Name
•If no relevant CI is found or the list is empty, set CI to: "Not
determined" (field_value = null).
•If multiple options exist, select the most relevant one.
Step 3: Present the Recommendation.
•PRESENT the recommended values to the user in the following bullet-point
format:
Recommended incident ({incident number}) categorization details:
◦Category: {recommended category}, (Reason: {reason for recommendation})
◦Subcategory: {recommended subcategory}, (Reason: {reason for
recommendation})
◦Caller's CI: {recommended CI}, (Reason: {reason for recommendation})
•Ensure this information is explicitly displayed before proceeding to the next step.
Step 4: Update the Incident. Update the incident record with the selected Category,
Subcategory, and CI values.
Key Considerations:

<!-- page 20 -->
•NEVER ask the user for input.
•Never proceed without retrieving incident details.
•If NO appropriate value is found, assign "Not determined" (field_value = null).
•Do NOT ask the user to manually determine category, subcategory, or CI.
•Always present recommendations before updating the incident.
•Ensure that the recommendations are logical and relevant to the incident details.
Example agentic workflow
Use the example agentic workflow with clear name, description, and list of steps fields to use as a
guide when creating your own agentic workflows.
Name
Investigate incident
Description
This workflow streamlines incident management by analyzing incidents, linking
them to existing problems, and identifying relevant catalog items. It leverages three
specialized AI agents: the ITSM Incident Resolution Investigation AI Agent retrieves
incident details, identifies similar incidents, and fetches relevant knowledge
articles; the Link Incident to Problem AI Agent searches for and links incidents
to existing problems based on contextual similarity; and the Find Catalog Item
AI Agent locates relevant catalog items and integrates their details into incident
records or provides direct links. This structured orchestration ensures efficient
incident resolution, reduces redundancy, and enhances decision-making by
leveraging historical data, organizational knowledge, and catalog resources,
ultimately improving enterprise incident management effectiveness.
List of steps
Step 1: Incident Analysis:
Analyze incident details and retrieve relevant historical data and knowledge articles.
Step 1.1: Retrieve Incident Context:
•Use the ITSM Incident Resolution Investigation AI Agent to fetch incident details
(short description, description, caller, state).
•If retrieval fails, inform the user: "Unable to retrieve incident details. Please verify
the incident number." and terminate workflow.
Step 1.2: Identify Similar Incidents and Knowledge Articles:
•Use the ITSM Incident Resolution Investigation AI Agent to find similar incidents
and relevant knowledge articles.
•Confirm with the user before adding resolutions to incident comments.
Step 1.3: Prepare Incident Documentation:
Update incident additional comments with approved resolutions and knowledge
article references, preparing clear documentation for next phase.
Step 2: Problem Linking:
Link the incident to an existing relevant problem, if applicable.