# ServiceNow AI Implementation


You can use Now Assist in Document Intelligence skills to extract information and find answers to
questions about documents.
Task Intelligence
Achieve faster response and task-solving times for your Agents, by using Task Intelligence. This
tool lets you engineer ML solutions that handle data and track the efficacy of those solutions.
Build, train, edit, and retrain machine-learning models in the Admin Console, and export them for
use across the ServiceNow AI Platform. Follow up with the Analytics dashboard, where you can
track your models' performance and effects on your business, and determine which predictions
are best for future reuse.
®
ServiceNow AI implementation
Getting ready to implement Now Assist is more than just installing plugins—it’s about laying
the groundwork for a seamless, intelligent experience across your workflows. Whether
© 2026 ServiceNow, Inc. All rights reserved. 14
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.


> **[Screenshot: Document Intelligence workspace — Now Assist extraction]**
> The Document Intelligence workspace showing a purchase order (Alectri brand) being processed. The left panel shows the original invoice with Apple Black Monitor line items. The right "Document Q&A" panel shows Now Assist auto-extracted: Vendor name, Order Form Total ($862,224.00), Order Form Number (GF-2023M-168), and a yes/no question about form date vs quote expiration. Banner: "Review the fields and/or the tables before submitting the task. Results predicted by Now Assist — be sure to review AI generated results for accuracy."

> **[Screenshot: Task Intelligence Admin Console]**
> Header: "Improve task creation with machine learning." Metrics: "Case sentiment" model, 49 predictions in last 7 days, 111 total (based on 170 new cases). Models table lists: Priority Model (Categorization, Training Error), Case sentiment (Sentiment, Deployed 06/22/2022), Demo with RA (Categorization, Deployed 06/15/2022), General Case Prediction (Categorization, Deployed Today). Right sidebar explains ML model basics.


you're enabling conversational catalogs, automating content generation, or enhancing user
interactions, a few key steps will ensure your data is ready, your applications are prepared, and
your organization's AI policy is in alignment with your implementation.
Get started
Now Assist overview AI governance Data readiness
Learn about the Learn about the Learn how to prepare
applications and features importance of AI your instance data
that make up the Now governance to ensure for Now Assist.
Assist experience. responsible use, regulatory
compliance, and alignment
with enterprise goals.
Application readiness Resolve common issues
Ensure that your instance Address issues or
is ready to take advantage gaps in your Now
of Now Assist by preparing Assist configuration.
Platform applications.
Additional implementation information is available on Now Create .
For additional Now Assist resources, see Additional resources for AI products and solutions.
© 2026 ServiceNow, Inc. All rights reserved. 15
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **Now Assist overview Learn about the applications and features that make up the Now Assist experience.** | **AI governance Learn about the importance of AI governance to ensure responsible use, regulatory compliance, and alignment with enterprise goals.** | **Data readiness Learn how to prepare your instance data for Now Assist.** |
|---|---|---|
| Application readiness Ensure that your instance is ready to take advantage of Now Assist by preparing Platform applications. | Resolve common issues Address issues or gaps in your Now Assist configuration. |  |

| **** |
|---|
|  |

Important:
•Not all model providers are available for customers with in-country SKUs, and some Now
Assist products/features are currently unavailable for in-country customers. For more
information, see the KB1584492 article in the Now Support Knowledge Base. Be sure to
check for model provider availability updates in future releases.
•Some Now Assist products/features are currently unavailable for customers in the
FedRAMP, NSC DOD IL5, or Australia IRAP-Protected data centers, self-hosted
customers, or in other restricted environments. For more information, see the
KB0743854 article in the Now Support Knowledge Base. Be sure to check for availability
updates in future releases.
•Some Now Assist products/features are currently available only for customers in some
regions. Be sure to check for availability updates in future releases.
•Some AI products and skills are not available in Regulated Markets. For more information,
see KB2593939: Regulated Markets AI Products/Skills Not Available . Be sure to check
for availability updates in future releases.
AI limitations
This application uses artificial intelligence (AI) and machine learning, which are rapidly evolving fields of study that generate predictions based on patterns
in data. As a result, this application may not always produce accurate, complete, or appropriate information. Furthermore, there is no guarantee that this
application has been fully trained or tested for your use case. To mitigate these issues, it is your responsibility to test and evaluate your use of this application for
accuracy, harm, and appropriateness for your use case, employ human oversight of output, and refrain from relying solely on AI-generated outputs for decision-
making purposes. This is especially important if you choose to deploy this application in areas with consequential impacts such as healthcare, finance, legal,
employment, security, or infrastructure. You agree to abide by ServiceNow’s AI Acceptable Use Policy , which may be updated by ServiceNow.
Data processing
This application requires data to be transferred from ServiceNow customers' individual instances to a centralized ServiceNow environment, which may be located
in a different data center region from the one where your instance is, and potentially to a third-party cloud provider, such as Microsoft Azure. This data is handled
per ServiceNow's internal policies and procedures, including our policies available through our CORE Compliance Portal .
Data collection
ServiceNow collects and uses the inputs, outputs, and edits to outputs of this application to develop and improve ServiceNow technologies including ServiceNow
models and AI products. Customers can opt out of future data collection at any time, as described in the Now Assist Opt-Out page.
Now Assist organization and tools
The Now Assist experience includes generative AI skills, agentic AI, and conversational user
engagement layer. A good AI experience depends on quality data and a coherent AI policy that
functions as its guiding star. AI Search capabilities and other tools help connect the pieces.
The following infographic illustrates the components of the Now Assist experience. You can
think of each area as a layer, with AI policy as the basis for your implementation. Data plays an
important role, since poor data will lead to poor outcomes, and the search experience drives
both generative and agentic AI capabilities. The conversational engagement layer allows your
users to communicate with AI and perform tasks and self-serve more easily.
© 2026 ServiceNow, Inc. All rights reserved. 16
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

Components of the Now Assist experience
AI policy
AI governance is defined by your organization and then implemented on the platform using
AI Control Tower. AI Control Tower is designed to scale with your organization’s AI maturity. It
enables end-to-end life cycle management of AI agents and models, from intake and evaluation
to deployment and optimization. It also acts as a bridge between governance committees and
implementation teams, ensuring that policy decisions are translated into technical configurations
and operational controls. The platform includes the AI Risk and Compliance application, which
comes with pre-built content aligned to the EU AI Act and NIST AI Risk Management Framework
(AI RMF), helping organizations accelerate compliance and implement responsible AI practices
from day one. For more information, see AI governance for Now Assist on the ServiceNow AI
Platform.
For real-time guardrail enforcement for AI interactions, you can use Now Assist Guardian to
monitor and mitigate risks related to offensive content, sensitive topics, and security threats in
generative AI outputs. Admins can configure these guardrails directly in the Now Assist Admin
console, and logs are available to track detection events and guide decisions about blocking or
escalation.
Roles and responsibilities:
AI steward [sn_ai_governance_ai_steward]
The AI steward role manages the platform's data assets and AI capabilities,
ensuring data quality, integrity, and ethical use. The steward also implements
governance policies to maintain compliance, security, and responsible AI practices
across ServiceNow applications and workflows.
AI asset/product owner [ sn_ai_asset_mgmt.ai_asset_owner]
The AI asset (or product) owner is responsible for driving the development and
delivery of AI-powered products, ensuring alignment with business goals and user
needs. They define product vision, manage feature prioritization, and translate
business requirements into technical deliverables.
AI Risk and Compliance Manager [sn_grc_ai_gov.ai_risk_and_compliance_manager]
The AI Risk and Compliance Manager is tasked with identifying, assessing,
and mitigating risks related to AI use within the enterprise. This role ensures AI
compliance with laws, regulations, and internal standards while addressing issues
such as bias, privacy, and transparency.
Now Assist Admin [sn_nowassist_admin.nsa_admin]
© 2026 ServiceNow, Inc. All rights reserved. 17
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.


