## Understanding Large Language Models LLMs


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