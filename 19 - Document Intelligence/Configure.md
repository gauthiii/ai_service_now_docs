# Configure
## SOURCE INFORMATION
* SECTION NAME: Document Intelligence
* SUBSECTION NAME: Configure
* SOURCE FILE NAME: Document Intelligence.pdf
* PAGE RANGE: 1541-1567 (page 1541 split at `Configuring Document Intelligence`; page 1567 split before `Integrating Document Intelligence with other applications`)
* EXTRACTION DATE: 2026-06-17

---
# CONTENT
> Source page: 1541

Configuring Document Intelligence
Activate Document Intelligence on your instance and get started with basic configuration.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
1. Install and configure Document Intelligence.
◦Set up Document Intelligence.
Review important information before you start setting up Document Intelligence.
◦Install Document Intelligence.
For the best configuration experience for document extraction use cases, install the
Document Intelligence Admin application.
◦Upgrade to Document Intelligence 3.0 or later from version 2.4 or earlier.
Document Intelligence 3.0 or later includes an updated database schema to support its
transition from a scoped application to a ServiceNow AI Platform plugin.
◦Configure Document Intelligence settings.
Use general settings to control how Document Intelligence displays information to users.
2. Configure Document Intelligence use cases.
Set up Document Intelligence to process different types of documents by telling it what data
you want to extract and what classes or categories you want to apply.
◦Set up document extraction use cases.
Create extraction use cases, add fields and field groups, and configure data extraction
modes to begin extracting data from your documents.
◦Manage document extraction use cases.
> Source page: 1542

Manage your Document Intelligence use cases to support your document extraction
requirements.
◦Set up document classification use cases.
Create classification use cases, add fields (classes), and train your use cases to begin
classifying documents.
◦Manage document classification use cases
Manage your Document Intelligence use cases to support your document classification
requirements.
Set up Document Intelligence
Review the following information before you start setting up Document Intelligence.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Checklist
Setup task
Description
Verify that the ServiceNow core applications or
plugins that are required to support Document
Intelligence are installed and activated.
Verify that the following applications or
plugins are installed and activated from
the ServiceNow Store. When you activate
the first plugin, its dependent plugins are
activated automatically. If not installed,
install and activate one application at a time
in the following order to ensure a smooth
implementation.
• Predictive Intelligence
(com.glide.platform_ml)
• Platform Document Intelligence
(com.glide.platform_ml_di)
• Document Intelligence UIB Component
(sn_docintel_iframe)
For more information, see Install Document
Intelligence.
(Optional) Install the Document Intelligence
Admin application for an improved user
experience for process owners to set up,
configure, and monitor their document
extraction solutions.
Install the Document Intelligence Admin
application from the ServiceNow®  Store.
Review the listing for information on
dependencies, licensing or subscription
requirements, and release compatibility.
Key features of the application include:
> Source page: 1543

Checklist (continued)
Setup task
Description
• Easily configure your document extraction
solutions by defining what you want to
extract from your documents.
• Monitor the performance of your document
extraction solutions and adjust the level of
automation.
Verify that you’ve assigned the required
ServiceNow AI Platform roles.
The following roles are used across the
Document Intelligence features:
• The administrator (admin) installs the
application from the ServiceNow Store and
assigns the roles.
• sn_docintel.admin
• sn_docintel.creation_agent
• sn_docintel.extraction_agent
• sn_docintel.manager
• sn_docintel.viewer
Domain separation
Review the domain separation topic
information if you intend to separate data,
processes, and administrative tasks.
See Domain separation and Document
Intelligence.
Verify that file extensions required to support
Document Intelligence are included in any
glide.attachment.extensions system property
customizations.
The glide.attachment.extensions system
property is empty by default. When
customizing it, ensure that the following file
extensions are included:
• jpeg
• jpg
• png
• pdf
For more information, see Restrict attachment
file extensions
Copy any use cases needed to support your
Document Intelligence implementation.
Follow the steps in Duplicate a document
extraction use case to copy a use case along
with its fields, field groups, integrations, flows,
and all the related machine learning (ML)
models.
Import any use cases needed to support your
Document Intelligence implementation.
Follow the steps in Import a document
extraction use case to import a use case along
> Source page: 1544

Checklist (continued)
Setup task
Description
with its fields, field groups, integrations, flows,
and all the related machine learning (ML)
models.
Install Document Intelligence
You can install Document Intelligence (sn_docintel) and Document Intelligence Admin
(sn_docintel_admin) if you have the admin role. The sn_docintel_admin application installs
related ServiceNow®  Store dependencies if they aren’t already installed.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Before you begin
• Confirm that the application and all of its associated ServiceNow Store applications have valid
ServiceNow entitlements. For more information, see Get entitlement for a ServiceNow product
or application
• Review the Document Intelligence
 application listing in the ServiceNow Store for information
on dependencies, licensing or subscription requirements, and release compatibility.
• Review the Document Intelligence Admin
 application listing in the ServiceNow Store
for information on dependencies, licensing or subscription requirements, and release
compatibility.
• Role required: admin
About this task
The following items are installed with Document Intelligence:
• Plugins
• Roles
• Tables
For more information, see Components installed with Document Intelligence.
Procedure
1. Navigate to All > System Applications > All Available Applications > All.
2. Find the Document Intelligence Admin application (sn_docintel_admin) using the filter criteria
and search bar.
You can search for the application by its name or ID. If you can’t find the application, you might
have to request it from the ServiceNow Store.
In the list next to the Install button, the versions that are available to you’re displayed.
3. Select a version from the list and select Install.
> Source page: 1545

In the Review Installation Details dialog box, any dependencies installed with your application
are listed.
4. If you're prompted, follow the links to the ServiceNow Store to get any additional entitlements
for dependencies.
5. Select Install.
Upgrade to Document Intelligence 3.0 or later from version 2.4 or earlier
Document Intelligence 3.0 or later includes an updated database schema to support its
transition from a scoped application to a ServiceNow AI Platform plugin.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Upgrade tasks
Review the information in this topic before you upgrade to Document Intelligence (DocIntel) 3.0
or later from version 2.4 or earlier.
For more information on installation, see Install Document Intelligence.
Before the upgrade
Document Intelligence 3.0 or later pre-upgrade checklist
Pre-upgrade task
Description
Choose a time to schedule the upgrade
Avoid performing the upgrade during the run
time of the nightly task definition (use case)
upgrade job. Upgrading the application at that
time would prevent use cases from upgrading
until the run time of the next day.
Update any custom code that points directly to
DocIntel database tables
After upgrading to Document Intelligence 3.0
or later from version 2.4 or earlier, DocIntel
will use new flow actions. DocIntel will also
use ServiceNow AI Platform database tables
(sys_di_) in place of the scoped application
tables (di_). All DocIntel data will be migrated
automatically to these platform tables.
Note:  Document extraction use cases
may not be available for use until the
migration is complete.
If you have custom code in your instance
that points directly to the scoped application
tables (di_), it should be updated, preferably to
the platform component using DocIntel APIs.
> Source page: 1546

