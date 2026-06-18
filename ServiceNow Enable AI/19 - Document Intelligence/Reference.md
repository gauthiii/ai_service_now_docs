# Reference
## SOURCE INFORMATION
* SECTION NAME: Document Intelligence
* SUBSECTION NAME: Reference
* SOURCE FILE NAME: Document Intelligence.pdf
* PAGE RANGE: 1600-1629 (page 1629 split before next major section `Task Intelligence`)
* EXTRACTION DATE: 2026-06-17

---
# CONTENT
> Source page: 1600

Document Intelligence references
The following topics provide additional information about the features and properties installed
with Document Intelligence.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Components installed with Document Intelligence
Several types of components are installed with activation of the Document Intelligence plugin,
including tables and user roles.
> Source page: 1601

Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Roles installed with Document Intelligence
For more information on roles, see Document Intelligence roles.
Role title [name]
Description
Contains roles
DocIntel Admin
[sn_docintel.admin]
Has full access to the
Document Intelligence
application, except for
modifying a subset of system
properties, and the billing
and internal tables.
• platform_ml_di.admin
• action_designer
• flow_designer
• sn_ace.ace_user
• canvas_user
• usage_admin
DocIntel Viewer
[sn_docintel.viewer]
Has view-only access on
Document Intelligence
document tasks that they are
authorized to view.
• snc_read_only
• platform_ml_di.viewer
DocIntel Extraction Agent
[sn_docintel.extraction_agent]
Extracts data and text
from documents using the
Document Intelligence
workspace.
platform_ml_di.extraction_agent
DocIntel Creation Agent
[sn_docintel.creation_agent]
Extracts information from
documents using the
Document Intelligence
workspace. Also enables
users to create Document
Intelligence document
tasks and submit them for
processing.
platform_ml_di.creation_agent
DocIntel Manager
[sn_docintel.manager]
Creates and edits use cases,
fields, field groups, and
document tasks. Views,
measures, and analyzes the
usage and effectiveness
of Document Intelligence
using the Platform Document
Intelligence Usage
dashboard. Grants access to
submit document tasks and
interact with the Document
Intelligence workspace.
• platform_ml_di.manager
• action_designer
• flow_designer
• sn_ace.ace_user
• canvas_user
• usage_admin
> Source page: 1602

Tables installed with Document Intelligence
Note:  Starting in Document Intelligence 3.0, DocIntel uses ServiceNow AI Platform
database tables (sys_di_) in place of the scoped application tables (di_). See Upgrade to
Document Intelligence 3.0 or later from version 2.4 or earlier.
Table
Description
Billable Event
[sys_di_billable_event]
Contains all the billable events for the instance. A billable
event corresponds to pages that have been processed using
Document Intelligence.
Recommendation Meta Info
[sys_di_candidate_meta_info]
[Internal table] Contains the data returned by the AI for field
group extraction and for missing value prediction.
Recommendation Score
[sys_di_candidate_score]
[Internal table] Contains the scores for each recommendation
calculated by the AI. There’s one record per field, for each
page of a document.
Field Value
[sys_di_extracted_value]
Contains all the data extracted in the instance, across all
document tasks.
Image
[sys_di_image]
[Internal table] Contains information about each page of a
document. There’s one record per document page.
Integration Setup
[sys_di_integration_setup]
Contains DocIntel use case integrations.
Field
[sys_di_key]
Contains all the fields created in the instance, across all
use cases. A field corresponds to a recommendation to be
extracted from documents.
Field Group
[sys_di_key_group]
Contains all the field groups created in the instance, across all
use cases. A field group is usually created to help extract data
from tables and lists.
Lock
[sys_di_lock]
Contains an index of locked task solution definitions. Used to
improve the performance of scheduled jobs.
DocIntel Aggregated Metrics
[sys_di_metrics_aggregated]
[Internal table] Contains aggregated metrics. Aggregation may
happen multiple times per day, based on system properties.
> Source page: 1603

Table
Description
DocIntel Daily Metrics
[sys_di_metrics_daily]
[Internal table] Contains the metrics aggregated daily. There’s
one record per aggregated metric.
DocIntel Metrics Job Log
[sys_di_metrics_job_log]
[Internal table] Contains a log of the metrics daily aggregation
jobs that happened in the instance.
DocIntel Raw Metrics
[sys_di_metrics_raw]
[Internal table] Contains a list of raw metrics collected by
Document Intelligence. The records are deleted when metrics
aggregation happens.
DocIntel OCR Input
[sys_di_ocr_input]
[Internal table] Contains image data to be sent to the OCR
module for processing. The records are deleted when
processing is complete.
PDF
[sys_di_pdf]
[Internal table] Contains a list of PDF files stored across tasks.
DocIntel PDF Input
[sys_di_pdf_input]
[Internal table] Contains PDF data to be sent to the PDF
module for processing. The records are deleted when
processing is complete.
DocIntel Prediction Input
[sys_di_prediction_input]
[Internal table] Contains the data needed to make suggestions
across all fields for a given document task. There’s one record
per document page.
Document Task
[sys_di_task]
Contains all the document tasks created in the instance,
across all use cases. A document task contains one or more
documents from which fields must be extracted.
Task Solution Definition
[sys_di_task_def_solution_def]
Contains the solution definitions related to DocIntel use cases.
DocIntel Use Case
[sys_di_task_definition]
Contains all the document processing use cases created in
the instance. A use case defines what and how data should be
extracted from a set of documents.
DocIntel Training Input
[sys_di_training_input]
[Internal table] Contains the data needed to improve the AI
models.
> Source page: 1604

Confidence scores
A confidence score is a measurement (percentage) of how reliable DocIntel is in providing a
recommendation for a field. The higher the score, the more reliable the recommendation.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Confidence scores increase as the AI model is trained through user input when processing
document tasks.
A score is displayed next to each recommendation.
Confidence score
In some areas, the score is color-coded with a different color for each confidence score range.
• Green indicates high confidence (76%-100%)
• Yellow indicates medium confidence (50%-75%)
• Red indicates low confidence (0%-49%)
To configure confidence score thresholds, see Configure data extraction modes.
Data extraction modes
Extraction modes determine how the data is extracted in the document task and how the
task is processed. The mode changes the behavior of the fields in the Document Intelligence
workspace.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
DocIntel uses the following extraction modes.
> Source page: 1605

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
Data normalization
Certain types of data extracted from documents are converted into a standard format so that
they appear the same across all fields.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
This process increases the usefulness of the data by enabling it to be grouped and analyzed
more easily. It also supports integration with other applications on the ServiceNow AI Platform.
> Source page: 1606

Field types
The following field types are converted to support data normalization:
Field type
Description
Date
Standard date format. For example, YYYY-MM-
DD.
Reference field
A field that uses a field in another table as a
standard. DocIntel matches the extracted data
to the standard.
For example, a use case has a reference
field called Vendor that points to the Name
column in the Company table as the reference.
When processing a document task, DocIntel
extracts “Degas Dairy Products, Inc” from the
document and fills the Vendor field with that
value. DocIntel compares the value to the
company names in the reference table and
finds “Degas Dairy Products, Inc” as a match.
In the document task, “Degas Dairy Products,
Inc” is matched to “Degas Dairy Products, Inc”
in the reference.
Integer
Whole number. For example, 12.
Decimal
Number with up to two decimal places. For
example, 12.5 or 12.55.
Floating point number
Number with up to seven decimal places. For
example, 12.0 to 12.0000000.
To set the field type, see Create a field for data extraction.
Display
A completed data extraction field shows the converted value next to it.
> Source page: 1607

You can adjust the converted date value by selecting Edit.
Note:  In some cases, the data extracted from the document may not be in a valid format to
be converted. For example, if DocIntel read the letter O instead of a number 0 in a date field
(11.12.2o23), then it would not be converted. In this case, edit the field to the correct format.
Ambiguous data
If there is data in a document that can be understood in more than one way, DocIntel interprets
that value based on the default selected for it in the use case configuration. DocIntel must
interpret an ambiguous value in order to accurately convert it to the normalized format.
For example, a use case has a Date field, and Month first  is selected as the default order to
interpret ambiguous dates. When a document containing the date 1/2/2024 is processed for the
use case, DocIntel interprets that date as January 2, not February 1, when it extracts that value
and converts it.
In such cases, the user completing a document task may need to confirm or correct the
conversion of ambiguous values. Depending on the field’s configuration in the use case,
automated document processing may be interrupted to ensure the conversion is accurate.
Document field statuses
The following is a list of the statuses for fields in DocIntel document tasks. These statuses apply
to fields for both document classification and data extraction.
> Source page: 1608

Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Statuses for document fields
Status
Icon
Description
To complete
The field must be filled in with
a value or marked as missing
in the document.
Completed
The field is filled in with a
value or marked as missing in
the document.
To review
The field is auto-filled and
needs review by a user.
Reviewed
The auto-filled field has been
reviewed by a user.
In progress
The field is in the process of
being filled in or reviewed.
Needs attention
The auto-filled field has
triggered a warning. The
causes for a warning include:
• A required field must
be filled in or marked as
missing in the document.
• An extracted value has a
low confidence score and
should be reviewed.
• An extracted value is
ambiguous and should be
verified.
Document Intelligence forms
Use forms to view and update Document Intelligence information.
> Source page: 1609

Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Check box list form
The Check box list form enables you to define a check box list for extraction.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
The Check box list form includes the following fields.
Check box list form
Field
Description
Check box list
Check box list name
The name for the check box list as it appears
in the Document Intelligence workspace.
Target table
The table that stores the document processing
results for the check box list.
Parent mapping to field
Field on the target table you want to align this
check box list with.
Note:  You must first select a target
table.
Check boxes
Check box title
The name for the check box as it appears in
the Document Intelligence workspace.
Select target field
Field on the target table that you want to align
this field with.
This field is used for integration with other
applications. See Integrate with a custom
application or workflow.
This field is required for extraction
Option to make a field required.
Required fields can’t be left unreviewed.
> Source page: 1610

