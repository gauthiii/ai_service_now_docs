# Add a trigger to an agentic workflow

_Source pages: 125–127 | Depth: 2_

---

<!-- page 125 -->
Note: Role masking should be applied as security general guidelines and adherence
to the principle of least privilege. Overriding the role masking requirement isn’t
recommended.
If you select AI user, the list of roles that the AI user has is displayed.
Result
You have created an ACL that determines who can discover and access your agentic workflow,
and you have assigned a user identity (and role masking, if relevant) to the agentic workflow to
determine what data it can access.
What to do next
Select Save and continue to move to the next step, Adding a trigger. Adding a trigger is optional.
You can also skip to the final step, Select channels and access.
Add a trigger to an agentic workflow
In the guided setup for an agentic workflow, add triggers to run the agentic workflow
automatically when certain conditions are met.
Before you begin
Role required: sn_aia.admin
About this task
Adding a trigger is optional. If you want your agentic workflow to be used only in chats such as
in Now Assist for Virtual Agent or Now Assist panel, you don't need to add a trigger. Only add a
trigger if you want to invoke the agentic workflow automatically when some event occurs.
Note: Triggers contain instance-specific information. If you are moving AI agents or
agentic workflows between instances using Update Sets, you must set the triggers to
inactive before adding them to the update sets and then activate them on the new instance.
If you don't want to add a trigger, skip to the final step, Select channels and access.
Procedure
1.Select Add trigger.
2. On the form, fill in the fields.

<!-- page 126 -->
Create a new trigger
Fields Description
Select trigger List of triggers that are available in the
instance.
Name Name of the trigger.
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
in the execution of your agentic workflow.
Try testing the agentic workflow execution
and user access first. To review overall trends
over many executions, try an automated
evaluation.

<!-- page 127 -->
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