Document Intelligence 3.0 or later pre-upgrade checklist (continued)
Pre-upgrade task
Description
If you have custom code using DocIntel 2.4 or
earlier flow actions, it should be updated to
use 3.0 or later flow actions.
For the list of tables, see Components
installed with Document Intelligence.
Add cross-scope records for integrations
For any integrations with Document
Intelligence, add cross-scope records for the
new DocIntel database tables.
Note:  Ensure that the existing cross-
scope records for the old tables are not
removed.
See the Cross-scope records section for the
list of records to be added.
For more detail on cross-scope records, see
Cross-scope privilege record
During the upgrade
Document Intelligence 3.0 or later upgrade checklist
Upgrade task
Description
Avoid using the Document Intelligence
workspace to extract fields
Wait until a document task is migrated to
the sys_di_task table before completing it
using the Document Intelligence workspace.
Completing a task during the upgrade may
lead to data loss.
After the upgrade
Document Intelligence 3.0 or later post-upgrade checklist
Post-upgrade task
Description
Test DocIntel integrations and custom
workflows
Test your use case integrations to ensure they
function with the new database schema.
Check for data loss
Some cases where you can lose data include:
• Any action resulting in the attachment
deletion in an old di_task record would
result in a missing attachment for the new
sys_di_task record.
> Source page: 1547

Document Intelligence 3.0 or later post-upgrade checklist (continued)
Post-upgrade task
Description
• Deletion of any new tasks created during
the data migration (that is, during or right
after the 3.0 or later upgrade) would result in
permanent deletion as those records might
not have entries in di_task tables.
• Deletion of an old “process_task” flow (or
any action resulting in that flow deletion)
would result in an empty flow reference in
the new integration setup records.
Post-upgrade migration of legacy use cases
imported through update sets
At any time after the completion of the
Document Intelligence 3.0 or later upgrade
and data migration, you can rerun the
migration batch script that ran during the
upgrade.
You may want to run this script if you must
migrate any imported use cases requiring
migration to the platform tables (sys_di_).
1. Navigate to All > System Definition >
Scheduled jobs.
2. Open the DocIntel migrate
remaining data  scheduled job.
3. Select the Active check box.
4. Select Execute Now.
Warning:  Never use the DocIntel
migrate remaining data  batch
job to rerun migration after deleting all
records from sys_di tables. You should
only use it to migrate missing data from
di_ tables to sys_di tables.
Cross-scope records
Cross-scope records for Document Intelligence 3.0 or later
Source scope
Target scope Target name
Operation Target type Status
Scope of integrating BU global
sys_di_task
Read
Table
Allowed
Scope of integrating BU global
sys_di_key
Read
Table
Allowed
Scope of integrating BU global
sys_di_key_group
Read
Table
Allowed
Scope of integrating BU global
sys_di_ocr_input
Read
Table
Allowed
Scope of integrating BU global
sys_di_pdf_input
Read
Table
Allowed
> Source page: 1548

Cross-scope records for Document Intelligence 3.0 or later (continued)
Source scope
Target scope Target name
Operation Target type Status
Scope of integrating BU global
sys_di_prediction_input Read
Table
Allowed
Scope of integrating BU global
sys_di_training_input
Read
Table
Allowed
Scope of integrating BU global
sys_di_key_hint
Read
Table
Allowed
Configure Document Intelligence settings
Use general settings to control how Document Intelligence displays information to users.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Before you begin
Role required: sn_docintel.admin, sn_docintel.manager, or admin
Procedure
1. Navigate to All > Document Intelligence > Document Data Extraction Administration >
Settings.
2. Adjust the settings as desired.
Note:  The following settings only apply to document extraction features.
DocIntel settings
Setting
Description
Exact match option
Select Auto-sync to enable the exact match
option. This lets the user select an icon to
view only the recommendations that match
exactly what they type.
Candidate score
Select Auto-sync to make confidence scores
visible next to each recommendation.
For more information, see Confidence scores.
Side panels
Select the location of the navigation panel
and document fields panel.
Default width of the extraction panel
Enter the default width of the document fields
(extraction) panel in pixels.
> Source page: 1549

Setting
Description
Default width of the thumbnail panel
Enter the default width of the navigation
(thumbnail) panel in pixels.
Default document fit for the image panel
Select how to display the document in the
document (image) panel.
Set up document extraction use cases
In Document Intelligence, a use case is used to define the structure of a type of document
you want to process. It's made up of the use case record and its related fields, field groups,
integrations, flows, and all the related machine learning (ML) models.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Overview of document extraction use cases
In a document extraction use case, you define the information that you want the AI to detect in
a document. Do this by specifying the type of document to process, the fields to detect, and the
location where document processing results are to be stored.
For example, if you want to process invoice documents, you may want an “Invoice” use case.
This use case could have fields for date, invoice number, item, and so on, to define which
information needs to be extracted from the document.
After you've defined a document extraction use case, agents can begin processing documents
for it in document tasks.
Note:  Use cases for Now Assist in Document Intelligence skills have a separate setup
process. For more information, see Configuring Now Assist in Document Intelligence.
Workflow
Set up a document extraction use case in the following steps.
> Source page: 1550

1. Create a use case.
Define the name, target table, and language for the use case.
2. Create a field for data extraction.
Define the fields that the AI will learn to detect and extract values from.
Define any groupings of fields to help extract and organize data gathered from tables or
information patterns, like check box lists.
3. Configure data extraction modes.
Define how fields should be extracted from documents in a document task.
4. Set up integrations.
Configure an integration to trigger document task processing or value extraction for workflows
with other applications.
As agents work on document tasks to extract field values from individual documents, the AI will
learn from the feedback and continue to improve.
Create a document extraction use case
Create a use case record to define a document you want to process in Document Intelligence.
For example, invoices or driving licenses.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Before you begin
Role required: sn_docintel.manager
Procedure
1. Navigate to All > Document Intelligence > Document Data Extraction Administration > Use
Cases.
2. Select New use case.
3. Enter a name for the use case.
4. Select a target table to store the document processing results for this use case.
5. Optional:  Change the language model used to support document extraction.
For more information, see Languages supported by Document Intelligence.
6. Select Save.
What to do next
After creating a use case, finish setting it up by adding fields and configuring the data extraction
modes.
> Source page: 1551

Create a field for data extraction
Set up fields as part of your use case. Document Intelligence uses fields to identify and extract
data from documents. Fields can be grouped to help DocIntel extract data from documents with
tables, check box lists, and other logical groupings of fields.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Before you begin
Role required: sn_docintel.manager
Procedure
1. Navigate to All > Document Intelligence > Document Data Extraction Administration > Use
Cases.
2. Select a use case in the list.
3. Go to the Fields tab and select Define your fields.
If you have already defined one or more fields and you want to add another field, select New
field.
4. Select the type of data that you want to extract from the document.
You can choose one of the following types of data to extract:
Single field
Single fields are used to extract a single piece of information in the document. For
example, a document number or a customer name.
Check box list
Check box lists are used to extract a check box or a group of check boxes. Each
check box can be checked or cleared.
Table
Tables are used to extract lists or tables of information. A table can have multiple
columns. The number of list items or table rows doesn’t have to be known in
advance.
Single field group
Single field groups are used to extract values that are grouped in the document.
For example, a location with an address, city, and country. Only one item can be
extracted for a single field group, as opposed to the multiple rows extracted for a
table.
A form displays based on the data type you selected.
5. On the form, fill in the fields.
The type of form depends on the type of field that you selected in the previous step.
◦Single field form
◦Single field group form
◦Check box list form
◦Table form
6. Select Save.
> Source page: 1552

