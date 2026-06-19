# Monitor
## SOURCE INFORMATION
* SECTION NAME: Document Intelligence
* SUBSECTION NAME: Monitor
* SOURCE FILE NAME: Document Intelligence.pdf
* PAGE RANGE: 1595-1600 (page 1600 split before `Document Intelligence references`)
* EXTRACTION DATE: 2026-06-17

---
# CONTENT
> Source page: 1595

Monitoring Document Intelligence performance
Track document extraction performance in Document Intelligence to understand its usage and
effectiveness.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
View reports on the Document Intelligence Admin home page
Monitor document extraction performance in the Admin experience.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Before you begin
• Ensure that the Document Intelligence application (sn_docintel) and Document Intelligence
Admin (com.snc.docintel_admin) ServiceNow®  Store application is installed and active. For
more information, see Install Document Intelligence.
• Have an active use case with multiple completed document tasks. For more information, see
Set up document extraction use cases.
• Role required: sn_docintel.admin, sn_docintel.manager, or admin.
About this task
You can review the value of your Document Intelligence (DocIntel) implementation when you
open the Document Intelligence Admin experience home page.
The Monitor DocIntel performance over time section displays the following measurements:
• The Accuracy of Extraction widget shows the average extraction accuracy per time period
for the selected use case. Accuracy is defined as the number of times that the AI's top
recommendation is the correct answer.
• The Agent effort widget shows the number of keystrokes that your agents need to perform
in order to extract all field values for a document task. This measurement is an average per
document task.
> Source page: 1596

Procedure
1. Navigate to All > Document Intelligence > Document Data Extraction Administration > Home.
2. Expand the Use Case list and select your use case.
3. Expand the Time Period list and select a date range.
4. Review the results displayed in the Accuracy of Extraction and the Agent effort widgets.
Document Intelligence monitoring dashboard
Monitor the overall performance of Document Intelligence over time in the Document
Intelligence monitoring dashboard.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Overview of the Document Intelligence monitoring dashboard
The Document Intelligence monitoring dashboard provides a high-level overview of your
Document Intelligence usage and value.
> Source page: 1597

The data visualizations show document extraction activity in your instance. For example:
• Active use cases
• Active document tasks
• Processed pages
• Processed document tasks
• Accuracy of the DocIntel recommendations
This dashboard provides useful answers to the following questions:
• How many documents are processed using DocIntel?
• How much of the document extraction is automated?
• How has DocIntel accuracy progressed over time?
View the Document Intelligence monitoring dashboard
Access the Document Intelligence monitoring dashboard on the Monitoring screen of the Admin
experience.
Before you begin
• Ensure that the Document Intelligence application (sn_docintel) and Document Intelligence
Admin (com.snc.docintel_admin) ServiceNow®  Store application is installed and active. For
more information, see Install Document Intelligence.
• Have an active use case with multiple completed document tasks. For more information, see
Set up document extraction use cases.
• Role required: sn_docintel.admin, sn_docintel.manager, or admin.
> Source page: 1598

Procedure
1. Navigate to All > Document Intelligence > Document Data Extraction Administration >
Monitoring.
2. Optional:  Select a date range in the Date range filter to show only the data within the selected
dates.
3. Optional:  Select one or more use cases in the Use cases filter to show only the data that
applies to the selected use cases.
4. Optional:  Select an object within a chart to see additional details.
Data visualizations in the Document Intelligence monitoring dashboard
The Document Intelligence monitoring dashboard uses data visualizations to display your
Document Intelligence (DocIntel) usage and performance data.
The following table describes the data visualizations shown on the Monitoring screen.
Data visualizations showing Document Intelligence usage and performance
Name
Description
Use cases by mode
The number of document extraction use cases
in this instance, grouped by extraction mode.
Pages processed
The number of pages processed for data
extraction using DocIntel in this instance over
the selected date range.
Document tasks processed
The number of DocIntel document tasks
processed in this instance over the selected
date range.
Document tasks by status
The number of DocIntel document tasks in this
instance, grouped by status.
Average accuracy per use case
The percentage of times that the top
recommendation from DocIntel is the correct
field value, based on the tasks completed for a
use case.
Document tasks per use case
The number of DocIntel document tasks for
each use case, grouped by status.
Use case performance dashboard
Monitor Document Intelligence (DocIntel) performance at the use case and field levels in the use
case performance dashboard.
Important:  Starting with the Zurich release, Document Intelligence is being prepared
for future deprecation. It will be hidden and no longer activated on new instances but will
continue to be supported. For details, see the Deprecation Process article [KB0867184
]
in the Now Support Knowledge Base. Instead, you can extract information from documents
using the Now Assist in Document Intelligence application. For more information, see Now
Assist in Document Intelligence.
Overview of the use case performance dashboard
The use case performance dashboard provides quality metrics for the use case.
> Source page: 1599