> **[Diagram: Components of the Now Assist Experience]**
> A horizontal five-column component diagram showing the Now Assist stack layers:
> | Layer | Components |
> |---|---|
> | **Policy** | AI Governance → AI Control Tower, Now Assist Guardian |
> | **Data** | Data Management → Now Assist Data Kit, Knowledge Graph, Now Assist Readiness Evaluation |
> | **Content** | AI Search → Now Assist in AI Search, External Content Connectors |
> | **AI skills + Agents** | AI agents → AI Agent Studio, MCP Client, MCP Server; Generative AI skills → Now Assist Admin console, Now Assist Skill Kit |
> | **User engagement** | Conversational AI → Now Assist in Virtual Agent, Assistant Designer |


The Now Assist admin is responsible for enabling and managing the Now Assist
Guardian guardrails within the Now Assist Admin console. This includes configuring
detection settings for offensiveness, prompt injection, and sensitive topics, as well
as monitoring logs to assess harmful or malicious AI outputs. The admin can toggle
guardrails on or off, choose actions like “Block and Log,” and tailor the configuration
to match organizational risk tolerance and use cases.
For more information about these tools, see:
•AI Control Tower
•AI Risk and Compliance
•Now Assist Guardian
Data management
You know the old saying, "Garbage in, garbage out?" Poor, incomplete, or unstructured data can
lead to poor AI outcomes. To prepare your data for AI implementation, see Data readiness for
implementing Now Assist on the ServiceNow AI Platform.
Now Assist provides several tools to help you manage data and provide user context on
your instance. The Now Assist Data Kit helps organizations manage AI training data on their
ServiceNow instance. It provides a centralized workspace to curate, generate, cleanse, and
evaluate datasets, including importing data from tables, adding ground truth, and creating
derived datasets. It supports synthetic data generation—up to 1,000 records at a time—and
includes tools to anonymize sensitive information for privacy compliance. Integrated with the
Now Assist Skill Kit, it enables teams to test custom AI skills and measure performance.
Knowledge Graph makes AI in Now Assist more personal by using structured enterprise data
to tailor responses to each user. It helps AI understand context, such as a user’s role, location,
or assigned assets, making answers more relevant and accurate. It also supports intelligent
slot-filling, automatically pulling in known information to streamline conversations and reduce
repetitive questions. This results in faster, more personalized, and trustworthy AI interactions.
Roles and responsibilities:
Now Assist Data Kit admin [sn_data_kit.admin]
This role is required to create, update, and publish datasets in Now Assist Data Kit.
Knowledge Graph admin [kg_admin]
This role is required to design, manage, and audit Knowledge Graph schemas,
including configuring nodes (tables), properties (columns), and relationships.
For more information about these tools, see:
•Now Assist Data Kit
•Knowledge Graph
•Now Assist Readiness Evaluation
Internal and external content search
Now Assist in AI Search is the primary tool used to find content on your instance, whether it's in
the form of knowledge articles, Service Catalog items, system users, Knowledge Graph schemas,
or content in enhanced chats using Now Assist in Virtual Agent.
Now Assist in AI Search is a plugin that enhances your existing AI Search configuration, adding
support for Now Assist Genius Result answers.
© 2026 ServiceNow, Inc. All rights reserved. 18
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

You can expand the amount of content available to Now Assist in AI Search by using External
Content Connectors. With this tool, AI Search applications can search content and metadata
from external content repositories such as Atlassian Confluence Cloud and Microsoft SharePoint
Online.
Roles and responsibilities:
AI Search admin [ais_admin]
This role is required to manage configuration settings for the AI Search application.
External Content Connectors admin [sn_ext_conn.xcc_admin]
This role is required to manage configuration and crawl settings for the External
Content Connectors application.
For more information about these tools, see:
•AI Search
•Now Assist in AI Search
•External Content Connectors
Generative AI skills
Now Assist product plugins provide workflow-specific, generative AI skills that are tailored to
specific use cases. For example, a skill might summarize a customer chat, suggest next steps in a
workflow, or generate resolution notes for a task. For a list of available skills by product, see Now
Assist skills.
Use the Now Assist Admin console to install and configure Now Assist plugins, as well as perform
the following tasks:
•Set up and configure skills to align with your business processes.
•Monitor and analyze usage, including adoption rates and performance metrics across the
platform.
•Manage provider policies, data handling rules, and access controls.
•Turn on and configure the Now Assist panel.
•Manage large language models (LLMs).
•Configure translation for Now Assist.
If you need to customize or adapt existing skills, you can use the Now Assist Skill Kit to build,
customize, and test generative AI skills that are tailored to your organization’s workflows.
With features like a prompt editor, visual builder, and evaluation tools, it helps you fine-tune
performance and ensure quality. It also integrates with the Now Assist Data Kit and Now Assist
Guardian for testing and governance, making it a flexible and secure way to extend AI across the
ServiceNow platform.
Roles and responsibilities:
Now Assist Admin [sn_nowassist_admin.nsa_admin]
This role is required to install Now Assist plugins, activate skills, and configure Now
Assist preferences and settings.
Skill Kit admin [sn_skill_builder.admin]
This role is required to create, update, and publish skills in Now Assist Skill Kit.
For more information about these tools and features, see:
© 2026 ServiceNow, Inc. All rights reserved. 19
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

•Overview tab in Now Assist Admin
◦Now Assist panel
◦Manage AI models
◦Analyzing Now Assist performance
◦Multilingual service for Now Assist
◦Now Assist for Mobile
•Now Assist Skill Kit
Agentic AI
In an agentic AI system, autonomous agents perform complex tasks by reasoning, planning,
and executing actions across multiple steps. These agents are not just reactive; they can
break down goals, make decisions, and coordinate with other agents or systems to complete
workflows. In AI Agent Studio, AI agents and agentic workflows are built to handle tasks such as
resolving incidents, managing requests, or navigating service catalogs using generative AI and
orchestration logic. For a list of available agentic workflows by product, see Now Assist agentic
workflows.
Use AI Agent Studio to perform the following tasks:
•Build or modify AI agents and agentic workflows using intuitive list views and guided setup
tools.
•Simulate tasks and view execution logic to refine agent behavior.
•Access execution logs and version control to track performance and changes.
•Use the Settings page to enable Now Assist Guardian for runtime safety, including detection of
offensive content and prompt injection.
•Use the AI Agent Analytics dashboard to view usage stats, efficiency gains, and execution
volume to help measure value.
The Model Context Protocol (MCP) client enables you to access the Model Context Protocol
tools that are hosted externally and published using an MCP Server. MCP facilitates
communication between an AI host application (like AI Agent Studio) and one or more MCP
servers that expose specific capabilities such as tools.
The MCP Server Console is a tool for administrators to set up and manage Model Context
Protocol (MCP) servers. These servers provide AI applications with access to ServiceNow
features like incident lookups, case summaries, and workflow actions. The console lets you
choose which capabilities to make available, ensuring everything stays secure and compliant.
Then, from an MCP client, users can request information from the server and automate
functionality using the available tools and data that the server returns.
Roles and responsibilities:
AI Agent Admin [sn_aia_admin]
This role is required to create, manage, update, test, and delete AI agents and
agentic workflows.
MCP Client Admin [sn_mcp_client.admin]
This role is required to administer the MCP client in AI Agent Studio. It is inherited
from the AI Agent Admin [sn_aia.admin] role.
MCP Server administrator [sn_mcp_server.admin]
This role is required to administer the MCP Server Console.
© 2026 ServiceNow, Inc. All rights reserved. 20
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