Result
The system added the new fields to the Fields list associated with the use case.
Deactivate a data extraction field
Deactivate fields that you don’t want to use as part of your use case.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Before you begin
Role required: sn_docintel.manager
Procedure
1. Navigate to All > Document Intelligence > Document Data Extraction Administration > Use
Cases.
2. Select a use case in the list.
3. Go to the Fields tab and select the field you want to deactivate.
4. On the form, select Deactivate Field.
5. In the confirmation box, select Deactivate.
Warning:  There is no way to reactivate the field after it has been deactivated.
Result
The deactivated field will not be used for data extraction or training.
Configure data extraction modes
Configure the extraction modes for use cases to define how Document Intelligence extracts
fields from documents.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Before you begin
Role required: sn_docintel.manager
About this task
Extraction modes determine how the data is extracted in the document task and how the
task is processed. The mode changes the behavior of the fields in the Document Intelligence
workspace.
DocIntel uses the following extraction modes.
> Source page: 1553

Extraction mode
Description
Recommendation
DocIntel provides recommendations for the
fields in the Document Intelligence workspace.
Choose the recommendation or manually
enter the value. All fields must be reviewed.
Recommendations are ordered based on
how confident the AI is in the prediction.
As DocIntel continues processing your
documents, recommendations improve over
time.
Auto-fill
DocIntel auto-fills the fields in the Document
Intelligence workspace. All fields must be
reviewed.
Auto-fill works only if the AI has enough
confidence to make the prediction. You can
change the confidence threshold by updating
the Auto-fill threshold field in the use case.
Fully automated
(Straight-through processing)
DocIntel automatically extracts the data for
all fields and processes the document task if
the confidence scores for all required fields
are above the defined confidence threshold.
Fields don’t need to be reviewed.
Note:  For Fully automated mode to
process tasks successfully, the use case
must have at least one field designated
as required.
DocIntel becomes more confident over time,
as it processes more and more documents.
Choose Fully automated mode for frequently
processed documents or if you’re confident in
the system.
Procedure
1. Navigate to All > Document Intelligence > Document Data Extraction Administration > Use
Cases.
2. Select the use case that you would like to configure.
3. Select the settings icon (
).
4. Select the extraction mode for the use case.
> Source page: 1554

◦If the DocIntel AI model needs further training to make recommendations with higher
confidence scores, leave the default recommendation mode in place without selecting any
other mode.
◦If DocIntel provides recommendations with confidence scores above the specified
threshold, select the Auto-fill mode option.
◦If DocIntel auto-fills the required fields with very high confidence scores, select the Fully
Automated mode option.
5. Optional:  Adjust the auto-fill threshold and warning threshold for Auto-fill mode.
◦(Optional) Auto-fill threshold: DocIntel only auto-fills the fields if the confidence score of the
top recommendation is at or above the percentage you define.
Fields with a confidence score lower than the threshold are left empty in the Document
Intelligence workspace, and the recommendation mode is available to extract these fields.
◦(Optional) Warning threshold: DocIntel shows a warning for empty fields and auto-filled
fields with a confidence score at or below the percentage that you define.
6. Optional:  Adjust the confidence threshold for required fields in Fully automated mode.
◦(Optional) DocIntel automatically completes and submits the document task if all required
fields have a confidence score at or above the percentage you define in the Fully-
automated threshold field.
◦(Optional) If any required field is below the threshold, the document task isn’t submitted
automatically and requires agent review. Fields that aren’t required may be left empty or
unreviewed.
◦(Optional) If there are no fields defined as required for the document task, then DocIntel
automatically completes and submits the document task.
7. Select Save.
Manage document extraction use cases
Manage your Document Intelligence use cases to efficiently support your document extraction
requirements.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
The following topics describe features that you can use to manage your document extraction use
cases.
• Duplicate a use case and modify it as needed to quickly set up a new use case with similar
fields, field groups, integrations, flows, and all the related machine learning (ML) models.
• Export and import trained use cases to share them across your ServiceNow®  instances.
• Delete a use case if you no longer need to process documents with it.
> Source page: 1555

Duplicate a document extraction use case
Make a copy of a use case to save time when you want to create a new use case that shares a
similar structure to another.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Before you begin
Role required: sn_docintel.manager
About this task
Follow these steps to create a copy of a use case along with its fields, field groups, integrations,
flows, and all related machine learning (ML) models.
Procedure
1. Navigate to All > Document Intelligence > Document Data Extraction Administration > Use
Cases.
2. In the list, select the display name of the use case that you want to copy.
3. On the use case screen, select the Duplicate this use case icon (
).
4. In the Duplicate use case box, type a name for the new use case.
> Source page: 1556

5. Select Duplicate.
Result
The duplicated use case is displayed in the use cases list.
Export a document extraction use case
Export a document extraction use case for use in another ServiceNow instance by adding it to an
update set.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Before you begin
• Ensure both instances have the same family release and the same version of Document
Intelligence installed when exporting and importing use cases.
• Role required: sn_docintel.manager
About this task
Follow these steps to add a document extraction use case to an update set along with its fields,
field groups, integrations, flows, and all related machine learning (ML) models. The update set
can then be exported for use in another instance.
The update set(s) are automatically created and set to "Completed" as a background process.
This process takes several minutes. The resulting update set(s) should not be manually set to
"Completed" or exported before the background job finishes.
For more information, see System update sets
> Source page: 1557

Procedure
1. Navigate to All > Document Intelligence > Document Data Extraction Administration > Use
Cases.
2. In the list, select the display name of the use case you want to export.
3. On the use case screen, select the options icon (
) and select Add to update set.
4. Select Add to update set.
The use case is added to a system update set.
5. Navigate to System Update Sets > Local Update Sets.
6. Select the update set you added.
7. On the update set form, select Export to XML under Related Links.
Import a document extraction use case
Import a document extraction use case for use in your ServiceNow instance.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Before you begin
• Update sets for a document extraction use case are downloaded according to the steps
provided in Export a document extraction use case.
• Ensure both instances have the same family release and the same version of Document
Intelligence installed when exporting and importing use cases.
• Role required: sn_docintel.manager
About this task
Follow these steps to import a document extraction use case along with its fields, field groups,
integrations, flows, and all related machine learning (ML) models.
For more information, see System update sets
Procedure
1. Navigate to All > System Update Sets > Retrieved Update Sets.
2. Under Related Links, select Import Update Set from XML.
3. Select the exported XML file and upload it.
4. Open the update set record.
5. Select Preview Update Set.
There may be a few errors for sys_di_extracted_values, stating Could not find a
record in sys_di_image for column image referenced in this
update.
This error is because those extracted values are empty and don't have a di_image.
6. Select Accept remote update.
> Source page: 1558

7. If there are no other errors, select Commit Update Set.
8. Repeat steps 3 through 7 for each update set.
Result
The use case is imported into the instance and appears in the use cases list.
Delete a document extraction use case
Delete a use case when it’s no longer needed for your documents.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Before you begin
Role required: sn_docintel.manager
Procedure
1. Navigate to All > Document Intelligence > Document Data Extraction Administration > Use
Cases.
2. In the list, select the display name of the use case that you want to delete.
3. On the use case screen, select the options icon (
) and select Delete.
4. In the confirmation box, select Delete.
Result
The use case is deleted, along with the related fields, field groups, integrations, flows, and
machine learning (ML) models.
Set up document classification use cases
A document classification use case is a set of categories used to classify your documents and
their individual pages. It’s made up of the use case record and its related fields (classes), and all
related machine learning (ML) models.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Overview of document classification use cases
In a document classification use case, you define the classes or categories that you want the AI
to detect and apply to a document. Do this by specifying the type of document to process, the
classes to apply, and the location where document processing results are stored.
For example, if you want to process identification documents, you may want an “Identity
Documents” use case. Then, add classes for passports, driver’s licenses, military IDs, and so on,
to label which type of documents are being processed.
> Source page: 1559

