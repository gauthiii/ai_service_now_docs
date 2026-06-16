### Now Assist Skills in the Platform Workflow


Available skills by workflow (continued)
Workflow Product Available skills
•Supplier summarization
•Supplier performance summarization
Finance & Supply Now Assist for Sourcing
•Negotiation summarization
Chain and Procurement
Operations (SPO) •Procurement case summarization
•Purchase requisition summarization
•Sourcing event summarization
•Sourcing request summarization
App Engine Now Assist for App Custom app record summarization
Engine
Impact Impact
•Jumpstart Your Now Assist for Creator
The Impact workflow •Jumpstart Your Now Assist in Document
contains technical Intelligence
accelerators that can
•Jumpstart Your Now Assist in Virtual Agent
help you get started more
quickly with some Now •Jumpstart Your Now Assist Skill Kit
Assist features.
Vault Now Assist for Vault
•Check role access
•Generate custom data pattern
•Schedule Data Discovery job
Other Now Assist for Zero Copy
•ERP data discovery
Connector
•ERP data query
Now Assist skills in the Platform workflow
Most Now Assist generative AI products include skills in the Platform workflow, such as product
navigation. Some Now Assist products include skills for the conversational user and platform
experience, as well as knowledge article recommendations.
Auto activation of generative AI platform skills
Starting with the Zurich Patch 4 release, some generative AI platform skills for Now Assist will be
active by default. This is applicable for commercial and regulated market customers.
•New users: When you install the Now Assist plugins, the related Now Assist skills will be turned
on automatically.
•Existing users: When you upgrade the Now Assist plugins, any unused skill will turn on.
© 2026 ServiceNow, Inc. All rights reserved. 58
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **Workflow** | **Product** | **Available skills** |
|---|---|---|
|  |  | •Supplier summarization •Supplier performance summarization |
| Finance & Supply Chain | Now Assist for Sourcing and Procurement Operations (SPO) | •Negotiation summarization •Procurement case summarization •Purchase requisition summarization •Sourcing event summarization •Sourcing request summarization |
| App Engine | Now Assist for App Engine | Custom app record summarization |
| Impact | Impact The Impact workflow contains technical accelerators that can help you get started more quickly with some Now Assist features. | •Jumpstart Your Now Assist for Creator •Jumpstart Your Now Assist in Document Intelligence •Jumpstart Your Now Assist in Virtual Agent •Jumpstart Your Now Assist Skill Kit |
| Vault | Now Assist for Vault | •Check role access •Generate custom data pattern •Schedule Data Discovery job |
| Other | Now Assist for Zero Copy Connector | •ERP data discovery •ERP data query |

1.If you have installed the plugins but never configured, activated or changed roles for a skill,
any skill with 'Default On' status will be enabled individually, after the upgrade.
2. If you have modified any role for a skill, turned it off and then back on, that skill will stay
turned off after the upgrade; maintaining your last known selection.
Some skills, such as the Group Action Framework (GAF) skills, support Platform functionality and
may require specific configuration.
Article optimization
Article optimization skill in ServiceNow AI Platform provides recommendations for improving
the quality and health of knowledge articles, providing actionable feedback to authors and
managers. The recommendations for knowledge articles become available after you activate the
Article Optimization skills in Now Assist Admin.
Article ptimization is a Platform skill that is enabled by the admin from the Knowledge feature
card. The skill allows agents and authors to review and use article optimization recommendations
to improve the quality and health of their knowledge articles.
For more information, see Review and optimize articles using Article Optimization .
Catalog item form slot-fill
With the catalog item form slot-fill skill, Now Assist can automatically complete catalog item forms
based on what users search for.
For instance, if requester looks up a standard laptop with 256 GB storage in silver color, the
resulting form will have those specifications already filled in provided they’re part of the form.
Requester can quickly review these pre-filled forms, making requests faster and more efficient.
To enable this feature, activate the catalog item form slot-fill skill so that requesters see their
search criteria reflected in the catalog item request forms. As soon as requesters searches for an
item, relevant fields in the form are populated with their search information, minimizing repetitive
entry and streamlining the request process.
Pre-filled fields show AI icons to help users validate values populated by Now Assist.
Note: Order guides, as well as the following variables, are not supported:
•MRVS (Multi-Row Variable Sets)
•Custom and custom with labels
•Attachments
•Masked
•Break
•Container
•UI page
•HTML
Now Assist Conversational Help
This skill uses Generative AI application capabilities to provide answers to the questions on the
Now Assist panel.
https://player.vimeo.com/video/1088792812?
h=bceb334712&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479.
© 2026 ServiceNow, Inc. All rights reserved. 59
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