For more information about these tools, see:
•Now Assist AI agents
◦AI Agent Studio
◦Implement access control in Now Assist AI agents
◦AI Agent Analytics dashboard
◦Examples of using AI agents
•Model Context Protocol Client
•MCP Server Console
Conversational AI engagement
Now Assist in Virtual Agent acts as the conversational front door to your organization’s AI
capabilities. It enables users to interact naturally with AI-powered assistants that understand
intent, recommend actions, and deliver synthesized responses—all within familiar channels like
the service portal, mobile app, and Microsoft Teams. This conversational layer connects users
to a wide range of AI-powered resources, including AI agents, generative AI skills, catalog items,
Virtual Agent topics, Q&A Genius results from AI Search, and even custom subflows and actions.
By integrating with the AI agent framework, Virtual Agent can discover and trigger agentic
workflows that dynamically solve problems based on context. For example, a user might ask
about ordering a device, and the system can invoke a multi-turn catalog ordering skill, refine the
request, and complete the task, all in one conversation. Similarly, Q&A Genius capabilities allow
users to ask open-ended questions and receive actionable answers, links, or follow-up options,
improving deflection rates and reducing the need for live agent intervention.
Now Assist in Virtual Agent also makes it easier to discover content without needing to know
exact keywords. Users can search for and interact with catalog items, AI agents, and Virtual
Agent topics using natural language. LLM topic discovery and Knowledge Graph slot-filling can
return personalized responses and reduce repetitive questions.
To configure Now Assist in Virtual Agent, you set up an assistant. An assistant is a container for
a specific conversational experience that can be delivered in portals on your instance, mobile
apps, Microsoft Teams, and Slack. Use the Assistant Designer to create, configure, and manage
these assistants, as well as link them to conversational assets in Virtual Agent.
To implement Now Assist in Virtual Agent, admins use guided setup that requires no deep
technical expertise. Assistant configuration includes the following options:
•AI agent enablement and orchestration
•Search sources
•Knowledge Graph schema usage
•Conversational assets, such as Virtual Agent topics, subflows, actions, generative AI skills, and
AI agents
•The portals, channels, or apps the assistant will be used in
•Branding: the look and feel of the assistant
•Chat experience, such as greeting, closing, and fallback messages
You can also customize an assistant for the Now Assist panel. The Now Assist panel is available
in workspace experiences and is typically used for contextual assistance within a specific
workflow or record. Now Assist panel assistants have different configuration options and skill
availability.
© 2026 ServiceNow, Inc. All rights reserved. 21
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

Roles and responsibilities:
Virtual Agent [virtual_agent_admin]
This role, or the admin role, is required to install Now Assist in Virtual Agent and set
up and manage assistants in Assistant Designer. It is also required for users who
create and manage Virtual Agent topics and assets.
Now Assist Admin [sn_nowassist_admin.nsa_admin]
This role is required to turn on and configure the Now Assist panel in the Now Assist
Admin console.
For more information about these tools, see:
•Now Assist in Virtual Agent
◦Configuring assistants overview
◦Enhanced chat
◦Integrating Now Assist in Virtual Agent with Microsoft Teams
◦Using Now Assist in Virtual Agent conversations with Slack
◦
•Now Assist for Mobile
•Now Assist panel
AI governance for Now Assist on the ServiceNow AI Platform
As organizations increasingly adopt AI to drive efficiency, innovation, and customer experience,
AI governance becomes essential to ensure responsible use, regulatory compliance, and
alignment with enterprise goals. Now Assist provides a comprehensive governance framework
through key roles and applications that work together to manage AI across its life cycle.
AI policy considerations
The following policy considerations shape how AI is deployed, monitored, and maintained
across the enterprise.
Data security and privacy
AI systems must comply with strict data handling protocols to protect sensitive
information. This includes the following:
•Data classification rules for personally identifiable information, protected health
information, and financial data.
•Encryption standards for data in transit and at rest.
•Data residency and sovereignty restrictions, which determine where data can be
stored and processed.
•Retention and deletion policies that govern how long data is kept and when it
must be purged.
Admins can configure Data Privacy for Now Assist to mask sensitive fields and
control what is shared with third-party models. For details, see Data Privacy for Now
Assist .
Compliance and regulations
AI deployments must adhere to a range of regulatory frameworks, including:
© 2026 ServiceNow, Inc. All rights reserved. 22
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

•HIPAA, PCI DSS, GDPR, CCPA, and FedRAMP, depending on the industry and
geography.
•Third-party/vendor risk management, especially when external models or
services are used.
•Logging and traceability requirements help ensure accountability in AI decisions.
Legal reviews are often required before publishing documentation or releasing
features, particularly when consolidating overlapping control objectives or
addressing model transparency.
Responsible AI use
To ensure ethical and effective AI, organizations should enforce the following:
•Model approval and usage guidelines, including naming conventions and
branding policies for AI agents.
•Bias and fairness safeguards, with AI Stewards evaluating risks like hallucination
or exposure of sensitive data.
•Human oversight requirements, ensuring AI augments rather than replaces
human judgment.
•Transparency obligations, such as disclosing the use of third-party models like
Azure OpenAI in product documentation.
Governance and change management
AI governance is supported by structured oversight and change control processes:
•Definition, review, and approval of enterprise-wide guardrails and new use cases.
•Change control and rollout processes ensure that AI features are deployed safely
and predictably.
•Incident response and escalation plans are in place to address issues such as
data breaches or model failures.
AI policy stakeholders
The following groups set and execute AI policy in an organization:
Policy setters
The Chief Information Officer (CIO) or Chief Technology Officer (CTO) sets the
overall technology strategy, ensuring AI initiatives align with enterprise architecture
and innovation goals. The Chief Information Security Officer (CISO) establishes
data security and encryption standards to safeguard sensitive information
across AI workflows. The Chief Data Officer (CDO) oversees data usage and
governance, ensuring that AI systems handle data ethically and in accordance
with organizational policies. Meanwhile, the Chief Privacy Officer and legal teams
are responsible for regulatory compliance, ensuring that AI deployments meet
requirements such as GDPR, HIPAA, and other jurisdictional or industry-specific
standards. Together, these leaders form the foundation of AI governance, guiding
implementation teams and administrators in deploying AI responsibly and securely.
Internal governance and oversight
Governance and oversight of AI in Now Assist is led by structured groups that define
and enforce responsible use. An AI Governance Committee and Data Governance
Council set enterprise-wide guardrails for AI, including standards for privacy,
fairness, and compliance, and are responsible for reviewing and approving new
© 2026 ServiceNow, Inc. All rights reserved. 23
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