After you’ve defined a document classification use case, agents can begin processing
documents for it in document tasks.
Workflow
Set up a document classification use case in the following steps.
1. Create a use case.
Define the name and properties for the use case.
2. Create document classes using fields.
Define the classes or categories that the AI will learn to detect and apply to documents.
3. Train the use case.
Initiate a training job to provide user inputs from completed document tasks to the AI for
continuous improvement.
As agents work on document tasks to classify documents and their individual pages, the AI
learns from the feedback and continues to improve.
Create a document classification use case
Create a use case record to begin defining the classes or categories that you want to apply to a
type of document or pages within the document.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Before you begin
Role required: sn_docintel.manager
Procedure
1. Navigate to All > Document Intelligence > Document Classification > Use Cases.
2. Select New.
3. On the form, fill in the fields.
Use case form
Field
Description
Display Name
The name for the use case as it appears in
the Document Intelligence workspace.
Document Type
Type of document to be processed for the
use case.
Document Config
Configuration of the document to be
processed for the use case.
> Source page: 1560

Field
Description
Autofill Threshold
DocIntel only auto-fills the classes
(fields) if the confidence score of the
top recommendation is at or above the
percentage you define.
Fields with a confidence score lower
than the threshold are left empty in the
Document Intelligence workspace, and the
recommendation mode is available to extract
these fields.
This field is available only if the Auto-fill mode
is enabled.
Fully Automated Threshold
Confidence score threshold for document
classifications, which enables a document
task to be fully automated in the Fully
Automated (Straight Through Processing)
mode.
Warning Threshold
DocIntel shows a warning for empty fields
and auto-filled fields with a confidence score
at or below the percentage that you define.
This field is available only if the Auto-fill mode
is enabled.
4. Select Submit.
What to do next
After creating a use case, finish setting it up by adding fields to create document classes. Then,
train the use case.
Create a document class
Create fields as part of your document classification use case. Document Intelligence uses fields
to define the classes or categories to apply to documents.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Before you begin
Role required: sn_docintel.manager
Procedure
1. Navigate to All > Document Intelligence > Document Classification > Use Cases.
2. Select a use case in the list.
> Source page: 1561

3. Go to the Fields tab and select New.
4. On the form, fill in the fields.
Define a new field form
Field
Description
Display Name
The name for the class as it appears in the
Document Intelligence workspace.
Use Case
The use case associated with this field (class)
record.
Type
The type of field (for example, a text field or a
check box option). Select text.
Active
Option to indicate whether the class is being
used.
5. Select Submit.
Result
The system added the new class field to the Fields list associated with the use case.
Document classification use case with classes
Train a use case
Train the document classification use case with user input from completed document tasks to
improve Document Intelligence recommendations over time.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
> Source page: 1562

Before you begin
• There must be at least one reviewed document task associated with the use case to train it.
Across all reviewed tasks, there must be at least two attachments for each type you defined in
your use case.
Begin by creating a document task and completing it using the Document Intelligence
workspace.
Note:  You won’t be able to process the task until the use case is trained, but you can
complete it by completing all the fields and submitting it.
• Role required: sn_docintel.manager
About this task
Document classification use cases don’t begin with pre-trained AI models, so it’s important to
train the models with user input from completed document tasks.
Note:  To reduce server load and minimize performance issues, the default limit for training
a use case is once every 30 days.
Procedure
1. Navigate to All > Document Intelligence > Document Classification > Use Cases.
2. Select a use case in the list.
3. Select Train Use Case.
DocIntel uses the extracted values from the document tasks in a Done status to train the
model.
Result
The train use case job begins. This job may take several hours to complete.
> Source page: 1563

Example: Test a use case
The following example shows how to train a document classification use case to process
identification documents.
1. You start by creating a document classification use case called Identification. You create a field
for each type of category you want to apply to your identification documents.
In this case, there are fields for a Drivers license, Passport, Military ID, and ID card.
2. Then you create document tasks containing attached examples of the categories you defined
in the fields.
Tip:  You should submit at least 50 documents to adequately train the AI model.
3. You complete the tasks by opening the documents in Document Intelligence workspace,
completing all the fields, and submitting them.
> Source page: 1564

a. Select each document task to open it.
b. Select Show in DocIntel.
c. Fill in the category.
d. Select Submit.
The document tasks will be in a Done state and so become available to train the model.
> Source page: 1565

4. You go back to the Identification use case screen and select Train Use Case.
Manage document classification use cases
Manage your Document Intelligence use cases to efficiently support your document
classification requirements.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
The following topics describe features you can use to manage your document classification use
cases.
Delete a document classification use case
Delete a use case when it's no longer needed for your documents.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Before you begin
Role required: sn_docintel.manager
Procedure
1. Navigate to All > Document Intelligence > Document Classification > Use Cases.
2. In the list, select the display name of the use case you want to delete.
3. On the use case screen, select Delete.
4. In the confirmation box, select Delete.
> Source page: 1566

Result
The use case is deleted along with the related fields, field groups, integrations, flows, and
machine learning (ML) models. The deletion of the related records may trigger their own related
deletions.
Manage field values
View the field values gathered from your processed document tasks. Review the values and add
any additional information.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Before you begin
Role required: sn_docintel.admin or sn_docintel.manager
About this task
When your document task completes, the extracted data or classifications appear in the Field
Values list. The field value form includes more information about the value.
Procedure
1. For document data extraction fields, navigate to All > Document Intelligence > Document Data
Extraction > Field Values.
For document classification fields or classes, navigate to All > Document Intelligence >
Document Classification > Field Values.
2. Select the name of the value (data).
3. On the form, review the fields.
Field
Description
Data
The field value extracted from the document.
Is Reviewed
Indicates whether this field value has been reviewed by a user.
Candidate ID
(Recommendation ID)
Internal system ID for the selected recommendation.
Index
For fields that are part of a field group: the order of the field value
in reference to other field values for the same field.
For regular fields, the index is always 0.
Exact Match
of Candidate
(Recommendation)
Indicates whether the field value exactly matches the AI's top
recommendation.
Field
Field from the use case that the value belongs to.
> Source page: 1567

Field
Description
Candidate
(Recommendation) Rank
Rank that the AI assigned to the selected recommendation.
Is Flagged
Whether a user has flagged this field value in the Document
Intelligence workspace.
Document task
Document task with the attached document from which the data
value was extracted.
Availability
Indicates whether this field value was available or missing in the
document.
Keystrokes
Number of keystrokes that were needed to extract this field value.
Target Record
The record where the field value is used.
Metadata
The metadata associated with the field value.
Target Table
The table that stores the field values.
Domain
Domain linked to this field value.
See Domain separation and Document Intelligence.
4. Select Update.

---
## IMAGE DESCRIPTIONS
Repeated page furniture: each source page includes the ServiceNow logo in the upper-left header and a standard copyright/page-number footer. These repeated layout elements are accounted for globally and not cropped as separate images for every page.

### Image 1: Important deprecation callout in Configure subsection

* Source page: 1541

