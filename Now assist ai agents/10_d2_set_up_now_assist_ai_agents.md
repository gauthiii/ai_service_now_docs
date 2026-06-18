# Set up Now Assist AI agents

_Source pages: 30–30 | Depth: 2_

---

<!-- page 30 -->
What to do next
Assign the admin role
Add the role sn_aia.admin to the user who will administer the AI Agent Studio,
and then navigate to All > AI Agent Studio > Overview.
Access the AI Agent Studio
Navigate to All > AI Agent Studio > Overview in the AI Agent Studio application
navigator where you can create and manage AI agents and agentic workflows.
Set up Now Assist AI agents
The default (base system) AI agents provide preconfigured agentic workflows that address
common business challenges across ServiceNow applications. Before activating the default AI
agents, you must verify that your instance meets the prerequisites and complete the required
configuration steps.
Before you begin
Role required: sn_aia_admin
About this task
Prerequisites
Platform version:
•Minimum: Yokohama Patch 1+ or Xanadu Patch 7+
•Recommended: Yokohama Patch 8 or Zurich Patch 4
Required plugins and store Apps
•Now Assist AI agents store app (version 6.0.17 or later as of December 2025)
•At least one Now Assist workflow plugin:
◦Now Assist for ITSM
◦Now Assist for HRSD
◦Now Assist for CSM
◦Now Assist for Security Operations
•Generative AI Controller plugin (minimum version 11.0.0)
Note: Select Load demo data during installation to access preconfigured
examples.
Licensing Requirements
Now Assist Pro Plus or Enterprise entitlement
Required User Roles
•sn_aia.admin - Provides access to AI Agent Studio
•sn_nowassist_admin.nsa_admin - Enables Now Assist administration
Procedure
1.Enable AI Search.
a.Navigate to AI Search > AI Search Status.
b.Verify that AI Search is enabled.