AI use cases. Supporting these bodies, the AI Steward ensures that AI is used
responsibly across workflows, overseeing data quality, managing risks such as
bias or data exposure, and monitoring adherence to regulatory requirements.
Additionally, AI Stewards monitor regulatory compliance, assess performance and
user feedback, and work with admins and developers to optimize AI automation
while minimizing risk.
Implementation and operations
Implementation and operations teams are responsible for securely deploying and
managing AI features in alignment with governance policies. The Now Assist admin
configures and manages Now Assist capabilities, ensuring that AI features are
properly mapped to workflows and governed according to enterprise standards.
Platform owners and ServiceNow admins oversee the deployment process,
making sure that all configurations comply with established policies and technical
requirements. Meanwhile, AI developers build, extend, and integrate AI features
into business workflows, working closely with admins and platform teams to deliver
scalable, compliant, and effective AI solutions. Together, these roles translate
governance policies into secure, functional AI implementations.
For more information about AI governance user roles, see Roles installed with AI Risk and
Compliance and Assign the data steward role.
For more resources about AI governance, see the following Best Practices topics:
•AI Governance White Paper
•Technical Governance Foundation Template
•Governance in operational phase: Roles and responsibilities
AI governance tools
Now Assist governance is specified in the following tools:
AI Control Tower
The AI Control Tower functions as the central hub for AI strategy, governance, and
analytics within Now Assist. It offers enterprise-wide visibility into AI assets, usage
patterns, and compliance status, enabling organizations to maintain oversight
and accountability. Through automated discovery and inventory of approved AI
assets, it streamlines asset management while embedding governance checks and
compliance alerts to ensure that all AI deployments remain secure and aligned with
organizational policies.
For more information, see AI Control Tower.
Now Assist Admin console
The Now Assist Admin console is key to managing AI governance by configuring
policies, enforcing data handling rules, and ensuring compliance with security and
privacy standards. Admins oversee provider policies at the skill level, track usage
analytics like success rates and adoption, and collaborate with AI stewards and
business SMEs to align AI with organizational goals. They also connect governance
committees with technical teams to support smooth policy execution.
For more information, see Overview tab in Now Assist Admin.
© 2026 ServiceNow, Inc. All rights reserved. 24
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

Data readiness for implementing Now Assist on the ServiceNow AI
Platform
High-quality data that is complete, accurate, and contextually relevant is the foundation for
delivering precise, meaningful, and trustworthy AI responses.
Now Assist requires high-quality data
To unlock the full potential of Now Assist on your instance, the quality of your data is paramount.
For AI to deliver accurate, context-aware, and actionable outputs, it must be trained and
operate on high-quality data that is complete, consistent, and structured. When your data is
well-prepared, Now Assist can interpret user queries with greater accuracy, enabling faster
resolutions and more effective self-service experiences.
Whether it's summarizing complex incidents, generating resolution notes, or creating knowledge
articles, Now Assist relies on detailed records that reflect the full lifecycle of a task. Short or
incomplete cases often lack the depth needed for meaningful AI interpretation, which can result
in vague or unhelpful responses. The importance of data readiness extends beyond technical
accuracy—it directly impacts user trust and adoption.
Clean, ready data also accelerates implementation. It minimizes the need for rework, reduces
deployment friction, and ensures that AI features like summarization, recommendations, and
workflow guidance operate smoothly from day one. This leads to higher ticket deflection rates
and improved operational efficiency, allowing teams to focus on strategic tasks rather than
repetitive support.
Moreover, high-quality data fosters trust in AI outputs. When users consistently receive reliable
and context-aware responses, their confidence in the system grows—driving adoption and
maximizing return on investment. Ultimately, investing in data quality is an investment in user
satisfaction, AI performance, and long-term success.
Follow these tips to assess your organization's data readiness:
•Audit task records for completeness and clarity, and ensure resolution fields are consistently
filled out with clear summaries.
•Avoid using vague or generic language in task descriptions and updates.
•Maintain a clean and structured knowledge base and ensure that knowledge articles are linked
to resolved cases.
For details, see Knowledge Base readiness for Now Assist on the ServiceNow AI Platform.
•Audit Service Catalog items.
For details, see Service Catalog readiness for Now Assist on the ServiceNow AI Platform.
•Use the Now Assist Readiness Evaluation app to assess catalog, case, and knowledge data.
•Use the Now Assist Data Kit to curate and cleanse data sources.
•Align stakeholders (data owners, product managers, engineers) around shared standards for
AI-ready data.
For details, see AI governance for Now Assist on the ServiceNow AI Platform.
For more information, see Now Assist Data Readiness Checklist .
© 2026 ServiceNow, Inc. All rights reserved. 25
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

Now Assist Readiness Evaluation app
Data readiness assessments can be time-consuming and manual, especially when evaluating
whether catalog items are conversational or if knowledge articles are embedded in inaccessible
formats like PDFs. The Now Assist Readiness Evaluation app helps automate this process
by analyzing service catalog entries, cases, and incidents, and then providing actionable
recommendations to prepare data for AI use. It also enables you to assess whether updates,
installations, or customizations of your instance could affect implementation. The assessments
provide direct hyperlinks to improve any issues found.
For more information, see Now Assist Readiness Evaluation.
Install Now Assist Readiness Evaluation by requesting it from the ServiceNow Store. Visit the
ServiceNow Store website to view all the available apps and for information about submitting
requests to the store. For cumulative release notes information for all released apps, see the
ServiceNow Store version history release notes .
Now Assist Data Kit
If the base system Now Assist skills don't fit your needs, use the Now Assist Data Kit to curate,
cleanse, and manage data for AI evaluations. You can create custom datasets and data
collections that can be used in Now Assist Skill Kit for evaluation. For more information, see Now
Assist Data Kit.
Application readiness for Now Assist on the ServiceNow AI
Platform
Now Assist leverages the power of the ServiceNow AI Platform to deliver AI solutions. Ensure that
your instance is ready to take advantage of AI capabilities by preparing Platform applications,
such as Service Catalog and AI Search.
Installing a Now Assist product such as Now Assist for IT Service Management (ITSM) gives you
access to AI capabilities in Platform applications as well as capabilities specific to your product
workflow. It's important to ensure that the appropriate Platform applications are ready for Now
Assist. To prepare your instance for Now Assist, review the following topics:
•Knowledge Base readiness for Now Assist on the ServiceNow AI Platform
•Service Catalog readiness for Now Assist on the ServiceNow AI Platform
•AI Search readiness for Now Assist on the ServiceNow AI Platform
•Now Assist in Virtual Agent readiness on the ServiceNow AI Platform
After ensuring that your AI policy, your data, and your applications are ready, you can begin to
implement Now Assist.
1.Ensure entitlement for at least one Now Assist application. For a list of available applications,
see Exploring Now Assist Admin.
Note: Some Now Assist products may require other entitlements.
2. In the ServiceNow Store, check version compatibilities and dependencies for Now Assist apps.
For more information, see Evaluating version requirements and dependencies .
3. Install Now Assist products from the Now Assist Admin console.
For more information, see Install Now Assist plugins.
© 2026 ServiceNow, Inc. All rights reserved. 26
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

