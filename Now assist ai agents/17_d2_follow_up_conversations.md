# Follow-up conversations

_Source pages: 48–48 | Depth: 2_

---

<!-- page 48 -->
Follow-up conversations
AI agents continue with follow-up conversations after the AI agent execution is complete.
Before you begin
Role required: sn_aia_admin
About this task
When the [sn_aia.enable_follow_up] system property is set to true and if there is no record
for the agentic workflow created in the Agent properties [sn_aia_property] table, then the AI
agents continue with the How else can I help you? follow-up message after the agentic
workflow execution.
The AI agent conversation doesn't get closed after the execution is complete by default. If you
would like to override the follow-up behavior for your AI agents for a specific agentic workflow,
you must create a record in the Agent Properties [sn_aia_property] table.
Procedure
1.Navigate to All > System Definitions > Tables and open the Agent Properties [sn_aia_property]
table.
2. Select New.
3. On the form, fill in the fields.
Agent Property form
Field Description
Name Name for the agent property record for the
agentic workflow.For example,
follow_up_behaviour
Value Provide the following values as per the
requirement: