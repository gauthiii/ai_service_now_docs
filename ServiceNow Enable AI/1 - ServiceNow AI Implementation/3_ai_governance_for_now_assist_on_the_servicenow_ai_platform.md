## AI Governance for Now Assist on the ServiceNow AI Platform


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