Customization and Now Assist
Customizing your ServiceNow instance is often necessary to meet unique business needs, but
it can introduce unintended consequences for Now Assist features. Changes to field names, UI
actions, workflows, or table structures may disrupt how Now Assist skills and agents operate. For
example, modifying field states or labels can interfere with skill conditions and input mapping,
while altering default UI actions may prevent agents from triggering correctly. Custom resolution
workflows might conflict with the logic embedded in native skills, and table-level variations
can affect where and how Now Assist functions across workflows. These customizations can
also create upgrade friction, requiring additional testing, rework, or reconfiguration to ensure
compatibility with new platform releases.
To mitigate these risks, you can use tools like the Now Assist Readiness Evaluation app to
identify high-impact customizations and plan for remediation before deploying or upgrading AI
features. For more information, see Now Assist Readiness Evaluation.
To maintain compatibility with Now Assist while accommodating custom configurations, several
mitigation strategies are available:
•Duplicate skills before adapting them.
•Adjust skill inputs and role conditions to reflect organizational processes.
•Add additional input sources, such as related tables or emails.
For more advanced needs, build custom generative AI skills tailored to your unique business
requirements, allowing for deeper integration without compromising core functionality.
For more information about customizing AI solutions, see How to approach building custom
generative AI solutions using Now Assist in the ServiceNow Community.
Knowledge Base readiness for Now Assist on the ServiceNow AI Platform
The knowledge base is the engine that enables Now Assist to deliver intelligent, accurate,
and context-aware responses across AI Search, Q&A Genius Results, and other AI-powered
experiences.
When users ask questions, Now Assist taps into your knowledge articles to generate answers
that reflect your organization’s expertise and policies. This means the quality, clarity, and
structure of your knowledge content directly influence the effectiveness of AI responses.
Outdated, inconsistent, or poorly written articles can lead to incorrect outputs and user
frustration. That’s why maintaining a clean, well-organized knowledge base is critical—not just for
documentation, but for enabling reliable AI performance.
The Knowledge Management Overview dashboard is a powerful tool for assessing AI readiness.
It provides key usage metrics such as article views, helpfulness ratings, and feedback trends,
helping content owners identify high-performing articles and prioritize updates to low-usage or
outdated content. For more information, see Knowledge Management Overview dashboard .
High-level checklist
1. Review existing KB articles and knowledge bases
Get the total count of published KB articles and the number of active knowledge
bases.
Why? To scope clean-up and identify high-priority content.
See: Knowledge Management Overview dashboard
2. Review the structural formatting of KB articles
© 2026 ServiceNow, Inc. All rights reserved. 27
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

Check for consistent template use (KCS-based, Q&A, Issue-Cause-Resolution, etc.).
Ensure that the Knowledge Management Advanced plugin is active.
If you're using custom templates, determine whether they follow a consistent format.
Also ensure that key steps are clearly defined and consistently populated.
Why? Using templates consistently improves LLM understanding and
summarization.
See:
•Knowledge article templates
•Activate the Knowledge Management Advanced plugin
3. Ensure metadata completeness in KB articles
Make sure that fields such as Meta, Meta Description, Category, Author, and Validity
are populated.
Why? This practice enables precise AI filtering and targeting.
See:
•Create a knowledge article
•Best practices to use your knowledge articles with Now Assist (generative AI)
(ServiceNow Community)
4. Perform maintenance audits
Flag KB articles that have not been updated in a year or more, that have no
metadata, are duplicates, or are about to expire.
Why? Outdated content degrades user trust and AI performance.
See:
•Knowledge Management Overview dashboard
•Retire a knowledge article
•Identify and review duplicate Knowledge articles (requires Now Assist in
Knowledge Management)
5. Review top searched queries
Identify search queries and articles for optimization, and limit Now Assist Q&A
functionality to high-quality, optimized KB articles.
Why? This prevents low-value content from surfacing in answers.
See: Knowledge Management dashboard
Service Catalog readiness for Now Assist on the ServiceNow AI Platform
A well-structured Service Catalog is essential to unlocking the full potential of Now Assist. As
the backbone of many self-service workflows, the catalog enables Now Assist to interpret user
requests accurately, present the right options, and minimize friction in the experience.
When catalog items are clearly defined and conversationally enabled, Now Assist in Virtual
Agent can surface them more effectively, leading to higher self-service rates and better issue
deflection.
© 2026 ServiceNow, Inc. All rights reserved. 28
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

However, catalogs that are cluttered, inconsistent, or overly complex make it difficult for AI to
parse and respond appropriately. That’s why auditing your existing catalog is a critical first step.
By identifying which items are AI-ready and optimizing those that aren’t, you ensure that Now
Assist can deliver intelligent, context-aware responses.
High-level checklist
1. Install the Catalog Conversational Coverage (sn_catalog_con_cov) plugin
This plugin gives you access to the conversational catalog overview dashboard.
See: Install an application or plugin
2. Review your catalog inventory
Use the conversational catalog overview dashboard to review all active catalog
items. From this list, determine which are most requested and the percentage that
are conversational.
Why? To focus improvement efforts on the catalog items with the highest impact.
See:
•Catalog Conversational Coverage
•Conversational catalog overview dashboard
3. Determine which catalogs can be made conversational
Identify catalog items with fewer than 15 variables. (Items with more than 15
variables are better suited to be submitted as pop-up links to forms.)
Note: Conversational catalog items require Now Assist in Virtual Agent.
For details, see Now Assist in Virtual Agent readiness on the ServiceNow AI
Platform.
Why? These are easier to convert and provide quick AI wins.
See: Service catalog variables
4. Analyze catalog item metadata
Ensure catalog items have clear, user-friendly names, tooltips, metadata, and
categories. Using templates can help with this as well.
Why? This prevents LLM confusion and improves conversational flow.
See:
•Service Catalog properties
•Edit a catalog item in Catalog Builder
•Create a catalog item using a template
5. Review advanced configurations
Review UI policies, client scripts, and user criteria.
Why? User criteria determines who can request an item, but policies and scripts are
ignored by Virtual Agent.
See:
© 2026 ServiceNow, Inc. All rights reserved. 29
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

•Service catalog UI policy
•Set security for items and categories
•Create a user criteria record in Service Catalog
•Create a Service Catalog client script
Tips
•Use Now Assist in Catalog Builder to generate catalog items .
•Limit the number of variables. Fewer is better.
•For form-based requests, select the Make item non-conversational in VA check box.
•Provide clear context for the LLM with distinct names, labels, and tooltips.
•Minimize the use of custom variable types. Use the service catalog variables included on the
platform instead.
•Limit client-side scripting and use regular expressions for validation.
•Avoid complex dependencies. Simplify variable relationships to ensure a smooth conversation
flow.
•Test and iterate: make changes based on feedback.
For more information about conversational catalogs in AI, see the following ServiceNow
Community articles:
•Guidance for making catalog items conversational
•How to request catalog items in Now Assist in Virtual Agent
AI Search readiness for Now Assist on the ServiceNow AI Platform
®
Now Assist in AI Search is built directly on the robust foundation of ServiceNow AI Search.
AI Search provides the underlying infrastructure that enables Now Assist to retrieve and rank
enterprise content—such as knowledge articles, records, and documentation—based on
relevance and access permissions.
Because AI Search adheres to ServiceNow security models, responses are always grounded
in content the user is authorized to access. Additionally, AI Search admin tools give you control
over relevancy tuning, allowing you to refine how content is surfaced and ensure that Now Assist
delivers the most useful and trustworthy results.
Every AI-generated answer includes citations and references, allowing users to see exactly
where the information came from. This not only boosts confidence in the accuracy of responses,
but also reduces the risk of hallucination by grounding outputs in your organization’s actual
content.
To maximize its impact, Now Assist in AI Search should be activated before Now Assist is more
broadly implemented. Once enabled, it powers actionable Q&A through Genius Results cards in
global search, Service Portal, Employee Center, and Virtual Agent.
High-level checklist
1. Verify AI Search status
Make sure AI Search is active on your instance. To check status, navigate to All > AI
Search > AI Search Status. If AI Search is not active, select the Request AI Search
button to initiate activation.
© 2026 ServiceNow, Inc. All rights reserved. 30
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

