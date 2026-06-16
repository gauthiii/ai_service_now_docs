### In-Product Experience for Agentic Workflows


Available agentic workflows by product (continued)
Product Available agentic workflows
Now Assist for Vulnerability Response
•Retrieve Vulnerability and exposure data with
generative AI
•Assess your exposure to vulnerabilities
•Analyze vulnerability remediation status
•Security Exposure 360
Now Assist for Workplace Service Delivery
•Automate map updates
(WSD)
•Help manage workplace reservations
•Manage temporary space closures
•Optimize cleaning activities
•Workplace Advisor QnA
Now Assist for Zero Copy Connector Explore ERP models
Now Assist Platform
•Analyze incident trends
•Classify tasks
•Generate my work plan
•Generate resolution plans
•Help optimize team productivity
•Identify ways to improve services
•Investigate IT problems
•Notification agent
•Process images for tasks
•Suggest survey responses
In-product experience for agentic workflows
Dedicated spaces in workspaces and in the Core UI enable you to use agentic workflows directly
in record forms. You can view agentic workflow progress and previous executions, and you can
answer follow-up questions for ones that require human supervision.
Agentic AI in the Core UI and workspaces
Agentic workflows can help accomplish complex tasks for you, such as generating resolution
notes for cases and incidents or investigating problems and root causes. You can view agentic
workflows running on a record in the AI Workflows panel in the Core UI form or in workspaces.
For agentic workflows that require human supervision, you can answer questions, approve next
steps, or provide other input. Along with current progress, you can also review historical runs to
compare results.
© 2026 ServiceNow, Inc. All rights reserved. 73
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **Product** | **Available agentic workflows** |
|---|---|
| Now Assist for Vulnerability Response | •Retrieve Vulnerability and exposure data with generative AI •Assess your exposure to vulnerabilities •Analyze vulnerability remediation status •Security Exposure 360 |
| Now Assist for Workplace Service Delivery (WSD) | •Automate map updates •Help manage workplace reservations •Manage temporary space closures •Optimize cleaning activities •Workplace Advisor QnA |
| Now Assist for Zero Copy Connector | Explore ERP models |
| Now Assist Platform | •Analyze incident trends •Classify tasks •Generate my work plan •Generate resolution plans •Help optimize team productivity •Identify ways to improve services •Investigate IT problems •Notification agent •Process images for tasks •Suggest survey responses |

You can create UI actions for your agentic workflows in AI Agent Studio. Open the agentic
workflow, navigate to the Select channels and access step in the guided setup, and create a UI
action.
If you don't see this panel, ensure that the property
com.glide.agentic_processes_view.enabled is set to true.
Agentic workflow execution list
The list of agentic workflow cards can be filtered by execution state. You can change which states
to filter by at any time.
Note: The difference between the Ready for review state and the Completed
state is that the former has generated some output. Agentic workflows without an output are
marked only as Completed.
The user responsible for answering follow-up questions is identified by the Supervised by
field. Only the user specified can answer questions to progress the agentic workflow, but others
can see the questions asked.
Each card displays the current or final processing message. You can see the full list of
processing messages by selecting the agentic workflow card to open the details.
Time estimates based on previous executions are provided for currently running workflows. For
completed workflows, the cards show the total time taken.
The execution list also displays the results of any workflows triggered in the Now Assist panel or
triggered automatically by events once they are complete.
© 2026 ServiceNow, Inc. All rights reserved. 74
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.


> **[Screenshot: Agentic workflow in Core UI — AI Activity panel]**
> Incident record INC0010015 ("Need replacement of laptop battery"): Priority 4-Low, Opened 2026-03-04, State: In Progress, Impact: 3-Low, Urgency: 3-Low. Right-side **AI Activity** panel shows two completed workflow cards:
> 1. **Generate Resolution Plan** — Ready for review, Beth Anglin (Owner), Completed at 9:47 AM
> 2. **Classify Tasks** — Ready for review, Beth Anglin (Owner), Completed on Mar 5, 2026
> Top toolbar: Save, Classify Task, Generate Resolution Plan, Create change request buttons.

> **[Screenshot: AI Activity panel — Execution state filter dropdown]**
> Filter options shown: Input required ✓, In progress ✓, Ready for review ✓, Completed, (Failed), Cancelled.


Agentic workflow execution details
When you select a specific agentic workflow, you can view the processing messages and history.
Processing messages show you what steps the agentic workflow has taken already and which
ones are still being completed.
You can change the processing messages for an AI agent or tool in AI Agent Studio. For an AI
agent, open the AI agent and go to the Select channels and access step. For a tool, open the AI
agent, go to the Add tools and information step, and select the tool to open the form modal.
The history space on the card can show previous answers to follow-up questions. For completed
agentic workflows, you can review the final output in the history if there is any. If there’s an output,
you can see the sources for the AI's reasoning by selecting the information icon. Citations can
include Knowledge Base articles and lists of records.
You can copy the text of the final output of an agentic workflow by selecting the copy icon.
© 2026 ServiceNow, Inc. All rights reserved. 75
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.


