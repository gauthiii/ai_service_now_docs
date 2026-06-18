# Reference

## SOURCE INFORMATION

* SECTION NAME: Now Assist in Document Intelligence
* SUBSECTION NAME: Reference
* SOURCE FILE NAME: Now Assist in Document Intelligence.pdf
* PAGE RANGE: 1524-1536 (starts at `Now Assist in Document Intelligence reference` on page 1524; page 1537 is next-section boundary content)
* EXTRACTION DATE: 2026-06-17

---

# CONTENT

> Source page: 1524

Now Assist in Document Intelligence reference
The following topics provide additional information about the features and properties installed
with Now Assist in Document Intelligence.
Components installed with Now Assist in Document Intelligence
Components are installed with the activation of Now Assist in Document Intelligence.
Roles installed
There are no roles installed with Now Assist in Document Intelligence. It uses the same roles
included with the Document Intelligence application.
For more information, see Components installed with Document Intelligence.


> Source page: 1525

Tables installed
Now Assist in Document Intelligence uses the same tables included with the Document
Intelligence application.
For more information, see Components installed with Document Intelligence.
Data extraction modes in Now Assist in Document Intelligence
The extraction mode determines how Now Assist in Document Intelligence processes a
document task.
Now Assist in Document Intelligence uses the following data extraction modes.
Extraction mode
Description
Default
Now Assist auto-fills each field in the
Document Intelligence workspace if it
recognizes a value for it in the document.
Now Assist may not always produce accurate,
complete, or appropriate information. All fields
should be reviewed for accuracy.
A reviewer can accept the predicted value or
manually enter a value.
Full automation
Now Assist automatically completes and
submits the document task without an agent
review. The values for all required fields are
auto-filled by Now Assist or are identified as
missing in the document.
By turning on Full automation mode, the agent
review used to check the accuracy of the
predicted values is bypassed.
There is a configuration option to suspend the
automation and require an agent review when
any of the required fields are missing in the
document.
Document and visual insights AI agent
The document and visual insights AI agent gathers context from user input and document or
image attachments, generates the requested information based on the content, and provides the
information along with any relevant task details.
Document and visual insights AI agent overview
The document and visual insights AI agent performs tasks to process documents and images.
Data extraction
Extract specific information.
Summarization


> Source page: 1526

Summarize the key topics of documents and images.
Question answering (Q&A)
Answer questions about the document or image content.
The document and visual insights AI agent is not typically used in standalone mode and any use
case can access it. For more information on AI agents, see Now Assist AI agents.
Role masking enables users to limit the roles and privileges of AI agents during tool execution.
AI agents that get installed with Now Assist applications are assigned pre-defined roles. If you
select Users with specific roles for user access, you must configure the security
controls to include these roles. Data access settings must also include these roles. For the
instructions to change the security controls, see Define security controls for an AI agent.
AI agent actions
When used, the AI agent may attempt the following actions:
• Determine the type of task to perform based on information provided by the user.
◦Data extraction
◦Summarization
◦Question answering (Q&A)
• Retrieve the relevant record details.
• Initiate the process based on the type of task.
• Provide the task results as directed.
• Prompt the user to upload a file for processing.
• Display the results of the AI agent actions in a document view screen.
• Provide citation sources.
• Notify the user of task completion and next steps.
Document Intelligence tool for Now Assist Skill Kit
Use the Document Intelligence tool to leverage extraction, question answering, and
summarization capabilities for a skill created with Now Assist Skill Kit.
Document Intelligence tool overview
A tool is a utility in Now Assist Skill Kit that is configured to convert skill inputs into skill outputs.
The Document Intelligence tool uses generative AI capabilities to extract information and
insights from document and image files. The extracted information is turned into structured data
that can be used in the platform.
You can use the tool editor to configure the Document Intelligence tool.


> Source page: 1527