The data visualizations show document extraction activity for the use case. For example:
• Agent effort to process document tasks
• Accuracy of the DocIntel recommendations
This dashboard provides useful answers to the following questions:
• How much effort is needed to complete document tasks for this use case?
• How has DocIntel accuracy progressed for this use case?
View the use case performance dashboard
Access the use case performance dashboard in the Performance tab on the use case screen.
Before you begin
• Ensure that the Document Intelligence application (sn_docintel) and Document Intelligence
Admin (com.snc.docintel_admin) ServiceNow®  Store application is installed and active. For
more information, see Install Document Intelligence.
• Have an active use case with multiple completed document tasks. For more information, see
Set up document extraction use cases.
• Role required: sn_docintel.admin, sn_docintel.manager, or admin.
Procedure
1. Navigate to All > Document Intelligence > Document Data Extraction Administration > Use
Cases.
2. Select the Performance tab.
3. Optional:  Select a date range in the Date range filter to show only the data within the selected
dates.
4. Optional:  Select one or more fields in the Fields filter to show only the data that applies to the
selected fields.
> Source page: 1600

5. Optional:  Select one or more field types in the Field type filter to show only the data that
applies to the selected field types.
6. Optional:  Select an object within a data visualization to see additional details.
Data visualizations in the use case performance dashboard
The use case performance dashboard provides data visualizations to display your usage and
performance data for the use case.
The following table describes the data visualizations shown on the Performance tab.
Data visualizations showing Document Intelligence use case activity
Name
Description
Accuracy of extraction
The average extraction accuracy per time
period for the use case. Accuracy is defined
as the number of times that the AI's top
recommendation is the correct answer.
Agent effort
The number of keystrokes your agents need
to press in order to extract all field values for
a document task. This measurement is an
average per document task.
Rank of recommendations selected
The number of times that DocIntel
recommendations from were selected by an
agent when completing a document task,
grouped by the order presented.
Field level accuracy
The percentage of times that the top
recommendation from DocIntel is the correct
value for a field.
Average key strokes per field
The average number of keystrokes an agent
performs to extract a value for a field.
Field level accuracy over time
The percentage of times over the selected
date range that the top recommendation from
DocIntel is the correct value for a field.

---
## IMAGE DESCRIPTIONS
Repeated page furniture: each source page includes the ServiceNow logo in the upper-left header and a standard copyright/page-number footer. These repeated layout elements are accounted for globally and not cropped as separate images for every page.

### Image 1: Important deprecation callout in Monitor subsection

* Source page: 1595

* Source crop: [_assets/figures/docintel_p1595_figure_manual_08.png](_assets/figures/docintel_p1595_figure_manual_08.png)

* Approximate PDF coordinates: x0=72.0, y0=157.0, x1=523.0, y1=244.0

A blue `Important` callout in the monitoring section repeats the Zurich deprecation preparation notice for Document Intelligence and redirects readers to Now Assist in Document Intelligence.

### Image 2: Document Intelligence Admin home dashboard

* Source page: 1596

* Source crop: [_assets/images/docintel_p1596_img01.png](_assets/images/docintel_p1596_img01.png)

* Approximate PDF coordinates: x0=72.0, y0=39.0, x1=504.0, y1=335.6

A dashboard screenshot titled `Document Intelligence (DocIntel)` with the subtitle `Help your agents process documents faster with artificial intelligence (AI)`. It includes filters for `Use Case` and `Time Period`, and two prominent widgets: `Accuracy of Extraction (%)` with value `72` and `Agent effort (Avg. KPET)` with value `14`. The image shows the high-level Admin home view for monitoring extraction performance.

### Image 3: Document Intelligence monitoring dashboard

* Source page: 1597

* Source crop: [_assets/images/docintel_p1597_img01.png](_assets/images/docintel_p1597_img01.png)

* Approximate PDF coordinates: x0=72.0, y0=39.0, x1=504.0, y1=346.1

A full monitoring dashboard screenshot with filters at the top and several visualization widgets. Visible widgets include an active use cases donut chart, active document tasks metric card, documents processed metric card, document tasks by state donut, processed pages over time line chart, and processed document tasks by use case bar chart. The dashboard visualizes overall instance activity and automation value over time.

### Image 4: Use case performance dashboard

* Source page: 1599

* Source crop: [_assets/images/docintel_p1599_img01.png](_assets/images/docintel_p1599_img01.png)

* Approximate PDF coordinates: x0=72.0, y0=39.0, x1=504.0, y1=326.2

A ServiceNow use case page with the `Performance` tab selected. It includes charts for `Accuracy of Extraction` and `Agent effort`, plus lower widgets such as rank of recommendations selected, field level accuracy, average key strokes per field, and field level accuracy over time. Filters and small action icons appear above the charts. The image shows use-case-specific performance monitoring rather than overall instance monitoring.

---
## TABLES
### Table 1: Data visualizations in the monitoring dashboard

* Source page: 1598

* Extracted dimensions: 7 rows x 2 columns

| Name | Description |
| --- | --- |
| Use cases by mode | The number of document extraction use cases<br>in this instance, grouped by extraction mode. |
| Pages processed | The number of pages processed for data<br>extraction using DocIntel in this instance over<br>the selected date range. |
| Document tasks processed | The number of DocIntel document tasks<br>processed in this instance over the selected<br>date range. |
| Document tasks by status | The number of DocIntel document tasks in this<br>instance, grouped by status. |
| Average accuracy per use case | The percentage of times that the top<br>recommendation from DocIntel is the correct<br>field value, based on the tasks completed for a<br>use case. |
| Document tasks per use case | The number of DocIntel document tasks for<br>each use case, grouped by status. |