Check box list form (continued)
Field
Description
Required fields affect how document tasks are
processed in the Fully automated extraction
mode. For more information, see Configure
data extraction modes.
New check box
Option to add a check box to the list.
Use the reorder icon (
) to reorder a check
box in the list.
Create multiple check box lists
Option to keep the pop-up window displayed
on the screen. Enable this option if you're
adding more than one check box list to the use
case.
Single field form
The Single field form enables you to define a single field for extraction.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
The Single field form includes the following fields.
Single field form
Field
Description
Single field name
The name for the field as it appears in the
Document Intelligence workspace.
Type
The type of the field. For example, a text or
date field.
Some field types convert the extracted value
into a standard format. For more information,
see Data normalization.
Converted date format
The date format that the extracted value is
converted to for data normalization.
This field is available when the Type field is set
to Date.
> Source page: 1611

Single field form (continued)
Field
Description
Target table
The table that stores the document processing
results for this use case.
Target field
Field on the target table that you want to align
this field with.
Note:  The use case must have a target
table selected.
This field is used for integration with other
applications. For more information, see
Integrate with a custom application or
workflow.
When the date is ambiguous in a document,
DocIntel will interpret it in the following order
The default interpretation of the date format.
For example, if you select Month first  in
this field, DocIntel will interpret an ambiguous
date like 1/2/2024 as January 2 when it
extracts that value from a document. If you
select Day first, it will interpret it as
February 1.
This field is available when the Type field is set
to Date.
When the number is ambiguous in a
document, DocIntel will interpret it as
The default interpretation of the number
format.
For example, if you select 1,00  in this field,
DocIntel will interpret an ambiguous number
like 5 as 5,00 instead of 5.00 when it extracts
that value from a document.
This field is available when the Type field is set
to Integer, Decimal, or Float.
Reference table
The table that stores the reference column.
It’s automatically populated based on the
selected target field.
This field displays when the Type field is set to
Reference field.
Reference column
The column in the reference table that
contains the referenced data.
DocIntel uses the reference column to find
data that matches the extracted field value
> Source page: 1612

Single field form (continued)
Field
Description
when processing a document task. The field
value is then converted to the format of the
reference. For more information on converted
values, see Data normalization.
This field is available when the Type field is set
to Reference field.
Distinguisher(s)
Additional columns in the reference table that
help the user to distinguish between similar
records.
This field is available when the Type field is set
to Reference field.
This single field is required for extraction
Option to make the field required.
Required fields can’t be left empty or
unreviewed. They also can’t contain
ambiguous values. An ambiguous value is a
field entry that can be interpreted in more than
one way.
If it's a reference field type, the required field
must have a valid, exact match. By default,
DocIntel uses the first matched record.
Required fields affect how document tasks are
processed in the Fully automated extraction
mode. For more information, see Configure
data extraction modes.
Select one of these options for cases when:
• the date/number is ambiguous in the
document
• there are multiple reference matches in the
document
Option for agent review in situations when
DocIntel encounters an ambiguous value in a
required field.
In such cases, the selected default
interpretation will apply to the extracted value.
The option is whether to interrupt full
automation of document tasks to allow agents
to verify the interpreted values. Otherwise,
continue automatic processing of document
tasks without the agent review.
Create multiple single fields
Option to keep the pop-up window displayed
on the screen. Enable this field if you’re adding
more than one single field to the use case.
Single field group form
The Single field group form enables you to define a related group of single fields for extraction.
> Source page: 1613

Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
The Single field group form includes the following fields.
Single field group form
Field
Description
Field group
Field group name
The name for the field group as it appears in
the Document Intelligence workspace.
Target table
The table that stores the document processing
results for the fields.
Parent mapping to field
Field on the target table that you want to align
this field group with.
Note:  You must first select a target
table.
This field group is required for extraction
Option to make the field as required.
Required fields can’t be left empty or
unreviewed. They also can’t contain
ambiguous values. An ambiguous value is a
field entry that can be interpreted in more than
one way.
If it’s a reference field type, the required field
must have a valid, exact match. By default,
DocIntel uses the first matched record.
Required fields affect how document tasks are
processed in the Fully automated extraction
mode. For more information, see Configure
data extraction modes.
Fields
Field name
The name for the field as it appears in the
Document Intelligence workspace.
Type
The type of the field. For example, a text or
date field.
> Source page: 1614

Single field group form (continued)
Field
Description
Some field types convert the extracted value
into a standard format. For more information,
see Data normalization.
Select Target Field
Field on the target table that you want to align
this field with.
This field is used for integration with other
applications. For more information, see
Integrate with a custom application or
workflow.
When the date is ambiguous in a document,
DocIntel will interpret it in the following order
The default interpretation of the date format.
For example, if you select Month first  in
this field, DocIntel will interpret an ambiguous
date like 1/2/2024 as January 2 when it
extracts that value from a document. If you
select Day first, it will interpret it as
February 1.
This field is available when the Type field is set
to Date.
When the number is ambiguous in a
document, DocIntel will interpret it as
The default interpretation of the number
format.
For example, if you select 1,00 in this field,
DocIntel will interpret an ambiguous number
like 5 as 5,00 instead of 5.00 when it extracts
that value from a document.
This field is available when the Type field is set
to Integer, Decimal, or Float.
Reference table
The table that stores the reference column.
It’s automatically populated based on the
selected target field.
This field displays when the Type field is set to
Reference field.
Reference column
The column in the reference table that
contains the referenced data.
DocIntel uses the reference column to find
data that matches the extracted field value
when processing a document task. The field
value is then converted to the format of the
> Source page: 1615

Single field group form (continued)
Field
Description
reference. For more information on converted
values, see Data normalization.
This field is available when the Type field is set
to Reference field.
Distinguisher(s)
Additional columns in the reference table that
help the user to distinguish between similar
records.
This field is available when the Type field is set
to Reference field.
This field is required for extraction
Option to make a field required.
Required fields can’t be left empty or
unreviewed. They also can’t contain
ambiguous values. An ambiguous value is a
field entry that can be interpreted in more than
one way.
If it’s a reference field type, the required field
must have a valid, exact match. By default,
DocIntel uses the first matched record.
Required fields affect how document tasks are
processed in the Fully automated extraction
mode. For more information, see Configure
data extraction modes.
Select one of these options for cases when:
• the date/number is ambiguous in the
document
• there are multiple reference matches in the
document
Option for agent review in situations when
DocIntel encounters an ambiguous value in a
required field.
In such cases, the selected default
interpretation will apply to the extracted value.
The option is whether to interrupt full
automation of document tasks to allow agents
to verify the interpreted values. Otherwise,
continue automatic processing of document
tasks without the agent review.
New single field
Option to add a field to the group.
Use the reorder icon (
) to reorder a field in
the group.
Create multiple field groups
Option to keep the pop-up window displayed
on the screen. Enable this option if you're
> Source page: 1616

Single field group form (continued)
Field
Description
adding more than one single field group to the
use case.
Table form
The Table form enables you to define a table for extraction.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
The Table form includes the following fields.
Table form
Field
Description
Table
Table name
The name for the table as it appears in the
Document Intelligence workspace.
Target table
The table that stores the document processing
results for these table fields.
Parent mapping to field
Field on the target table that you want to align
this table with.
Note:  You must first select a target
table.
This table is required for extraction
Option to make the table fields required.
Required table fields can't be left empty
or unreviewed. They also can’t contain
ambiguous values. An ambiguous value is a
field entry that can be interpreted in more than
one way.
Required fields affect how document tasks are
processed in the Fully automated extraction
mode. For more information, see Configure
data extraction modes.
Columns
> Source page: 1617

Table form (continued)
Field
Description
Column title
Name of the column header in the table.
Type
The type of the field in the table column. For
example, a text or date field.
Some field types convert the extracted value
into a standard format. For more information,
see Data normalization.
Select target field
Field on the target table that you want to align
this field with.
This field is used for integration with other
applications. For more information, see
Integrate with a custom application or
workflow.
When the date is ambiguous in a document,
DocIntel will interpret it in the following order
The default interpretation of the date format.
For example, if you select Month first  in
this field, DocIntel will interpret an ambiguous
date like 1/2/2024 as January 2 when it
extracts that value from a document. If you
select Day first, it will interpret it as
February 1.
This field is available when the Type field is set
to Date.
When the number is ambiguous in a
document, DocIntel will interpret it as
The default interpretation of the number
format.
For example, if you select 1,00  in this field,
DocIntel will interpret an ambiguous number
like 5 as 5,00 instead of 5.00 when it extracts
that value from a document.
This field is available when the Type field is set
to Integer, Decimal, or Float.
Reference table
The table that stores the reference column.
It’s automatically populated based on the
selected target field.
This field displays when the Type field is set to
Reference field.
Reference column
The column in the reference table that
contains the referenced data.
> Source page: 1618