* Source crop: [_assets/figures/docintel_p1541_figure_manual_05.png](_assets/figures/docintel_p1541_figure_manual_05.png)

* Approximate PDF coordinates: x0=72.0, y0=278.0, x1=523.0, y1=365.0

A blue `Important` callout at the beginning of `Configuring Document Intelligence` repeats the Zurich deprecation preparation notice. It warns that Document Intelligence will be hidden and no longer activated on new instances, while continuing to be supported, and directs users to Now Assist in Document Intelligence.

### Image 2: Document extraction use case workflow screenshot and annotated use case form

* Source page: 1549

* Source crop: [_assets/images/docintel_p1549_img01.png](_assets/images/docintel_p1549_img01.png)

* Approximate PDF coordinates: x0=72.0, y0=443.0, x1=504.0, y1=611.2

An instructional composite screenshot for setting up document extraction use cases. The left side shows a simplified flow from a use case to `Single fields`, `field group (table)`, and `table columns (fields)`, with labels indicating how document information is structured. The right side shows the ServiceNow use case page with a `Use case` header, tabs such as Fields and Field Groups, a Fields list, and highlighted regions for `Fields` and `Field group (table)`. Purple callouts emphasize where the user defines single fields, table field groups, and table columns. The figure explains the relationship between use case records, fields, field groups, and table columns.

### Image 3: Inline UI icon

* Source page: 1553

* Source crop: [_assets/images/docintel_p1553_img01.png](_assets/images/docintel_p1553_img01.png)

* Approximate PDF coordinates: x0=197.2, y0=636.5, x1=212.2, y1=650.7

Small inline UI icon embedded in the procedure, table, or screenshot callout on source page 1553. The icon is used as a visual locator for the adjacent instruction, such as a menu, edit, draw-tool, add-line, remove-line, reorder, status, or field-control icon. The crop is retained for traceability; approximate PDF coordinates are (197.2, 636.5, 212.2, 650.7).

### Image 4: Use Cases list with PC-Invoice selected

* Source page: 1555

* Source crop: [_assets/images/docintel_p1555_img01.png](_assets/images/docintel_p1555_img01.png)

* Approximate PDF coordinates: x0=82.0, y0=342.6, x1=514.0, y1=574.2

A ServiceNow list screenshot. The left application navigator highlights Document Intelligence > Document Data Extraction Administration > `Use Cases`. The main list is titled `Use Cases` and contains rows such as `PC-Invoice` and `Case`; `PC-Invoice` is highlighted with a purple box. The screenshot supports the instruction to open a use case before duplicating it.

### Image 5: Duplicate this use case icon

* Source page: 1555

* Source crop: [_assets/images/docintel_p1555_img02.png](_assets/images/docintel_p1555_img02.png)

* Approximate PDF coordinates: x0=383.0, y0=588.2, x1=398.0, y1=603.2

Small toolbar icon next to the instruction to select the `Duplicate this use case` icon. It identifies the action used to copy a use case. Approximate source coordinates: (383.0, 588.2, 398.0, 603.2).

### Image 6: Duplicate use case modal

* Source page: 1556

* Source crop: [_assets/images/docintel_p1556_img01.png](_assets/images/docintel_p1556_img01.png)

* Approximate PDF coordinates: x0=82.0, y0=39.0, x1=514.0, y1=258.6

A ServiceNow use case page is dimmed behind a modal titled `Duplicate use case`. The use case appears to be `PC-Invoice`; the modal contains a field for the copy name, visible as `Copy of PC-Invoice`, and action buttons `Cancel` and `Duplicate`. A duplicate icon in the page toolbar is highlighted. The image shows the exact place where a manager enters the new use case name and confirms duplication.

### Image 7: Options icon

* Source page: 1557

* Source crop: [_assets/images/docintel_p1557_img01.png](_assets/images/docintel_p1557_img01.png)

* Approximate PDF coordinates: x0=310.0, y0=112.0, x1=325.0, y1=127.0

Small vertical-ellipsis/options icon in the procedure for exporting a use case. It marks the menu used to access export/update-set actions. Approximate source coordinates: (310.0, 112.0, 325.0, 127.0).

### Image 8: Options icon

* Source page: 1558

* Source crop: [_assets/images/docintel_p1558_img01.png](_assets/images/docintel_p1558_img01.png)

* Approximate PDF coordinates: x0=310.0, y0=362.2, x1=325.0, y1=377.2

Small vertical-ellipsis/options icon in the procedure for deleting or managing a use case. It marks the menu that opens available actions. Approximate source coordinates: (310.0, 362.2, 325.0, 377.2).

### Image 9: Document classification use case with classes

* Source page: 1561

* Source crop: [_assets/images/docintel_p1561_img01.png](_assets/images/docintel_p1561_img01.png)

* Approximate PDF coordinates: x0=102.0, y0=391.2, x1=534.0, y1=597.2

A ServiceNow use case form for a document classification use case. The screenshot shows upper fields such as display name, language, thresholds, and target table, with tabs including `Fields` and `Document Tasks`. The Fields list contains class-like entries such as Expense, Survey, and Other, and a `New` button is visible. It illustrates that document classification use cases define fields/classes that represent the possible document categories.

### Image 10: Train use case task list

* Source page: 1562

* Source crop: [_assets/images/docintel_p1562_img01.png](_assets/images/docintel_p1562_img01.png)

* Approximate PDF coordinates: x0=82.0, y0=422.4, x1=514.0, y1=680.8

A Document Intelligence use case screen with a `Train Use Case` button highlighted near the top. The `Document Tasks` tab is selected and shows rows such as PDF, invoice, survey, and mixed document samples. Status values including `New`, `Done`, and `In Progress` are highlighted. The image demonstrates that reviewed document tasks provide training data and that the Train Use Case action becomes relevant after sufficient completed tasks exist.

### Image 11: Identification classification use case classes

* Source page: 1563

* Source crop: [_assets/images/docintel_p1563_img01.png](_assets/images/docintel_p1563_img01.png)

* Approximate PDF coordinates: x0=82.0, y0=172.5, x1=514.0, y1=390.7

A use case screen for an example classification use case, likely `Identification`. A purple box highlights the Display Name field at the top and another highlights the class list in the Fields tab. Visible class names include identification-document categories such as Driver License, Passport, Bank Statement, Survey, and Other. The `New` button is highlighted to show where additional class fields can be added.

### Image 12: Identification use case document tasks

* Source page: 1563

* Source crop: [_assets/images/docintel_p1563_img02.png](_assets/images/docintel_p1563_img02.png)

* Approximate PDF coordinates: x0=82.0, y0=474.5, x1=514.0, y1=692.7

A use case screen with the `Document Tasks` tab selected. The list shows multiple document tasks with document names and processing/review status columns. The `New` button is highlighted. This screenshot supports the example step of creating document tasks and uploading documents so the classification model has examples for training.

### Image 13: Process task action for classification example

* Source page: 1564

* Source crop: [_assets/images/docintel_p1564_img01.png](_assets/images/docintel_p1564_img01.png)

* Approximate PDF coordinates: x0=92.0, y0=95.5, x1=524.0, y1=313.8

A ServiceNow use case/task screen with the `Process Task` button highlighted. The list below shows a task record associated with the example identification use case. The image shows where to start document processing after creating a document task and attaching a sample document.

### Image 14: Classify panel with California driver license sample

* Source page: 1564

