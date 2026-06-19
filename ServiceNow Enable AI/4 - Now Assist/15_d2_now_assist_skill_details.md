# Now Assist skill details

_Source pages: 156–157 | Depth: 2_

---

<!-- page 156 -->
◦To create a new granular feedback selection, select New.
◦To change an existing granular feedback option, select the option.
12. Enter or change the fields: Description, Message, Message Key, Bundle Id, Application, Active,
Order.
13.Select Submit.
14.To access the stored feedback data, in the filter navigator field, enter
sys_ci_analytics.list to display the CI Analytics table.
15.Select the appropriate entry to view the feedback data.
Configure processing messages
For Now Assist panel premium chat, configure processing messages to control the status
updates that appear in the chat interface while Now Assist works on a request. You can
customize the text of processing messages to better reflect your organization's terminology or
the specific actions your AI agents perform.
Before you begin
Role required: admin
Procedure
1.In the filter navigator field, enter sys_properties.list.
2. In the selection fields, select Name from the drop-down list and enter
processing_messages in the Search field.
3. If you have Now Assist panel premium chat, configure
sn_aia.og_ao.enable_processing_messages to enable or disable processing messages.
Using Now Assist Admin
Use Now Assist Admin to explore the various Now Assist plugins, skills and associated
Generative AI application features you are entitled to.
Now Assist skill details
Explore details of Now Assist skills, security and usage data.
Explore details about various skills within a workflow. This page contains information about skill,
usage and consumption information, and a summary of security and governance data.
Note: The minimum version required to access the skill details page is Zurich patch 10
and Australia patch 3.

<!-- page 157 -->
The View details option displays skill details under these tabs:
•Overview: General description of the skill
•Usage: Details about the skill usage, adoption and AI assist consumption. The report on total
execution, active users and executions across channels can be exported in .csv or excel
format.
◦Total executions: Count of the number of times the selected skill is executed
◦Active users: Total number of unique users who have utilized this skill

> **[Screenshot: Now Assist skill detail card for Incident sentiment analysis]**
> A skill detail card showing the "Incident sentiment analysis" skill with status badges "Not started", "Out-of-box", "Now LLM Service". Description: "View requester's sentiment corresponding to the Incident. View trend and reason for the sentiment to take informed decisions…" Last updated by admin, Jul 18 2025. A teal "View details for Incident sentiment analysis" link appears. Two large buttons at the bottom: "View details" and "Activate skill".
>
> **[Screenshot: Skill detail – Overview tab for Incident assist]**
> The skill detail page for "Incident assist" (status: Not started) showing three tabs: Overview, Usage, Security and governance. Overview tab content: Description "Resolve incidents faster and easier by asking questions in the Now Assist panel." Metadata fields: Workflow: Technology, Product: ITSM, Feature: Incident, Skill type: Out-of-box, Available display locations: – (none), Last updated: 2025-07-21 14:18:02, Last updated by: admin. An "Activate skill" button appears top-right.
>
> **[Screenshot: Skill detail – Usage tab for Incident assist]**
> Same skill (Incident assist) on the Usage tab. Date filter "Date: 2026-05-18 – 2026-05-25". "Usage and adoption" section with three KPI tiles: "Total executions: 0 — 0 (0.0%) since previous period May 11 – M…", "Active users: 0 — same trend text", "Executions by channels: No data available." Below those tiles: "Assist consumption" section header.