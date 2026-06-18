# Configure

## SOURCE INFORMATION

* SECTION NAME: Now Assist in Document Intelligence
* SUBSECTION NAME: Configure
* SOURCE FILE NAME: Now Assist in Document Intelligence.pdf
* PAGE RANGE: 1511-1522 (ends before `Using Now Assist in Document Intelligence` on page 1522)
* EXTRACTION DATE: 2026-06-17

---

# CONTENT

> Source page: 1511

Configuring Now Assist in Document Intelligence
If you have the admin role, you can configure the Now Assist in Document Intelligence feature,
enabling agents to use its generative AI skills within their application workspace.
The following diagram shows the process for setting up the extract information platform skill in
Now Assist.
Now Assist in Document Intelligence configuration steps
In this workflow:
• Install Now Assist.
• Activate the extract information skill in the Platform workflow.
• Create one or more use cases for the skill.
• Define fields, tables, or questions for the use case.
• Test use case performance with a sample document.
• Set up integrations with your workflows.
• Review the use case and activate it.
Activate a Now Assist in Document Intelligence skill
Activate the Now Assist in Document Intelligence skills that agents can use to help analyze and
extract information from documents with generative AI.
Before you begin
Now Assist in Document Intelligence skills are turned on by default. The skills will be
automatically available to appropriate role users for the application. The new default behavior
works as follows:
New customers


> Source page: 1512

When you install a Now Assist product, designated skills are turned on
automatically.
Existing customers who are upgrading (starting with Australia Patch 1)
There is no change to skills that are currently enabled and customized. A skill is
turned on if:
• The Now Assist plugin is installed, but the skill was never turned on.
• An admin has never adjusted roles for the skill.
A skill is not turned on if:
• The skill was previously turned on, and then turned off again.
• An admin has adjusted roles for the skill.
For more information, see Now Assist skills, agents, and agentic workflows on by
default.
Before activating a document intelligence skill in Now Assist, the following applications and their
respective plugins must be installed.
• Now Assist
For more information, see Install Now Assist plugins.
• Document Intelligence
For more information, see Install Document Intelligence.
• Now Assist in Document Intelligence
For more information, see Install Now Assist plugins.
Role required: admin
About this task
Now Assist in Document Intelligence skills are now turned on by default. If a skill was previously
turned on and then turned off, or if an administrator has adjusted roles for the skill, perform the
steps in this task to reactivate the skill.
This task doesn’t apply to the Multimodal chat skill. The multimodal chat skill is used to enable
chat responses about the content of uploaded documents and images. It is only used on
the server side by the document and visual insights AI agent and by the question answering
capability in Now Assist in Virtual Agent. This skill doesn’t require configuration in the Now Assist
Admin console.
Procedure
1. Navigate to All > Now Assist Admin > Skills.
2. In the workflow list, select Platform > Other.
3. In the list of Platform skills, select Activate skill for the document intelligence skill that you
want to activate.
For more information on document intelligence skills, see Exploring Now Assist in Document
Intelligence.
The guided use case setup opens.
4. Create a use case.


> Source page: 1513

a. To create a new use case, follow the steps in Set up a use case for Now Assist in Document
Intelligence.
b. Select Save and continue.
5. Define access.
a. Optional: Define a different access control list (ACL) for the skill.
(Optional) An ACL enables you to restrict who is able to access and execute the skill to only
users with the correct role.
i. Select the Edit icon (
) for Roles.
ii. Select an option.
Option
Description
Any authenticated user
(Optional) As long as a user is logged in,
they can access and execute the skill.
Select roles
(Optional) Select the roles that a user must
have to execute the skill.
Note: If you select multiple roles, a
user must only have one of the roles
to execute the skill.
iii. Select Apply.
b. Select Save and continue.
6. Review and activate.
a. Review the configuration selections you’ve made for the skill.
b. Optional: Select Back to return to a previous step and make a change.
c. Select Activate.
Result
The skill is active and available to the selected user roles.
Set up a use case for Now Assist in Document Intelligence
Create a use case record to define a document you want to process with Now Assist in Document
Intelligence.
Before you begin
• If the Now Assist in Document Intelligence skill has been deactivated, activate the skill. For
more information, see Activate a Now Assist in Document Intelligence skill.
• Role required: Admin, DocIntel Admin, DocIntel Manager


