# Use
## SOURCE INFORMATION
* SECTION NAME: Document Intelligence
* SUBSECTION NAME: Use
* SOURCE FILE NAME: Document Intelligence.pdf
* PAGE RANGE: 1574-1595 (page 1595 split before `Monitoring Document Intelligence performance`)
* EXTRACTION DATE: 2026-06-17

---
# CONTENT
> Source page: 1574

Using Document Intelligence
Use document tasks to process documents for classification and data extraction in Document
Intelligence.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
In a document task, you upload the single or multi-page documents you want to process. Then
DocIntel processes them by detecting and analyzing text in those documents and auto-filling or
providing recommendations to populate the fields defined in the use case.
For document tasks that aren’t yet fully automated, training the DocIntel AI is an important part of
achieving full automation.
> Source page: 1575

Process document tasks in the following steps:
1. Create a document task.
a. Create the task record.
b. Process the document task.
2. Complete a document task.
a. Use the Document Intelligence workspace to train the AI.
b. Submit the document task.
Create a document task
Create a document task and upload single or multi-page documents that are in JPEG, PNG, or
PDF formats to start extracting text or classifying documents.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Before you begin
Role required: sn_docintel.creation_agent
About this task
These are the manual steps to create a document task. If you have integrations set up with
other workflows, this task may be automated. See Integrating Document Intelligence with other
applications.
Procedure
1. Do one of the following:
◦To create a document task for document data extraction, navigate to All > Document
Intelligence > Document Data Extraction > Create Document Task.
◦To create a document task for document classification, navigate to All > Document
Intelligence > Document Classification > Create Document Task.
2. On the form, fill in the fields.
New document task record
Field
Description
Display Name
The name associated with this use case. For
example, PO-1.
Use Case
The use case created for this document type.
3. Select the Manage Attachments icon and select the document you want to upload for
processing.
> Source page: 1576

4. Select Process Task.
Document Intelligence analyzes the document and extracts data or classes for the fields
defined in the use case.
What to do next
Find the document task in the document tasks list. After the Is Processed field changes to
True, Document Intelligence has completed the analysis of the document. You can proceed
to complete the document task, which helps train the AI through your input or review of the
extracted fields.
Complete a document task
After the document task processing is finished, complete the task by providing input or review to
train the AI.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Before you begin
Role required: sn_docintel.extraction_agent
Procedure
1. Do one of the following:
◦To complete a document task for document data extraction, navigate to All > Document
Intelligence > Document Data Extraction > Document Tasks.
◦To complete a document task for document classification, navigate to All > Document
Intelligence > Document Classification > Document Tasks.
2. Review the document task list and ensure that the document task's Is Processed field is set to
true.
The following image shows the list of document tasks. If the Is Processed field for a task is true,
that indicates that the task has been processed and is available for user input.
If the status appears as Setup, go to the document task record and select Process Task.
> Source page: 1577

Document tasks list
3. Select the processed document task.
4. Select Show in DocIntel.
The following image shows how to navigate to the Document Intelligence workspace for data
extraction.
Navigating to the DocIntel workspace
The Document Intelligence workspace opens in a new tab.
5. Use the Document Intelligence workspace to review the document fields and select the
appropriate recommendations.
Learn how to use the Document Intelligence workspace to extract fields.
Learn how to use the Document Intelligence workspace to classify documents.
6. Select Submit to complete the document task.
Extract fields using the Document Intelligence workspace
Use the Document Intelligence workspace for field extraction, searching for recommendations,
flagging fields, and identifying missing fields to complete document tasks.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Overview of the Document Intelligence workspace
The Document Intelligence (DocIntel) workspace provides document management features that
enable you to quickly review and process text extraction.
With the Document Intelligence workspace, you can:
> Source page: 1578

• Efficiently review the AI's recommendations, and confirm your document's extracted text.
• Flag fields, identify missing fields, and review pending fields.
To get started with the Document Intelligence workspace:
• Create a document task for a document data extraction use case, upload a document, and
process the task.
• After DocIntel has processed the task, you can begin using the workspace. See Complete a
document task.
Layout of the Document Intelligence workspace
The following illustration shows the Document Intelligence workspace for a document task. The
workspace includes the following areas:
• 1 - Thumbnail panel
• 2 - Document image panel
• 3 - Document controls
• 4 - Document fields panel
• 5 - Table panel
Note:  In this view, the document fields panel is expanded so that the fields are visible.
Thumbnail panel
In the thumbnail panel of the workspace, you can select one page from a multiple-page
document. The selected page is displayed in the document image panel. Selecting a page
doesn’t affect what is displayed in the document fields panel.
The following image shows a document with two pages in the thumbnail panel.
> Source page: 1579

Document image panel
The document image panel displays the page selected in the thumbnail panel.
As you move through the recommendations in the fields in the document fields panel, they’ll be
highlighted in the document image panel to help you select the correct option.
You can also extract information directly from the document image using the draw tool. For more
details, see Extract fields using the draw tool.
Document controls
When you’re reviewing a document for extraction, you can use various controls to maximize the
viewing area, zoom, or focus on the areas that you need. You can also extract information directly
from the document image using the draw tool. For more details, see Extract fields using the draw
tool.
> Source page: 1580

The following illustration shows document controls.
Document fields panel
The document fields panel enables you to open items for review, including viewing the AI's
recommendations. You can also flag fields or mark fields as missing in the document.
Note:  An asterisk indicates a required field.
The following illustration shows the different features of the document fields panel.
Table panel
The table panel enables you to open table rows for review, including viewing the AI's
recommendations. You can also flag fields or mark fields as missing in the document. Other table
controls enable you to insert rows and resize columns as needed.
Note:  An asterisk in the column heading indicates a required field.
The following illustration shows the different features of the table panel.
> Source page: 1581

Extract single fields
Extract text and number fields from your document in the document fields panel.
Before you begin
Role required: sn_docintel.extraction_agent
About this task
Use the following steps to extract single fields from a document.
If the fields are already auto-filled with values, you can review them to ensure they are correct or
adjust the fields as needed.
Tip:  You can also use the draw tool to easily extract fields directly on the document image.
For more information, see Extract fields using the draw tool.
Procedure
1. In the document fields panel, expand Fields.
2. Select a field.
3. Begin typing in the field and select a recommendation from the drop-down list.
The recommendation with the highest confidence score displays at the top of the list.
Tip:  As you move through the recommendations in the drop-down list, they’re
highlighted in the document to help you select the correct option.
4. Optional:  If needed, filter or flag the recommendations
◦To filter the list to show only a recommendation that matches exactly what you type, select
the exact match mode icon (
) in the field.
◦To flag the field for later attention, select Flag for follow-up in the field options menu (
).
◦If you can’t find an appropriate match in the document, select Missing in the document in
the field options menu. To undo, select the Edit icon (
) in the field.
The field will be marked as complete when you move to the next field.
5. Optional:  If needed, confirm or correct any field value conversions.
> Source page: 1582