Table form (continued)
Field
Description
DocIntel uses the reference column to find
data that matches the extracted field value
when processing a document task. The field
value is then converted to the format of the
reference. For more information on converted
values, see Data normalization.
This field is available when the Type field is set
to Reference field.
Distinguisher(s)
Additional columns in the reference table that
help the user to distinguish between similar
records.
This field is available when the Type field is set
to Reference field.
This field is required for extraction
Indicates whether a column required. It’s
automatically selected or cleared based on
whether the table is required.
Required column fields can't be left empty
or unreviewed. They also can’t contain
ambiguous values. An ambiguous value is a
field entry that can be interpreted in more than
one way.
If it’s a reference field type, the required field
must have a valid, exact match. By default,
DocIntel uses the first matched record.
Required fields affect how document tasks are
processed in the Fully automated extraction
mode. For more information, see Configure
data extraction modes.
Select one of these options for cases when:
• the date/number is ambiguous in the
document
• there are multiple reference matches in the
document
Option for agent review in situations when
DocIntel encounters an ambiguous value in a
required field.
In such cases, the selected default
interpretation will apply to the extracted value.
The option is whether to interrupt full
automation of document tasks to allow agents
to verify the interpreted values. Otherwise,
continue automatic processing of document
tasks without the agent review.
New column
Option to add a column to the table.
> Source page: 1619

Table form (continued)
Field
Description
Use the reorder icon (
) to reorder a column
in the table.
Create multiple tables
Option to keep the pop-up window displayed
on the screen. Enable this option If you're
adding more than one table to the use case.
Document Intelligence properties
Document Intelligence (DocIntel) system properties control the behavior of the Document
Intelligence application.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
The DocIntel Manager (sn_docintel.manager) can modify the system properties for DocIntel.
Note:
Document Intelligence 3.0 includes new and updated system properties. For more detail
about the upgrade, see Upgrade to Document Intelligence 3.0 or later from version 2.4 or
earlier.
Document Intelligence 2.4- system properties
Property name
Description
Values
sn_docintel.default_field_sidebar_width
The default sidebar
width for the document
fields panel in the
Document Intelligence
workspace.
Allowed:
Format of
[integer]px
Default: 416px
sn_docintel.default_image_fit
The default image fit
for the document panel
viewer in the Document
Intelligence workspace.
Allowed:
fit_to_page,
fit_to_width
Default:
fit_to_page
sn_docintel.default_thumbnail_sidebar_width
The default thumbnail
sidebar width for the
navigation panel in the
Document Intelligence
workspace.
Allowed:
Format of
[integer]px
> Source page: 1620

Property name
Description
Values
Default: 167px
sn_docintel.field_sidebar_layout_position
The layout position
for the document
fields panel in the
Document Intelligence
workspace, in relation
to the document fields
panel sidebar.
Allowed: right,
left
Default: right
sn_docintel.show_exact_match_option
Show the exact match
option for each field
in the document fields
panel in the Document
Intelligence workspace.
Allowed: true,
false
Default: true
sn_docintel.show_candidate_score
Show confidence
scores on the
recommendations
selection menu in
the document fields
panel in the Document
Intelligence workspace.
Allowed: true,
false
Default: true
sn_docintel.warning_score_threshold
Threshold used to
show the warning
icon for low-score
recommendations in
the document fields
panel in the Document
Intelligence workspace.
Allowed:
Number
between 0.0
and 1.0
Default: 0.7
sn_docintel.autofill_threshold
Minimum score
threshold required
to auto-fill
recommendations.
Allowed:
Number
between 0.0
and 1.0
Default: 0.0
sn_docintel.straight_through_processing_threshold Minimum score
threshold required
for straight-through
processing of a
document task.
Allowed:
Number
between 0.0
and 1.0
Default: 1.0
Document Intelligence 3.0+ system properties
Property name
Description
Values
glide.platform_ml_di.doc_classifier.
days_between_trainings
Document classifier property
Default: 30
> Source page: 1621

Property name
Description
Values
Minimum number of days between
trainings for a given document classifier
use case.
glide.platform_ml_di.doc_data_extractor.
warning_score_threshold
Document extraction property
Threshold used to show the warning
icon for low-score recommendations
in the document fields panel in the
Document Intelligence workspace.
Allowed:
Number
between
0.0 and 1.0
Default: 0.7
glide.platform_ml_di.doc_data_extractor.
straight_through_processing_threshold
Document extraction property
Minimum score threshold required
for straight-through processing of a
document task.
Allowed:
Number
between
0.0 and 1.0
Default: 1.0
glide.platform_ml_di.doc_data_extractor.
show_exact_match_option
Document extraction property
Show the exact match option for each
field in the document fields panel in the
Document Intelligence workspace.
Allowed:
true, false
Default:
true
glide.platform_ml_di.doc_data_extractor.
show_candidate_score
Document extraction property
Show confidence scores on the
recommendations selection menu
in the document fields panel in the
Document Intelligence workspace.
Allowed:
true, false
Default:
true
glide.platform_ml_di.doc_data_extractor.
field_sidebar_layout_position
Document extraction property
The layout position for the document
fields panel in the Document
Intelligence workspace, in relation to
the document fields panel sidebar.
Allowed:
right, left
Default:
right
glide.platform_ml_di.doc_data_extractor.
default_thumbnail_sidebar_width
Document extraction property
The default thumbnail sidebar width for
the navigation panel in the Document
Intelligence workspace.
Allowed:
Format of
[integer]px
Default:
167px
glide.platform_ml_di.doc_data_extractor.
default_image_fit
Document extraction property
The default image fit for the document
panel viewer in the Document
Intelligence workspace.
Allowed:
fit_to_page,
fit_to_width
Default:
fit_to_page
> Source page: 1622

Property name
Description
Values
glide.platform_ml_di.doc_data_extractor.
default_field_sidebar_width
Document extraction property
The default sidebar width for the
document fields panel in the Document
Intelligence workspace.
Allowed:
Format of
[integer]px
Default:
416px
glide.platform_ml_di.doc_data_extractor.
autofill_threshold
Document extraction property
Minimum score threshold required to
auto-fill recommendations.
Allowed:
Number
between
0.0 and 1.0
Default:
0.01
glide.platform_ml_di.doc_data_extractor.
draw_tool_enable
This property is used to enable or
disable draw tool features for table
extraction.
Allowed:
true, false
Default:
true
Document Intelligence roles
Document Intelligence is installed with these roles.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
To learn more about managing per-user subscriptions, see Managing per-user subscriptions in
Subscription Management
 and contact your account representative.
DocIntel Admin [sn_docintel.admin]
Has full access to the Document Intelligence application, except for modifying a subset of system
properties, and the billing and internal tables.
Contains Roles
List of roles contained within the role.
• platform_ml_di.admin
• action_designer
• flow_designer
• sn_ace.ace_user
• canvas_user
• usage_admin
> Source page: 1623

Groups
List of groups this role is assigned to by default.
None.
Special considerations
Important:  Avoid granting an admin role when more specialized roles are available.
DocIntel Viewer [sn_docintel.viewer]
Has view-only access on Document Intelligence document tasks that they are authorized to view.
Contains Roles
List of roles contained within the role.
• snc_read_only
• platform_ml_di.viewer
Groups
List of groups this role is assigned to by default.
None.
Special considerations
Important:  Avoid granting an admin role when more specialized roles are available.
DocIntel Extraction Agent [sn_docintel.extraction_agent]
Extracts information from documents using the Document Intelligence workspace.
Contains Roles
List of roles contained within the role: platform_ml_di.extraction_agent.
Groups
List of groups this role is assigned to by default.
None.
Special considerations
Important:  Avoid granting an admin role when more specialized roles are available.
DocIntel Creation Agent [sn_docintel.creation_agent]
Extracts information from documents using the Document Intelligence workspace. Also enables
users to create Document Intelligence document tasks and submit them for processing.
Contains Roles
List of roles contained within the role: platform_ml_di.creation_agent.
> Source page: 1624

Groups
List of groups this role is assigned to by default.
None.
Special considerations
Important:  Avoid granting an admin role when more specialized roles are available.
DocIntel Manager [sn_docintel.manager]
Creates and edits use cases, fields, field groups, and document tasks. Views, measures, and
analyzes the usage and effectiveness of Document Intelligence using the Platform Document
Intelligence Usage dashboard. Grants access to submit document tasks and interact with the
Document Intelligence workspace.
Contains Roles
List of roles contained within the role.
• platform_ml_di.manager
• action_designer
• flow_designer
• sn_ace.ace_user
• canvas_user
• usage_admin
Groups
List of groups this role is assigned to by default.
None.
Special considerations
Important:  Avoid granting an admin role when more specialized roles are available.
Document Intelligence terminology
Before getting started with Document Intelligence (DocIntel), it's important to understand some
key concepts used in the application.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Updated terminology
As of Document Intelligence v2.3, DocIntel features include updated terminology.
> Source page: 1625

Terminology updates
New term
Old term
Document task
Task, extraction task
Field
Key, attribute
Field group
Key group
Field value
Extracted value
Integration
Integration setup
Recommendation
Candidate, suggestion
Fully automated
Straight through processing
Use case
Task definition
classification
In Document Intelligence, the process of categorizing documents and document pages
based on their type.
confidence score
A numerical value assigned to a recommendation by Document Intelligence indicating
its certainty about the extracted information. The higher the score, the more reliable the
recommendation.
document class
A field used to apply a category or label to a document and to pages within a document in
Document Intelligence.
For example, for an identity document use case, the classes might be passport, driver’s
license, birth certificate, and the like.
document task
A document processing activity in Document Intelligence. It includes the information that
you want to extract from the document or documents.
extraction
In Document Intelligence, the process of identifying relevant information in a document
and using it as a basis for the AI to recommend a field value.
field
A single piece of information to extract from a document in Document Intelligence. For
example, the date on a document.
Fields are sometimes called keys or attributes.
field group
A group of fields that belong together in Document Intelligence. Field groups are used to
extract information from lists and tables.
> Source page: 1626

