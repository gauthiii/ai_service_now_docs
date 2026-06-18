# Using Now Assist Readiness Evaluation

_Source: ServiceNow Now Assist documentation, pages 1060-1068._

## Overview

The Now Assist Readiness Evaluation app helps you find actionable items in your implementation preparation and provides direct hyperlinks to improve upon those gaps. Use the app to help you prepare to launch generative AI, agentic AI, or both in Now Assist for your organization.

The following is a high-level overview of the documentation topics in this section that you can refer to on how to use and interpret the Now Assist Readiness Evaluation results:

- **Using Now Assist Readiness Evaluation dashboard** — View an overall dashboard of your assessments' findings divided up into percentages and bar chart visuals.
- **Assessing readiness status** — View an overall dashboard of readiness and issue categorization before implementing Now Assist.
- **Reviewing your Now Assist assessment** — View the Now Assist assessment report results for the five available Now Assist products.
- **Reviewing your agentic AI assessment** — View the agentic AI assessment report results for IT Service Management (ITSM) and Customer Service Management (CSM).

## Features

### Using Now Assist Readiness Evaluation dashboard

The Now Assist Readiness Evaluation dashboard comes with two dashboard tabs: **Agentic AI - Assessment** and **Now Assist Assessment**. Navigate to **Workspaces > Now Assist Readiness Evaluation** to access the dashboard. The Now Assist Readiness Evaluation dashboard is the first tab you see.

The dashboard is a powerful product feature that accelerates generative and agentic AI readiness for Now Assist by delivering automated, data-driven insights.

> **Note:** The **Remediation properties** tab may also appear on the Now Assist Readiness Evaluation dashboard. This tab only appears if the `sn_assess.effort_visibility` system property is set to **true**. For more information about this system property, see Now Assist Readiness Evaluation system properties.

After reviewing the dashboard and making the suggested assessment changes, rerun your scheduled jobs to see how your results improve.

#### Agentic AI - Assessment dashboard tab

Helps determine agentic AI readiness for IT Service Management (ITSM) and Customer Service Management (CSM) by delivering automated, data-driven insights.

> **Note:** For results to appear in this dashboard, confirm that you have completed the configuration steps first. For more information on configuration, see Configuring Now Assist Readiness Evaluation.

Details of the agentic AI - Assessment dashboard tab:

- **Total Estimated Effort (Days)** — Shows the total estimated work effort in development days.
- **Remediation Effort by Category** — Shows the estimated work effort needed to correct the findings for each product, depending on the findings category, in a bar chart.
- **Estimated Effort - Trends** — Shows the trends over time in a bar chart for each products' estimated work effort.
- **Assessment Findings** — Shows the number of assessment items that need attention.
- **Findings by Category** — Shows the percentage of each assessment finding category for each product in a bar chart.
- **Finding Trends** — Shows the trends over time in a bar chart for the products that need the most attention before implementation.

You can select each widget on the dashboard to have that table data open in a separate tab.

#### Now Assist Assessment dashboard tab

Helps determine generative AI readiness for Now Assist by delivering automated, data-driven insights.

> **Note:** For results to appear in this dashboard, verify that you have completed the configuration steps first. For more information on configuration, see Configuring Now Assist Readiness Evaluation.

Details of the Now Assist Assessment dashboard tab (same widget set as the agentic AI tab):

- **Total Estimated Effort (Days)** — Shows the total estimated work effort in development days.
- **Remediation Effort by Category** — Shows the estimated work effort needed to correct the findings for each product, depending on the findings category, in a bar chart.
- **Estimated Effort - Trends** — Shows the trends over time in a bar chart for each products' estimated work effort.
- **Assessment Findings** — Shows the number of assessment items that need attention.
- **Findings by Category** — Shows the percentage of each assessment finding category for each product in a bar chart.
- **Finding Trends** — Shows the trends over time in a bar chart for the products that need the most attention before implementation.

You can select each widget on the dashboard to have that table data open in a separate tab.

### Assessing readiness status

The app shows you a high-level overview of your go or no-go status for your organization's readiness to implement agentic AI, generative AI, or both in Now Assist.

An overall ready or action-required status is determined by percentage rules:

- A green **Ready** button appears if over 75% of your instance is ready to implement agentic AI, generative AI, or both in Now Assist.
- A yellow **Action Required** button appears if 75% or less of your instance is determined to be ready to implement agentic AI, generative AI, or both in Now Assist.