(Optional) Some field types convert the extracted value into a standard format. See Data
normalization.
When the extracted value is ambiguous in a document, DocIntel interprets it as defined in the
field configuration. A note prompts you to confirm or edit the converted value.
◦Select Confirm in the converted value field to confirm that the converted value is accurate.
◦Select Edit, enter the updated value, and select Save to correct the conversion.
Extract check box fields
Extract check box fields from your document in the document fields panel.
Before you begin
Role required: sn_docintel.extraction_agent
About this task
Use the following steps to extract check box fields from a document.
If the check box fields are already auto-filled, you can review them to ensure they are correct or
adjust the fields as needed.
Procedure
1. In the document fields panel, expand Fields.
2. Select a field.
A list of check boxes displays if the field is designated as a check box field type.
3. Select the check boxes that apply to the field group.
For each check box selected, DocIntel may provide one or more potential matches in the
document.
a. Select a check box.
b. If there's more than one recommendation on the document image that matches the check
box, select the one that applies.
You can select or deselect a recommendation on the document at any time.
> Source page: 1583

Tip:
▪Press Tab on the keyboard to move through the recommendations.
▪Press Enter or Return to select one.
▪To deselect a recommendation, select another one.
c. If there are no recommendations found, or if none of the recommendations are correct,
select Show all check box recommendations in the check box options menu (
) and
choose from any other options in the document.
Tip:  Flag the check box for later attention by selecting Flag for follow-up in the check
box option menu.
d. If you can’t find an appropriate match for the check box in the document, select No match
found in the check box option menu.
e. Repeat these steps for each check box that applies to the field group.
4. If you're in the Recommendation mode, ensure that all fields are marked complete.
If you're in the Auto-fill mode, mark the fields as reviewed.
Extract table fields
Extract table fields from your document in the table panel.
Before you begin
Role required: sn_docintel.extraction_agent
About this task
Use the following steps to extract table fields from a document.
If the fields are already auto-filled with values, you can review them to ensure they’re correct or
adjust the fields as needed.
Tip:  You can also use the draw tool to easily extract tables directly on the document
image. For more information, see Extract fields using the draw tool.
Procedure
1. In the document fields panel, expand Tables.
The Tables section only displays fields assigned to a table field group.
2. Select a table.
The table panel displays.
3. Select the recommendation that applies to each table field.
◦To select a recommendation, begin typing in the field and select a recommendation from the
drop-down list.
Tip:  As you move through the recommendations in the drop-down list, they are
highlighted in the document to help you select the correct option.
> Source page: 1584

◦To flag the field for later attention, select Flag for follow-up in the field options menu (
).
◦If you can’t find an appropriate match in the document, select Missing in the document in
the field options menu. To undo, select the Edit icon (
) in the field.
4. Optional:  If needed, confirm or correct any field value conversions.
(Optional) Some field types convert the extracted value into a standard format. See Data
normalization.
When the extracted value is ambiguous in a document, DocIntel interprets it as defined in the
field configuration. A note prompts you to confirm or edit the converted value.
◦Select Confirm in the converted value field to confirm that the converted value is accurate.
◦Select Edit, enter the updated value, and select Save to correct the conversion.
5. Adjust the table rows as needed.
Warning:  If you have a grid on the document image, changes made directly to the
table rows can’t be synced to the grid(s). The grid(s) will be removed to avoid conflicting
data.
◦To add a row, select New row.
◦To clear all field values in the row, select Clear row values in the row options menu (
).
◦To insert a row, select Insert row above or Insert row below in the row options menu.
◦To delete a row, select Delete row in the row options menu.
◦To mark a row as reviewed, select Mark row as reviewed in the row options menu.
◦To make changes to multiple rows, select the check box in the first column of each row and
select an action from the Action on selected rows list.
6. Review and complete the rows.
◦If you filled in the fields, ensure that all rows are marked as complete.
◦If the fields are auto-filled with values, then all rows are marked as reviewed.
> Source page: 1585

Extract fields using the draw tool
Use the draw tool to extract information directly from text and tables on the document image.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Overview of the draw tool
When viewing a processed document in the Document Intelligence workspace, you can use the
draw tool to extract and review fields from the document image.
Especially in cases when there are no recommendations yet or incorrect recommendations, the
draw tool is useful for selecting the specific area on the document you want to extract.
Any extracted table fields should already appear in a grid over the table. An extracted single field
appears as a labeled box over the text. You can review the extracted fields right from the grid or
box and make adjustments as needed. If the table fields are empty or there is no grid, you can
create one or more grids over the table to extract the fields.
Extract a single field using the draw tool
Use the draw tool to extract a single field directly from the document image.
Before you begin
Role required: sn_docintel.extraction_agent
About this task
Use the following steps to extract a single field from a document using the draw tool. The
extracted data is used to fill the related field in the document fields panel.
If the field is auto-filled, a box already appears over the extracted text. You can adjust the field as
needed.
> Source page: 1586

Procedure
1. In the document fields panel, expand Fields.
2. Select a field.
The Draw Tool icon (
) is enabled in the document controls toolbar.
If the field is already auto-filled and the box appears over the field, or if you’ve already drawn a
box, proceed to step 5.
3. Select the Draw Tool icon (
).
4. Draw a box over the area on the document image that you want to extract.
An editable box appears over the text. The field name is displayed next to the box. The
extracted text in the box appears highlighted.
Box drawn on a single field
The extracted text fills the related field in the document fields panel.
Tip:  Press Enter or Return in the filled field to move to the next field and draw a new box.
5. Optional:  Adjust the box as needed.
Option
Description
Resize the box
(Optional) Select the box. Drag the box edge
or corner to the desired position.
The updated text in the box is extracted and
fills the related field in the document fields
panel.
Remove the box
(Optional) Select the Remove the box icon
(
).
The box is deleted and the extracted value is
removed from the field.
Extract to a different field
(Optional) Select the field name next to the
box and choose another option from the list.
> Source page: 1587

6. Optional:  Edit the extracted text by entering the changes in the field.
DocIntel may not detect all the text within the selected area. In this case, you may need to
enter the information directly in the field.
Extract a table using the draw tool
Use the draw tool to extract a table directly from the document image.
Before you begin
Role required: sn_docintel.extraction_agent
About this task
Use the following steps to extract a table from a document using the draw tool. The extracted
data is used to fill the related table fields.
If the table fields are auto-filled, a draw tool grid is already available based on the extracted
fields. You can adjust the fields as needed. For more information, see Adjust the draw tool grid.
You can select multiple sections of a table throughout the pages of a document.
Procedure
1. In the document fields panel, expand the Tables section.
The Tables section only displays fields assigned to a table field group.
2. Select a table in the Tables section.
The table panel is displayed, and the Draw Tool icon (
) is enabled in the document controls
toolbar.
If the table fields are already auto-filled and the grid appears over the table, or if you’ve already
drawn a grid, proceed to step 5.
Tip:  Collapse the Table panel using the Collapse table panel icon (
), if needed.
3. Select the Draw Tool icon (
).
4. Draw a box over the area on the document image that you want to extract.
Tip:  Include the header row of the table in the selection area.
An editable grid appears over the table. The grid defines the table cells in the area that you
selected. The row numbers in the grid correspond to the rows in the Table panel.
The text in the cell appears surrounded by a dotted-line box before it is extracted to the table
fields. After it is extracted, it appears in a solid-line box.
> Source page: 1588

