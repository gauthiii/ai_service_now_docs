# Explore

## SOURCE INFORMATION

* SECTION NAME: Now Assist in Document Intelligence
* SUBSECTION NAME: Explore
* SOURCE FILE NAME: Now Assist in Document Intelligence.pdf
* PAGE RANGE: 1502-1510 (includes section landing content on 1502-1503; TOC subsection begins on 1504)
* EXTRACTION DATE: 2026-06-17

---

# CONTENT

> Source page: 1502

## Boundary content appearing before the Now Assist in Document Intelligence section heading

None.
Special considerations
None.
ML Report User [ml_report_user]
Can read the ml_predictor_results table and the ml_predictor_results_task table.
Contains Roles
List of roles contained within the role.
pa_viewer
Groups
List of groups this role is assigned to by default.
None.
Special considerations
None.


This boundary content appears above the `Now Assist in Document Intelligence` section heading on source page 1502. It is preserved here for page-completeness review and is not treated as Now Assist in Document Intelligence subsection content.


> Source page: 1502

Now Assist in Document Intelligence
With ServiceNow® Now Assist in Document Intelligence, you can use generative AI to get key
information from digital documents into your automation workflows.
https://player.vimeo.com/video/1164703930?
h=61afcd70f4&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479
Get started
Explore
Learn about the generative AI
skills that are available in Now
Assist in Document Intelligence
Configure
Activate Now Assist in
Document Intelligence and
configure the generative AI skills


> Source page: 1503

Use
Use the generative AI capabilities
that are offered by Now Assist
in Document Intelligence
Reference
Get details about forms, tables, and more
Important:
• Not all model providers are available for customers with in-country SKUs, and some Now
Assist products/features are currently unavailable for in-country customers. For more
information, see the KB1584492
article in the Now Support Knowledge Base. Be sure to
check for model provider availability updates in future releases.
• Some Now Assist products/features are currently unavailable for customers in the
FedRAMP, NSC DOD IL5, or Australia IRAP-Protected data centers, self-hosted
customers, or in other restricted environments. For more information, see the
KB0743854
article in the Now Support Knowledge Base . Be sure to check for availability
updates in future releases.
• Some Now Assist products/features are currently available only for customers in some
regions. Be sure to check for availability updates in future releases.
• Some AI products and skills are not available in Regulated Markets. For more information,
see KB2593939: Regulated Markets AI Products/Skills Not Available
. Be sure to check
for availability updates in future releases.
Troubleshoot and get help
• Additional resources for AI products and solutions.
• ServiceNow Community on AI and Intelligence
.
• Access real-time courses, self-paced training, and career resources at ServiceNow
University
.
• Search the Known Error Portal
for known error articles.
• Contact Customer Service and Support
.
None of the Advanced AI and Data Products provide legal or professional advice. The outputs provided by the Advanced AI and Data Products are for
informational purposes only and are not a substitute for advice from a qualified professional. Customer assumes all responsibility and obligations with respect
to any decisions, advice, conclusions, legal opinions, recommendations made or given as a result of the use of the services, including without limitation, any
decision made, or action taken by Customer in reliance upon the Advanced AI and Data Products.
The Advance AI and Data Products and services do not and are not intended to constitute legal advice and do not create an attorney-client relationship.
AI limitations
This application uses artificial intelligence (AI) and machine learning, which are rapidly evolving fields of study that generate predictions based on patterns
in data. As a result, this application may not always produce accurate, complete, or appropriate information. Furthermore, there is no guarantee that this
application has been fully trained or tested for your use case. To mitigate these issues, it is your responsibility to test and evaluate your use of this application for
accuracy, harm, and appropriateness for your use case, employ human oversight of output, and refrain from relying solely on AI-generated outputs for decision-
making purposes. This is especially important if you choose to deploy this application in areas with consequential impacts such as healthcare, finance, legal,
employment, security, or infrastructure. You agree to abide by ServiceNow’s AI Acceptable Use Policy
, which may be updated by ServiceNow.