* Source crop: [_assets/images/docintel_p1564_img02.png](_assets/images/docintel_p1564_img02.png)

* Approximate PDF coordinates: x0=92.0, y0=378.5, x1=524.0, y1=597.0

A Document Intelligence workspace screenshot showing a sample California driver license image in the document viewer. The right `Classify` panel contains a category recommendation field, with `Driver License` visible as the selected or recommended category, and a `Submit` button in the upper-right. This figure demonstrates reviewing and applying a classification to a document in the workspace.

### Image 15: Train Use Case button after reviewed tasks

* Source page: 1565

* Source crop: [_assets/images/docintel_p1565_img01.png](_assets/images/docintel_p1565_img01.png)

* Approximate PDF coordinates: x0=82.0, y0=77.2, x1=514.0, y1=295.5

A use case screen with the `Train Use Case` button highlighted above a list of document tasks. The tabs include Fields and Document Tasks. The screenshot supports the final training step in the identification example, after sample document tasks have been processed and reviewed.

---
## TABLES
### Table 1: Checklist for setting up Document Intelligence

* Source page: 1542

* Extracted dimensions: 3 rows x 2 columns

| Setup task | Description |
| --- | --- |
| Verify that the ServiceNow core applications or<br>plugins that are required to support Document<br>Intelligence are installed and activated. | Verify that the following applications or<br>plugins are installed and activated from<br>the ServiceNow Store. When you activate<br>the first plugin, its dependent plugins are<br>activated automatically. If not installed,<br>install and activate one application at a time<br>in the following order to ensure a smooth<br>implementation.<br>• Predictive Intelligence<br>(com.glide.platform ml)<br>• Platform Document Intelligence<br>(com.glide.platform ml di)<br>• Document Intelligence UIB Component<br>(sn docintel iframe)<br>For more information, see Install Document<br>Intelligence. |
| (Optional) Install the Document Intelligence<br>Admin application for an improved user<br>experience for process owners to set up,<br>configure, and monitor their document<br>extraction solutions. | Install the Document Intelligence Admin<br>®<br>application from the ServiceNow Store.<br>Review the listing for information on<br>dependencies, licensing or subscription<br>requirements, and release compatibility.<br>Key features of the application include: |

### Table 2: Checklist (continued)

* Source page: 1543

* Extracted dimensions: 7 rows x 2 columns

| Setup task | Description |
| --- | --- |
|  | • Easily configure your document extraction<br>solutions by defining what you want to<br>extract from your documents.<br>• Monitor the performance of your document<br>extraction solutions and adjust the level of<br>automation. |
| Verify that you’ve assigned the required<br>ServiceNow AI Platform roles. | The following roles are used across the<br>Document Intelligence features:<br>• The administrator (admin) installs the<br>application from the ServiceNow Store and<br>assigns the roles.<br>• sn_docintel.admin<br>• sn_docintel.creation_agent<br>• sn_docintel.extraction_agent<br>• sn_docintel.manager<br>• sn_docintel.viewer |
| Domain separation | Review the domain separation topic<br>information if you intend to separate data,<br>processes, and administrative tasks.<br>See Domain separation and Document<br>Intelligence. |
| Verify that file extensions required to support<br>Document Intelligence are included in any<br>glide.attachment.extensions system property<br>customizations. | The glide.attachment.extensions system<br>property is empty by default. When<br>customizing it, ensure that the following file<br>extensions are included:<br>• jpeg<br>• jpg<br>• png<br>• pdf<br>For more information, see Restrict attachment<br>file extensions . |
| Copy any use cases needed to support your<br>Document Intelligence implementation. | Follow the steps in Duplicate a document<br>extraction use case to copy a use case along<br>with its fields, field groups, integrations, flows,<br>and all the related machine learning (ML)<br>models. |
| Import any use cases needed to support your<br>Document Intelligence implementation. | Follow the steps in Import a document<br>extraction use case to import a use case along |

### Table 3: Checklist (continued)

* Source page: 1544

* Extracted dimensions: 2 rows x 2 columns

| Setup task | Description |
| --- | --- |
|  | with its fields, field groups, integrations, flows,<br>and all the related machine learning (ML)<br>models. |

### Table 4: Document Intelligence 3.0 or later pre-upgrade checklist

* Source page: 1545

* Extracted dimensions: 3 rows x 2 columns

| Pre-upgrade task | Description |
| --- | --- |
| Choose a time to schedule the upgrade | Avoid performing the upgrade during the run<br>time of the nightly task definition (use case)<br>upgrade job. Upgrading the application at that<br>time would prevent use cases from upgrading<br>until the run time of the next day. |
| Update any custom code that points directly to<br>DocIntel database tables | After upgrading to Document Intelligence 3.0<br>or later from version 2.4 or earlier, DocIntel<br>will use new flow actions. DocIntel will also<br>use ServiceNow AI Platform database tables<br>(sys_di ) in place of the scoped application<br>tables (di ). All DocIntel data will be migrated<br>automatically to these platform tables.<br>Note: Document extraction use cases<br>may not be available for use until the<br>migration is complete.<br>If you have custom code in your instance<br>that points directly to the scoped application<br>tables (di ), it should be updated, preferably to<br>the platform component using DocIntel APIs. |

### Table 5: Document Intelligence 3.0 or later pre-upgrade checklist (continued)

* Source page: 1546

* Extracted dimensions: 3 rows x 2 columns

| Pre-upgrade task | Description |
| --- | --- |
|  | If you have custom code using DocIntel 2.4 or<br>earlier flow actions, it should be updated to<br>use 3.0 or later flow actions.<br>For the list of tables, see Components<br>installed with Document Intelligence. |
| Add cross-scope records for integrations | For any integrations with Document<br>Intelligence, add cross-scope records for the<br>new DocIntel database tables.<br>Note: Ensure that the existing cross-<br>scope records for the old tables are not<br>removed.<br>See the Cross-scope records section for the<br>list of records to be added.<br>For more detail on cross-scope records, see<br>Cross-scope privilege record . |

### Table 6: Document Intelligence 3.0 or later upgrade checklist

* Source page: 1546

* Extracted dimensions: 2 rows x 2 columns

| Upgrade task | Description |
| --- | --- |
| Avoid using the Document Intelligence<br>workspace to extract fields | Wait until a document task is migrated to<br>the sys_di task table before completing it<br>using the Document Intelligence workspace.<br>Completing a task during the upgrade may<br>lead to data loss. |

### Table 7: Document Intelligence 3.0 or later post-upgrade checklist

* Source page: 1546

* Extracted dimensions: 3 rows x 2 columns

| Post-upgrade task | Description |
| --- | --- |
| Test DocIntel integrations and custom<br>workflows | Test your use case integrations to ensure they<br>function with the new database schema. |
| Check for data loss | Some cases where you can lose data include:<br>• Any action resulting in the attachment<br>deletion in an old di task record would<br>result in a missing attachment for the new<br>sys_di task record. |

### Table 8: Document Intelligence 3.0 or later post-upgrade checklist (continued)

* Source page: 1547

* Extracted dimensions: 3 rows x 2 columns

