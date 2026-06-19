# Explore Now Assist AI agents

_Source pages: 3–25 | Depth: 1_

---

<!-- page 3 -->
Data collection
ServiceNow collects and uses the inputs, outputs, and edits to outputs of this application to develop and improve ServiceNow technologies including ServiceNow
models and AI products. Customers can opt out of future data collection at any time, as described in the Now Assist Opt-Out page.
For more information, see the Now Assist documentation.
Explore Now Assist AI agents
Learn how the Now Assist AI agents enhance live agent productivity by mimicking human-like
intelligence to manage tasks ranging from automated responses to complex problem solving.
Now Assist AI agents overview
The Now Assist AI agents are virtual agents within the ServiceNow AI Platform ecosystem. They
can perform specific tasks and functions, often using natural language instead of traditional
code.
AI agents can perform the following tasks:
•Analyze data.
•Retrieve information from knowledge bases and enterprise systems.
•Execute automated actions.
•Collaborate with other agents to resolve issues or accomplish requests.
Example: Imagine you need to reset your password. Multiple AI agents might be involved:
1.One agent understands the request.
2. Another verifies your account details.
3. A third agent conducts a security check.
4.A fourth agent resets the password and notifies you.
Agentic AI framework
AI Agent Studio
The AI Agent Studio enables you to create, manage, and test AI agents and agentic
workflows in a unified environment.
agentic system
The ServiceNow AI Platform's agentic system uses AI agents, orchestrated by an
Orchestrator, to execute Agentic workflows.
AI agents
On the ServiceNow AI Platform agentic system, an AI agent contains a set of large
language model (LLM) instructions with the tools to accomplish tasks.
agentic workflow
Agentic workflows are smart, context-aware, automated processes designed and
executed by AI agents. They represent dynamic, human-like processes where
specialized AI agents collaborate to accomplish complex goals. Here are a few key
characteristics of Agentic workflows:
•Autonomous: Operate independently without constant human intervention.
•Adaptive: Adjust to changing situations and business needs.

<!-- page 4 -->
•Collaborative: Work together to complete complex tasks.
•Intelligent: Use large language models and business data to make informed
decisions.
Orchestrator
The AI agent Orchestrator is a central management system that coordinates AI
agents to ensure they collaborate effectively to complete complex workflows.
For more information, see Understand the Now Assist AI agents.
Guided Setup
The guided setup process in the helps you configure your AI Agent triggers, data
sources, and display locations based on your specific business needs.
Now Assist panel
The Now Assist panel is a user-facing interface, commonly accessed through the
context menu or chat interfaces. It provides quick access to agents' capabilities and
enhances productivity by summarizing records, creating content, and analyzing
alerts.
Tools
Tools equip your AI agents with the necessary capabilities to complete their tasks.
Adding a tool to an AI agent enables various functionalities and helps the AI agents
achieve their objectives.
How to put Now Assist AI agents to work
AI agents can use a variety of tools, such as web searches, record operations, and flows, to work
on agentic workflows that you define.
Navigate to All > AI Agent Studio > Overview > Get an overview of what to expect and select
View steps to see how you can successfully put your AI agents to work.
1.Create an agentic workflow: agentic workflows define the problem and situation that you want
your AI agents to work on. Without an agentic workflow, your agents don’t know when or what
to work on.
2. Create AI agents: AI agents use tools to execute tasks. Consider the tasks needed to solve the
agentic workflow you created. Create one or more agents to execute those tasks.
3. Test the agentic workflow: See how your AI agents perform. Make adjustments to either the
agentic workflow or AI agents. Test until everything’s working the way you want.
4.Deploy: Put your AI agents to work across your organization.

<!-- page 5 -->
AI agents configuration and execution
Now Assist AI agents have two components: AI agents and agentic workflows. By using Guided
Setup in AI Agent Studio, you create AI agents and workflows, add tools or define triggers, and
define the availability or display location. After they're created, you can duplicate, modify, and
test them in AI Agent Studio.
In run time, triggers in the primary and secondary interfaces cause agentic workflow execution,
where one or more AI agents execute the plan with the help of the AI agent Orchestrator to
accomplish the task. After agentic workflow execution, the output appears in the Now Assist

