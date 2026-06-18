# Testing and monitoring predictions

## SOURCE INFORMATION

* SECTION NAME: Predictive Intelligence
* SUBSECTION NAME: Testing and monitoring predictions
* SOURCE FILE NAME: Predictive Intelligence.pdf
* PAGE RANGE: 1487-1496 (shared boundary pages split at source headings)
* EXTRACTION DATE: 2026-06-17

---

# CONTENT

> Source page: 1487

### Testing and monitoring predictions

Evaluate the coverage and precision of your machine-learning (ML) solutions by testing them.
Once deployed, track their performance over time. Improve predictions by using performance
information to refine your solutions.

#### Testing solutions

After your ML solutions are trained, you can call on the Predictive Intelligence API to make a
solution prediction. Use the API to test the following solutions:
• Test a classification solution prediction
• Test a similarity solution prediction

#### Monitoring predictions

For classification predictions, use the Prediction Results dashboard to track the coverage and
precision of predictions over time.
To learn how, see Track classification prediction results over time.

#### Prediction troubleshooting

For troubleshooting common issues with solution predictions, see the Predictive Intelligence
Common issues [KB781893]
article in the Now Support Knowledge Base.

#### Test a classification solution prediction

Once your machine-learning (ML) solutions are trained, you can call on the Predictive
Intelligence API to make a solution prediction. In this example procedure, we use the REST API
Explorer to test a classification solution prediction for incident categorization.

#### Before you begin

Train your ML solution prior to testing a prediction.
Role required: web_service_admin, rest_api_explorer, or admin or ml_admin

#### About this task

This procedure uses sample data to illustrate what you can do in your instance, and may not
represent data or records that are actually in your instance.
This scenario illustrates a classification solution prediction for a hypothetical ML solution that
you have previously created and trained. You can also use the REST API Explorer to test a
similarity solution prediction.

> Source page: 1488

#### Procedure

1. Navigate to All > Predictive Intelligence > Classification > Solution Definitions.
2. Locate the ML solution definition whose prediction you want to test, and copy its Name value
to your clipboard or a Notepad file.
In this case, use the Name field value in your ML Solution Definition Incident Categorization
record, as illustrated in the following example.
3. Write down and save the Input Fields used in your ML Solution Definition record that you want
the REST API Explorer to use in its call to the Predictive Intelligence API.
In this case, we use the short _description field, as the prediction model has been trained to
use this field to learn its category definition.
4. Navigate to System Web Services > REST > REST API Explorer.
5. Set these choice fields as follows.

#### Field

#### Value

#### Namespace

now (leave as default)

#### API Name

Predictive Intelligence

#### API Version

latest (leave as default)
The Predictive Intelligence form appears. You use this form to prepare your call request to the
Predictive Intelligence API.
6. In the solution-name Value field, type ml_incident_categorization.

> Source page: 1489

#### Note: This is the Name value you captured in Step 1 of this procedure.

7. Click Add query parameter.
The Predictive Intelligence form refreshes to show the Query parameters section.
8. Type short_description in the first field.

#### Note: This is the input field you captured in Step 2 of this procedure.

9. Type a short description of an incident in the second field.
For instance, type Unable to connect.
10. Click the Send button.
The REST API Explorer sends your request to the Predictive Intelligence API.
The system predicts the output value in the Response Body section of the API output. You can
use other short descriptions to test what the solution is predicting.
11. Optional: Send a different request to the Predictive Intelligence API so that you can test the
prediction model again.
a. Return to the Query parameters section of the Predictive Intelligence form.
b. Type a short description that references a different kind of incident in the second field.
For example, type Unable to connect to MSSQL.
c. Click the Send button.
The Response Body section may refresh to show a different outcome than what you saw in
Step 9, depending on which incident categories you configured in your solution definition
setup. In other words, changing the short description text can recategorize the incident as a
different kind of issue.

#### Example:

You can also test the Predictive Intelligence prediction model when you create a new incident
record using the incident form.
1. Navigate to Incident > Create New.
2. In the new Incident form that loads, set the fields as follows.
  ◦User: Enter the Caller name.
  ◦Category: Leave as default.
  ◦Short description: Enter a short description that you want to test.
3. Submit the incident form.
Result: When the form refreshes, an information message appears with the incident category
automatically set to a specific value.

#### Note: For some short descriptions, the prediction might not process because the solution

does not have enough confidence in predicting the value for this input.

#### Related topics

Predictive Intelligence API
MLPredictor - Global

> Source page: 1490

#### Test a similarity solution prediction