5. Adjust the grid as needed.
For more information, see Adjust the draw tool grid.
6. Optional:  To select another section of the table on the same or a different page of the
document:
a. Select the Draw Tool icon (
).
b. Draw a box over the other area on the document image that you want to extract.
Note:  It isn’t possible to draw a new grid over an existing one.
The grid number beside the table name shows the updated grid number. For example, “Line
items (2/2)” shows you are in the second out of two grids used to extract the Line items table
fields.
c. Adjust the grid as needed.
7. Optional:  To hide the grid(s), select the Hide/show the grid(s) icon (
).
(Optional) A partly-transparent box shows where a hidden grid is located on the document.
Select the hidden grid or the Hide/show the grid(s) icon to show the grid.
8. Extract the data.
◦Select Extract data.
This button displays if no data has been extracted yet.
◦Select Update fields.
> Source page: 1589

This button displays if the table fields are already filled and you have made changes that will
overwrite some of them.
The Update fields button shows the number of fields to be updated.
The data in the grid(s) are extracted and used to fill the related table fields.
If there are any empty cells or missing columns in the grid(s), the related table fields are set to
Missing in the document.
Adjust the draw tool grid
Adjust the draw tool grid to better fit the information that you want to extract from the document
image.
Before you begin
• These steps apply to tables that have a draw tool grid on the document image. For more
information, see Extract a table using the draw tool.
• Role required: sn_docintel.extraction_agent
About this task
Use the following steps to make changes to a grid. You can then extract the updates to the
related table fields.
Procedure
1. On the document image, select the grid that you want to change.
If you have more than one grid on the document, only one displays editing tools. The other grid
appears as an overlay until you select it for editing.
> Source page: 1590

2. Adjust the grid as needed.
Adjustments are auto-saved.
Any adjustments that produce a change to previous extractions are indicated in the cell corner.
The text in the cell appears surrounded by a solid-line box if it’s already extracted. It appears in
a dotted-line box if it isn’t extracted yet.
Option
Description
Move the grid
Drag the Move icon (
) to the desired posi
tion.
Change a column header
Select the column header and select the col
umn where the data will be extracted to in the
table fields.
Make the first row a header row
Select the row header and check the This is a
header row check box.
Move a column or row border
Drag the border to the desired position.
Add a new column or row
Go to the outside border of the grid and se
lect the Add a line icon (
).
Adding a line splits the affected cells so they
can be extracted to separate fields.
Remove a column or row border
Select the Remove a line icon (
) at the end
of the border outside the grid.
Removing a line merges the affected cells so
they can be extracted to the same fields.
Remove the grid
Select the Remove the grid icon (
).
This action only removes the grid, not the ex
tracted data.
Ignore a table column or row
a. Select the column or row heading.
b. Select the Do not extract this column/row
check box.
c. Select Save.
Review a field on the document image
Use the draw tool to review auto-filled fields directly from the document image panel.
> Source page: 1591

Before you begin
• These steps apply to tables that have a draw tool grid or single fields that have a draw tool box
on the document. For more information, see Extract a table using the draw tool or Extract a
single field using the draw tool.
• Role required: sn_docintel.extraction_agent
Procedure
1. On the document image, point to a grid cell or field box you want to review.
For a single field, an editable box appears over the text. The field name is displayed next to the
box.
For a table field, the text in the grid cell appears surrounded by a box if the value is extracted.
2. Verify the value that appears in the field’s tooltip.
◦If the value is accurate, move on to review the next field.
◦If the value must be changed, edit the field.
See Edit a field on the document image.
3. Repeat steps 1 and 2 for each field that you want to review.
Edit a field on the document image
Edit the fields on the document image to make sure that the correct information is extracted.
Before you begin
• These steps apply to tables that have a draw tool grid or single fields that have a draw tool box
on the document. For more information, see Extract a table using the draw tool or Extract a
single field using the draw tool.
• Role required: sn_docintel.extraction_agent
> Source page: 1592

About this task
Use the following steps to change to a field by editing the recommendation on the document
image. The text detected by DocIntel appears surrounded by a box.
Procedure
1. On the document image, select the text box or the grid cell that you want to edit.
A dialog box appears, showing the related field.
2. Enter a value in the text box or select another recommendation from the list.
3. Select Save.
Classify documents using the Document Intelligence workspace
Use the Document Intelligence workspace to label your documents. The workspace enables
you to train the AI model by providing direct input and by validating or correcting the
recommendations provided by DocIntel.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Overview of the Document Intelligence workspace
The Document Intelligence (DocIntel) workspace provides features that enable you to quickly
apply classes or categories to the attached documents and each of their pages.
To get started with the Document Intelligence workspace, complete the following:
> Source page: 1593

• Create a document task for a document classification use case, upload a document, and
process the task.
• After DocIntel has processed the task, you can begin using the workspace. See Complete a
document task.
Layout of the Document Intelligence workspace
The following image shows the Document Intelligence workspace for a document task. The
workspace includes the following areas:
• 1 - Thumbnail panel
• 2 - Document image panel
• 3 - Document controls
• 4 - Classify panel
Note:  In this view, the documents in the Classify panel are expanded so that the
categories are visible.
Thumbnail panel
In the thumbnail panel of the workspace, you can select one page from one or more multiple-
page documents. The selected page is displayed in the document image panel. Selecting a page
doesn’t affect what is displayed in the Classify panel.
Document image panel
The document image panel displays the page selected in the thumbnail panel.
Document controls
When you’re reviewing a document for classification, you can use various controls to rotate,
maximize the viewing area, zoom, or focus on the areas that you need.
Classify panel
The Classify panel enables you to open each document and page classification for review,
including viewing the AI's recommendations.
The following image shows the Classify panel with a category field for each attachment in the
document task, enabling you to enter or review the category.
> Source page: 1594

Classify documents and document pages
Classify your documents in the Classify panel.
Before you begin
Role required: sn_docintel.extraction_agent
About this task
Use the following steps to apply categories to document attachments and each of their pages.
In this context, a document page is the individual page object of the digital document file, as
displayed in the thumbnail panel of the workspace. A document file may contain multiple logical
groupings of documents (like a PDF file with several invoices, each spanning several pages).
Based on the contents, apply the categorization to the document file and the file pages.
If the categories are already auto-filled with values, you can review them to ensure they are
correct or adjust them as needed.
Procedure
1. In the Classify panel, review any auto-filled categories for each document to ensure they’re
correct.
2. Select a category for a document by selecting the Category field.
3. Select an appropriate recommendation for the document using the recommendation list.
◦Begin typing in the Category field and select a recommendation from the list.
The recommendation with the highest confidence score displays at the top of the list.
◦Select Mixed categories for a multi-page document that includes more than one document
type.
Otherwise, if you select a category for a multi-page document, that category is applied to all
of the document's pages.
◦Select Blank Page for a blank page in a document.
◦Select No category found if you can’t find a correct match.
The document will be marked as complete when you move to the next Category field.
4. Select a recommendation for each page of a Mixed categories document.
> Source page: 1595

The page will be marked as complete when you move to the next page.
5. Optional:  If needed, flag the documents or pages for later attention by selecting Flag for
follow-up in the options menu from the options icon (
).

---
## IMAGE DESCRIPTIONS
Repeated page furniture: each source page includes the ServiceNow logo in the upper-left header and a standard copyright/page-number footer. These repeated layout elements are accounted for globally and not cropped as separate images for every page.

### Image 1: Important deprecation callout in Use subsection

* Source page: 1574

* Source crop: [_assets/figures/docintel_p1574_figure_manual_07.png](_assets/figures/docintel_p1574_figure_manual_07.png)

* Approximate PDF coordinates: x0=72.0, y0=570.0, x1=523.0, y1=657.0

