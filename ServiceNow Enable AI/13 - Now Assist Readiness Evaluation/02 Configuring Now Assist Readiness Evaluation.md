# Configuring Now Assist Readiness Evaluation

_Source: ServiceNow Now Assist documentation, pages 1058-1059._

## Overview

Run the scheduled jobs and complete the Now Assist Readiness Evaluation guided setup configuration steps before viewing the generative AI and agentic AI assessment results.

Before configuring the Now Assist Readiness Evaluation app, confirm that the Now Assist Readiness Evaluation app is installed. Navigate to **All > System Definition > Plugins**, and search for either the app name, **Now Assist Readiness Evaluation**, or app ID, **sn_assess**, to confirm.

Configuration consists of two high-level steps:

1. **Run the GenAI/AgenticAI Assessment scheduled job** — Run the GenAI/AgenticAI Assessment scheduled job so that agentic and generative AI assessment results populate in **Workspaces > Now Assist Readiness Evaluation**.
2. **Configure the Now Assist Readiness Evaluation guided setup** — Complete the configuration for the five Now Assist jobs. Additional configuration is required to work with the Now Assist for HRSD assessment.

## Features

- Single scheduled job (**GenAI/Agentic AI Assessment**) that triggers both agentic and generative AI assessments.
- Guided setup that walks you through the five Now Assist generative AI assessment jobs.
- Optional additional configuration (Restricted Caller Access Privileges and System Properties) required only for Now Assist for HR Service Delivery (HRSD).

## Functionalities

### Components, fields, and navigation

- **Plugin / app**: Now Assist Readiness Evaluation, App ID **sn_assess**.
- **Scheduled Jobs** filter: **Application is Now Assist Readiness Evaluation**.
- **Scheduled job name**: GenAI/Agentic AI Assessment.
- **Update Personalized List icon** — used from the list header to add the Application column if it is not displayed.
- **Guided setup sections** (three sections appear in the Agentic AI Assessment Guided Setup):
  - **Scheduled Jobs**
  - **Restricted Caller Access Privileges** (only applicable for HRSD)
  - **System Properties** (only applicable for HRSD)
- **Restricted Caller Access Privileges table** — Status column values **Requested** and **Allowed**.
- **Application scope** required for HRSD sub-steps: **Human Resources: Core**.

### Roles

- **admin** — required to run the scheduled job and to complete the guided setup.

## Instructions / Procedures

### Run the GenAI/AgenticAI Assessment scheduled job

Before you can view the agentic AI or Now Assist assessment results, you must first run the GenAI/AgenticAI Assessment scheduled job.

**Before you begin**

- Role required: admin

**Procedure**

1. Navigate to **All > System Definition > Scheduled Jobs**.
2. Set the Scheduled Jobs filter to **Application is Now Assist Readiness Evaluation**, and then select **Run**.

   > **Tip:** If the Application column isn't displayed in your ServiceNow instance, personalize the column settings using the **Update Personalized List** icon from the list header.

3. Select **GenAI/Agentic AI Assessment** from the **Name** column.
4. Select **Execute Now**. This action begins the scheduled job for the agentic and generative AI assessments found in **Workspaces > Now Assist Readiness Evaluation**.

**What to do next**

If you must rerun all the scheduled jobs, or specifically the agentic AI scheduled jobs for ITSM and CSM, repeat these steps.

> **Note:** You must complete the additional steps in the Now Assist Readiness Evaluation guided setup if you want to work with the Now Assist for HRSD product. If you don't complete the additional guided setup steps for the Now Assist for HRSD product, the assessment continuously fails. For more information about completing the Now Assist Readiness Evaluation guided setup, see Configure the Now Assist Readiness Evaluation guided setup.

### Configure the Now Assist Readiness Evaluation guided setup

Before you can review the Now Assist assessments in **Workspaces > Now Assist Readiness Evaluation**, you must first complete the configuration for the five Now Assist jobs.

**Before you begin**

- Before completing this guided setup, you must first run the generative AI and agentic AI scheduled jobs. For more information, see Run the GenAI/AgenticAI Assessment scheduled job.
- Role required: admin

**Procedure**

1. Navigate to **All > System Definition > Plugins**.
2. In the search bar, search for **Now Assist Readiness Evaluation**.
3. Select the **Installed** tab to view the installed store application **Now Assist Readiness Evaluation** (App id: sn_assess).
4. Select **Now Assist Readiness Evaluation**.
5. In the **Get started** area, select **Configure**.
6. Review the **Want to know how it works?** screen, and then select **Continue**. You're redirected to the **Agentic AI Assessment Guided Setup**.

   > **Tip:** You can also access the Agentic AI Assessment Guided Setup screen by navigating directly to **All > Now Assist Readiness Evaluation > Guided Setup**.

   Three sections appear: **Scheduled Jobs**, **Restricted Caller Access Privileges**, and **System Properties**. The Restricted Caller Access Privileges and System Properties sections are only applicable if you want to work with Now Assist for HR Service Delivery (HRSD).

(Note: The guided setup procedure continues on the following documentation page, "Using Now Assist Readiness Evaluation," with steps 7 through 13, including the optional HRSD configuration sub-steps.)

## Figures, Diagrams & Screenshots

**Figure (p.1058):** Text-only documentation page. The top of the page continues the "Now Assist Readiness Evaluation benefits (continued)" table (mapping benefits such as improving implementation gaps via hyperlinks and receiving estimated remediation effort to the Reviewing your Now Assist assessment / Reviewing your agentic AI assessment features and the Admins user). Below this is the "What to explore next" list and the start of the "Configuring Now Assist Readiness Evaluation" topic, including the "Configuration overview" with the numbered list of the two configuration steps and the beginning of the "Run the GenAI/AgenticAI Assessment scheduled job" procedure. No screenshots or diagrams appear on this page.

**Figure (p.1059):** Text-only documentation page presenting the procedure steps for running the GenAI/AgenticAI Assessment scheduled job (steps 1-4 with the Tip referencing the Update Personalized List icon) and the beginning of the "Configure the Now Assist Readiness Evaluation guided setup" procedure (steps 1-6). Inline within the Tip text is a small "Update Personalized List" gear/list icon. No full screenshots, dashboards, or diagrams appear on this page beyond that small inline icon and the ServiceNow header logo.