Once your machine-learning (ML) solutions are trained, you can call on the Predictive
Intelligence API to make a solution prediction. In this example procedure, we use the
REST API Explorer application to test a similarity solution prediction for resolved incident
recommendations.

#### Before you begin

Train your ML solution prior to testing a prediction.
Role required: web_service_admin, rest_api_explorer, or admin or ml_admin

#### About this task

This procedure uses sample data to illustrate what you can do in your instance, and may not
represent data or records that are actually in your instance.
This scenario illustrates a similarity solution prediction for a hypothetical ML solution that
you have previously created and trained. You can also use the REST API Explorer to test a
classification solution prediction.

#### Procedure

1. Navigate to All > Predictive Intelligence > Similarity > Solution Definitions.
2. Locate the ML solution definition whose prediction you want to test, and copy its Name value
to your clipboard or a Notepad file.
In this case, we use the Name field value in your ML Solution Definition Recommended
Resolved Incidents record, as illustrated in the following example.
3. Copy the Input Fields value(s) used in your ML Solution Definition record that you want the
REST API Explorer to use in its call to the Predictive Intelligence API.
In this case, we use the Short description field type, as the prediction model has been trained
to use this field to learn, pair, and recommend similar records for your review.
4. Right-click the browser tab you're using to view your instance, and select Duplicate.

> Source page: 1491

5. In the duplicate browser tab, navigate to System Web Services > REST > REST API Explorer.
6. Click Explore.
7. Set these choice fields as follows.

#### Field

#### Value

#### Namespace

now (leave as default)

#### API Name

Predictive Intelligence

#### API Version

latest (leave as default)
The Predictive Intelligence form appears. You use this form to prepare your call request to the
Predictive Intelligence API.
8. In the solution-name Value field, enter
ml_x_snc_global_recommended_resolved_incidents.

#### Note: This is the Name value you captured in Step 2 of this procedure.

9. Click Add query parameter.
10. In the Query parameters section, enter the value of one of the Input Fields from the solution
you're testing.
a. In the first field, paste short_description.

#### Note: This is one of the input fields you captured in Step 2 of this procedure.

You can use other field types, such as Description or Resolution notes to test what the
solution is predicting.
b. In the second field, enter some text that you might find in an incident record.
For instance, enter Discovery errors.
11. Click the [+] button to create a second query condition that defines the number of results you
want to query.
a. In the first field, enter top_n.
b. In the second field, enter 3.
These conditions set the query to retrieve the top three most similar incident records.
12. Click Send.
The REST API Explorer sends your request to the Predictive Intelligence API.
13. In the Response body section, copy the three outcome values that your API call returned, as
illustrated in the image below.

> Source page: 1492

14. In your original browser tab, navigate to Servicedesk > Incidents.
15. As shown in the image below, set filter conditions for the three REST API outcomes to the
Incidents table list view.
a. Add the Active and Sys ID conditions below to the Incidents list view Filter icon.
b. Paste the three REST API outcomes into the Input value field of the Sys ID condition that you
created.
c. Click Run.
16. Per the image below, compare the returned list of incidents with the input for the prediction
output in the REST API Explorer.

> Source page: 1493

a. Click the Incident Number to open the Incident record.
b. Per the image below, review the Resolution notes text in the Incident record.

#### Related topics

Predictive Intelligence API
MLPredictor - Global

#### Track classification prediction results over time

Use the Prediction Results dashboard to determine if classification solution predictions are
improving over time. Identify solutions that need refining or retraining.

#### Before you begin

• Role required: admin, ml_admin, or ml_report_user

#### About this task

The Prediction Results dashboard reports on coverage, precision, and recall over time for
classification solutions.
With the Xanadu release, this dashboard has been migrated to the
Next Experience UI. Customers upgrading from previous releases

> Source page: 1494

can access the Core UI version from the current dashboard.
On the Prediction Results dashboard, statistics are provided in two timeframes: the average for
the past 30 days, and daily. The indicators coverage, precision, and recall are defined as follows.

#### Prediction Results indicators

#### Report type

#### Definition

Coverage
The percentage of predictions that yielded an
outcome out of the total number of predictions
that were attempted.
Precision
The percentage of predictions where the
predicted value was the same as the final
value of the field when the report closed.
Recall
The percentage of correct predictions that
yielded an outcome out of the total number of
predictions that were attempted.

#### Procedure

1. Navigate to All > Predictive Intelligence > Classification > Prediction Results Report.
2. In the Prediction Results dashboard Filter by solution prompt, select the solution statistics you
want to review.
The system updates the dashboard based on the solution you selected.
3. Identify classes with anomalous coverage, precision, or recall values.

#### Example

For example, identify solutions where coverage, precision, or recall is declining over time.