Each finding is broken down and automatically tagged as a **product**, **data**, or **configuration** issue. Having issues categorized lets you know whether you should open a Now Support case, cleanse data, or adjust platform settings.

- The **Agentic AI Assessment Home Page** tab displays the Ready or Action Required buttons for Now Assist agentic AI in ITSM, CSM, and Now Assist for HRSD.
- The **Now Assist Assessment Home Page** tab details the go or no-go status for Now Assist products and features, including:
  - Now Assist in AI Search
  - Now Assist in Virtual Agent
  - Now Assist for IT Service Management (ITSM)
  - Now Assist for Customer Service Management (CSM)
  - Now Assist for HR Service Delivery (HRSD)

Select the assessment feature's tile on the home page to be redirected to that assessment tab's report results. To impact these percentages, rerun your scheduled jobs after making your suggested assessment fixes.

> **Note:** The readiness assessment percentages displayed on each card do not update in real-time. After making the fixes recommended in your assessment results, rerun the scheduled jobs to view the updated assessment percentages.

### Reviewing your Now Assist assessment

This automated assessment process evaluates potential implementation impacts and provides actionable insights for Now Assist products.

> **Note:** Before viewing your Now Assist assessments, you must first have run the scheduled jobs to get the assessment results. If you haven't run your scheduled jobs, you're prompted to do so on an individual job level. For more information, see Run the GenAI/AgenticAI Assessment scheduled job and Configure the Now Assist Readiness Evaluation guided setup.

The **Summary** tab provides a consolidated summary of features, including Now Assist capabilities across AI Search, Virtual Agent (VA), IT Service Management (ITSM), Customer Service Management (CSM), and HR Service Delivery (HRSD), as well as their corresponding estimated remediation efforts. The results shown are estimates. You should evaluate results provided by Now Assist Readiness Evaluation for accuracy and appropriateness for your use case.

To understand the estimated remediation effort, select the **Legends** button. The legend shows the estimated remediation effort using sizing verbiage and colors, along with an estimated timeline of remediation in development days. The legend also includes descriptions of the icons found next to the assessment questions.

After reviewing the summary, select the individual assessment links to be redirected to that specific assessment in a new browser tab. The questions for each Now Assist assessment differ. For example, the questions and answers on the Now Assist in AI Search assessment are different than the questions and answers on the Now Assist in Virtual Agent assessment.

> **Note:** The assessments gather information from tables. To view any of the tables' available questions, answers, assessments, or assessment run successes or failures, search for the applicable table in the navigation filter:
> - Questions [sn_assess_question] table
> - Answers [sn_assess_answer] table
> - Assessment [sn_assess_assessment] table
> - Assessment Run [sn_assess_assessment_run] table
>
> For more information about how to search for tables in the navigation filter, see Navigate directly to a table.

The assessments include visual indicators to guide you on non-blocker and blocker results:

- **Informational (green check)** — Informational area and no further action needed.
- **Required (red X)** — Further action is needed to resolve findings before implementation. These required areas include estimated remediation efforts.
- **Recommended (yellow warning triangle)** — Recommended area warning, but the finding should be evaluated before implementation. These recommendations are observations that should be reviewed prior to implementation but no estimated remediation effort is provided.

You can select **Download Report** to export the entire Now Assist assessment report in PDF format from the Summary tab. The exported report includes hyperlinks to the specific individual assessments. Selecting Download Report on an individual assessment downloads only that report in PDF format. After selecting a hyperlink in the PDF, that record or table opens in a separate browser tab.

> **Note:** You don't have to select Download Report to work directly with the problematic records or tables found in the assessment. Each assessment includes hyperlinks to the records or tables that need attention. Selecting a hyperlink opens the record or table in a separate browser tab.

After reviewing the assessment and making the suggested assessment changes, rerun your scheduled jobs to see how your results improve.

### Reviewing your agentic AI assessment

This automated assessment process evaluates potential implementation impacts and provides actionable insights for agentic AI in Now Assist for IT Service Management (ITSM) and Now Assist for Customer Service Management (CSM).

> **Note:** Before viewing your agentic AI assessments, you must first have run the scheduled job to get the assessment results. If you haven't run your scheduled jobs, you're prompted to do so on an individual job level. For more information, see Run the GenAI/AgenticAI Assessment scheduled job.