> Source page: 1514

About this task
In a use case, you define the information you want Now Assist to get from a document by
specifying the type of document to process, the fields and tables to detect or questions you want
to ask, and the location where document processing results are stored.
Once you have defined a use case, users can begin processing documents for it in the related
workflows.
For more information on use cases, see Use cases in Now Assist in Document Intelligence.
Procedure
1. Navigate to All > Now Assist Admin > Skills.
2. In the workflow list, select Platform.
3. In the Platform skills list, find the applicable document intelligence skill and select Edit in the
options menu (
).
4. Select New use case.
The guided use case setup opens.
5. Define the use case.
a. Enter a name for the use case.
b. Select a target table to store the document processing results for this use case.
c. Select the language of the files processed for the use case.
If the files contain multiple languages, select the primary language.
For more information, see Languages supported by Now Assist in Document Intelligence.
d. Select the large language model (LLM) that will make predictions for the documents
processed with this use case.
For more information, see Large language models used by Now Assist in Document
Intelligence.
e. Optional: Turn on image mode to process images more efficiently.
(Optional) Image mode sends pages to the LLM as images to leverage the visual capability
of the multimodal LLM as well as any of the languages supported by it.
Note: Selecting image mode reduces the page count limit to 10 pages per file.
The image mode option is available when a multimodal LLM is selected.
Note: Now LLM Service is a text-only model and doesn't support image mode.
f. Select Save and continue.
6. Define information or questions.


> Source page: 1515

a. Select Add a field.
If you have already defined one or more fields, tables, or questions and you want to add
another, select New field.
b. Select the type of information you want to get from the document.
You can choose one of the following:
Field
Fields are used to extract a single piece of information in the document. For
example, a document number or a customer name.
Table
Tables are used to extract lists or tables of information. A table can have
multiple columns. The number of list items or table rows doesn’t have to be
known in advance.
Question
Define the question you want to ask about the document.
A form displays based on the information type you selected.
c. On the form, fill in the fields.
The type of form depends on the type of field.
▪Question form for use case setup
▪Field form for use case setup
▪Table form for use case setup


> Source page: 1516

Field form for document extraction
d. Select Save.
The system adds the new fields, tables, or questions to the Information list associated with
the use case.
e. Optional: To edit or delete a field, table, or question, select the appropriate option in the
options menu (
) of the row.
f. Select Save and Continue.
7. Test the use case performance with a sample document.
Select Test a new document.


> Source page: 1517

a. Select a document.
Option
Description
Upload from record
i. Select Upload from record.
ii. Enter search criteria in the search field.
iii. Select a record from the list.
This option is available when a target table
is selected for the use case.
Upload from this device
i. Select Upload from this device.
ii. Select Add file.
iii. Select a file and select Open.
iv. Select Upload.
b. Select Continue.
Tip: Select the Open in a new tab button (
) to view the document in a larger
workspace on a separate browser tab.
The Document Intelligence workspace appears in a frame on the Test output screen.
c. Review the performance of the skill for the test document.
d. Select Save and continue.
8. Add integrations.
Integrate the document intelligence use case with a workflow.
This option is available when a target table is selected for the use case.
For more information on Document Intelligence integrations, see Integrate with a custom
application or workflow.
a. Select Add integration.
If you have already defined one or more integrations and you want to add another, select
New integration.
b. Enter a name for the integration.
c. Select the type of integration you want to use.
The Process task type creates an integration point to automatically create and process
document tasks based on specific triggers happening in the target table.


> Source page: 1518

