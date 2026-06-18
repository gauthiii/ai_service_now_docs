# Configuring AI Agent Advisor

> **Source document:** AI Agent Advisor  
> **Pages:** 5–7



### Supported user interfaces

The AI Agent Advisor application is supported in the Now Assist Center workspace.
The Now Assist Center workspace provides features that enable you to set up of your AI
solutions in a unified experience without switching between separate Now Assist applications.
For more information, see Now Assist Center workspace.

### Application information

AI Agent Advisor (sn_agent_miner) is available as a plugin from the ServiceNow Store.
This store app has the following dependencies.

### Required applications

Plugin name Plugin ID Version Type
AI Agent Advisor sn_agent_miner 0.2.1 App
Insights Clustering sn_icu 2.0.2 App
Utils
Group-Action sn_gaf 6.0.5 App
Framework
AI Search
Now Assist Admin sn_nowassist_admin 8.0.7 App
console
Now Assist sn_nowassist_diagn 4.0.2 App
Troubleshooting
Admin Experience sn_ace 5.2.0 App
Framework
Platform AI Agents sn_uxc_gen_ai 12.0.12 App
and Skills
Generative AI sn_generative_ai 13.0.3 App
Controller
Predictive Intelligence Platform version Plugin
For more information, see Configuring AI Agent Advisor.

### Configuring AI Agent Advisor

Configure settings for AI Agent Advisor.

### Confirm installation of AI Agent Advisor

Confirm the installation of the AI Agent Advisor application.

### Before you begin

All required plugins must be installed before attempting to run AI Agent Advisor. For a list of
dependencies, see Supporting information for AI Agent Advisor.
Role required: AI Agent Advisor admin [sn_agent_miner.app_admin]

| Plugin name | Plugin ID | Version | Type |
| --- | --- | --- | --- |
| AI Agent Advisor | sn_agent_miner | 0.2.1 | App |
| Insights Clustering Utils | sn_icu | 2.0.2 | App |
| Group-Action Framework | sn_gaf | 6.0.5 | App |
| AI Search |  |  |  |
| Now Assist Admin console | sn_nowassist_admin | 8.0.7 | App |
| Now Assist Troubleshooting | sn_nowassist_diagn | 4.0.2 | App |
| Admin Experience Framework | sn_ace | 5.2.0 | App |
| Platform AI Agents and Skills | sn_uxc_gen_ai | 12.0.12 | App |
| Generative AI Controller | sn_generative_ai | 13.0.3 | App |
| Predictive Intelligence |  | Platform version | Plugin |


### About this task

AI Agent Advisor installs and runs automatically as part of the standard Now Assist setup. No
manual steps are required. After Now Assist is installed and configured, AI Agent Advisor will be
present on your instance and will begin analysis automatically.
Follow these steps to confirm the installation of the AI Agent Advisor plugin.

### Procedure

1.Confirm the AI Agent Advisor plugin is installed by navigating to System Definition > Plugins
and selecting the Installed tab.
2. Optional: If the AI Agent Advisor plugin is not installed, perform the following steps to
manually install it.
a.Navigate to System Definition > Plugins.
b.In the search box, type AI Agent Advisor.
c.In the Store applications section under the Available for you tab, select the AI Agent Advisor
card.
  d. Select Install.
  e. Select a version from the list.
f.Select an installation schedule option.
g.Select Install.
The AI Agent Advisor application will install at the selected time.
3. Navigate to All > Now Assist Center or Workspaces > Now Assist Center to confirm the
successful installation.
The Now Assist Center home page opens.
Confirm the following:
  - Automation opportunities appear on the Now Assist Center home page.
  - All AI Agent Advisor dependencies are installed.
Navigate to System Definition > Plugins and select the Installed tab to confirm all required
plugins are installed.
  - Scheduled jobs are installed.
Navigate to System Definition > Scheduled Jobs to confirm that the Agent Miner jobs for
incidents, cases, and cluster matching are included in the list.

### Result

The AI Agent Advisor application is installed and available to the appropriate user roles.

### Set up automation opportunity discovery for AI Agent Advisor

Configure the data sources, filters, and schedule that AI Agent Advisor uses to analyze your
instance and identify automation opportunities.


### Before you begin

For AI Agent Advisor to run a successful analysis, the data source must contain a minimum of
500 records.
Role required: sn_na_center.nac_admin

### About this task

AI Agent Advisor runs a scheduled analysis of your instance records to discover automation
opportunities. Follow these steps to specify which records to include, apply filters to focus the
analysis, and set the frequency and timing of the analysis.
In the event an error occurs when performing these steps, see the troubleshooting steps
described in KB article KB2931703 on Now Support.

### Procedure

1.Navigate to All > Now Assist Center or Workspaces > Now Assist Center.
2. Select Change advisor settings in the AI Agent Advisor section of the home page.
You can also select Admin ( ) in the side navigation bar and select AI Agent Advisor under
Settings on the Admin page.
The AI Agent Advisor Setup tab opens showing a card for each data source. Enable the data
sources you want AI Agent Advisor to analyze.
Incident and Case data sources are enabled by default.
Data sources on the Automation Opportunities Setup page
3. Select the More options button ( ) in the card you want to configure and select Edit.
Choose any of the following data sources:

> **[Screenshot: Data Sources on the Automation Opportunities Setup Page]**
>
> A ServiceNow workspace UI screenshot. The top navigation bar (dark) shows breadcrumb tabs "Admin" and "AI Agent Advisor ×". A teal "View automation opportunities" button is in the top-right corner. The page title reads "AI Agent Advisor setup" with subtitle "Set up and activate what tables to search for automation opportunities."
>
> Three data source cards are shown in a 2-column grid layout (2 cards top, 1 card bottom-left):
>
> - **Cases (top-left):** White card, "Cases" heading with ⋮ menu. Description: "Analyze case records to identify common customer service patterns and automation opportunities in case resolution workflows." Metadata row: Status=Active (green badge), Last run=May 17, 2026 18:44:21, Scheduled to run=Every 30 days, Number of records=507.
> - **Interactions (top-right):** White card, "Interactions" heading with a red "Failed to generate" badge and ⋮ menu. Description: "Analyze interaction records to uncover frequent customer service trends and pinpoint automation opportunities within resolution workflows." Metadata: Status=Active, Last run=May 17, 2026 19:01:07, Every 30 days, 4,768 records.
> - **Incidents (bottom-left):** White card, "Incidents" heading with red "Failed to generate" badge and ⋮ menu. Description: "Analyze incident records to discover repetitive IT issues and standardized resolution procedures suitable for automation." Metadata: Status=Active, Last run=May 17, 2026 19:16:31, Every 30 days, 2,031 records.

