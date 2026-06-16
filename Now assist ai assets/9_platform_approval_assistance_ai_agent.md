# Platform Approval assistance AI agent

*Source: document pages 111–112 (PDF chunk pages 11–12)*

---



<!-- doc page 111 -->

Platform Approval assistance AI agent
The Approval assistance AI agent is an AI agent that enables you to see your list of pending
approvals, as well as see the details about your pending approvals. You can then approve or
reject requests and tickets from Now Assist in Virtual Agent.
Approval assistance AI agent overview
Roles required: approver_user, sn_request_approver_read
Note: Add the necessary roles to enable reading of other tables whose records go
through the approval process. For example, you can add the sn_change_read role to read
Change Request records.
The benefit of using the Approval assistance AI agent is that you don't need to navigate to a
specific page to approve your tickets. You can ask the AI agent about your pending approval
requests and then tell the AI agent to approve or reject those approvals. The AI agent will ask
follow-up questions and offer context-aware responses to simplify your experience.
Ask you administrator to configure the display fields and the knowledge base (KB) search fields
to generate a Gen AI checklist to assist the Approval assistance AI agent in making targeted
decisions. The checklist uses KB articles and policies to assist the Approval assistance AI
agent in decision making. The checklist fetches information from knowledge base articles about
specific requester approval tickets. An approval_admin and admin role are required to configure
the Approval assistance AI agent. For more information, see Configure Service Portal Approval
Configuration record .
Note: Provide cross-scope privileges to the Now Assist Agents for Requester plugin
for tables whose records are restricted within the scope of an application. For more
information, see Define cross-scope access to an application resource .
Prerequisites and setup
To access this AI agent, you must have Now Assist Agent for Requester (version 3 of the standard
plugin) installed on your instance, which is installed with Now Assist for Platform. You can get
Now Assist for Platform when you install any other Now Assist application, such as Now Assist for
IT Service Management (ITSM).
The Approval assistance AI agent displays data from the Approvals [sysapproval_approver]
table. If the user has been assigned to approve a request, the approval record is shown.
Role masking
Required role:
Role masking enables users to limit the roles and privileges of AI agents during tool execution.
AI agents that get installed with Now Assist applications are assigned pre-defined roles. If you
select Users with specific roles for user access, you must configure the security
controls to include these roles. Data access settings must also include these roles. For the
instructions to change the security controls, see Define security controls for an AI agent.
In the data access settings, you must also add the necessary roles to enable reading of the
tables for the records you want to evaluate for readiness. For example, you can add the itil role to
the AI agent's list of approved roles so that it can access Incident records.
Accessing the Approval assistance AI agent
To access the AI agent:

ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.


<!-- doc page 112 -->

1.Navigate to All > AI Agent Studio > Create and manage.
2. Go to the AI Agents tab.
3. Select Approval assistance AI agent.
Sample utterances
After the agent has been activated in AI Agent Studio, enter phrases such as the following or
similar queries to run the AI Agent in Virtual Agent, the Now Assist panel, or Microsoft Teams.
•Can you give me a list of pending approvals?
•What are the pending approvals for time off requests?
•Show me a list of pending approval requests by priority.
•Give me details about my approval request?
Performing approval action on an approval record
The Approval assistance AI agent shows approval requests that require an action on your part.
After the approval information is provided by the agent, select Approve or Reject for a specific
approval record, or type Approve or Reject. If you reject an approval request, then add a
comment about the rejection reason.

ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.