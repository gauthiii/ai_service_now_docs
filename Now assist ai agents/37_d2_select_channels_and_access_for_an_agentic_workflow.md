# Select channels and access for an agentic workflow

_Source pages: 128–129 | Depth: 2_

---

<!-- page 128 -->
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
You have added triggers to your agentic workflow to run it automatically under the specified
conditions.
What to do next
Select Save and continue to move to the final step, Select channels and access.
Select channels and access for an agentic workflow
In the guided setup for an agentic workflow, activate the agentic workflow to use in the Now
Assist panel or UI actions in the Core UI and workspaces.
Before you begin
Role required: sn_aia.admin
About this task
The final step of the agentic workflow guided setup includes options for where a user can invoke
the agentic workflow. The Now Assist panel is available to users with the correct role. You can
specify the exact conditions when a UI action is available to users on a table.

<!-- page 129 -->
Procedure
1.Select whether you want users to use the Now Assist panel to invoke the agentic workflow.
2. Optional: Add a UI action to your agentic workflow.
a.Select Add UI action.
b.Enter the UI action label.
(Optional) The UI action label is the text that the user sees in the button on the table.
c.Select a table where the UI action can be used.
(Optional) Users who are accessing a record on the selected table can view the UI action
in the Core UI and workspaces. See In-product agentic AI for more information about the AI
Workflows panel.
d. Specify conditions for the UI action to appear and select Add.
(Optional) For example, you could only show a UI action for a Generate resolution plan
agentic workflow if the record state is Active.
Note: The display for a new UI action is turned on by default.
(Optional)
3. Select Save and test.
Result
You have completed the guided setup for creating an agentic workflow. Your new agentic
workflow can be edited at any time using AI Agent Studio.