Document Intelligence tool in the Tool Editor
For more information on adding the Document Intelligence tool to a custom skill in Now Assist
Skill Kit, see Add Document Intelligence.
Document Intelligence tool actions
The Document Intelligence tool provides the following capabilities for a custom skill to process
documents and images.
Ask a question
Define a question to ask the large language model (LLM) about the content of a file
attachment.
Extract information
Pull structured data and insights from file content.
Extract values from the files based on the fields, tables, and questions defined in a
Now Assist in Document Intelligence use case. Use an existing use case or create a
new one that meets the needs of your custom skill.
Summarize files
Generate a concise summary the key topics of the file content.
For more information on creating custom Now Assist prompts and skills, see Now Assist Skill Kit.
Field types in Now Assist in Document Intelligence
The field type specifies the information that is retrieved from a document with Now Assist in
Document Intelligence.
The following field types are available to administrators when configuring fields for use cases.
Note: Some field types convert the extracted value into a standard format. For more
information, see Data normalization.
Now Assist in Document Intelligence field types
Field type
Description
Boolean (True/False)
Holds a true/false value. In document Q&A
questions, the value is displayed as a yes or
no answer. The answer can be followed by


> Source page: 1528

Now Assist in Document Intelligence field types (continued)
Field type
Description
an explanation generated by Now Assist, if
enabled by the admin.
This field type is available for questions
defined in the use case setup.
Date
Date, displayed in the date format extracted
from the document.
This field type is available for fields and tables
defined in the use case setup.
Decimal
A number with up to two decimal places (for
example, 12.5 or 12.55).
This field type is available for fields and tables
defined in the use case setup.
Float (floating point number)
A number with up to seven decimal places (for
example, 12.0 to 12.0000000).
This field type is available for fields and tables
defined in the use case setup.


> Source page: 1529

Now Assist in Document Intelligence field types (continued)
Field type
Description
Integer
Whole number (for example, 12).
This field type is available for fields and tables
defined in the use case setup.
Reference
A reference field stores a reference to a field
on another table. For example, the Caller field
on the Incident table is a reference to the User
[sys_user] table.
For more information, see Reference field
type
.
This field type is available for fields and tables
defined in the use case setup.
Text
Text field.
This field type is available for fields, tables,
and questions defined in the use case setup.
Now Assist in Document Intelligence forms
Use forms to view and update Now Assist in Document Intelligence information.
Question form for use case setup
The Question form enables you to define a question you want to ask about the document.


> Source page: 1530

The Question form includes the following fields.
Single field form
Field
Description
Question
The question about the document. This
question is sent to the generative AI for a
prediction.
Write a clear and concise question about the
information you want to find in the document.
For example, "Is this document subject to
expiration?".
Below the question, add details about how
generative AI can best provide the correct
answer. For example, “Review the sections
where validity, duration or time frames are
discussed and look for any details about
expiration dates, renewal requirements, or
explicit statements declaring the document
as permanent. Answer ‘Yes’ if the document
is subject to an expiration date. Answer ‘No’ if
there is no mention of expiration or contains
an explicit statement that it is permanent.”
Tip: View the Question assistance tab
for additional guidance on forming an
effective question.
This question is displayed to the agent when
reviewing the answers in the Document
Intelligence workspace.
Field Type
The type of field (for example, a text or
Boolean field).
For more information, see Field types in Now
Assist in Document Intelligence.
Provide an explanation for the answer
Option to have the generative AI provide an
explanation based on the document text that
supports a yes or no answer.
This field is available when the Field Type field
is set to Boolean (True/False).
Target table
The table that stores the document processing
results for this use case.
Target field
Field on the target table you want to align this
field with.


> Source page: 1531

Single field form (continued)
Field
Description
The use case must have a target table
selected.
This single field is required for extraction
Option to make a question required. Required
questions can’t be left empty or unreviewed.
Create multiple single fields
Option to keep the form displayed on the
screen. Enable this if you are adding more
than one question to the use case.
Field form for use case setup
The Field form enables you to define a single field for extraction.
The Field form includes the following fields.
Single field form
Field
Description
Field name
The name for the field as it appears in the
Document Intelligence workspace.
Clearly state the information you want to
extract. Be specific, clear and concise. For
example: "Order number"
Details
A description of the information you want
to extract. Along with the field name, the
description is used to help the LLM predict the
text to extract from the document.
Include any relevant context or additional
details to identify the right information.
This might include keywords. For example,
"The contract number or the number of the
reference contract”.
Provide examples of what information
you want to extract. For example,
“AGR-2023-0042”, “CON2039739”, or
“BV-22122KEY”.
Example of a description:
Field name: “Currency”
Details: “The currency in which the contract
is denominated. Only valid for Order Forms.
Otherwise, leave it empty (''). If the currency


