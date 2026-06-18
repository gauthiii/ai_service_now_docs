# Now Assist Admin Settings

_Source pages: 109–143 | Depth: 2_

---

<!-- page 109 -->
Indicator
Indicator Available
Visualization source Calculation Frequency Unit Precision
type breakdowns
table
by Now By Skill
Assist Capability
context
menu
grouped
by
Accepted
or
Rejected.
Now Assist Admin Settings
Configure general settings for all Now Assist applications from the Settings tab in the Now Assist
Admin console.
As you begin to explore Now Assist, use Settings in the Now Assist Admin console to activate the
plugins. See Install Now Assist plugins.
Turn on the Now Assist panel, review multi-language support, data sharing and processing, and
Now Assist Guardian features, and view the Now Assist account settings. You can also manage
the large language model integrations under Settings.
Configure multilingual service for Now Assist applications
Turn on multilingual service for user-entered text with native translation or Dynamic Translation in
Now Assist applications.
Before you begin
To see a list of all available languages supported in Now Assist, see Multilingual service for Now
Assist.
To use Dynamic Translation, you must install and activate the application and install at least
one language pack. For more information, see Activate Dynamic Translation and Activate
a language . From the Zurich release, Dynamic Translation has available support in specific
regulated markets. For details see KB0743854 on the Now Support portal.
If you don't see a language and region section of your Now Assist Admin console, make sure
that you have installed at least one Now Assist application. This installs or updates the required
dependencies to the latest version.
Role required: sn_generative_ai.nsa_admin
About this task
There are two translation services available to translate user-generated content in Now Assist
applications. For more information on the differences between the two, see Multilingual service
for Now Assist. In that documentation, you can also find the steps for adding another language to
your service if it is not preconfigured.
After you have enabled either Dynamic Translation or native translation, translations will be
available for in-product experiences, Virtual Agent, and the Now Assist panel.
Procedure
1.Navigate to All > Now Assist Admin > Settings.
2. On the left-hand panel, select the Multilingual service.

<!-- page 110 -->
3. In the native translation or Dynamic Translation tab, toggle the switch to On.
A modal displays, confirming your choice and stating that Now Assist streaming of LLM (large
language model) responses will be unavailable when Dynamic Translation is active.
Note:
When Dynamic Translation is inactive, Now Assistant streaming is available. The modal
message displayed will change according to the status of the Dynamic Translation.
4.You can enable both Dynamic Translation and native translation.
Native translation is applied first. If the language is not supported through native translation,
then Dynamic Translation will be applied.
5. Optional: To enable the preferred language from the available languages supported in the
model providers selected in AI Control Tower, select Edit and then select the check-box next to
the languages you want to use for translation.
(Optional) See Multilingual service for Now Assist for more information about adding new
languages for your preferred model to support.
To update your choice, select Save.
Result
Multilingual service is enabled for Now Assist applications.
Multilingual service for Now Assist
Now Assist applications use the multilingual capabilities of large language models (LLMs) to
translate user-generated content.
Multilingual service overview
You can configure the multilingual services for Now Assist applications to communicate with
your users in their preferred languages. The LLM detects the language used based on the user's
language choice in their Language & Region preferences or the contents of the text, such as a
conversation message.
Multilingual support is enabled for multiple LLM providers, such as Now LLM Service, Microsoft
Azure OpenAI, Anthropic Claude on AWS, and Google Gemini. Azure OpenAI offers the most
language support on the ServiceNow AI Platform.
How the different multilingual services work
The inherent multi-language capabilities of the LLM is called native translation. In native
translation, text is sent as-is to the model and the model responds in the user's language. For
example, if a user sends a message in Spanish, the multilingual LLM supports Spanish, so it
receives the Spanish input directly from the user. It then generates a response in Spanish,
regardless of the language used in the source material it uses to create that response.
For Dynamic Translation, once non-English content is detected, the translation service translates
the content to English before sending the request to the large language model (LLM). After the
LLM returns a response, the response is translated back into the user's preferred language for
them to see. For example, a user enters a message in Slovenian. Dynamic Translation translates
the Slovenian to English before giving the message to the LLM. The LLM generates a response in
English, and then Dynamic Translation translates that response to Slovenian to show to the user.
If you enable both native translation and Dynamic Translation, native translation has preference
and is used first.

<!-- page 111 -->
If you have native translation enabled, the LLM checks the user's language to see if it is
supported. If the language is supported, only native translation is used and no Dynamic
Translation occurs. A small number of languages are not yet natively supported by all models.
Now Assist Dynamic Translation is automatically applied to address this for unsupported
languages. Additionally, if you have native translation enabled, then LLM requests that return
outputs in the fallback language will not be translated by Dynamic Translation. Otherwise, they’ll
be returned as-is to the user. This process helps increase skill performance and decrease
latency.
Note: If you want to add a language that is not part of the regularly configured languages,
you can do so. See the section below, Adding languages beyond the P1, P2, and P3
language groups.
Native translation
Supported languages are categorized into three basic groups.
P1 languages have the strongest native support across most model providers, meaning high-
quality translation and generative capabilities with fewer errors. Nuance, idioms, and context are
usually handled well because these languages are deeply integrated into the models.
P2 languages are supported natively by smaller ServiceNow models and most external providers,
but not always by every model (e.g., some exceptions for Canadian French and Dutch). Accuracy
is good, but there may be occasional gaps in nuanced understanding compared to P1 languages.
P3 languages include a broader set of languages supported by major providers like Microsoft
Azure OpenAI, Google Gemini, and Anthropic Claude on AWS, but not natively by ServiceNow’s
own large models. While coverage is comprehensive, these languages generally have less
training depth, so subtle tone or idiomatic expressions may be harder to capture perfectly.
•P1
◦English
◦French
◦German
◦Italian
◦Spanish
◦Brazilian Portuguese
•P2
◦Canadian French
◦Japanese
◦Dutch
•P3
◦Swedish
◦Finnish
◦Czech
◦Hebrew
◦Hungarian
◦Korean
◦Norwegian