<!-- page 6 -->
panel. To learn more about an AI agent Orchestrator is, see the Understand the Now Assist AI
agents.
AI Agent Studio
Create, manage, or test AI agents and agentic workflows so that you can create self-executing
workflows to help you achieve your business goals.
https://player.vimeo.com/video/1096896405?
h=81ff7b3861&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479
AI Agent Studio overview
With the AI Agent Studio application, you can create, manage, or test AI agents and agentic
workflows all in one place. To enable the agentic AI experience, you must first install Now Assist
AI agents. For more information, see Install Now Assist AI agents.
The Overview page has three sections where you can find the information that you must
understand, begin, and continue developing AI agents and agentic workflows. When you first go
to the AI Agent Studio, tour points are available to guide you through the experience.
In the Ready-made agentic workflows and AI agents section, you can find the templates and
ready-made AI agents and agentic workflows that you can incorporate as-is or in custom
workflows that you create. You can even explore more templates to find the ones that best fit your
needs.
In the Recent agentic workflows and AI agents activity section, you can find the agentic
workflows or AI agents that have been created or configured most recently. On both List views,
you can create, duplicate, or delete agentic workflows or AI agents. The tab also includes a
link to the AI Agents Dashboard where you can review the details about AI agent usage and
performance.
The third section is a card to open a modal with a journey checklist that describes the steps to
incorporate the AI agents into your workflows successfully and a video that provides an overview
of the AI agents and workflows to get you started. Select View steps to open this section.
The following example shows the Overview page of AI Agent Studio.

<!-- page 7 -->
AI Agent Studio overview page
Managing agentic workflows and AI agents
From the AI Agent Studio Create and manage page, you can create, duplicate, or manage the
existing agentic workflows and AI agents. This page has two tabs, one for agentic workflows
and one for AI agents. You can edit the columns of the List view to change what information is
displayed. You can also search or filter the Lists to find the agentic workflows and AI agents that
you're looking for quickly. By selecting the name of the agentic workflow or AI agent, you can
open Guided Setup to configure or reconfigure the agentic workflow or AI agent.
The following example shows the AI Agent Studio create and manage page after several Now
Assist applications are installed.
AI Agent Studio Create and manage page
Agentic AI activity
The activity page contains execution logs for both agentic workflows and AI agents. The list
allows you to filter based on various fields, including the version. For more information on
creating multiple versions of the List of steps field, see Version control for AI agents and
agentic workflows.

<!-- page 8 -->
The following example shows several execution logs in AI Agent Studio.
AI Agent Studio activity page
Testing agentic AI
From the AI Agent Studio testing page, you can review the different tests for your AI agents and
agentic workflows, both manual and automated. You can test the performance of your agentic
AI by simulating a single execution manually, or you can use automated agentic evaluations for
testing multiple executions. Single tests are best for evaluating whether the AI agent or agentic
workflow does what you expect it to. Agentic evaluations are better at finding underlying patterns
and trends that may not be noticeable one execution at a time.
Note: The testing feature does not support the Now Assist panel assistance for live
agent interactions. To connect to a live agent, use Now Assist in Virtual Agent instead.
Otherwise, during live agent chat sessions, requester and agent users may be logged out
unexpectedly due to sessions expiring prematurely.
There are two types of manual tests you can do: AI agent or agentic workflow to
test execution or Test access to test security controls. You can view your executed tests in
the two tabs of the testing page. For manual execution tests, you can select the reply button to
repeat the test. You can open the full details page of an automated test by selecting the test's
name in the list in the Automated tab.
The following example shows the inputs for a Generate Resolution Plan agentic workflow testing
setup of AI Agent Studio.