> Source page: 1532

Single field form (continued)
Field
Description
symbol is '$', answer 'USD'. Examples: 'USD',
'EUROS', 'GBP', etc.”
Tip: View the Field assistance tab
for additional guidance on forming an
effective field.
Field Type
The type of field. For example, a text or date
field. For more information, see Field types in
Now Assist in Document Intelligence.
Some field types convert the extracted value
into a standard format. For more information,
see Data normalization.
Target table
The table that stores the document processing
results for this use case.
Target field
Field on the target table you want to align this
field with.
The use case must have a target table
selected.
This single field is required for extraction
Option to make a field required.
Required fields can’t be left empty or
unreviewed.
Create multiple single fields
Option to keep the form displayed on the
screen. Enable this if you are adding more
than one single field to the use case.
Table form for use case setup
The Table form enables you to define a table for extraction.
The Table form includes the following fields.
Table form
Field
Description
Table
Table name
The name for the table as it appears in the
Document Intelligence workspace.


> Source page: 1533

Table form (continued)
Field
Description
Additional Details
A description of the table information you
want to extract. Along with the table name, the
description is used to help the LLM predict the
table fields to extract from the document.
Include any relevant context or additional
details to identify the right information.
Target table
The table that stores the document processing
results for these table fields.
Parent mapping to field
Field on the target table you want to align this
table with.
You must first select a target table.
This table is required for extraction
Option to make the table fields required.
Required table fields can’t be left empty or
unreviewed.
Columns
Column title
Name of the column header in the table.
Column type
The type of field in the table column. For
example, a text or date field. For more
information, see Field types in Now Assist in
Document Intelligence.
Some field types convert the extracted value
into a standard format. For more information,
see Data normalization.
Select target field
Field on the target table you want to align this
field with.
The use case must have a target table
selected.
New column
Option to add a column to the table.
Create multiple tables
Option to keep the form displayed on the
screen. Enable this option if you’re adding
more than one table to the use case.


> Source page: 1534

Limitations in Now Assist in Document Intelligence
There are several important limitations to be aware of when you’re using Now Assist in Document
Intelligence.
Now Assist in Document Intelligence skill limits
The following table lists the important limitations for the skills in Now Assist in Document
Intelligence.
Skill limits for Now Assist in Document Intelligence
Limit
Description
File formats
The supported file formats are JPEG, PNG,
PDF, and DOCX.
Note: Encrypted files are not
supported.
File size limit
The file size limit is 20 MB.
Page count limit
If image mode is turned on for the use case,
the page count limit is 10 pages per file.
If image mode is turned off, the page count
limit is:
• 200 pages per file if no tables are defined
for the use case.
• 20 pages per file if a table is defined for the
use case.
Image mode is selected during use case
setup. For more information, see Set up a use
case for Now Assist in Document Intelligence.
Maximum number of fields per use case
The maximum number of fields per use case is
50.
Supported languages
For image files that need optical character
recognition (OCR) to detect the text in them,
there are OCR models to support different
language groups. For more information,
see Languages supported by Now Assist in
Document Intelligence.
For text-based files, the skill recognizes any
language supported by the selected or default
model, as described in the model card for
the LLM. For more information on LLMs, see
Large language models used by Now Assist in
Document Intelligence.


> Source page: 1535

