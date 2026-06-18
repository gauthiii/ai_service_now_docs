# Exploring Now Assist Readiness Evaluation

_Source: ServiceNow Now Assist documentation, pages 1054-1057._

## Overview

The Now Assist Readiness Evaluation app helps prepare your organization for implementing agentic AI for ITSM and CSM, Now Assist for five products, or both. The app automates assessment processes, evaluates data readiness impacting implementation, and provides actionable insights to promote adopting Now Assist quickly. The app enables you to assess whether updates, installations, or customizations of your instance could affect implementation. The assessments provide direct hyperlinks to improve any issues found.

The Now Assist Readiness Evaluation app is a solution designed to simplify and automate the agentic AI and Now Assist implementation assessment process. The app helps to determine whether your organization's instance is ready to implement generative and agentic AI features in Now Assist. Previously, manually assessing your organization's instance readiness was time consuming and took significant effort. Now, you can use the Now Assist Readiness Evaluation app to automate gathering, processing, and analyzing instance data so that you can review your instance readiness more quickly. The app provides results within seconds, helping to reduce manual effort and promoting rapid and reliable assessments.

The app includes assessment information for Now Assist by separating agentic AI solutions and generative AI solutions by tabs. Agentic AI solution information appears in the agentic AI tab, and generative AI solution information appears in the Now Assist tab.

To get started, the app presents three tiles: **Explore**, **Configure**, and **Use**.

- **Explore** — Learn about the Now Assist Readiness Evaluation app.
- **Configure** — Run scheduled jobs and configure the app through the Now Assist Readiness Evaluation guided setup.
- **Use** — Learn about how to use the Now Assist Readiness Evaluation dashboards and assessments to prepare for implementing agentic AI, Now Assist, or both.

### Important availability notes

- Not all model providers are available for customers with in-country SKUs, and some Now Assist products/features are currently unavailable for in-country customers. For more information, see the **KB1584492** article in the Now Support Knowledge Base. Be sure to check for model provider availability updates in future releases.
- Some Now Assist products/features are currently unavailable for customers in the FedRAMP, NSC DOD IL5, or Australia IRAP-Protected data centers, self-hosted customers, or in other restricted environments. For more information, see the **KB0743854** article in the Now Support Knowledge Base. Be sure to check for availability updates in future releases.
- Some Now Assist products/features are currently available only for customers in some regions. Be sure to check for availability updates in future releases.
- Some AI products and skills are not available in Regulated Markets. For more information, see **KB2593939: Regulated Markets AI Products/Skills Not Available**. Be sure to check for availability updates in future releases.

### AI limitations

This application uses artificial intelligence (AI) and machine learning, which are rapidly evolving fields of study that generate predictions based on patterns in data. As a result, this application may not always produce accurate, complete, or appropriate information. Furthermore, there is no guarantee that this application has been fully trained or tested for your use case. To mitigate these issues, it is your responsibility to test and evaluate your use of this application for accuracy, harm, and appropriateness for your use case, employ human oversight of output, and refrain from relying solely on AI-generated outputs for decision-making purposes. This is especially important if you choose to deploy this application in areas with consequential impacts such as healthcare, finance, legal, employment, security, or infrastructure. You agree to abide by ServiceNow's AI Acceptable Use Policy, which may be updated by ServiceNow.

### Data processing

This application requires data to be transferred from ServiceNow customers' individual instances to a centralized ServiceNow environment, which may be located in a different data center region from the one where your instance is, and potentially to a third-party cloud provider, such as Microsoft Azure. This data is handled per ServiceNow's internal policies and procedures, including our policies available through our CORE Compliance Portal.

### Data collection

ServiceNow collects and uses the inputs, outputs, and edits to outputs of this application to develop and improve ServiceNow technologies including ServiceNow models and AI products. Customers can opt out of future data collection at any time, as described in the Now Assist Opt-Out page.

## Features

The app evaluates and assesses both agentic AI solutions and generative AI Now Assist products after the necessary scheduled jobs have run.

### Agentic AI solutions evaluated

- **Agentic AI for Now Assist for IT Service Management (ITSM)** — Evaluates whether customizations on ITSM-related parent tables (such as Incident and Task) may interfere with AI agent behavior, task execution, or decision-making. The assessment identifies and flags high-risk customizations to help promote seamless agent operations and stable instance performance. Each finding includes interactive hyperlinks to the impacted records, enabling you to review, validate, and address potential issues without navigating away from the dashboard.
- **Agentic AI for Now Assist for Customer Service Management (CSM)** — Assesses whether customizations on CSM-specific tables (such as Case and Interaction) impact AI agent functionality. The assessment evaluates data completeness, field modifications, and scripting issues that may hinder agent-driven tasks and offers targeted estimated remediation to maintain agent efficacy. Each assessment finding includes interactive hyperlinks to the affected records, enabling you to navigate, validate, and resolve issues directly from the dashboard.

### Generative AI Now Assist products evaluated