The Extract values type creates an integration point to automatically propagate the
extracted values to the target table when extraction has been completed in Now Assist in
Document Intelligence.
d. Use the conditions to select certain fields as specific triggers for the integration.
Conditions are available if you selected Process task in the previous step. For more
information on conditions, see OR conditions
.
e. Optional: Select the Create Flow option to create a flow for this integration in Workflow
Studio.
Tip: This option should be selected, unless you are planning to write your own custom
script to set up the integration. Be sure the integration is activated on Workflow Studio.
For more information, see Building flows
.
f. Select Save.
g. Select Save and continue.
9. Review and activate.
a. Review the configuration selections you’ve made for the use case.
b. Optional: Select Back to return to a previous step and make a change
c. Select Complete setup.
Turn on Full automation mode for a use case
Turn on Full automation mode to automatically complete and submit document tasks without an
agent review. Full automation mode is turned off by default in use cases.
Before you begin
• Set up a use case for a Now Assist in Document Intelligence skill. For more information, see Set
up a use case for Now Assist in Document Intelligence.
• Role required: sn_docintel.manager
About this task
The extraction mode determines how Now Assist in Document Intelligence processes document
tasks for a use case. For more information, see Data extraction modes in Now Assist in Document
Intelligence.
Turn on Full automation mode if you want Now Assist to bypass the agent review used to check
the accuracy of the predicted values. Now Assist auto-fills the values for all required fields
or marks them as missing in the document. Document tasks created for the use case are
automatically completed and submitted by Now Assist.
Warning: Now Assist may not always produce accurate, complete, or appropriate
information. By choosing to bypass the agent review, there is no way to check the accuracy
of the predicted values before using the data in your workflows.
Procedure
1. Navigate to All > Now Assist Admin > Skills.
2. In the workflow list, select Platform.


> Source page: 1519

3. In the Platform skills list, find the applicable document intelligence skill and select Edit in the
options menu (
).
4. Select the use case you would like to configure.
5. Click the settings icon (
).
6. On the Extraction mode screen, select the Full automation mode (no agent review required)
option.
7. Optional: Select the Any required field is missing in the document option to turn off the
automation and require an agent review when any of the required fields are missing in the
document.
8. Close the Settings box.
Change the language models for a use case
Choose the language models for a Now Assist in Document Intelligence use case.
Before you begin
• Set up a use case for the extract information from documents skill. For more information, see
Set up a use case for Now Assist in Document Intelligence.
• Role required: sn_docintel.manager
About this task
Language models are used to detect information in documents and make predictions for
information extraction.
Third-party large language model (LLM) providers are available for Now Assist skills and AI
agents in addition to Now LLM Service. For more information on LLMs in Now Assist, see Manage
AI models.
For each Now Assist in Document Intelligence use case, only one LLM can be enabled at a time.
Now Assist employs the selected LLM when processing documents for the use case.
For image files that need optical character recognition (OCR) to detect the text in them, OCR
models are used to support different language groups. The language selected during use case
setup helps the OCR model to detect text in the images.
Procedure
1. Navigate to All > Now Assist Admin > Skills.
2. In the workflow list, select Platform.
3. In the Platform skills list, find the applicable document intelligence skill and select Edit in the
options menu (
).
4. Select the use case you would like to configure.
5. Select the settings icon (
).
6. Select the Manage LLMs screen.
7. Select the LLM that will make predictions for the documents processed with this use case.
For more information, see Large language models used by Now Assist in Document
Intelligence.
8. Optional: Turn on image mode to process images more efficiently.


> Source page: 1520

(Optional) Image mode sends pages to the LLM as images to leverage the visual capability of
the multimodal LLM as well as any of the languages supported by it.
The image mode option is available when a multimodal LLM is selected.
Note: Selecting image mode reduces the page count limit to 10 pages per file.
9. Select the Language of the files processed for the use case.
If the files contain multiple languages, select the primary language.
For more information, see Languages supported by Now Assist in Document Intelligence.
10. Select Save.
Result
The selected languages are enabled for the use case.
Edit a use case in Now Assist in Document Intelligence
Edit a use case to change the name, fields, tables, questions, and integrations.
Before you begin
Role required: Admin, DocIntel Admin, DocIntel Manager
About this task
Follow these steps to edit a use case along with its fields, tables, questions, integrations, and
flows.
Use cases marked as read-only can’t be edited. However, you can make a copy of a read-only
use case that is editable. For more information, see Make a copy of a use case in Now Assist in
Document Intelligence.
Procedure
1. Navigate to All > Now Assist Admin > Skills.
2. In the workflow list, select Platform.
3. In the Platform skills list, find the applicable document intelligence skill and select Edit in the
options menu (
).
4. In the row of the use case you want to edit, select Edit in the options menu (
).
5. Make changes as needed.
For more information on use case setup, see Set up a use case for Now Assist in Document
Intelligence
Make a copy of a use case in Now Assist in Document Intelligence
Make a copy of a use case to save time when you need to create a new use case with a similar
structure.
Before you begin
Role required: Admin, DocIntel Admin, DocIntel Manager


