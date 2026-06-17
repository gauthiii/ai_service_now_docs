# Platform Request status AI agent

*Source: document pages 114–115 (PDF chunk pages 14–15)*

---



<!-- doc page 114 -->

is ready for work. Using the AI agent can help fulfillers focus on actionable work by reducing
manual checks for missing supporting details or back-and-forth conversations. Instead of having
to check whether tasks are waiting on pending approvals or unanswered questions, fulfillers can
see what actionable work is available and prioritize it.
Prerequisites and setup
To access this AI agent, you must have Now Assist Agent for Platform installed on your instance,
which is installed with any other Now Assist application, such as Now Assist for IT Service
Management (ITSM).
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
Accessing the Issue Readiness AI agent
To access the AI agent:
1.Navigate to All > AI Agent Studio > Create and manage.
2. Go to the AI Agents tab.
3. Select Issue Readiness.
Testing the Issue Readiness AI agent
You can manually test the AI agent execution on the Testing page of AI Agent Studio if you have
the sn.aia_admin role and all other roles configured in the security controls. Select the AI agent,
start a manual test, and use utterances in the Task field like the ones below.
Sample utterances
After the agent has been activated in AI Agent Studio, enter phrases such as the following or
similar queries to run the AI Agent in Virtual Agent, the Now Assist panel, or Microsoft Teams.
•Is INC001234 ready for work?
•Do I have enough details on CSM0001234 to start?
Platform Request status AI agent
The Request status AI agent is an AI agent that enables you to view tickets and make updates to
them from Now Assist in Virtual Agent, the Now Assist panel, or Microsoft Teams.
Request status AI agent
The Request status AI agent enables you to view your open tickets, check the status of tickets,
view a summary of the previous comments from the AI agent or others working on the ticket, and
add comments through Now Assist in Virtual Agent, the Now Assist panel, or Microsoft Teams.

ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.


<!-- doc page 115 -->

You can upload a file as an attachment to an open ticket or incident to support a request action.
For example, if you lose your identity card you may request a replacement in the Request status
AI agent. You may be asked to upload an email or document that has your manager's approval
to get the replacement ID card. In the Request status AI agent, you just type, I need to attach a
document to this incident or ticket. The Request status AI agent then provides the Click here to
upload a file option within the AI agent chat for you to upload an attachment to the ticket. You
upload the manager approval and the service agent can then approve your request for a new ID.
To find more information about an open ticket, you can ask the Request status AI agent follow-up
questions based on previous answers from the agent. For example:
•Can you check the latest progress on my most recent request?
•When did I submit this ticket?
•Who is working on it?
•I want to add a comment to my ticket.
•I also want to add an attachment to my ticket.
When you ask for the details of a request, you can perform any other ticket tasks configured
by your administrator in the Standard Ticket configuration, such as reopening an incident, and
resolving a ticket. You don't need to navigate to a specific page to view your tickets. The AI agent
can ask follow-up questions and offer context-aware responses to simplify your experience.
The tools and triggers that are associated with the Request status AI agent are provided by
Now Assist applications. You can activate the AI agent by making triggers active and setting the
display settings to include Virtual Agent. If you want to change this AI agent's instructions, you
must duplicate it, adjust the settings to suit your specific needs, and activate the duplicated
version of the AI agent instead.
Prerequisites and setup
To access this AI agent, you must have Now Assist Agent for Requester installed on your
instance, which is installed with Now Assist for Platform. You can get Now Assist for Platform
when you install any other Now Assist application, such as Now Assist for IT Service
Management (ITSM).
To configure which actions are available, a user with the admin or sp_admin role can configure
the Standard Ticket configuration for a table. In the Standard Ticket actions related list, you can
add, change, or remove actions. All actions available from the Standard Ticket configuration can
be used by the Request status AI agent. See Configure actions for standard ticket page for
more information.
To make the Request status agent available for users, you must navigate to the Toggle display
step of the guided setup in AI Agent Studio. Toggle Virtual Agent to true and select an assistant.
To make the Request status AI agent available in Microsoft Teams, you must configure an
assistant for Now Assist in Virtual Agent to use a Teams channel. See Display your assistant on
a portal or channel for steps to enable Teams for your assistant. Then, in the Request status AI
agent guided setup in AI Agent Studio, select the assistant you configured for Microsoft Teams in
the Toggle display step.
Role masking
Required role:
Role masking enables users to limit the roles and privileges of AI agents during tool execution.
AI agents that get installed with Now Assist applications are assigned pre-defined roles. If you

ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.