#### What to do next

Refine the solution definition filter by including or excluding classes as needed. After updating,
retrain the solution.

#### Reviewing prediction errors with the Observability Dashboard

The Observability Dashboard offers a unified view and actionable insights for errors detected
in Predictive Intelligence. Use this dashboard to visualize logged errors and gain information on
prediction reliability and potential problem areas.
View the PI - Observability Dashboard by navigating to Predictive Intelligence > Observability >
Observability Dashboard. The dashboard contains the following widgets.

> Source page: 1495

• Total Number of Prediction Errors
• Prediction Errors Breakdown by Date
• Prediction Errors Count by Capability
• Prediction Error Count by Error Type
• Error Types by Capability
• Successful and Unsuccessful Predictions Breakdown by Date
You can drill down to the underlying records from the widget graphics. You can also change the
date range of all widgets by selecting Date to open the selector.

#### PI Observability Dashboard — upper four widgets

The PI - Observability Dashboard draws from a table dedicated to logging prediction errors: ML
Predictor Error Logs [ml_predictor_error_logs].
• Fields in the table include Error Type, Error Message, Status code, Solution, and Capability.
• View this table's records directly by navigating to Predictive Intelligence > Observability >
Prediction Error Logs.
• Roles required to access the table: ml_report_user or ml_admin.
The table logs the following types of granular errors.
• Client-side issues (400 Series) — captures request errors such as timeouts and invalid inputs.
• Server-side issues (500 Series) — tracks internal server errors encountered during prediction.
• Internal prediction failures — identifies instances when the model was unable to generate a
prediction.
• Low confidence predictions — records log results falling below a defined confidence threshold.

#### Note: Errors in training aren't included in this table.

> Source page: 1496

#### PI Observability Dashboard — lower two widgets


---

## IMAGE DESCRIPTIONS

### Repeated ServiceNow page header/logo

The ServiceNow-branded wordmark appears in the upper-left corner of reviewed source pages for this subsection. It is a recurring branding image, not a technical diagram. It contains the visible brand text `servicenow`, with green accenting in the `now` portion. Reviewed pages: 1487, 1488, 1489, 1490, 1491, 1492, 1493, 1494, 1495, 1496.

### Small UI icons and inline pictograms

No small non-logo icon/pictogram image blocks were detected within this subsection boundary.

### Source page 1488 — Image 1

![Source page 1488 image 1](_assets/p1488_image01.png)

* **Bounding box:** x=112.0, y=141.3, width=432.0 pt, height=102.3 pt.
* **Nearby source context:** 1. Navigate to All > Predictive Intelligence > Classification > Solution Definitions. / 2. Locate the ML solution definition whose prediction you want to test, and copy its Name value / In this case, use the Name field value in your ML Solution Definition Incident Categorization
* **What is shown:** This embedded source image appears near the source context `1. Navigate to All > Predictive Intelligence > Classification > Solution Definitions. / 2. Locate the ML solution definition whose prediction you want to test, and copy its Name value / In this case, use the Name field value in your ML Solution Definition Incident Categorization`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1488_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1488 — Image 2

![Source page 1488 image 2](_assets/p1488_image02.png)

* **Bounding box:** x=112.0, y=322.6, width=432.0 pt, height=200.4 pt.
* **Nearby source context:** In this case, use the Name field value in your ML Solution Definition Incident Categorization / 3. Write down and save the Input Fields used in your ML Solution Definition record that you want / In this case, we use the short _description field, as the prediction model has been trained to
* **What is shown:** This embedded source image appears near the source context `In this case, use the Name field value in your ML Solution Definition Incident Categorization / 3. Write down and save the Input Fields used in your ML Solution Definition record that you want / In this case, we use the short _description field, as the prediction model has been trained to`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1488_image02.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1490 — Image 3

![Source page 1490 image 3](_assets/p1490_image01.png)

* **Bounding box:** x=112.0, y=378.4, width=432.0 pt, height=79.0 pt.
* **Nearby source context:** 1. Navigate to All > Predictive Intelligence > Similarity > Solution Definitions. / 2. Locate the ML solution definition whose prediction you want to test, and copy its Name value / In this case, we use the Name field value in your ML Solution Definition Recommended
* **What is shown:** This embedded source image appears near the source context `1. Navigate to All > Predictive Intelligence > Similarity > Solution Definitions. / 2. Locate the ML solution definition whose prediction you want to test, and copy its Name value / In this case, we use the Name field value in your ML Solution Definition Recommended`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1490_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1490 — Image 4

![Source page 1490 image 4](_assets/p1490_image02.png)