> Source page: 1504

Data processing
This application requires data to be transferred from ServiceNow customers' individual instances to a centralized ServiceNow environment, which may be located
in a different data center region from the one where your instance is, and potentially to a third-party cloud provider, such as Microsoft Azure. This data is handled
per ServiceNow's internal policies and procedures, including our policies available through our CORE Compliance Portal
.
Data collection
ServiceNow collects and uses the inputs, outputs, and edits to outputs of this application to develop and improve ServiceNow technologies including ServiceNow
models and AI products. In addition, this application will collect information extracted from documents. Customers can opt out of future data collection at any
time, as described in the Now Assist Opt-Out page.
For more information, see the Now Assist documentation.
Exploring Now Assist in Document Intelligence
With Now Assist in Document Intelligence, you can use generative AI to extract key information
from your documents and images for use in your workflows.
Now Assist in Document Intelligence overview
Now Assist in Document Intelligence makes the following generative AI capabilities available:
• Extract information from documents. Extract information in the form of fields, tables, and
answers to predefined questions from documents and image files. The information can be
reviewed by agents in the Document Intelligence workspace, stored in mapped fields, and
used as defined in the workflow.
• Document Q&A: Agents can save time when reviewing documents by using the predictive
capabilities of generative AI to provide answers to predefined questions.
• Document and visual insights AI agent. The AI agent gathers context from user input and
document or image attachments, generates the requested information based on the content,
and provides the information along with any relevant task details. For more information on AI
agents, see Document and visual insights AI agent.
• Contract metadata extraction and contract analysis. The skills for contract metadata extraction
and contract analysis are only available with the Now Assist in Contract Management
application. For more information, see Now Assist in Contract Management
.
• Attachment summarization. Agents can view a summary of attachment content along with the
record summary in ITSM. Attachment summarization is available in Now Assist for ITSM. For
more information, see Customize a Now Assist for IT Service Management (ITSM) skill
.
• Document chat. Agents can receive chat responses based on document content. Document
chat is available in Now Assist for Virtual Agent. For more information, see Upload documents
in a chat
.
• Invoice data extraction. Extract invoice details from PDFs submitted through email or supplier
portal and automatically process the digitized invoice within Accounts Payable Operations
(APO). For more information, see Now Assist for Accounts Payable Operations (APO)
.
• ESG information extraction. Extract ESG-related information from invoices to support
Operational Sustainability Management (ESG) initiatives and regulatory compliance. For
more information, see Filter citations documents for Operational Sustainability Management
(formerly ESG Management)
.
Now Assist in Document Intelligence skills
Now Assist in Document Intelligence skills are enabled in the Platform workflow on the Now
Assist Admin Console. For more information on activating the skills, see Activate a Now Assist in
Document Intelligence skill.


> Source page: 1505

Extract information from documents
The extract information from documents skill allows you to use Now Assist
predictions to extract fields and tables and find answers to predefined questions
from a document or image. Agents can review and edit predictions in the Document
Intelligence workspace. For more information, see Review extracted information in
the Document Intelligence workspace.
Multimodal chat
The multimodal chat skill is used to enable chat responses about the content
of uploaded documents and images. It is only used on the server side by the
document and visual insights AI agent and by the question answering capability
in Now Assist for Virtual Agent. This skill doesn’t require configuration in the Now
Assist Admin console.
For more information on these capabilities, see Document and visual insights AI
agent and Upload documents in a chat
.
Now Assist in Document Intelligence workflow
The following diagram shows how the Now Assist in Document Intelligence skills are set up and
used to process documents.


> Source page: 1506

Now Assist in Document Intelligence flow
In this workflow:
• An admin activates a skill and sets up a use case for it.
• A workflow integration creates a document task as part of its flow.
• A document is uploaded for processing in a document task.
• Now Assist processes the document and makes predictions based on the fields defined in the
use case.
• If the use case is not set to full automation, the task is sent to a live agent for review.


