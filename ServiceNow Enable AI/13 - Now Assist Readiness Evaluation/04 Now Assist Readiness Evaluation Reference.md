# Now Assist Readiness Evaluation Reference

_Source: ServiceNow Now Assist documentation, page 1069._

## Overview

Now Assist Readiness Evaluation admins and implementers can work with select system properties for additional customization. Use system properties to customize your readiness assessment results.

## Features

- Customize readiness assessment behavior and results through ServiceNow system properties.
- Control assessment performance limits for large data volumes.
- Control visibility and customization of estimated remediation efforts, including exposing the **Remediation properties** tab on the Now Assist Readiness Evaluation dashboard.

## Functionalities

### Access

Access these properties from the **System Property [sys_properties]** table.

### Roles

- **admin** / implementers — work with these system properties for additional customization.

### Now Assist Readiness Evaluation system properties

| Property | Description |
| -------- | ----------- |
| `sn_assess.assessment_limit` | Reduce performance issues when a large volume of data is assessed. Adjust this system property, if needed, so that the job can run successfully. The default value is **10000**. |
| `sn_assess.effort_visibility` | Customize the estimated remediation effort for select efforts. This property controls multiple sections associated with remediation effort. The default value is **false**. When this system property is set to **true**, the **Remediation properties** tab appears on the Now Assist Readiness Evaluation dashboard. You customize the estimated remediation efforts via the Remediation properties tab. All input values represent estimated remediation efforts in days. After making changes to the estimated remediation efforts, select **Save**, and then re-run the assessments to see the updated remediation efforts reflected. |

## Instructions / Procedures

This reference topic does not contain a discrete numbered procedure. The actionable guidance is embedded in the property descriptions:

- **To customize remediation efforts:** Set `sn_assess.effort_visibility` to **true**, which surfaces the **Remediation properties** tab on the Now Assist Readiness Evaluation dashboard. Enter values (in days) on that tab, select **Save**, and then re-run the assessments to see the updated remediation efforts reflected.
- **To handle large data volumes:** Adjust `sn_assess.assessment_limit` (default 10000) as needed so the assessment job can run successfully.

## Figures, Diagrams & Screenshots

**Figure (p.1069):** This page contains one screenshot and one reference table.

- **Example of the Agentic AI - ITSM assessment** (top of page) — A screenshot of the Agentic AI - ITSM assessment report. It shows the assessment view with a date/header bar, a list of assessment questions (findings) on the left/body with their answers and status icons, and a green status indicator at the upper right (consistent with a Ready/passing state). Action controls such as Legends and Download Report are visible. The figure illustrates the structure of the individual agentic AI ITSM assessment, including the question-and-answer findings and embedded hyperlinks to the affected records/tables. Caption text below the screenshot reminds the reader that, after reviewing the assessment and making the suggested changes, they should rerun the scheduled jobs to see how results improve (see Run the GenAI/AgenticAI Assessment scheduled job).
- **Now Assist Readiness Evaluation system properties table** (lower half of page) — The rendered reference table listing the two system properties (`sn_assess.assessment_limit` and `sn_assess.effort_visibility`) and their descriptions, as reproduced in the Functionalities section above. No additional diagrams appear on this page beyond the ServiceNow header logo.