### Table 2: Data visualizations showing Document Intelligence use case activity

* Source page: 1600

* Extracted dimensions: 7 rows x 2 columns

| Name | Description |
| --- | --- |
| Accuracy of extraction | The average extraction accuracy per time<br>period for the use case. Accuracy is defined<br>as the number of times that the AI's top<br>recommendation is the correct answer. |
| Agent efof rt | The number of keystrokes your agents need<br>to press in order to extract all field values for<br>a document task. This measurement is an<br>average per document task. |
| Rank of recommendations selected | The number of times that DocIntel<br>recommendations from were selected by an<br>agent when completing a document task,<br>grouped by the order presented. |
| Field level accuracy | The percentage of times that the top<br>recommendation from DocIntel is the correct<br>value for a field. |
| Average key strokes per field | The average number of keystrokes an agent<br>performs to extract a value for a field. |
| Field level accuracy over time | The percentage of times over the selected<br>date range that the top recommendation from<br>DocIntel is the correct value for a field. |

---
## FIGURES
### Figure 1: Important deprecation callout in Monitor subsection

* Source page: 1595

* Source crop: [_assets/figures/docintel_p1595_figure_manual_08.png](_assets/figures/docintel_p1595_figure_manual_08.png)

A blue `Important` callout in the monitoring section repeats the Zurich deprecation preparation notice for Document Intelligence and redirects readers to Now Assist in Document Intelligence.

### Figure 2: Document Intelligence Admin home dashboard

* Source page: 1596

* Source crop: [_assets/images/docintel_p1596_img01.png](_assets/images/docintel_p1596_img01.png)

A dashboard screenshot titled `Document Intelligence (DocIntel)` with the subtitle `Help your agents process documents faster with artificial intelligence (AI)`. It includes filters for `Use Case` and `Time Period`, and two prominent widgets: `Accuracy of Extraction (%)` with value `72` and `Agent effort (Avg. KPET)` with value `14`. The image shows the high-level Admin home view for monitoring extraction performance.

### Figure 3: Document Intelligence monitoring dashboard

* Source page: 1597

* Source crop: [_assets/images/docintel_p1597_img01.png](_assets/images/docintel_p1597_img01.png)

A full monitoring dashboard screenshot with filters at the top and several visualization widgets. Visible widgets include an active use cases donut chart, active document tasks metric card, documents processed metric card, document tasks by state donut, processed pages over time line chart, and processed document tasks by use case bar chart. The dashboard visualizes overall instance activity and automation value over time.

### Figure 4: Use case performance dashboard

* Source page: 1599

* Source crop: [_assets/images/docintel_p1599_img01.png](_assets/images/docintel_p1599_img01.png)

A ServiceNow use case page with the `Performance` tab selected. It includes charts for `Accuracy of Extraction` and `Agent effort`, plus lower widgets such as rank of recommendations selected, field level accuracy, average key strokes per field, and field level accuracy over time. Filters and small action icons appear above the charts. The image shows use-case-specific performance monitoring rather than overall instance monitoring.

---
## QUALITY ASSURANCE NOTES
* PAGES REVIEWED: 1595-1600
* IMAGES REVIEWED: 4 non-header image entries; 4 major screenshot/diagram/callout/figure entries. Repeated ServiceNow header logos and footers are documented as page furniture.
* TABLES REVIEWED: 2 table entries assigned to this subsection and converted into Markdown tables in the `TABLES` section.
* FIGURES REVIEWED: 4 major figures/diagrams/screenshots/callouts with detailed component-level descriptions.
* OCR ISSUES FOUND: The PDF contains a selectable text layer, but extraction artifacts were present, including soft-hyphen characters, split link punctuation, ligature-like errors such as `difefrent`/`efefctive`/`fei ld`, and table-extraction spacing issues in bracketed role and table identifiers.
* OCR ISSUES CORRECTED: Soft hyphen and zero-width characters were normalized; repeated footer/page furniture was removed from main content and accounted for in QA; common text-layer artifacts were corrected; tables were separately extracted and converted to Markdown with cleaned cells.
* RECHECK PASSES COMPLETED: 12/12: page completeness, text extraction, table extraction, image extraction/documentation, diagram interpretation, section mapping, subsection mapping, file names, folder names, Markdown formatting, missed-content review, and OCR/text-layer cleanup review.
* SECTION/SUBSECTION MAPPING NOTE: Page 1595 starts at the exact source heading `Monitoring Document Intelligence performance`.
* SECTION/SUBSECTION MAPPING NOTE: Page 1600 is shared with `Reference`; use-case performance dashboard continuation before `Document Intelligence references` remains in `Monitor`.
* FOOTER/PAGE FURNITURE NOTE: The repeated ServiceNow logo, copyright notice, trademark notice, and page number appear on each source page; they are accounted for globally and removed from repeated content extraction to avoid duplicated page furniture.