> Source page: 1507

• The agent provides input to validate or correct the values predicted by Now Assist.
• The task is completed and the integrated workflow proceeds as defined.
Now Assist in Document Intelligence benefits
Now Assist in Document Intelligence provides the following benefits.
Benefit
Feature
User
Start fast with a guided set up
of your use cases to identify
the information you want to
get from your documents.
Set up document intelligence
use cases
DocIntel Admin
[sn_docintel.admin]
DocIntel Manager
[sn_docintel.manager]
Accelerate the extraction of
information from documents
in the form of fields, tables,
and answers to predefined
questions, and turn it into
structured data in the
platform.
Review extracted information
in the Document Intelligence
workspace
DocIntel Extraction Agent
[sn_docintel.extraction_agent]
Use cases in Now Assist in Document Intelligence
In Now Assist in Document Intelligence, a use case is used to define the information you want
generative AI to detect from a document.
Use cases for Now Assist in Document Intelligence skills
Now Assist in Document Intelligence supports use cases for the following skills:
Extract information from documents
In an extract information use case, define the information you want Now Assist to
extract from a document in the form of fields, tables, and questions.
You can define a specific field to extract, a table structure with multiple columns, or
a question you want generative AI to answer based on the text in a document.
For example, if you need to process information from purchase order forms, you
may want a use case with fields to extract the form date and number, a table to
extract the itemized list with prices, and questions such as “Does the order include
any items with ‘gift card’ in the description".
Use case structure
A use case is made up of the use case record and its related fields, tables, and questions as well
as any integrations, and flows.
Now Assist in Document Intelligence uses fields to identify the specific information in documents
to consider when making predictions. Tables are used to extract information in the cells that
appear under table columns. Questions are used to produce an answer based on analysis of the
text in a document.


> Source page: 1508

Use case setup
Use the Now Assist Features interface to set up use cases for Now Assist in Document
Intelligence skills. Use cases for the Document Intelligence application have a separate setup
process. For more information, see Configuring Document Intelligence.
Use case setup involves defining the use case name and details, defining the fields, tables, and
questions, setting up integrations and flows, and testing the use case.
For more information, see Set up a use case for Now Assist in Document Intelligence.
Tip: To save time when you need to create a new use case that shares a similar structure
to another, make a copy of the existing use case and edit the details of the copy. For more
information, see Make a copy of a use case in Now Assist in Document Intelligence.
Once you completed the setup of a use case, agents can begin processing documents for it.
Document Intelligence workspace with Now Assist
Use the Document Intelligence workspace to review the generative AI predictions made by Now
Assist for a document or image file. You can also identify missing information in the file.
Overview of the Document Intelligence workspace with Now Assist
The Document Intelligence workspace provides document management features that enable
you to quickly review and process documents and image files.
With the Document Intelligence workspace, you can:
• Efficiently review the generative AI recommendations and confirm your file's extracted text.
• Review generative AI’s answers to predefined questions to derive key information from your
file.
• Identify missing information and review pending items.
Layout of the Document Intelligence workspace
The following illustration shows the Document Intelligence workspace. The workspace includes
the following areas:
• 1 - Thumbnail panel
• 2 - Document image panel
• 3 - Document controls
• 4 - Extraction review panel
• 5 - Table panel


> Source page: 1509

Document Intelligence workspace
Thumbnail panel
In the thumbnail panel of the workspace, you can select one page from a multiple-page
document. The selected page is displayed in the document image panel. Selecting a page does
not affect what is displayed in the document fields panel.
Document image panel
The document image panel displays the page selected in the thumbnail panel.
If Now Assist can detect the source of its prediction in the document, it will highlight it in the
document image panel when you select a field to review.
Document controls
When you are reviewing a document for extraction, you can use various controls to maximize the
viewing area, zoom, or focus on the areas that you need.
You can also extract information directly from the document image using the draw tool. For more
details, see Extract fields using the draw tool.


