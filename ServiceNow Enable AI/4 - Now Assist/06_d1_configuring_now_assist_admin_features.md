# Configuring Now Assist Admin features

_Source pages: 144–155 | Depth: 1_

---

<!-- page 144 -->
3. In the Account details section of the panel, review what is included with your Now Assist
license.
What to do next
Turn on the skills that you want for your Now Assist workflow applications so that you can
use generative AI capabilities across the ServiceNow AI Platform. For more information, see
Configuring Now Assist Admin features.
Configuring Now Assist Admin features
Use the Now Assist Admin console to activate the various Now Assist applications and skills that
you’re entitled to.
Configuration overview
Install and activate the plugins, turn on the Now Assist panel, and view the account settings. You
must install at least one Now Assist application before you can configure any skills.
The following example shows the Settings page with four available plugins to install, including
Now Assist for HRSD and Now Assist for Creator.

<!-- page 145 -->
Now Assist Admin settings page
Install Now Assist plugins
Install Now Assist plugins to enable generative AI on your instance.
Before you begin
Role required: admin
Follow these instructions to get started with Now Assist Admin:
1.To get started with Now Assist, you must install at least one Now Assist application on your
instance.
2. License any Now Assist software from the ServiceNow Store and install it through the
Application Manager to access Now Assist Admin.
3. The Now Assist Admin console guides your implementation, starting with installation.
4.Check out the Now Assist Journey Checklist for more information.
About this task
Now Assist applications often function interdependently. Now Assist Suites help reduce runtime
errors and update issues by bundling compatible versions of Now Assist applications together
during installation and updates.
For more information about how Now Assist Suites work, see Now Assist suite versions in the
Application Manager.
For details about available Now Assist Suites and their compatibility with ServiceNow AI Platform
versions, see Now Assist Suite release notes .
Procedure
1.Navigate to All > Now Assist Admin > Settings.
If you’re already in Now Assist Admin, select the Settings tab.
2. On the Settings page, select Plugins.

<!-- page 146 -->
Plugins appear as cards. Review all Now Assist plugins on the Available for you tab. Plugins
that you have already installed appear on the Installed tab.
3. Optional: If you don't already have a license for the plugin, request a license from the
®
ServiceNow Store.
a.Select Get plugins on the card for the plugin that you want to install.
b.In the confirmation window, select Install Plugin to open the ServiceNow Store page for the
plugin in a new browser tab.
c.Request the license.
For additional information, see Getting apps and trials from the ServiceNow Store .
4.Navigate to Admin > Application Manager > Available for you.
5. Find and select the Now Assist application you want to install.
6.Select Install.
7.In the Select suite version drop-down menu, select a Now Assist Suite version.
The available suite versions are compatible with your instance. If you have other Now
Assist applications already installed on your instance, they might require update for suite
compatibility. For more information about Now Assist Suite compatibility, see Now Assist suite
versions in the Application Manager.
If you haven't installed a Now Assist Suite version yet, you have the option to choose none in
the version selector. This option enables you to begin using Now Assist Suites at a time that
works best for your organization.
8.Optional: If you have available application customizations, use the Customized ver. drop-
down menu to select which customization to use.
Your customizations might not be compatible with a new application version. Update
the application in a non-production instance, then make any necessary changes to your
customization and validate compatibility before making updates in production instances.
For more information about managing customizations, see Manage customizations to
applications .
9.Optional: Include demo data if it's desired and available.

