# Select channels and status for an AI agent

_Source pages: 104–105 | Depth: 2_

---

<!-- page 104 -->
Audit rows are still written, but the evaluator performs no detection, sends no
warnings, and never disables triggers.
warn_only
The evaluator sends a daily warning email for each day the breach pattern is
present. Triggers are never inactive. This is the shipped default.
enforce
The evaluator sends the same tiered warnings on Days 1 and 2. On Day 3, it sends a
final warning and deactivates the trigger configuration, including associated many-
to-many and override rows.
Escalation sequence
In warn_only or enforce mode, the evaluator sends progressively stronger email
notifications as the breach continues.
•Day 1 — Early warning: [1 of 3] Action Recommended — Trigger Firing at Unusual Rate
•Day 2 — Stronger warning: [2 of 3] Action Required — Trigger Has Been Firing at High Volume
for 2 Consecutive Days
•Day 3 — Final warning (enforce mode also disables): [3 of 3] Trigger inactive — High Volume
Detected for 3 Consecutive Days
Each email includes the agent name, trigger name, affected record count, and a direct link to the
trigger configuration.
Select channels and status for an AI agent
In the guided setup for an AI agent, activate the AI agent to use in an assistant in Now Assist for
Virtual Agent, and set the processing messages.
Before you begin
Role required: sn_aia.admin
About this task
The final step of the AI agent guided setup includes options for where you can invoke the agentic
workflow as well as set the processing message. You must select which assistants for Now Assist
in Virtual Agent you want to be able to invoke the AI agent. Your processing messages appear
when the AI agent is running and when the AI agent's task is completed.
Procedure
1.Select whether you want users to use Now Assist in Virtual Agent to invoke the AI agent.
If enabled, you must select which chat assistants have access to the AI agent. You can edit
assistants using Assistant Designer.
2. Optional: Set the processing and completion messages for your AI agent.
(Optional) You can set a processing message, completion message, or both. If you don't want
to use a specific type of message, unselect the toggle next to the message field.
You can also use Now Assist to generate the messages for you by selecting Generate
messages. You can change the messages after they're generated.

<!-- page 105 -->
3. Activate the AI agent.
Select the This AI agent is active toggle to activate the AI agent only when you want users to
be able to use it. If you want to test your AI agent first, wait until after you have tested it before
activating it. You can return to the guided setup later.
If you don't see this option, you may need to scroll.
Note: If you have installed the Off Glide Conversation Server plugin
(com.glide.cs.offglide) on your ServiceNow AI Agent Studio instance, then agent learning
and voice agents won't work if the assistant is in Premium Chat mode.
4.Select Save and test.
Result
You have completed the guided setup for creating an AI agent. Your new AI agent can be edited
at any time using AI Agent Studio.