> **[Screenshot: Agentic workflow execution detail — Generate Resolution Plan]**
> Detail view showing:
> - Status: **Ready for review** (green badge)
> - Owner: Beth Anglin, Completed Mar 5, 2026
> - Step list (each ✓ checked): Created a plan → Started AI Agent "Next action r..." → Used tool "Get record detai..." → Optimized results → Checked on remaining steps → Searching in Similar records → Used tool "WebSearch" → Used tool "Get Related List..." → Used tool "Get similar recor..." → Used tool "Get relevant kn..." → Checked on remaining steps (×2) → Used tool "Save activity not..." → Checked on remaining steps → Used tool "Check Plan Acti..." → Checking on remaining steps.


Fields updated with agentic AI
If an agentic workflow changes the value of a field, Now Assist displays a label under the field
value stating that the value was modified by AI.
AI presence indicator
When an agentic workflow is in progress on the record, an icon is displayed at the top of the
record form along with other UI actions. If selected, you can see how many agentic workflows are
running on the record and the general status of each one.
If there’s an agentic workflow in progress that you don't want to complete, you can cancel it.
Select the more options icon on the agentic workflow card, and then select Cancel.
Alerts for agentic workflow status changes and required input
When an agentic workflow changes states, such as when it completes or has a follow-up
question, an alert appears at the top of the screen. If the workflow generates an output, you can
select the Review button to see the final result.
Enable the in-product experience for agentic workflows
Enable the AI Workflows panel and UI actions for agentic workflows on forms in the Core UI and
workspaces to track agentic AI executions.
Before you begin
Role required: admin
© 2026 ServiceNow, Inc. All rights reserved. 76
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.


> **[Screenshot: Agentic workflow — Review output panel]**
> Completed "Review output" panel for a laptop battery replacement incident.
> **Completed resolution steps:** No completed steps — no prior actions recorded.
> **Pending resolution steps:**
> - Verify 5-year Dell factory warranty coverage for parts and labor
> - Contact OIT Help Desk at 8-HELP to confirm hardware issue
> - If hardware confirmed, contact Dell directly; have system tag number ready
> - Dell ships replacement battery with prepaid return label
> - Hardware Support can replace under warranty for a labor charge
> - Laptop batteries are CRUs; Dell does not reimburse Hardware Support labor
> - Reference: Dell Warranty and Battery Replacement policy (URL provided)
> Thumbs up/down feedback icons. Disclaimer: "Generated by Now Assist. Check for accuracy."


About this task
Agentic workflows can perform work on certain records, and you can track their progress or
provide input in the AI Workflows panel available for forms and workspaces. See In-product
agentic AI for more details about the functions and features of the AI Workflows panel.
The following task describes the process for enabling the system property that
allows you to see the AI Workflows panel and see UI actions for agentic workflows:
com.glide.agentic_processes_view.enabled.
To enable users to access agentic workflows with UI actions, you can open the agentic workflow
in AI Agent Studio and navigate to the Select channels and access step. You can select a UI
action as a possible way to access the workflow. See Select channels and access for agentic
workflows for more information.
Procedure
1.Navigate to All > System Properties > All Properties.
2. Select New.
3. In the Name field, enter com.glide.agentic_processes_view.enabled.
4.In the Value field, enter true.
Result
The In-product agentic experience, including the AI Workflows panel, is available.
What to do next
Monitor agentic workflow execution on forms in the Core UI and workspaces, or create UI actions
to grant users access.
Platform agentic workflows
You can use the available Now Assist AI agents Platform agentic workflows to achieve business
outcomes with self-executing autonomous AI agents.
Use the following agentic workflows that are available with ServiceNow AI Platform.
Available agentic workflows for Platform
Agentic
workflow Description Available AI agents
name
Analyze Detects recurring patterns, predicts disruptions, and enables Issue trend
task trends proactive resolutions with actionable recommendations. analysis AI Agent
Classify Triages tasks by updating fields, evaluating sentiment, and Record field value
tasks summarizing. prediction AI agent
Generate Provides a personalized work plan based on current work Prioritize work AI
my work and historical data of previous work. agent
plan
© 2026 ServiceNow, Inc. All rights reserved. 77
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **Agentic workflow name** | **Description** | **Available AI agents** |
|---|---|---|
| Analyze task trends | Detects recurring patterns, predicts disruptions, and enables proactive resolutions with actionable recommendations. |  |
| Classify tasks | Triages tasks by updating fields, evaluating sentiment, and summarizing. |  |