Limits for the document and visual insights AI agent
The following table lists the important limitations for the document and visual insights AI agent.
Document and visual insights AI agent limits
Limit
Description
File formats
The supported file formats are JPEG, PNG,
PDF, DOCX, XLSX, CSV, TXT, and PPTX.
File size limit
The file size limit is 20 MB.
Page count limit
For each document task, the page count limit
is 200 pages per file.
If the AI agent performs the extraction based
on a use case that includes a table, the limit
decreases to 20 pages per file.
Supported languages
For image and text-based files, the AI agent
recognizes any language supported by the
selected or default model, as described in the
model card for the LLM. For more information
on LLMs, see Large language models used by
Now Assist in Document Intelligence.
Large language models used by Now Assist in Document Intelligence
Now Assist in Document Intelligence uses large language models (LLMs) to perform generative
AI and agentic AI capabilities.
You can select the LLM when creating a use case. The LLM can also be selected for the AI agent
to use when processing documents and images.
Multimodal LLMs can support image mode, as they are capable of processing multiple types
of inputs like text, sound, images, and more, to generate a text response. Processing may take
longer for image inputs.
Note: The document and visual insights AI agent only uses multimodal LLMs. The text-
only Now LLM Service is not a supported model for the AI agent.
The following table lists the available LLMs for Now Assist in Document Intelligence.
LLM options for Now Assist in Document Intelligence
LLM
Highlights
Now Assist default
Use the LLM selected as the default for all
Now Assist skills. For more information, see
Manage AI models.


> Source page: 1536

LLM options for Now Assist in Document Intelligence (continued)
LLM
Highlights
Now LLM Service - Large
Text-only model used for AI-driven solutions
to support natural language understanding,
automation, and decision support.
Now LLM Service - Small
Text-only model used for enterprise AI
applications by enhancing text-based
automation and content generation within
ServiceNow workflows.
Google Cloud - Gemini Large
Multimodal model with advanced reasoning
and problem-solving capabilities.
Google Cloud - Gemini Small
Multimodal model with strong performance
in summarization, rewriting, and content
transformation.
Azure OpenAI - GPT Large
Multimodal model with a strong performance
on tasks involving analysis, summarization,
and multi-step problem solving.
Azure OpenAI - GPT Small
Multimodal model that is lightweight, high-
efficiency, and effective for routine workflows
with summarization, paraphrasing, and Q&A.
Amazon Bedrock - Claude Large
Multimodal model with strong context
management for long documents and dialogs.
Amazon Bedrock - Claude Small
Multimodal model with lower latency and
higher efficiency for real-time applications.
For more information, see Large language models on the ServiceNow AI Platform.
Languages supported by Now Assist in Document Intelligence
Now Assist in Document Intelligence supports text in multiple languages.
For text-based files, the Now Assist recognizes any language supported by the selected or
default model, as described in the model card for the LLM. For more information on LLMs, see
Large language models used by Now Assist in Document Intelligence.
For image files that need optical character recognition (OCR) to detect the text in them, OCR
models are used to support different language groups. The language selected during use case
setup helps the OCR model to detect text in the images. For more information, see Set up a use
case for Now Assist in Document Intelligence.
The following table lists the available OCR models.
OCR models for Now Assist in Document Intelligence
OCR model
Languages supported
Latin model (Default)
English, Dutch, French, German, Italian,
Portuguese, and Spanish
CJ model
Japanese and Chinese (simplified)

---

## IMAGE DESCRIPTIONS

### Repeated ServiceNow header logo and footer marks - source pages 1524-1536

The ServiceNow logo and recurring footer were reviewed on every assigned page. They are not duplicated as content because they are branding artifacts.

### Document Intelligence tool in the Tool Editor screenshot - source page 1527

Asset: `_assets/images/p1527_tool_editor_document_intelligence_tool.png`

The screenshot shows the Now Assist Skill Kit **Tool editor** interface with an **Add tool** modal. Tabs visible across the top include **Prompt editor**, **Tool editor**, **Prompt performance**, and **Skill settings**. In the modal, the **Tool type** dropdown is open and lists options including **Flow Action**, **Retriever**, **Script**, **Skill**, **Sub Flow**, **Web Search**, **Predictive Intelligence**, and **Document Intelligence**. The **Document Intelligence** option is highlighted/selected. The background canvas includes a left panel named **Tools**, a **Run tools** button on the right, and a flow node labeled **End**. The purpose is to show where administrators add the Document Intelligence tool to a custom Now Assist skill.

### Field type UI example images - source pages 1528-1529

Assets: `_assets/images/p1528_field_type_ui_examples.png`, `_assets/images/p1529_field_type_ui_examples.png`

