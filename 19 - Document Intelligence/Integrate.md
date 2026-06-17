# Integrate
## SOURCE INFORMATION
* SECTION NAME: Document Intelligence
* SUBSECTION NAME: Integrate
* SOURCE FILE NAME: Document Intelligence.pdf
* PAGE RANGE: 1567-1574 (page 1574 split before `Using Document Intelligence`)
* EXTRACTION DATE: 2026-06-17

---
# CONTENT
> Source page: 1567

Integrating Document Intelligence with other applications
Extend the capabilities of Document Intelligence to other ServiceNow applications. Other
applications can take advantage of document classification and extraction using Document
Intelligence.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Integrate with a custom application or workflow
Configure an integration to trigger document task processing or value extraction. Integrations
can be used to quickly set up flows with other applications.
> Source page: 1568

Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Before you begin
• You must first add a target table to your use case before creating an integration.
• The target table must be readable and writable. Ensure the Can read and Can update
check boxes are selected in the Application Access tab of the target table record. For more
information, see Create a table
• Role required: sn_docintel.admin or sn_docintel.manager
About this task
Define integration points for your Document Intelligence solution. Two integration points are
provided for data extraction use cases: one to automatically create and process Document
Intelligence document tasks, and one to automatically propagate the field values to another
application when extraction has been completed in Document Intelligence. For document
classification use cases, there’s also an integration point to map to a data extraction use case.
Procedure
1. Do one of the following:
a. To integrate a data extraction use case, navigate to All > Document Intelligence > Document
Data Extraction Administration > Use Cases.
b. To integrate a document classification use case, navigate to All > Document Intelligence >
Document Classification > Use Cases.
2. Select the use case for which you want to set up integration points.
3. Do one of the following:
a. For a data extraction use case, go to the Integrations tab and select Set up your first
integration.
If you have already defined one or more integrations and you want to add another, select
New integration.
> Source page: 1569

b. For a document classification use case, go to the Integration Setups tab and select New.
4. On the form, fill in the fields.
Field for data
extraction
Field for
document
classification
Description
Name your
Integration
Name
Name for the integration.
Use case
Use case
Use case to use for the integration task.
Where do you
want to take the
documents from
and store the
extracted data?
Target table
Table to receive data from or send data to.
Note:  The target table is taken from the use case.
What type of
integrations you
want to set?
Type
For data extraction and document classification use
cases, the options include Process Task or Extract
Values. Document classification use cases also have a
Map To Document Data Extraction Use Case option.
The Process Task type creates an integration point to
automatically create and process DocIntel document
tasks based on specific triggers happening in the target
table.
The Extract Values type creates an integration point to
automatically propagate the extracted values to the target
> Source page: 1570

Field for data
extraction
Field for
document
classification
Description
table when extraction has been completed in DocIntel
(that is, when the document task status changes to Done).
The Map To Document Data Extraction Use Case type
creates an integration point that allows a processed
document classification value to automatically create a
new data extraction task.
Conditions
Filters used to select certain fields to use as specific
triggers for the integration.
Process Task only.
Create Flow
Select this option to create a flow for this integration in
Workflow Studio.
This option should be selected, unless you’re planning to
write your own custom script to set up the integration.
5. Do one of the following:
a. For data extraction, select Save.
b. For document classification, select Submit.
Example: Integration
The following images show two example integrations. The first image is a Process Task
integration that triggers when a record needs review. The second image is an Extract Values
integration that can automatically send extracted fields to the invoice table.
> Source page: 1571

New Process Task integration
New Extract Values Integration
What to do next
If you selected to create a flow, finish the activation in Workflow Studio.
> Source page: 1572