<!-- page 147 -->
a.Select the option to install demo data next to each Now Assist application you want demo
data for.
The option to install demo data isn't available for all applications.
b.Turn on the Load demo data for selected apps toggle switch.
10.Select Continue to review the installation details.
Trouble?
If any applications display "Installation blocked," it means that application version isn't
licensed yet. Either uninstall the application or license the required version.
11. Install the application now or schedule installation for a later time.
Installation option Procedure
a.Leave the default option to Install now se­
Install now lected.
b.Select Install.
a.Select the option to Install later.
Install later b.Enter a start date and start time.
c.Select Schedule.
12. Return to the Now Assist Admin console.
13.In the dialog box, select Refresh.
14.Either close the dialog box to review all of your plugins or select View all (Plugin) Assists and
Skills to review the features of your new plugin.
Result
Your plugin is successfully installed.
If you encounter issues installing or updating applications, see this knowledge article for steps
that may address your issue. Otherwise, you can make a Support case.
What to do next
Activate the Now Assist panel standard chat or Activate a Now Assist skill.
Now Assist suite versions in the Application Manager
The Application Manager uses Now Assist suite versions to verify compatibility between multiple
Now Assist applications in one instance.
Now Assist applications often function interdependently, which can result in runtime errors when
one Now Assist application is dependent on a specific version of another one. Now Assist suites
help reduce runtime errors by bundling compatible versions of Now Assist applications together.
Suite versions are independent from the application versions that they contain.
The Application Manager uses Now Assist suite versions to verify compatibility between every
new Now Assist application version you install and all Now Assist application versions already
present on your instance. This verification happens when installing new applications for the first
time and when updating application versions. The installation details for Now Assist applications
enable you to select a Now Assist suite version and review which applications, if any, need to be
updated or procured for suite compatibility.

<!-- page 148 -->
Now Assist installation details
A Now Assist application version might be included in multiple Now Assist suite versions based
on its compatibility with other applications. When you install or update a Now Assist application,
you can choose any suite version that the application is compatible with. Based on the Now
Assist suite version you choose, multiple applications might be updated.
Example: Now Assist suite versions in the Application Manager
Some Now Assist applications are part of multiple Now Assist suites because they're compatible
with multiple other Now Assist application versions.
Note: The following examples are for illustrative purposes only. They might not reflect
actual Now Assist suite versions.
Assume that you want to install Now Assist for ITSM for the first time. You have the following Now
Assist applications installed on your instance already:
•Now Assist for ITOM (version 1.5.0)
•Now Assist for Creator (version 27.1.1)
When you start to install Now Assist for ITSM, you can select different Now Assist suite versions
based on the versions of Now Assist for ITSM that are compatible with your instance. You can
choose from Now Assist suite 4.0.0, 3.0.0, or 2.0.0.
Now Assist suite 4.0.0
The latest available Now Assist suite version is selected by default. The following information is
displayed when Now Assist suite version 4.0.0 is selected:
Example Now Assist suite 4.0.0
Now Assist application Version Status
Now Assist for ITSM 9.0.1 Will be installed
Now Assist for ITOM 2.0.3 Will be updated
Now Assist for Creator 27.2.2 Will be updated
Now Assist suite version 4.0.0 includes the latest versions of Now Assist for ITSM, Now Assist for
ITOM, and Now Assist for Creator.

<!-- page 149 -->
If you want to update to the latest version of Now Assist for ITSM and Now Assist for ITOM now,
Now Assist suite version 4.0.0 could be a good option.
Note: Test application updates in a non-production environment to verify expected
functionality before making updates in production instances.
Now Assist suite 3.0.0
The following information is displayed when you select Now Assist suite version 3.0.0:
Example Now Assist suite 3.0.0
Now Assist application Version Status
Now Assist for ITSM 9.0.1 Will be installed
Now Assist for ITOM 2.0.2 Will be updated
Now Assist for Creator 27.2.2 Will be updated
Now Assist suite 3.0.0 includes the latest version of Now Assist for ITSM (9.0.1). It also includes a
newer (but not the latest) version of Now Assist for ITOM and the latest version of Now Assist for
Creator.
Now Assist for ITSM version 9.0.1 and Now Assist for Creator version 27.2.2 are both in Now Assist
suites 3.0.0 and 4.0.0. The difference between Now Assist suite versions 3.0.0 and 4.0.0 are the
versions of Now Assist for ITOM that are available. Which version of Now Assist for ITOM you
want can help you decide between updating to Now Assist suite 3.0.0 or 4.0.0.
Now Assist suite 2.0.0
The following information is displayed when you select Now Assist suite version 2.0.0:
Suite 2.0.0
Now Assist application Version Status
Now Assist for ITSM 8.0.0 Will be installed
Now Assist for ITOM 1.5.0 Up to date
Now Assist for Creator 27.1.1 Up to date
Now Assist suite 2.0.0 includes versions of Now Assist for ITOM and Now Assist for Creator that
are already installed on your instance. The latest version of Now Assist for ITSM isn't part of Now
Assist suite 2.0.0, but a previous version (8.0.0) is.
In this case, you can choose to install the older version of Now Assist for ITSM, and not update
your other Now Assist applications yet.
Note: Not updating the suite version might not be an option. Depending on compatibility
of a new Now Assist application, you might have to update your Now Assist suite version to
complete installation.
Activate the Now Assist panel standard chat
Activate the Now Assist panel standard chat to enable your agents to use Now Assist skills, such
as task summarization or navigation, in a side panel on the user interface.