The field type tables contain small embedded UI example screenshots. The examples illustrate the visible presentation of extracted values for field types such as Boolean, Date, Decimal, Float, Integer, Reference, and Text. The Boolean example shows a question-style response with a yes/no answer and supporting explanation area. The date example shows a date-like extracted value. The numeric examples show decimal/float/integer style values. The reference example indicates a field that stores a link/reference to another table record. The text example shows a short extracted text value. These screenshots support the adjacent table descriptions and demonstrate how field values may appear in the Document Intelligence workspace.

### Reference tables and visual table layouts - source pages 1525, 1527-1536

The Reference subsection includes multiple structured tables with shaded header rows and bordered cells. These tables list extraction modes, field types, form fields, skill limits, AI agent limits, LLM options, and OCR models. The tables are converted into Markdown in the TABLES section. Visual table styling such as gray headers and grid lines is not semantically significant, but it was reviewed to verify rows, columns, headers, and continuations across page breaks.

### Inline link/control icons - source pages 1524-1536

Small inline icons appear near linked documentation names and UI references. These icons indicate clickable documentation links or UI controls in the source. They were reviewed for page completeness and do not alter the text of the tables or procedures.

### Cropped image inventory for this subsection

* Source page 1524: `_assets/images/p1524_img8_413_142.png` - raster-image - Small inline UI icon or control glyph visible in the procedure text.
* Source page 1524: `_assets/images/p1524_img16_413_275.png` - raster-image - Small inline UI icon or control glyph visible in the procedure text.
* Source page 1524: `_assets/images/p1524_img21_342_342.png` - raster-image - Small inline UI icon or control glyph visible in the procedure text.
* Source page 1527: `_assets/images/p1527_img3_102_51.png` - raster-image - Embedded UI screenshot or large visual image from the source page.
* Source page 1528: `_assets/images/p1528_img6_301_157.png` - raster-image - Embedded UI screenshot or large visual image from the source page.
* Source page 1528: `_assets/images/p1528_img10_301_375.png` - raster-image - Embedded UI screenshot or large visual image from the source page.
* Source page 1528: `_assets/images/p1528_img14_301_538.png` - raster-image - Embedded UI screenshot or large visual image from the source page.
* Source page 1529: `_assets/images/p1529_img4_301_87.png` - raster-image - Embedded UI screenshot or large visual image from the source page.
* Source page 1529: `_assets/images/p1529_img8_301_241.png` - raster-image - Embedded UI screenshot or large visual image from the source page.
* Source page 1529: `_assets/images/p1529_img13_301_467.png` - raster-image - Embedded UI screenshot or large visual image from the source page.
* Source page 1529: `_assets/images/p1529_img17_301_606.png` - raster-image - Embedded UI screenshot or large visual image from the source page.
* Source page 1527: `_assets/images/p1527_tool_editor_document_intelligence_tool.png` - screenshot - Screenshot of the Tool Editor Add tool dialog with Document Intelligence as a tool type.
* Source page 1528: `_assets/images/p1528_field_type_ui_examples.png` - screenshot-group - Small UI examples embedded in the field type table for Boolean, Date, Decimal, and Float field types.
* Source page 1529: `_assets/images/p1529_field_type_ui_examples.png` - screenshot-group - Small UI examples embedded in the field type table for Integer, Reference, and Text field types.

---

## TABLES

### Table 1 - source page(s) 1525 - Data extraction modes in Now Assist in Document Intelligence


* Rows reviewed: 3
* Columns reviewed: 2


| Extraction mode | Description |
| --- | --- |
| Default | Now Assist auto-fills each field in the Document Intelligence workspace if it recognizes a value for it in the document. Now Assist may not always produce accurate, complete, or appropriate information. All fields should be reviewed for accuracy. A reviewer can accept the predicted value or manually enter a value. |
| Full automation | Now Assist automatically completes and submits the document task without an agent review. The values for all required fields are auto-filled by Now Assist or are identified as missing in the document. By turning on Full automation mode, the agent review used to check the accuracy of the predicted values is bypassed. There is a configuration option to suspend the automation and require an agent review when any of the required fields are missing in the document. |