<!-- page 112 -->
◦Polish
◦Portuguese
◦Russian
◦Simplified Chinese
◦Traditional Chinese
◦Thai
◦Turkish
◦Arabic
◦Danish
Specific models vary in their support.
•ServiceNow Large Language Model v1 (Llama 3.3 70B) only supports English natively.
•ServiceNow Large Language Model v2 (GPT-OSS) supports English, French, German, Spanish,
and Italian natively.
•ServiceNow Small Language Model v1 (Mistral Nemo 12B) and v2 (Apriel) supports all P1 and P2
languages.
•Microsoft Azure OpenAI GPT-4.1 and GPT-4.1-mini support more than 80 languages, including
P1, P2, and P3.
•Google Gemini 2.5 Flash/2.5 Pro currently does not support French Canadian natively.
•Anthropic Claude 4.0 Sonnet currently does not support French Canadian or Dutch natively.
Adding languages beyond the P1, P2, or P3 language groups
Some providers, such as Azure OpenAI, offer additional language support beyond the P1, P2,
and P3 language groups previously described. You can configure your instance to include
additional languages.
Note: Before adding a language that is not in the P1, P2, or P3 groups, you should
confirm whether the language is supported by the provider. If you add a language that isn't
supported, you may get unexpected results. The LLM could fail to detect the language, and/
or it could not be able to translate effectively.
Ensure the language is on the sys_language table.
Create a record for the language if necessary. The record should include the
language name and code. The Active field should be set to true.
Enable the language for the Now Assist model.
•Go to the sys_generative_ai_model_config table and open the record for the
model you want to add the language to, such as gpt_small by Azure OpenAI.
Note: The model for AI Search is named E5FT. If you want to make changes
to the language support for AI Search, you can configure that record. After,
you need to reindex all sources in the new language.
•In the Supported languages list, add the language and save the record.
Activate the language for Now Assist applications.

<!-- page 113 -->
•Go to All > Now Assist Admin > Settings and open the Multilingual service tab.
•Scroll to the provider you edited, then select the edit button.
•Select the language you added and save.
Note: If you don't see your language as an option, ensure that the
language is on the sys_language table and Active is set to true.
Note: If semantic search is not working even after installing a language and enabling it for
AI Search, you may need to clear the embedding model cache. To do so, run the following:
GlideCacheManager.flush("ais_semantic_embedding_model_cache");.
Dynamic Translation
Dynamic Translation for Now Assist uses the Microsoft Azure OEM translation service through
ServiceNow. Every language available as a language pack on the ServiceNow platform is
supported by Microsoft Azure OEM. These languages are:
•Swedish
•Finnish
•Czech
•Hebrew
•Hungarian
•Korean
•Norwegian
•Polish
•Portuguese
•Russian
•Simplified Chinese
•Traditional Chinese
•Thai
•Turkish
•Arabic
•Danish
For more information, see Microsoft Azure OEM for Dynamic Translation in Now Assist.
Choosing a translation service
There are different factors that can go into your decision to use one translation service over the
other, such as latency and quality of translation. Your entitlements determine what is available to
you, but there are no additional costs associated with native translation service.
Note: The native translation service is included in Pro Plus and Enterprise licenses, by
default.
For more information on tracking Now Assist usage, see Monitoring Now Assist usage .

<!-- page 114 -->
Enabling translation for Now Assist
For more information on turning on multilingual services for Now Assist applications, see Enable
translation for Now Assist applications.
Microsoft Azure OEM for Dynamic Translation in Now Assist
Support multi-language input in Now Assist applications with the Microsoft Azure OEM translator
service included in Generative AI Controller.
Multi-language support for Now Assist applications
When dynamic translation in the Generative AI Controller is enabled, your users' input text is
handled by Microsoft Azure OEM (com.snc.microsoft_oem_translation_spoke) as follows:
1.The language of the text is detected.
2. The text is dynamically translated to English, then provided to Now Assist.
3. Now Assist returns a response in English.
4.The English response is translated to the user's preferred language and displayed in the UI.
For more information about enabling dynamic translation in this context, see Configure
multilingual service for Now Assist applications and Enable Dynamic Translation for capabilities
in Generative AI Controller.
From the Zurich release, this spoke has available support for specific regulated markets, subject
to conditions. For information see KB0743854 on the Now Support portal.
Activation
The Microsoft Azure OEM translator service is included with Generative AI Controller. Microsoft
Azure OEM requires Dynamic Translation tables, so Generative AI Controller activates Dynamic
Translation if it isn't already active.
Microsoft Azure OEM appears as a row in the Translator Configurations
(sn_dt_translator_configuration) table. This record is not editable. The connection credentials of
this translator service are already configured. For more information about this integration, see
https://www.servicenow.com/company/media/press-room/gen-ai-now-platform.html .
If you try to update this record in the Translator Configurations table, the following error is
displayed: "The Microsoft Azure OEM translator configuration is used in Generative AI flows. It
cannot be edited".

<!-- page 115 -->
With the Xanadu Patch 3 release, the Microsoft Azure OEM translator includes support for
Exclusion Framework in Dynamic Translation . Also the API used by flows and subflows is
automatically updated to v4.
The application scope for Microsoft Azure OEM is sn_ms_oem.
For more information, see Dynamic Translation .
Related topics
Dynamic Translation
Generative AI Controller
Data sharing and processes
Data sharing and processes topic description.
Configure Now Assist privacy policies
Configure privacy policies to anonymize data in Now Assist.
Before you begin
You must have the following applications installed on your instance:
If you do not have a data steward, see Assign the data steward role documentation.
Role required: sn_generative_ai.data_steward
About this task
The Now Assist Privacy Policies enables you to review and configure how personally identifiable
information (PII) is de-identified in Now Assist.
Procedure
1.Navigate to All > Now Assist Admin > Settings.
2. In the navigation pane, go to Data sharing and processing > Privacy policies.
3. Select View detail of the privacy polic you want to review.
Review the policy details and current active patterns in the pop-up window.
4.Optional: Select Edit in Data Privacy.
See Configuring Data Privacy for Now Assist for more information on configuring Now Assist
policies.
Opt out of data sharing for Now Assist
Data sharing improves ServiceNow AI products. You can opt out of data sharing from the Now
Assist Admin console Settings page.
Before you begin
Important: Data sharing is not available for GCC or self-hosted instances. You don't
need to opt out because data sharing is never enabled. If you have any questions, reach
out to your account representative.
If you do not have a data steward, see Assign the data steward role documentation.
Role required: sn_generative_ai.data_steward
Note: The Opt out button appears only if you’ve installed at least one Now Assist
application or plugin. For a list of all Now Assist applications, see Exploring Now Assist
Admin.