<!-- page 9 -->
AI Agent Studio testing page
AI Agent Studio testing execution
AI Agent Studio settings
From the AI Agent Studio Settings page, you can enable Now Assist Guardian for your AI agents.
By using Now Assist Guardian, you can configure:
•Offensiveness detection
•Prompt injection attempt decision
•Long-term memory for AI agents
The following image shows the AI Agent Studio settings.

<!-- page 10 -->
AI Agent Studio settings page
AI Agent Analytics dashboard
From the AI Agent Analytics dashboard, you can review the vital statistics about your AI agents
and agentic workflows. You can see the data about the number of agents and agentic workflows
used, time-to-resolution efficiency gain, and the number of executions.
The following example shows the overview page for the AI Agent Analytics dashboard.

<!-- page 11 -->
AI Agent Analytics dashboard overview page
Understand the Now Assist AI agents
The Now Assist AI agents application is designed to securely leverage your data, workflows, and
integrations directly within the ServiceNow AI Platform. AI agents can dynamically adjust their
actions based on the progress and changing conditions of incidents or cases to help ensure that
they stay focused on achieving their objectives.
Now Assist AI agents Orchestrator
The AI Agent Studio guides users in leveraging AI agents effectively, while AI Orchestrator
ensures seamless collaboration among them. The AI agent Orchestrator is a central
management system that coordinates AI agents to ensure that they collaborate effectively to
complete complex workflows. It can also retrieve missing context from users when needed. AI
agents operate iteratively, seeking assistance from the Orchestrator if they encounter difficulties.
The Orchestrator enhances inter-agent communication and centralizes coordination. The
Orchestrator allows AI agents to share information effectively and transition tasks seamlessly,
regardless of where the process originates. As a result, the Orchestrator is essential for

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

<!-- page 21 -->
Step 2.1: Receive Incident Documentation:
Use Link Incident to Problem AI Agent to validate incident details and confirm no
existing problem linkage.
Step 2.2: Identify Relevant Problems:
•Execute search for relevant problems using incident short description.
•If no relevant problems found, inform the user: "No relevant problems found to
link." and proceed to Catalog Item Identification.
Step 2.3: Link Incident to Problem:
•Present most similar problem details to the user for approval.
•Upon user approval, link incident to problem using "Set problem to incident" tool;
confirm successful linkage to the user.
Step 3: Catalog Item Identification:
Identify and integrate relevant catalog items into the incident record.
Step 3.1: Receive Incident and Problem Context:
Use Find Catalog Item AI Agent to validate incident context and prepare for catalog
item search.
Step 3.2: Execute Catalog Item Search:
•Perform targeted search for relevant catalog items based on incident description.
•If no catalog items found, inform the user: "No relevant catalog items identified."
and proceed to final delivery.
Step 3.3: Integrate Catalog Item Details:
•Present catalog item choices to the user; upon selection, either add catalog item
details to incident additional comments or provide direct catalog item link.
•Confirm successful integration or delivery to the user and complete workflow.
Group Action Framework
Group Action Framework (GAF) is an intelligence feature on the ServiceNow AI Platform that
groups related records and applies actions to them using LLMs.
GAF overview
GAF is composed of two processes. The grouping process identifies clusters of similar records
(incident, cases, KB articles, etc.) and selects a set of representative records for the cluster.
The actioning process maps new records to clusters and executes large language model (LLM)
instructions for those clusters to achieve certain tasks, such as summarizing the contents of a
cluster or generating resolution steps based on steps that worked for records in that cluster. GAF
processes together benefit your AI agents and Now Assist generative features in multiple ways.

