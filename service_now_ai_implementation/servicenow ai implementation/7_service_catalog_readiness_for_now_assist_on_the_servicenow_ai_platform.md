### Service Catalog Readiness for Now Assist on the ServiceNow AI Platform


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