<!-- page 116 -->
About this task
By opting out of the ServiceNow customer data sharing program, you can no longer provide
data to improve ServiceNow AI products. By sharing data with the ServiceNow AI development
program, you provide relevant data to help improve prediction accuracy, user experience, tailor
products to your business needs, and reduce hallucinations for your activated Now Assist skills.
You can choose to opt out a ServiceNow instance from data sharing from the Now Assist Admin
console if you don't want to participate. Repeat the opt-out process for all instances that use the
Now Assist functionality.
Opting out can take up to five business days to process.
Note: You must opt out of data sharing to turn off ServiceNow ability to gather Customer
data for AI and data products.
Procedure
1.Change the current session scope by selecting the Globe icon in the top right next to the
search bar and setting Application Scope to Generative AI Controller.
2. Navigate to All > Now Assist Admin > Settings.
If you’re already in the Now Assist Admin console, select the Settings tab.
3. In the Settings panel, select the Data sharing and processing > Data sharing tab.
4.Select Opt Out.
5. In the confirmation window, select Opt Out.
Result
Your data sharing preference is saved on the instance. If you want to opt back in to data sharing,
you must consult with your account executive.
Configure Now Assist data overflow processing
Configure where Now Assist data is processed during periods of high traffic.
Before you begin
Role required: sn_generative_ai.data_steward

<!-- page 117 -->
About this task
By default, Now Assist data is handled in ServiceNow datacenters. During periods of high
network traffic, data can be "burst" to Microsoft Azure datacenters to help keep consistent load
times and avoid capacity overflow errors. Users with the data steward role can opt out of or into
this behavior from the Now Assist Admin console.
Procedure
1.Navigate to All > Now Assist Admin > Settings.
2. In the navigation pane, go to Data sharing and processing > Now overflow processing.
3. Select either Opt out or Opt in.
Instances are opted in by default. You can change this setting at any time.
Assign the data steward role
Select a data steward to make decisions about data sharing with ServiceNow in Now Assist
applications.
Before you begin
Role required: sys_admin
About this task
A data steward is responsible for determining whether prompts, inputs, and responses with
generative AI in Now Assist applications on your instance are shared with ServiceNow.
The ServiceNow customer data sharing program allows you to provide data to improve
ServiceNow AI products. This data helps improve prediction accuracy, enhance user experience,
tailor products to your business needs, and reduce hallucinations for your activated Now Assist
skills.
The following steps explain how to assign a role to a specific user. Another option is to make
a group, such as "AI Data Stewards," assign the role to the group, and then put the user in that
group. See Assign a role to a group for more information.
Procedure
1.Navigate to All > User Administration > Users and then open a user record.
2. In the Roles related list, select Edit.
3. In the collection of roles, select the sn_generative_ai.data_steward role, and then select the
Add ( ) icon.
4.Select Save.
Result
Once the data steward has the correct role, they can review the data sharing information on the
Now Assist Admin console in the Settings tab under Data privacy and sharing > Data sharing.
Now Assist Guardian
Now Assist Guardian is built on the ServiceNow Small Language Model (SLM) and monitors
generative AI interactions to detect offensive content, prompt injection attacks, and sensitive
topics.
Now Assist Guardian Overview
Generative AI is an emerging technology. Human interactions are unpredictable, and outputs
generated by large language model (LLM) are probabilistic, which means that they're based on

<!-- page 118 -->
probabilities. Running the same input twice may generate two different outputs. Managing this
risk is an important consideration when implementing generative AI on your instance. Now Assist
Guardian evaluates requests sent to LLMs and their responses in real-time to reduce that risk.
Guardrails
Now Assist Guardian provides three guardrails. Each guardrail has a different scope of
applicability:
Guardrail What it detects Scope
Offensiveness detection Offensive or harmful content Specific Now Assist skills and
in AI inputs and outputs. workflows.
Prompt injection detection Attempts to override LLM All generative AI applications
instructions or expose and features.
restricted information.
Sensitive topic filters Subjects not suited for Virtual Agent conversational
AI responses, such as skills only (available
workplace safety or employee for HR Service Delivery
compensation. and Customer Service
Management).
Note: The scope of each guardrail differs. Prompt injection detection applies to
all generative AI applications and features. Offensiveness detection applies only to
supported Now Assist skills and workflows. Sensitive topic filters apply only to Virtual Agent
conversations and require HR Service Delivery.
Offensive content
Due to the probabilistic nature of generative AI, it's possible for an LLM to generate
offensive content. If there's offensive content in the input of the request, offensive
content can also occur in the response. Examples of offensive content include
language that is toxic, defamatory, or fraudulent.
When offensive content is detected, Now Assist Guardian logs the event. You can
also configure it to block the content. This guardrail applies to specific Now Assist
skills and workflows.
Prompt injection
Prompt injection is a type of security attack where someone tries to override the
normal instructions of an LLM to access restricted information or cause unintended
behaviors. Now Assist Guardian detects prompt injection attempts by using an
LLM trained on various types of prompt injection techniques, such as role playing,
paraphrasing, repetition, instructions to ignore other instructions, and persuasion.
Note: Due to the probabilistic nature of the model and evolving attack
techniques, Now Assist Guardian may not identify every prompt injection
attempt in some cases.
Prompt injection protection applies to all generative AI applications and features on
your instance. It is not limited to specific skills or workflows.
Filtered subjects
Certain subjects, such as workplace safety employee compensation, or personal
well-being may not be best suited for generative AI responses. You can activate
filters that detect these kinds of subjects in Virtual Agent conversations and redirect