<!-- page 22 -->
•Improves consistency and quality of agentic and generative AI features by using the best
examples from groups of records.
•Reduces the cost of LLM calls by only executing on the representative records.
•Scales to accommodate large amounts of data because selected records can represent any
size cluster.
Skills used in GAF
Multiple skills are involved in GAF setup and execution. They are modular, so not all executions
will use all skills, but they can be used together in tandem. These skills are used exclusively for
GAF and currently cannot be included on their own in custom agentic workflows.
Grouping skill
Clusters related records using machine learning techniques.
Topic-labeling skill
Adds human-readable names to the clusters using an LLM to make the clusters
easier to identify.
Action strategy skill
Selects representative records from each cluster for the mapper and reducer skills
to use.
Action mapper skill
Runs LLM inference calls for the selected representative records, producing a
record summary for the selected records.
Action reducer skill
Uses the generated summaries created by the mapper skill to produce a single
summary for the entire cluster.
GAF and Now Assist in AI Search
GAF uses AI Search to improve its effectiveness and can use it as a fallback option in case GAF
does not return any results. GAF can work without Now Assist in AI Search, but if it is enabled
then GAF has optimized prediction. The optimized prediction feature increases clustering
capacity up to 500,000 records and improves recall speed.
See Install Now Assist in AI Search and Set up AI Search for Group Action Framework for more
information on configuring AI Search for GAF.
Version control for AI agents and agentic workflows
Version control enables you to track changes made to instructions sent to the LLM for AI agents
and agentic workflows.
Version control overview
When creating an AI agent or agentic workflow, the List of steps field is important because
it provides the context necessary for the large language model (LLM) to accomplish tasks. You
can use version control to create multiple versions of the List of steps field in the guided
setup. Tracking your changes with version control helps enable you to experiment and test new
instructions. You can create versions, edit and refine versions, and revert to previous versions as
needed.

<!-- page 23 -->
Version control modal
Creating versions
You can create a version by selecting View versions > New version in the guided setup of an
AI agent or agentic workflow. Doing so brings up the Create a new version modal where
you can name the version and make changes. Naming your version enables you to identify what
changes were made to make it easier to track.
You can choose to make the new version active immediately by selecting the Set as active
toggle.
For more information about writing effective descriptions and instructions, see General
guidelines for creating AI agents and agentic workflows.
When creating a new version, you also have the option to use Now Assist to refine your current
List of steps. You must already have an active version for this option to be available.
Selecting View versions > Refine version brings up the modal where Now Assist generates and
displays a new List of steps for you to review. You can change any of the generated text, or
you can use it as it was generated. Select Create to use the new, refined version.

<!-- page 24 -->
Create a new version modal
Changing between versions
When you have multiple versions of the same List of steps field, you can switch which one
is active at any time. Choosing to make a new version active enables you to test it and evaluate
its effectiveness.
If you’re updating an agentic workflow, you can execute an agentic evaluation run to measure
performance.
You can decide which version is active by selecting View versions in the guided setup. Toggle
the Set as active field and save your changes to make the new version active.
Testing different versions
You can test different versions of an agentic workflow or AI agent from the AI Agent Studio
Testing page. The Version selector dropdown displays both active and inactive versions with
the currently active version marked as (Active). You can also start evaluation runs for specific
versions by selecting Set up evaluation run.

<!-- page 25 -->
Version selector in the AI Agent Studio Testing page
Version logs
The AI Agent Studio Activity page enables you to track AI agent and agentic workflow executions
by version. When in the guided setup, you can select View version logs in the View all
versions modal. Choosing to view the version logs opens the Activity tab in a new window
with the list filtered for the version you selected.
When viewing the Activity tab at any time, you can choose to filter by version. The more specific
your version names, the easier it is to identify those changes in the list.
Example execution logs
AI agent learning
Enhance AI agent learning through episodic memory, enabling agents to improve by learning
from past successful interactions.
Episodic memory overview
The episodic memory represents historical experiences and their associated learnings in the
form of feedback. It's the ability to reflect on and learn from them by applying memory of similar