The **Summary** tab provides a consolidated summary of overall findings along with summarization and resolution notes for ITSM and CSM. The results shown are estimates. You should evaluate results provided by Now Assist Readiness Evaluation for accuracy and appropriateness for your use case.

To better understand the estimated remediation effort, select the **Legends** button. The legend shows the estimated remediation effort using sizing verbiage and colors, along with an estimated timeline of remediation in development days. The legend also includes descriptions of the icons found next to the assessment questions.

After reviewing the summary, select the individual assessment tabs to review those specific assessments. The questions for each assessment differ. For example, the questions and answers on the Agentic AI - ITSM assessment tab are different than the questions and answers on the Agentic AI - CSM assessment tab.

The same table-search note (Questions, Answers, Assessment, Assessment Run tables) and the same set of visual indicators (Informational / Required / Recommended) and **Download Report** behavior described for the Now Assist assessment also apply to the agentic AI assessment.

## Functionalities

### Navigation

- **Workspaces > Now Assist Readiness Evaluation** — entry point for the dashboard, home page (readiness status), Now Assist assessment, and agentic AI assessment.
- **Home icon** — review your assessments' home page (readiness status).
- **Assessment icon** — review your Now Assist assessment.
- **Agentic AI assessment icon** — review your agentic AI assessment.

### Dashboard tabs

- **Now Assist Readiness Evaluation dashboard** (first tab)
- **Agentic AI - Assessment** tab
- **Now Assist Assessment** tab
- **Remediation properties** tab (appears only when `sn_assess.effort_visibility` = true)

### Dashboard widgets (both Agentic AI and Now Assist tabs)

- Total Estimated Effort (Days)
- Remediation Effort by Category (bar chart)
- Estimated Effort - Trends (bar chart)
- Assessment Findings
- Findings by Category (bar chart)
- Finding Trends (bar chart)

### Readiness status buttons and categories

- **Ready** (green) — over 75% ready.
- **Action Required** (yellow) — 75% or less ready.
- Finding categories: **product**, **data**, **configuration**.

### Legends — Estimated Remediation Effort sizing

| Effort | Time (in days) |
| ------ | -------------- |
| None   | 0              |
| Small  | 1-5            |
| Medium | 6-10           |
| Large  | 11-30          |
| XL     | 31-90          |
| XXL    | >90            |

**Icon Details (Legends):**

- Informational (green check)
- Required (red X)
- Recommended (yellow warning triangle)

### Tables used by assessments

- Questions **[sn_assess_question]**
- Answers **[sn_assess_answer]**
- Assessment **[sn_assess_assessment]**
- Assessment Run **[sn_assess_assessment_run]**

### Other components

- **Legends** button
- **Download Report** button (Summary tab and per-individual assessment; exports PDF with hyperlinks)
- Interactive hyperlinks to records/tables in each assessment

### Roles

- Configuration and review tasks are performed by Admins (the app is intended for admin users).

## Instructions / Procedures

### Guided setup (continuation, steps 7-13)

This page continues the **Configure the Now Assist Readiness Evaluation guided setup** procedure (steps 1-6 are on the previous documentation page).

7. Select **Start** in the Scheduled Jobs section. You're redirected to the five scheduled Now Assist generative AI jobs.

   > **Note:** You're unable to run agentic AI scheduled jobs from this guided setup. To run agentic AI scheduled jobs, you must do so through the GenAI/AgenticAI Assessment scheduled job. For more information on running the agentic AI scheduled job, see Run the GenAI/AgenticAI Assessment scheduled job.

8. Select the link to the specific scheduled job to have that job open in a new browser tab. For example, if you select the **Now Assist Assessment - AI Search** link, that scheduled job appears in a new browser tab.
9. Select **Execute Now** to begin that job. The job begins and you're redirected back to the guided setup.
10. Select **Next** in the guided setup.
11. Repeat steps 8-10 until you have run the scheduled jobs for the five Now Assist assessments. You have completed the Now Assist assessment jobs. If you ran the HRSD job, continue to the following optional steps.
12. **Optional:** If you have run the job for HRSD, select the **Change The State to Allowed for the following records** link on the **Restricted Caller Access Privileges** screen.

    > **Note:** The following sub-steps can only be completed when in the **Human Resources: Core** application scope. For more information on changing application scopes, see Select an application from the application picker.

    a. Change the **Status** column from **Requested** to **Allowed** on the Restricted Caller Access Privileges table, and then go back to the guided setup.
    b. Select **Next** on the Restricted Caller Access Privileges screen.
    c. Select the **Configure System Properties** link on the **System Properties** screen to review the system properties.
    d. Select **Mark Complete**.