* **Bounding box:** x=112.0, y=536.4, width=432.0 pt, height=174.8 pt.
* **Nearby source context:** In this case, we use the Name field value in your ML Solution Definition Recommended / 3. Copy the Input Fields value(s) used in your ML Solution Definition record that you want the / In this case, we use the Short description field type, as the prediction model has been trained
* **What is shown:** This embedded source image appears near the source context `In this case, we use the Name field value in your ML Solution Definition Recommended / 3. Copy the Input Fields value(s) used in your ML Solution Definition record that you want the / In this case, we use the Short description field type, as the prediction model has been trained`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1490_image02.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1492 — Image 5

![Source page 1492 image 5](_assets/p1492_image01.png)

* **Bounding box:** x=112.0, y=39.0, width=356.2 pt, height=281.2 pt.
* **Nearby source context:** No nearby heading text was detected.
* **What is shown:** This embedded source image appears near the source context `No nearby heading text was detected.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1492_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1492 — Image 6

![Source page 1492 image 6](_assets/p1492_image02.png)

* **Bounding box:** x=112.0, y=459.8, width=432.0 pt, height=128.3 pt.
* **Nearby source context:** a. Add the Active and Sys ID conditions below to the Incidents list view Filter icon. / b. Paste the three REST API outcomes into the Input value field of the Sys ID condition that you / c. Click Run.
* **What is shown:** This embedded source image appears near the source context `a. Add the Active and Sys ID conditions below to the Incidents list view Filter icon. / b. Paste the three REST API outcomes into the Input value field of the Sys ID condition that you / c. Click Run.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1492_image02.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1493 — Image 7

![Source page 1493 image 7](_assets/p1493_image01.png)

* **Bounding box:** x=122.0, y=67.2, width=432.0 pt, height=141.5 pt.
* **Nearby source context:** a. Click the Incident Number to open the Incident record.
* **What is shown:** This embedded source image appears near the source context `a. Click the Incident Number to open the Incident record.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1493_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1493 — Image 8

![Source page 1493 image 8](_assets/p1493_image02.png)

* **Bounding box:** x=122.0, y=250.3, width=432.0 pt, height=223.3 pt.
* **Nearby source context:** a. Click the Incident Number to open the Incident record. / b. Per the image below, review the Resolution notes text in the Incident record.
* **What is shown:** This embedded source image appears near the source context `a. Click the Incident Number to open the Incident record. / b. Per the image below, review the Resolution notes text in the Incident record.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1493_image02.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1494 — Image 9

![Source page 1494 image 9](_assets/p1494_image01.png)

* **Bounding box:** x=72.0, y=51.5, width=432.0 pt, height=161.9 pt.
* **Nearby source context:** can access the Core UI version from the current dashboard.
* **What is shown:** This embedded screenshot/figure supports the Predictive Intelligence observability or monitoring topic. It depicts dashboard or report-style UI components such as widgets, charts, lists, labels, or result panes used to understand solution prediction behavior, errors, or logged outputs.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1494_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are dashboard/report relationships: each widget or chart summarizes a metric or list derived from Predictive Intelligence prediction activity. No separate network topology or security boundary is shown.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1495 — Image 10

![Source page 1495 image 10](_assets/p1495_image01.png)

* **Bounding box:** x=102.0, y=209.8, width=432.0 pt, height=247.4 pt.
* **Nearby source context:** • Successful and Unsuccessful Predictions Breakdown by Date / date range of all widgets by selecting Date to open the selector. / PI Observability Dashboard — upper four widgets
* **What is shown:** This embedded screenshot/figure supports the Predictive Intelligence observability or monitoring topic. It depicts dashboard or report-style UI components such as widgets, charts, lists, labels, or result panes used to understand solution prediction behavior, errors, or logged outputs.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1495_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are dashboard/report relationships: each widget or chart summarizes a metric or list derived from Predictive Intelligence prediction activity. No separate network topology or security boundary is shown.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1496 — Image 11

![Source page 1496 image 11](_assets/p1496_image01.png)