> **[Diagram: AI agents configuration and execution flow]**
> Two-panel architecture diagram on a white background.
>
> **Top panel — "Configure Now Assist AI Agents"** (dark green header bar): Two parallel vertical flows side by side.
> Left flow (AI Agent path): "Create AI agent" (teal rounded box) ← arrow from "AI Agent Studio" (bold black box, centre) → "Create agentic workflow" (green box, right). Below "Create AI agent": "Add tools" (teal) → "Define trigger" (teal) → "Define availability" (teal) → with a branch left to "Clone AI agent" (orange box) and "Virtual Agent" (white/outline box) → "AI agent created" (orange/amber box). From "AI agent created" branches left to "Modify / Delete AI agent" (orange), right to "Test AI response (optional)" (teal) → "Orchestrator in action" (white outline) → "Response (view AI agent processing steps using the tools defined)" (teal).
> Right flow (Agentic workflow path): "Create agentic workflow" → "Define trigger" → "Define availability" → "Now Assist panel" (white outline) with annotation "Agentic workflow uses one or more AI agents" → "Agentic workflow created" (orange). Branches: "Clone agentic workflow" (orange right), "Modify / Delete agentic workflow" (orange right), "Test AI response (optional)" → "Orchestrator in action" → "Response (view agentic workflow processing steps using the instructions defined)" (teal).
>
> **Bottom panel — "AI Agents at work"** (dark navy header bar): Three columns connected by arrows: "Triggers" column (white box) containing two icons — person/Primary Interface and database/Secondary Interface → arrow to "Agentic workflow execution" (green box: "Orchestrator coordinates with AI agents to ensure that they collaborate and complete complex workflows") → arrow to "Result" column containing "Task accomplishment" (green box).

> **[Screenshot: AI Agent Studio overview page]**
> Full-width screenshot of the AI Agent Studio overview page. Navigation bar shows "servicenow" logo, All, Favorites, History, Workspaces, Admin, and centred "AI Agent Studio ★" badge with search bar and icons. Secondary tab bar: Overview (active underlined), Create and manage, Testing, Settings. Top-right button: "Manage evaluation runs ↗".
>
> Page title "AI Agent Studio" with subtitle "Create, manage, and monitor agentic workflows and the AI agents working across your organization." An animated graphic with nodes/connections appears at top right. A "Preview" badge with "Introduction to agentic AI" video thumbnail and "Take tour / View steps" buttons appear on the right.
>
> "Ready-made agentic workflows and AI agents" section with "Explore all" button. Two visible AI agent cards: "Problem Investigator" – "The Problem Investigator Agent specializes in root cause identification, impact assessment, and remediation planning." and "Incident trends analyser" – "Analyses grouped incident data to identify recurring issues and root causes. Provides detailed, actionable recommendations using structured analyses."
>
> "Recent agentic workflows and AI agents activity" section with "View analytics ↗" link. Two tabs: "Agentic workflows" and "AI agents". List table with columns: Name, Description, AI agents, Date created. Four rows: "Investigate IT problems" (1 agent, 2025-02-10), "Suggest survey responses" (2 agents, 2025-02-10), "Analyze incident trends" (1 agent, 2025-02-19), "Analyze and improve services" (2 agents, 2025-02-19). "View all" link bottom-right.
>
> **[Screenshot: AI Agent Studio Create and manage page]**
> The "Create and manage" tab showing "Manage agentic workflows and AI agents" with subtitle and two tabs: "Agentic workflows" (selected with badge "8") and "AI agents". "New" teal button top-right. List columns: Name, Description, AI agents, Created by, Date updated, Date created. Four workflows listed: Investigate IT problems, Suggest survey responses, Analyze incident trends, Analyze and improve services, each with same metadata. Pagination showing "1 – 4 of 4", Records per page: 20.