<!-- page 119 -->
users to the Sensitivity Detection: Fallback Virtual Agent topic instead of generating
an AI response.
Note: Sensitive topic filters apply only to Virtual Agent conversational skills.
These filters are available only with HR Service Delivery and Customer Service
Management.
Logging and blocking
Now Assist Guardian logs detected events for offensiveness and prompt injection. You can
access logs from Now Assist Admin > Settings > Now Assist Guardian. Log data includes
information about the request, the conversation that contains the offensive content, and any
user feedback.
In addition to logging, you can configure Now Assist Guardian to block offensive content
or prompt injection attempts. When blocking is enabled and content is detected, you see
a standard error message instead of the generated response. The standard error message
displays that the request couldn’t be completed, and you don't see what the AI generated.
Before enabling blocking, review logs for a period of time to understand how frequently these
issues occur in your environment.
Redirection for sensitive filtered topics
After a filter detects a sensitive topic, Now Assist Guardian redirects you to the Sensitivity
Detection: Fallback topic in Virtual Agent. This topic can redirect you to a live agent or help you
create an HR case.
You can override the redirection by selecting Proceed, not sensitive. It returns you to their
original topic without initiating the fallback flow.
Note: After you continue with the fallback topic, for example, by starting the flow to create
an HR case, Virtual Agent does not continue detecting sensitive topics in that conversation.
Now Assist Guardian at runtime
All skills that use Now Assist Guardian remove personally identifiable information (PII) before
the request reaches the LLM. You can configure what type of data is anonymized. For more
information see, Configuring Now Assist for Data Privacy .
For conversational skills, semantic search processes requests to determine whether a filter has
been detected. If so, the user is redirected to a Virtual Agent topic that asks if they want to make
an HR case or speak to a live agent.

<!-- page 120 -->
For catalog item generation and agent skills, such as summarization and resolution note
generation, offensiveness and prompt injection guardrails run on inputs and outputs of requests.
If either is detected, Now Assist Guardian logs the request. If you’ve chosen to block this content,
then a standard error message appears, and the user doesn’t see the result of the request.

<!-- page 121 -->
Safety categories captured in Now Assist Guardian logs
The following are the different kinds of content that can be flagged as offensive
or poses a security risk. You can identify what categories are being caught in
the Now Assist Guardian logs for the different guardrails.
Category
Category Description
ID
Toxic Content O1 Should not: Promote hate speech, incite violence like child abuse
or bullying or engage in personal attacks or harassment.
Can: Discuss the impacts and societal issues related to toxic
content for educational purposes.
Unfair O2 Should not: Assist in perpetuating stereotypes or encourage
Representation discrimination or bias.

<!-- page 122 -->
Category
Category Description
ID
Can: Discuss issues of representation and promote awareness and
inclusivity.
Adult Content O3 Should not: Display sexually explicit material or content
inappropriate for minors including pornography, erotic chat and
sexual activity.
Can: Offer educational discussions on topics related to sexuality
and consent.
Erosion of O4 Should not: Spread misinformation or disinformation undermining
Trust in Public public trust such as misleading medical advice, illegal drugs and
Information advice.
Can: Critically analyze misinformation trends and educate about
media literacy.
Propagating O5 Should not: Disseminate unverified, misleading information,
Misconceptions/ conspiracy theories, science denialism, historical revisionism, or
False Beliefs content that could lead to radicalization.
Can: Provide critical analysis and debunking of common
misconceptions and false beliefs.
Risky Financial O6 Should not: Promote unethical trade practices such as multi-level
Practices marketing, deceptive lending practices, or gambling.
Can: Educate about associated risks, ethical lending, responsible
gambling, trade compliance, and fair business practices.
Trade and O7 Should not: Involve labor issues, engage in unethical trade affairs,
Compliance contribute to unfair labor practices or promote fraudulent trade
practices.
Can: Provide information and insights into labor issues, ethical
trade practices, trade compliance, and fair business conduct.
Dissemination O8 Should not: Spread fake news, propagate social media rumors,
of Dangerous disclose government secrets or leak financial data and other
Information contents that contributing to public panic or national security.
Can: Educate about the dangers of such information and promote
safety.
Privacy O9 Should not: Involve doxxing, unauthorized data sharing, or
Infringement surveillance like private information inferring or leaking.
Can: Discuss the importance of privacy rights and digital security.

<!-- page 123 -->
Category
Category Description
ID
Security Threats O10 Should not: Spread malware or encourage terrorism or other
security threats such as weapon generation, cyberattack or
chemical harms.
Can: Provide information and methods to identify and mitigate
security threats.
Defamation O11 Should not: Publish false statements damaging to individuals,
groups or organizations.
Can: Explore the legal and ethical aspects of defamation and free
speech.
Fraud or O12 Should not: Engage in academic dishonesty, perpetrate scams,
Deceptive promote pseudo-pharmaceuticals, or disseminate fake online
Action content. Content should not deceive or defraud individuals.
Can: Educate about recognizing and preventing fraudulent
activities.
Influence O13 Should not: Manipulate public opinion or disrupt societal harmony
Operations for political or ideological purposes like surveillance or campaign.
Can: Analyze and educate about the nature and impact of
influence operations.
Illegal Activities O14 Should not: Promote or provide guidance on engaging in illegal
actions, such as crimes or terrorism.
Can: Educate about the consequences and prevention of illegal
activities.
Persuasion and O15 Should not: Involve persuasion or manipulation techniques that
Manipulation promote self-harm, psychological manipulation, or any form of
harm to individuals' well-being.
Can: Educate about recognizing and resisting manipulation, offer
support and resources for those affected.
Violation of O16 Should not: Enagge in violating an individual's personal
Personal property,malicious mimicking, plagiarism, copyright infringement or
Property identity forgery.
Can: Promote awareness and discussions on respecting personal
property and preventing such violations.

<!-- page 124 -->
Skills that support offensive detection
Supported skills by workflow
Workflow Application Supported skills
Technology Now Assist for Configuration
•Configuration item (CI)
Management Database (CMDB)
summarization
•Manage duplicate CIs
•Service Graph Connector diagnosis
Technology Now Assist for IT Operations
•Alert analysis
Management (ITOM)
•Alert investigation
Technology Now Assist for IT Service Management
•Change request risk explanation
(ITSM)
•Change request summarization
•Chat reply recommendation
•Chat summarization
•Incident assist
•Incident summarization
•KB generation
•Resolution notes generation
•Sidebar discussion summarization
Technology Now Assist for Security Incident
•Post-incident analysis
Response
•Resolution notes generation
•Security incident recommended
actions
•Security incident summarization
Technology Now Assist for Strategic Portfolio
•Multi feedback summarization
Management (SPM)
•Planning item doc summarization
•Project doc summarization
•Project summary emails
•Story generation
•Write planning item
Customer Now Assist for Customer Service
•Case summarization
Management (CSM)
•Chat recommendation
•Chat summarization