> Source page: 1510

Extraction review panel
The extraction review panel enables you to open items for review, including viewing the
generative AI predictions. You can also mark fields as missing in the document.
Note: An asterisk indicates a required field.
Table panel
The table panel enables you to open table rows for review, including viewing the generative AI
recommendations. You can also flag fields or mark fields as missing in the document. Additional
table controls allow you to insert rows and resize columns as needed.
Note: An asterisk in the column heading indicates a required field.
Supporting information for Now Assist in Document Intelligence
Get a quick overview of the important information that is related to the Now Assist in Document
Intelligence application.
Supported versions
Now Assist in Document Intelligence is supported starting with Yokohama (Patch 1).
• Now Assist Admin Console v5.0
• Now Assist for Platform 7.0
• Document Intelligence v6.0
• Now Assist in Document Intelligence v2.0
Supported user interfaces
The Now Assist in Document Intelligence application is supported for the Document Intelligence
workspace.
For more information, see Document Intelligence workspace with Now Assist.
Supported languages
Now Assist in Document Intelligence supports text in multiple languages. For information on
supported languages, see Languages supported by Now Assist in Document Intelligence.
Application information
Now Assist in Document Intelligence skills are available in the Platform workflow.
Activate the Now Assist in Document Intelligence store app (sn_docintel_gen_ai) to configure the
document extraction and Q&A skills.
This store app has the following dependencies:
• Now Assist Admin Console (sn_nowassist_admin)
• Now Assist for Platform (sn_genai_platform)
• Document Intelligence (sn_docintel)
For more information, see Configuring Now Assist in Document Intelligence.

---

## IMAGE DESCRIPTIONS

### Repeated ServiceNow header logo and footer marks - source pages 1502-1510

The ServiceNow logo appears in the upper-left corner on each page and the recurring copyright/trademark footer appears at the bottom. These elements are branding/navigation artifacts rather than subsection content, but they were reviewed on every assigned page. They are not duplicated as substantive content in the extracted body.

### Get started tile layout - source pages 1502-1503

Assets: `_assets/images/p1502_get_started_explore_configure_tiles.png`, `_assets/images/p1503_get_started_use_reference_tiles.png`

The section landing page uses a two-by-two tile layout split across pages 1502 and 1503. The visible tiles are **Explore**, **Configure**, **Use**, and **Reference**. Each tile has an icon and a short purpose statement. The **Explore** tile uses a compass-like icon and says that it is for learning about the generative AI skills available in Now Assist in Document Intelligence. The **Configure** tile uses a wrench/gear icon and says it is for activating Now Assist in Document Intelligence and configuring the generative AI skills. The **Use** tile uses a person icon and says it is for using the generative AI capabilities offered by Now Assist in Document Intelligence. The **Reference** tile uses an open-book icon and says it is for details about forms, tables, and more. The layout establishes the same four navigation categories used by the TOC and by the generated Markdown files.

### Important availability callout - source page 1503

Asset: `_assets/images/p1503_important_availability_callout.png`

A blue **Important** callout with an information icon lists deployment and availability caveats. It states that not all model providers are available for customers with in-country SKUs, that some Now Assist products/features are unavailable for FedRAMP, NSC DOD IL5, Australia IRAP-Protected data centers, self-hosted customers, or other restricted environments, that some products/features are region-limited, and that some AI products and skills are not available in Regulated Markets. The callout visually separates compliance/availability warnings from the general section introduction.

### Now Assist in Document Intelligence flow figure area - source pages 1505-1507

Asset: `_assets/images/p1506_now_assist_document_intelligence_flow.png`