> **[Screenshot: AI Agent Studio activity page — execution logs]**
> The Activity tab of AI Agent Studio showing "View agentic workflow and AI agent activity" with subtitle. "All executions 189" counter shown. Filter/refresh/settings icons top-right. Table columns: Created, Created by, State, State Reason, Run Type, Agentic workflow, AI Agent, Objective, Version, Replay. Seven rows visible:
> - 2025-06-24 04:14:37 | abel.tuter | Completed | | Testing | Default VA Workflow | (blank) | i want to add notes | V1 | ○
> - 2025-06-24 08:38:40 | admin | Completed | User has requested to end the conversati | Chat | Default VA Workflow | (blank) | incident_details: INC0009005 | (blank) | ○
> - 2025-06-25 09:40:53 | abel.tuter | Terminated | No Activity | Testing | (blank) | IT Ticket Agent | Create IT Ticket | (blank) | ○
> - 2025-06-25 03:42:54 | fred.luddy | Completed | | Testing | (blank) | KB content consolidation AI agent | consolidate article 0000010 try to prefix with KB | (blank) | ○
> - 2025-06-25 04:16:00 | admin | Completed | | Testing | Triage cases | (blank) | table is interaction and recordid is IMS0000002 | V1 | ○
> - 2025-06-25 01:39:28 | beth.anglin | Completed | | Testing | (blank) | Next Best Action Agent | Solve INC0009005 | (blank) | ○
> - 2025-06-25 03:01:15 | beth.anglin | Completed | | Testing | (blank) | IT Ticket Agent | Update incident INC00091021 | V1 | ○

> **[Screenshot: AI Agent Studio testing page]**
> The Testing tab. Title "Test how agentic AI performs." Subtitle "Give AI agents and agentic workflows real tasks to complete and see if they provide the expected results." Two side-by-side option cards: "Manual test" (icon with clock/settings) – bullet points: gain insight, view decision log, Good for: testing a single example. "Start manual test" teal button. "Automated evaluation" (icon with chart/arrows) – bullet points: assess performance at scale, aggregate results for task completion and tool choice accuracy, Good for: testing a pattern of behavior. "Start automated evaluation ↗" button.
>
> "Track test results" section with "Manual tests" and "Automated tests" tabs. Filter and refresh icons. Table columns: Created, Created by, State, State Reason, Agentic workflow, AI Agent. Two rows: 2025-11-13 09:51:14 | abel.tutor | Completed | No Activity | (blank) | Incident Details Agent; 2025-11-13 11:36:04 | abraham.lincoln | Completed | (blank) | (blank) | Skill Details.
>
> **[Screenshot: AI Agent Studio testing execution detail — dual-panel view]**
> Split-screen view of a test execution in progress. Left panel shows breadcrumb "Testing Home > Test Details > Manual Test" and a vertical "steps" list: Created a plan, Started AI Agent 'Next action recommendation AI agent', Used the tool 'Get record details', Optimised results, Checking on remaining steps. A "Processing…" status with gear icon at bottom. Centre panel shows a flow diagram with nodes: Task Start (circle with target icon) → Orchestrator (gear/cog icon) → Next action recommendati… (AI Agent node) → Get record details (Tool node). Panel includes "Find on map ×" button and zoom/fit controls. Right panel shows "AI agent decision logs" with expandable entries: Access verification (Completed), Orchestrator (Completed), Gen AI – AIA ReAct Engine (Completed), Next action recommendation AI agent (Ongoing), Gen AI – AIA ReAct Engine (Completed), Tool – Get record details (Completed), Orchestrator (Queued). Green/amber/grey status badges.

> **[Screenshot: AI Agent Studio settings page — Now Assist Guardian Offensiveness]**
> The Settings tab of AI Agent Studio. Left sidebar navigation shows two sections: "Now Assist Guardian" (expanded, with sub-items: Offensiveness (selected/highlighted in blue), Prompt Injection, Long-term memory) and "External AI agents" (expanded, with sub-items: Discoverability, Data access, Manage MCP servers, Model provider). Main content area breadcrumb: "Settings > Now Assist Guardian: Offensiveness". Page title "Offensiveness". Description: "Detect and monitor content created with generative AI in conversational experiences that may include offensive material, such as toxicity, profanity, or sexism." A toggle row: "Offensiveness ON" with a blue toggle (enabled). Text: "Offensiveness is turned on for all AI Agents." A "Detection Impact" section shows "Log only" (current setting, shown as a dropdown/selector with a "⋮" menu). Right sidebar shows "Helpful resources" with links: Now Assist Guardian ↗, Now LLM Service model cards ↗, ServiceNow AI Forum ↗. FAQs section with three expandable items.

