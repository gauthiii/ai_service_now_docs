# Add a trigger to an AI agent

_Source pages: 99–103 | Depth: 2_

---

<!-- page 99 -->
If you select AI user, the list of roles that the AI user has is displayed.
Result
You have created an ACL that determines who can discover and access your AI agent, and you
have assigned a user identity (and role masking, if relevant) to the AI agent to determine what
data it can access.
What to do next
Select Save and continue to move to the next step, Adding a trigger. Adding a trigger is optional.
You can also skip to the final step, Select channels and access.
Add a trigger to an AI agent
In the guided setup for an AI agent, add triggers to run the AI agent automatically when certain
conditions are met.
Before you begin
Role required: sn_aia.admin
About this task
Adding a trigger is optional. If you want your AI agent to be used only in chats, you don't need
to add a trigger. Only add a trigger if you want to invoke the AI agent automatically when some
event occurs.
Note: Triggers contain instance-specific information. If you are moving AI agents or
agentic workflows between instances using Update Sets, you must set the triggers to
inactive before adding them to the update sets and then activate them on the new instance.
If you don't want to add a trigger, skip to the final step, Select channels and access.
Procedure
1.Select Add trigger.
2. On the form, fill in the fields.
Create a new trigger
Fields Description
Select trigger List of triggers that are available in the
instance.
Name Name of the trigger.

<!-- page 100 -->
Fields Description
Trigger objective Additional user statements or sample
utterances that help guide when to trigger
this agentic workflow.
Define when this trigger occurs
Fields Description
Table Name of the applicable table for your agentic
workflow.
Conditions Conditions that you can add to control the
trigger configuration. You must have at least
one condition.
Select + Add condition set to add conditions
to your agentic workflow trigger.
Active trigger toggle Only enable the trigger once you’re confident
in the execution of your AI agent. Try testing
the AI agent execution and user access. To
review overall trends over many executions,
try an automated evaluation.

<!-- page 101 -->
Select where to show this launch
Fields Description
Channel
Medium for the agentic workflow output: Now
Assist panel or Virtual Agent.
Note: To view the output from a
triggered agentic workflow in the
Now Assist panel, you need the
now_assist_panel_user role.
Show an alert to users Alerts appear in the selected channel.

<!-- page 102 -->
If you choose a scheduled trigger, additional options are available, such as the day of the week
and time when you want the trigger to run.
Note: When running a scheduled trigger, not every record is included in the execution.
By default, the value is 10. If you want to change this number, you must set the
sn_aia.max_scheduled_trigger_query system property to a different value.
If you choose an email trigger, the target emails must exist on the Reply [sys_reply] table.
New emails aren’t available as triggers.
3. Select Add.
4.Repeat the preceding steps for additional triggers.
Result
You have added triggers to your AI agent to run it automatically under the specified conditions.
What to do next
Select Save and continue to move to the final step, Select channels and access.
Kill Switch in Now Assist AI Agents
The kill switch feature detects and stops runaway AI agent triggers that execute repeatedly
against the same records, preventing unnecessary consumption of Now Assist interactions.
Kill Switch Overview
An AI agent trigger can match the same record multiple times within a short period during
executions. When left unchecked, a misconfiguration trigger condition can process the same
incident five or more times per day, across dozens of records, for several consecutive days. Each
trigger activation spawns a conversation and consumes assists, resulting in charges for activity
that provides no customer value.
The kill switch feature detects when the same record is triggering the same agent objective
beyond a threshold in a single day and automatically disables the agent. It monitors trigger

<!-- page 103 -->
activity, issues tiered alert notifications to trigger and agent owners, and optionally disables the
trigger automatically after a configurable breach threshold is reached.
Default detection thresholds
The kill switch evaluates trigger activity against the following default thresholds. All thresholds
are configurable by users through system properties:
•Fires per record per 24-hour window: 5
•Distinct records breaching the threshold: 25
•Consecutive days of breach before action: 3
Five tunable system properties control these thresholds and the feature's operating mode:
•kill_switch.mode: Default value: warn_only. For the different operating modes the
property contains, see Operating modes.
•kill_switch.max_fires_per_window: Fires per record that mark it as breaching.
Default value: 5.
•kill_switch.min_distinct_records: Breaching records needed for the window to
count as runaway. Default value: 25.
•kill_switch.window_size: Length of one observation window. Default value: 1440
min / 24h.
•kill_switch.consecutive_windows_duration: The total look back span. Default
value: 4320 min / 3 days.
Architecture
The kill switch uses two fully decoupled execution paths.
Trigger activation path
Runs on every conversation start. When a trigger matches a record and fires, an
audit row is written to the audit table before the conversation begins. Audit writes
never interrupt or fail the user's conversation.
Evaluator path
A scheduled job runs once daily. It reads the audit table, computes a cycleStart
date, and assigns each active trigger a stage value (K) from 0 to 3 based on the
number of consecutive days the trigger has breached the threshold. If K is 1 or
higher, the evaluator sends a warning email. If K reaches 3 and enforce mode is
active, the evaluator also disables the trigger.
Note:
•Warning emails are sent to the trigger creator and to the creators of any agents or
workflows associated with the trigger. Alerts follow the same notification mechanism used
for all existing Now Assist alert purposes.
•Re-enabling an inactive trigger resets the cycle, so the next evaluator run treats the
trigger as a fresh Day 1.
Operating modes
The kill_switch.mode system property controls how the feature responds to a detected
breach.
off

> **[Screenshot: Edit a trigger modal]**
> A modal titled "Edit a trigger" with X close button. Fields: "Select trigger *" dropdown showing "Updated". "Create a new trigger" section (expanded with ∧ chevron): "Name *" field containing "Solution accepted"; "Trigger objective * ⓘ" text area containing "Add a work note to \${number} with, summarized final accepted solution" with a language/settings icon; "Trigger is OFF" toggle (grey/disabled). Footer: "Cancel" and teal "Save" buttons.