For example, a group named "item" contains description, quantity, and unit price fields from
a purchase order.
field value
The final output of the Document Intelligence application. The output contains the values
for the specified fields that were extracted for a given document task.
recommendation
A bit of text found on a document. The recommendation includes details about its location
in the document, such as the page of a document and the specific location on that page.
The recommendations that the AI provides are sorted based on how likely the AI believes a
given recommendation to be the correct value for the current field.
unstructured document
A document that mainly contains free-form textual information and does not conform to a
specific format or structure.
use case
A use case is a set of configurations used to define the structure of a type of document that
you want to process. It’s made up of the use case record and its related fields, field groups,
integrations, flows, and all the related machine learning (ML) models. The use case also
includes the mode for how the extraction should occur.
Document task statuses
The following is a list of the statuses for DocIntel document tasks. These statuses apply to tasks
for both document classification and data extraction.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Statuses for document tasks
Status
Description
Setup
The task has been created and is getting
prepared for processing.
New
The task has been initiated by an admin or by
a user who has selected Process Task. The
documents for the task are being processed
and the fields aren’t yet populated.
In Progress
The documents for the task are processed.
The fields are populated through auto-fill
or by a user, who reviews and updates the
predictions generated by the AI as needed.
> Source page: 1627

Statuses for document tasks (continued)
Status
Description
Done
The task is completed after having been
automatically processed in Fully Automated
mode or after a user has reviewed the fields
and selected Submit.
Failed
The task encountered an error during its
processing and failed to process.
Domain separation and Document Intelligence
This domain separation overview relates to Document Intelligence. Domain separation enables
you to separate data, processes, and administrative tasks into logical groupings called domains.
You can then control several aspects of this separation, including which users can see and
access data.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Support level
Support: Basic.
How domain separation works with Document Intelligence
Follow these steps to achieve domain separation:
• Create a user with the required sn_docintel.admin roles in the respective domain.
• Replicate the following for every domain:
◦Document tasks
◦Fields
Languages supported by Document Intelligence
The Document Intelligence application provides support for documents in different languages.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
The language model configured for a use case allows Document Intelligence to detect data
in documents, make predictions for field values, and further train the model in the selected
languages.
> Source page: 1628

Select the language model when creating a document extraction use case. For more information,
see Create a document extraction use case.
The following table lists the languages supported for Document Intelligence along with the
models used to support them.
Document Intelligence languages and models
Model
Languages
Default
English, French, German, Spanish,
Portuguese, Dutch, Italian, Czech, Danish,
Finnish, Norwegian, and Swedish.
OCR for Japanese and Chinese
Chinese (simplified) and Japanese
Limitations in Document Intelligence
There are several important limitations to be aware of when you’re using Document Intelligence.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
For a list of the important limitations in Now Assist in Document Intelligence that differ from the
limitations in Document Intelligence, see Limitations in Now Assist in Document Intelligence.
The following table is a list of the important limitations in Document Intelligence.
Limits in Document Intelligence
Limit
Description
File formats
The supported file formats are JPEG, PNG, and
PDF.
File size limits
The file size limit is 10 MB.
Page count limit per document task
Document Intelligence supports a 10-page
count limit for JPEG and PNG.
For PDFs, the page count limit is 25.
Supported languages
For information on supported languages,
see Languages supported by Document
Intelligence.
Document rotation
Document Intelligence supports rotating in 90-
degree increments.
Text alignment
The text must be aligned horizontally within
the document.
Minimum character size
The minimum character size is 15 pixels.
Character type
Document Intelligence supports only printed
character types in a document.
> Source page: 1629

Limits in Document Intelligence (continued)
Limit
Description
Character set
Document Intelligence detects the following
characters:
• a-z, A-Z, 0–9
• á à â ä ã å ß ç é è ê ë î ï í ñ ó ò ô ö õ ú ù ü û œ
• Á À Â Ä Ã Å ẞ Ç É È Ê Ë Î Ï Í Ñ Ó Ò Ô Ö Õ Ú Ù
Ü Û Œ
• , : ; . ‘ \ ” ! ? ¿ ¡ + - * ( ) [ ] } { & % @   / | ~ ^ < > `
± = _ $ £ ¢ €
Sync/async operations
Async
Maximum number of document tasks
processed per instance per day
The maximum number of document tasks
processed per instance per day is 2000.
Maximum number of fields per use case
The maximum number of fields per document
extraction use case is 50.
The maximum number of fields (categories)
per document classification use case is 30.

---
## IMAGE DESCRIPTIONS
Repeated page furniture: each source page includes the ServiceNow logo in the upper-left header and a standard copyright/page-number footer. These repeated layout elements are accounted for globally and not cropped as separate images for every page.

### Image 1: Important deprecation callout in Reference subsection

* Source page: 1600

* Source crop: [_assets/figures/docintel_p1600_figure_manual_09.png](_assets/figures/docintel_p1600_figure_manual_09.png)

* Approximate PDF coordinates: x0=72.0, y0=586.0, x1=523.0, y1=673.0

A blue `Important` callout at the beginning of the references section repeats the Document Intelligence future deprecation notice and states that Now Assist in Document Intelligence should be used for extracting information from documents.

### Image 2: Confidence score display example

* Source page: 1604

* Source crop: [_assets/images/docintel_p1604_img01.png](_assets/images/docintel_p1604_img01.png)

* Approximate PDF coordinates: x0=102.0, y0=253.9, x1=355.5, y1=403.9

A close-up field recommendation list showing `Lodging` and values such as `USD 750`, `USD`, and `750`. Confidence scores of `50%` appear to the right, along with page indicators such as `p1`. A text entry field at the bottom contains `Lodging`. The image demonstrates that recommendations display percentage confidence scores next to candidate values.

### Image 3: Reference field matching diagram

* Source page: 1606

* Source crop: [_assets/images/docintel_p1606_img01.png](_assets/images/docintel_p1606_img01.png)

* Approximate PDF coordinates: x0=301.1, y0=370.0, x1=517.1, y1=451.3

A diagram showing a `Document task` feeding values into `Fields`, including `Vendor` and `Material ID`. Green highlighted values such as `Degas Dairy Products, Inc` connect to a `Company reference table`, where corresponding reference rows are highlighted. The diagram explains how a reference field compares extracted document values against a standard table to find a matching referenced record.

### Image 4: Integer normalization example

* Source page: 1607

* Source crop: [_assets/images/docintel_p1607_img01.png](_assets/images/docintel_p1607_img01.png)

* Approximate PDF coordinates: x0=72.0, y0=39.0, x1=372.0, y1=189.0

A data-normalization card with a green check mark and label `Order number`. It shows the extracted value `179.00` and a down/turn arrow to normalized integer value `179`. The image demonstrates converting an extracted numeric value into the configured integer field type.

### Image 5: Date normalization reference example

* Source page: 1607

* Source crop: [_assets/images/docintel_p1607_img02.png](_assets/images/docintel_p1607_img02.png)

* Approximate PDF coordinates: x0=72.0, y0=192.2, x1=372.0, y1=394.7

A date conversion panel showing `Date *`, extracted value `10/03/2022`, conversion to `2022-03-10`, warning text `Make sure the converted date is correct`, and `Edit` and `Confirm` buttons. It is a reference example for converted field values and ambiguous-date review.

### Image 6: Inline UI icon

* Source page: 1608

* Source crop: [_assets/images/docintel_p1608_img01.png](_assets/images/docintel_p1608_img01.png)

* Approximate PDF coordinates: x0=226.2, y0=188.6, x1=241.2, y1=202.9

Small inline UI icon embedded in the procedure, table, or screenshot callout on source page 1608. The icon is used as a visual locator for the adjacent instruction, such as a menu, edit, draw-tool, add-line, remove-line, reorder, status, or field-control icon. The crop is retained for traceability; approximate PDF coordinates are (226.2, 188.6, 241.2, 202.9).

### Image 7: Inline UI icon

* Source page: 1608

* Source crop: [_assets/images/docintel_p1608_img02.png](_assets/images/docintel_p1608_img02.png)

* Approximate PDF coordinates: x0=226.2, y0=248.1, x1=241.2, y1=263.1

Small inline UI icon embedded in the procedure, table, or screenshot callout on source page 1608. The icon is used as a visual locator for the adjacent instruction, such as a menu, edit, draw-tool, add-line, remove-line, reorder, status, or field-control icon. The crop is retained for traceability; approximate PDF coordinates are (226.2, 248.1, 241.2, 263.1).

### Image 8: Inline UI icon

* Source page: 1608

* Source crop: [_assets/images/docintel_p1608_img03.png](_assets/images/docintel_p1608_img03.png)

* Approximate PDF coordinates: x0=226.2, y0=307.6, x1=241.2, y1=321.9

Small inline UI icon embedded in the procedure, table, or screenshot callout on source page 1608. The icon is used as a visual locator for the adjacent instruction, such as a menu, edit, draw-tool, add-line, remove-line, reorder, status, or field-control icon. The crop is retained for traceability; approximate PDF coordinates are (226.2, 307.6, 241.2, 321.9).

### Image 9: Inline UI icon

* Source page: 1608

* Source crop: [_assets/images/docintel_p1608_img04.png](_assets/images/docintel_p1608_img04.png)

* Approximate PDF coordinates: x0=226.2, y0=354.6, x1=241.2, y1=369.6

Small inline UI icon embedded in the procedure, table, or screenshot callout on source page 1608. The icon is used as a visual locator for the adjacent instruction, such as a menu, edit, draw-tool, add-line, remove-line, reorder, status, or field-control icon. The crop is retained for traceability; approximate PDF coordinates are (226.2, 354.6, 241.2, 369.6).

### Image 10: Inline UI icon

* Source page: 1608

* Source crop: [_assets/images/docintel_p1608_img05.png](_assets/images/docintel_p1608_img05.png)

* Approximate PDF coordinates: x0=226.2, y0=401.6, x1=240.4, y1=416.6

Small inline UI icon embedded in the procedure, table, or screenshot callout on source page 1608. The icon is used as a visual locator for the adjacent instruction, such as a menu, edit, draw-tool, add-line, remove-line, reorder, status, or field-control icon. The crop is retained for traceability; approximate PDF coordinates are (226.2, 401.6, 240.4, 416.6).

### Image 11: Inline UI icon

* Source page: 1608

* Source crop: [_assets/images/docintel_p1608_img06.png](_assets/images/docintel_p1608_img06.png)

* Approximate PDF coordinates: x0=226.2, y0=448.6, x1=241.2, y1=461.7

Small inline UI icon embedded in the procedure, table, or screenshot callout on source page 1608. The icon is used as a visual locator for the adjacent instruction, such as a menu, edit, draw-tool, add-line, remove-line, reorder, status, or field-control icon. The crop is retained for traceability; approximate PDF coordinates are (226.2, 448.6, 241.2, 461.7).

### Image 12: Inline UI icon

* Source page: 1610

* Source crop: [_assets/images/docintel_p1610_img01.png](_assets/images/docintel_p1610_img01.png)

* Approximate PDF coordinates: x0=401.9, y0=182.2, x1=414.6, y1=197.2

Small inline UI icon embedded in the procedure, table, or screenshot callout on source page 1610. The icon is used as a visual locator for the adjacent instruction, such as a menu, edit, draw-tool, add-line, remove-line, reorder, status, or field-control icon. The crop is retained for traceability; approximate PDF coordinates are (401.9, 182.2, 414.6, 197.2).

### Image 13: Inline UI icon

* Source page: 1615

* Source crop: [_assets/images/docintel_p1615_img01.png](_assets/images/docintel_p1615_img01.png)

* Approximate PDF coordinates: x0=401.9, y0=668.2, x1=414.6, y1=683.2

Small inline UI icon embedded in the procedure, table, or screenshot callout on source page 1615. The icon is used as a visual locator for the adjacent instruction, such as a menu, edit, draw-tool, add-line, remove-line, reorder, status, or field-control icon. The crop is retained for traceability; approximate PDF coordinates are (401.9, 668.2, 414.6, 683.2).

### Image 14: Inline UI icon

* Source page: 1619

* Source crop: [_assets/images/docintel_p1619_img01.png](_assets/images/docintel_p1619_img01.png)

* Approximate PDF coordinates: x0=401.9, y0=87.7, x1=414.6, y1=102.7

Small inline UI icon embedded in the procedure, table, or screenshot callout on source page 1619. The icon is used as a visual locator for the adjacent instruction, such as a menu, edit, draw-tool, add-line, remove-line, reorder, status, or field-control icon. The crop is retained for traceability; approximate PDF coordinates are (401.9, 87.7, 414.6, 102.7).

---
## TABLES
### Table 1: Document Intelligence roles

* Source page: 1601

* Extracted dimensions: 6 rows x 3 columns

| Role title [name] | Description | Contains roles |
| --- | --- | --- |
| DocIntel Admin<br>[sn_docintel.admin] | Has full access to the<br>Document Intelligence<br>application, except for<br>modifying a subset of system<br>properties, and the billing<br>and internal tables. | • platform_ml_di.admin<br>• action designer<br>• flow designer<br>• sn ace.ace user<br>• canvas user<br>• usage admin |
| DocIntel Viewer<br>[sn_docintel.viewer] | Has view-only access on<br>Document Intelligence<br>document tasks that they are<br>authorized to view. | • snc read only<br>• platform_ml_di.viewer |
| DocIntel Extraction Agent<br>[sn_docintel.extraction_agent] | Extracts data and text<br>from documents using the<br>Document Intelligence<br>workspace. | platform_ml_di.extraction agent |
| DocIntel Creation Agent<br>[sn_docintel.creation_agent] | Extracts information from<br>documents using the<br>Document Intelligence<br>workspace. Also enables<br>users to create Document<br>Intelligence document<br>tasks and submit them for<br>processing. | platform_ml_di.creation agent |
| DocIntel Manager<br>[sn_docintel.manager] | Creates and edits use cases,<br>fields, field groups, and<br>document tasks. Views,<br>measures, and analyzes the<br>usage and effectiveness<br>of Document Intelligence<br>using the Platform Document<br>Intelligence Usage<br>dashboard. Grants access to<br>submit document tasks and<br>interact with the Document<br>Intelligence workspace. | • platform_ml_di.manager<br>• action designer<br>• flow designer<br>• sn ace.ace user<br>• canvas user<br>• usage admin |

### Table 2: Tables installed with Document Intelligence

* Source page: 1602

* Extracted dimensions: 11 rows x 2 columns

| Table | Description |
| --- | --- |
| Billable Event<br>[sys_di billable event] | Contains all the billable events for the instance. A billable<br>event corresponds to pages that have been processed using<br>Document Intelligence. |
| Recommendation Meta Info<br>[sys_di candidate meta info] | [Internal table] Contains the data returned by the AI for field<br>group extraction and for missing value prediction. |
| Recommendation Score<br>[sys_di candidate score] | [Internal table] Contains the scores for each recommendation<br>calculated by the AI. There’s one record per field, for each<br>page of a document. |
| Field Value<br>[sys_di extracted value] | Contains all the data extracted in the instance, across all<br>document tasks. |
| Image<br>[sys_di image] | [Internal table] Contains information about each page of a<br>document. There’s one record per document page. |
| Integration Setup<br>[sys_di integration setup] | Contains DocIntel use case integrations. |
| Field<br>[sys_di key] | Contains all the fields created in the instance, across all<br>use cases. A field corresponds to a recommendation to be<br>extracted from documents. |
| Field Group<br>[sys_di key group] | Contains all the field groups created in the instance, across all<br>use cases. A field group is usually created to help extract data<br>from tables and lists. |
| Lock<br>[sys_di lock] | Contains an index of locked task solution definitions. Used to<br>improve the performance of scheduled jobs. |
| DocIntel Aggregated Metrics<br>[sys_di metrics aggregated] | [Internal table] Contains aggregated metrics. Aggregation may<br>happen multiple times per day, based on system properties. |

### Table 3: Tables installed with Document Intelligence (continued)

* Source page: 1603

* Extracted dimensions: 12 rows x 2 columns

| Table | Description |
| --- | --- |
| DocIntel Daily Metrics<br>[sys_di metrics daily] | [Internal table] Contains the metrics aggregated daily. There’s<br>one record per aggregated metric. |
| DocIntel Metrics Job Log<br>[sys_di metrics job log] | [Internal table] Contains a log of the metrics daily aggregation<br>jobs that happened in the instance. |
| DocIntel Raw Metrics<br>[sys_di metrics raw] | [Internal table] Contains a list of raw metrics collected by<br>Document Intelligence. The records are deleted when metrics<br>aggregation happens. |
| DocIntel OCR Input<br>[sys_di ocr input] | [Internal table] Contains image data to be sent to the OCR<br>module for processing. The records are deleted when<br>processing is complete. |
| PDF<br>[sys_di pdf] | [Internal table] Contains a list of PDF files stored across tasks. |
| DocIntel PDF Input<br>[sys_di pdf input] | [Internal table] Contains PDF data to be sent to the PDF<br>module for processing. The records are deleted when<br>processing is complete. |
| DocIntel Prediction Input<br>[sys_di prediction input] | [Internal table] Contains the data needed to make suggestions<br>across all fields for a given document task. There’s one record<br>per document page. |
| Document Task<br>[sys_di task] | Contains all the document tasks created in the instance,<br>across all use cases. A document task contains one or more<br>documents from which fields must be extracted. |
| Task Solution Definition<br>[sys_di task def solution def] | Contains the solution definitions related to DocIntel use cases. |
| DocIntel Use Case<br>[sys_di task definition] | Contains all the document processing use cases created in<br>the instance. A use case defines what and how data should be<br>extracted from a set of documents. |
| DocIntel Training Input<br>[sys_di training input] | [Internal table] Contains the data needed to improve the AI<br>models. |

### Table 4: Data extraction modes reference

* Source page: 1605

* Extracted dimensions: 4 rows x 2 columns

| Extraction mode | Description |
| --- | --- |
| Recommendation | DocIntel provides recommendations for the<br>fields in the Document Intelligence workspace.<br>Choose the recommendation or manually<br>enter the value. All fields must be reviewed.<br>Recommendations are ordered based on<br>how confident the AI is in the prediction.<br>As DocIntel continues processing your<br>documents, recommendations improve over<br>time. |
| Auto-fill | DocIntel auto-fills the fields in the Document<br>Intelligence workspace. All fields must be<br>reviewed.<br>Auto-fill works only if the AI has enough<br>confidence to make the prediction. You can<br>change the confidence threshold by updating<br>the Auto-fill threshold field in the use case. |
| Fully automated<br>(Straight-through processing) | DocIntel automatically extracts the data for<br>all fields and processes the document task if<br>the confidence scores for all required fields<br>are above the defined confidence threshold.<br>Fields don’t need to be reviewed.<br>Note: For Fully automated mode to<br>process tasks successfully, the use case<br>must have at least one field designated<br>as required.<br>DocIntel becomes more confident over time,<br>as it processes more and more documents.<br>Choose Fully automated mode for frequently<br>processed documents or if you’re confident in<br>the system. |

### Table 5: Field types

* Source page: 1606

* Extracted dimensions: 6 rows x 2 columns

| Field type | Description |
| --- | --- |
| Date | Standard date format. For example, YYYY-MM-<br>DD. |
| Reference field | A field that uses a field in another table as a<br>standard. DocIntel matches the extracted data<br>to the standard.<br>For example, a use case has a reference<br>field called Vendor that points to the Name<br>column in the Company table as the reference.<br>When processing a document task, DocIntel<br>extracts “Degas Dairy Products, Inc” from the<br>document and fills the Vendor field with that<br>value. DocIntel compares the value to the<br>company names in the reference table and<br>finds “Degas Dairy Products, Inc” as a match.<br>In the document task, “Degas Dairy Products,<br>Inc” is matched to “Degas Dairy Products, Inc”<br>in the reference. |
| Integer | Whole number. For example, 12. |
| Decimal | Number with up to two decimal places. For<br>example, 12.5 or 12.55. |
| Floating point number | Number with up to seven decimal places. For<br>example, 12.0 to 12.0000000. |

### Table 6: Document field statuses

* Source page: 1608

* Extracted dimensions: 7 rows x 3 columns

| Status | Icon | Description |
| --- | --- | --- |
| To complete |  | The field must be filled in with<br>a value or marked as missing<br>in the document. |
| Completed |  | The field is filled in with a<br>value or marked as missing in<br>the document. |
| To review |  | The field is auto-filled and<br>needs review by a user. |
| Reviewed |  | The auto-filled field has been<br>reviewed by a user. |
| In progress |  | The field is in the process of<br>being filled in or reviewed. |
| Needs attention |  | The auto-filled field has<br>triggered a warning. The<br>causes for a warning include:<br>• A required field must<br>be filled in or marked as<br>missing in the document.<br>• An extracted value has a<br>low confidence score and<br>should be reviewed.<br>• An extracted value is<br>ambiguous and should be<br>verified. |

### Table 7: Check box list form

* Source page: 1609

* Extracted dimensions: 9 rows x 2 columns

| Field | Description |
| --- | --- |
| Check box list |  |
| Check box list name | The name for the check box list as it appears<br>in the Document Intelligence workspace. |
| Target table | The table that stores the document processing<br>results for the check box list. |
| Parent mapping to field | Field on the target table you want to align this<br>check box list with.<br>Note: You must first select a target<br>table. |
| Check boxes |  |
| Check box title | The name for the check box as it appears in<br>the Document Intelligence workspace. |
| Select target field | Field on the target table that you want to align<br>this field with.<br>This field is used for integration with other<br>applications. See Integrate with a custom<br>application or workflow. |
| This field is required for extraction | Option to make a field required.<br>Required fields can’t be left unreviewed. |

### Table 8: Check box list form (continued)

* Source page: 1610

* Extracted dimensions: 4 rows x 2 columns

| Field | Description |
| --- | --- |
|  | Required fields afef ct how document tasks are<br>processed in the Fully automated extraction<br>mode. For more information, see Configure<br>data extraction modes. |
| New check box | Option to add a check box to the list.<br>Use the reorder icon ( ) to reorder a check<br>box in the list. |
| Create multiple check box lists | Option to keep the pop-up window displayed<br>on the screen. Enable this option if you're<br>adding more than one check box list to the use<br>case. |

### Table 9: Single field form

* Source page: 1610

* Extracted dimensions: 4 rows x 2 columns

| Field | Description |
| --- | --- |
| Single field name | The name for the field as it appears in the<br>Document Intelligence workspace. |
| Type | The type of the field. For example, a text or<br>date field.<br>Some field types convert the extracted value<br>into a standard format. For more information,<br>see Data normalization. |
| Converted date format | The date format that the extracted value is<br>converted to for data normalization.<br>This field is available when the Type field is set<br>to Date. |

### Table 10: Single field form (continued)

* Source page: 1611

* Extracted dimensions: 7 rows x 2 columns

| Field | Description |
| --- | --- |
| Target table | The table that stores the document processing<br>results for this use case. |
| Target field | Field on the target table that you want to align<br>this field with.<br>Note: The use case must have a target<br>table selected.<br>This field is used for integration with other<br>applications. For more information, see<br>Integrate with a custom application or<br>workflow. |
| When the date is ambiguous in a document,<br>DocIntel will interpret it in the following order | The default interpretation of the date format.<br>For example, if you select Month first in<br>this field, DocIntel will interpret an ambiguous<br>date like 1/2/2024 as January 2 when it<br>extracts that value from a document. If you<br>select Day first, it will interpret it as<br>February 1.<br>This field is available when the Type field is set<br>to Date. |
| When the number is ambiguous in a<br>document, DocIntel will interpret it as | The default interpretation of the number<br>format.<br>For example, if you select 1,00 in this field,<br>DocIntel will interpret an ambiguous number<br>like 5 as 5,00 instead of 5.00 when it extracts<br>that value from a document.<br>This field is available when the Type field is set<br>to Integer, Decimal, or Float. |
| Reference table | The table that stores the reference column.<br>It’s automatically populated based on the<br>selected target field.<br>This field displays when the Type field is set to<br>Reference field. |
| Reference column | The column in the reference table that<br>contains the referenced data.<br>DocIntel uses the reference column to find<br>data that matches the extracted field value |

### Table 11: Single field form (continued)

* Source page: 1612

* Extracted dimensions: 6 rows x 2 columns

| Field | Description |
| --- | --- |
|  | when processing a document task. The field<br>value is then converted to the format of the<br>reference. For more information on converted<br>values, see Data normalization.<br>This field is available when the Type field is set<br>to Reference field. |
| Distinguisher(s) | Additional columns in the reference table that<br>help the user to distinguish between similar<br>records.<br>This field is available when the Type field is set<br>to Reference field. |
| This single field is required for extraction | Option to make the field required.<br>Required fields can’t be left empty or<br>unreviewed. They also can’t contain<br>ambiguous values. An ambiguous value is a<br>field entry that can be interpreted in more than<br>one way.<br>If it's a reference field type, the required field<br>must have a valid, exact match. By default,<br>DocIntel uses the first matched record.<br>Required fields afef ct how document tasks are<br>processed in the Fully automated extraction<br>mode. For more information, see Configure<br>data extraction modes. |
| Select one of these options for cases when:<br>• the date/number is ambiguous in the<br>document<br>• there are multiple reference matches in the<br>document | Option for agent review in situations when<br>DocIntel encounters an ambiguous value in a<br>required field.<br>In such cases, the selected default<br>interpretation will apply to the extracted value.<br>The option is whether to interrupt full<br>automation of document tasks to allow agents<br>to verify the interpreted values. Otherwise,<br>continue automatic processing of document<br>tasks without the agent review. |
| Create multiple single fields | Option to keep the pop-up window displayed<br>on the screen. Enable this field if you’re adding<br>more than one single field to the use case. |

### Table 12: Single field group form

* Source page: 1613

* Extracted dimensions: 9 rows x 2 columns

| Field | Description |
| --- | --- |
| Field group |  |
| Field group name | The name for the field group as it appears in<br>the Document Intelligence workspace. |
| Target table | The table that stores the document processing<br>results for the fields. |
| Parent mapping to field | Field on the target table that you want to align<br>this field group with.<br>Note: You must first select a target<br>table. |
| This field group is required for extraction | Option to make the field as required.<br>Required fields can’t be left empty or<br>unreviewed. They also can’t contain<br>ambiguous values. An ambiguous value is a<br>field entry that can be interpreted in more than<br>one way.<br>If it’s a reference field type, the required field<br>must have a valid, exact match. By default,<br>DocIntel uses the first matched record.<br>Required fields afef ct how document tasks are<br>processed in the Fully automated extraction<br>mode. For more information, see Configure<br>data extraction modes. |
| Fields |  |
| Field name | The name for the field as it appears in the<br>Document Intelligence workspace. |
| Type | The type of the field. For example, a text or<br>date field. |

### Table 13: Single field group form (continued)

* Source page: 1614

* Extracted dimensions: 7 rows x 2 columns

| Field | Description |
| --- | --- |
|  | Some field types convert the extracted value<br>into a standard format. For more information,<br>see Data normalization. |
| Select Target Field | Field on the target table that you want to align<br>this field with.<br>This field is used for integration with other<br>applications. For more information, see<br>Integrate with a custom application or<br>workflow. |
| When the date is ambiguous in a document,<br>DocIntel will interpret it in the following order | The default interpretation of the date format.<br>For example, if you select Month first in<br>this field, DocIntel will interpret an ambiguous<br>date like 1/2/2024 as January 2 when it<br>extracts that value from a document. If you<br>select Day first, it will interpret it as<br>February 1.<br>This field is available when the Type field is set<br>to Date. |
| When the number is ambiguous in a<br>document, DocIntel will interpret it as | The default interpretation of the number<br>format.<br>For example, if you select 1,00 in this field,<br>DocIntel will interpret an ambiguous number<br>like 5 as 5,00 instead of 5.00 when it extracts<br>that value from a document.<br>This field is available when the Type field is set<br>to Integer, Decimal, or Float. |
| Reference table | The table that stores the reference column.<br>It’s automatically populated based on the<br>selected target field.<br>This field displays when the Type field is set to<br>Reference field. |
| Reference column | The column in the reference table that<br>contains the referenced data.<br>DocIntel uses the reference column to find<br>data that matches the extracted field value<br>when processing a document task. The field<br>value is then converted to the format of the |

### Table 14: Single field group form (continued)

* Source page: 1615

* Extracted dimensions: 7 rows x 2 columns

| Field | Description |
| --- | --- |
|  | reference. For more information on converted<br>values, see Data normalization.<br>This field is available when the Type field is set<br>to Reference field. |
| Distinguisher(s) | Additional columns in the reference table that<br>help the user to distinguish between similar<br>records.<br>This field is available when the Type field is set<br>to Reference field. |
| This field is required for extraction | Option to make a field required.<br>Required fields can’t be left empty or<br>unreviewed. They also can’t contain<br>ambiguous values. An ambiguous value is a<br>field entry that can be interpreted in more than<br>one way.<br>If it’s a reference field type, the required field<br>must have a valid, exact match. By default,<br>DocIntel uses the first matched record.<br>Required fields afef ct how document tasks are<br>processed in the Fully automated extraction<br>mode. For more information, see Configure<br>data extraction modes. |
| Select one of these options for cases when:<br>• the date/number is ambiguous in the<br>document<br>• there are multiple reference matches in the<br>document | Option for agent review in situations when<br>DocIntel encounters an ambiguous value in a<br>required field.<br>In such cases, the selected default<br>interpretation will apply to the extracted value.<br>The option is whether to interrupt full<br>automation of document tasks to allow agents<br>to verify the interpreted values. Otherwise,<br>continue automatic processing of document<br>tasks without the agent review. |
| New single field | Option to add a field to the group.<br>Use the reorder icon ( ) to reorder a field in<br>the group. |
| Create multiple field groups | Option to keep the pop-up window displayed<br>on the screen. Enable this option if you're |

### Table 15: Single field group form (continued)

* Source page: 1616

* Extracted dimensions: 2 rows x 2 columns

| Field | Description |
| --- | --- |
|  | adding more than one single field group to the<br>use case. |

### Table 16: Table form

* Source page: 1616

* Extracted dimensions: 7 rows x 2 columns

| Field | Description |
| --- | --- |
| Table |  |
| Table name | The name for the table as it appears in the<br>Document Intelligence workspace. |
| Target table | The table that stores the document processing<br>results for these table fields. |
| Parent mapping to field | Field on the target table that you want to align<br>this table with.<br>Note: You must first select a target<br>table. |
| This table is required for extraction | Option to make the table fields required.<br>Required table fields can't be left empty<br>or unreviewed. They also can’t contain<br>ambiguous values. An ambiguous value is a<br>field entry that can be interpreted in more than<br>one way.<br>Required fields afef ct how document tasks are<br>processed in the Fully automated extraction<br>mode. For more information, see Configure<br>data extraction modes. |
| Columns |  |

### Table 17: Table form (continued)

* Source page: 1617

* Extracted dimensions: 8 rows x 2 columns

| Field | Description |
| --- | --- |
| Column title | Name of the column header in the table. |
| Type | The type of the field in the table column. For<br>example, a text or date field.<br>Some field types convert the extracted value<br>into a standard format. For more information,<br>see Data normalization. |
| Select target field | Field on the target table that you want to align<br>this field with.<br>This field is used for integration with other<br>applications. For more information, see<br>Integrate with a custom application or<br>workflow. |
| When the date is ambiguous in a document,<br>DocIntel will interpret it in the following order | The default interpretation of the date format.<br>For example, if you select Month first in<br>this field, DocIntel will interpret an ambiguous<br>date like 1/2/2024 as January 2 when it<br>extracts that value from a document. If you<br>select Day first, it will interpret it as<br>February 1.<br>This field is available when the Type field is set<br>to Date. |
| When the number is ambiguous in a<br>document, DocIntel will interpret it as | The default interpretation of the number<br>format.<br>For example, if you select 1,00 in this field,<br>DocIntel will interpret an ambiguous number<br>like 5 as 5,00 instead of 5.00 when it extracts<br>that value from a document.<br>This field is available when the Type field is set<br>to Integer, Decimal, or Float. |
| Reference table | The table that stores the reference column.<br>It’s automatically populated based on the<br>selected target field.<br>This field displays when the Type field is set to<br>Reference field. |
| Reference column | The column in the reference table that<br>contains the referenced data. |

### Table 18: Table form (continued)

* Source page: 1618

* Extracted dimensions: 6 rows x 2 columns

| Field | Description |
| --- | --- |
|  | DocIntel uses the reference column to find<br>data that matches the extracted field value<br>when processing a document task. The field<br>value is then converted to the format of the<br>reference. For more information on converted<br>values, see Data normalization.<br>This field is available when the Type field is set<br>to Reference field. |
| Distinguisher(s) | Additional columns in the reference table that<br>help the user to distinguish between similar<br>records.<br>This field is available when the Type field is set<br>to Reference field. |
| This field is required for extraction | Indicates whether a column required. It’s<br>automatically selected or cleared based on<br>whether the table is required.<br>Required column fields can't be left empty<br>or unreviewed. They also can’t contain<br>ambiguous values. An ambiguous value is a<br>field entry that can be interpreted in more than<br>one way.<br>If it’s a reference field type, the required field<br>must have a valid, exact match. By default,<br>DocIntel uses the first matched record.<br>Required fields afef ct how document tasks are<br>processed in the Fully automated extraction<br>mode. For more information, see Configure<br>data extraction modes. |
| Select one of these options for cases when:<br>• the date/number is ambiguous in the<br>document<br>• there are multiple reference matches in the<br>document | Option for agent review in situations when<br>DocIntel encounters an ambiguous value in a<br>required field.<br>In such cases, the selected default<br>interpretation will apply to the extracted value.<br>The option is whether to interrupt full<br>automation of document tasks to allow agents<br>to verify the interpreted values. Otherwise,<br>continue automatic processing of document<br>tasks without the agent review. |
| New column | Option to add a column to the table. |

### Table 19: Table form (continued)

* Source page: 1619

* Extracted dimensions: 3 rows x 2 columns

| Field | Description |
| --- | --- |
|  | Use the reorder icon ( ) to reorder a column<br>in the table. |
| Create multiple tables | Option to keep the pop-up window displayed<br>on the screen. Enable this option If you're<br>adding more than one table to the use case. |

### Table 20: Document Intelligence properties

* Source page: 1619

* Extracted dimensions: 4 rows x 3 columns

| Property name | Description | Values |
| --- | --- | --- |
| sn_docintel.default field sidebar width | The default sidebar<br>width for the document<br>fields panel in the<br>Document Intelligence<br>workspace. | Allowed:<br>Format of<br>[integer]px<br>Default: 416px |
| sn_docintel.default image fit | The default image fit<br>for the document panel<br>viewer in the Document<br>Intelligence workspace. | Allowed:<br>fit to page,<br>fit to width<br>Default:<br>fit to page |
| sn_docintel.default thumbnail sidebar width | The default thumbnail<br>sidebar width for the<br>navigation panel in the<br>Document Intelligence<br>workspace. | Allowed:<br>Format of<br>[integer]px |

### Table 21: Document Intelligence properties (continued)

* Source page: 1620

* Extracted dimensions: 8 rows x 3 columns

| Property name | Description | Values |
| --- | --- | --- |
|  |  | Default: 167px |
| sn_docintel.field sidebar layout position | The layout position<br>for the document<br>fields panel in the<br>Document Intelligence<br>workspace, in relation<br>to the document fields<br>panel sidebar. | Allowed: right,<br>left<br>Default: right |
| sn_docintel.show exact match option | Show the exact match<br>option for each field<br>in the document fields<br>panel in the Document<br>Intelligence workspace. | Allowed: true,<br>false<br>Default: true |
| sn_docintel.show candidate score | Show confidence<br>scores on the<br>recommendations<br>selection menu in<br>the document fields<br>panel in the Document<br>Intelligence workspace. | Allowed: true,<br>false<br>Default: true |
| sn_docintel.warning score threshold | Threshold used to<br>show the warning<br>icon for low-score<br>recommendations in<br>the document fields<br>panel in the Document<br>Intelligence workspace. | Allowed:<br>Number<br>between 0.0<br>and 1.0<br>Default: 0.7 |
| sn_docintel.autofill threshold | Minimum score<br>threshold required<br>to auto-fill<br>recommendations. | Allowed:<br>Number<br>between 0.0<br>and 1.0<br>Default: 0.0 |
| sn_docintel.straight through processing threshold | Minimum score<br>threshold required<br>for straight-through<br>processing of a<br>document task. | Allowed:<br>Number<br>between 0.0<br>and 1.0<br>Default: 1.0 |

### Table 22: Document Intelligence properties (continued)

* Source page: 1620

* Extracted dimensions: 2 rows x 3 columns

| Property name | Description | Values |
| --- | --- | --- |
| glide.platform_ml_di.doc classifier.<br>days between trainings | Document classifier property | Default: 30 |

### Table 23: Document Intelligence properties (continued)

* Source page: 1621

* Extracted dimensions: 9 rows x 3 columns

| Property name | Description | Values |
| --- | --- | --- |
|  | Minimum number of days between<br>trainings for a given document classifier<br>use case. |  |
| glide.platform_ml_di.doc data extractor.<br>warning score threshold | Document extraction property<br>Threshold used to show the warning<br>icon for low-score recommendations<br>in the document fields panel in the<br>Document Intelligence workspace. | Allowed:<br>Number<br>between<br>0.0 and 1.0<br>Default: 0.7 |
| glide.platform_ml_di.doc data extractor.<br>straight through processing threshold | Document extraction property<br>Minimum score threshold required<br>for straight-through processing of a<br>document task. | Allowed:<br>Number<br>between<br>0.0 and 1.0<br>Default: 1.0 |
| glide.platform_ml_di.doc data extractor.<br>show exact match option | Document extraction property<br>Show the exact match option for each<br>field in the document fields panel in the<br>Document Intelligence workspace. | Allowed:<br>true, false<br>Default:<br>true |
| glide.platform_ml_di.doc data extractor.<br>show candidate score | Document extraction property<br>Show confidence scores on the<br>recommendations selection menu<br>in the document fields panel in the<br>Document Intelligence workspace. | Allowed:<br>true, false<br>Default:<br>true |
| glide.platform_ml_di.doc data extractor.<br>field sidebar layout position | Document extraction property<br>The layout position for the document<br>fields panel in the Document<br>Intelligence workspace, in relation to<br>the document fields panel sidebar. | Allowed:<br>right, left<br>Default:<br>right |
| glide.platform_ml_di.doc data extractor.<br>default thumbnail sidebar width | Document extraction property<br>The default thumbnail sidebar width for<br>the navigation panel in the Document<br>Intelligence workspace. | Allowed:<br>Format of<br>[integer]px<br>Default:<br>167px |
| glide.platform_ml_di.doc data extractor.<br>default image fit | Document extraction property<br>The default image fit for the document<br>panel viewer in the Document<br>Intelligence workspace. | Allowed:<br>fit to page,<br>fit to width<br>Default:<br>fit to page |

### Table 24: Document Intelligence properties (continued)

* Source page: 1622

* Extracted dimensions: 4 rows x 3 columns

| Property name | Description | Values |
| --- | --- | --- |
| glide.platform_ml_di.doc data extractor.<br>default field sidebar width | Document extraction property<br>The default sidebar width for the<br>document fields panel in the Document<br>Intelligence workspace. | Allowed:<br>Format of<br>[integer]px<br>Default:<br>416px |
| glide.platform_ml_di.doc data extractor.<br>autofill threshold | Document extraction property<br>Minimum score threshold required to<br>auto-fill recommendations. | Allowed:<br>Number<br>between<br>0.0 and 1.0<br>Default:<br>0.01 |
| glide.platform_ml_di.doc data extractor.<br>draw tool enable | This property is used to enable or<br>disable draw tool features for table<br>extraction. | Allowed:<br>true, false<br>Default:<br>true |

### Table 25: Terminology updates

* Source page: 1625

* Extracted dimensions: 9 rows x 2 columns

| New term | Old term |
| --- | --- |
| Document task | Task, extraction task |
| Field | Key, attribute |
| Field group | Key group |
| Field value | Extracted value |
| Integration | Integration setup |
| Recommendation | Candidate, suggestion |
| Fully automated | Straight through processing |
| Use case | Task definition |

### Table 26: Statuses for document tasks

* Source page: 1626

* Extracted dimensions: 4 rows x 2 columns

| Status | Description |
| --- | --- |
| Setup | The task has been created and is getting<br>prepared for processing. |
| New | The task has been initiated by an admin or by<br>a user who has selected Process Task. The<br>documents for the task are being processed<br>and the fields aren’t yet populated. |
| In Progress | The documents for the task are processed.<br>The fields are populated through auto-fill<br>or by a user, who reviews and updates the<br>predictions generated by the AI as needed. |

### Table 27: Statuses for document tasks (continued)

* Source page: 1627

* Extracted dimensions: 3 rows x 2 columns

| Status | Description |
| --- | --- |
| Done | The task is completed after having been<br>automatically processed in Fully Automated<br>mode or after a user has reviewed the fields<br>and selected Submit. |
| Failed | The task encountered an error during its<br>processing and failed to process. |

### Table 28: Document Intelligence languages and models

* Source page: 1628

* Extracted dimensions: 3 rows x 2 columns

| Model | Languages |
| --- | --- |
| Default | English, French, German, Spanish,<br>Portuguese, Dutch, Italian, Czech, Danish,<br>Finnish, Norwegian, and Swedish. |
| OCR for Japanese and Chinese | Chinese (simplified) and Japanese |

### Table 29: Limits in Document Intelligence

* Source page: 1628

* Extracted dimensions: 9 rows x 2 columns

| Limit | Description |
| --- | --- |
| File formats | The supported file formats are JPEG, PNG, and<br>PDF. |
| File size limits | The file size limit is 10 MB. |
| Page count limit per document task | Document Intelligence supports a 10-page<br>count limit for JPEG and PNG.<br>For PDFs, the page count limit is 25. |
| Supported languages | For information on supported languages,<br>see Languages supported by Document<br>Intelligence. |
| Document rotation | Document Intelligence supports rotating in 90-<br>degree increments. |
| Text alignment | The text must be aligned horizontally within<br>the document. |
| Minimum character size | The minimum character size is 15 pixels. |
| Character type | Document Intelligence supports only printed<br>character types in a document. |

### Table 30: Limits in Document Intelligence (continued)

* Source page: 1629

* Extracted dimensions: 5 rows x 2 columns

| Limit | Description |
| --- | --- |
| Character set | Document Intelligence detects the following<br>characters:<br>• a-z, A-Z, 0–9<br>• á à â ä ã å ß ç é è ê ë î ï í ñ ó ò ô ö õ ú ù ü û œ<br>• Á À Â Ä Ã Å ẞ Ç É È Ê Ë Î Ï Í Ñ Ó Ò Ô Ö Õ Ú Ù<br>Ü Û Œ<br>• , : ; . ‘ \ ” ! ? ¿ ¡ + - * ( ) [ ] } { & % @ / \| ~ ^ < > `<br>± = _ $ £ ¢ € |
| Sync/async operations | Async |
| Maximum number of document tasks<br>processed per instance per day | The maximum number of document tasks<br>processed per instance per day is 2000. |
| Maximum number of fields per use case | The maximum number of fields per document<br>extraction use case is 50.<br>The maximum number of fields (categories)<br>per document classification use case is 30. |

---
## FIGURES
### Figure 1: Important deprecation callout in Reference subsection

* Source page: 1600

* Source crop: [_assets/figures/docintel_p1600_figure_manual_09.png](_assets/figures/docintel_p1600_figure_manual_09.png)

A blue `Important` callout at the beginning of the references section repeats the Document Intelligence future deprecation notice and states that Now Assist in Document Intelligence should be used for extracting information from documents.

### Figure 2: Confidence score display example

* Source page: 1604

* Source crop: [_assets/images/docintel_p1604_img01.png](_assets/images/docintel_p1604_img01.png)

A close-up field recommendation list showing `Lodging` and values such as `USD 750`, `USD`, and `750`. Confidence scores of `50%` appear to the right, along with page indicators such as `p1`. A text entry field at the bottom contains `Lodging`. The image demonstrates that recommendations display percentage confidence scores next to candidate values.

### Figure 3: Reference field matching diagram

* Source page: 1606

* Source crop: [_assets/images/docintel_p1606_img01.png](_assets/images/docintel_p1606_img01.png)

A diagram showing a `Document task` feeding values into `Fields`, including `Vendor` and `Material ID`. Green highlighted values such as `Degas Dairy Products, Inc` connect to a `Company reference table`, where corresponding reference rows are highlighted. The diagram explains how a reference field compares extracted document values against a standard table to find a matching referenced record.

### Figure 4: Integer normalization example

* Source page: 1607

* Source crop: [_assets/images/docintel_p1607_img01.png](_assets/images/docintel_p1607_img01.png)

A data-normalization card with a green check mark and label `Order number`. It shows the extracted value `179.00` and a down/turn arrow to normalized integer value `179`. The image demonstrates converting an extracted numeric value into the configured integer field type.

### Figure 5: Date normalization reference example

* Source page: 1607

* Source crop: [_assets/images/docintel_p1607_img02.png](_assets/images/docintel_p1607_img02.png)

A date conversion panel showing `Date *`, extracted value `10/03/2022`, conversion to `2022-03-10`, warning text `Make sure the converted date is correct`, and `Edit` and `Confirm` buttons. It is a reference example for converted field values and ambiguous-date review.

---
## QUALITY ASSURANCE NOTES
* PAGES REVIEWED: 1600-1629
* IMAGES REVIEWED: 14 non-header image entries; 5 major screenshot/diagram/callout/figure entries. Repeated ServiceNow header logos and footers are documented as page furniture.
* TABLES REVIEWED: 30 table entries assigned to this subsection and converted into Markdown tables in the `TABLES` section.
* FIGURES REVIEWED: 5 major figures/diagrams/screenshots/callouts with detailed component-level descriptions.
* OCR ISSUES FOUND: The PDF contains a selectable text layer, but extraction artifacts were present, including soft-hyphen characters, split link punctuation, ligature-like errors such as `difefrent`/`efefctive`/`fei ld`, and table-extraction spacing issues in bracketed role and table identifiers.
* OCR ISSUES CORRECTED: Soft hyphen and zero-width characters were normalized; repeated footer/page furniture was removed from main content and accounted for in QA; common text-layer artifacts were corrected; tables were separately extracted and converted to Markdown with cleaned cells.
* RECHECK PASSES COMPLETED: 12/12: page completeness, text extraction, table extraction, image extraction/documentation, diagram interpretation, section mapping, subsection mapping, file names, folder names, Markdown formatting, missed-content review, and OCR/text-layer cleanup review.
* SECTION/SUBSECTION MAPPING NOTE: Page 1600 starts at the exact source heading `Document Intelligence references`.
* SECTION/SUBSECTION MAPPING NOTE: Page 1629 is shared with the next major TOC section. The `Limits in Document Intelligence (continued)` table above `Task Intelligence` is included in `Reference`; the next-section `Task Intelligence` content is preserved as boundary content in `_assets/boundary_content_page_1629.md`.
* NEXT-SECTION BOUNDARY NOTE: Source page 1629 contains Document Intelligence reference content above the next major section heading `Task Intelligence`; only the Document Intelligence portion is included in this file, and the Task Intelligence boundary content is preserved in `_assets/boundary_content_page_1629.md`.
* FOOTER/PAGE FURNITURE NOTE: The repeated ServiceNow logo, copyright notice, trademark notice, and page number appear on each source page; they are accounted for globally and removed from repeated content extraction to avoid duplicated page furniture.