See:
•Configuring AI Search
®
•Enable AI Search in supported ServiceNow AI Platform applications
2. Review search sources
Configure search sources to determine what data will be searched by user queries.
See:
•Control access to searchable content using search sources
•Create a search source for AI Search
3. Configure search sources for external content
Allows Now Assist Q&A search to include external content.
See:
•Indexing and searching external content in AI Search
•Create an indexed source
•Configuring External Content Connectors
4. Enable AI Search on one or more portals
Display AI Search results in the portals on your instance.
See:
•Search application configurations
®
•Enabling and configuring AI Search in ServiceNow AI Platform applications
5. Install Now Assist in AI Search
Install a Now Assist product in the Now Assist Admin console.
See: Install Now Assist in AI Search
6. Enable Now Assist Q&A Genius Results in AI Search portals
Specify the Now Assist Genius Result types you want to make available in each
of your AI Search portals. Now Assist Multi-Content Response Genius Results
use an LLM to generate search and chat responses that synthesize information
from knowledge articles, Service Catalog items, and other available content types.
Answers are presented in Q&A format.
See:
•Enable Now Assist Genius Results in AI Search portals and mobile applications
•Now Assist Q&A Genius Results
7. Verify AI Search widget customizations
Customized AI Search widgets may not correctly show Q&A search results even
when configured for Now Assist, since customizations get skipped during upgrades.
See:
© 2026 ServiceNow, Inc. All rights reserved. 31
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

®
The ServiceNow AI Platform offers a variety of search tools, which may return different answers
for the same or similar searches. This disparity in results is expected. For more information, see
Search result disparities between AI Search and Now Assist search features .
Tip: For more information, see Now Assist in AI Search FAQ in ServiceNow Community.
Now Assist in Virtual Agent readiness on the ServiceNow AI Platform
Now Assist enhances Virtual Agent with AI-driven capabilities that understand natural language,
guide users through complex tasks, and deliver high-confidence answers without relying on rigid
keyword matching or manual configurations.
Now Assist in Virtual Agent provides the following features:
•AI asset discovery
Say goodbye to time-consuming keyword or NLU configurations. Now Assist uses LLMs to
automatically discover and match user intents to Virtual Agent topics and other AI assets,
including generative AI skills, AI agents and agentic workflows, and subflows and actions.
•Simplified deployment
Using LLM-powered Virtual Agent topics, teams can accelerate rollout and improve
conversation quality. This means less effort spent on manual tuning and more time delivering
value.
•AI Search Genius Results
Users receive curated, actionable responses via Genius cards, which contain summarized
knowledge with direct actions such as Request this item.
•Conversational catalog ordering
Users can request Service Catalog items using natural conversation. Virtual Agent asks
clarifying questions and confirms the user's intent before completing the request.
Note: Service Catalog items must be marked as conversational to work with Virtual
Agent. For details, see Catalog item conversational details page overview .
•Multi-turn Q&A
Follow-up questions are handled seamlessly, allowing users to refine their queries and get
better answers.
Setting up Now Assist in Virtual Agent requires customizing or creating a new LLM assistant. You
can assign an assistant to one or more portals. If LLM Virtual Agent topics aren't associated with
an LLM assistant, they aren't discoverable.
High-level checklist
1. Install Now Assist in Virtual Agent
You can install it from the Conversational Interfaces admin console once you have
installed a Now Assist product such as Now Assist for IT Service Management
(ITSM).
To set up Now Assist in Virtual Agent, you configure an assistant.
See: Configuring assistants overview
© 2026 ServiceNow, Inc. All rights reserved. 32
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **Tip: For more information, see** | **Now Assist in AI Search FAQ** | **in ServiceNow Community.** |
|---|---|---|

| **Catalog item conversational details page overview** | **** |
|---|---|

2. Review your Virtual Agent topic inventory
Review your topics and identify high-volume user intents. You can use the
Conversational Analytics dashboard and Automation Discovery reports.
Why? This helps you identify the top self-solve opportunities in Virtual Agent.
See:
•Conversational Analytics dashboard
•Create an Automation Discovery report
Review your knowledge base
Identify KB articles that can self-serve any of the top intents you identified.
Why? This simplifies topic management and enables self-service.
See: Knowledge Base readiness for Now Assist on the ServiceNow AI Platform
4. Migrate NLU topics to LLM
Use the topic migration tool in Virtual Agent to convert NLU topics to LLM.
Why? Leverage existing Virtual Agent topics with minimal effort.
See: Migrating NLU/keyword Virtual Agent topics to LLM topics
5. Review Service Catalog items
Identify self-serve catalog items that can be replaced with existing LLM topics.
Why? To avoid redundancy and eliminate the need to create new Virtual Agent
topics.
See: Service Catalog readiness for Now Assist on the ServiceNow AI Platform
Review LLM Virtual Agent topics that come with Now Assist
Use these LLM topics as a starting point for Virtual Agent topic creation.
Why? New LLM versions of older NLU Virtual Agent topics reduce rework.
See: ITSM Virtual Agent pre-built LLM topics
Tips
•When migrating legacy NLU topics, ensure that you optimize topic descriptions so that the
topic is clearly described and aligned with the intent and expected results.
For details, see .
•You can customize the look of your assistant and the chat experience during guided setup.
For details, see Brand and personalize an assistant .
•You can choose the chat experience you want for each assistant:
◦Standard chat
◦Enhanced chat
© 2026 ServiceNow, Inc. All rights reserved. 33
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

•You can integrate Now Assist in Virtual Agent with Microsoft Teams.
For details, see Integrating Now Assist in Virtual Agent with Microsoft Teams .
For more information about conversational catalogs in AI, see the following information from
ServiceNow Community and YouTube:
•How to request catalog items in Now Assist in Virtual Agent
•Microsoft Copilot integration with Now Assist FAQ - Zurich release
•AI Academy: Enhanced chat experience with Now Assist in Virtual Agent
Understanding large language models (LLMs)
Large language models are generative, not retrieval-based. They create responses dynamically
using probability, which means you can’t expect identical outputs every time. This variability is a
feature, not a bug, because it allows for flexibility, creativity, and adaptability.
How LLMs work
Large language models (LLMs), like ChatGPT or Copilot, are advanced AI systems that are
trained on massive amounts of text to understand and generate human-like language. They build
a statistical model of language, so they don’t store fixed answers like an encyclopedia. When you
ask a question, the model generates an answer one word (or token) at a time, choosing the next
most likely word based on probabilities learned during training. This prediction process makes
them powerful, but it's also why they are non-deterministic. This means the system does not
always produce the exact same result (output) for the same prompt (input).
Why results may vary
Even if you provide the same question or prompt twice, the response can differ. Here’s why:
Probabilistic sampling
The model doesn’t always pick the single most likely word. It samples from several
likely options. This introduces variation.
Temperature settings
Temperature controls randomness, and this internal parameter varies among
LLM models. A higher temperature delivers more creative responses, while lower
temperatures tend to be more repetitive.
Multiple valid answers
Many questions have more than one correct way to explain something. The model
may choose different phrasing or emphasis each time.
Context sensitivity
Tiny changes in punctuation or prior conversation can shift the output.
System-level factors
Hardware concurrency, floating-point math, and backend updates can introduce
slight variations, even when everything else is fixed.
For example, think of it like rolling dice to pick words. When you ask a question, the model
doesn’t follow a fixed script. Instead, it looks at many possible next words and picks one based
on probabilities—like rolling weighted dice. The dice are weighted toward the most likely words,
but there’s still a chance for variation. If you roll again (ask the same question), you might get a
slightly different sequence, even though the rules didn’t change. This randomness is intentional.
It makes the model flexible and creative, rather than rigid and repetitive.
© 2026 ServiceNow, Inc. All rights reserved. 34
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

