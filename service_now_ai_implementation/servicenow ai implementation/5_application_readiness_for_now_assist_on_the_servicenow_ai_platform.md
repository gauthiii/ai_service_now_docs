## Application Readiness for Now Assist on the ServiceNow AI Platform


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