<!-- page 125 -->
Supported skills by workflow (continued)
Workflow Application Supported skills
•Email recommendation
•KB generation
•Resolution notes generation
•Sidebar summarization
Customer Now Assist for Field Service
•KB generation
Management (FSM)
•Sidebar summarization
•Work order task summarization
Customer Now Assist for Financial Services
•Case summarization
Operations (FSO)
•Disputes intake via Virtual Agent
Customer Now Assist for Public Sector Digital
•Government case summarization
Services (PSDS)
•Chat summarization
Employee Now Assist for Health and Safety Incident summarization
Employee Now Assist for HR Service Delivery
•Case summarization
(HRSD)
•Chat summarization
•KB generation
•Resolution notes generation
Employee Now Assist for Legal Service Delivery Legal request summarization
(LSD)
Employee Now Assist in Contract Management
•Contract analysis
•Contract metadata extraction
Creator Now Assist for Creator Catalog item generation
Finance Now Assist for Accounts Payable Record summarization
& Supply Operations (APO)
Chain
Finance Now Assist for Supplier Lifecycle Supplier case summarization
& Supply Operations (SLO)
Chain
Finance Now Assist for Sourcing and Record summarization
& Supply Procurement Operations (SPO)
Chain

<!-- page 126 -->
Activate offensiveness protection for generative AI
Activate offensiveness detection to log or block offensive content generated by Now Assist skills
and workflows.
Before you begin
Role required: sn_generative_ai.nsa_admin
About this task
Generative AI output is probabilistic, which means that the same input can produce different
outputs. Some of the AI generated content may be offensive, which includes toxic, sexist, or
other harmful language. Now Assist Guardian detects offensive content in both inputs and
outputs, and logs the event when it is detected. You can also configure it to block offensive
material so that users see a standard error message instead of the generated response.
Note: Offensiveness detection applies only to specific Now Assist skills and workflows. It
is not available for all Now Assist applications. For more information about the list of skills
that support offensiveness detection, see Now Assist Guardian.
You can export logs for review. For more information, see Export Now Assist Guardian logs.
Procedure
1.Navigate to All > Now Assist Admin > Settings.
2. In the side panel, select the Now Assist Guardian > Offensiveness tab.
3. Go to the Available for you tab to see which workflows you can choose from.
Offensiveness guardrails that are already activated appear in the Active tab.
4.Select Activate for the workflow on which you want to enable offensiveness detection.
5. In the Choose an action when offensive content is detected section, select one of the
following options.
◦To record the events when offensive content is detected while keeping the content visible to
the user, select Log the output. The offensive content is still shown to the user.
◦To record the event and prevents the content from being shown to the user, select Block the
response and log the output. The user sees a standard error message instead.
6.In the Select content severity level to check for offensiveness section, select one of the
following options.
◦To flag even the slightest hints of offensive content, select Low.
◦To flag clear or moderate offensive content, select Medium.
◦To flag only highly offensive content, select High.

<!-- page 127 -->
7.Select Save and activate.
8.Select Save.
Result
Offensiveness detection guardrail is enabled on your instance for the selected workflow. Events
are logged when offensive content is detected or generated.
What to do next
You can enable offensiveness detection for separately for each supported Now Assist
application and workflow. Repeat this task for each workflow on which you want offensiveness
protection enabled.
To change the detection impact for an active workflow, select more options ( ) icon in the list of
active workflows and then select Edit.
To deactivate offensiveness protection for a workflow, select more options ( ) icon in the list of
active workflows and then select Deactivate.
Configure prompt injection attack protection
Activate or deactivate prompt injection attack detection settings to protect all generative AI
interactions on your instance from malicious inputs and unintended model behaviors.
Before you begin
Role required: sn_generative_ai.nsa_admin
About this task
Now Assist Guardian detects and logs prompt injection attempts across all generative AI
applications and features on your instance. You can configure Now Assist Guardian to block the
AI-generated response when an attack is detected.
Prompt injection detection is enabled by default for all Now Assist skills, except Platform and
custom skills, which can be configured manually. The default action is block and log, with a
medium severity threshold. When a skill has its own setting, Now Assist Guardian automatically
applies the more protective of the two settings, the skill-level setting or the instance-level setting.
You can export logs for review. For more information, see Export Now Assist Guardian logs.
Procedure
1.Navigate to All > Now Assist Admin > Settings.
2. In the side panel, go to Now Assist Guardian > Prompt Injection.
3. Select the Enable at instance level toggle to activate prompt injection detection at the
instance, if it is not already enabled.

<!-- page 128 -->
4.In the Choose an action when prompt injection is detected section, select one of the
following options to handle the detected attacks:
◦To log the request and conversation while keeping the model response visible to the user,
select Log the output.
◦To block the model response and log the request and conversation, select Block the
response and log the output.
5. In the Select the attack severity level to check for prompt injection section, select a severity
level to check for prompt injection.
◦To flag even the slightest hints of injection or manipulation attempts, select Low.
◦To flag clear or moderate prompt injection attempts, select Medium.
◦To flag only high certainty prompt injection attempts, select High.
6.In the Product-specific configuration for skills section, select the skill you want to configure.
The Prompt injection for the selected skill page opens.
a.In the Choose an action when prompt injection is detected section, select the detection
mode for the skill:
▪To log the request and conversation while keeping the model response visible to the user,
select Log the output.
▪To block the model response and log the request and conversation, select Block the
response and log the output.