Important: This Now Assist skill is turned on by default. The skill will be automatically
available to appropriate role users for the application. For more information, see Now Assist
skills, agents, and agentic workflows on by default.
The Now Assist Conversational Help skill displays as Get Help on the Now Assist panel.
Note: The Get Help feature is available as a part of Now Assist entitlements and no new
subscription is required. The feature is enabled by default and you can turn it off in the Now
Assist Admin Settings. The ServiceNow Now LLM Service (Large Language Model) is the
default model provider for this Now Assist skill to retrieve precise answers to the users'
questions.
You can ask your question in two ways:
•Select Get Help skill and submit a query to use the help option in the Now Assist panel.
•Submit your query directly in the Now Assist panel. It will perform discovery and find the most
appropriate skill among the listed, based on the keywords you entered. This discovered skill is
used to retrieve answers for your queries.
Note: The available skills displayed in the Now Assist panel can be customized in
consultation with the integration teams.
How Conversational Help works
Your query goes through the following steps to retrieve the best response.
1.AI search
The query is be sent to a central ServiceNow instance, where AI Search will search the
knowledge table that stores content from product doc content.
We use Instance Data Replication (IDR) that synchronizes product documentation content
from Now Support instances.
Note: Multiple central ServiceNow instances are deployed across three regions: US
East or US West, EMEA, and APJC.
2. The top matching chunks (or records) along with the user’s query, are sent to the Now Assist
Q&A Genius Result configuration to generate a meaningful, contextual answer.
3. Re-ranking
The Now Assist Q&A, an out of box (OOB) capability, re-ranks the retrieved chunks to ensure
better relevance.
4.Cache lookup
◦If the user query exists in the cache, the pre-stored answer is returned.
◦If the query is not cached, the query and re-ranked chunks are sent to Now LLM to generate
a meaningful answer.
The Now LLM retrieves the most relevant result from https://www.servicenow.com/docs/ portal
and displays it in the same panel.
Note: Effective from this release, the query will retrieve results based exclusively on the
release version of the user's current instance. This enhancement is integrated into the
query process to ensure the delivery of precise results that reflect the latest updates and
features.
© 2026 ServiceNow, Inc. All rights reserved. 60
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

For more information, see Fetch end points in Now Assist Conversational Help skills.
Now Assist extract information from documents
The extract information from documents skill allows you to use Now Assist predictions to extract
information from document and image files.
Now Assist uses generative AI capabilities to extract values from the document based on the
fields, tables, and questions defined in the skill’s use case. The extracted information is turned
into structured data that can be used in the platform.
Agents can use the Document Intelligence workspace to review and confirm the extracted
information.
© 2026 ServiceNow, Inc. All rights reserved. 61
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.


> **[Screenshot: Now Assist Panel — Conversational Help opening screen]**
> The Now Assist slide-out panel showing the AI greeting: "Hi! How can I help you with your work today?" with suggested actions: generate a kb article, Generate resolution notes, Get Help, Suggest configuration items for a change. Six quick-action buttons: Generate KB Article, Generate resolution notes, Summarize a record, Summarize conversation, Suggest configuration items for a change, and **Get Help** (highlighted in blue). Text input field "Reply to Now Assist..." at the bottom with a send button.


