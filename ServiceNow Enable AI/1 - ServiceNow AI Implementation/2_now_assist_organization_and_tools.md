## Now Assist Organization and Tools


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