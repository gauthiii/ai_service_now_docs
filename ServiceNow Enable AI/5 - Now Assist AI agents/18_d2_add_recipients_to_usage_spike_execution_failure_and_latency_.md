# Add recipients to usage spike, execution failure, and latency error email notifications

_Source pages: 49–49 | Depth: 2_

---

<!-- page 49 -->
Field Description
◦no_followup_close_conversation: Closes
the conversation after the use case is
complete.
◦no_followup_open_conversation: Keeps
the conversation open after the use case is
complete.
Target table The table where the target agentic workflow
resides: Agentic workflows [sn_aia_use case]
table.
Target record The record of the target agentic workflow or
AI agent.
Application The application scope for the agent property
record: Now Assist AI agents.
4.Select Submit.
Add recipients to usage spike, execution failure, and latency error email
notifications
Add or change recipients to email notifications triggered by unexpected or undesired behavior in
AI agent and agentic workflow executions.
Before you begin
Set your application scope to Now Assist AI Agents.
Role required: admin
About this task
There are different email notifications that can be configured: one for Assist usage spikes, one
for failed AI agent executions, and two for latency errors. The properties for configuring the
thresholds for sending these notifications can be found in the Now Assist AI Agents Reference.
Procedure
1.Navigate to All > System Notification > Email > Notifications.
2. In the Name field, search for AI Agent, and select the notification you want to edit.
There are different Notifications records for the different sources of alert. If you want to change
the recipients for all types of alerts, you must edit each of the Notification records individually.
3. Open the Who will receive tab.
4.Select the unlock icon for the type of recipient you want to add or change.
To quickly add yourself to the list of recipients, select the Add me icon next to the Users field.
5. Select the users and groups you want to receive email alerts.
If you select Send to event creator, the owner of the AI agent or agentic workflow that triggered
the alert receives a notification.