Extracted information in the Document Intelligence workspace
For more information, see Review extracted information in the Document Intelligence workspace.
Knowledge content recommendation
Knowledge generative AI skills on the ServiceNow AI Platform provides recommendations for
editing a knowledge article. Once activated, this skill is available on the Now Assist context
menu.
The Now Assist Knowledge content recommendation is a Platform skill that is enabled by the
admin from the Knowledge feature card. The skill allows agents and authors to use the Now
Assist context menu to elaborate and shorten content in a knowledge article.
The Now Assist context menu in Knowledge Management
For more information, see Edit an article using the Now Assist context menu .
Potential knowledge gaps
The Potential Knowledge Gap helps in finding missing or incomplete knowledge coverage by
analyzing service interactions. Gap recommendations become available after you activate the
Knowledge Gaps skills in Now Assist Admin.
The Knowledge Gaps feature (also known as Potential Gaps) helps knowledge managers
and service teams discover missing or insufficient knowledge articles by analyzing service
case and incident patterns. When the relevant skills are activated, Now Assist generates gap
recommendations to guide the creation or improvement of knowledge content.
For more information, see Manage potential knowledge gaps
© 2026 ServiceNow, Inc. All rights reserved. 62
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.


> **[Screenshot: Document Intelligence workspace — Invoice Q&A]**
> The Document Intelligence workspace with a CPB Software (Germany) GmbH invoice to Musterkunde AG for WMACCESS Internet services (Feb 1–29, 2024). Now Assist panel summary: basic fee for wmView €130.00, various transaction fees, total €381.12, VAT 19% = €72.41, gross total €453.53. "Summarise the document" button and text input visible. Disclaimer: "Some answers generated by AI. Be sure to check for accuracy."

> **[Screenshot: Now Assist context menu in Knowledge Management]**
> The ServiceNow Knowledge article editor (KCS Article KB0010583 v0.01) with a floating Now Assist context menu over selected text, offering two options: **Elaborate** (expand the content) and **Shorten** (condense the content).


Navigation
Use the navigation skill in Now Assist to take you where you want to go on the ServiceNow AI
Platform.
Overview of navigation
Navigation is a skill in the Now Assist panel that handles record search requests during a chat.
When you ask for records or tables in plain language Now Assist shows you links in the chat to
take you to the best match to your request. For example, you could enter Show me incident
records.
In the following figure, the user entered navigate me to incidents in the Now Assist
panel. Now Assist responds with a link to the Incidents table.
Navigation query and response in the Now Assist panel
When you click the link, the list of all records in the Incidents table displays.
Navigating to the Incidents table from the Now Assist panel
© 2026 ServiceNow, Inc. All rights reserved. 63
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.


> **[Screenshot: Navigation — Query and response]**
> ServiceNow Admin Home dashboard with the Now Assist panel open. User typed "navigate me to incidents." Now Assist responded: "This is where you can view the records" with a **View Incident** button. Admin home shows open incidents and open request items widgets (both showing "No data available").

> **[Screenshot: Incidents table navigation result]**
> The full Incidents list view (All > Keywords = emails) showing columns: Number, Opened, Short description, Caller, Priority, State, Category. Sample records: INC0010253 (Language issue, Abraham Lincoln, In Progress, Software), INC0010248 (Order stuck in load status, Alejandra Pranatt, New, Inquiry/Help), INC0009005 (Email server is down, David Miller, Critical, New, Software), and others. Now Assist panel retains conversation history on the right.


Refining your results
You can refine your results further by using more detailed requests. If you enter Show me all
incident records whose status is Complete, Now Assist shows you only the
records in the table with a Complete status.
In the following example, the user asks for all P1 incidents that are in the New state.
A refined query of the Incidents table
The number of results is based on how many potential results Now Assist finds in response
to your request. If Now Assist finds more than 10 results, the list is paginated. In the following
example, Now Assist finds two possible tables: the Catalog Item table and the Catalog table.
Multiple table results in the Now Assist panel
If Now Assist does not understand your request, you receive an error message asking you to
rephrase your request. You can also choose to navigate to a "best guess" based on your previous
request.
© 2026 ServiceNow, Inc. All rights reserved. 64
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.


> **[Screenshot: Refined query — P1 Incidents in New state]**
> Incidents list filtered to Priority=1-Critical AND State=New: INC0009005 (Email server is down, David Miller, Critical, New, Software) and INC0007001 (Employee payroll application server is down, David Miller, Critical, New, Hardware). Now Assist panel shows user asked "show me all P1 incidents whose state is new" with a resulting View Incident link.