* **Bounding box:** x=102.0, y=52.0, width=432.0 pt, height=178.5 pt.
* **Nearby source context:** PI Observability Dashboard — lower two widgets
* **What is shown:** This embedded screenshot/figure supports the Predictive Intelligence observability or monitoring topic. It depicts dashboard or report-style UI components such as widgets, charts, lists, labels, or result panes used to understand solution prediction behavior, errors, or logged outputs.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1496_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are dashboard/report relationships: each widget or chart summarizes a metric or list derived from Predictive Intelligence prediction activity. No separate network topology or security boundary is shown.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```


---

## TABLES

### Source page 1488 — Table 1

**Nearby source context:** In this case, we use the short _description field, as the prediction model has been trained to / 4. Navigate to System Web Services > REST > REST API Explorer. / 5. Set these choice fields as follows.

| Field | Value |
| --- | --- |
| Namespace | now (leave as default) |
| API Name | Predictive Intelligence |
| API Version | latest (leave as default) |

### Source page 1491 — Table 2

**Nearby source context:** 5. In the duplicate browser tab, navigate to System Web Services > REST > REST API Explorer. / 6. Click Explore. / 7. Set these choice fields as follows.

| Field | Value |
| --- | --- |
| Namespace | now (leave as default) |
| API Name | Predictive Intelligence |
| API Version | latest (leave as default) |

### Source page 1494 — Table 3

**Nearby source context:** Prediction Results indicators

| Report type | Definition |
| --- | --- |
| Coverage | The percentage of predictions that yielded an<br>outcome out of the total number of predictions<br>that were attempted. |
| Precision | The percentage of predictions where the<br>predicted value was the same as the final<br>value of the field when the report closed. |
| Recall | The percentage of correct predictions that<br>yielded an outcome out of the total number of<br>predictions that were attempted. |


---

## FIGURES

| Figure / visual | Source page | Asset or location | Analysis |
|---|---:|---|---|
| Embedded screenshot or instructional image 1 | 1488 | `_assets/p1488_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 2 | 1488 | `_assets/p1488_image02.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 3 | 1490 | `_assets/p1490_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 4 | 1490 | `_assets/p1490_image02.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 5 | 1492 | `_assets/p1492_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 6 | 1492 | `_assets/p1492_image02.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 7 | 1493 | `_assets/p1493_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 8 | 1493 | `_assets/p1493_image02.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Observability/dashboard screenshot 9 | 1494 | `_assets/p1494_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Observability/dashboard screenshot 10 | 1495 | `_assets/p1495_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Observability/dashboard screenshot 11 | 1496 | `_assets/p1496_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Markdown-converted table/grid 1 | 1488 | TABLES section | Source table/grid region converted into Markdown; nearby context: In this case, we use the short _description field, as the prediction model has been trained to / 4. Navigate to System Web Services > REST > REST API Explorer. / 5. Set these choice fields as follows. |
| Markdown-converted table/grid 2 | 1491 | TABLES section | Source table/grid region converted into Markdown; nearby context: 5. In the duplicate browser tab, navigate to System Web Services > REST > REST API Explorer. / 6. Click Explore. / 7. Set these choice fields as follows. |
| Markdown-converted table/grid 3 | 1494 | TABLES section | Source table/grid region converted into Markdown; nearby context: Prediction Results indicators |


---

## QUALITY ASSURANCE NOTES

* PAGES REVIEWED: 1487, 1488, 1489, 1490, 1491, 1492, 1493, 1494, 1495, 1496. Source page range: 1487-1496 (shared boundary pages split at source headings).
* IMAGES REVIEWED: 20 image blocks assigned/reviewed: 9 recurring header logo block(s), 0 small icon/pictogram block(s), and 11 large screenshot/diagram crop(s).
* TABLES REVIEWED: 3 table/grid region(s) converted to Markdown. Table pages: 1488, 1491, 1494.
* FIGURES REVIEWED: 11 large screenshot/diagram figure(s) plus 3 table/grid visual(s).
* OCR ISSUES FOUND: No unresolved OCR issues were identified in the main PDF text layer after cleanup. Embedded screenshot crops are preserved as source assets; automated image OCR was not applied in this pass to avoid inserting low-confidence text, and this is explicitly marked in each image record.
* OCR ISSUES CORRECTED: Removed recurring footer/page-number noise from the main content stream, normalized nonbreaking spaces and soft-hyphen/control artifacts, preserved bullets/numbering/property names, and converted detected tables to Markdown.
* SECTION MAPPING NOTES: Folder name is exactly `Predictive Intelligence`. File name and subsection name are exactly `Testing and monitoring predictions` from the TOC. Shared source pages were split at heading coordinates from the PDF text layer.
* PAGE FOOTERS REVIEWED: Reviewed recurring ServiceNow copyright/trademark footer and logical page numbers. Footer text reviewed: `© 2026 ServiceNow, Inc. All rights reserved. ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries. Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.`
* RECHECK PASSES COMPLETED: 12/12: page completeness, text extraction, table extraction, image extraction, diagram interpretation, section mapping, subsection mapping, file names, folder names, Markdown formatting, missed-content review, and OCR/text-layer cleanup.
* VERIFICATION ARTIFACTS: Large image crops and `image_inventory.csv` are stored in the `_assets` folder inside this section folder.