> Source page: 1521

About this task
Follow these steps to create a copy of a use case along with its fields, tables, questions,
integrations, and flows.
Procedure
1. Navigate to All > Now Assist Admin > Skills.
2. In the workflow list, select Platform.
3. In the Platform skills list, find the applicable document intelligence skill and select Edit in the
options menu (
).
4. In the row of the use case you want to copy, select Make a copy in the options menu (
).
5. In the confirmation box, select Make a copy.
6. Select Continue.
7. Enter a name for the use case.
8. Select Make a copy.
Result
The duplicated use case appears in the use cases list.
What to do next
Edit the new use case to make any necessary changes and test it to make sure it functions
properly.
For more information, see Edit a use case in Now Assist in Document Intelligence.
Deactivate a use case in Now Assist in Document Intelligence
Deactivate a use case that you don’t want to use for your documents.
Before you begin
Role required: Admin, DocIntel Admin, DocIntel Manager
Procedure
1. Navigate to All > Now Assist Admin > Skills.
2. In the workflow list, select Platform.
3. In the Platform skills list, find the applicable document intelligence skill and select Edit in the
options menu (
).
4. In the row of the use case you want to deactivate, select Deactivate in the options menu (
).
5. In the confirmation box, select Yes.
Result
The use case is deactivated. The deactivated use case will not be used for document
processing.
Delete a use case in Now Assist in Document Intelligence
Delete a use case when it is no longer needed for your documents.
Before you begin
Role required: Admin, DocIntel Admin, DocIntel Manager


> Source page: 1522

Procedure
1. Navigate to All > Now Assist Admin > Skills.
2. In the workflow list, select Platform.
3. In the Platform skills list, find the applicable document intelligence skill and select Edit in the
options menu (
).
4. In the row of the use case you want to delete, select Delete in the options menu (
).
5. In the confirmation box, select Delete.
Result
The use case along with the related fields, tables, questions, integrations, and flows are deleted.

---

## IMAGE DESCRIPTIONS

### Repeated ServiceNow header logo and footer marks - source pages 1511-1522

The ServiceNow logo and recurring copyright/trademark footer were reviewed on every assigned page. They are stable branding artifacts and are not repeated as substantive content in the CONTENT section.

### Now Assist in Document Intelligence configuration steps figure area - source page 1511

Asset: `_assets/images/p1511_configuration_steps_figure_area.png`

The page introduces a diagram named **Now Assist in Document Intelligence configuration steps**. The central diagram area renders blank/invisible in both PDFium and Poppler, but the text layer provides the workflow sequence. The identified flow components are: **Install Now Assist**, **Activate the extract information skill in the Platform workflow**, **Create one or more use cases for the skill**, **Define fields, tables, or questions for the use case**, **Test use case performance with a sample document**, **Set up integrations with your workflows**, and **Review the use case and activate it**. The relationship between the steps is linear: prerequisite installation leads to skill activation, use case creation, information definition, testing, integration setup, and activation. The technical purpose is to summarize the configuration lifecycle before the detailed procedures. No network/security-zone boundaries are shown.

### Field form for document extraction screenshot - source page 1516

Asset: `_assets/images/p1516_field_form_for_document_extraction.png`