### Table 2 - source page(s) 1527-1529 - Now Assist in Document Intelligence field types


* Rows reviewed: 8
* Columns reviewed: 2


| Field type | Description |
| --- | --- |
| Boolean (True/False) | Holds a true/false value. In document Q&A questions, the value is displayed as a yes or no answer. The answer can be followed by an explanation generated by Now Assist, if enabled by the admin. This field type is available for questions defined in the use case setup. |
| Date | Date, displayed in the date format extracted from the document. This field type is available for fields and tables defined in the use case setup. |
| Decimal | A number with up to two decimal places (for example, 12.5 or 12.55). This field type is available for fields and tables defined in the use case setup. |
| Float (floating point number) | A number with up to seven decimal places (for example, 12.0 to 12.0000000). This field type is available for fields and tables defined in the use case setup. |
| Integer | Whole number (for example, 12). This field type is available for fields and tables defined in the use case setup. |
| Reference | A reference field stores a reference to a field on another table. For example, the Caller field on the Incident table is a reference to the User [sys_user] table. For more information, see Reference field type. This field type is available for fields and tables defined in the use case setup. |
| Text | Text field. This field type is available for fields, tables, and questions defined in the use case setup. |

### Table 3 - source page(s) 1530-1531 - Question form for use case setup - Single field form


* Rows reviewed: 8
* Columns reviewed: 2


| Field | Description |
| --- | --- |
| Question | The question about the document. This question is sent to the generative AI for a prediction. Write a clear and concise question about the information you want to find in the document. For example, "Is this document subject to expiration?". Below the question, add details about how generative AI can best provide the correct answer. For example, “Review the sections where validity, duration or time frames are discussed and look for any details about expiration dates, renewal requirements, or explicit statements declaring the document as permanent. Answer ‘Yes’ if the document is subject to an expiration date. Answer ‘No’ if there is no mention of expiration or contains an explicit statement that it is permanent.” Tip: View the Question assistance tab for additional guidance on forming an effective question. This question is displayed to the agent when reviewing the answers in the Document Intelligence workspace. |
| Field Type | The type of field (for example, a text or Boolean field). For more information, see Field types in Now Assist in Document Intelligence. |
| Provide an explanation for the answer | Option to have the generative AI provide an explanation based on the document text that supports a yes or no answer. This field is available when the Field Type field is set to Boolean (True/False). |
| Target table | The table that stores the document processing results for this use case. |
| Target field | Field on the target table you want to align this field with. The use case must have a target table selected. |
| This single field is required for extraction | Option to make a question required. Required questions can’t be left empty or unreviewed. |
| Create multiple single fields | Option to keep the form displayed on the screen. Enable this if you are adding more than one question to the use case. |

### Table 4 - source page(s) 1531-1532 - Field form for use case setup - Single field form


* Rows reviewed: 8
* Columns reviewed: 2


| Field | Description |
| --- | --- |
| Field name | The name for the field as it appears in the Document Intelligence workspace. Clearly state the information you want to extract. Be specific, clear and concise. For example: "Order number". |
| Details | A description of the information you want to extract. Along with the field name, the description is used to help the LLM predict the text to extract from the document. Include any relevant context or additional details to identify the right information. This might include keywords. For example, “The contract number or the number of the reference contract”. Provide examples of what information you want to extract. For example, “AGR-2023-0042”, “CON2039739”, or “BV-22122KEY”. Example of a description: Field name: “Currency” Details: “The currency in which the contract is denominated. Only valid for Order Forms. Otherwise, leave it empty (''). If the currency symbol is '$', answer 'USD'. Examples: 'USD', 'EUROS', 'GBP', etc.” Tip: View the Field assistance tab for additional guidance on forming an effective field. |
| Field Type | The type of field. For example, a text or date field. For more information, see Field types in Now Assist in Document Intelligence. Some field types convert the extracted value into a standard format. For more information, see Data normalization. |
| Target table | The table that stores the document processing results for this use case. |
| Target field | Field on the target table you want to align this field with. The use case must have a target table selected. |
| This single field is required for extraction | Option to make a field required. Required fields can’t be left empty or unreviewed. |
| Create multiple single fields | Option to keep the form displayed on the screen. Enable this if you are adding more than one single field to the use case. |