| Post-upgrade task | Description |
| --- | --- |
|  | • Deletion of any new tasks created during<br>the data migration (that is, during or right<br>after the 3.0 or later upgrade) would result in<br>permanent deletion as those records might<br>not have entries in di task tables.<br>• Deletion of an old “process task” flow (or<br>any action resulting in that flow deletion)<br>would result in an empty flow reference in<br>the new integration setup records. |
| Post-upgrade migration of legacy use cases<br>imported through update sets | At any time after the completion of the<br>Document Intelligence 3.0 or later upgrade<br>and data migration, you can rerun the<br>migration batch script that ran during the<br>upgrade.<br>You may want to run this script if you must<br>migrate any imported use cases requiring<br>migration to the platform tables (sys_di ).<br>1. Navigate to All > System Definition ><br>Scheduled jobs.<br>2. Open the DocIntel migrate<br>remaining data scheduled job.<br>3. Select the Active check box.<br>4. Select Execute Now.<br>Warning: Never use the DocIntel<br>migrate remaining data batch<br>job to rerun migration after deleting all<br>records from sys_di tables. You should<br>only use it to migrate missing data from<br>di tables to sys_di tables. |

### Table 9: Cross-scope records for Document Intelligence 3.0 or later

* Source page: 1547

* Extracted dimensions: 6 rows x 6 columns

| Source scope | Target scope | Target name | Operation | Target type | Status |
| --- | --- | --- | --- | --- | --- |
| Scope of integrating BU | global | sys_di task | Read | Table | Allowed |
| Scope of integrating BU | global | sys_di key | Read | Table | Allowed |
| Scope of integrating BU | global | sys_di key group | Read | Table | Allowed |
| Scope of integrating BU | global | sys_di ocr input | Read | Table | Allowed |
| Scope of integrating BU | global | sys_di pdf input | Read | Table | Allowed |

### Table 10: Cross-scope records for Document Intelligence 3.0 or later (continued)

* Source page: 1548

* Extracted dimensions: 4 rows x 6 columns

| Source scope | Target scope | Target name | Operation | Target type | Status |
| --- | --- | --- | --- | --- | --- |
| Scope of integrating BU | global | sys_di prediction input | Read | Table | Allowed |
| Scope of integrating BU | global | sys_di training input | Read | Table | Allowed |
| Scope of integrating BU | global | sys_di key hint | Read | Table | Allowed |

### Table 11: Document Intelligence settings

* Source page: 1548

* Extracted dimensions: 5 rows x 2 columns

| Setting | Description |
| --- | --- |
| Exact match option | Select Auto-sync to enable the exact match<br>option. This lets the user select an icon to<br>view only the recommendations that match<br>exactly what they type. |
| Candidate score | Select Auto-sync to make confidence scores<br>visible next to each recommendation.<br>For more information, see Confidence scores. |
| Side panels | Select the location of the navigation panel<br>and document fields panel. |
| Default width of the extraction panel | Enter the default width of the document fields<br>(extraction) panel in pixels. |

### Table 12: Document Intelligence settings (continued)

* Source page: 1549

* Extracted dimensions: 3 rows x 2 columns

| Setting | Description |
| --- | --- |
| Default width of the thumbnail panel | Enter the default width of the navigation<br>(thumbnail) panel in pixels. |
| Default document fit for the image panel | Select how to display the document in the<br>document (image) panel. |

### Table 13: Data extraction modes

* Source page: 1553

* Extracted dimensions: 4 rows x 2 columns

| Extraction mode | Description |
| --- | --- |
| Recommendation | DocIntel provides recommendations for the<br>fields in the Document Intelligence workspace.<br>Choose the recommendation or manually<br>enter the value. All fields must be reviewed.<br>Recommendations are ordered based on<br>how confident the AI is in the prediction.<br>As DocIntel continues processing your<br>documents, recommendations improve over<br>time. |
| Auto-fill | DocIntel auto-fills the fields in the Document<br>Intelligence workspace. All fields must be<br>reviewed.<br>Auto-fill works only if the AI has enough<br>confidence to make the prediction. You can<br>change the confidence threshold by updating<br>the Auto-fill threshold field in the use case. |
| Fully automated<br>(Straight-through processing) | DocIntel automatically extracts the data for<br>all fields and processes the document task if<br>the confidence scores for all required fields<br>are above the defined confidence threshold.<br>Fields don’t need to be reviewed.<br>Note: For Fully automated mode to<br>process tasks successfully, the use case<br>must have at least one field designated<br>as required.<br>DocIntel becomes more confident over time,<br>as it processes more and more documents.<br>Choose Fully automated mode for frequently<br>processed documents or if you’re confident in<br>the system. |

### Table 14: Document classification use case form

* Source page: 1559

* Extracted dimensions: 4 rows x 2 columns

| Field | Description |
| --- | --- |
| Display Name | The name for the use case as it appears in<br>the Document Intelligence workspace. |
| Document Type | Type of document to be processed for the<br>use case. |
| Document Config | Configuration of the document to be<br>processed for the use case. |

### Table 15: Document classification use case form (continued)

* Source page: 1560

* Extracted dimensions: 4 rows x 2 columns

| Field | Description |
| --- | --- |
| Autofill Threshold | DocIntel only auto-fills the classes<br>(fields) if the confidence score of the<br>top recommendation is at or above the<br>percentage you define.<br>Fields with a confidence score lower<br>than the threshold are left empty in the<br>Document Intelligence workspace, and the<br>recommendation mode is available to extract<br>these fields.<br>This field is available only if the Auto-fill mode<br>is enabled. |
| Fully Automated Threshold | Confidence score threshold for document<br>classifications, which enables a document<br>task to be fully automated in the Fully<br>Automated (Straight Through Processing)<br>mode. |
| Warning Threshold | DocIntel shows a warning for empty fields<br>and auto-filled fields with a confidence score<br>at or below the percentage that you define.<br>This field is available only if the Auto-fill mode<br>is enabled. |

### Table 16: Define a new field form

* Source page: 1561

* Extracted dimensions: 5 rows x 2 columns

| Field | Description |
| --- | --- |
| Display Name | The name for the class as it appears in the<br>Document Intelligence workspace. |
| Use Case | The use case associated with this field (class)<br>record. |
| Type | The type of field (for example, a text field or a<br>check box option). Select text. |
| Active | Option to indicate whether the class is being<br>used. |

### Table 17: Manage field values form

* Source page: 1566

* Extracted dimensions: 7 rows x 2 columns

| Field | Description |
| --- | --- |
| Data | The field value extracted from the document. |
| Is Reviewed | Indicates whether this field value has been reviewed by a user. |
| Candidate ID<br>(Recommendation ID) | Internal system ID for the selected recommendation. |
| Index | For fields that are part of a field group: the order of the field value<br>in reference to other field values for the same field.<br>For regular fields, the index is always 0. |
| Exact Match<br>of Candidate<br>(Recommendation) | Indicates whether the field value exactly matches the AI's top<br>recommendation. |
| Field | Field from the use case that the value belongs to. |

### Table 18: Manage field values form (continued)

* Source page: 1567

* Extracted dimensions: 10 rows x 2 columns

| Field | Description |
| --- | --- |
| Candidate<br>(Recommendation) Rank | Rank that the AI assigned to the selected recommendation. |
| Is Flagged | Whether a user has flagged this field value in the Document<br>Intelligence workspace. |
| Document task | Document task with the attached document from which the data<br>value was extracted. |
| Availability | Indicates whether this field value was available or missing in the<br>document. |
| Keystrokes | Number of keystrokes that were needed to extract this field value. |
| Target Record | The record where the field value is used. |
| Metadata | The metadata associated with the field value. |
| Target Table | The table that stores the field values. |
| Domain | Domain linked to this field value.<br>See Domain separation and Document Intelligence. |