<!-- page 150 -->
Before you begin
You must install at least one Now Assist application before you can turn on the Now Assist panel.
Role required: sn_generative_ai.nsa_admin
About this task
You must have the now_assist_panel_user role to have access to the Now Assist panel once you
turn it on.
To learn more about the Now Assist panel, and how it can assist your agents, see Now Assist
panel.
Procedure
1.Navigate to All > Now Assist Admin > Now Assist Experiences.
If you’re already in Now Assist Admin, select the Now Assist Experiences tab.
2. Select Now Assist panel.
3. Enable the Now Assist panel on your instance by selecting Turn On.
4.In the Turn on Now Assist panel dialog box, select Turn on.
5. If you want to use assistants, you must activate them.
See Configuring assistants overview for information on activating assistants.

<!-- page 151 -->
What to do next
For examples of the Now Assist panel in action for Now Assist applications, see the following
topics:
•Summarize a chat conversation by using Now Assist for Customer Service Management
(CSM)
•Summarize a Sidebar discussion by using Now Assist for IT Service Management (ITSM)
•Summarize an issue using Now Assist for Integrated Risk Management (IRM)
•Generate a knowledge article from HR Agent Workspace with Now Assist for HRSD
Activate Now Assist panel enhanced chat
Activate the Now Assist panel enhanced chat to enable your agents to use Now Assist skills,
such as task summarization or navigation, in a side panel on the user interface.
Before you begin
You must install at least one Now Assist application before you can turn on the Now Assist panel.
Role required: sn_nowassist_admin.nsa_admin
About this task
You must have the now_assist_panel_user role to have access to the Now Assist panel once you
turn it on.
To learn more about the Now Assist panel, and how it can assist your agents, see Now Assist
panel.
Procedure
1.Navigate to All > Conversational Interfaces > Assistants.
2. On the Assistants page, select Now Assist Panel - Platform
(default).

<!-- page 152 -->
3. On the Now Assist Panel - Platform (default) page, select Display
experience.
4.Select the Add agent experiences drop-down menu and then select Unified Navigation app
shell.
5. Select the ellipsis to change the chat experience from standard chat to enhanced
chat.
Important: Switching to enhanced chat is permanent and can't be undone after you
have selected Save and then Save and continue.

<!-- page 153 -->
6.On the Edit chat experience screen, select Enhanced
chat.
7.Select Save.
8.If you want to use assistants, you must activate them.
See Configuring assistants overview for information on activating assistants.
What to do next
For examples of the Now Assist panel in action for Now Assist applications, see the following
topics:
•Summarize a chat conversation by using Now Assist for Customer Service Management
(CSM)
•Summarize a Sidebar discussion by using Now Assist for IT Service Management (ITSM)
•Summarize an issue using Now Assist for Integrated Risk Management (IRM)
•Generate a knowledge article from HR Agent Workspace with Now Assist for HRSD
Enable voice input for Now Assist panel
Give users the option to use their voice when interacting with the Now Assist panel to make
the panel more accessible. Voice input enables you to use the panel without needing to use a
keyboard.
Before you begin
Note: Voice input is automatically activated when the Now Assist panel is activated. As
of the Zurich Patch 4 release, voice input is configured in Enable additional chat features
and not with this option.
You must have installed at least one Now Assist application with a skill that uses the Now Assist
panel. See Now Assist panel for more information about supported skills.
Role required: sn_generative_ai.nsa_admin
About this task
You can give users the option to use voice input in the Now Assist panel. This feature provides an
additional input method to interact with Now Assist skills in English. Once it’s enabled, users can
choose to activate this feature in their personal accessibility preferences by toggling on Enable