A blue `Important` callout in the `Using Document Intelligence` introduction repeats the Document Intelligence future deprecation notice and references `KB0867184`, establishing that readers should consider Now Assist in Document Intelligence for current/future extraction scenarios.

### Image 2: Document task attachment upload and Process Task button

* Source page: 1576

* Source crop: [_assets/images/docintel_p1576_img01.png](_assets/images/docintel_p1576_img01.png)

* Approximate PDF coordinates: x0=82.0, y0=39.0, x1=514.0, y1=166.7

A ServiceNow document task form is dimmed behind an `Attachments` dialog. The dialog shows an upload/paperclip graphic and an uploaded attachment area. A purple arrow points toward the `Process Task` button on the form. The image demonstrates that a user attaches a document and then starts processing by selecting `Process Task`.

### Image 3: Document tasks list

* Source page: 1577

* Source crop: [_assets/images/docintel_p1577_img01.png](_assets/images/docintel_p1577_img01.png)

* Approximate PDF coordinates: x0=112.0, y0=52.0, x1=544.0, y1=173.4

A ServiceNow list of document tasks. The list contains multiple rows with columns such as display name, state, processed status, use case, and related dates. The screenshot shows how to locate a processed document task after processing completes.

### Image 4: Document task form with Show in DocIntel button

* Source page: 1577

* Source crop: [_assets/images/docintel_p1577_img02.png](_assets/images/docintel_p1577_img02.png)

* Approximate PDF coordinates: x0=112.0, y0=271.2, x1=544.0, y1=373.4

A ServiceNow document task form with the `Show in DocIntel` button highlighted. The form contains fields such as display name, use case, target table, working message, and error message. The screenshot shows the action used to open the Document Intelligence workspace for the selected task.

### Image 5: Document Intelligence workspace layout for data extraction

* Source page: 1578

* Source crop: [_assets/images/docintel_p1578_img01.png](_assets/images/docintel_p1578_img01.png)

* Approximate PDF coordinates: x0=72.0, y0=355.7, x1=504.0, y1=621.4

An annotated Document Intelligence workspace screenshot for an invoice task. Numbered callouts identify major regions: `1` the thumbnail panel on the left; `2` the central document image panel with highlighted extracted text; `3` the top toolbar with page navigation and viewer controls; `4` the Fields panel on the right; and `5` the bottom table/field-group grid used for extracted line items. A `Submit` button appears near the top-right. The figure explains the workspace zones agents use to review extracted fields and tables.

### Image 6: Workspace field review notification and invoice viewer

* Source page: 1579

* Source crop: [_assets/images/docintel_p1579_img01.png](_assets/images/docintel_p1579_img01.png)

* Approximate PDF coordinates: x0=72.0, y0=39.0, x1=504.0, y1=274.2

A Document Intelligence workspace screenshot with an invoice document displayed in the central viewer and a fields panel on the right. A notification reads that the user should review this field and other fields before submitting the task. The right panel includes field status counts and a `Submit` button. The image demonstrates that fields may require human review before final submission.

### Image 7: PO number field recommendation mapped from invoice text

* Source page: 1579

* Source crop: [_assets/images/docintel_p1579_img02.png](_assets/images/docintel_p1579_img02.png)

* Approximate PDF coordinates: x0=72.0, y0=371.9, x1=504.0, y1=560.5

A close-up workspace screenshot showing an invoice line where `PO NUMBER` text is highlighted in the document. A purple arrow points from the document evidence to the corresponding field in the right Fields panel, where the value is selected or filled. This illustrates how a recommendation on the document image maps to a structured field in the side panel.

### Image 8: Document image panel toolbar

* Source page: 1580

* Source crop: [_assets/images/docintel_p1580_img01.png](_assets/images/docintel_p1580_img01.png)

* Approximate PDF coordinates: x0=72.0, y0=51.5, x1=504.0, y1=165.2

A Document Intelligence viewer screenshot showing the document thumbnail panel, a single-page invoice, and the top image toolbar. Visible toolbar controls include page navigation, zoom, fit, rotate, and related viewer icons. The figure identifies the document-image area and the controls used to move around and inspect the page.

### Image 9: Data extraction workspace with invoice table value highlighted

* Source page: 1580

* Source crop: [_assets/images/docintel_p1580_img02.png](_assets/images/docintel_p1580_img02.png)

* Approximate PDF coordinates: x0=72.0, y0=287.7, x1=504.0, y1=543.0

A workspace screenshot with the invoice in the document viewer, the Fields and Tables panel on the right, and a highlighted extracted value in the invoice line-item table. The visual demonstrates reviewing extracted table or field values while seeing their evidence in the source document.

### Image 10: Table field group review grid with options menu

* Source page: 1581

* Source crop: [_assets/images/docintel_p1581_img01.png](_assets/images/docintel_p1581_img01.png)

* Approximate PDF coordinates: x0=72.0, y0=39.0, x1=504.0, y1=259.8

A Document Intelligence workspace screenshot with a source invoice table at the top and a structured extraction grid at the bottom. A row in the grid is selected and an options menu is open on the right side of the grid. The menu includes actions for reviewing or changing extracted table values. The screenshot shows how table extraction results are presented and managed in the workspace.

### Image 11: Inline UI icon

* Source page: 1581

* Source crop: [_assets/images/docintel_p1581_img02.png](_assets/images/docintel_p1581_img02.png)

* Approximate PDF coordinates: x0=224.0, y0=638.1, x1=239.0, y1=650.9

Small inline UI icon embedded in the procedure, table, or screenshot callout on source page 1581. The icon is used as a visual locator for the adjacent instruction, such as a menu, edit, draw-tool, add-line, remove-line, reorder, status, or field-control icon. The crop is retained for traceability; approximate PDF coordinates are (224.0, 638.1, 239.0, 650.9).

### Image 12: Inline UI icon

* Source page: 1581

* Source crop: [_assets/images/docintel_p1581_img03.png](_assets/images/docintel_p1581_img03.png)

* Approximate PDF coordinates: x0=488.4, y0=659.9, x1=503.4, y1=674.9

Small inline UI icon embedded in the procedure, table, or screenshot callout on source page 1581. The icon is used as a visual locator for the adjacent instruction, such as a menu, edit, draw-tool, add-line, remove-line, reorder, status, or field-control icon. The crop is retained for traceability; approximate PDF coordinates are (488.4, 659.9, 503.4, 674.9).

### Image 13: Inline UI icon

* Source page: 1581

* Source crop: [_assets/images/docintel_p1581_img04.png](_assets/images/docintel_p1581_img04.png)

* Approximate PDF coordinates: x0=339.3, y0=696.4, x1=354.3, y1=711.4

Small inline UI icon embedded in the procedure, table, or screenshot callout on source page 1581. The icon is used as a visual locator for the adjacent instruction, such as a menu, edit, draw-tool, add-line, remove-line, reorder, status, or field-control icon. The crop is retained for traceability; approximate PDF coordinates are (339.3, 696.4, 354.3, 711.4).

### Image 14: Date normalization confirmation panel

* Source page: 1582

* Source crop: [_assets/images/docintel_p1582_img01.png](_assets/images/docintel_p1582_img01.png)

* Approximate PDF coordinates: x0=82.0, y0=109.0, x1=382.0, y1=311.5

