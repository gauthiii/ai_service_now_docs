### Now Assist in Virtual Agent Readiness on the ServiceNow AI Platform


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