---
## FIGURES
### Figure 1: Important deprecation callout in Configure subsection

* Source page: 1541

* Source crop: [_assets/figures/docintel_p1541_figure_manual_05.png](_assets/figures/docintel_p1541_figure_manual_05.png)

A blue `Important` callout at the beginning of `Configuring Document Intelligence` repeats the Zurich deprecation preparation notice. It warns that Document Intelligence will be hidden and no longer activated on new instances, while continuing to be supported, and directs users to Now Assist in Document Intelligence.

### Figure 2: Document extraction use case workflow screenshot and annotated use case form

* Source page: 1549

* Source crop: [_assets/images/docintel_p1549_img01.png](_assets/images/docintel_p1549_img01.png)

An instructional composite screenshot for setting up document extraction use cases. The left side shows a simplified flow from a use case to `Single fields`, `field group (table)`, and `table columns (fields)`, with labels indicating how document information is structured. The right side shows the ServiceNow use case page with a `Use case` header, tabs such as Fields and Field Groups, a Fields list, and highlighted regions for `Fields` and `Field group (table)`. Purple callouts emphasize where the user defines single fields, table field groups, and table columns. The figure explains the relationship between use case records, fields, field groups, and table columns.

### Figure 3: Use Cases list with PC-Invoice selected

* Source page: 1555

* Source crop: [_assets/images/docintel_p1555_img01.png](_assets/images/docintel_p1555_img01.png)

A ServiceNow list screenshot. The left application navigator highlights Document Intelligence > Document Data Extraction Administration > `Use Cases`. The main list is titled `Use Cases` and contains rows such as `PC-Invoice` and `Case`; `PC-Invoice` is highlighted with a purple box. The screenshot supports the instruction to open a use case before duplicating it.

### Figure 4: Duplicate use case modal

* Source page: 1556

* Source crop: [_assets/images/docintel_p1556_img01.png](_assets/images/docintel_p1556_img01.png)

A ServiceNow use case page is dimmed behind a modal titled `Duplicate use case`. The use case appears to be `PC-Invoice`; the modal contains a field for the copy name, visible as `Copy of PC-Invoice`, and action buttons `Cancel` and `Duplicate`. A duplicate icon in the page toolbar is highlighted. The image shows the exact place where a manager enters the new use case name and confirms duplication.

### Figure 5: Document classification use case with classes

* Source page: 1561

* Source crop: [_assets/images/docintel_p1561_img01.png](_assets/images/docintel_p1561_img01.png)

A ServiceNow use case form for a document classification use case. The screenshot shows upper fields such as display name, language, thresholds, and target table, with tabs including `Fields` and `Document Tasks`. The Fields list contains class-like entries such as Expense, Survey, and Other, and a `New` button is visible. It illustrates that document classification use cases define fields/classes that represent the possible document categories.

### Figure 6: Train use case task list

* Source page: 1562

* Source crop: [_assets/images/docintel_p1562_img01.png](_assets/images/docintel_p1562_img01.png)

A Document Intelligence use case screen with a `Train Use Case` button highlighted near the top. The `Document Tasks` tab is selected and shows rows such as PDF, invoice, survey, and mixed document samples. Status values including `New`, `Done`, and `In Progress` are highlighted. The image demonstrates that reviewed document tasks provide training data and that the Train Use Case action becomes relevant after sufficient completed tasks exist.

### Figure 7: Identification classification use case classes

* Source page: 1563

* Source crop: [_assets/images/docintel_p1563_img01.png](_assets/images/docintel_p1563_img01.png)

A use case screen for an example classification use case, likely `Identification`. A purple box highlights the Display Name field at the top and another highlights the class list in the Fields tab. Visible class names include identification-document categories such as Driver License, Passport, Bank Statement, Survey, and Other. The `New` button is highlighted to show where additional class fields can be added.

### Figure 8: Identification use case document tasks

* Source page: 1563

* Source crop: [_assets/images/docintel_p1563_img02.png](_assets/images/docintel_p1563_img02.png)

A use case screen with the `Document Tasks` tab selected. The list shows multiple document tasks with document names and processing/review status columns. The `New` button is highlighted. This screenshot supports the example step of creating document tasks and uploading documents so the classification model has examples for training.

### Figure 9: Process task action for classification example

* Source page: 1564

* Source crop: [_assets/images/docintel_p1564_img01.png](_assets/images/docintel_p1564_img01.png)

A ServiceNow use case/task screen with the `Process Task` button highlighted. The list below shows a task record associated with the example identification use case. The image shows where to start document processing after creating a document task and attaching a sample document.

### Figure 10: Classify panel with California driver license sample

* Source page: 1564

* Source crop: [_assets/images/docintel_p1564_img02.png](_assets/images/docintel_p1564_img02.png)

A Document Intelligence workspace screenshot showing a sample California driver license image in the document viewer. The right `Classify` panel contains a category recommendation field, with `Driver License` visible as the selected or recommended category, and a `Submit` button in the upper-right. This figure demonstrates reviewing and applying a classification to a document in the workspace.

### Figure 11: Train Use Case button after reviewed tasks

* Source page: 1565

* Source crop: [_assets/images/docintel_p1565_img01.png](_assets/images/docintel_p1565_img01.png)

A use case screen with the `Train Use Case` button highlighted above a list of document tasks. The tabs include Fields and Document Tasks. The screenshot supports the final training step in the identification example, after sample document tasks have been processed and reviewed.

---
## QUALITY ASSURANCE NOTES
* PAGES REVIEWED: 1541-1567
* IMAGES REVIEWED: 15 non-header image entries; 11 major screenshot/diagram/callout/figure entries. Repeated ServiceNow header logos and footers are documented as page furniture.
* TABLES REVIEWED: 18 table entries assigned to this subsection and converted into Markdown tables in the `TABLES` section.
* FIGURES REVIEWED: 11 major figures/diagrams/screenshots/callouts with detailed component-level descriptions.
* OCR ISSUES FOUND: The PDF contains a selectable text layer, but extraction artifacts were present, including soft-hyphen characters, split link punctuation, ligature-like errors such as `difefrent`/`efefctive`/`fei ld`, and table-extraction spacing issues in bracketed role and table identifiers.
* OCR ISSUES CORRECTED: Soft hyphen and zero-width characters were normalized; repeated footer/page furniture was removed from main content and accounted for in QA; common text-layer artifacts were corrected; tables were separately extracted and converted to Markdown with cleaned cells.
* RECHECK PASSES COMPLETED: 12/12: page completeness, text extraction, table extraction, image extraction/documentation, diagram interpretation, section mapping, subsection mapping, file names, folder names, Markdown formatting, missed-content review, and OCR/text-layer cleanup review.
* SECTION/SUBSECTION MAPPING NOTE: Page 1541 begins at the exact source heading `Configuring Document Intelligence`; benefits-table continuation above that heading is assigned to `Explore`.
* SECTION/SUBSECTION MAPPING NOTE: Page 1567 is shared with `Integrate`; table continuation before `Integrating Document Intelligence with other applications` remains in `Configure`.
* FOOTER/PAGE FURNITURE NOTE: The repeated ServiceNow logo, copyright notice, trademark notice, and page number appear on each source page; they are accounted for globally and removed from repeated content extraction to avoid duplicated page furniture.
