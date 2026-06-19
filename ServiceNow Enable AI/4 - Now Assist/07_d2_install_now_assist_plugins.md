# Install Now Assist plugins

_Source pages: 145–148 | Depth: 2_

---

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