The screenshot shows a modal-style form labeled **Field name** with tabs **Field** and **Field Assistance**. Visible controls include required **Field name** input, required **Details** text area, required **Field Type** dropdown set to **Text**, **Target table** set to **Invoice task**, **Target field** search input, a checked checkbox labeled **This single field is required for extraction**, a toggle labeled **Create multiple single fields**, and **Cancel** and **Save** buttons at the bottom. The screen demonstrates how administrators define a field for extraction and map it to the target table/field. Required fields are marked with an asterisk. The purpose is to show the UI used in the use-case setup workflow.

### Inline procedure icons - source pages 1513-1522

Multiple small inline icons appear next to instructions, including edit icons, option-menu icons, settings icons, an open-in-new-tab icon, and similar UI glyphs. These icons point users to the exact controls in the Now Assist Admin interface. The recurring vertical-dot option menu is associated with Edit, Make a copy, Deactivate, Delete, and row-level actions. The settings icon is associated with extraction mode and language model configuration. These inline images are represented in `_assets/images` as small control-glyph crops and were reviewed for procedure fidelity.

### Warning callout - source page 1518

A yellow **Warning** callout states that Now Assist may not always produce accurate, complete, or appropriate information, and that bypassing the agent review removes the chance to check predicted values before they are used in workflows. The callout is tied to the full automation configuration procedure and defines a risk boundary between human-reviewed extraction and automated submission.

### Cropped image inventory for this subsection

* Source page 1513: `_assets/images/p1513_img9_199_185.png` - raster-image - Small inline UI icon or control glyph visible in the procedure text.
* Source page 1514: `_assets/images/p1514_img10_154_230.png` - raster-image - Small inline UI icon or control glyph visible in the procedure text.
* Source page 1516: `_assets/images/p1516_img3_122_51.png` - raster-image - Embedded UI screenshot or large visual image from the source page.
* Source page 1516: `_assets/images/p1516_img8_164_523.png` - raster-image - Small inline UI icon or control glyph visible in the procedure text.
* Source page 1517: `_assets/images/p1517_img16_313_337.png` - raster-image - Small inline UI icon or control glyph visible in the procedure text.
* Source page 1519: `_assets/images/p1519_img4_154_57.png` - raster-image - Small inline UI icon or control glyph visible in the procedure text.
* Source page 1519: `_assets/images/p1519_img8_190_99.png` - raster-image - Small inline UI icon or control glyph visible in the procedure text.
* Source page 1519: `_assets/images/p1519_img30_154_594.png` - raster-image - Small inline UI icon or control glyph visible in the procedure text.
* Source page 1519: `_assets/images/p1519_img34_197_636.png` - raster-image - Small inline UI icon or control glyph visible in the procedure text.
* Source page 1520: `_assets/images/p1520_img20_154_508.png` - raster-image - Small inline UI icon or control glyph visible in the procedure text.
* Source page 1520: `_assets/images/p1520_img23_435_532.png` - raster-image - Small inline UI icon or control glyph visible in the procedure text.
* Source page 1521: `_assets/images/p1521_img8_154_160.png` - raster-image - Small inline UI icon or control glyph visible in the procedure text.
* Source page 1521: `_assets/images/p1521_img11_479_184.png` - raster-image - Small inline UI icon or control glyph visible in the procedure text.
* Source page 1521: `_assets/images/p1521_img28_154_551.png` - raster-image - Small inline UI icon or control glyph visible in the procedure text.
* Source page 1521: `_assets/images/p1521_img31_497_575.png` - raster-image - Small inline UI icon or control glyph visible in the procedure text.
* Source page 1522: `_assets/images/p1522_img7_154_112.png` - raster-image - Small inline UI icon or control glyph visible in the procedure text.
* Source page 1522: `_assets/images/p1522_img10_456_136.png` - raster-image - Small inline UI icon or control glyph visible in the procedure text.
* Source page 1522: `_assets/images/p1522_img18_102_333.png` - raster-image - Embedded UI screenshot or large visual image from the source page.
* Source page 1511: `_assets/images/p1511_configuration_steps_figure_area.png` - figure - Figure area for Now Assist in Document Intelligence configuration steps. The central graphic is blank/invisible in rendered PDF; the text layer supplies the workflow bullets.
* Source page 1516: `_assets/images/p1516_field_form_for_document_extraction.png` - screenshot - Screenshot of the Field form for document extraction.
* Source page 1522: `_assets/images/p1522_document_processing_workflow.png` - diagram - Document processing workflow diagram for Now Assist in Document Intelligence.