> **[Screenshot: Multiple table results]**
> Now Assist responding to "Show me active catalog items" with: "There are 2 potential tables matching what you are looking for. Which table would you like to view?" Two buttons: **Catalog Item: sc_cat_item** and **Catalog: sc_catalog**.


Rephrase request message in the Now Assist panel
Now Assist in Standard Ticket Page
The Now Assist in Standard Ticket Page skill allows you to display summaries generated by Now
Assist, providing overviews of recent activities and ticket details.
When this skill is active, the standard ticket page on the Service Portal displays a Summarize
button. If requesters want to see the ticket activity and a summary of information generated by
Now Assist, they can select the Summarize button.
The Summarize button appears when at least one field is configured. If no field values are
configured, the button does not appear, regardless of whether the Now Assist in Standard Ticket
Page skill is active.
Requester Approval Checklist skill
®
The Requester Approval Checklist skill in the ServiceNow AI Platform generates a structured
checklist by mapping real-time request data against your organization’s knowledge articles.
Important: This Now Assist skill is turned on by default. The skill will be automatically
available to appropriate role users for the application. For more information, see Now Assist
skills, agents, and agentic workflows on by default.
This skill is available within Now Assist Agents for Requester v3.1 and is designed to provide
instant, data-backed decision support across in-product, agentic, and workflow experiences.
The skill uses information from the following sources to promote accuracy:
Knowledge articles
Defines the evaluation criteria based on your company policy.
System data
Fetches requester profiles and historical data from ServiceNow.
Approval request
Analyze the details submitted in a live request.
Requester Approval Checklist structure
The output is presented in a two-step format: Criteria (what is required) and Reason (why it
passed, failed, or has missing information). Each item has one of the following statuses: Met, Not
met, or Unknown.
© 2026 ServiceNow, Inc. All rights reserved. 65
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.


> **[Screenshot: Rephrase request error message]**
> Now Assist panel showing: "Sorry, I am not able to generate proper filters based on your request. Do you want to rephrase your request to try again or directly navigate to the table list to add filters on your own?" Two action buttons: **Rephrase request** and **Navigate to table list**. Incidents list view visible in the background.


Note: All referenced knowledge base articles are provided as links at the end of the
checklist for easy verification.
Key skill considerations
Integration
The skill is built for workflows and agentic experiences, but doesn't support follow-
up questions and answers.
Decision support
The skill provides information only. It doesn't perform actions like Approve, Reject,
or Comment.
Flexibility and control
The Requester Approval Checklist respects the approval configuration to provide
flexibility and control.
For more information, see Platform Approval assistance AI agent and Configure Service Portal
Approval Configuration record .
Smart Documents skill
Accelerate document insights with instant summaries, interactive Q&A, and FAQs using Now
Assist in Document Management.
Smart Documents Skill overview
The Smart Documents skill provides a concise summary of the document associated with a
workflow, along with interactive Q&A and FAQs, enabling you to quickly understand the content,
explore key insights and get answers to specific questions.
You can summarize a document in a workspace, ask interactive questions, and view FAQs.
To learn how, see Generate summary and ask questions using Now Assist in Document
Management
The following diagram shows that by using the Smart Document skill, you can quickly get insights
from a document, such as a white paper, report, policy, contract, or case file.
© 2026 ServiceNow, Inc. All rights reserved. 66
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.


> **[Screenshot: Smart Documents skill — Invoice summary in Now Assist panel]**
> Document Management workspace showing a CPB Software invoice (sample-invoice(2).pdf, page 1 of 3) with line items: Basic Fee services, Basic Fee additional user accounts, Basic Free wmPos, Change of user accounts, and Transaction Fees T2–T9 (all €0.00). Now Assist panel displays an AI-generated document summary with billing period, service details, and calculated totals. Disclaimer: "Some answers generated by AI. Be sure to check for accuracy."


