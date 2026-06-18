# Now LLM Service updates

*Source: document pages 117–120 (PDF chunk pages 17–20)*

---



<!-- doc page 117 -->

Third party AI model providers (continued)
Model provider Large language model Version Deployment policy
en-us/azure/ai-
OpenAI GPT 5.4, services/openai/
GPT-5.2, and GPT-5.2- how-to/deployment-
mini types global-
standard
V1: GPT 4.1 and GPT
4.1 mini
Google Google Gemini Gemini 2.5 Flash and https://
2.5 Pro cloud.google.com/
vertex-ai/generative-
ai/docs/learn/
locations
AWS AWS Claude V2: https://
docs.aws.amazon.com/
•Claude 4.6 Sonnet
bedrock/latest/
•Claude Haiku 4.5 userguide/models-
regions.html
V1: Claude 4.0 Sonnet
Note: Some out of box skills, Agents, and Agentic Workflows do not support Now
LLM Service or third party model providers. To learn more about the exceptions to LLM
service and third party model providers support, see https://support.servicenow.com/kb?
id=kb_article_view&sysparm_article=KB2222333
Large language model selection
This selection is supported at various levels such as, skill, skill group and instance levels.
However, the controls that define LLMs mapping to different skills, allowed at various global
locations, are configured and approved in AI Control Tower by the AI steward. The model
provider options for custom skills created in Now Assist skill kit and AI Agent Studio are also
configured in AI Control Tower.
The Manage large language models feature enables the admin persona to perform additional
actions like:
•Edit the model provider at the instance, skill group and skill levels
•Deactivate active skills which are non-compliant with fallback as No. See Explore AI model
providers to learn more.
•View audit history on policy updates by AI steward in AI Control Tower
•Select allowed model providers across domain separated instances.
See Manage AI models to learn about managing.
For more information on selecting and updating model providers, see Manage model providers.
Now LLM Service updates
The Now LLM Service provides access to specialized large language models (LLMs) that are
developed by ServiceNow. It also provides access to open-source LLMs that are selected,
configured, or enhanced by ServiceNow, from the ServiceNow community and partners. Review

ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| Model provider | Large language model | Version | Deployment policy |
| --- | --- | --- | --- |
|  |  | OpenAI GPT 5.4, GPT-5.2, and GPT-5.2- mini V1: GPT 4.1 and GPT 4.1 mini | en-us/azure/ai- services/openai/ how-to/deployment- types global- standard |
| Google | Google Gemini | Gemini 2.5 Flash and 2.5 Pro | https:// cloud.google.com/ vertex-ai/generative- ai/docs/learn/ locations |
| AWS | AWS Claude | V2: •Claude 4.6 Sonnet •Claude Haiku 4.5 V1: Claude 4.0 Sonnet | https:// docs.aws.amazon.com/ bedrock/latest/ userguide/models- regions.html |



<!-- doc page 118 -->

these reference materials and model cards for additional information about the Now LLM Service
and about the models used.
Model cards
Large language models (LLMs) are complex machine-learning models that are trained on large
datasets like websites and documentation to perform language-related tasks, such as text
generation for case summaries and resolution notes.
Model cards explain the specific model's context, intended use, training data, limitations, and
other important information.
These model cards are for skills that use the Now LLM Service. There are certain skills, such as
Now Assist Multi-Turn Catalog Ordering, that use Azure OpenAI instead. To see what LLM a skill
is using, you can check the skill list in the Now Assist Admin console and review the LLM service
column.
Model card for ServiceNow large language model
Model used for AI-driven solutions to support natural language understanding,
automation, and decision support.
This model card is available in Yokohama patch 1 and later.
Model card for ServiceNow large language model (V2)
Model for enterprise AI that enhances text-based automation and content
generation in ServiceNow workflows, including requester OOTB skills, custom skills,
and agentic use cases.
This model is for Generative AI Controller application 11.2 or higher.
Model card for ServiceNow small language model
Model used for enterprise AI applications by enhancing text-based automation and
content generation within ServiceNow workflows.
This model card is available in Yokohama patch 1 and later.
Model card for ServiceNow small language model (V2)
Model for enterprise AI that enhances text-based automation and content
generation in ServiceNow workflows, including creator and fulfiller OOTB skills as
well as custom skills.
This model is for Generative AI Controller application 11.2 or higher.
Model card for ServiceNow third party large language model
Model used for AI-driven solutions for text generation, summarization, and
conversational AI.
Model card for ServiceNow Voice AI Speech-to-Text and Text-to-Speech models
Models used within ServiceNow AI Voice Agents for converting spoken user input to
text and generating natural-sounding speech from AI responses.
Model card for ServiceNow Now Assist Guardian model
This model provides content moderation and helps identify different kinds of
prompt injection attacks and offensive content.
Model card for ServiceNow Inferred CSAT and Factors large language model

ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.