For more information about supported LLM models, see Large language models on the
ServiceNow AI Platform.
Variations in search
®
The ServiceNow AI Platform offers a variety of search tools, which may return different answers
for the same or similar searches. This disparity in results is expected. For more information, see
the following topics:
•Discrepancies when using different AI search tools
•Search result disparities between AI Search and Now Assist search features
Solving installation and configuration issues with Now Assist
Use this checklist to address issues or gaps in your Now Assist configuration.
Common issues by Now Assist feature
Feature Issue Solution
AI agents I can't find Install the Now Assist for Spokes application from the ServiceNow
agent spokes Store. For details, see Now Assist for Integration Hub .
AI Control No data Verify that the Conversation Evaluator [sn_na_conv_eval] plugin
Tower on the is active. Also verify that the Smooth Flowing Conversation Chat
Evaluations Eval skill is active in the Now Assist Admin console. (This skill
tab may appear in the Platform workflow or in the Other workflow,
depending on your instance.)
AI Search External You can use External Content Connectors to include other
content isn't sources in your search results. For details, see External Content
included in Connectors .
search results
AI Search Now Assist
1.Verify that AI Search and Now Assist in AI Search are installed
in AI Search
and configured.
Genius
results don't 2. To use Now Assist Q&A Genius Results in AI Search
appear applications, link the Now Assist Q&A Genius Result
configuration to your search profiles for those applications.
For details, see Link a Genius Result configuration to a search
profile .
3. Verify that all Now Assist plugins are up to date.
4.Try repairing the plugins.
Knowledge I can't
1.Verify that Now Assist in Knowledge Management is installed
articles generate a
and configured.
knowledge
article 2. Verify that all Now Assist plugins are up to date.
3. Verify that the knowledge generation skill is activated. For
details, see Activate a Now Assist skill.
4.Try repairing the plugins.
© 2026 ServiceNow, Inc. All rights reserved. 35
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **Feature** | **Issue** | **Solution** |
|---|---|---|
| AI agents | I can't find agent spokes | Install the Now Assist for Spokes application from the ServiceNow Store. For details, see Now Assist for Integration Hub . |
| AI Control Tower | No data on the Evaluations tab | Verify that the Conversation Evaluator [sn_na_conv_eval] plugin is active. Also verify that the Smooth Flowing Conversation Chat Eval skill is active in the Now Assist Admin console. (This skill may appear in the Platform workflow or in the Other workflow, depending on your instance.) |
| AI Search | External content isn't included in search results | You can use External Content Connectors to include other sources in your search results. For details, see External Content Connectors . |
| AI Search | Now Assist in AI Search Genius results don't appear | 1.Verify that AI Search and Now Assist in AI Search are installed and configured. 2. To use Now Assist Q&A Genius Results in AI Search applications, link the Now Assist Q&A Genius Result configuration to your search profiles for those applications. For details, see Link a Genius Result configuration to a search profile . 3. Verify that all Now Assist plugins are up to date. 4.Try repairing the plugins. |
| Knowledge articles | I can't generate a knowledge article | 1.Verify that Now Assist in Knowledge Management is installed and configured. 2. Verify that all Now Assist plugins are up to date. 3. Verify that the knowledge generation skill is activated. For details, see Activate a Now Assist skill. 4.Try repairing the plugins. |

Common issues by Now Assist feature (continued)
Feature Issue Solution
Knowledge The KB Now Assist in Knowledge Management formatters may
articles generation be missing from the form layout, possibly due to form
popup customizations. For details, see KB1710178 .
doesn't
appear in
Core UI
Now Assist I want to See Product subscriptions overview .
applications view my
subscriptions
Now Assist Can't access
•Verify that the skill is configured to display in the Now Assist
panel skills in the
panel. For details, see Edit a Now Assist skill.
Now Assist
panel •If you are using Now Assist in Virtual Agent, verify that search
sources were configured for the Now Assist panel. You can
specify search sources for a Now Assist panel assistant when
you set it up. Search sources are essential for the Now Assist
panel and Virtual Agent. Without them, they cannot discover or
rank skills and agentic workflows. For details, see Configuring
assistants overview and Assign search sources to a chat
assistant .
If Now Assist in Virtual Agent is not installed, the Now Assist
panel uses default search sources.
Now Assist Some users Many Now Assist skills require specific user roles. Verify that
panel don't get a there are active skills with the user's role. For details, see Activate
response to a a Now Assist skill.
question
Now Assist I don't want Disable the Now Assist panel when you configure the skill. For
panel skills to be details, see Edit a Now Assist skill.
available in
Now Assist
panel
Now Assist Options for The sn_nowassist_admin.user role provides read-only access
panel Now Assist only. To make configuration changes, the user must have the
panel are sn_nowassist_admin.nsa_admin role.
grayed out
in the Now
Assist Admin
console
Now Assist Errors after Try repairing affected plugins. For details, see Repair a
setup clone ServiceNow application .
Now Assist The Q&A Set up AI Search. For details, see Configuring AI Search .
setup results skill
is not in
the Now
Assist Admin
console
© 2026 ServiceNow, Inc. All rights reserved. 36
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **Feature** | **Issue** | **Solution** |
|---|---|---|
| Knowledge articles | The KB generation popup doesn't appear in Core UI | Now Assist in Knowledge Management formatters may be missing from the form layout, possibly due to form customizations. For details, see KB1710178 . |
| Now Assist applications | I want to view my subscriptions | See Product subscriptions overview . |
| Now Assist panel | Can't access skills in the Now Assist panel | •Verify that the skill is configured to display in the Now Assist panel. For details, see Edit a Now Assist skill. •If you are using Now Assist in Virtual Agent, verify that search sources were configured for the Now Assist panel. You can specify search sources for a Now Assist panel assistant when you set it up. Search sources are essential for the Now Assist panel and Virtual Agent. Without them, they cannot discover or rank skills and agentic workflows. For details, see Configuring assistants overview and Assign search sources to a chat assistant . If Now Assist in Virtual Agent is not installed, the Now Assist panel uses default search sources. |
| Now Assist panel | Some users don't get a response to a question | Many Now Assist skills require specific user roles. Verify that there are active skills with the user's role. For details, see Activate a Now Assist skill. |
| Now Assist panel | I don't want skills to be available in Now Assist panel | Disable the Now Assist panel when you configure the skill. For details, see Edit a Now Assist skill. |
| Now Assist panel | Options for Now Assist panel are grayed out in the Now Assist Admin console | The sn_nowassist_admin.user role provides read-only access only. To make configuration changes, the user must have the sn_nowassist_admin.nsa_admin role. |
| Now Assist setup | Errors after clone | Try repairing affected plugins. For details, see Repair a ServiceNow application . |
| Now Assist setup | The Q&A results skill is not in the Now Assist Admin console | Set up AI Search. For details, see Configuring AI Search . |

