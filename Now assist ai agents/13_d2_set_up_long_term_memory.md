# Set up long-term memory

_Source pages: 35–38 | Depth: 2_

---

<!-- page 35 -->
3. Select Configure to be redirected to Now Assist Admin.
4.In the Choose a default model provider field, select from the following choices.
◦Now LLM Service
◦AWS Claude
◦Azure OpenAI
◦Google Gemini
◦Amazon Bedrock
The new generative AI Config property records sys_generative_ai_config and
sys_generative_ai_prompt_config have been introduced for the following model
providers:
◦Amazon Bedrock: claude-sonnet-4-6
◦Azure OpenAI: gpt 5.4
Both the properties share a definition field that references the same
sys_one_extend_capability_definition record, which identifies the LLM provider.
Note: THe new prompt config records are set to true by default.
5. To use a different model provider:
a.Navigate to the sys_generative_ai_prompt table.
b.Filter and group by the relevant skill definition.
c.Locate the record for the appropriate skill and provider.
d. Set the preferred record as default.
6.Review the impacted AI agents.
Certain AI agents may require specific model providers. Select the AI agents tab in the Impact
overview section to see which AI agents are affected by any changes to the model provider.
7.Select Save.
Result
Your chosen LLM is used globally for all AI agents and agentic workflows.
Set up long-term memory
Make AI agents remember your preference or facts from previous interactions and use memories
for more focused conversations.
Before you begin
Role required: sn_aia.admin
Procedure
1.Navigate to All > AI Agent Studio > Settings.
2. Select Long-term memory.

<!-- page 36 -->
3. Configure the User facts and preferences.
a.Turn on the Allow all AI agents to retain user information using the toggle button.
b.Turn on the Allow all AI agents to apply their knowledge in conversations using the toggle
button.
c.Turn on the Allow an LLM to identify categories of memories using the toggle button.
d. To view the existing categories of memories, select View.
e. To view the relationships or mappings between AI agents and categories, select View.
4.Configure Past executions outcomes by turning on the Allow all AI agents to learn from past
executions using the toggle button.
When you want to turn off agent learning from past executions, you will see a confirmation pop
up. Selecting Disable will disable agent learning.

<!-- page 37 -->
Long-term memory categories
Long-term memory (LTM) categories define the types of semantic information that a Now Assist
AI agent can learn and retain about users over time. You can add new categories and map them
to specific agents to personalize agent responses based on accumulated user context.
Semantic memory in the AI agent Memories table (sn_aia_memory_list) is organized by
LTM categories. Each category represents a distinct type of user-specific information, such as
software preferences, workplace context, or communication style. By mapping categories to an
agent, you control what the agent learns and retains across interactions.
How LTM categories work
When an agent executes, the platform evaluates the interaction for user-specific facts that match
the agent's configured LTM categories. Matched facts are stored as semantic memory records in
the AI Agent Memories [sn_aia_memory] table, scoped to the user and category. On subsequent
interactions, the agent retrieves relevant semantic memories and uses them to personalize its
responses without requiring the user to repeat context.
LTM categories are defined globally and can be mapped to one or more agents. An agent only
learns and retrieves memories for the categories explicitly mapped to it.
Default LTM categories
The platform includes the following default LTM categories:
Software and tools
Captures information about applications, tools, and software configurations relevant
to the user, such as operating system version or approved applications.
Work context
Captures facts about the user's role, department, location, and workplace
preferences, such as remote work setup or team structure.
User preferences
Captures communication preferences and interaction style, such as preferred
language, response format, or notification settings.
You can extend this list by creating custom categories suited to your organization's use cases.
How categories affect memory extraction
During memory extraction, the platform runs an LLM prompt that evaluates the agent interaction
against the descriptions of each mapped LTM category. If the interaction contains information
that matches a category, a semantic memory record is created or updated in the AI Agent
Memories table with the following fields:
Category
The LTM category that the memory is associated with.
User
The user whose interaction generated the memory.
Memory
The extracted user-specific fact, stored as a JSON object.
Type
Set to Semantic for category-based memories.

<!-- page 38 -->
Semantic memories are retrieved at runtime using retrieval-augmented generation (RAG) and
injected into the agent prompt to personalize the response for the current user.
Considerations
•Category descriptions directly influence LLM extraction quality. Use specific, unambiguous
language to reduce false positives or missed extractions.
•Mapping too many categories to a single agent can increase extraction processing time. Map
only the categories relevant to the agent's use case.
•To verify that semantic memories are being extracted, open the AI Agent Memories table and
filter by Type = Semantic and the relevant agent or user.
Create long-term memory category
Add a long-term memory category to add it an AI agent while setting up long term memory
Before you begin
Role required: sn_aia.admin
Procedure
1.Navigate to AI Agent Studio > Settings > Long-term memory.
2. Select View All against View the existing categories of memories.
3. On the AI Agent Memory Categories page, select New.
4.On the form, fill in the fields.
Field Description
Name A descriptive label for the category,
such as Hardware preferences or
Accessibility needs.
Description A brief explanation of what type of user
information this category captures.
The description is used by the LLM extraction
prompt to identify relevant facts during agent
execution, so precise language improves
extraction accuracy.
5. Select Save.
After saving the record, the category is activated by default and is available to map to one or
more AI agents.
Map long-term memory category
Map the created long-term memory category to the agents that should use it. Categories must be
mapped individually to each agent; they are not applied globally by default.
Before you begin
Role required: sn_aia.admin
About this task
The mapping of LTM categories is done directly while creating an AI agent at the Define the
specialty page.