A field panel example for `Date *`. The extracted value is `10/03/2022`; below it the converted value is shown as `2022-03-10` under the label `Converted to YYYY-MM-DD`. A yellow warning states `Make sure the converted date is correct`, and buttons `Edit` and `Confirm` appear under `Confirm the converted value`. The image illustrates ambiguous date normalization and the human confirmation control.

### Image 15: Inline UI icon

* Source page: 1583

* Source crop: [_assets/images/docintel_p1583_img01.png](_assets/images/docintel_p1583_img01.png)

* Approximate PDF coordinates: x0=456.5, y0=136.8, x1=471.5, y1=151.8

Small inline UI icon embedded in the procedure, table, or screenshot callout on source page 1583. The icon is used as a visual locator for the adjacent instruction, such as a menu, edit, draw-tool, add-line, remove-line, reorder, status, or field-control icon. The crop is retained for traceability; approximate PDF coordinates are (456.5, 136.8, 471.5, 151.8).

### Image 16: Inline UI icon

* Source page: 1584

* Source crop: [_assets/images/docintel_p1584_img01.png](_assets/images/docintel_p1584_img01.png)

* Approximate PDF coordinates: x0=490.8, y0=44.7, x1=505.8, y1=59.7

Small inline UI icon embedded in the procedure, table, or screenshot callout on source page 1584. The icon is used as a visual locator for the adjacent instruction, such as a menu, edit, draw-tool, add-line, remove-line, reorder, status, or field-control icon. The crop is retained for traceability; approximate PDF coordinates are (490.8, 44.7, 505.8, 59.7).

### Image 17: Inline UI icon

* Source page: 1584

* Source crop: [_assets/images/docintel_p1584_img02.png](_assets/images/docintel_p1584_img02.png)

* Approximate PDF coordinates: x0=339.3, y0=81.3, x1=354.3, y1=96.3

Small inline UI icon embedded in the procedure, table, or screenshot callout on source page 1584. The icon is used as a visual locator for the adjacent instruction, such as a menu, edit, draw-tool, add-line, remove-line, reorder, status, or field-control icon. The crop is retained for traceability; approximate PDF coordinates are (339.3, 81.3, 354.3, 96.3).

### Image 18: Date normalization confirmation panel repeated example

* Source page: 1584

* Source crop: [_assets/images/docintel_p1584_img03.png](_assets/images/docintel_p1584_img03.png)

* Approximate PDF coordinates: x0=82.0, y0=197.8, x1=382.0, y1=400.3

A second occurrence of the date-normalization panel. It again shows `Date *`, the extracted value `10/03/2022`, conversion to `2022-03-10`, the warning `Make sure the converted date is correct`, and the `Edit` and `Confirm` buttons. It reinforces that agents may need to verify converted values before completing a task.

### Image 19: Inline UI icon

* Source page: 1584

* Source crop: [_assets/images/docintel_p1584_img04.png](_assets/images/docintel_p1584_img04.png)

* Approximate PDF coordinates: x0=481.2, y0=547.1, x1=496.2, y1=562.1

Small inline UI icon embedded in the procedure, table, or screenshot callout on source page 1584. The icon is used as a visual locator for the adjacent instruction, such as a menu, edit, draw-tool, add-line, remove-line, reorder, status, or field-control icon. The crop is retained for traceability; approximate PDF coordinates are (481.2, 547.1, 496.2, 562.1).

### Image 20: Completed fields view in the extraction workspace

* Source page: 1585

* Source crop: [_assets/images/docintel_p1585_img01.png](_assets/images/docintel_p1585_img01.png)

* Approximate PDF coordinates: x0=72.0, y0=324.2, x1=504.0, y1=563.7

A Document Intelligence workspace screenshot showing an invoice in the central viewer and the right-side Fields panel with status tabs such as All, To complete, and Completed. The panel indicates a completed or near-completed state and the `Submit` button is visible. It supports the procedure for completing document extraction tasks after fields are reviewed.

### Image 21: Inline UI icon

* Source page: 1586

* Source crop: [_assets/images/docintel_p1586_img01.png](_assets/images/docintel_p1586_img01.png)

* Approximate PDF coordinates: x0=175.9, y0=103.8, x1=190.9, y1=118.1

Small inline UI icon embedded in the procedure, table, or screenshot callout on source page 1586. The icon is used as a visual locator for the adjacent instruction, such as a menu, edit, draw-tool, add-line, remove-line, reorder, status, or field-control icon. The crop is retained for traceability; approximate PDF coordinates are (175.9, 103.8, 190.9, 118.1).

### Image 22: Inline UI icon

* Source page: 1586

* Source crop: [_assets/images/docintel_p1586_img02.png](_assets/images/docintel_p1586_img02.png)

* Approximate PDF coordinates: x0=205.3, y0=167.1, x1=220.3, y1=181.4

Small inline UI icon embedded in the procedure, table, or screenshot callout on source page 1586. The icon is used as a visual locator for the adjacent instruction, such as a menu, edit, draw-tool, add-line, remove-line, reorder, status, or field-control icon. The crop is retained for traceability; approximate PDF coordinates are (205.3, 167.1, 220.3, 181.4).

### Image 23: Draw tool box for extracting a single field

* Source page: 1586

* Source crop: [_assets/images/docintel_p1586_img03.png](_assets/images/docintel_p1586_img03.png)

* Approximate PDF coordinates: x0=112.0, y0=260.9, x1=544.0, y1=414.4

A screenshot of a document image with a rectangular selection box around a date on an identification document. An arrow points from the selected text in the image to a date field in the right Fields panel. The visible field value is formatted like `04-01-2018`. The figure demonstrates using the draw tool to map a region of the document image to a single field value.

### Image 24: Inline UI icon

* Source page: 1586

* Source crop: [_assets/images/docintel_p1586_img04.png](_assets/images/docintel_p1586_img04.png)

* Approximate PDF coordinates: x0=309.6, y0=642.1, x1=324.6, y1=656.5

Small inline UI icon embedded in the procedure, table, or screenshot callout on source page 1586. The icon is used as a visual locator for the adjacent instruction, such as a menu, edit, draw-tool, add-line, remove-line, reorder, status, or field-control icon. The crop is retained for traceability; approximate PDF coordinates are (309.6, 642.1, 324.6, 656.5).

### Image 25: Inline UI icon

* Source page: 1587

* Source crop: [_assets/images/docintel_p1587_img01.png](_assets/images/docintel_p1587_img01.png)

* Approximate PDF coordinates: x0=329.6, y0=356.3, x1=344.6, y1=370.6

Small inline UI icon embedded in the procedure, table, or screenshot callout on source page 1587. The icon is used as a visual locator for the adjacent instruction, such as a menu, edit, draw-tool, add-line, remove-line, reorder, status, or field-control icon. The crop is retained for traceability; approximate PDF coordinates are (329.6, 356.3, 344.6, 370.6).

### Image 26: Inline UI icon

* Source page: 1587

* Source crop: [_assets/images/docintel_p1587_img02.png](_assets/images/docintel_p1587_img02.png)

* Approximate PDF coordinates: x0=417.5, y0=431.4, x1=431.0, y1=446.4

Small inline UI icon embedded in the procedure, table, or screenshot callout on source page 1587. The icon is used as a visual locator for the adjacent instruction, such as a menu, edit, draw-tool, add-line, remove-line, reorder, status, or field-control icon. The crop is retained for traceability; approximate PDF coordinates are (417.5, 431.4, 431.0, 446.4).