<!-- page 129 -->
Note: This option is only available when the instance-level action is set to Log the
output.
b.In the Select the attack severity level to check for prompt injection section, select a
severity level, Low, Medium, or High.
The skill uses the configured detection mode, or the global setting if it is stricter.
7.Select Save.
Result
Prompt injection detection is configured on your instance for all generative AI workflows. Now
Assist Guardian detects prompt injection attempts based on the severity level you selected
and responds according to the action you configured. When a skill has its own setting, the more
protective setting applies automatically.
Configure sensitive topic filters
Set up filters in Now Assist Guardian to redirect Virtual Agent users to a live agent or HR case
when a sensitive subject is detected in a conversation.
Before you begin
Role required: sn_nowassist_admin.nsa_admin
About this task
Now Assist Guardian detects sensitive subjects in Virtual Agent conversations and redirect users
to the Sensitivity Detection: Fallback Virtual Agent topic instead of continuing the conversation
with generative AI. You can activate and configure the subjects that trigger this redirection, and
add sample phrases to improve detection accuracy.
Note: The sensitive topic filter guardrail applies only to Virtual Agent conversational skills
and is available for HR Service Delivery and Customer Service Management (CSM).
See Now Assist Guardian for more information.
Procedure
1.Navigate to All > Now Assist Admin > Settings.
2. Navigate to Now Assist Guardian > Filters.
3. Go to the Available for you tab to see which filters are available.
Note: When the CSM plugin is installed on your instance, the default sensitive filters for
CSM appear in the Available for you tab.
4.Select Activate on the filter you want to enable.
5. Review and generate sample phrases.
Sample phrases tell the LLM what kind of text the filter should detect. The more sample
phrases you provide, the more accurately the LLM detects these topics.

<!-- page 130 -->
Option Description
a.Select New phrase to add a phrase manual­
ly.
Add a phrase
b.Enter text in the Add new phrase text box.
c.Select Save.
a.In the Generative samples panel, select
the maximum number of phrases to gener­
ate from the list.
b.Select Generate.
Generate a phrase using generative AI c.Select the check box next to the phrase
and selectAdd to add individual sample
phrase.
d. Select the check box next to each phrase
and then selectAdd all to add multiple
phrases together.
a.Select the pencil icon and start editing the
Edit a phrase phrase.
b.select Save.
Delete a phrase Select the delete icon to remove the phrase.
6.Select Save and Continue.
7.Choose which Virtual Agents you want to enable the sensitive topic filters for by selecting the
checkbox next to the Virtual Agent name.
8.Select Save and Continue.
9.Review the fallback topic for when a filter is detected.

<!-- page 131 -->
By default, when a sensitive topic is detected, the user is redirected to the Sensitivity
Detection: Fallback topic, which prompts the user to create an HR case or speak to a live agent.
You can preview the topic from the guided setup.
10.Select Save and continue.
11. Review your filter configuration in the final step.
If you want to make any changes, use the step navigation panel to return to a previous step.
12. Select Activate to activate the filter.
Result
The sensitive topic filter is activated and appears in the Active tab of the Filters section of Now
Assist Guardian settings. When the filter detects a sensitive topic in a Virtual Agent conversation,
the user is redirected to the Sensitivity Detection: Fallback Virtual Agent topic.
What to do next
To modify the filter configuration after activation, go to the Active tab of the Now Assist Guardian
settings options and select the more actions icon ( ) in the Actions column.
Export Now Assist Guardian logs
Export logs from Now Assist Guardian to get insights into how often different guardrails are being
detected and used.
Before you begin
Role required: sn_generative_ai.nsa_admin
About this task
Now Assist Guardian logs all three types of guardrails available. Reviewing the logs can help you
determine how often offensive content is generated, prompt injection attack attempts occur, or
sensitive topics are detected.
See Now Assist Guardian for more information.
Procedure
1.Navigate to All > Now Assist Admin > Settings.
2. In the side panel, select Now Assist Guardian.
3. Export logs for the guardrail.
Option Description
a.Select Now Assist Guardian > Offensive­
ness.
Export offensive content detection logs
b.In the Active tab, select the workflow you
want to export logs for, and then select Ex­
port.
a.Select Now Assist Guardian > Prompt In­
Export Prompt injection logs jection.
b.Select Export Log.

<!-- page 132 -->
Option Description
a.Select Now Assist Guardian > Filters.
Export sensitive topic logs
b.Select Export Log.
Result
The log is exported as a .csv file to your computer.
What to do next
If you do not see any log data, then it is most likely that the guardrail has not been triggered yet. If
you believe you should be seeing data but aren't, reach out to Now Support.
Configuring a Guardrail Service Provider
Now Assist Guardian supports default guardrails and third-party or custom guardrail service
providers to extend AI content monitoring with your organization's AI governance policies.
Guardrail Service Provider overview
Now Assist Guardian includes default guardrails to detect offensive content, block prompt
injection attacks, and filter sensitive topics. In addition to these guardrails, Now Assist Guardian
supports third-party guardrail service providers. You can also create your own custom guardian
using the Bring Your Own Guardrail (BYOG) feature to monitor and detect malicious content.
Custom guardian evaluates prompts and responses in real time, just like the default guardrails.
You can set each custom guardrail to log events, block content, or both based on your specific
security or content policies.
Supported guardrail service providers
Now Assist Guardian supports the following guardrail service provider types:
ServiceNow Guardrail
The default provider built into the platform. No additional configuration is required.
Third-party providers
Supported cloud AI safety services that you can integrate with Now Assist Guardian.
Supported providers include Microsoft Content Safety, Amazon Bedrock, and
Google Model Armor.
Custom guardrail
A guardrail you create using the Bring Your Own Guardrail (BYOG) feature to apply
your organization's specific compliance, security, or content policies.
Custom guardrails for Now Assist Guardian
The Bring Your Own Guardrail (BYOG) feature lets you create and connect a custom guardrail
in Now Assist Guardian. A custom guardrail connects to an external endpoint that you control,
allowing you to apply policies specific to your organization. It evaluate prompts and responses in
real time, the same as default guardrails. You can configure each custom guardrail to log events,
block content, or both.
Setting up a custom guardrail involves three steps:
1.Create a connection and credential alias for the custom guardian and complete its setup. The
alias supports Basic Auth, OAuth 2.0, and API Key credential types.
For more information, see Create a Connection & Credential alias .

