## Set up automation opportunity discovery for AI Agent Advisor

> **Source document:** AI Agent Advisor  
> **Pages:** 6–7



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

