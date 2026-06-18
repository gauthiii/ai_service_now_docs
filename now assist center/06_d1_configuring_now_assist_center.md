# Configuring Now Assist Center

> **Source document:** Now Assist Center  
> **Pages:** 17–18



### Application information

Now Assist Center (sn_na_center) is available as a plugin from the ServiceNow Store.
This store app has no dependencies.
For more information, see Configuring Now Assist Center.

### Configuring Now Assist Center

Install and configure settings for Now Assist Center.

### Confirm installation of Now Assist Center

Confirm the installation of the Now Assist Center application.

### Before you begin

Review the Now Assist Center application listing in the ServiceNow Store for information on
dependencies, licensing or subscription requirements, and release compatibility.
Role required: admin

### About this task

Now Assist Center installs and runs automatically as part of the standard Now Assist for Platform
setup. No manual steps are required. After Now Assist for Platform is installed and configured,
Now Assist Center will be present on your instance.
Follow these steps to confirm the installation of the Now Assist Center plugin.

### Procedure

1.Confirm the Now Assist Center plugin is installed by navigating to All > System Definition >
Plugins and selecting the Installed tab.
2. Optional: If the Now Assist Center plugin is not installed, perform the following steps to
manually install it.
a.Navigate to All > System Definition > Plugins.
b.In the search box, type Now Assist Center.
c.In the Store applications section under the Available for you tab, select the Now Assist
Center card.
  d. Select Install.
  e. Select a version from the list.
f.Review the installation details and select Continue.
g.Select an installation schedule option.

h.Select Install.
The Now Assist Center application will install at the selected time.
3. Navigate to All > Now Assist Center or Workspaces > Now Assist Center to confirm the
successful installation.

### Result

The application is installed and available to the appropriate user roles.

### Enable the Now Assist panel

Enable the Now Assist panel to have your AI companion perform setup, configuration, and
administrative tasks more quickly using natural language prompts.

### Before you begin

Role required: sn_na_center.nac_admin

### About this task

The Now Assist panel is turned on by default. If it is turned off, follow these steps to turn on the
Now Assist panel.
The Now Assist panel must be enabled for administrators to use the conversational interface in
Now Assist Center. When the panel is turned off, a banner appears on the home page notifying
you that the conversational experience is unavailable, with a link to the settings page.
For more information on the capabilities of Now Assist panel, see Now Assist panel.

### Procedure

1.Navigate to All > Now Assist Center or Workspaces > Now Assist Center.
2. Select Admin in the side navigation bar.
3. Under Now Assist Experiences on the Now Assist Admin page, select Now Assist Panel.
4.Select Turn on to enable the Now Assist panel.
5. Select Turn on again to confirm.

### Result

The Now Assist panel is enabled and available globally via the sparkle icon ( ) in the Next
Experience Unified Navigation. The panel understands where users are in the application and
can personalize responses accordingly, streamlining the completion of tasks.

### Set up automation opportunity discovery in Now Assist Center

Configure the data sources, filters, and schedule that AI Agent Advisor uses to analyze your
instance and identify automation opportunities.
AI Agent Advisor runs a scheduled analysis of your instance records to discover automation
opportunities. Follow these steps to specify which records to include, apply filters to focus the
analysis, and set the frequency and timing of the analysis.
For more information, see Set up automation opportunity discovery for AI Agent Advisor.