### Image 27: Inline UI icon

* Source page: 1587

* Source crop: [_assets/images/docintel_p1587_img03.png](_assets/images/docintel_p1587_img03.png)

* Approximate PDF coordinates: x0=205.3, y0=465.8, x1=220.3, y1=480.1

Small inline UI icon embedded in the procedure, table, or screenshot callout on source page 1587. The icon is used as a visual locator for the adjacent instruction, such as a menu, edit, draw-tool, add-line, remove-line, reorder, status, or field-control icon. The crop is retained for traceability; approximate PDF coordinates are (205.3, 465.8, 220.3, 480.1).

### Image 28: Draw tool grid over invoice table

* Source page: 1588

* Source crop: [_assets/images/docintel_p1588_img01.png](_assets/images/docintel_p1588_img01.png)

* Approximate PDF coordinates: x0=82.0, y0=39.0, x1=514.0, y1=297.3

A screenshot showing a pink draw-tool grid over an invoice line-item table. Column headers include Description, Quantity, Unit Price, and Total; the grid has row numbers, column boundaries, and resize handles. A button labeled `Extract data` appears at the top right. The figure shows how an agent defines a table extraction grid directly on the document image.

### Image 29: Inline UI icon

* Source page: 1588

* Source crop: [_assets/images/docintel_p1588_img02.png](_assets/images/docintel_p1588_img02.png)

* Approximate PDF coordinates: x0=215.3, y0=397.9, x1=230.3, y1=412.1

Small inline UI icon embedded in the procedure, table, or screenshot callout on source page 1588. The icon is used as a visual locator for the adjacent instruction, such as a menu, edit, draw-tool, add-line, remove-line, reorder, status, or field-control icon. The crop is retained for traceability; approximate PDF coordinates are (215.3, 397.9, 230.3, 412.1).

### Image 30: Inline UI icon

* Source page: 1588

* Source crop: [_assets/images/docintel_p1588_img03.png](_assets/images/docintel_p1588_img03.png)

* Approximate PDF coordinates: x0=397.3, y0=559.9, x1=412.3, y1=573.6

Small inline UI icon embedded in the procedure, table, or screenshot callout on source page 1588. The icon is used as a visual locator for the adjacent instruction, such as a menu, edit, draw-tool, add-line, remove-line, reorder, status, or field-control icon. The crop is retained for traceability; approximate PDF coordinates are (397.3, 559.9, 412.3, 573.6).

### Image 31: Annotated draw tool grid controls

* Source page: 1589

* Source crop: [_assets/images/docintel_p1589_img01.png](_assets/images/docintel_p1589_img01.png)

* Approximate PDF coordinates: x0=82.0, y0=416.1, x1=514.0, y1=725.6

An annotated screenshot of the draw tool grid with purple labels pointing to controls and regions: `Move grid`, `Table name and grid number`, `Add a line`, `Column header`, `Number of changed cells`, `Row header`, `Ignore a column`, `Changed cells`, and `Remove a line`. A small invoice table appears below as the source evidence. The figure explains every major grid control used to adjust table extraction boundaries and columns.

### Image 32: Inline UI icon

* Source page: 1590

* Source crop: [_assets/images/docintel_p1590_img01.png](_assets/images/docintel_p1590_img01.png)

* Approximate PDF coordinates: x0=402.5, y0=179.1, x1=417.5, y1=192.2

Small inline UI icon embedded in the procedure, table, or screenshot callout on source page 1590. The icon is used as a visual locator for the adjacent instruction, such as a menu, edit, draw-tool, add-line, remove-line, reorder, status, or field-control icon. The crop is retained for traceability; approximate PDF coordinates are (402.5, 179.1, 417.5, 192.2).

### Image 33: Inline UI icon

* Source page: 1590

* Source crop: [_assets/images/docintel_p1590_img02.png](_assets/images/docintel_p1590_img02.png)

* Approximate PDF coordinates: x0=418.5, y0=383.4, x1=433.5, y1=397.8

Small inline UI icon embedded in the procedure, table, or screenshot callout on source page 1590. The icon is used as a visual locator for the adjacent instruction, such as a menu, edit, draw-tool, add-line, remove-line, reorder, status, or field-control icon. The crop is retained for traceability; approximate PDF coordinates are (418.5, 383.4, 433.5, 397.8).

### Image 34: Inline UI icon

* Source page: 1590

* Source crop: [_assets/images/docintel_p1590_img03.png](_assets/images/docintel_p1590_img03.png)

* Approximate PDF coordinates: x0=450.2, y0=458.1, x1=465.2, y1=473.1

Small inline UI icon embedded in the procedure, table, or screenshot callout on source page 1590. The icon is used as a visual locator for the adjacent instruction, such as a menu, edit, draw-tool, add-line, remove-line, reorder, status, or field-control icon. The crop is retained for traceability; approximate PDF coordinates are (450.2, 458.1, 465.2, 473.1).

### Image 35: Inline UI icon

* Source page: 1590

* Source crop: [_assets/images/docintel_p1590_img04.png](_assets/images/docintel_p1590_img04.png)

* Approximate PDF coordinates: x0=460.8, y0=545.8, x1=475.8, y1=560.2

Small inline UI icon embedded in the procedure, table, or screenshot callout on source page 1590. The icon is used as a visual locator for the adjacent instruction, such as a menu, edit, draw-tool, add-line, remove-line, reorder, status, or field-control icon. The crop is retained for traceability; approximate PDF coordinates are (460.8, 545.8, 475.8, 560.2).

### Image 36: Text box selection for invoice number

* Source page: 1591

* Source crop: [_assets/images/docintel_p1591_img01.png](_assets/images/docintel_p1591_img01.png)

* Approximate PDF coordinates: x0=82.0, y0=207.8, x1=349.0, y1=305.3

A close-up of document text showing `Date: 10/03/2022` and `Invoice number: 1035`. A purple label bubble reads `Invoice #` and points to the selected value `1035`. The image demonstrates selecting a detected text box and assigning it to a field.

### Image 37: Table cell selection with hover label

* Source page: 1591

* Source crop: [_assets/images/docintel_p1591_img02.png](_assets/images/docintel_p1591_img02.png)

* Approximate PDF coordinates: x0=82.0, y0=341.1, x1=514.0, y1=470.4

A close-up of the draw-tool grid in a table. The cell containing `Server Equipment` is highlighted with a border and a dark tooltip also reads `Server Equipment`. Adjacent columns include Description and Quantity. The image shows how a user selects or edits a specific table cell extracted from a document.

### Image 38: Edit recommendation dropdown in table extraction

* Source page: 1592

* Source crop: [_assets/images/docintel_p1592_img01.png](_assets/images/docintel_p1592_img01.png)

* Approximate PDF coordinates: x0=82.0, y0=164.8, x1=514.0, y1=449.4

A Document Intelligence workspace screenshot with an invoice table under a pink extraction grid. A cell is selected and a dropdown of text recommendations is open, showing alternative detected values. The bottom panel shows the corresponding field/table row with a highlighted value. The figure demonstrates editing a recommendation directly on the document image and synchronizing it to structured table fields.

### Image 39: Document Intelligence workspace layout for classification

* Source page: 1593

* Source crop: [_assets/images/docintel_p1593_img01.png](_assets/images/docintel_p1593_img01.png)