<!-- page 154 -->
voice input for the Now Assist panel. See Configure Next Experience accessibility preferences
for more information about setting personal accessibility preferences.
Voice-to-text input can help users with mobility impairments access generative AI skills without
using a keyboard. This feature can also be useful to blind or low-vision users, neurodivergent
users, non-native language speakers, and mobile users on the go, such as field service agents.
The voice input feature is not supported in regulated markets.
Procedure
1.Navigate to All > Now Assist Admin > Now Assist Experiences.
If you’re already in the Now Assist Admin console, navigate to the Now Assist Experiences
page.
2. Go to the Now Assist panel tab.
3. In the Settings section, turn on the toggle for Voice Input.
Result
Users can choose whether they can use their voice to interact with the Now Assist panel in their
Next Experience accessibility preferences.
Configure disambiguation
Configure the disambiguation property that controls when the assistant asks clarifying questions
before responding to a Now Assist in Virtual Agent or Now Assist panel user request.
Before you begin
Role required: admin
About this task
Disambiguation or clarification helps the Now Assist assistant handle situations where the
user's request is ambiguous. Rather than returning an overwhelming list of results, the assistant
evaluates the request using a confidence scoring system and asks clarifying questions if
needed.
Procedure
1.In the filter navigator field, enter sys_properties.list.
2. In the selection fields, select Name from the drop-down list and enter type_2_disamb in
the Search field.
3. Configure the disambiguation property:
If you have
◦Now Assist in Virtual Agent or
◦Now Assist panel (standard chat, enhanced chat, or premium chat)
then use this configuration:
Property Possible values Default value Definition
sn_aia.type_2_disamb off/low/high off
◦off - clarification
is disabled. The
assistant responds

<!-- page 155 -->
Property Possible values Default value Definition
directly to all
queries without
asking follow-up
questions.
◦low - clarification is
triggered for highly
ambiguous queries.
◦high - clarification
is triggered more
frequently, covering
a broader range of
ambiguous queries.
4.To view the disambiguation data, in the filter navigator field, enter
sys_generative_ai_log.
Configure response feedback
Configure the response feedback options that appear when users select thumbs up or thumbs
down on a Now Assist in Virtual Agent or Now Assist panel response.
Before you begin
Role required: admin
Procedure
1.In the filter navigator field, enter
sys_now_assist_deployment_config_attributes.list to display the Now
Assist Deployment Config Attributes table.
2. In the selection fields, select Name from the drop-down list and enter granular in the
Search field.
3. If you want to change whether negative granular feedback is enabled for Now Assist in Virtual
Agent, select is_negative_granular_feedback_enabled that has Now Assist in Virtual Agent
(default) as the Deployment Configuration.
4.On the next screen, change the value to true if you want negative granular feedback to be
enabled or to false if you do not want negative granular feedback to be enabled.
5. Select Submit.
6.If you want to change whether positive granular feedback is enabled for Now Assist in Virtual
Agent, select is_positive_granular_feedback_enabled that has Now Assist in Virtual Agent
(default) as the Deployment Configuration.
7.On the next screen, change the value to true if you want positive granular feedback to be
enabled or to false if you do not want positive granular feedback to be enabled.
8.Select Submit.
9.To configure the feedback options, in the filter navigator field, enter
sys_now_assist_message_bundle.list to display the Now Assist Message Bundles
table.
10.In the selection fields, select for text from the drop-down list and enter granular in the
Search field.
11. Do one of the following: