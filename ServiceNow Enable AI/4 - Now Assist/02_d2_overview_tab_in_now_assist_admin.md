# Overview tab in Now Assist Admin

_Source pages: 9–13 | Depth: 2_

---

<!-- page 9 -->
Benefit Feature Users
Monitor Now Assist consumption on your Monitoring Now Assist Administrators
instance. usage in Subscription
Management
Overview tab in Now Assist Admin
The Now Assist Admin console provides quick and effortless access to the important information
that you need to set up, configure, and monitor Now Assist applications and features.
x Now Assist Admin overview
Now Assist Admin overview tab
Begin your exploration of the Now Assist features and skills in the Now Assist Admin console.
This console contains everything that you need to install, configure, and learn about the different
generative AI features on the ServiceNow AI Platform.
The following example shows the Now Assist Admin Overview page.
Now Assist Admin Overview page
Now Assist Admin workflow
Take five steps to begin using the Now Assist Admin console.
1. Install plugins.
On the Available for you tab of the Settings page, you can review the available
plugins and install the ones that are relevant to your business needs. Each plugin
contains the skills that you can activate to enable generative AI features on your
instance. The following diagram shows the Available for you tab.

<!-- page 10 -->
Available for you tab on the Now Assist Admin Settings > Plugins
page
2. (Optional) Turn on the Now Assist panel.
The Now Assist panel integrates the Now Assist skills into the Next Experience UI.
By turning on the Now Assist panel directly from the Now Assist Admin console, you
enable agents to access skills from anywhere on the ServiceNow AI Platform.
For more information about the Now Assist panel, see Now Assist panel overview.
This step is optional because the skills can also display in-product in the Core UI
and in Workspaces.
You can turn the Now Assist panel on from the Now Assist Experiences page of the
Admin console.

<!-- page 11 -->
Now Assist Experiences page with Now Assist panel
3. Activate skills.
Skills are features that are created for a specific use case in a Now Assist
application. Use the Now Assist Skills page to explore the skills that are available
with your installed plugins. The following diagram shows the available features and
skills in the Technology workflow.
Available Now Assist features and skills in the Technology workflow
After deciding which skills best fit your business needs, you can activate them from
the console. Some skills require configuration so that you can customize the skill
to your needs, such as determining the skill inputs and triggers. You can select the
skills that you want to configure in the Now Assist Admin Features page.
The following example shows a step in the guided setup of the skill activation
process, which is choosing where to display the skill. Skills can be displayed in-
product, including the Core UI and Workspaces, or in the Now Assist panel. You can
choose either or both locations. The following diagram shows the process for chat
summarization activation in Now Assist Admin.

<!-- page 12 -->
Chat summarization activation in Now Assist Admin
4. Review your Now Assist account settings.
The Now Assist Admin console Settings page enables you to set up language
support, if you have Dynamic Translation enabled on your instance, and review your
account details. Get up-to-date information about what plugins are available to you
and the status of data sharing on your instance.
Now Assist Admin console account settings
5. Monitor and analyze skill performance.
Use the metrics available on the Overview page to review the summaries,
performance information, and issues that need your attention. The following
example shows the current plugin status, as well as the number of active skills.

<!-- page 13 -->
Plugin and Skills status on the Now Assist Admin Overview page
The Now Assist Admin console contains the Now Assist journey checklist with additional
instructions for implementing Now Assist on your instance.
Now Assist journey checklist
You can consult the following checklist from the Now Assist Admin console
Overview page at any time to guide your implementation of Now Assist applications,
features, and skills.
Learn more about the Now Assist journey
•Get an overview of the Now Assist framework.
•Discover the Now Assist panel.
•Explore the Now Assist skills available.
•Activate and configure a Now Assist skill using the Now Assist Admin console.
•Analyze and monitor Now Assist skill usage and performance.

> **[Screenshot: Now Assist Admin Overview Page]**
> Full-width ServiceNow Next Experience screenshot of the Now Assist Admin console Overview page. Top navigation bar shows: "servicenow" logo, All, Favorites, History, Workspaces, Admin menus, a centred "Now Assist Admin ★" badge, search bar, and icon toolbar. Below the nav, a secondary tab bar shows: Overview (active), Now Assist Skills, Now Assist Experiences, Performance, Settings.
>
> Main content area is split into two columns. Left/centre column shows a "Now Assist Summary" card with two sub-panels: "Plugin status" (donut chart showing 4 installed in teal vs 27 not installed in orange, with a "Review now" link) and "Skills status" (donut chart with 139 total skills broken down: Not started 64, Draft 9, Inactive 3, Active 63). Below these panels is a "Skill usage" card with date filter "All skills / Date range" and two KPI tiles: "Number of actions: 0" and "Avg number of unique users per day who triggered action: 0".
>
> Right sidebar shows a red "Needs Attention" banner with the count "109" in large text, followed by four expandable items: "Plugins not installed (27)", "Skills inactive (3)", "Skills in draft state (10)", "Skills not started (69)". Below this is a "Now Assist Journey Checklist" card with a teal "View checklist" button.

> **[Screenshot: Available for you tab on the Now Assist Admin Settings > Plugins page]**
> Screenshot of the Plugins settings page. Breadcrumb reads "Settings > Plugins". Page title is "Plugins" with subtitle "List of all Now Assist AI plugins available per product." Two tabs shown: "Available for you" (selected) and "Installed". A workflow dropdown filter on the right reads "Workflow: All". Below, "All available plugins (11)" header appears.
>
> Three plugin cards visible in a 3-column grid: 1) "Now Assist for Security Operations (SecOps)" – with a colourful circular icon, description "GenAI related features for Security Operations that are powered by Now Assist", and a "Get plugins" button. 2) "Now Assist for HR Service Delivery (HRSD)" – similar layout, "GenAI related features for HR Service Delivery that are powered by Now Assist", "Get plugins" button. 3) "Now Assist for Creator" – book/document icon, "Helping creators build with the power of Generative AI", "Get plugins" button. A partial fourth row of cards is visible at bottom.

> **[Screenshot: Now Assist Experiences page with Now Assist panel]**
> Two-part screenshot. Upper portion shows the Now Assist Experiences page in the Admin console. Left sidebar lists items: "Now Assist panel" and "Now Assist context menu". Main area shows a card titled "Now Assist panel – Included in license" with product touchpoint metadata and a summary paragraph. A "Manage" sidebar on the right shows "Now Assist panel is turned on for your users" with a green "Turn off" button. A "Settings" section shows "Voice Input OFF" with a toggle.
>
> Lower portion shows the Now Assist Skills page for Technology workflow. Left nav shows a tree of workflows: Technology (expanded showing Risk & Sustainability, ITSM, CMDB, Security Operations, SAM, ITOM, CWM, SPM, OTSM, EA), Customer, Employee, Creator, App Engine, Platform. Main area titled "Now Assist skills for ITSM" shows a table with columns: Name, Status, Skill type, LLM Provider, Displayed On, Last updated, Action. Rows include: Incident sentiment analysis (Draft, Out-of-box, Now LLM Service, Jul 18 2025, Activate button), Email recommendation (Draft, Out-of-box, Nov 11 2024), Incident assist (Not started, Out-of-box), Change request risk explanation (Not started, Now LLM Service, Sep 4 2024), KB generation (Draft, Out-of-box, May 15 2025), Incident summarization (Active green badge, Out-of-box, In-product Now Assist panel, Oct 28 2025, Deactivate), Role Masking (Draft, Custom, Now LLM Service, Oct 7 2025, Activate), Clone of Incident summarization (Not started, Out-of-box, Sep 16 2025, Turn on).

> **[Screenshot: Chat summarization activation wizard in Now Assist Admin]**
> Guided activation wizard for the "Chat summarization" skill (labelled "CSM" in a small badge). An "Exit" button is in the top-right. Left sidebar shows four steps in a vertical stepper: 1) Define trigger (filled circle – complete), 2) Choose Input (filled), 3) Select display (filled), 4) Review and activate (filled). Main content area for step 1 "Define trigger" shows the prompt "Choose when and how the skill will be triggered" with an "Explain this" link. Four toggle rows, all currently OFF: "Virtual Agent to Live Agent handoff" (summary created when conversation moves from virtual to live agent), "Live Agent to Live Agent handoff" (conversation moves from live to live agent), "Quick action" (agents can use summarize quick action), "Chat wrap-up" (chat summary field auto-populates after conversation ends). Bottom-right has "Back" and a teal "Save and continue" button.
>
> **[Screenshot: Now Assist Admin console account settings]**
> Settings > Account page in the Now Assist Admin console. Left sidebar shows navigation items: Plugins, Multilingual service, Data sharing and process…, Now Assist Guardian, Manage AI models, Manage Integration, Account (selected/highlighted). Main area shows "Account" heading with subtitle "View your account license information and manage data sharing." An "Account details" card shows "Version 12.0.3-6" and "Your license includes:" with an "All included in license" badge. Two bullet items with green check icons: "Now Assist panel – Empower users with a personal generative AI assistant..." and "Now Assist skills – Unlock Now Assist skills you can configure to improve user productivity."

> **[Screenshot: Plugin and Skills status on the Now Assist Admin Overview page]**
> Close-up of the "Now Assist Summary" card. Left panel: "Plugin status" donut chart showing 2 installed (small teal slice) vs 11 not installed (large orange slice) with a "Review now" link below. Right panel: "Skills status" donut chart showing 128 total skills. Legend below the chart: Not started 96 (dark blue), Draft 2 (medium blue), Inactive 3 (light grey), Active 27 (teal).
>
> **[Screenshot: Now Assist checklist modal]**
> A modal overlay titled "Now Assist checklist" with an X close button. Subtitle reads "The following steps make up your Now Assist journey and will allow you to get the most out of generative AI skills." Five numbered circle steps: 1) Install Now Assist plugins – "Visit the store to install the plugin specific to the product workflows. Browse all available plugins." 2) Turn on Now Assist panel – "After a plugin is installed, return to this console to turn on the Now Assist panel…" 3) Activate Now Assist skills – "Once the panel is turned on, configure and customise information sources..." 4) Review account settings – "Review account information and manage data sharing." 5) Analyze Now Assist skills – "Track and monitor the progress of your Now Assist skills." A teal "Done" button is at the bottom-right.