* Approximate PDF coordinates: x0=72.0, y0=287.6, x1=504.0, y1=413.7

An annotated workspace screenshot for classification with numbered callouts. The left thumbnail panel is marked `1`, the document/image panel is marked `2`, the top toolbar is marked `3`, and the Classify panel on the right is marked `4`. The screenshot explains the key workspace regions used when classifying documents and pages.

### Image 40: Classify panel with category fields

* Source page: 1594

* Source crop: [_assets/images/docintel_p1594_img01.png](_assets/images/docintel_p1594_img01.png)

* Approximate PDF coordinates: x0=72.0, y0=39.0, x1=504.0, y1=191.2

A workspace screenshot with a document displayed in the center and the `Classify` panel on the right. The panel includes a Category field and category options such as Mixed categories, Blank Page, and No category found. The image demonstrates reviewing and assigning document/page categories during classification tasks.

### Image 41: Options icon for flagging follow-up

* Source page: 1595

* Source crop: [_assets/images/docintel_p1595_img01.png](_assets/images/docintel_p1595_img01.png)

* Approximate PDF coordinates: x0=333.0, y0=69.7, x1=348.0, y1=84.7

Small options icon referenced by the instruction to select `Flag for follow-up` from the options menu while classifying documents or pages. Approximate source coordinates: (333.0, 69.7, 348.0, 84.7).

---
## TABLES
### Table 1: Document task form

* Source page: 1575

* Extracted dimensions: 3 rows x 2 columns

| Field | Description |
| --- | --- |
| Display Name | The name associated with this use case. For<br>example, PO-1. |
| Use Case | The use case created for this document type. |

### Table 2: Draw tool box adjustment options

* Source page: 1586

* Extracted dimensions: 4 rows x 2 columns

| Option | Description |
| --- | --- |
| Resize the box | (Optional) Select the box. Drag the box edge<br>or corner to the desired position.<br>The updated text in the box is extracted and<br>fills the related field in the document fields<br>panel. |
| Remove the box | (Optional) Select the Remove the box icon<br>( ).<br>The box is deleted and the extracted value is<br>removed from the field. |
| Extract to a different field | (Optional) Select the field name next to the<br>box and choose another option from the list. |

### Table 3: Draw tool grid adjustment options

* Source page: 1590

* Extracted dimensions: 9 rows x 2 columns

| Option | Description |
| --- | --- |
| Move the grid | Drag the Move icon ( ) to the desired posi<br>tion. |
| Change a column header | Select the column header and select the col<br>umn where the data will be extracted to in the<br>table fields. |
| Make the first row a header row | Select the row header and check the This is a<br>header row check box. |
| Move a column or row border | Drag the border to the desired position. |
| Add a new column or row | Go to the outside border of the grid and se<br>lect the Add a line icon ( ).<br>Adding a line splits the affected cells so they<br>can be extracted to separate fields. |
| Remove a column or row border | Select the Remove a line icon ( ) at the end<br>of the border outside the grid.<br>Removing a line merges the affected cells so<br>they can be extracted to the same fields. |
| Remove the grid | Select the Remove the grid icon ( ).<br>This action only removes the grid, not the ex<br>tracted data. |
| Ignore a table column or row | a. Select the column or row heading.<br>b. Select the Do not extract this column/row<br>check box.<br>c. Select Save. |

---
## FIGURES
### Figure 1: Important deprecation callout in Use subsection

* Source page: 1574

* Source crop: [_assets/figures/docintel_p1574_figure_manual_07.png](_assets/figures/docintel_p1574_figure_manual_07.png)

A blue `Important` callout in the `Using Document Intelligence` introduction repeats the Document Intelligence future deprecation notice and references `KB0867184`, establishing that readers should consider Now Assist in Document Intelligence for current/future extraction scenarios.

### Figure 2: Document task attachment upload and Process Task button

* Source page: 1576

* Source crop: [_assets/images/docintel_p1576_img01.png](_assets/images/docintel_p1576_img01.png)

A ServiceNow document task form is dimmed behind an `Attachments` dialog. The dialog shows an upload/paperclip graphic and an uploaded attachment area. A purple arrow points toward the `Process Task` button on the form. The image demonstrates that a user attaches a document and then starts processing by selecting `Process Task`.

### Figure 3: Document tasks list

* Source page: 1577

* Source crop: [_assets/images/docintel_p1577_img01.png](_assets/images/docintel_p1577_img01.png)

A ServiceNow list of document tasks. The list contains multiple rows with columns such as display name, state, processed status, use case, and related dates. The screenshot shows how to locate a processed document task after processing completes.

### Figure 4: Document task form with Show in DocIntel button

* Source page: 1577

* Source crop: [_assets/images/docintel_p1577_img02.png](_assets/images/docintel_p1577_img02.png)

A ServiceNow document task form with the `Show in DocIntel` button highlighted. The form contains fields such as display name, use case, target table, working message, and error message. The screenshot shows the action used to open the Document Intelligence workspace for the selected task.

### Figure 5: Document Intelligence workspace layout for data extraction

* Source page: 1578

* Source crop: [_assets/images/docintel_p1578_img01.png](_assets/images/docintel_p1578_img01.png)

An annotated Document Intelligence workspace screenshot for an invoice task. Numbered callouts identify major regions: `1` the thumbnail panel on the left; `2` the central document image panel with highlighted extracted text; `3` the top toolbar with page navigation and viewer controls; `4` the Fields panel on the right; and `5` the bottom table/field-group grid used for extracted line items. A `Submit` button appears near the top-right. The figure explains the workspace zones agents use to review extracted fields and tables.

### Figure 6: Workspace field review notification and invoice viewer

* Source page: 1579

* Source crop: [_assets/images/docintel_p1579_img01.png](_assets/images/docintel_p1579_img01.png)

A Document Intelligence workspace screenshot with an invoice document displayed in the central viewer and a fields panel on the right. A notification reads that the user should review this field and other fields before submitting the task. The right panel includes field status counts and a `Submit` button. The image demonstrates that fields may require human review before final submission.

### Figure 7: PO number field recommendation mapped from invoice text

* Source page: 1579

* Source crop: [_assets/images/docintel_p1579_img02.png](_assets/images/docintel_p1579_img02.png)

A close-up workspace screenshot showing an invoice line where `PO NUMBER` text is highlighted in the document. A purple arrow points from the document evidence to the corresponding field in the right Fields panel, where the value is selected or filled. This illustrates how a recommendation on the document image maps to a structured field in the side panel.

### Figure 8: Document image panel toolbar

* Source page: 1580

* Source crop: [_assets/images/docintel_p1580_img01.png](_assets/images/docintel_p1580_img01.png)

A Document Intelligence viewer screenshot showing the document thumbnail panel, a single-page invoice, and the top image toolbar. Visible toolbar controls include page navigation, zoom, fit, rotate, and related viewer icons. The figure identifies the document-image area and the controls used to move around and inspect the page.

### Figure 9: Data extraction workspace with invoice table value highlighted

* Source page: 1580

* Source crop: [_assets/images/docintel_p1580_img02.png](_assets/images/docintel_p1580_img02.png)

A workspace screenshot with the invoice in the document viewer, the Fields and Tables panel on the right, and a highlighted extracted value in the invoice line-item table. The visual demonstrates reviewing extracted table or field values while seeing their evidence in the source document.

### Figure 10: Table field group review grid with options menu