> **[Screenshot: AI Agent Analytics dashboard overview page]**
> Full-width dashboard screenshot titled "AI Agent Analytics" with subtitle and tab bar: Overview (active), Status, Insights, Assist consumption, Performance, Troubleshooting, Security. Edit button top-right.
>
> "Summary" section with three KPI cards in a row: (1) "Average inferred CSAT for AI agents in last 7 days" – gauge chart showing needle at 3.00 on a 1.00–7.00 scale. (2) "Execution tasks in last 7 days" – donut chart with legend: Success (dark), Ongoing (medium), Cancelled (light), Queued (lightest). (3) "AI Agent errors in last 90 days" – small line chart with x-axis showing week labels (W2 2025 through W13 2025+) and a "Errors" legend.
>
> Three more charts in a second row: "AI agent tool type" – donut chart with legend segments: Script, Flow Action, Subflow, Task, Capability, Model Control. "AI agent tool execution mode" – donut chart with legend: Autonomous, Supervised (disabled), Supervised (supervised). "Execution plans in last 7 days" – donut chart with legend: Successful, Terminated, Abandoned.
>
> "AI agent executions" table with columns: By AI agent & By AI agent execution status, W13 2026, W12 2026, W11 2026, W10 2026, W9 2026, W8 2026, W7 2026, Change (Change %), Trend (sparkline). Ten rows including ITSM incident resolution investigation AI agent (11 executions W13), Instruction Refinement AI agent (8), Performance analysis AI agent (8), Find catalog item AI agent (2), Dodgen Super Fan (2), Zoom Issue Agent (2), Addition AI Agent (0), Demo Next Best Action Agent zp1 (0), Technology for New Hire Agent EXT (0), Incident knowledge article AI agent (0). Each row has a sparkline trend line on the right.
>
> "What's going on with your AI agents over time?" section with three KPI tiles: "Number of agentic workflows: 46 — 0 (0.0%) since March 31", "Number of AI agents: 152 — 0 (0.0%) since March 31", "Number of tools: 399 — 0 (0.0%) since March 31". Below: "AI agent execution plans" table with rows: Generate Resolution Plan (0 across all weeks), Help resolve IT requests (0), Help resolve tuition requests (Capd) (0), HR workflow (0).

> **[Screenshot: Version control modal — View all versions]**
> A modal dialog titled "View all versions" with an X close button. Left sidebar shows four section tabs with radio buttons: "Section 8" (selected, filled circle), "Section 6" (empty circle), "Add sections" (empty), "Expertise" (filled/dot indicating active). Main content area shows fields: "Version number: 4", "Updated by: abel.tuter", "Updated on: 6/26/2025", and a "Set as active" toggle (currently off). "Version name *" field contains "Section 8". "List of steps * ⓘ" with "Instruction for LLM" link top-right. A multi-line text area shows: "Section 1: Incident Logging / 1. Create a new incident record in the system. / 2. Enter the date of the incident… / 3. Enter the time… / 4. Enter a description… / 5. Enter the reporter's information… / 6. Assign a unique identifier… // Section 2: Incident Assignment / 7. Identify the type of issue reported…" (text truncated). Footer buttons: "View version logs ↗" link (left), "Cancel" and teal "Save" buttons (right).

> **[Screenshot: Create a new version modal]**
> Modal dialog titled "Create a new version" with X close button. Fields shown: "Version number: 2", "Created by: abel.tuter", "Created on: 6/24/2025", and "Set as active" toggle (ON, blue). "Version name *" field contains "New Section 8". "List of steps * ⓘ" with "Instruction for LLM" link top-right. Same multi-line steps text area as View all versions modal, showing Section 1: Incident Logging (steps 1-6) and beginning of Section 2: Incident Assignment (step 7). Footer: "Cancel" and teal "Create" buttons.