For more information, see Building flows
Integrate with Customer Service Management
Document Intelligence provides document extraction capabilities to Customer Service
Management (CSM). Extract relevant information from email and case attachments, such as
credit card numbers or customer addresses, and add that information to cases.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Agents can review values for extracted fields and make corrections as needed by accessing the
Document Intelligence interface directly from the case. From this interface, agents can confirm
correct values, fix incorrect values, and continue to train the model. This Human In the Loop
(HITL) interaction of verifying the recommended values enables agents to refine the model and
continually improve performance.
Create use cases that identify the information to extract from attachments, such as invoices, and
automatically add that information to case fields, depending on the configuration. Labels identify
the extracted fields on the case form.
For more information, see Document Intelligence for CSM
How Document Intelligence works with CSM
When a case is created, the Document Intelligence for CSM feature checks to see:
• If the case has one or more attachments
• If the attachment types are specified in the
sn_csm_ml_task.case.docintel.parsing_supported_types system property
If the case meets those requirements, the feature:
• Identifies the right use case to use based on the case or case type and the use case filters.
• Creates a task using the use case, the sys_id of each attachment, and the case reference.
• Sends the task, attachment sys_ids, and case reference as inputs to the prediction model.
• Uses optical character recognition (OCR) solutions to extract data from the documents.
• Sets the status of the task to Done after the solution has completed.
• If the extraction mode in the use case is set to Fully automated (straight through processing),
the extracted field values are added to the case.
• If the extraction mode is set to Auto-fill or Recommendation, the agent can validate the field
values in the Document Intelligence interface.
Enable Document Intelligence for CSM
Set the system properties and activate the required flows to enable Document Intelligence for
CSM.
See Document Intelligence for Customer Service
> Source page: 1573

Integrate with Financial Services Operations
Document Intelligence provides document extraction capabilities to Financial Services
Operations (FSO).
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Document Intelligence integration with FSO enables machine learning (ML) to assist in quickly
automating document processing and accurately extracting information from documents.
Admins can further integrate Document Intelligence with the FSO Document Processor to enable
users to extract and store fields from a document.
For more information, see Document Intelligence for FSO
How Document Intelligence works with FSO
Document Intelligence works within the Document Processor as follows:
• Creating a Document Type (sn_doc_processor_type) creates a record on DocIntel Use Case
(sys_di_task_definition)
• Creating a Document Attribute (sn_doc_processor_attribute) creates a DocIntel field
(sys_di_key) record
• Updating the Document Attribute record updates the field record
Creating a Document Verification Task (sn_doc_processor_verification_task) creates a DocIntel
Document Task (sys_di_task) if it meets the following requirements:
• Document Verification task has "ocr_processing_needed" checked
• Document Verification task has a document attached
• Document Verification task is in state "Submitted"
After the DocIntel document task is complete, the values should be extracted to the Extracted
Fields (sn_doc_processor_extracted_value) table.
Enable Document Intelligence for FSO
Ensure all the necessary applications and plugins are installed and activated to enable
Document Intelligence in the FSO Document Processor.
See Enable Document Intelligence for FSO
Integrate with Accounts Payable Operations
Document Intelligence provides document extraction capabilities to Accounts Payable
Operations (com.sn_ap_ic).
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
> Source page: 1574

Accounts Payable Operations uses the capabilities of Document Intelligence to extract
information quickly and accurately from invoice documents that are received as email
attachments and then create invoice records in the Accounts Payable Operations application.
For more information, see Accounts Payable Operations integration with Document
Intelligence
How Document Intelligence works with Accounts Payable Operations
DocIntel for Accounts Payable Operations extracts the required information from invoices
received as email attachments, creates invoice records in Accounts Payable Management, and
adds the extracted information into the invoice records.
For more information, see How Accounts Payable Operations integration with Document
Intelligence works
Enable Document Intelligence for Accounts Payable Operations
Ensure all the necessary applications and plugins are installed and activated to enable
Document Intelligence in the Accounts Payable Operations application plugin.
See Components installed with Accounts Payable Operations integration with Document
Intelligence
Integrate with Automation Center
Use Automation Center to discover opportunities to automate document processing with
Document Intelligence.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
In Automation Center, you can view Document Intelligence automation metrics and discover
automation opportunities. For more details on Automation Center, see Automation Center

---
## IMAGE DESCRIPTIONS
Repeated page furniture: each source page includes the ServiceNow logo in the upper-left header and a standard copyright/page-number footer. These repeated layout elements are accounted for globally and not cropped as separate images for every page.

### Image 1: Important deprecation callout in Integrate subsection

* Source page: 1567

* Source crop: [_assets/figures/docintel_p1567_figure_manual_06.png](_assets/figures/docintel_p1567_figure_manual_06.png)