- **Now Assist for AI Search** — Provides insights into the status and configuration of AI Search, such as active or inactive profiles, widget versions, and estimated remediation efforts. The assessment also evaluates Knowledge Management by assessing article counts, categories, group restrictions, and top searches or articles viewed. Additionally, the assessment highlights areas for improvement, offering actionable feedback to enhance knowledge quality and hygiene.
- **Now Assist for Virtual Agent (VA)** — Checks if Virtual Agent is live, tracks active topics and catalog items, and identifies barriers to conversational functionality. The assessment highlights opportunities to convert non-conversational items to conversational ones and tracks automation in catalog items, along with estimated remediation efforts.
- **Now Assist for IT Service Management (ITSM)** — Reviews customizations and configurations in the Incident and Task tables, such as fields, UI actions, and scripts. The assessment highlights changes made, tracks data completeness, and provides key metrics to improve accuracy and consistency in ITSM processes. The assessment also specifies the estimated remediation effort required and reports the language used in the instance.
- **Now Assist for Customer Service Management (CSM)** — Reviews customizations in the Case and Task tables, tracks changes to fields, and monitors data completeness for key fields. The assessment provides insights into past cases and field-filling percentages, helping improve data accuracy in Customer Service Management. The assessment also reports the estimated remediation effort needed and the language used in the instance.
- **Now Assist for HR Service Delivery (HRSD)** — Analyzes customizations in the HR Core Case and Task tables, tracking field-level changes and promoting data completeness for critical fields. The assessment provides insights into historical HR Core cases, including field population percentages, to enhance data accuracy in HRSD processes. Additionally, the feature identifies estimated remediation efforts required and reports the languages used within the instance.

> **Note:** Additional configuration is needed to run the HRSD assessment successfully. For more information, see Configure the Now Assist Readiness Evaluation guided setup.

## Functionalities

### Users

| User  | Description                                                                                                                   |
| ----- | --------------------------------------------------------------------------------------------------------------------------- |
| Admin | Admins use the Now Assist Readiness Evaluation app to prepare for implementing generative and agentic AI features in Now Assist. |

### Benefits

| Benefit | Feature | Users |
| ------- | ------- | ----- |
| Run scheduled jobs for applicable agentic and generative AI Now Assist products from a single assessment job. | Run the GenAI/AgenticAI Assessment scheduled job | Admins |
| Review an overall dashboard of your issues before implementing agentic and generative AI Now Assist. | Using Now Assist Readiness Evaluation dashboard | Admins |
| View your overall go or no-go status to implement Now Assist generative AI skills or agentic AI agents, and view the go or no-go status' issues categorized by percentage. | Assessing readiness status | Admins |
| Review summary information of overall implementation readiness. | Reviewing your Now Assist assessment and Reviewing your agentic AI assessment | Admins |
| Improve the gaps for implementation by using the hyperlinks found in the assessments to fix issues. Direct hyperlinks to records and tables make it easier to validate, investigate, or act without switching contexts. | Reviewing your Now Assist assessment and Reviewing your agentic AI assessment | Admins |
| Receive an estimated remediation effort of development work days to fix issues before implementation. | Reviewing your Now Assist assessment and Reviewing your agentic AI assessment | Admins |

### Related topics

- Now Assist
- Now Assist AI agents

## Instructions / Procedures

This topic is an introductory and conceptual overview; it does not contain step-by-step procedures. To get started, choose one of the **Explore**, **Configure**, or **Use** tiles.

### What to explore next

To learn more about configuring and using the Now Assist Readiness Evaluation app, see:

- Configuring Now Assist Readiness Evaluation
- Using Now Assist Readiness Evaluation

## Figures, Diagrams & Screenshots

**Figure (p.1054):** Page header screenshot showing the ServiceNow logo. The remainder of the page is text covering the end of the prior "Check compatibility of Subflow or Action" procedure and the introductory "Now Assist Readiness Evaluation" heading, which states the app helps prepare your organization for implementing agentic AI for ITSM and CSM, Now Assist for five products, or both, and prompts the reader to "Choose one of these tiles to get started." No substantive graphic appears on this page beyond the logo.

**Figure (p.1055):** Three side-by-side getting-started tiles laid out across the top of the page, each with an icon above descriptive text:
- **Explore** (magnifying-glass / search icon) — "Learn about the Now Assist Readiness Evaluation app."
- **Configure** (gear / settings icon) — "Run scheduled jobs and configure the app through the Now Assist Readiness Evaluation guided setup."
- **Use** (presentation / chart icon) — "Learn about how to use the Now Assist Readiness Evaluation dashboards and assessments to prepare for implementing agentic AI, Now Assist, or both."
Below the tiles is a highlighted blue "Important" callout box containing the four availability bullet points (in-country SKUs/KB1584492, FedRAMP/IL5/IRAP/KB0743854, regional availability, and Regulated Markets/KB2593939), followed by the AI limitations, Data processing, and Data collection legal text and the "Related topics" links (Now Assist, Now Assist AI agents). The tiles are navigational/decorative entry points to the Explore, Configure, and Use content.

**Figure (p.1056):** Text-only documentation page titled "Exploring Now Assist Readiness Evaluation" and "Now Assist Readiness Evaluation overview." Inline within the body text are two small UI tab icons: a labeled "agentic_AI" tab icon (indicating where agentic AI solution information appears) and an unlabeled tab icon (indicating where generative AI / Now Assist solution information appears). The page lists and describes the agentic AI solutions (ITSM, CSM) and begins the generative AI products list (Now Assist for AI Search, Now Assist for Virtual Agent). No screenshots or dashboards appear on this page.

**Figure (p.1057):** Text-only page continuing the generative AI product descriptions (ITSM, CSM, HRSD) and presenting two data tables: the "Users" table (single row: Admin) and the "Now Assist Readiness Evaluation benefits" table mapping each benefit to its feature and the Admins user. No screenshots or diagrams appear on this page beyond the ServiceNow header logo; the visuals are the rendered tables described in the Functionalities section above.