Availability
Now Assist Products and Workflows
Workflow Product
Technology Now Assist for IT Service Management (ITSM)
Customer
Now Assist for Customer Service Management (CSM)
Now Assist for Field Service Management (FSM)
Employee Now Assist for HR Service Delivery (HRSD)
Governance,Risk, and Compliance Now Assist for Third-party Risk Management (TPRM)
Now Assist Q&A Genius Results
The Now Assist Q&A Genius Results skill enables users to get answers to their questions from
knowledge articles, external sources, and uploaded files directly in the Now Assist panel.
Overview of Now Assist Q&A Genius Results
Now Assist Q&A Genius Results answers your questions in the Now Assist panel using content
from knowledge base articles, external sources, such as Microsoft SharePoint, Google Drive,
and Confluence Cloud, and files you upload. You can also attach images or documents to get
answers grounded in that content. Answers are summarized from the most relevant content
across one or more sources, so you get a single, consolidated response instead of a list of
articles to read through. Each response shows the source so you can refer back to the original
article or document. If the skill can't find a relevant answer, it returns a no-result response instead
of a generic reply.
The skill supports multi-turn conversations by retaining your conversation history so that follow-
up questions are answered in the context of what you previously asked without re-uploading your
file or repeating yourself.
The skill is part of the Platform workflow and is turned on by default. To turn it off, navigate to Now
Assist Admin > Now Assist Skills > Platform and select Deactivate skill on the skill card.
Use cases
Now Assist Q&A Genius Results is useful in the following use cases:
•Search across knowledge articles and external sources such as SharePoint or Confluence to
get a single consolidated answer.
•Ask follow-up questions to build on a previous answer within the same session, without
repeating context.
•Upload a screenshot of an error and ask Now Assist what it means and how to resolve it,
without describing the image manually in text.
•Upload a PDF crash log or SLA document and ask questions about its contents, without
reading through the full document.
© 2026 ServiceNow, Inc. All rights reserved. 67
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **Workflow** | **Product** |
|---|---|
| Technology | Now Assist for IT Service Management (ITSM) |
| Customer | Now Assist for Customer Service Management (CSM) Now Assist for Field Service Management (FSM) |
| Employee | Now Assist for HR Service Delivery (HRSD) |
| Governance,Risk, and Compliance | Now Assist for Third-party Risk Management (TPRM) |

© 2026 ServiceNow, Inc. All rights reserved. 68
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

Supported file types and limits
You can upload one file per session. The following file types are supported:
•Images: PNG, JPG (maximum 10 MB)
•Documents: PDF, DOCX (maximum 10 MB)
Now Assist agentic workflows
You can customize Now Assist agentic workflows to meet the needs of your users in different
workflows. For example, you can use agentic AI to help resolve tasks, execute routine but
variable procedures, and investigate root causes or analytical trends.
Agentic workflows overview
Agentic workflows use multiple AI agents to achieve specific outcomes. Different workflows
offer different available tasks. Many agentic workflow templates are available for you to activate,
duplicate, or customize. For more information, see Activate an agentic workflow template and
Duplicate an agentic workflow.
For more information about the in-product agentic AI experience, see In-product agentic AI. You
can create UI actions for your agentic workflows in AI Agent Studio. Open the agentic workflow,
navigate to the Select channels and access step in the guided setup, and create a UI action.
Workflow and product agentic workflows
The following table describes the available AI agents agentic workflows that are included in Now
Assist applications.
Available agentic workflows by product
Product Available agentic workflows
Now Assist for Configuration Management
•Create configuration item
Database (CMDB)
•Provide advice on CMDB governance
•Search CMDB
Now Assist in Contract Management
•Conversational contract search and
insights
•Manage contract repository
Now Assist for Creator Create a theme using Now Assist
Now Assist for Customer Service
•Accelerate complaint case handling
Management (CSM)
•AI voice agent in CSM
•Provide Customer 360 insights
•Triage cases
Now Assist for Enterprise Architecture (EA) Generate enterprise architecture diagram
© 2026 ServiceNow, Inc. All rights reserved. 69
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **Product** | **Available agentic workflows** |
|---|---|
| Now Assist for Configuration Management Database (CMDB) | •Create configuration item •Provide advice on CMDB governance •Search CMDB |
| Now Assist in Contract Management | •Conversational contract search and insights •Manage contract repository |
| Now Assist for Creator | Create a theme using Now Assist |
| Now Assist for Customer Service Management (CSM) | •Accelerate complaint case handling •AI voice agent in CSM •Provide Customer 360 insights •Triage cases |
| Now Assist for Enterprise Architecture (EA) | Generate enterprise architecture diagram |