* Approximate PDF coordinates: x0=72.0, y0=538.0, x1=523.0, y1=624.0

A blue `Important` callout at the start of the Integrate subsection repeats the Document Intelligence future deprecation notice and points readers to Now Assist in Document Intelligence for document information extraction.

### Image 2: Integration setup entry point in use case performance screen

* Source page: 1569

* Source crop: [_assets/images/docintel_p1569_img01.png](_assets/images/docintel_p1569_img01.png)

* Approximate PDF coordinates: x0=92.0, y0=39.0, x1=524.0, y1=319.8

A ServiceNow use case page for `Invoice Processing with Tables - TOI` with the `Integrations` tab highlighted. The top contains performance widgets such as `Accuracy of Extraction` and `Agent effort`. In the Integrations related list, the `New Integration` button is highlighted. The image shows the starting point for creating an integration that connects Document Intelligence with a custom workflow or application.

### Image 3: Create Integration modal for Process Task integration

* Source page: 1571

* Source crop: [_assets/images/docintel_p1571_img01.png](_assets/images/docintel_p1571_img01.png)

* Approximate PDF coordinates: x0=102.0, y0=52.0, x1=534.0, y1=376.3

A `Create Integration` modal shows a configuration for processing invoice tasks. Visible fields include `Name your Integration` with `Process invoice tasks`, `Use case` set to `Invoices Processing - Accounts Payable`, a prompt about when to create tasks with value `Invoice`, and an integration type set to `Process Task`. A condition builder row is visible: `State` `is` `Requires Review`, with `or`/`and` controls. The `Create Flow` checkbox is selected, and `Cancel` and `Save` buttons are present. The screenshot explains how to create an integration that creates or processes document tasks when record conditions are met.

### Image 4: Create Integration modal for Extract Values integration

* Source page: 1571

* Source crop: [_assets/images/docintel_p1571_img02.png](_assets/images/docintel_p1571_img02.png)

* Approximate PDF coordinates: x0=102.0, y0=402.5, x1=534.0, y1=702.4

A second `Create Integration` modal shows an extraction integration. Visible fields include `Name your Integration` with `Extract field values to Invoice table`, `Use case` set to `Invoices Processing - Accounts Payable`, document type `Invoice`, and integration type `Extract Values`. The `Create Flow` checkbox is selected, and `Cancel` and `Save` buttons are present. This screenshot explains how extracted DocIntel values can be pushed into an application record or table.

---
## TABLES
### Table 1: Integration setup form

* Source page: 1569

* Extracted dimensions: 5 rows x 3 columns

| Field for data<br>extraction | Field for<br>document<br>classification | Description |
| --- | --- | --- |
| Name your<br>Integration | Name | Name for the integration. |
| Use case | Use case | Use case to use for the integration task. |
| Where do you<br>want to take the<br>documents from<br>and store the<br>extracted data? | Target table | Table to receive data from or send data to.<br>Note: The target table is taken from the use case. |
| What type of<br>integrations you<br>want to set? | Type | For data extraction and document classification use<br>cases, the options include Process Task or Extract<br>Values. Document classification use cases also have a<br>Map To Document Data Extraction Use Case option.<br>The Process Task type creates an integration point to<br>automatically create and process DocIntel document<br>tasks based on specific triggers happening in the target<br>table.<br>The Extract Values type creates an integration point to<br>automatically propagate the extracted values to the target |

### Table 2: Integration setup form (continued)

* Source page: 1570

* Extracted dimensions: 4 rows x 3 columns

| Field for data<br>extraction | Field for<br>document<br>classification | Description |
| --- | --- | --- |
|  |  | table when extraction has been completed in DocIntel<br>(that is, when the document task status changes to Done).<br>The Map To Document Data Extraction Use Case type<br>creates an integration point that allows a processed<br>document classification value to automatically create a<br>new data extraction task. |
| Conditions |  | Filters used to select certain fields to use as specific<br>triggers for the integration.<br>Process Task only. |
| Create Flow |  | Select this option to create a flow for this integration in<br>Workflow Studio.<br>This option should be selected, unless you’re planning to<br>write your own custom script to set up the integration. |