Common issues by Now Assist feature (continued)
Feature Issue Solution
Now Assist Features/
•Verify that all of your Now Assist plugins are up to date.
setup skills are
For details, see Install an update to a ServiceNow Store
missing or
application .
generally not
working •Verify that version and dependency requirements are
met. For details, see Evaluating version requirements and
dependencies .
•For skills, verify that they are active in the Now Assist Admin
console. For details, see Activate a Now Assist skill.
•Verify that the user has the correct role for the skill.
•Try clearing the cookies and cache in the web browser.
•Try repairing Generative AI Controller. For details, see Repair a
ServiceNow application .
Now Assist Can't edit a
setup skill Verify that you have the Now Assist Admin role:
sn_nowassist_admin.nsa_admin.
You can edit a skill or make a copy of a skill to edit. For details,
see Edit a Now Assist skill and Make a copy of a Now Assist skill.
Now Assist Missing
•Verify that all of your Now Assist plugins are up to date.
setup entries, fields,
For details, see Install an update to a ServiceNow Store
and errors
application .
•Try repairing the application. For details, see Repair a
ServiceNow application .
•Try repairing Generative AI Controller. For details, see Repair a
ServiceNow application .
Now Assist Problems
•Verify that you have a license for the application.
setup upgrading
Now Assist •If the application was not previously installed, request it from
applications the ServiceNow Store (Opt In).
•If the application was previously installed, you may need to
procure it from the ServiceNow Store again. For details, see
Updating applications .
Now Assist Skills not Now Assist skills are not available in Legacy Workspace. Upgrade
setup working in to Service Operations Workspace to use Now Assist.
Legacy Agent
Workspace
© 2026 ServiceNow, Inc. All rights reserved. 37
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **Feature** | **Issue** | **Solution** |
|---|---|---|
| Now Assist setup | Features/ skills are missing or generally not working | •Verify that all of your Now Assist plugins are up to date. For details, see Install an update to a ServiceNow Store application . •Verify that version and dependency requirements are met. For details, see Evaluating version requirements and dependencies . •For skills, verify that they are active in the Now Assist Admin console. For details, see Activate a Now Assist skill. •Verify that the user has the correct role for the skill. •Try clearing the cookies and cache in the web browser. •Try repairing Generative AI Controller. For details, see Repair a ServiceNow application . |
| Now Assist setup | Can't edit a skill | Verify that you have the Now Assist Admin role: sn_nowassist_admin.nsa_admin. You can edit a skill or make a copy of a skill to edit. For details, see Edit a Now Assist skill and Make a copy of a Now Assist skill. |
| Now Assist setup | Missing entries, fields, and errors | •Verify that all of your Now Assist plugins are up to date. For details, see Install an update to a ServiceNow Store application . •Try repairing the application. For details, see Repair a ServiceNow application . •Try repairing Generative AI Controller. For details, see Repair a ServiceNow application . |
| Now Assist setup | Problems upgrading Now Assist applications | •Verify that you have a license for the application. •If the application was not previously installed, request it from the ServiceNow Store (Opt In). •If the application was previously installed, you may need to procure it from the ServiceNow Store again. For details, see Updating applications . |
| Now Assist setup | Skills not working in Legacy Agent Workspace | Now Assist skills are not available in Legacy Workspace. Upgrade to Service Operations Workspace to use Now Assist. |

Common issues by Now Assist feature (continued)
Feature Issue Solution
Now Assist Don't
•Verify that the skill is active. For details, see Activate a Now
for Code see code
Assist skill.
suggestions
•Verify that the user has the appropriate role. Any authenticated
builder can use the related active skill.
•Verify that autocomplete is enabled. For details, see Generate
code with autocomplete .
Now Assist Skills not
•Verify that the skill is active in the Now Assist Admin console.
for Creator available or
not working •Verify that the user has the appropriate role. Any authenticated
builder can use the related active skill.
Now Assist Now Assist
•Verify that you have at least one Now Assist product installed.
Skill Kit Skill Kit is not
For details, see Install Now Assist plugins.
visible on my
instance •Verify that the sn_skill_builder.admin role is assigned to the
user.
Now Assist Skills are Verify that the sn_skill_builder.admin role is assigned to the user.
Skill Kit read-only
Now Assist Topic not
•Verify that the Virtual Agent topic is in the Active state and is
in Virtual returning as
published. For details, see Publish a Virtual Agent topic .
Agent expected
•Verify that the topics are using LLM topic discovery. NLU/
keyword topics cannot be used in a portal that is using Now
Assist in Virtual Agent. You can migrate NLU/keyword topics to
LLM, however. For details, see Migrating NLU/keyword Virtual
Agent topics to LLM topics .
Now Assist Can't add Verify that the topics are using LLM topic discovery. NLU/keyword
in Virtual topics to the topics cannot be added to a portal that is using Now Assist in
Agent portal Virtual Agent. You can migrate these topics to LLM, however. For
details, see Migrating NLU/keyword Virtual Agent topics to LLM
topics .
Now Assist Configuration
1.Verify that the plugin is up to date. For details, see Install an
in Virtual issues
update to a ServiceNow Store application .
Agent
2. Follow the guided setup to install and configure it. For details,
see Configuring assistants overview .
Now Assist Unable to If you're using a custom fallback topic, this option may be
in Virtual choose unavailable in guided setup. For details, see KB1760362: Now
Agent fallback Assist Chat Setup Not Allowing to Set Fallback Option . You may
options in need to log in to view the article.
setup
© 2026 ServiceNow, Inc. All rights reserved. 38
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **Feature** | **Issue** | **Solution** |
|---|---|---|
| Now Assist for Code | Don't see code suggestions | •Verify that the skill is active. For details, see Activate a Now Assist skill. •Verify that the user has the appropriate role. Any authenticated builder can use the related active skill. •Verify that autocomplete is enabled. For details, see Generate code with autocomplete . |
| Now Assist for Creator | Skills not available or not working | •Verify that the skill is active in the Now Assist Admin console. •Verify that the user has the appropriate role. Any authenticated builder can use the related active skill. |
| Now Assist Skill Kit | Now Assist Skill Kit is not visible on my instance | •Verify that you have at least one Now Assist product installed. For details, see Install Now Assist plugins. •Verify that the sn_skill_builder.admin role is assigned to the user. |
| Now Assist Skill Kit | Skills are read-only | Verify that the sn_skill_builder.admin role is assigned to the user. |
| Now Assist in Virtual Agent | Topic not returning as expected | •Verify that the Virtual Agent topic is in the Active state and is published. For details, see Publish a Virtual Agent topic . •Verify that the topics are using LLM topic discovery. NLU/ keyword topics cannot be used in a portal that is using Now Assist in Virtual Agent. You can migrate NLU/keyword topics to LLM, however. For details, see Migrating NLU/keyword Virtual Agent topics to LLM topics . |
| Now Assist in Virtual Agent | Can't add topics to the portal | Verify that the topics are using LLM topic discovery. NLU/keyword topics cannot be added to a portal that is using Now Assist in Virtual Agent. You can migrate these topics to LLM, however. For details, see Migrating NLU/keyword Virtual Agent topics to LLM topics . |
| Now Assist in Virtual Agent | Configuration issues | 1.Verify that the plugin is up to date. For details, see Install an update to a ServiceNow Store application . 2. Follow the guided setup to install and configure it. For details, see Configuring assistants overview . |
| Now Assist in Virtual Agent | Unable to choose fallback options in setup | If you're using a custom fallback topic, this option may be unavailable in guided setup. For details, see KB1760362: Now Assist Chat Setup Not Allowing to Set Fallback Option . You may need to log in to view the article. |