### Table 5 - source page(s) 1532-1533 - Table form for use case setup


* Rows reviewed: 13
* Columns reviewed: 2


| Field | Description |
| --- | --- |
| Table |  |
| Table name | The name for the table as it appears in the Document Intelligence workspace. |
| Additional Details | A description of the table information you want to extract. Along with the table name, the description is used to help the LLM predict the table fields to extract from the document. Include any relevant context or additional details to identify the right information. |
| Target table | The table that stores the document processing results for these table fields. |
| Parent mapping to field | Field on the target table you want to align this table with. You must first select a target table. |
| This table is required for extraction | Option to make the table fields required. Required table fields can’t be left empty or unreviewed. |
| Columns |  |
| Column title | Name of the column header in the table. |
| Column type | The type of field in the table column. For example, a text or date field. For more information, see Field types in Now Assist in Document Intelligence. Some field types convert the extracted value into a standard format. For more information, see Data normalization. |
| Select target field | Field on the target table you want to align this field with. The use case must have a target table selected. |
| New column | Option to add a column to the table. |
| Create multiple tables | Option to keep the form displayed on the screen. Enable this option if you’re adding more than one table to the use case. |

### Table 6 - source page(s) 1534 - Skill limits for Now Assist in Document Intelligence


* Rows reviewed: 6
* Columns reviewed: 2


| Limit | Description |
| --- | --- |
| File formats | The supported file formats are JPEG, PNG, PDF, and DOCX. Note: Encrypted files are not supported. |
| File size limit | The file size limit is 20 MB. |
| Page count limit | If image mode is turned on for the use case, the page count limit is 10 pages per file. If image mode is turned off, the page count limit is: • 200 pages per file if no tables are defined for the use case. • 20 pages per file if a table is defined for the use case. Image mode is selected during use case setup. For more information, see Set up a use case for Now Assist in Document Intelligence. |
| Maximum number of fields per use case | The maximum number of fields per use case is 50. |
| Supported languages | For image files that need optical character recognition (OCR) to detect the text in them, there are OCR models to support different language groups. For more information, see Languages supported by Now Assist in Document Intelligence. For text-based files, the skill recognizes any language supported by the selected or default model, as described in the model card for the LLM. For more information on LLMs, see Large language models used by Now Assist in Document Intelligence. |

### Table 7 - source page(s) 1535 - Document and visual insights AI agent limits


* Rows reviewed: 5
* Columns reviewed: 2


| Limit | Description |
| --- | --- |
| File formats | The supported file formats are JPEG, PNG, PDF, DOCX, XLSX, CSV, TXT, and PPTX. |
| File size limit | The file size limit is 20 MB. |
| Page count limit | For each document task, the page count limit is 200 pages per file. If the AI agent performs the extraction based on a use case that includes a table, the limit decreases to 20 pages per file. |
| Supported languages | For image and text-based files, the AI agent recognizes any language supported by the selected or default model, as described in the model card for the LLM. For more information on LLMs, see Large language models used by Now Assist in Document Intelligence. |

### Table 8 - source page(s) 1535-1536 - LLM options for Now Assist in Document Intelligence


* Rows reviewed: 10
* Columns reviewed: 2


| LLM | Highlights |
| --- | --- |
| Now Assist default | Use the LLM selected as the default for all Now Assist skills. For more information, see Manage AI models. |
| Now LLM Service - Large | Text-only model used for AI-driven solutions to support natural language understanding, automation, and decision support. |
| Now LLM Service - Small | Text-only model used for enterprise AI applications by enhancing text-based automation and content generation within ServiceNow workflows. |
| Google Cloud - Gemini Large | Multimodal model with advanced reasoning and problem-solving capabilities. |
| Google Cloud - Gemini Small | Multimodal model with strong performance in summarization, rewriting, and content transformation. |
| Azure OpenAI - GPT Large | Multimodal model with a strong performance on tasks involving analysis, summarization, and multi-step problem solving. |
| Azure OpenAI - GPT Small | Multimodal model that is lightweight, high-efficiency, and effective for routine workflows with summarization, paraphrasing, and Q&A. |
| Amazon Bedrock - Claude Large | Multimodal model with strong context management for long documents and dialogs. |
| Amazon Bedrock - Claude Small | Multimodal model with lower latency and higher efficiency for real-time applications. |