<!-- page 133 -->
2. Create a custom guardian in the Generative AI Custom Guardian Transformer
[sys_generative_ai_custom_guardian_transformer_list.do] table.
For more information, see Create a custom guardian.
3. Select your preferred guardrail service providers to monitor content.
For more information, see Setup a Guardrail Service Provider.
Create a custom guardian
Create your own custom guardian to monitor and detect requests sent to LLM.
Before you begin
Configure a connection and credential alias for your preferred provider. For more information,
see Create a Connection & Credential alias .
Role required: admin
Procedure
1.Navigate to All, and then enter
sys_generative_ai_custom_guardian_transformer_list.do
in the filter to go to the Generative AI Custom Guardian Transformer
[sys_generative_ai_custom_guardian_transformer_list.do] table.
2. Select New.
3. In the Name field, enter the name of the custom guardian.
4.Create a request transformer script.
a.In the Request Transformer filed, enable the Turn on ECMAScript 2021 (ES12) mode toggle
to create script.
The following example shows the request transformer script for the custom guardian request
structure.
((function(inputs) {
/*
inputs structure: {
prompt: object, The textual content that needs to be
evaluated with guardian
threshold_setting: object
connection_attributes: object
}
write code here to construct the request body and any custom
headers needed using the inputs object.
*/
// construct body using the inputs like input.prompt and so
on.
var body = {};
//construct headers using the inputs
var headers = {};
return {
body: body,
headers: headers
};
})(inputs);

<!-- page 134 -->
5. Select the Active option.
6.Create a response transformer script.
a.In the Response Transformer filed, enable the Turn on ECMAScript 2021 (ES12) mode
toggle to create script.
The following example shows the response transformer script for the custom guardian
response structure.
(function(inputs) {
/*
write code here to transform the custom guardian response
into standard guardian response format expected by platform
inputs structure: {
response_body: object,
threshold_setting: object
}
*/
// write code here to populate the response object.
var guardianResponse = {};
//Set flagged to true, if the guardian has flagged the text.
Categories are optional and are for logging purpose only
// if transformer setting is Prompt Injection, expected
response format: {security:{flagged:false,categories:[]}}
// if transformer setting is Offensiveness, expected
response format: {safety:{flagged:false,categories:[]}}
// if transformer setting is ALL, expected response format:
{safety:{flagged:false,categories:[]},security:{flagged:fals
e,categories:[]}}
return guardianResponse;
})(inputs);
7.In the Guardian Setting field, select a guardrail of your choice.
◦Select All to handle the detection of both offensiveness and prompt injection together.
◦Select Offensiveness to enable the detection of offensive or harmful content.
◦Select Prompt Injection to enable the detection of prompt attacks.
Note: If your LLM can evaluate both offensiveness and prompt injection in a single
request, select All. If not, create separate guardrail records for each offensiveness and
prompt injection.
8.In the Connection And Credential Alias field, select the alias that you want to integrate with
your custom guardian.
9.Select Submit.
10.Set up the custom guardian token limit.

<!-- page 135 -->
a.Navigate to All > System Definition > Tables.
b.Select the Gen AI Control Setting Data [sys_gen_ai_control_setting_data] table.
c.In the Related Links section, select Show List.
d. Search for the Custom Guardian Token limit record in the Gen AI Control Data column.
e. Update the Value field of the Custom Guardian Token limit record with the maximum number
of tokens per request.
The token limit defines the maximum number of tokens the guardrail can process in a single
evaluation. If the request content exceeds this limit, the content splits into smaller parts.
Each part is evaluated separately against the guardrail rules.
For example, if the token limit is 1000 and the request content is 2500 tokens, the system
splits it into three parts and evaluates each one individually.
Setup a Guardrail Service Provider
Select a guardrail service provider of your choice in Now Assist Guardian to monitor and detect
Now Assist interactions for harmful, offensive, and prompt injection content.
Before you begin
Role required: sn_nowassist_admin.nsa_admin
About this task
Now Assist Guardian supports multiple guardrail service provider types to monitor and detect
harmful content. Select a provider based on your organization's requirements. Only one provider
can be active at a time. For more information about supported service providers, see Configuring
a Guardrail Service Provider.
Procedure
1.Navigate to All > Now Assist Admin > Settings.
2. Navigate to Now Assist Guardian > Guardrail service providers.
3. In the Set default provider section, select a service provider from the list of guardrail service
providers.
4.Select Save and activate.
Result
The selected guardrail service provider monitors and evaluates all Now Assist interactions for
harmful, offensive, or prompt injection content.
Manage AI models
Access and select the LLM (large language model) provider used for various Now Assist skills.
The selection impacts all the skills within the capability.
Before you begin
Role required: admin, sn_nowassist_admin.nsa_admin
This feature is available in Now Assist Admin version 6.2 and Yokohama patch 6 onwards.
To enable the model provider selection, ensure that the skill is available in that region. The
configuration controls for the approved model providers and corresponding compliant skills

<!-- page 136 -->
for specific regions are approved in AI Control Tower by the AI steward. For example, to
update the model provider for Now Assist Q&A Genius Results, ensure that all the skills under
Conversational skills are available and active in the region.
As per the AI Control Tower settings, the model provider selection is available at multiple levels,
including skill, skill group, and instance levels in Now Assist Admin. Therefore, in a situation
where a skill is not compliant or a model provider is unavailable in a particular region, Now
Assist Admin console presents the admin persona with alternate region scope options seeking
approval permissions to proceed with model provider selection. For example: You opt to switch
to another model provider to use a particular Now Assist skill. Consider, the region scope must
be changed to global location for the skill to work. Here, you can proceed only after consenting to
the region scope change.
Note: For regulated markets:
•The Manage LLM option will not be available to customers on the Now Assist Admin user
interface.
•Only Now LLM Service skills will be available to customers. Any skill that leverages
external providers (e.g., Azure) will be hidden on the Now Assist Admin console. With the
exception of NSC region, skills leveraging Azure OpenAI is available to the users.
Procedure
1.Navigate to All > Now Assist Admin > Settings.
2. Navigate to Settings > Manage model providers.
3. Review these on the Manage model providers page:
◦Policy Summary set by your organization about skills using non-compliant model providers.
Note: Note the routing and fallback exception details. These details are also derived
from the AI Control Tower configurations.

<!-- page 137 -->
◦Model providers assigned to the Now Assist skills and skill groups.
◦Policy and skill updates by the AI steward in AI Control Tower under the Change History tab.
Manage model providers
Edit or customise the model provider for a skill or skill group at the instance level from the list
of supported third party model providers, including the default Now LLM Service. You can also
review the model policy set by your organisation, and view the change history here.
Before you begin
Role required: admin
Let's take an example of editing the model provider for skill group.
Procedure
1.Navigate to All > Now Assist Admin.
2. Navigate to Settings > Manage AI models.
3. Select Manage model providers.
4.Select Edit model provider to edit the model provider for the instance or customize it to update
it at the skill or skill group level.
5. Select Instance scope to update the model provider for all the skills and skill groups in the
instance.
a.Choose the Default model provider and select Save and activate to update your selection.
The impacted skills and skill groups will display alongside.
b.Select Save to update the model provider.
You will receive a confirmation message if you have reviewed the change and the impact.
Note: The agreement acceptance message is displayed only for the first time user.

<!-- page 138 -->
6.Edit the model provider for a skill or skill group, after selecting the instance level model
provider.
This customization will override the instance level selection and update all capabilities
associated with that group.
7.Select Customize to select the model provider for a particular skill or skill group.
a.Select the Default model provider for specific skill or skill group.
Select the skill group as AI agents to change the model provider for Now Assist in Virtual
Agent.
b.Select Save and activate to update your selection.
Note: The Websearch AI search answers skill is only compatible with Google Gemini as
the LLM provider. If you want to change the LLM provider to Azure OpenAI for this skill,
see Configure AI Search answers capability for web search for more information.
8.Select Cancel, go back to revert or Yes, activate to save the updates.
The status summary of skills for which the model provider change updated successfully or
failed, displays.
9.Review and accept the consent modal message to accept the terms for changing the region
scope of the selected model provider.
There are certain market regions restricted for particular model providers. The region scope
must be changed to global location for the skills to be able to use the selected model provider.
10.Select Yes, activate to accept and apply the selection.
You receive a message confirming model provider selection. The selection will also notify if any
of the skills within that capability are not updated with the selection.

<!-- page 139 -->
Note: The skill and skill level customizations are overwritten once you update the model
providers at the instance level.
You can also select Cancel, go back to review or reject the changes.
11. Follow similar steps for editing the model provider for a particular skill.
Manage Integration
Choose the preferred integration type for configuring the available model providers. There are
two ways to configure a model provider in Now Assist Admin. You can either select Original
Equipment Manufacturer (OEM) or Bring Your Own Key (BYOK).
Before you begin
Role required: admin
With Bring Your Own Key (BYOK) option, you can apply your own license key to use the
Generative AI application capabilities from the given provider. The alternate option is OEM
®
where, ServiceNow uses license from the provider to access the Generative AI application
capabilities.
Procedure
1.Navigate to All > Now Assist Admin.
2. Navigate to Settings > Manage integration.
®
3. Change the model provider to use either the ServiceNow key or Bring Your Own Key (BYOK)
across all the third party model providers.
This enables Bring Your Own Key (BYOK) selection for third party model providers across all
features except AI Agents.
4.Select the integration type for the providers that allow such a configuration.

<!-- page 140 -->
You can find the providers that allow BYOK type integration only, under Non Managed
integration section.
Manage version
Manage the version of the model providers across skills and instance levels. You can change
and update versions for the out-of-box and custom skills.
Before you begin
Role required: admin
See Default and target model version to know more about default and target model versions.
Procedure
1.Navigate to All > Now Assist Admin.
2. Navigate to Settings > Manage AI models.
3. Select Manage model version.
4.View the summary of the active, deprecated, retiring model versions, and recommended
actions, providing effective version management system to the admins.
Note: A model version will not be available for selection as target model version, if it is
in deprecated, retired, in review or rejected state.
5. Identify your use case and key factors to choose the model that best fits your needs.

<!-- page 141 -->
6.View or update the model version instantly under the Overview tab.
7.You can edit the model provider version for out-of-box or custom skills for the instance or
customize it to update it at the skill or skill group level, under the respective tabs.
Customizing the model version for skills replaces the instance-level model version currently
assigned to each provider. This action is typically reserved for specific situations.
8.Select Instance level configuration to manage the model provider version for the skill across
the instance.

<!-- page 142 -->
a.Select Out-of-box skills to set the target model version against the current version of the
applicable model providers, for the default skills.
b.Select Custom skills to set the target model version against the current version of the
applicable model providers, for the custom skills.
c.Select Save and activate to update your changes.
d. Select Update model version to override ServiceNow shipped mappings or create a new
default and target model versions mapping.
9.Select Skills to manage the model provider version at the skill level.

<!-- page 143 -->
a.Search or select the skills you wish to refresh the model version for, and the applicable
model provider.
b.Select the default and the target model provider version.
c.Select Save and activate to update your changes.
d. Select Update model version for skills to override ServiceNow shipped mappings or create
a new default and target model versions mapping, at the skill level.
Review Now Assist account
Review your Now Assist license details on the Account page of the Now Assist Admin console to
make sure that you're up to date on what's available to you.
Before you begin
Role required: sn_generative_ai.nsa_admin
About this task
From the Account page, you can review the licensing information to verify which plugins and
features you're entitled to and what their status is.
Procedure
1.Navigate to All > Now Assist Admin > Settings.
If you’re already in the Now Assist Admin console, select the Settings tab.
2. In the Settings page, select Account.

> **[Screenshot: Multi-language support – Microsoft Azure OEM Translator Configuration form]**
> ServiceNow form record for a Translator Configuration named "Microsoft Azure OEM". Form fields: Name: "Microsoft Azure OEM", Version: "v4", Active: checked. Two tabs: "Preferences" (active) and "Language Code Mappings". Under Preferences: "Choose a translate subflow" with "Translate Text" selected and a search icon; "Mark as default for translation" checkbox (unchecked). "Choose a detect subflow" with "Detect Language V4" and a search icon; "Mark as default for detection" checkbox (unchecked). Bottom buttons: Update, Delete.