The source text introduces a diagram named **Now Assist in Document Intelligence flow**. In the rendered PDF, the central graphic area on page 1506 is visually blank/invisible in both PDFium and Poppler renderers, while the page text layer provides the diagram title and workflow notes. The visible/extracted workflow notes identify the components and sequence: an admin activates a skill and sets up a use case; a workflow integration creates a document task; a document is uploaded for processing; Now Assist processes the document and makes predictions based on fields defined in the use case; if the use case is not set to full automation, the task is sent to a live agent for review; the agent validates or corrects values predicted by Now Assist; the task is completed and the integrated workflow proceeds as defined. The business purpose is to show the relationship between administrative setup, workflow-triggered document tasks, Now Assist prediction, optional human review, and downstream workflow continuation. No network/security-zone boundaries are visibly shown in the rendered figure.

### Document Intelligence workspace screenshots - source page 1509

Assets: `_assets/images/p1509_document_intelligence_workspace_layout.png`, `_assets/images/p1509_document_controls_detail.png`

The first screenshot shows the Document Intelligence workspace with numbered callouts corresponding to the layout list on page 1508: **1 - Thumbnail panel**, **2 - Document image panel**, **3 - Document controls**, **4 - Extraction review panel**, and **5 - Table panel**. The thumbnail panel appears at the left side for selecting a page from a multi-page document. The document image panel occupies the central review area. The extraction review panel appears on the right for reviewing predicted fields/questions. The table panel appears in the lower area for table-row review. The second screenshot focuses on document controls and shows controls used to maximize the viewing area, zoom, focus on relevant document regions, and support drawing/extracting information directly from the document image. The technical purpose is to orient reviewers to the workspace panels used when validating generative AI extraction results.

### Inline and external-link icons - source pages 1502-1510

Small link icons and UI glyphs are visible near some referenced ServiceNow documentation links. These icons indicate clickable external or related-documentation links in the original HTML/PDF source. They do not change the instructional text but were reviewed as part of page completeness.

### Cropped image inventory for this subsection

* Source page 1502: `_assets/images/p1502_img22_386_529.png` - raster-image - Content icon, tile icon, or UI illustration visible in the source page.
* Source page 1503: `_assets/images/p1503_img3_160_80.png` - raster-image - Content icon, tile icon, or UI illustration visible in the source page.
* Source page 1503: `_assets/images/p1503_img8_386_80.png` - raster-image - Content icon, tile icon, or UI illustration visible in the source page.
* Source page 1509: `_assets/images/p1509_img3_102_51.png` - raster-image - Embedded UI screenshot or large visual image from the source page.
* Source page 1509: `_assets/images/p1509_img9_72_451.png` - raster-image - Embedded UI screenshot or large visual image from the source page.
* Source page 1502: `_assets/images/p1502_get_started_explore_configure_tiles.png` - tile-grid - Get started layout showing Explore and Configure tiles for Now Assist in Document Intelligence.
* Source page 1503: `_assets/images/p1503_get_started_use_reference_tiles.png` - tile-grid - Get started layout showing Use and Reference tiles for Now Assist in Document Intelligence.
* Source page 1503: `_assets/images/p1503_important_availability_callout.png` - callout - Blue Important availability and restricted-environment callout.
* Source page 1506: `_assets/images/p1506_now_assist_document_intelligence_flow.png` - figure - Flow figure area for Now Assist in Document Intelligence workflow. The central graphic area is blank/invisible in both PDFium and Poppler renders; the text layer supplies the flow bullets.
* Source page 1509: `_assets/images/p1509_document_intelligence_workspace_layout.png` - screenshot - Screenshot showing the Document Intelligence workspace layout with numbered panels.
* Source page 1509: `_assets/images/p1509_document_controls_detail.png` - screenshot - Screenshot showing document controls in the Document Intelligence workspace.

---

## TABLES

### Table 1 - source page(s) 1507 - Now Assist in Document Intelligence benefits


* Rows reviewed: 3
* Columns reviewed: 3


