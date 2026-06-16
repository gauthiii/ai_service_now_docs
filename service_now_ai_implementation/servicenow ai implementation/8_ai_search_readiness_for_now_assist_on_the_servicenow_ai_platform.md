### AI Search Readiness for Now Assist on the ServiceNow AI Platform


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