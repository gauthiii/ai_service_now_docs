# Install Now Assist AI agents

_Source pages: 29–29 | Depth: 2_

---

<!-- page 29 -->
AI Agent Studio Skills migration
You can auto-migrate all the AI Agent Studio skills from on-glide execution path to the off-glide
execution path by setting the Off-Glide Enabled to true, to enable the skill migration to Mosaic.
To do this:
•Navigate to the OneExtend Capabilities [sys_one_extend_capability.list] table.
•Find the Now Assist AI Agents application.
•Set the Off-Glide Enabled to true
•Select Save.
Install Now Assist AI agents
Install Now Assist AI agents on your ServiceNow instance to enable the agentic AI experience.
Before you begin
To get started with AI agents, you must have:
•License requirements: A ServiceNow Pro Plus or Enterprise Plus license.
Note: A Now Assist License is required. Now Assist AI Agents is available to all users
who have Now Assist.
•Instance requirements: An instance on Zurich Patch 2 or later.
•Application requirements: The following store applications and all the dependency
applications must be installed and updated:
◦Now Assist for IT or HRSD (or other workflows).
Note: AI agents aren’t standalone applications that you can install directly. To enable
AI agents on your instance, you must install and activate other Now Assist applications
that include AI agents, such as Now Assist for IT Service Management (ITSM) or Now
Assist for Customer Service Management (CSM).
◦Now Assist AI Agents store application
•AI Search enabled on your instance.
•The Now Assist panel must be turned on.
Note: You can access AI agents in the Now Assist panel. To enable the Now Assist
panel, see Turn on the Now Assist panel.
Role required: sn_aia.admin
Procedure
1.Navigate to All > System Definition > Plugins.
2. Search for and select a Now Assist application, such as Now Assist for IT Service Management
(ITSM) or Now Assist for Platform.
3. Select Install.
Result
AI agents associated with the Now Assist application are installed on your instance.