| Benefit | Feature | User |
| --- | --- | --- |
| Start fast with a guided set up of your use cases to identify the information you want to get from your documents. | Set up document intelligence use cases | DocIntel Admin [sn_docintel.admin]; DocIntel Manager [sn_docintel.manager] |
| Accelerate the extraction of information from documents in the form of fields, tables, and answers to predefined questions, and turn it into structured data in the platform. | Review extracted information in the Document Intelligence workspace | DocIntel Extraction Agent [sn_docintel.extraction_agent] |

---

## FIGURES

### Figure 1 - Now Assist in Document Intelligence flow - source pages 1505-1507

* Figure title: `Now Assist in Document Intelligence flow`.
* Source asset: `_assets/images/p1506_now_assist_document_intelligence_flow.png`.
* Visible/rendered diagram status: the central visual flowchart is blank/invisible in the rendered page output; the text layer and adjacent bullets supply the figure’s workflow content.
* Components documented from source text: DocIntel Admin/admin setup, skill activation, use case setup, workflow integration, document task, uploaded document, Now Assist processing/prediction, full automation decision, live agent review, corrected/validated values, completed task, and integrated workflow continuation.
* Flow documented from source text: admin activates skill and sets up use case -> workflow integration creates document task -> document is uploaded -> Now Assist processes document and predicts values based on use-case fields -> if not full automation, task goes to live agent -> agent validates/corrects values -> task completes -> integrated workflow proceeds.
* Business purpose: show how setup, document processing, optional human review, and workflow continuation fit together.
* Technical purpose: show the lifecycle of a document task processed by Now Assist in Document Intelligence.
* Security boundaries: no explicit network, data-center, role boundary, or trust-zone boundary is visible in the rendered figure; the surrounding content assigns roles such as DocIntel Admin/Manager/Extraction Agent and describes human review as a control point.

---

## QUALITY ASSURANCE NOTES

* PAGES REVIEWED: 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509, 1510.
* IMAGES REVIEWED: 11 cropped non-logo image/control glyph(s), repeated ServiceNow logos, footer marks, visual callouts, and subsection-specific screenshots/figures. Image inventory: `_assets/image_inventory.csv`.
* TABLES REVIEWED: 1 assigned table(s) converted to Markdown. Table inventory: `_assets/table_inventory.csv`.
* FIGURES REVIEWED: Figure descriptions include source page, asset link, components, connections/flows where applicable, business purpose, technical purpose, and security-boundary notes.
* OCR ISSUES FOUND: PDF text extraction contained recurring footer/header noise, line-wrap artifacts, occasional missing spaces from the PDF text layer, inline icon artifacts, and rendered figure areas on pages 1506 and 1511 that appear blank/invisible despite accessible text-layer workflow descriptions.
* OCR ISSUES CORRECTED: Recurring footer/header noise was removed from CONTENT, hidden/control characters and soft-hyphen artifacts were normalized, obvious missing-space artifacts were corrected when verified by context, shared page boundaries were split at exact source headings, tables were reconstructed into Markdown, and image/figure crops were saved to `_assets/images`.
* SECTION MAPPING NOTES: Page 1502 contains carryover content from the previous `Predictive Intelligence` reference section above the Now Assist in Document Intelligence heading. That content is preserved as boundary material for page-completeness review. Page 1506 and page 1511 contain flow figure areas that render blank/invisible in both PDFium and Poppler; the accessible text layer and adjacent bullets were used and the rendering issue is flagged.
* FILE NAME VERIFIED AGAINST TOC: Yes.
* FOLDER NAME VERIFIED AGAINST TOC: Yes.
* RECHECK PASSES COMPLETED: 12/12: page completeness, text extraction, table extraction, image extraction/documentation, diagram interpretation, section mapping, subsection mapping, file names, folder names, Markdown formatting, missed-content review, and OCR/text-layer cleanup review.