---
## FIGURES
### Figure 1: Important deprecation callout in Integrate subsection

* Source page: 1567

* Source crop: [_assets/figures/docintel_p1567_figure_manual_06.png](_assets/figures/docintel_p1567_figure_manual_06.png)

A blue `Important` callout at the start of the Integrate subsection repeats the Document Intelligence future deprecation notice and points readers to Now Assist in Document Intelligence for document information extraction.

### Figure 2: Integration setup entry point in use case performance screen

* Source page: 1569

* Source crop: [_assets/images/docintel_p1569_img01.png](_assets/images/docintel_p1569_img01.png)

A ServiceNow use case page for `Invoice Processing with Tables - TOI` with the `Integrations` tab highlighted. The top contains performance widgets such as `Accuracy of Extraction` and `Agent effort`. In the Integrations related list, the `New Integration` button is highlighted. The image shows the starting point for creating an integration that connects Document Intelligence with a custom workflow or application.

### Figure 3: Create Integration modal for Process Task integration

* Source page: 1571

* Source crop: [_assets/images/docintel_p1571_img01.png](_assets/images/docintel_p1571_img01.png)

A `Create Integration` modal shows a configuration for processing invoice tasks. Visible fields include `Name your Integration` with `Process invoice tasks`, `Use case` set to `Invoices Processing - Accounts Payable`, a prompt about when to create tasks with value `Invoice`, and an integration type set to `Process Task`. A condition builder row is visible: `State` `is` `Requires Review`, with `or`/`and` controls. The `Create Flow` checkbox is selected, and `Cancel` and `Save` buttons are present. The screenshot explains how to create an integration that creates or processes document tasks when record conditions are met.

### Figure 4: Create Integration modal for Extract Values integration

* Source page: 1571

* Source crop: [_assets/images/docintel_p1571_img02.png](_assets/images/docintel_p1571_img02.png)

A second `Create Integration` modal shows an extraction integration. Visible fields include `Name your Integration` with `Extract field values to Invoice table`, `Use case` set to `Invoices Processing - Accounts Payable`, document type `Invoice`, and integration type `Extract Values`. The `Create Flow` checkbox is selected, and `Cancel` and `Save` buttons are present. This screenshot explains how extracted DocIntel values can be pushed into an application record or table.

---
## QUALITY ASSURANCE NOTES
* PAGES REVIEWED: 1567-1574
* IMAGES REVIEWED: 4 non-header image entries; 4 major screenshot/diagram/callout/figure entries. Repeated ServiceNow header logos and footers are documented as page furniture.
* TABLES REVIEWED: 2 table entries assigned to this subsection and converted into Markdown tables in the `TABLES` section.
* FIGURES REVIEWED: 4 major figures/diagrams/screenshots/callouts with detailed component-level descriptions.
* OCR ISSUES FOUND: The PDF contains a selectable text layer, but extraction artifacts were present, including soft-hyphen characters, split link punctuation, ligature-like errors such as `difefrent`/`efefctive`/`fei ld`, and table-extraction spacing issues in bracketed role and table identifiers.
* OCR ISSUES CORRECTED: Soft hyphen and zero-width characters were normalized; repeated footer/page furniture was removed from main content and accounted for in QA; common text-layer artifacts were corrected; tables were separately extracted and converted to Markdown with cleaned cells.
* RECHECK PASSES COMPLETED: 12/12: page completeness, text extraction, table extraction, image extraction/documentation, diagram interpretation, section mapping, subsection mapping, file names, folder names, Markdown formatting, missed-content review, and OCR/text-layer cleanup review.
* SECTION/SUBSECTION MAPPING NOTE: Page 1567 starts at the exact source heading `Integrating Document Intelligence with other applications`.
* SECTION/SUBSECTION MAPPING NOTE: Page 1574 is shared with `Use`; Accounts Payable Operations integration content before `Using Document Intelligence` remains in `Integrate`.
* FOOTER/PAGE FURNITURE NOTE: The repeated ServiceNow logo, copyright notice, trademark notice, and page number appear on each source page; they are accounted for globally and removed from repeated content extraction to avoid duplicated page furniture.