* Source page: 1581

* Source crop: [_assets/images/docintel_p1581_img01.png](_assets/images/docintel_p1581_img01.png)

A Document Intelligence workspace screenshot with a source invoice table at the top and a structured extraction grid at the bottom. A row in the grid is selected and an options menu is open on the right side of the grid. The menu includes actions for reviewing or changing extracted table values. The screenshot shows how table extraction results are presented and managed in the workspace.

### Figure 11: Date normalization confirmation panel

* Source page: 1582

* Source crop: [_assets/images/docintel_p1582_img01.png](_assets/images/docintel_p1582_img01.png)

A field panel example for `Date *`. The extracted value is `10/03/2022`; below it the converted value is shown as `2022-03-10` under the label `Converted to YYYY-MM-DD`. A yellow warning states `Make sure the converted date is correct`, and buttons `Edit` and `Confirm` appear under `Confirm the converted value`. The image illustrates ambiguous date normalization and the human confirmation control.

### Figure 12: Date normalization confirmation panel repeated example

* Source page: 1584

* Source crop: [_assets/images/docintel_p1584_img03.png](_assets/images/docintel_p1584_img03.png)

A second occurrence of the date-normalization panel. It again shows `Date *`, the extracted value `10/03/2022`, conversion to `2022-03-10`, the warning `Make sure the converted date is correct`, and the `Edit` and `Confirm` buttons. It reinforces that agents may need to verify converted values before completing a task.

### Figure 13: Completed fields view in the extraction workspace

* Source page: 1585

* Source crop: [_assets/images/docintel_p1585_img01.png](_assets/images/docintel_p1585_img01.png)

A Document Intelligence workspace screenshot showing an invoice in the central viewer and the right-side Fields panel with status tabs such as All, To complete, and Completed. The panel indicates a completed or near-completed state and the `Submit` button is visible. It supports the procedure for completing document extraction tasks after fields are reviewed.

### Figure 14: Draw tool box for extracting a single field

* Source page: 1586

* Source crop: [_assets/images/docintel_p1586_img03.png](_assets/images/docintel_p1586_img03.png)

A screenshot of a document image with a rectangular selection box around a date on an identification document. An arrow points from the selected text in the image to a date field in the right Fields panel. The visible field value is formatted like `04-01-2018`. The figure demonstrates using the draw tool to map a region of the document image to a single field value.

### Figure 15: Draw tool grid over invoice table

* Source page: 1588

* Source crop: [_assets/images/docintel_p1588_img01.png](_assets/images/docintel_p1588_img01.png)

A screenshot showing a pink draw-tool grid over an invoice line-item table. Column headers include Description, Quantity, Unit Price, and Total; the grid has row numbers, column boundaries, and resize handles. A button labeled `Extract data` appears at the top right. The figure shows how an agent defines a table extraction grid directly on the document image.

### Figure 16: Annotated draw tool grid controls

* Source page: 1589

* Source crop: [_assets/images/docintel_p1589_img01.png](_assets/images/docintel_p1589_img01.png)

An annotated screenshot of the draw tool grid with purple labels pointing to controls and regions: `Move grid`, `Table name and grid number`, `Add a line`, `Column header`, `Number of changed cells`, `Row header`, `Ignore a column`, `Changed cells`, and `Remove a line`. A small invoice table appears below as the source evidence. The figure explains every major grid control used to adjust table extraction boundaries and columns.

### Figure 17: Text box selection for invoice number

* Source page: 1591

* Source crop: [_assets/images/docintel_p1591_img01.png](_assets/images/docintel_p1591_img01.png)

A close-up of document text showing `Date: 10/03/2022` and `Invoice number: 1035`. A purple label bubble reads `Invoice #` and points to the selected value `1035`. The image demonstrates selecting a detected text box and assigning it to a field.

### Figure 18: Table cell selection with hover label

* Source page: 1591

* Source crop: [_assets/images/docintel_p1591_img02.png](_assets/images/docintel_p1591_img02.png)

A close-up of the draw-tool grid in a table. The cell containing `Server Equipment` is highlighted with a border and a dark tooltip also reads `Server Equipment`. Adjacent columns include Description and Quantity. The image shows how a user selects or edits a specific table cell extracted from a document.

### Figure 19: Edit recommendation dropdown in table extraction

* Source page: 1592

* Source crop: [_assets/images/docintel_p1592_img01.png](_assets/images/docintel_p1592_img01.png)

A Document Intelligence workspace screenshot with an invoice table under a pink extraction grid. A cell is selected and a dropdown of text recommendations is open, showing alternative detected values. The bottom panel shows the corresponding field/table row with a highlighted value. The figure demonstrates editing a recommendation directly on the document image and synchronizing it to structured table fields.

### Figure 20: Document Intelligence workspace layout for classification

* Source page: 1593

* Source crop: [_assets/images/docintel_p1593_img01.png](_assets/images/docintel_p1593_img01.png)

An annotated workspace screenshot for classification with numbered callouts. The left thumbnail panel is marked `1`, the document/image panel is marked `2`, the top toolbar is marked `3`, and the Classify panel on the right is marked `4`. The screenshot explains the key workspace regions used when classifying documents and pages.

### Figure 21: Classify panel with category fields

* Source page: 1594

* Source crop: [_assets/images/docintel_p1594_img01.png](_assets/images/docintel_p1594_img01.png)

A workspace screenshot with a document displayed in the center and the `Classify` panel on the right. The panel includes a Category field and category options such as Mixed categories, Blank Page, and No category found. The image demonstrates reviewing and assigning document/page categories during classification tasks.

---
## QUALITY ASSURANCE NOTES
* PAGES REVIEWED: 1574-1595
* IMAGES REVIEWED: 41 non-header image entries; 21 major screenshot/diagram/callout/figure entries. Repeated ServiceNow header logos and footers are documented as page furniture.
* TABLES REVIEWED: 3 table entries assigned to this subsection and converted into Markdown tables in the `TABLES` section.
* FIGURES REVIEWED: 21 major figures/diagrams/screenshots/callouts with detailed component-level descriptions.
* OCR ISSUES FOUND: The PDF contains a selectable text layer, but extraction artifacts were present, including soft-hyphen characters, split link punctuation, ligature-like errors such as `difefrent`/`efefctive`/`fei ld`, and table-extraction spacing issues in bracketed role and table identifiers.
* OCR ISSUES CORRECTED: Soft hyphen and zero-width characters were normalized; repeated footer/page furniture was removed from main content and accounted for in QA; common text-layer artifacts were corrected; tables were separately extracted and converted to Markdown with cleaned cells.
* RECHECK PASSES COMPLETED: 12/12: page completeness, text extraction, table extraction, image extraction/documentation, diagram interpretation, section mapping, subsection mapping, file names, folder names, Markdown formatting, missed-content review, and OCR/text-layer cleanup review.
* SECTION/SUBSECTION MAPPING NOTE: Page 1574 starts at the exact source heading `Using Document Intelligence`.
* SECTION/SUBSECTION MAPPING NOTE: Page 1595 is shared with `Monitor`; classification procedure continuation before `Monitoring Document Intelligence performance` remains in `Use`.
* FOOTER/PAGE FURNITURE NOTE: The repeated ServiceNow logo, copyright notice, trademark notice, and page number appear on each source page; they are accounted for globally and removed from repeated content extraction to avoid duplicated page furniture.