13. Select **Close**.

**Result:** You have completed configuration for the Now Assist assessments.

**What to do next:** You can navigate to **Workspaces > Now Assist Readiness Evaluation** to review your assessment results.

### Access the Now Assist Readiness Evaluation dashboard

Navigate to **Workspaces > Now Assist Readiness Evaluation**. The Now Assist Readiness Evaluation dashboard is the first tab you see. Select the **Agentic AI - Assessment** or **Now Assist Assessment** tab. You can select each widget on the dashboard to have that table data open in a separate tab.

### Assess readiness status

1. Navigate to **Workspaces > Now Assist Readiness Evaluation**.
2. Select the **Home** icon to review your assessments' home page.
3. Review the Ready (green) or Action Required (yellow) buttons on the Agentic AI Assessment Home Page and Now Assist Assessment Home Page tabs.
4. Select the assessment feature's tile on the home page to be redirected to that assessment tab's report results.
5. To impact the percentages, rerun your scheduled jobs after making your suggested assessment fixes.

### Review your Now Assist assessment

1. Navigate to **Workspaces > Now Assist Readiness Evaluation** and select the **assessment** icon.
2. Review the **Summary** tab for a consolidated summary across AI Search, VA, ITSM, CSM, and HRSD and their estimated remediation efforts.
3. Select the **Legends** button to understand the estimated remediation effort sizing and icon meanings.
4. Select the individual assessment links to open each specific assessment in a new browser tab.
5. Use the visual indicators (Informational / Required / Recommended) to interpret findings.
6. Optionally select **Download Report** to export the report (entire Summary or an individual assessment) in PDF format with hyperlinks. Alternatively, select hyperlinks directly in the assessment to open the relevant record or table in a separate browser tab.
7. After making changes, rerun your scheduled jobs to see how your results improve.

### Review your agentic AI assessment

1. Navigate to **Workspaces > Now Assist Readiness Evaluation** and select the **agentic AI assessment** icon.
2. Review the **Summary** tab for the consolidated summary of overall findings with summarization and resolution notes for ITSM and CSM.
3. Select the **Legends** button to understand the estimated remediation effort sizing and icon meanings.
4. Select the individual assessment tabs (for example, Agentic AI - ITSM and Agentic AI - CSM) to review those specific assessments.
5. Use the visual indicators (Informational / Required / Recommended) to interpret findings.
6. Optionally select **Download Report** to export the report in PDF format with hyperlinks, or select hyperlinks directly to open the relevant record or table.
7. After making changes, rerun your scheduled jobs to see how your results improve.

## Figures, Diagrams & Screenshots

**Figure (p.1060):** Text-only documentation page. Continues the guided-setup procedure steps 7-13 (including the optional HRSD sub-steps a-d, the Result, and the What to do next) and begins the "Using Now Assist Readiness Evaluation" topic with its "Overview" bullet list. No screenshots or diagrams appear on this page beyond the ServiceNow header logo.

**Figure (p.1061):** Text-only documentation page describing the "Using Now Assist Readiness Evaluation dashboard" topic and the Agentic AI - Assessment dashboard tab widget definitions (Total Estimated Effort, Remediation Effort by Category, Estimated Effort - Trends, Assessment Findings, Findings by Category, Finding Trends). It also contains the Note about the Remediation properties tab and the `sn_assess.effort_visibility` property. No screenshots appear on this page; the dashboard screenshot itself spans onto page 1062.

**Figure (p.1062):** Dashboard screenshot — "Example of the Now Assist Readiness Evaluation Dashboard's Agentic AI - Assessment." The screenshot shows the Now Assist Readiness Evaluation Dashboard with the **Agentic AI - Assessment** tab selected (alongside a "Now Assist Assessment" tab in the header). Two large numeric KPI tiles are prominently displayed: a large **4** (one KPI, e.g., Total Estimated Effort / Days) and a large **14** (another KPI, e.g., Assessment Findings). To the right are colored bar-chart panels (orange/teal/blue bars) corresponding to the Remediation Effort by Category, Estimated Effort - Trends, Findings by Category, and Finding Trends widgets. The figure illustrates how the agentic AI dashboard surfaces estimated effort and findings counts with supporting bar charts. The lower portion of the page is text beginning the "Now Assist Assessment dashboard tab" description (Total Estimated Effort, Remediation Effort by Category, Estimated Effort - Trends).