---

## TABLES

### Table 1 - source page(s) 1513 - Activate skill - Define access options


* Rows reviewed: 3
* Columns reviewed: 2


| Option | Description |
| --- | --- |
| Any authenticated user | (Optional) As long as a user is logged in, they can access and execute the skill. |
| Select roles | (Optional) Select the roles that a user must have to execute the skill. Note: If you select multiple roles, a user must only have one of the roles to execute the skill. |

### Table 2 - source page(s) 1517 - Test use case - document upload options


* Rows reviewed: 3
* Columns reviewed: 2


| Option | Description |
| --- | --- |
| Upload from record | i. Select Upload from record. ii. Enter search criteria in the search field. iii. Select a record from the list. This option is available when a target table is selected for the use case. |
| Upload from this device | i. Select Upload from this device. ii. Select Add file. iii. Select a file and select Open. iv. Select Upload. |

---

## FIGURES

### Figure 1 - Now Assist in Document Intelligence configuration steps - source page 1511

* Figure title: `Now Assist in Document Intelligence configuration steps`.
* Source asset: `_assets/images/p1511_configuration_steps_figure_area.png`.
* Visible/rendered diagram status: the central diagram is blank/invisible in the rendered page output; the text layer provides the full workflow list.
* Components: Now Assist installation, extract information skill activation, use case creation, information definition, sample document testing, workflow integration setup, and use case review/activation.
* Flow: Install Now Assist -> activate extract information skill in the Platform workflow -> create use case(s) -> define fields/tables/questions -> test with a sample document -> set up workflow integrations -> review and activate.
* Business purpose: guide administrators through the order of configuration tasks.
* Technical purpose: identify prerequisites and configuration phases before users process documents.
* Security/role boundary: the text states that the admin role is required for configuration, and access controls/roles can be adjusted during skill activation; no network zones are shown.

---

## QUALITY ASSURANCE NOTES

* PAGES REVIEWED: 1511, 1512, 1513, 1514, 1515, 1516, 1517, 1518, 1519, 1520, 1521, 1522.
* IMAGES REVIEWED: 21 cropped non-logo image/control glyph(s), repeated ServiceNow logos, footer marks, visual callouts, and subsection-specific screenshots/figures. Image inventory: `_assets/image_inventory.csv`.
* TABLES REVIEWED: 2 assigned table(s) converted to Markdown. Table inventory: `_assets/table_inventory.csv`.
* FIGURES REVIEWED: Figure descriptions include source page, asset link, components, connections/flows where applicable, business purpose, technical purpose, and security-boundary notes.
* OCR ISSUES FOUND: PDF text extraction contained recurring footer/header noise, line-wrap artifacts, occasional missing spaces from the PDF text layer, inline icon artifacts, and rendered figure areas on pages 1506 and 1511 that appear blank/invisible despite accessible text-layer workflow descriptions.
* OCR ISSUES CORRECTED: Recurring footer/header noise was removed from CONTENT, hidden/control characters and soft-hyphen artifacts were normalized, obvious missing-space artifacts were corrected when verified by context, shared page boundaries were split at exact source headings, tables were reconstructed into Markdown, and image/figure crops were saved to `_assets/images`.
* SECTION MAPPING NOTES: Page 1522 is a shared boundary page. Content before `Using Now Assist in Document Intelligence` belongs to Configure and content from that heading onward belongs to Use. The configuration-steps diagram area on page 1511 renders blank/invisible; the source text layer provides the workflow bullets and this issue is flagged.
* FILE NAME VERIFIED AGAINST TOC: Yes.
* FOLDER NAME VERIFIED AGAINST TOC: Yes.
* RECHECK PASSES COMPLETED: 12/12: page completeness, text extraction, table extraction, image extraction/documentation, diagram interpretation, section mapping, subsection mapping, file names, folder names, Markdown formatting, missed-content review, and OCR/text-layer cleanup review.