<!-- doc page 119 -->

This model is designed to ingest a conversation and predict a CSAT score as well as
factors that explain the predicted score.
June 2026
The June release includes updates to third-party model defaults, a change to the default
reasoning effort setting for GPT-5 Mini, and the retirement of the Now LLM long-term support
(LTS) SKU.
•Third-party default model version update: Teams that did not update their third-party default
model versions to the latest available versions in the May release must do so in the June
release. GAIC 13.1.2 is the required version for this update.
•GPT-5 Mini — reasoning_effort default change: The default reasoning_effort
setting for GPT-5 Mini has changed from none to minimal. This change is included in GAIC
Snapshot 14.0.0, which is compatible with Now Assist for Platform 12.0.0.
Teams using GPT-5 Mini should run regression and functional testing to confirm that the new
default works as expected. If you explicitly set reasoning_effort in your generative AI
config additional properties, smoke test to verify there are no unexpected effects. If you have
reasoning_effort: none set in additional properties, update the value to minimal
and run regression and functional testing.
•Claude Sonnet 4.0 retirement: Claude Sonnet 4.0 references are being redirected on the
backend. No team action is required.
◦claude_large / Claude 4.0 Sonnet redirects to Claude 4.5 Sonnet
◦claude_small / Claude 4.0 Sonnet redirects to Claude 4.5 Sonnet
•Now LLM LTS SKU retired: ServiceNow no longer offers the LTS model SKU. There are no testing
requirements or expectations for teams related to this retirement.
May 2025
An advanced 12B general-purpose small language model (SLM) with a singular, high-
performance architecture that supports a wide range of tasks in ServiceNow’s context was
released. Fine-tuned on Mistral-Nemo-12B-Instruct, this model is designed and optimized for
tasks like Agent Assist, Text-to-Flow, Text-to-Cypher, Safety & Content Moderation and Text-to-
Code.
Key Enhancements:
•Enhanced instruction adherence: Improved the model’s capability to accurately interpret and
follow user instructions, ensuring that the model can better understand and execute complex
commands. Leading to more precise and reliable outcomes than previous releases.
•Increased context window: increased context window from 16K to 32K, enabling the model
to better understand long-form inputs, maintain coherence over extended interactions, and
support more complex tasks with richer contextual awareness.
•Improved multilingual proficiency: Boosted performance across languages compared to
previous releases, with notable enhancements in Japanese processing.

ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.


<!-- doc page 120 -->

•Optimized for ServiceNow workflow related capabilities: Extended support coverage for Text-
to-Flow, and improved the performance of Text-to-Code, Text-to-Cypher etc.
•Continuously enhanced model deployment consolidation: Integrates ServiceNow-related
tasks into a single model, reducing system complexity at the same time while elevating overall
performance.
March 2025
A powerful 12B general-purpose small language model (SLM) designed to enhance a wide range
of applications, including text-to-code and agent use cases was released. Fine-tuned on Mistral-
Nemo-12B, it streamlines deployment and consolidates multiple functionalities into a singular,
architecture.
Key Enhancements:
•Optimized to fulfill use cases: Enhances case summarization, chat summarization, resolution
notes, and knowledge base generation across supported languages, including improvements
in Japanese quality.
•Superior text-to-code and text-to-cypher performance: Delivers major advancements in Glide
JavaScript and generic JavaScript editing and generation, along with improved accuracy in
query generation and execution for structured databases.
•Robust content moderation and safety: Provides stronger protection against adversarial
prompts, jail-breaking attempts, and harmful content generation, ensuring safer deployment
with built-in content filtering.
•Unified model deployment:integrates ServiceNow-related tasks into a single model, thereby
reducing system complexity while elevating overall performance.
•Improved instruction adherence: Delivers better instruction following and consistency across
varying levels of prompt and instruction strictness than the current text-to-text NowLLM.
November 2024
Several key improvements were added to the Now LLM Service that are aimed at enhancing
performance and quality.
•Multilingual support: Now LLM Service supports 8 additional languages, enabling global teams
to use the model in their native languages.
The supported languages are: English, German, French, Japanese, Dutch, French Canadian,
Spanish, Brazilian Portuguese, and Italian.
•JSON format support: The model now provides output in JSON format, making it easier for
developers to integrate with various applications and automate workflows seamlessly.
◦Deterministic responses: JSON mode ensures structured, consistent output, which improves
predictability and reliability when integrating with applications.
◦Error reduction: Unlike free-form text mode, JSON responses are less prone to format errors
or stray characters, minimizing integration issues.
◦Lower token consumption: The fixed structure of JSON can reduce token usage, making it
more efficient and cost-effective for applications with high response frequency.
•Improvements in instruction following: The model has been fine-tuned to understand and
follow instructions more precisely. This enables the model to deliver more to-the-point and
actionable responses, helping users get the information they need faster and more efficiently.

ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.