**Figure (p.1063):** Dashboard screenshot — "Example of the Now Assist Readiness Evaluation Dashboard's Now Assist Assessment." The screenshot shows the Now Assist Readiness Evaluation Dashboard with the **Now Assist Assessment** tab selected. Two large numeric KPI tiles are displayed: a large **8** and a large **2**, accompanied by colored bar-chart panels (orange/teal/blue) representing the Remediation Effort by Category, Estimated Effort - Trends, Findings by Category, and Finding Trends widgets. The figure illustrates how the generative AI (Now Assist) dashboard presents estimated effort, assessment-finding counts, and category/trend bar charts. The remaining page text continues the widget descriptions and begins the "Assessing readiness status" topic.

**Figure (p.1064):** Two home-page screenshots:
- **Example of the Agentic AI Assessment Home Page** (top) — A row of status cards, each showing a product/area (ITSM, CSM, HRSD) with a readiness percentage and a status button. Cards display green **Ready** buttons for areas over 75% ready and yellow **Action Required** buttons for areas at 75% or less; visible percentage values appear on each card. This illustrates the go/no-go readiness status for Now Assist agentic AI.
- **Example of the Now Assist Assessment Home Page** (bottom) — A grid of tiles for Now Assist products/features (Now Assist in AI Search, Now Assist in Virtual Agent, Now Assist for ITSM, Now Assist for CSM, Now Assist for HRSD), each showing a readiness percentage and a green Ready or yellow Action Required status button. This illustrates the go/no-go status for the five generative AI Now Assist products. The page also contains the Note that percentages do not update in real time and the start of the "Reviewing your Now Assist assessment" topic.

**Figure (p.1065):** Legends panel screenshot — "Example of Legends estimated remediation effort sizing." A floating panel (opened via the highlighted **Legends** button shown at the right edge) titled **Estimated Remediation Effort** with two columns: the effort sizing label and **Time (in days)**. Rows read: **None** = 0; **Small** (green) = 1-5; **Medium** (yellow/amber) = 6-10; **Large** (orange) = 11-30; **XL** (darker orange/red) = 31-90; **XXL** (red) = >90. Below is an **Icon Details** section showing: a green check = **Informational**, a red X = **Required**, and a yellow warning triangle = **Recommended**. The figure illustrates how to interpret the remediation effort sizing colors and the per-question status icons in the Now Assist assessment.

**Figure (p.1066):** Assessment screenshot — "Example of the Now Assist in Virtual Agent assessment." The screenshot shows a Now Assist assessment report page for Virtual Agent, with a left-hand list/navigation of assessment items, a series of assessment questions with their answers and status icons (informational/required/recommended), and visible action controls such as Legends and Download Report. The figure illustrates the structure of an individual Now Assist product assessment, including the question-and-answer findings and the embedded hyperlinks to records/tables. The page also contains the table-search note (sn_assess_question, sn_assess_answer, sn_assess_assessment, sn_assess_assessment_run) and the visual-indicator descriptions.

**Figure (p.1067):** Legends panel screenshot — "Example of Legends estimated remediation effort sizing" (agentic AI assessment version). Identical in structure to the p.1065 legend: an **Estimated Remediation Effort** panel with the None=0, Small=1-5, Medium=6-10, Large=11-30, XL=31-90, XXL=>90 sizing rows (color-coded green through red), plus the **Icon Details** section (green check = Informational, red X = Required, yellow triangle = Recommended). The highlighted **Legends** button is visible at the right. The figure illustrates the remediation effort sizing and icon meanings within the agentic AI assessment context.

**Figure (p.1068):** Text-only documentation page covering the "Reviewing your agentic AI assessment" continuation — the Summary tab description, the table-search note, the visual-indicator (Informational / Required / Recommended) descriptions, and the Download Report behavior. No screenshots or diagrams appear on this page beyond the ServiceNow header logo. (The "Example of the Agentic AI - ITSM assessment" screenshot referenced by this section appears on the following page, 1069.)