### Table 9 - source page(s) 1536 - OCR models for Now Assist in Document Intelligence


* Rows reviewed: 3
* Columns reviewed: 2


| OCR model | Languages supported |
| --- | --- |
| Latin model (Default) | English, Dutch, French, German, Italian, Portuguese, and Spanish |
| CJ model | Japanese and Chinese (simplified) |

---

## FIGURES

### Figure 1 - Document Intelligence tool in the Tool Editor - source page 1527

* Figure title: `Document Intelligence tool in the Tool Editor`.
* Source asset: `_assets/images/p1527_tool_editor_document_intelligence_tool.png`.
* Components: Tool editor tab, Add tool modal, Tool type dropdown, selectable tool types, Document Intelligence option, left Tools panel, Run tools button, and background flow canvas.
* Relationship: the Document Intelligence tool is selected as a tool type that can be added to a custom Now Assist Skill Kit skill.
* Business purpose: show where a skill builder selects Document Intelligence as a tool.
* Technical purpose: connect custom skill configuration with document/image extraction, Q&A, and summarization capabilities.
* Security boundaries: no explicit security-zone boundary is shown; security is handled by role masking, security controls, and data access settings in the surrounding text.

### Figure 2 - Field type UI example images - source pages 1528-1529

* Source assets: `_assets/images/p1528_field_type_ui_examples.png`, `_assets/images/p1529_field_type_ui_examples.png`.
* Components: small UI examples embedded inside the field-type table cells.
* Relationship: each small UI example corresponds to an adjacent field-type row in the table and illustrates how extracted values may be displayed.
* Technical purpose: demonstrate output presentation for Boolean, Date, Decimal, Float, Integer, Reference, and Text field types.
* Security boundaries: none shown.

---

## QUALITY ASSURANCE NOTES

* PAGES REVIEWED: 1524, 1525, 1526, 1527, 1528, 1529, 1530, 1531, 1532, 1533, 1534, 1535, 1536.
* IMAGES REVIEWED: 14 cropped non-logo image/control glyph(s), repeated ServiceNow logos, footer marks, visual callouts, and subsection-specific screenshots/figures. Image inventory: `_assets/image_inventory.csv`.
* TABLES REVIEWED: 9 assigned table(s) converted to Markdown. Table inventory: `_assets/table_inventory.csv`.
* FIGURES REVIEWED: Figure descriptions include source page, asset link, components, connections/flows where applicable, business purpose, technical purpose, and security-boundary notes.
* OCR ISSUES FOUND: PDF text extraction contained recurring footer/header noise, line-wrap artifacts, occasional missing spaces from the PDF text layer, inline icon artifacts, and rendered figure areas on pages 1506 and 1511 that appear blank/invisible despite accessible text-layer workflow descriptions.
* OCR ISSUES CORRECTED: Recurring footer/header noise was removed from CONTENT, hidden/control characters and soft-hyphen artifacts were normalized, obvious missing-space artifacts were corrected when verified by context, shared page boundaries were split at exact source headings, tables were reconstructed into Markdown, and image/figure crops were saved to `_assets/images`.
* SECTION MAPPING NOTES: Page 1524 is a shared boundary page with Use; only content from `Now Assist in Document Intelligence reference` onward is included. Page 1537 starts the next TOC section `Document Intelligence` and is excluded from Reference content but accounted for as next-section boundary material.
* FILE NAME VERIFIED AGAINST TOC: Yes.
* FOLDER NAME VERIFIED AGAINST TOC: Yes.
* RECHECK PASSES COMPLETED: 12/12: page completeness, text extraction, table extraction, image extraction/documentation, diagram interpretation, section mapping, subsection mapping, file names, folder names, Markdown formatting, missed-content review, and OCR/text-layer cleanup review.
