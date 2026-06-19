# Deploy AI voice agents

_Source pages: 137–195 | Depth: 1_

---

<!-- page 137 -->
Delete an agentic workflow
Delete an agentic workflow from AI Agent Studio.
Before you begin
Role required: sn_aia_admin
About this task
You must assign appropriate permissions by using the access control lists (ACLs) to delete
agentic workflows in AI Agent Studio.
Note: You can't delete the default agentic workflows.
Procedure
1.Navigate to All > AI Agent Studio > Create and manage > Agentic workflows.
2. Select the check box of the agentic workflow that you want to delete and select Delete.
You can also delete multiple agentic workflows by selecting multiple agentic workflow records
at a time.
Note: Some agentic workflows installed with Now Assist applications can't be deleted.
3. In the confirmation pop-up window, select Delete.
Result
The selected agentic workflows are deleted from the Agentic workflows list AI Agent Studio.
Deploy AI voice agents
AI voice agents are generative AI-powered agents that bring natural, conversational experiences
to phone-based support. As part of the broader AI agent ecosystem, they connect with
telephony providers to replace rigid menu trees with seamless and human-like interactions that
can help make support faster and more intuitive.
AI voice agents overview
AI voice agents use generative AI to deliver natural, dynamic conversations that help users
complete tasks, resolve issues, and access information.
AI voice agents are part of the ServiceNow AI Platform capabilities and can be deployed from
the base system or customized to meet specific business needs. AI voice agents are managed
through the AI Agent Studio, which provides tools for creating, deploying, and monitoring AI
voice agents.
AI voice agents are associated with voice assistants, which act as a virtual help desk. A voice
assistant can host multiple AI voice agents. Each AI voice agent is equipped with specific AI
instructions, tools, and knowledge to resolve user issues. You can configure welcome messages,
select voice profiles from the voice library, and define fallback options like live agent routing or
record producer-based ticket creation.
When you create or edit a voice assistant, you configure communication channels to define how
the voice assistant connects to users. Communication channels are organised into two tabs:

<!-- page 138 -->
•Telephony provider — connects the voice service to phone networks. Select a communication
channel type, then select a CCaaS provider.
•Web Real-Time Communication (WebRTC) — connects the voice service to mobile
applications.
Note: AI voice agents support the following:
•LLMs (large language model): Azure OpenAI, Google Gemini, and AWS Claude. Now
LLM Service is also supported but limited to English language only.
•Telephony providers: Twilio (WebSocket), Genesys (WebSocket and SIP), Amazon
Connect (PSTN), 3CLogic (WebSocket), and Five9 (SIP). Mobile and web applications are
supported through the Web Real-Time Communication (WebRTC) channel.
Deploying AI voice agents
To get started with AI voice agents, perform the following steps.
1.Install Now Assist AI voice agents
2. Configure user identification and authentication
3. Create an AI voice assistant
4.Create an AI voice agent
5. Test AI voice agents
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
For more information, see the Now Assist documentation.
Privacy notice
By using this feature, you confirm that your use (including use by your service providers) complies with relevant anti-wiretapping, recording consent, and other
privacy laws, as applicable.
Related topics
HR Voice AI agents
Agentic AI in the Voice application

<!-- page 139 -->
Install Now Assist AI voice agents
Install Now Assist AI voice agents on your ServiceNow instance to enable voice-based support
through agentic AI experience.
Before you begin
Role required: sn_aia_admin
About this task
AI voice agents aren’t standalone applications that you can install directly. To enable
AI voice agents on your instance, you must install and activate Now Assist for Platform
(sn_genai_platform), which is the base application for platform AI voice agents. Now Assist for
Platform is auto-installed with any of your Now Assist products, for example, Now Assist for IT
Service Management (ITSM) and Now Assist for HR Service Delivery (HRSD).
Procedure
1.Navigate to All > System Definition > Plugins.
2. Search for the following plugins.
◦Now Assist for Platform (sn_genai_platform) for enabling default platform AI voice agents
◦IT Service Management AI voice agent collection (sn_itsm_voice_aia) for enabling default
ITSM AI voice agents. See Agentic AI in the Voice application for more information.
◦HR Voice AI Agents (sn_hr_voice_aia) for enabling default HRSD AI voice agents. See HR AI
voice agents for more information.
3. Select Install to install each of the required plugins.
Result
AI voice agents associated with the applications are installed on your instance.
Create an AI voice assistant
Create an AI voice assistant to enable natural, conversational voice interactions between users
and AI voice agents.
Before you begin
Role required: virtual_agent_admin or admin
Set up your preferred user identification and authentication methods to allow access to AI voice
agents. See Authentication factors for more information.
About this task
An AI voice assistant enables natural, conversational voice interactions between users and
AI voice agents. It uses speech-to-text (STT), large language model (LLM), and text-to-speech
(TTS) to understand and respond to callers in real time. You can configure a voice assistant
with personalized voice and welcome message, fallback options, and assign AI voice agents
with specific AI instructions. The fallback options include live agent transfer and ticket creation,
based on the origin of the call.
Procedure
1.Navigate to All > Conversational Interfaces > Assistant Designer > Assistants and select
Create assistant.
2. Select Voice-only option in the Create an assistant window and select Continue.

<!-- page 140 -->
Voice-only option in Create assistant
3. Add basic details of the assistant.
Basic details form
a.On the form, fill in the fields.
Basic details form
Field Description
Name
Name of the voice assistant. Provide a name
according to the business outcome that the
voice assistant targets.
For example: HR Service Desk
Description
Brief summary of the business outcomes
that your voice assistant targets.

<!-- page 141 -->
Field Description
Example for the HR Service Desk: HR
service desk to help resolve employee
requests and inquiries.
Tags Add tags to track analytics for the voice
assistant. For example, HR.
Adding or removing tags will apply the
changes immediately. These will be tracked
in analytics.
b.Select Save and continue.
You’re directed to the AI agents page.
4.Add one or more AI voice agents to the voice assistant by selecting Add from library and
select Save and continue.
Note: Adding AI agents is optional. If no AI agents are added, you can add them later
by editing this assistant. The assistant will be inactive. Select Add from library to add
an existing agent, or select Create to create a new one. See Create an AI voice agent for
more information.
5. Select a voice personality.
Voice personality selection
a.Select the primary language your assistant will use for interacting with callers.
You can configure a primary language and up to three secondary languages. You can select
from the following languages:
▪English
▪German
▪Spanish

<!-- page 142 -->
▪Japanese
▪Korean
▪Dutch
▪Brazilian Portuguese
▪Italian
▪Mandarin Simplified
▪French
▪Canadian French
▪British English
▪Mexican Spanish
▪Thai
▪Hindi
▪Danish
▪Russian
▪Turkish
See Multilingual support for voice assistants for more information.
b.Add a personalized welcome message to greet the callers calling into the voice assistant.
c.On the Voice persona tab, select a voice persona that best suits the conversational
experience that you want to deliver through the voice assistant.
Preview the voice samples to determine the appropriate voice and tone. All AI voice agents
connected to the voice assistants share the same voice.
d. Optional: Select + Add language to add secondary languages.
For each secondary language, select the corresponding voice persona. The order of
secondary languages reflects the caller experience during language selection.
e. Optional: On the Pronunciation dictionary tab, add custom pronunciations for domain-
specific or company-specific terms.

<!-- page 143 -->
Pronunciation dictionary
Select Add entry and provide the word or phrase and its pronunciation in either phonetic
spelling or phoneme format. Pronunciation entries are specific to the selected language and
are applied during voice interactions.
f.Select Save and continue.
You’re directed to the Communication channels page.
6.Set up communication channels for the user to interact with the assistant.
Select a Provider application to deploy this voice assistant to. This field is required for all
communication channel types.
Configure at least one communication channel to activate the voice assistant.
Communication channels step

<!-- page 144 -->
a.Select the Telephony provider tab to connect the voice assistant to a phone network.
Select a communication channel type from the Communication channel dropdown, then
select a CCaaS provider and configure the required fields. For more information, see
Integrating voice assistant with CCaaS provider.
b.Select the Web Real-Time Communication (WebRTC) tab to connect the voice assistant to
mobile and external applications.
Select Mobile applications to configure ServiceNow applications such as chat launcher
functions, voice launcher functions, and prominent action button overrides. You can also
configure external applications. For more information, see Integrate voice assistant with
mobile app voice launcher.
c.Select Save and continue.
You're directed to the Caller verification page.
7.Identify and authenticate the caller.
Authentication settings apply only to telephony provider communication channel. If you have
selected only mobile communication channel, skip this step.
Caller identification and authentication method selection
Identification and authentication factors must be configured at the platform level, where
you define which tables and columns the system should use for both identification and
authentication. After the factors are defined, they appear here as selectable options for your
voice agent configuration. For more information, see Authentication factors .
a.Select the method used to identify the caller when the call begins.
Caller identification determines who the caller is before any authentication occurs. The
information provided by the caller is matched with system records to identify the caller. If you
select phone number as the primary identification method, enable the checkbox to allow the

<!-- page 145 -->
system to automatically match the caller’s phone number to the incoming caller Id received
from the telephony system.
b.Optional: Select the fallback method to identify the caller.
If the caller can't be uniquely identified through the primary method, the system
automatically retries using the fallback method.
c.Enable caller access to AI voice agents by selecting the authentication type, First factor, and
Second factor methods.
Caller authentication verifies the caller’s identity before allowing access to AI voice agents
that require authentication.
Select from the following authentication types.
▪Multi-factor authentication (MFA) requires callers to successfully complete more than
one verification method configured before the system grants access. MFA is required by
default.
▪Single factor authentication requires the user to complete the configured
verification method. To enable single factor authentication, you must set the
glide.voice.authenticate.mfa_mandatory system property to false.
Select from the following First factor authentication methods.
▪Knowledge-based authentication (KBA)
▪Okta Verify push notification
▪SMS verification code
▪Authenticator app time-based One Time Password (TOTP)
▪Soft PIN
▪Email one-time password (OTP)
Select from the following Second factor authentication methods.
Numeric authentication factors such as SMS verification code, Authenticator app time-based
One Time Password (TOTP), and Soft PIN support voice input. Callers can respond verbally
instead of using the keypad. Voice input for each factor can be configured at platform level
and scoped per voice service. See Authentication factors for more information.

<!-- page 146 -->
Note: The option selected as the First factor is not available in the Second factor
dropdown. KBA authentication, for example, employee security questions, requires
questions to be configured at platform level with the Channel field set to Voice and the
Type field set to Identification, Authentication, or both. Questions configured this way
automatically appear in Assistant Designer for selection. Explicit service mapping is not
required.
Base system questions are available out of the box for the voice channel at both
the identification and authentication levels and are ready to use without additional
configuration.
For secure and consistent verification, KBA authentication factor must use numeric
data only, for example, date of birth, Social Security Number, or employee Id.
Additionally, the source table used must reference the sys_user table so that
caller identity can be validated reliably across the platform. See Knowledge-based
authentication (Security Questions) for more information.
KBA now also supports external authentication. The caller's system ID and their spoken
response are passed to a verification script, which checks the answer against an
external system and returns a true or false result. Optionally, context from earlier
responses in the same session can be passed to the script. Configure external
authentication scripts at platform level.
Email OTP authentication requires platform-level configuration before it can
be selected here. Configure the email field and source table in the Email OTP
configuration screen. By default, the email address is sourced from the sys_user table.
The source table must reference the sys_user table, and the selected column must be
an email field. Email OTP configuration can be scoped to a specific voice service. See
Email One-time passwords (OTP) authentication for more information.
d. Optional: Enable the Authenticate at the start of the call option to prompt callers for
authentication or identification details before the voice assistant responds to any request.
When enabled, every caller is prompted to complete authentication or identification at the
start of the call, regardless of which AI voice agent handles the interaction.
e. Select Save and continue.
You’re directed to the Safeguards page.
8.Set up safeguards to create a secure and seamless experience for users interacting with the
assistant.

<!-- page 147 -->
Safeguards selection
a.Set fallback options to route the call to a live agent or create a ticket.
When a voice agent cannot complete a user's request, the system determines the
appropriate fallback behavior based on the call origin, for example, telephony provider or
mobile channel.
▪Telephony provider requires either connect to live agent or a record producer as fallback
option.
▪Mobile channel requires a record producer as fallback option.
▪Connect to live agent option. When selected, this option redirects the caller to a live
agent. You must set up live agent transfer for your telephony provider separately.
Note: You can enable the Capture details before live agent handoff option, in
which the voice agent prompts the caller to provide details in order to triage the call
to the appropriate live agent.
▪Generate a ticket with record producer option. When selected, this option creates a ticket
for further tracking.
Note: If you choose to use generating a ticket with record producer as the fallback
option, you must keep the fields in the record producer simple and short to optimize
the user experience for both the communication channels. For example, a short
description, description, and an optional field for the callback number should
suffice. You can also enable the Require authentication option, which restricts ticket
creation to authenticated employees.
b.Set the time limits for call duration and reprompting users after inactivity.
▪Set Max call duration to trigger fallback behavior when the call reaches this limit. You can
set up to 10 minutes.
▪Set the duration of inactivity after which the user is reprompted for a response. If there's
still no response, the call is disconnected. You can set up to 300 seconds.
c.Select Save and continue.
You're directed to the Advanced settings page.

<!-- page 148 -->
9.Configure advanced settings for the voice assistant.
Advanced settings let you configure supplementary features for the voice assistant.
a.In the Noise cancellation section, select the level of background noise cancellation
intensity.
Noise cancellation reduces background noise from the caller's side so the voice agent can
better hear them. Select from the following levels:
▪Low: Picks up even the quietest background noises. Use in quiet environments where
background sounds such as TV or music may be present.
▪Medium (default): Picks up somewhat quiet background noises. Use in environments with
moderate background noise, such as public places or areas with normal talking.
▪High: Picks up only the loudest background noises. Use in very noisy environments such
as construction sites or areas with loud background speech.
b.Select Save and continue.
You're directed to the Review page.
10.Review your voice assistant configuration.
You can change the configuration later.
11. Select Save and activate to complete the configuration steps or review a previous step by
selecting Back.
Activating the assistant also activates any inactive AI agents associated with it.The following
conditions must be met in order to activate the assistant. If any of these conditions are not met,
select Save and close to return later.
◦At least one communication channel is selected (telephony provider or mobile channel)
◦At least one AI agent is associated with the assistant
◦If a telephony provider is enabled, authentication is set up and fallback is configured to
either connect to a live agent or create a record producer.
◦If a mobile channel is enabled, fallback is configured to create a record producer.
What to do next
Test the execution of your AI voice agent by manually calling in the telephony number to
see if the AI voice agent functions the way you defined it. Review the transcript and logs for
troubleshooting and improving the conversational experience of users. See AI voice agent
transcript and logs tables for information on the tables containing transcript and logs.
Configure custom assistant
Configure a custom telephony provider to use instead of the out-of-the-box voice assistant.
Before you begin
Role required: admin
Procedure
1.Configure the token by doing one of the following, depending on the token type:
◦Static token:
a.Navigate to All, and then enter token_verification.list in the navigation filter.
b.Select New.

<!-- page 149 -->
c.On the form, fill in the fields.
Token Verifications form
Field Description
Name Name of the authentication token, such as AI voice token.
Description Description of the authentication token, such as Voice Agent Auth
Token.
Token Authentication token that is used to authenticate the provider application.
Enter the authentication token that you generated using any general
programming or scripting language, or select the Generate Secure Token
related link.
d. Select Submit.
◦Hash token:
a.Navigate to All, and then enter hash_message_verification.list in the
navigation filter.
b.Select New.
c.On the form, fill in the fields.
Hash Message Verification form
Fields Description
Name Name of the authentication token, such as AI voice token.
Description Description of the authentication token, such as Voice Agent Auth
Token.
Secret Authentication token (random string).
d. Select Submit.
2. Set up Provider Authentication for token-based authentication.
a.Navigate to All, and then enter message_auth.list in the navigation filter.
b.Select New.
c.On the form, fill in the fields.
Message Auth form
Field Description
Name Name of the message authentication, such as AI voice
token.
Provider Name of the provider, for example, AI Voice provider.
Group name Not required.
Service Portal Not required.

<!-- page 150 -->
Field Description
Inbound message Select the Static token or Hash message token that you
verification created.
Outbound message Select the Static token or Hash message token that you
creation created.
Outbound service token This field is not supported.
d. Select Submit.
3. Set the channel identity.
a.Navigate to All, and then enter sys_cs_provider_application.list in the
navigation filter.
b.Select the AI Voice Agent Provider Application record to open it.
If you want to use an existing application or create a new provider application, be sure to
update the existing configuration according to the values mentioned in Configuration for
custom AI voice agent provider before proceeding further.
c.In the Provider Channel Identity form, locate the Message auth field and select the message
auth that you set up previously.
d. Select Update.
Create an AI voice agent
Create an AI voice agent in the AI Agent Studio to resolve cases, incidents, or tasks through the
phone channel.
Before you begin
Role required: sn_voice_aia.admin
Procedure
1.Navigate to the New AI Agent page in the Assistant Designer or AI Agent Studio.
To Do this
Navigate in Assistant Designer
a.Go to the Asset Library and select Create
asset.
The Create asset window appears.

<!-- page 151 -->
To Do this
b.Select AI Agent.
You are redirected to the New AI Agent
workflow in the AI Agent Studio.
Navigate in AI Agent Studio
a.Go to All > AI Agent Studio > Create and
manage and select the AI agents tab.
b.In the Add drop-down list, select Voice to
create an AI voice agent.
2. On the Define the specialty page, describe your AI agent and provide instructions on how you
want your AI agent to perform its tasks.
Select Generate details to generate a description and instructions with Now Assist. If you
provide the description of what you want the agent to do, you can select Generate to write the
name, description, AI agent role, and instructions fields for you. You can change those fields
after the text has been generated or try again with new instructions.
Note: The more details that you provide, the more accurately your AI agent can perform.
a.On the form, fill in the fields.
Give a unique name and description form
Field Description
AI agent name
Name of the AI agent. Provide a name
according to the outcome that you want your
AI agent to achieve.
For example: Incident manager.
AI agent description
Brief summary of what your AI agent can do
autonomously. Outline all the activities that
you want your AI agent to perform.
Example for the Incident manager: The
Incident manager AI agent assists users
with existing incidents by gathering
information over the phone, matching it to
records in the system, and sharing relevant
incident details. It can also make limited
updates to the incident using preconfigured
tools.
b.On the form, fill in the fields.

<!-- page 152 -->
Note: The AI agent uses this information as guidance to tailor its responses and
actions.
Define the role and required steps form
Field Description
AI Agent role
Capabilities and responsibilities for your AI
agent. Roles enable your AI agent to perform
its required actions.
Example for the Incident manager: You’re an
AI agent with the purpose of communicating
incident details and making changes to
those incidents for users calling in as long
as they match the caller for those incidents.
You have access to tools that can retrieve
a few fields for incidents, comments, and
escalate the urgency. Only proceed with
gathering information and tool execution
if the user and caller listed on the incident
match.
List of steps
Necessary steps to be followed by the AI
agent while carrying out its role.
Note: The instructions are sent to the
large language model (LLM).
Example for the Incident manager: Incidents
are records for tracking issues and their
resolution updates through a set of journal
entries. Your objective is to act as an
incident manager. If the user provides an
incident number, verify the caller identity
before sharing permitted details. If no
number is given, match incidents using the
short description and confirm with the user.
Allow updates only if the user matches the
caller. Offer live agent transfer if the user is
unsatisfied.
To resolve an incident:
i. Verify the caller number.
ii.Search for incident records associated
with the user.
iii. Consider the context and relationship
between different data points.
iv.If the user provides an incident number,
verify their identity against the caller field
before sharing permitted details. Proceed
with updates or modifications only after
the caller's identity is verified.

<!-- page 153 -->
Field Description
v. If no incident number is given, search
using the short description, list matching
incidents with brief summaries, and
confirm which one the users wants to
explore further.
vi. Only share allowed fields (for example,
incident number, caller, dates, urgency,
state, short description, comments).
Summarize comments if there are more
than five, and notify the user if a field is
empty or restricted.
vii.If the user is unsatisfied, offer to transfer
to a live agent. End the conversation
politely if they’re satisfied or after a
transfer.
Follow these guidelines for writing effective Instructions:
▪Define the AI agent's role:
▪Clearly state the primary function of the AI agent in one or two sentences.
▪Example: The AI agent acts as a customer service assistant.
▪Outline specialties:
▪Specify the key areas or tasks that the AI agent handles.
▪Example: Specializes in handling inquiries and resolving customer issues.
▪Identify the business problem:
▪Articulate the specific business challenge for the AI agent to address.
▪Example: Reducing customer wait times by 50%.
▪Describe the workflow:
▪Provide a brief scenario of how the AI agent is to be used.
▪Example: Automating responses to common queries and escalating complex issues to
human agents.
▪Be concise and clear:
▪Use simple and direct language.
▪Avoid jargon and technical terms.
▪Example: The AI agent helps customers find answers quickly.
▪Provide actionable steps:
▪Include specific instructions on how to set up and use the AI agent.
▪Example: Step 1: Define the types of inquiries the AI agent handles. Step 2: Integrate the
AI agent with the customer service platform.

<!-- page 154 -->
▪Include examples:
▪Provide real-world examples to illustrate how the AI agent should function.
▪Example: For example, the AI agent can automatically respond to questions about the
order status.
▪Focus on outcomes:
▪Emphasize the benefits and outcomes of using the AI agent.
▪Example: Using the AI agent leads to faster resolution times and higher customer
satisfaction scores.
By following these general guidelines, you can create clear and effective prompt instructions
that enable you to use AI agents to their fullest potential. For more information and
examples, see General guidelines for creating AI agents.
c.Optional: Determine if the AI agent can be accessed by third parties.
Making your AI agent discoverable allows you to use your ServiceNow AI agent on other
platforms. You can still use it on your ServiceNow instances as well.
d. Select Save and continue to move to the next step.
3. In the Add tools and information tab, configure additional tools and data sources that provide
capabilities necessary to your AI agent to accomplish its objectives.
Select Recommend Tools for Now Assist to suggest the tools that are required for the AI
agent to carry out the tasks that it's built for. Now Assist suggests tools based on the AI agent
description and instructions given in the previous section.
You can add the tools suggested by Now Assist or manually select the tools from the Add tool
drop-down list. You must add at least one tool to continue setting up your AI agent, but you can
also add more tools to your AI agent. The data input and output type for tools must be string for
optimal voice experience.
The following tools are available for AI voice agents:
◦File upload: Different file types such as PDF, DOCX, or TXT formats that you can add to your
AI agent.
◦Flow action: Custom automated processes in your system that you can add to your AI agent.
Example for the Incident manager agent: Fetch details of the incident.
◦Knowledge Graph: Various Knowledge Graph items that you can add to you AI agent.
◦MCP server tool: An MCP server tool that you can to your AI agent.
◦Record operation: Different record operations that you can add to your AI agent.
◦Script: Editable scripts and APIs that you can add to your AI agent.
◦Search retrieval: Information retrieval processes in your system that you can add to your AI
agent.
Note: Create a dedicated search profile that includes only the KB articles for AI voice
agents to reduce the search scope and minimize latency.
◦Sub flow: Automated flows in your system that you can add to your AI agent.

<!-- page 155 -->
4.In the Define security controls tab, define who can access the AI agent and what data the AI
agent has access to.
a.Define the users who can access this AI agent (ACLs).
Choose from:
▪Any authenticated user: A user who is logged in can access the AI agent.
▪Users with specific roles: Users that are assigned specific roles can access the AI agent.
Selecting this option enables you to select the roles in the Role drop-down list.
▪Public: Anyone can access the AI agent, even without logging in.
b.Optional: If you selected Public, select Require caller identification to have the AI voice
agent identify the caller before the conversation begins.
(Optional) When selected, the agent uses the caller identification methods configured
in the Caller Identification section of the voice assistant to match the caller to a name.
Identification does not authenticate the caller or grant additional access. The session
continues with public user permissions.
Note: This option is available only for voice agents configured with Public access.
c.Define the user identity of the AI agents to determine what data it has access to.
The default selection is Dynamic user, in which the user passes their roles to the AI agent
which allows the AI agent to run as the user that invokes it. The user's ACLs determine the
data accessible to the AI agent.
5. Select channels and activation status for your AI voice agent.
a.Select Allow to enable users to use phone calls to invoke the AI agent.
b.In the Voice assistants field, select Now Assist Voice Deployment or a custom provider.
Voice assistants are created in Assistant Designer. See Create a voice assistant for more
information.
c.Activate the AI agent by toggling the Status.
d. Optional: Select Test in assistant to test your AI voice agent in the voice testing experience.
▪If one voice assistant is linked, the voice testing panel opens directly.
▪If multiple voice assistants are linked, select the voice assistant you want to use for testing.
▪If no voice assistants are linked, Test in assistant is disabled. Link a voice assistant first.
6.Select Done to save the configuration.
Integrating voice assistant with CCaaS provider
Enable users to get voice-based support from ServiceNow AI voice agents by integrating
ServiceNow voice assistant with supported third-party Contact Center as a Service providers
(CCaaS).
When you create or edit a voice assistant, you configure communication channels to define how
the assistant connects to users. Select a Provider application to deploy the assistant to — this
field is required for all communication channel types and appears above the channel tabs.

<!-- page 156 -->
Communication channels are organized into two tabs:
•Telephony provider — connects the voice assistant to a phone network.
•Web Real-Time Communication (WebRTC) — connects the voice assistant to mobile
applications.
Note: To configure a telephony provider, select a communication channel type from the
Communication channel drop-down, then select a CCaaS provider. The available CCaaS
providers depend on the selected channel type. To remove a linked provider, select Unlink
this provider.
Telephony providers
The following sections describe the configuration fields for each supported CCaaS provider
under the Telephony provider tab.
Twilio voice service (WebSocket)
Twilio voice service configuration fields
Field Description
Phone number to live agent Phone number to connect the caller to a live agent when
required.
Authentication Token Authentication token to authenticate to your Twilio voice
service account.
URL Read-only. Autogenerated URL to connect Twilio voice service
to the voice assistant.
Genesys voice service (Audio Connector)
Genesys uses the Audio Connector integration and the WebSocket channel type. After the
configuration is saved, copy the generated credentials and paste them into your Genesys Cloud
account to complete the integration.
Genesys Audio Connector configuration fields
Field Description
Base connection URI Read-only. Autogenerated WebSocket URL to connect the
Genesys Cloud Audio Connector to the voice assistant. Copy
this value to your Genesys Cloud account.
Connector ID Read-only. Autogenerated identifier for the Genesys Cloud
Audio Connector. Copy this value to your Genesys Cloud
account.
Client secret Read-only. Base64-encoded client secret for secure access.
Copy this value to your Genesys Cloud account.
API key Read-only. API key to authenticate your Genesys Cloud service
to the voice assistant. Copy this value to your Genesys Cloud
account.

<!-- page 157 -->
Genesys voice service (SIP)
Genesys voice service configuration fields
Field Description
Transfer number/address SIP URI to transfer the call to the Genesys voice service. Use
the format user@domain, where the user part is up to 16
characters and the domain part is up to 256 characters. URI
parameters are not supported.
Transfer method Read-only. Set to REFER for Genesys voice service.
ServiceNow SIP Trunk Read-only. The ServiceNow SIP fully qualified domain name for
information your region, used to route calls from Genesys voice service to
the voice assistant. For configuration details, see KB3023612 .
x-snc-param Read-only. Generated token to send to your Genesys CCaaS
account to authenticate requests to the voice assistant.
Amazon Connect (PSTN)
Amazon Connect configuration fields
Field Description
Transfer method Read-only. Set to BYE for Amazon Connect.
ServiceNow call context Read-only. The URL used by Amazon Connect to send call
context data to the voice assistant when a call arrives.
Call context API Read-only. Authentication credentials (mTLS certificate or
OAuth2) used to secure call context requests from Amazon
Connect to the voice assistant.
Client ID Read-only. Generated client ID for OAuth2 authentication
of call context requests from Amazon Connect to the voice
assistant.
Client Secret Read-only. Generated client secret for OAuth2 authentication
of call context requests from Amazon Connect to the voice
assistant.
ServiceNow call context Read-only. Reference information for configuring the Amazon
information Connect call context in your AWS account.
3CLogic (WebSocket)
3CLogic uses the WebSocket channel type. After the configuration is saved, copy the generated
credentials and paste them into your 3CLogic account to complete the integration.
3CLogic configuration fields
Field Description
URL Read-only. Autogenerated WebSocket URL to connect the
3CLogic voice service to the voice assistant. Copy this value to
your 3CLogic account.

<!-- page 158 -->
3CLogic configuration fields (continued)
Field Description
Client ID Read-only. Generated client ID to authenticate requests from
3CLogic to the voice assistant. Copy this value to your 3CLogic
account.
Client Secret Read-only. Generated client secret to authenticate requests
from 3CLogic to the voice assistant. Copy this value to your
3CLogic account.
Web Real-Time Communication (WebRTC)
The Web Real-Time Communication (WebRTC) tab connects the voice assistant to mobile
applications.
For more information, see Integrate voice assistant with mobile app voice launcher.
Integrate ServiceNow voice assistant with Twilio voice service
Enable users to get support from AI voice agents by integrating a ServiceNow AI voice assistant
with the Twilio voice service.
Before you begin
ServiceNow AI voice assistant uses the authentication token of your Twilio account to connect to
the Twilio voice service. To obtain the authentication token, do the following.
1.Sign up or log in to your Twilio admin console.
2. Navigate to Account Dashboard > Account Info.
3. Copy your Account SID and Auth Token.
Role required: sn_aia.admin
About this task
Connect your Twilio voice service to a ServiceNow voice assistant using the WebSocket
communication channel. After the integration is configured, Twilio routes calls to the ServiceNow
voice assistant. When the interaction is complete, the integration supports transferring the caller
to a live agent.
Procedure
1.Navigate to All > Conversational Interfaces > Assistant Designer > Assistants.
2. Find the voice assistant that you want to connect to Twilio and select Edit.
3. Select Communication channels from the guided setup navigation.
4.In the Provider application field, select the provider application to deploy the voice assistant
to.
5. Select the Telephony provider tab.
6.From the Communication channel dropdown, select WebSocket.
7.From the CCaaS provider dropdown, select Twilio and fill in the fields.

<!-- page 159 -->
Twilio voice service configuration fields
Field Description
Authentication token Authentication token to connect the
®
ServiceNow voice assistant to your Twilio
voice service. Enter the Auth Token that you
collected earlier.
URL Read-only. Autogenerated URL to connect
®
Twilio voice service to the ServiceNow voice
assistant. Copy the URL for use in the Twilio
console.
If you do not see the URL, make sure
an endpoint is associated with the
sys_service record for AIVoiceAgents.
This endpoint is used to generate the URL
required for your integration. If no endpoint
is present in the record, click Refresh
Connections to populate it.
Twilio voice service integration configuration

<!-- page 160 -->
8.In the Twilio console, go to your purchased number's configuration and set the URL copied
earlier as the Webhook URL.
Twilio voice service configuration
Integrate ServiceNow voice assistant with Genesys Cloud service (Audio Connector)
Enable users to get support from AI voice agents by integrating a ServiceNow AI voice assistant
with Genesys Cloud service using the Audio Connector integration.
Before you begin
•Be aware of Genesys Audio Connector limits and throttling policies. See Organization rate
limits and Platform API rate limits for more information.
•Be sure to host the ServiceNow instance in a region the same as or closer to the region where
the Genesys Cloud service is hosted to minimize latency.
•If you want to route live agent transfer via Advanced Work Assignment (AWA), download and
install the Unified Experience from Genesys - Core and Unified Experience from Genesys
Store apps.
Role required: sn_aia.admin
About this task
Connect your Genesys Cloud contact center to a ServiceNow voice assistant using the Audio
Connector integration and the WebSocket communication channel. After the integration is
configured, Genesys Cloud routes calls to the ServiceNow voice assistant through the Audio
Connector. When call handling is complete, the integration supports transferring the caller to a
live agent queue.
Procedure
1.Navigate to All > Conversational Interfaces > Assistant Designer > Assistants.
2. Find the voice assistant that you want to connect to Genesys Cloud service and select Edit.
3. Select Communication channels from the guided setup navigation.
4.In the Provider application field, select the provider application to deploy the voice assistant
to.
5. Select the Telephony provider tab.

<!-- page 161 -->
6.From the Communication channel dropdown, select WebSocket.
7.From the CCaaS provider dropdown, select Genesys.
The following fields are generated. Copy these values to configure the Audio Connector
integration in your Genesys Cloud account.
Genesys Audio Connector configuration fields
Field Description
Base connection URI Read-only. Autogenerated WebSocket URL to connect your
Genesys Cloud Audio Connector to the ServiceNow voice
assistant. Copy the URL for use in the Audio Connector
configuration.
If you do not see the URL, make sure an endpoint
is associated with the sys_service record for
AIVoiceAgents. This endpoint is used to generate the URL
required for your integration. If no endpoint is present in the
record, click Refresh Connections to populate it.
Connector ID Read-only. Autogenerated identifier for the Genesys Cloud
Audio Connector. Copy the value for use in the Audio
Connector configuration.
Client secret Read-only. Base64-encoded client secret used to provide
secure access to the required resources. Copy the value for
use in the Audio Connector configuration.
For more information on Client secret and API key, see Client
Authentication .
API key Read-only. API key to authenticate your Genesys Cloud
service to the ServiceNow voice assistant. Copy the value for
use in the Audio Connector configuration.
Genesys Cloud service integration configuration
8.Create Audio Connector integration.

<!-- page 162 -->
a.Navigate to Menu > IT and Integrations > Integrations and select Add new integration.
b.Select Audio Connector as the integration type and select Install.
c.In the Details tab, name the integration, for example, Audio Connector - Voice.
d. In the Configuration tab, select Properties, and add the Base connection URI from your
ServiceNow voice assistant integration for Genesys Cloud in the Base connection URI field.
.
e. Select Credentials, and add the API key and Client secret obtained from ServiceNow voice
assistant integration for Genesys Cloud.
f.Select Save.
9.Architect the inbound call flow.
a.Use the search bar to navigate to Architect and create the inbound call flow according to
your requirements.
Note:
In the Connector ID field, enter the Connector ID obtained from creating ServiceNow
voice assistant integration for Genesys Cloud.
If you intend to use live agent transfer as the fallback option, add the transfer logic in
the call flow and validate the flow.

<!-- page 163 -->
Sample inbound call flow
b.Select Save to save and Publish to publish the call flow.
10.Configure call routing.
a.Use the search bar to navigate to Call Routing and create a call route.
For more information on creating a call flow routing, see Add a call route .
b.Assign the inbound call flow that you created earlier to the call route.

<!-- page 164 -->
c.Select Save.
11. Assign a phone number to the call route.
a.Use the search bar to navigate to Telephony and select DID numbers.
b.Select a DID number and assign the number to the call route created earlier.
Integrate ServiceNow voice assistant with Genesys Cloud service (SIP)
Enable users to get support from AI voice agents by integrating a ServiceNow voice assistant
with Genesys Cloud service using the Session Initiation Protocol (SIP) communication channel.
Before you begin
•Create a voice assistant. See Create an AI voice assistant for more information.
Role required: sn_aia.admin
About this task
Connect your Genesys Cloud contact center to a ServiceNow voice assistant using the Session
Initiation Protocol (SIP) communication channel. After the integration is configured, Genesys
Cloud routes calls to the ServiceNow SIP endpoint, where the AI voice agent handles the
interaction. When call handling is complete, the integration supports transferring the caller to a
live agent queue using the SIP REFER transfer method.
Procedure
1.Navigate to All > Conversational Interfaces > Assistant Designer > Assistants.
2. Find the voice assistant that you want to connect to Genesys Cloud service and select Edit.
3. Select Communication channels from the guided setup navigation.
4.In the Provider application field, select the provider application to deploy the voice assistant
to.
5. Select the Telephony provider tab.
6.From the Select communication channels dropdown, select Session Initiation Protocol (SIP).

<!-- page 165 -->
7.From the CCaaS provider dropdown, select Genesys.
Enter the Transfer number/address and note the following generated values. You will need
these to configure the SIP trunk in your Genesys Cloud account.
Genesys SIP configuration fields
Field Description
Transfer number/address SIP URI to transfer the call to your Genesys Cloud service.
Use the format user@domain, where the user part is up to
16 characters and the domain part is up to 256 characters.
URI parameters are not supported.
Transfer method Read-only. Set to REFER for Genesys Cloud service.
ServiceNow SIP Trunk Read-only. The ServiceNow SIP fully qualified domain
information name (FQDN) for your region, used to route calls from
Genesys Cloud service to the voice assistant. For SIP trunk
configuration details including IP addresses and FQDNs per
region, see KB3023612 .
x-snc-param Read-only. Generated token to send to your Genesys Cloud
account to authenticate requests to the voice assistant.
Genesys SIP integration configuration
8.In your Genesys Cloud account, configure the SIP trunk using the ServiceNow SIP FQDN and
authentication token.
Use the ServiceNow SIP Trunk information and the x-snc-param token generated in the
previous step. For SIP trunk configuration details, see KB3023612 .
Result
Genesys Cloud service is connected to your ServiceNow voice assistant. Incoming calls routed
through Genesys Cloud service are handled by the AI voice agent, which responds with a
greeting and processes the caller's requests.

<!-- page 166 -->
What to do next
For live agent transfer configuration and advanced SIP trunk settings, refer to your Genesys
Cloud documentation or contact Genesys support.
Integrate ServiceNow voice assistant with 3CLogic
Enable users to get support from AI voice agents by integrating a ServiceNow AI voice assistant
with the 3CLogic voice service.
Before you begin
•Create a voice assistant. See Create an AI voice assistant for more information.
Role required: sn_aia.admin
About this task
Connect your 3CLogic voice service to a ServiceNow voice assistant using the WebSocket
communication channel. When the integration is complete, incoming calls routed through
3CLogic are handled by the AI voice agent. When call handling is complete, the integration
supports transferring the caller to a live agent queue.
Procedure
1.Navigate to All > Conversational Interfaces > Assistant Designer > Assistants.
2. Find the voice assistant that you want to connect to 3CLogic and select Edit.
3. Select Communication channels from the guided setup navigation.
4.In the Provider application field, select the provider application to deploy the voice assistant
to.
5. Select the Telephony provider tab.
6.From the Select communication channels dropdown, select WebSocket.
7.From the CCaaS provider dropdown, select 3CLogic.
The following read-only fields are generated. Copy these values to your 3CLogic account to
complete the integration.
3CLogic configuration fields
Field Description
URL Autogenerated WebSocket URL to connect the 3CLogic voice
service to the voice assistant.
Client ID Generated client ID to authenticate requests from 3CLogic to
the voice assistant.
Client Secret Generated client secret to authenticate requests from
3CLogic to the voice assistant.
8.In your 3CLogic account, paste the URL, Client ID, and Client Secret into the corresponding
fields.
9.Complete any additional configuration required in your 3CLogic account.
For provider-side configuration steps specific to your 3CLogic deployment, contact 3CLogic
customer support .

<!-- page 167 -->
Result
The 3CLogic voice service is connected to your ServiceNow voice assistant. Incoming calls
routed through 3CLogic are handled by the AI voice agent, which responds with a greeting and
processes the caller's requests.
Note: Call recording is not available for 3CLogic integrations.
What to do next
For live agent transfer configuration and advanced 3CLogic settings, contact 3CLogic customer
support .
Integrate ServiceNow voice assistant with Amazon Connect
Enable users to get support from AI voice agents by integrating a ServiceNow voice assistant
with Amazon Connect.
Before you begin
•Create a voice assistant. See Create an AI voice assistant for more information.
•Access to your Amazon Connect instance with permissions to create Lambda functions,
configure contact flows, and manage Identity and Access Management (IAM) roles.
Role required: sn_aia.admin
About this task
Connect your Amazon Connect contact center to a ServiceNow voice assistant using the Public
Switched Telephone Network (PSTN) communication channel. When a call arrives, Amazon
Connect invokes a Lambda function that retrieves a PSTN number from the ServiceNow Call
Context API and transfers the call to the voice assistant. After the voice assistant handles the
interaction, the Lambda function retrieves the interaction context and routes the call to a queue
or ends the call.
Procedure
1.Navigate to All > Conversational Interfaces > Assistant Designer > Assistants.
2. Find the voice assistant that you want to connect to Amazon Connect and select Edit.
3. Select Communication channels from the guided setup navigation.
4.In the Provider application field, select the provider application to deploy the voice assistant
to.
5. Select the Telephony provider tab.
6.From the Select communication channels dropdown, select Public Switched Telephone
Network (PSTN).
7.From the CCaaS provider dropdown, select Amazon Connect.
The following read-only fields are generated in the Call context service section. Copy and
save these values — you will need them to configure the integration on the Amazon Connect
side.
Amazon Connect configuration fields
Field Description
Transfer method Read-only. Set to BYE for Amazon Connect.
Call context API Read-only. The URL that Amazon Connect uses to
send call context data to the voice assistant. Copy this

<!-- page 168 -->
Field Description
value for use as the call_context_api_path and
voice_service_host_name Lambda environment
variables.
Client ID Read-only. Generated client ID for OAuth2 authentication.
Copy this value for use in the AWS Parameter Store setup.
Client Secret Read-only. Generated client secret for OAuth2
authentication. Copy this value for use in the AWS Parameter
Store setup.
KB doc Reference information for configuring the PSTN connection
between Amazon Connect and the ServiceNow voice
assistant. See KB3027295 for more information.
Amazon Connect integration configuration
Also note the voice service sys_id, which you can find in the URL when viewing the voice
service record. You will need this value in the Amazon Connect configuration steps.
8.Enable context data persistence for the voice service.
a.Navigate to sys_now_assist_deployment_config_attributes.list.
b.Filter the list to find the configuration attribute records for your voice service.
c.Locate the attribute named persist_context_data and change its value from false
to true.
This setting allows the Lambda function to retrieve interaction context data from ServiceNow
after the voice assistant completes the call.
9.In your AWS account, create the Lambda function that connects Amazon Connect to the voice
assistant.

<!-- page 169 -->
a.From the AWS console, create a new Lambda function.
b.In the Lambda function code editor, replace the default handler code with the Lambda
function code.
See Amazon Connect Lambda function code.
c.Set the following environment variables on the Lambda function.
Lambda environment variables
Variable Value
call_context_api_pathThe path portion of the ServiceNow call context URL — the
part of the URL after .com.
now_instance_host_namTehe ServiceNow instance URL.
now_instance_name The name of your ServiceNow instance.
ssm_oauth_path The AWS Parameter Store path for OAuth credentials. Set
after completing the Parameter Store setup in the following
steps.
voice_service_host_naTmhee hostname from the ServiceNow call context URL.
d. Grant your Amazon Connect instance permission to invoke the Lambda function.
In the Amazon Connect console, navigate to your instance, select Flows, and under AWS
Lambda, add the Lambda function with the Invoke Lambda use case. Confirm the policy was
added in the Lambda console under Configuration > Permissions.
e. Replace the Lambda execution role permissions policy with the Identity and Access
Management (IAM) policy.
See Amazon Connect Lambda Identity and Access Management (IAM) policy.
In the Lambda console, navigate to Configuration > Permissions > Execution Role and
replace the existing permissions policy. Replace <region>, <account-id>, and
<lambda-function-name> with your values.
f.Create a CloudWatch log group for the Lambda function.
In the AWS console, navigate to CloudWatch > Log Management. If no log group exists for
your Lambda function, create one named /aws/lambda/<your_Lambda_name>.
g.Create the OAuth credentials in AWS Parameter Store.
From the AWS console, navigate to Parameter Store and create the following parameters
using SecureString as the type.
Parameter Store entries
Name Value
/com.servicenow.cti/<sn-instance-id>/ Client ID from the
<voice-service-id>/client_id ServiceNow voice service
configuration.

<!-- page 170 -->
Name Value
Where sn-instance-id is the value of the
instance_id system property, and voice-service-
id is the voice service sys_id.
/com.servicenow.cti/<sn-instance-id>/ Client Secret from the
<voice-service-id>/client_secret ServiceNow voice service
configuration.
Where sn-instance-id is the value of the
instance_id system property, and voice-service-
id is the voice service sys_id.
h.Add the AWS PowerTools layer to the Lambda function.
In the Lambda console, navigate to the Lambda function and select Layers. Add the AWS
layer AWSLambdaPowertoolsTypeScriptV2, version 2.33.0 or later.
10.Import and configure the Amazon Connect contact flow.
a.In your Amazon Connect instance, create a new contact flow by importing the Voice AI
inbound flow JSON.
See Amazon Connect Voice AI inbound flow.
In the Amazon Connect console, navigate to Routing > Flows, select Create flow, then use
the import option. Replace all placeholder values with your own before importing.
b.In the first AWS Lambda function block of the contact flow, set the function ARN to the
Lambda you created and set the voice_service_id input parameter to the sys_id of
the voice service.
c.In the second AWS Lambda function block, set the function ARN to the same Lambda
function.
d. Save and publish the contact flow.
Note: When Amazon Connect transfers the call to ServiceNow, the contact flow must
pass the original caller's phone number as the caller ID. Verify that your contact flow
is configured to preserve the original caller ID during the transfer, not the Amazon
Connect transfer number.
11. Associate a phone number with the contact flow.
a.In the Amazon Connect service dashboard, navigate to Channels > Phone numbers.
b.Claim a new number or select an existing number to associate with the contact flow.
Associating a phone number with the contact flow enables incoming calls to be routed
through the voice assistant.
Result
Amazon Connect is connected to your ServiceNow voice assistant. Incoming calls routed
through Amazon Connect are handled by the AI voice agent, which responds with a greeting
and processes the caller's requests. When call handling is complete, the contact flow routes the
caller to a queue or ends the call.

<!-- page 171 -->
What to do next
Test the integration by placing a call through your Amazon Connect phone number and verifying
that the voice assistant responds correctly. Review the CloudWatch logs for the Lambda function
to troubleshoot any connection issues.
Integrate ServiceNow voice assistant with Five9
Enable users to get support from AI voice agents by integrating a ServiceNow voice assistant
with Five9 voice service.
Before you begin
•Create a voice assistant. See Create an AI voice assistant for more information.
Role required: sn_aia.admin
About this task
Connect your Five9 contact center to a ServiceNow voice assistant using the Session Initiation
Protocol (SIP) communication channel. After the integration is configured, Five9 routes calls
to the ServiceNow SIP endpoint, where the AI voice agent handles the interaction. When call
handling is complete, the integration supports transferring the caller to a live agent queue.
Procedure
1.Navigate to All > Conversational Interfaces > Assistant Designer > Assistants.
2. Find the voice assistant that you want to connect to Five9 and select Edit.
3. Select Communication channels from the guided setup navigation.
4.In the Provider application field, select the provider application to deploy the voice assistant
to.
5. Select the Telephony provider tab.
6.From the Select communication channels dropdown, select Session Initiation Protocol (SIP).
7.From the CCaaS provider dropdown, select Five9.
The following read-only fields are generated. Use these values to configure the SIP trunk in
your Five9 account.
Five9 configuration fields
Field Description
Transfer method Read-only. Set to BYE for Five9.
ServiceNow SIP Trunk Read-only. The ServiceNow SIP fully qualified domain name
information (FQDN) for your region, used to route calls from Five9 to the
voice assistant. For SIP trunk configuration details including
IP addresses and FQDNs per region, see KB3023612 .
x-snc-param Read-only. Generated token to send to your Five9 account to
authenticate requests to the voice assistant.

<!-- page 172 -->
Five9 integration configuration
8.In your Five9 IVR, add the x-snc-param as a SIP custom header using the Set Variable Module.
In the Set Variable Module, use the following function to pass the x-snc-param value
generated in the previous step:
PUT(ToIVA, "x-snc-param", "x-snc-param value")
Result
Five9 is connected to your ServiceNow voice assistant. Incoming calls routed through Five9
are handled by the AI voice agent, which responds with a greeting and processes the caller's
requests.
What to do next
For live agent transfer configuration and advanced SIP trunk settings, refer to the Five9 BYO SIP
Trunk Integration Guide or contact Five9 support.
Integrate voice assistant with mobile app launcher
Configure your voice assistant to be accessible through the voice launcher functions in mobile
app.
Before you begin
Role required: virtual_agent_admin or admin
•You must have a voice assistant created in Assistant Designer
•Mobile app voice launcher function must be configured using Now Assist for Mobile before you
can assign it to an assistant. See Configure Mobile AI Voice Agent for more information.
Procedure
1.Navigate to All > Conversational Interfaces > Assistant Designer > Assistants.
2. Find the voice assistant that you want to connect to a mobile app voice launcher and select
Edit.
3. Select Communication channels in the Settings tab and select Mobile channels tab.

<!-- page 173 -->
Voice launcher function setup
4.In Voice launcher functions, select from the Add voice launcher function drop-down to add a
voice launcher function to open the assistant in voice mode.
5. Optional: In Chat launcher functions, select from the Add chat launcher function drop-down
to add a chat launcher function to open the assistant in chat mode.
6.In Prominent action button override, select from the Add tab override drop-down to allow a
prominent action button to launch the assistant.
The prominent action button overrides what’s been defined in the chat launcher and voice
launcher functions. See Configuring a prominent action button for more information on
configuring the prominent action button.
7.Select Save to save the configuration.
Test AI voice agents
Test your AI voice agents associated with a voice assistant from the Assistant Designer. You can
make browser-based voice calls and view turn-by-turn analysis of AI voice agents invoked, tools
executed, and latency data during the conversation.
Use the voice testing experience to evaluate how your AI voice agents handle real conversations
before deploying them. You can access voice testing from Assistant Designer or from AI Agent
Studio.

<!-- page 174 -->
Test from Assistant Designer
Navigate to the voice assistant in Assistant Designer and select Test to open the voice testing
interface. See Test a voice assistant from Assistant Designer for step-by-step instructions.
Test from AI Agent Studio
Launch the voice testing interface directly from the agent's channel configuration in AI Agent
Studio. See Test a voice agent from AI Agent Studio for step-by-step instructions.
Test a voice assistant from Assistant Designer
Test your voice assistant and the AI voice agents assigned to it by making browser-based voice
calls and viewing turn-by-turn analysis directly from Assistant Designer.
Before you begin
The following are required to access the voice testing experience:
•Conversational Studio v7 or later
•Zurich Patch 7 or later
•Microphone enabled on your device
•Now Assist for Virtual Agent version 19 or later
Roles required: sn_aia.admin and sn_voice_aia.admin
About this task
Use voice testing to evaluate how your voice assistant handles real conversations before
deploying it.
•Voice mode: Initiate a call, speak to the assistant using your microphone. The assistant
responds with synthesized speech.
•Chat mode: Type messages in a chat interface. This mode follows the same testing experience
as chat assistants.
As the conversation progresses, the Analysis tab shows a turn-by-turn breakdown including
timestamps, the agent or tool invoked for each utterance, tool execution latency, and tool status,
helping you identify gaps and fine-tune behavior.
Procedure
1.Navigate to All > Assistant Designer > Assistants tab and select Test for the voice assistant
you wish to test.
The voice testing interface opens in a new window. The window displays:
◦Left panel: A drop down for testing mode with Voice and Chat options. Live transcription of
the conversation along with the assistant greeting and input controls.
◦Right panel: Assistant summary showing the assistant name, telephony provider (if
configured), language, voice personality, and the Analysis tab.

<!-- page 175 -->
Voice assistant test window
2. Test your voice assistant.
a.In voice mode, select Start call (green phone button) to begin voice-based testing.
Your browser may prompt you to allow microphone access. Click Allow to proceed.
The call connects using WebRTC (Web Real-Time Communication). A voice waveform
animation indicates the connection is active.
b.Speak to the assistant using your microphone.
The assistant processes your speech and responds with synthesized voice output. The
conversation transcript appears in the left panel.
Voice assistant testing in Voice mode

<!-- page 176 -->
c.Continue the conversation to test different scenarios and intents.
d. When finished, select End call (red phone button) to disconnect.
a.In chat mode, type your message in the Reply field at the bottom of the conversation panel.
Text-based testing follows the same experience as testing chat assistants. You can view the
chat transcription, AI agents invoked and tools executed.
b.Select the send button to submit your message.
The assistant processes your text input and responds in the conversation panel.
Voice assistant testing in Chat mode
c.Continue the conversation to test different scenarios and intents.
3. Select the Analysis tab in the right panel to view real-time analysis.
The Analysis tab shows a turn-by-turn breakdown of the conversation. For each user utterance,
the following details are displayed where applicable:
◦Timestamp — the date and time of the utterance.
◦Agent name — the name of the AI voice agent invoked, or voice assistant if no agent was
invoked.
◦Tool name — the name of the tool invoked, where applicable. Expand a tool name to view:
▪Tool inputs
▪Tool execution latency

<!-- page 177 -->
▪Tool status (success or failure)
▪Tool response
The Analysis tab displays a turn-by-turn breakdown of AI voice agents invoked, tools executed,
and tool execution latency for the conversation.
4.Select Restart to start a new voice conversation or close the browser window to exit testing.
Selecting Restart clears the current conversation and resets the testing session.
Result
You have tested your voice assistant using the voice testing interface. Use the analysis results to
identify issues with agent routing, tool execution, or voice assistant performance, and refine your
assistant configuration as needed.
Test a voice agent from AI Agent Studio
Test your AI voice agent directly from AI Agent Studio by launching the voice testing interface
from the agent's channel configuration page.
Before you begin
At least one voice assistant must be linked to the AI voice agent. Without a linked voice assistant,
you cannot test the voice agent.
Role required: sn_aia.admin
Procedure
1.Navigate to All > Conversational Interfaces > AI Agent Studio.
2. Find the AI voice agent that you want to test and select it to open the agent configuration.
3. Select the Select channels and status page from the guided setup navigation.
4.Select Test in assistant and select the voice assistant you want to test from the dropdown.
The voice testing interface opens. See Test a voice assistant from Assistant Designer for
details on using the testing interface.
Result
The AI voice agent is tested from AI Agent Studio. Use the analysis results to identify gaps in
agent routing or tool execution and refine your voice agent configuration as needed.
AI voice agent analytics
The Voice dashboard page in the Analytics tab of Assistant Designer helps you monitor the
usage and performance metrics for AI voice agents.
Accessing AI voice agent analytics
To view the dashboard, navigate to All > Assistant Designer > Analytics and select the Voice
tab. See Voice page in assistant analytics for more information.
AI voice agent reference
Reference information for AI voice agents.
AI voice agent roles
The following table lists the roles installed with the Voice for Now Assist plugin.

<!-- page 178 -->
Roles Description
sn_voice_aia.admin Provides access to agents configuration flow
sn_voice_aia.guest Enables employees to use AI voice agents
without authentication
sn_voice_aia.integration Enables access to integrations such as Oracle
AI voice agent attributes
The AI voice agent attributes enable you to configure the authentication functionality for AI voice
agents. Navigate to All > System Definition > Tables and search for Now Assist Deployment
Config Attributes table to view the attributes.
The following table lists the attributes related to AI voice agent configuration.
Attribute Description
voice_max_retries The maximum number of retries allowed for
successful authentication before the user
account is locked. The default value is 3.
voice_minutes_account_is_locked The number of minutes the user account is
locked for, following maximum retries. The
default value is 1440 minutes.
persist_context_data Controls whether interaction context data is
persisted to Glide after a call. Set to true to
enable context data storage, which is required
for Amazon Connect integrations. The default
value is false. This attribute is scoped per
voice assistant deployment.
AI voice agent system properties
The following table consists of system properties to set up AI voice agents.
Property Description
sn_aia.enable_voice_agent_setup The system property to enable AI voice
agents. Set the value of the property to true to
enable AI voice agents on the instance.
glide.voice.authenticate.mfa_mandatory Controls whether multi-factor authentication
is required for caller verification. Set to false
to enable single factor authentication. Default
value is true.
Configuration for custom AI voice agent provider
The following table captures the required configurations on your instance to support AI voice
agents. These configurations are required only if you’re creating a new messaging channel,
provider channel, and provider channel identity for AI voice agents.

<!-- page 179 -->
Field Value
Messaging channel
Type Phone
Synchronous True
Provider Channel
Provider attributes action sn_va_as_service.virtual_agent__bot_to_bot_provider_attributes
Sender subflow sn_va_as_service.virtual_agent__bot_to_bot_contextual_action
Contextual action sn_va_as_service.virtual_agent__bot_to_bot_contextual_action
Allow account linking True
Account linking type Verification question
Automatic link action sn_va_as_service.virtual_agent__bot_to_bot_auto_link_account
Rich control mappings
Control type DefaultAction
Outbound transformer action sn_va_as_service.virtual_agent__bot_to_bot_action_outbound_transformer
Provider Channel Identity
Message auth Name of the message authentication that you
created as part of
Provider Identity properties
allow_storing_history_in_ongoing_conversation True
AI voice agent analytics indicators details
The following table maps the visualizations to the indicator sources and the calculation behind
the metrics shown in the dashboard.
AI voice agent analytics indicator details
Indicator Available
Visualization Calculation Frequency Unit Precision
type breakdowns
Total voice Automated Count of all None Daily 0
conversations voice calls
Calls Automated Count of None Daily 0
completed voice calls
without a where
live agent Agent
chat=false
ConversationsA utomated Count of None Daily 0
transferred voice calls
to a live where
agent Agent
chat=true

<!-- page 180 -->
AI voice agent analytics indicator details (continued)
Indicator Available
Visualization Calculation Frequency Unit Precision
type breakdowns
Number Automated Count of None Daily 0
of tickets Interaction
created Related
Records
where
Agent chat
= false and
Interaction
Virtual
agent =
true and
Interaction
Type =
Phone and
Interaction
AI Voice =
true
ConversationsA utomated Count of None Daily 0
disconnected voice calls
where
State=Closed
Abandoned
Inferred sn_na_analytiAcsv_eirnasgieg hts None Daily 1
customer table of session
satisfaction CSAT
(CSAT):
average
score (out
of 5)
Average Formula [[AI Agent- None Daily Minutes 0
voice Summed
conversation duration
duration of calls]] /
[[AI Agents-
Total Calls]]
Number of sn_na_analytiCcso_uinnts iogfh ts None Daily 0
deflected table voice calls
conversations where
per AI agent Resolved is
Yes
AI voice agent transcript and logs tables
The following tables contain details of the voice calls, from initiation and conversation details to
agent actions and tool executions.

<!-- page 181 -->
AI voice agent transcript and log tables
Table Details
sn_aia_execution_plan The sn_aia_execution_plan table stores
execution plans associated with voice
calls. Each record in this table represents a
single execution plan and contains detailed
information about the interactions and actions
that occurred during the call.
sn_aia_tools_execution The sn_aia_tools_execution table logs
information related to tool executions during
a voice call. Each record represents a single
tool execution and captures details about the
agent, the tool used, and the outcome of that
execution.
sys_cs_conversation The sys_cs_conversation table stores the
conversation record created at the start of
a voice call. Its creation timestamp marks
the beginning of the call. This table contains
metadata and transcripts associated with
the conversation, like state, device type, and
transcripts from the call.
Note: Personally Identifiable
Information (PII) data is redacted from
transcripts before it is stored.
Interactions The Interactions table is similar to
sys_cs_conversation and is created at the
same time as the conversation record. It
contains much of the same information related
to the voice call.
sys_generative_ai_log The sys_generative_ai_log table stores
general-purpose logs for generative AI
interactions during a voice call. If an agent
uses an LLM (Large Language Model) during
the call, this table records the relevant details
such as prompt, response, and errors.
Amazon Connect Lambda function code
Use the following Lambda function code when creating the Lambda function for the Amazon
Connect and ServiceNow voice assistant integration. Copy this code into the Lambda function
code editor. All dynamic values are read from environment variables set on the Lambda function.
const https = require('https');
const { getParameter, setParameter } =
require('@aws-lambda-powertools/parameters/ssm');
// Structured logger
────────────────────────────────────────────────────────
function log(level, message, context = {}) {
console[level === 'ERROR' ? 'error' : level === 'WARN' ? 'warn' : 'log'](

<!-- page 182 -->
JSON.stringify({ level, message, ...context })
);
}
// HTTP helper
──────────────────────────────────────────────────────────────
function sendHttpsRequest(options, postData) {
return new Promise((resolve, reject) => {
const req = https.request(options, (res) => {
let body = '';
res.on('data', (chunk) => { body += chunk; });
res.on('end', () => {
if (res.statusCode >= 200 && res.statusCode < 300) {
resolve(body);
} else {
reject(new Error(`HTTP ${res.statusCode} for
${options.method} ${options.hostname}${options.path}`));
}
});
});
req.on('error', reject);
if (postData) req.write(postData);
req.end();
});
}
// SSM
───────────────────────────────────────────────────────────────
───────
async function writeSsmParam(name, value) {
log('INFO', 'Writing SSM parameter', { param: name });
try {
await setParameter(name, { value, overwrite: true });
log('INFO', 'SSM parameter written successfully', { param: name });
} catch (err) {
// Non-fatal: token was fetched; caching failure is logged but not re-thrown
log('WARN', 'SSM write failed — token will not be cached', { param: name,
error: err.message });
}
}
// JWT
───────────────────────────────────────────────────────────────
───────
function getJwtExpiryMs(jwt) {
try {
const parts = jwt.split('.');
const payload =
JSON.parse(Buffer.from(parts[1], 'base64url').toString('utf8'));
if (typeof payload.exp !== 'number') throw new Error('exp claim is missing or
not a number');
return payload.exp * 1000;
} catch (e) {
throw new Error(

<!-- page 183 -->
`Failed to parse JWT exp claim — OAuth provider must issue
JWT access tokens: ${e.message}`
);
}
}
// OAuth
───────────────────────────────────────────────────────────────
─────
function fetchOauthToken(clientId, clientSecret) {
const payload = new URLSearchParams({
grant_type: 'client_credentials',
client_id: clientId,
client_secret: clientSecret
}).toString();
const options = {
hostname: process.env.now_instance_host_name,
path: '/oauth_token.do',
method: 'POST',
headers: {
'Content-Type': 'application/x-www-form-urlencoded',
'Content-Length': Buffer.byteLength(payload),
'Accept': 'application/json'
}
};
return sendHttpsRequest(options, payload);
}
async function fetchClientIDSecret(basePath, voiceServiceId) {
const clientIdPath =
`${basePath}/${voiceServiceId}/client_id`;
const clientSecretPath =
`${basePath}/${voiceServiceId}/client_secret`;
try {
const [clientId, clientSecret] = await Promise.all([
getParameter(clientIdPath, { decrypt: true }),
getParameter(clientSecretPath, { decrypt: true })
]);
return { clientId, clientSecret };
} catch (err) {
throw new Error(
`Failed to fetch client credentials from SSM at
${basePath}/${voiceServiceId}: ${err.message}`
);
}
}
async function getAccessToken(basePath, voiceServiceId) {
// 1. Try cache
──────────────────────────────────────────────────────────
const paramPath = `${basePath}/${voiceServiceId}/access_token`;
let cachedRaw;
try {

<!-- page 184 -->
cachedRaw = await getParameter(paramPath, { decrypt: true,
maxAge: 10 });
} catch (e) {
log('WARN', 'SSM cache read failed — treating as cache miss', { param:
paramPath, error: e.message });
}
if (cachedRaw) {
try {
const { access_token, expires_at } = JSON.parse(cachedRaw);
const ttlMs = expires_at - Date.now();
if (access_token && expires_at && ttlMs > 0) {
log('INFO', 'Using cached access token', { expiresInMs: ttlMs });
return access_token;
}
log('INFO', 'Cached token expired — refreshing', { expiresInMs: ttlMs });
} catch (e) {
log('WARN', 'Cached token parse failed — refreshing', { error:
e.message });
}
}
// 2. Fetch fresh token
──────────────────────────────────────────────────
const { clientId, clientSecret } = await
fetchClientIDSecret(basePath, voiceServiceId);
let body;
try {
body = await fetchOauthToken(clientId, clientSecret);
} catch (err) {
throw new Error(`OAuth token request failed: ${err.message}`);
}
let access_token;
try {
access_token = JSON.parse(body).access_token;
} catch (err) {
throw new Error(`Failed to parse OAuth response:
${err.message}`);
}
if (!access_token) throw new Error('OAuth response is missing access_token');
const expires_at = getJwtExpiryMs(access_token);
await writeSsmParam(paramPath, JSON.stringify({ access_token,
expires_at }));
return access_token;
}
// Call context
─────────────────────────────────────────────────────────────
function getCallContext(accessToken, contactData, voiceServiceId)
{
const payload = JSON.stringify({
call_correlation_id: contactData.ContactId,
voice_service_id: voiceServiceId,

<!-- page 185 -->
ani: contactData.CustomerEndpoint?.Address ?? '',
instance_name: process.env.now_instance_name
});
const options = {
hostname: process.env.voice_service_host_name,
path: process.env.call_context_api_path,
method: 'POST',
agent: new https.Agent({ rejectUnauthorized: false }),
headers: {
'Content-Type': 'application/json',
'Authorization': `Bearer ${accessToken}`,
'Content-Length': Buffer.byteLength(payload)
}
};
log('INFO', 'Requesting call context', { contactId:
contactData.ContactId, voiceServiceId });
return sendHttpsRequest(options, payload);
}
// Interaction context
──────────────────────────────────────────────────────
function getInteractionContext(accessToken, ccaasCallId) {
const path =
`/api/now/table/interaction_context` +
`?sysparm_query=interaction.client_session_id%3D
${ccaasCallId}%5Ename%3Dbot_context_data` +
`&sysparm_fields=name%2Cvalue` +
`&sysparm_limit=1`;
const options = {
hostname: process.env.now_instance_host_name,
path,
method: 'GET',
headers: {
'Authorization': `Bearer ${accessToken}`,
'Accept': 'application/json'
}
};
log('INFO', 'Requesting interaction context', { ccaasCallId });
return sendHttpsRequest(options, null);
}
// Handler
───────────────────────────────────────────────────────────────
───
exports.handler = async (event) => {
const contactData = event.Details?.ContactData;
const operation = event.Details?.Parameters?.operation;
const voiceServiceId =
event.Details?.Parameters?.voice_service_id;
const basePath = process.env.ssm_oauth_path;

<!-- page 186 -->
if (!basePath) {
log('ERROR', 'Missing required env var: ssm_oauth_path');
return { statusCode: 500, body: JSON.stringify({ error: 'Missing
env var ssm_oauth_path' }) };
}
// Obtain access token
───────────────────────────────────────────────────
let accessToken;
try {
accessToken = await getAccessToken(basePath, voiceServiceId);
} catch (e) {
log('ERROR', 'Failed to obtain access token', { error: e.message });
return { statusCode: 500, body: JSON.stringify({ error:
e.message }) };
}
// getCallContext
────────────────────────────────────────────────────────
if (operation === 'getCallContext') {
if (!voiceServiceId) {
log('ERROR', 'Missing voice_service_id for getCallContext');
return { statusCode: 400, body: JSON.stringify({ error: 'Missing
voice_service_id in event Parameters' }) };
}
let callContextResponse;
let dnis, tracing_id;
try {
callContextResponse = await getCallContext(accessToken,
contactData, voiceServiceId);
({ dnis, tracing_id } = JSON.parse(callContextResponse));
log('INFO', 'Call context retrieved', { contactId:
contactData.ContactId });
} catch (e) {
log('ERROR', 'getCallContext request failed', { error: e.message,
contactId: contactData?.ContactId });
return { statusCode: 502, body: JSON.stringify({ error:
`getCallContext failed: ${e.message}` }) };
}
return { statusCode: 200, dnis, tracing_id };
}
// getInteractionContext
─────────────────────────────────────────────────
if (operation === 'getInteractionContext') {
let interactionContextName = null;
let interactionContextValue = null;
let interactionId = null;
let snTransferReason = null;
try {
const contextResponse = await
getInteractionContext(accessToken, contactData.ContactId);

<!-- page 187 -->
const record = JSON.parse(contextResponse).result?.[0] ??
null;
interactionContextName = record?.name ?? null;
interactionContextValue = record?.value ?? null;
if (interactionContextValue) {
const valueObj = JSON.parse(interactionContextValue);
interactionId = valueObj?.interactionId ?? null;
snTransferReason =
valueObj?.sessionVariables?.snTransferReason ?? null;
}
if(!interactionId) {
throw new Error("Interaction context failed to retrive");
}
log('INFO', 'Interaction context retrieved', { contactId:
contactData.ContactId, interactionId });
} catch (e) {
// Non-fatal: return nulls so the contact flow can handle the missing data gracefully
log('ERROR', 'Failed to fetch or parse interaction context', { error:
e.message, contactId: contactData?.ContactId });
return { statusCode: 500, interactionId: null };
}
return {
statusCode: 200,
interactionContextName,
interactionContextValue,
interactionId,
snTransferReason,
body: JSON.stringify({ interactionContextName,
interactionContextValue, interactionId, snTransferReason })
};
}
// Unknown operation
─────────────────────────────────────────────────────
log('ERROR', 'Unknown or missing operation', { operation });
return { statusCode: 400, body: JSON.stringify({ error: `Unknown
operation: ${operation}` }) };
};
Amazon Connect Lambda Identity and Access Management (IAM) policy
Replace the Lambda execution role permissions policy with the following. Replace <region>,
<account-id>, and <lambda-function-name> with your values before applying.
{
"Version": "2012-10-17",
"Statement": [
{
"Action": [
"kms:Decrypt",
"kms:Encrypt"
],
"Resource": "*",
"Effect": "Allow",

<!-- page 188 -->
"Sid": "InlinePolicy0"
},
{
"Action": [
"logs:CreateLogStream",
"logs:PutLogEvents",
"ssm:PutParameter",
"ssm:GetParameter",
"ssm:GetParametersByPath"
],
"Resource": [
"arn:aws:logs:<region>:<account-id>:log-group:/aws/lambda/<lambda-function-name>:l
og-stream:*",
"arn:aws:ssm:<region>:<account-id>:parameter/com.servicenow.cti/*"
],
"Effect": "Allow",
"Sid": "InlinePolicy1"
}
]
}
Amazon Connect Voice AI inbound flow
Import the following JSON to create the Voice AI inbound contact flow in Amazon Connect.
Replace <region>, <account-id>, <lambda-function-name>, <instance-id>,
<queue-id>, and <voice-service-sys-id> with your values before importing.
{
"Version": "2019-10-30",
"StartAction": "ed95af7d-fab7-4df3-86f0-e5b4226101eb",
"Metadata": {
"entryPointPosition": {
"x": 40,
"y": 40
},
"ActionMetadata": {
"ed95af7d-fab7-4df3-86f0-e5b4226101eb": {
"position": {
"x": 188.8,
"y": 39.2
}
},
"08f00810-b884-4af5-99d2-cb8c18afaf8a": {
"position": {
"x": 2362.4,
"y": 40.8
}
},
"590a4c69-3afc-41ee-9421-e2dc55166991": {
"position": {
"x": 2603.2,
"y": 48.8
}
},
"642abbac-6c23-441f-94a6-48e67082fa47": {
"position": {

<!-- page 189 -->
"x": 2136.8,
"y": 42.4
},
"parameters": {
"QueueId": {
"displayName": "BasicQueue"
}
},
"queue": {
"text": "BasicQueue"
}
},
"36c1da1b-e95b-4685-bd6c-3cf4d22b06b7": {
"position": {
"x": 2608,
"y": 243.2
}
},
"0e65ca4c-6e0c-4cf5-ae90-91bb10a2c311": {
"position": {
"x": 440.8,
"y": 44.8
}
},
"ad63da6d-da3f-4ef2-ba91-31f8e8eb4238": {
"position": {
"x": 1911.2,
"y": 42.4
},
"conditions": [],
"conditionMetadata": [
{
"id": "93edeb32-3c74-4ffe-9716-1e4642038881",
"operator": {
"name": "Equals",
"value": "Equals",
"shortDisplay": "="
},
"value": "user_requested"
}
]
},
"04052d59-7bba-4ca4-9aa6-597ee230c262": {
"position": {
"x": 1704.8,
"y": 43.2
},
"dynamicParams": []
},
"4940e566-4c7a-4bb4-b938-305c7498cdbe": {
"position": {
"x": 1509.6,
"y": 46.4
},
"parameters": {
"LambdaFunctionARN": {
"displayName": "<lambda-function-name>"

<!-- page 190 -->
}
},
"dynamicMetadata": {
"operation": false
}
},
"8f634a38-6e73-45b5-8db9-0235190f33af": {
"position": {
"x": 2848.8,
"y": 231.2
}
},
"33608cd6-6e7a-47b9-8380-6977b3dcf123": {
"position": {
"x": 672,
"y": 42.4
},
"parameters": {
"LambdaFunctionARN": {
"displayName": "<lambda-function-name>"
}
},
"dynamicMetadata": {
"operation": false,
"voice_service_id": false
}
},
"8ea17f75-2185-4a68-af81-e9f6908c47fb": {
"position": {
"x": 1292,
"y": 39.2
},
"parameters": {
"ThirdPartyPhoneNumber": {
"countryCode": "",
"useDynamic": true
}
}
},
"a7ea0786-08fa-41c7-aabb-0b2bdda36c64": {
"position": {
"x": 876.8,
"y": 43.2
},
"dynamicParams": []
},
"fa2af8ef-be9d-4685-8bc5-f37166a06c0e": {
"position": {
"x": 1512.8,
"y": 342.4
}
},
"d0a02e42-281e-4068-91d5-ec81ef07f655": {
"position": {
"x": 1086.4,
"y": 43.2
},

<!-- page 191 -->
"conditionMetadata": [
{
"id": "3e23d991-b5f1-48e8-a2be-76408086206c",
"operator": {
"name": "Equals",
"value": "Equals",
"shortDisplay": "="
},
"value": "200"
}
]
}
},
"Annotations": [],
"name": "Voice AI inbound flow",
"description": "",
"type": "contactFlow",
"status": "published",
"hash": {}
},
"Actions": [
{
"Parameters": {
"SkipWhenDTMFBufferEnabled": "false",
"Text": "Hi Welcome to ServiceNow"
},
"Identifier": "ed95af7d-fab7-4df3-86f0-e5b4226101eb",
"Type": "MessageParticipant",
"Transitions": {
"NextAction": "0e65ca4c-6e0c-4cf5-ae90-91bb10a2c311",
"Errors": [
{
"NextAction": "0e65ca4c-6e0c-4cf5-ae90-91bb10a2c311",
"ErrorType": "NoMatchingError"
}
]
}
},
{
"Parameters": {},
"Identifier": "08f00810-b884-4af5-99d2-cb8c18afaf8a",
"Type": "TransferContactToQueue",
"Transitions": {
"NextAction": "590a4c69-3afc-41ee-9421-e2dc55166991",
"Errors": [
{
"NextAction": "590a4c69-3afc-41ee-9421-e2dc55166991",
"ErrorType": "QueueAtCapacity"
},
{
"NextAction": "590a4c69-3afc-41ee-9421-e2dc55166991",
"ErrorType": "NoMatchingError"
}
]
}
},
{

<!-- page 192 -->
"Parameters": {
"SkipWhenDTMFBufferEnabled": "false",
"Text": "Failed to connect to an agent"
},
"Identifier": "590a4c69-3afc-41ee-9421-e2dc55166991",
"Type": "MessageParticipant",
"Transitions": {
"NextAction": "8f634a38-6e73-45b5-8db9-0235190f33af",
"Errors": [
{
"NextAction": "8f634a38-6e73-45b5-8db9-0235190f33af",
"ErrorType": "NoMatchingError"
}
]
}
},
{
"Parameters": {
"QueueId": "arn:aws:connect:<region>:<account-id>:instance/<instance-id>/queue/<que
ue-id>"
},
"Identifier": "642abbac-6c23-441f-94a6-48e67082fa47",
"Type": "UpdateContactTargetQueue",
"Transitions": {
"NextAction": "08f00810-b884-4af5-99d2-cb8c18afaf8a",
"Errors": [
{
"NextAction": "590a4c69-3afc-41ee-9421-e2dc55166991",
"ErrorType": "NoMatchingError"
}
]
}
},
{
"Parameters": {
"SkipWhenDTMFBufferEnabled": "false",
"Text": "Call completed, thank you"
},
"Identifier": "36c1da1b-e95b-4685-bd6c-3cf4d22b06b7",
"Type": "MessageParticipant",
"Transitions": {
"NextAction": "8f634a38-6e73-45b5-8db9-0235190f33af",
"Errors": [
{
"NextAction": "8f634a38-6e73-45b5-8db9-0235190f33af",
"ErrorType": "NoMatchingError"
}
]
}
},
{
"Parameters": {
"FlowLoggingBehavior": "Enabled"
},
"Identifier": "0e65ca4c-6e0c-4cf5-ae90-91bb10a2c311",
"Type": "UpdateFlowLoggingBehavior",

<!-- page 193 -->
"Transitions": {
"NextAction": "33608cd6-6e7a-47b9-8380-6977b3dcf123"
}
},
{
"Parameters": {
"ComparisonValue": "$.Attributes.snTransferReason"
},
"Identifier": "ad63da6d-da3f-4ef2-ba91-31f8e8eb4238",
"Type": "Compare",
"Transitions": {
"NextAction": "36c1da1b-e95b-4685-bd6c-3cf4d22b06b7",
"Conditions": [
{
"NextAction": "642abbac-6c23-441f-94a6-48e67082fa47",
"Condition": {
"Operator": "Equals",
"Operands": [
"user_requested"
]
}
}
],
"Errors": [
{
"NextAction": "36c1da1b-e95b-4685-bd6c-3cf4d22b06b7",
"ErrorType": "NoMatchingCondition"
}
]
}
},
{
"Parameters": {
"Attributes": {
"snTransferReason": "$.External.snTransferReason",
"interactionId": "$.External.interactionId"
},
"TargetContact": "Current"
},
"Identifier": "04052d59-7bba-4ca4-9aa6-597ee230c262",
"Type": "UpdateContactAttributes",
"Transitions": {
"NextAction": "ad63da6d-da3f-4ef2-ba91-31f8e8eb4238",
"Errors": [
{
"NextAction": "8f634a38-6e73-45b5-8db9-0235190f33af",
"ErrorType": "NoMatchingError"
}
]
}
},
{
"Parameters": {
"LambdaFunctionARN": "arn:aws:lambda:<region>:<account-id>:function:<lambda-functi
on-name>",
"InvocationTimeLimitSeconds": "3",

<!-- page 194 -->
"InvocationType": "SYNCHRONOUS",
"LambdaInvocationAttributes": {
"operation": "getInteractionContext"
},
"ResponseValidation": {
"ResponseType": "STRING_MAP"
}
},
"Identifier": "4940e566-4c7a-4bb4-b938-305c7498cdbe",
"Type": "InvokeLambdaFunction",
"Transitions": {
"NextAction": "04052d59-7bba-4ca4-9aa6-597ee230c262",
"Errors": [
{
"NextAction": "8f634a38-6e73-45b5-8db9-0235190f33af",
"ErrorType": "NoMatchingError"
}
]
}
},
{
"Parameters": {},
"Identifier": "8f634a38-6e73-45b5-8db9-0235190f33af",
"Type": "DisconnectParticipant",
"Transitions": {}
},
{
"Parameters": {
"LambdaFunctionARN": "arn:aws:lambda:<region>:<account-id>:function:<lambda-functi
on-name>",
"InvocationTimeLimitSeconds": "3",
"InvocationType": "SYNCHRONOUS",
"LambdaInvocationAttributes": {
"operation": "getCallContext",
"voice_service_id": "<voice-service-sys-id>"
},
"ResponseValidation": {
"ResponseType": "STRING_MAP"
}
},
"Identifier": "33608cd6-6e7a-47b9-8380-6977b3dcf123",
"Type": "InvokeLambdaFunction",
"Transitions": {
"NextAction": "a7ea0786-08fa-41c7-aabb-0b2bdda36c64",
"Errors": [
{
"NextAction": "fa2af8ef-be9d-4685-8bc5-f37166a06c0e",
"ErrorType": "NoMatchingError"
}
]
}
},
{
"Parameters": {
"ThirdPartyPhoneNumber": "$.Attributes.pstnNumber",
"ThirdPartyConnectionTimeLimitSeconds": "30",

<!-- page 195 -->
"ContinueFlowExecution": "True"
},
"Identifier": "8ea17f75-2185-4a68-af81-e9f6908c47fb",
"Type": "TransferParticipantToThirdParty",
"Transitions": {
"NextAction": "4940e566-4c7a-4bb4-b938-305c7498cdbe",
"Errors": [
{
"NextAction": "fa2af8ef-be9d-4685-8bc5-f37166a06c0e",
"ErrorType": "CallFailed"
},
{
"NextAction": "fa2af8ef-be9d-4685-8bc5-f37166a06c0e",
"ErrorType": "ConnectionTimeLimitExceeded"
},
{
"NextAction": "fa2af8ef-be9d-4685-8bc5-f37166a06c0e",
"ErrorType": "NoMatchingError"
}
]
}
},
{
"Parameters": {
"Attributes": {
"pstnNumber": "$.External.dnis",
"statusCode": "$.External.statusCode"
},
"TargetContact": "Current"
},
"Identifier": "a7ea0786-08fa-41c7-aabb-0b2bdda36c64",
"Type": "UpdateContactAttributes",
"Transitions": {
"NextAction": "d0a02e42-281e-4068-91d5-ec81ef07f655",
"Errors": [
{
"NextAction": "fa2af8ef-be9d-4685-8bc5-f37166a06c0e",
"ErrorType": "NoMatchingError"
}
]
}
},
{
"Parameters": {
"SkipWhenDTMFBufferEnabled": "false",
"Text": "Failed to connect"
},
"Identifier": "fa2af8ef-be9d-4685-8bc5-f37166a06c0e",
"Type": "MessageParticipant",
"Transitions": {
"NextAction": "8f634a38-6e73-45b5-8db9-0235190f33af",
"Errors": [
{
"NextAction": "8f634a38-6e73-45b5-8db9-0235190f33af",
"ErrorType": "NoMatchingError"
}
]

> **[Screenshot: Create an assistant — Voice-only option selection]**
> The "Create an assistant" wizard screen in Virtual Agent Assistant Designer. Two option cards shown vertically: "Chat-based" – thumbnail screenshot of a chat UI, description "People can interact with it in chat experiences across display experiences. Examples: HR Assistant / CSM Agent Assistant / Creator Studio Assistant", radio button (unselected). "Voice-only" – thumbnail screenshot of a voice/phone UI, description "People can interact with it only over the phone. Examples: Home Genius Assistant / Voice Navigator Assistant / Digital Concierge Assistant", radio button (selected, blue dot). "Continue" teal button at bottom-right.
>
> **[Screenshot: Basic details form for voice assistant]**
> The Assistant Designer interface showing "Employee Service Center" assistant being created. Left sidebar stepper: Basic details (filled/active, blue), All agents (empty), Voice personality (empty), Communications… (empty), Caller verification (empty), Safeguards (empty), Advanced settings (empty), Review (empty). Main content title "Let's fill out some details". Sub-title "Start by entering a unique name for the assistant and describing its purpose." Form fields: "Name *" = "Employee Service Center"; "Description *" = "The Employee Service Center voice assistant provides employees with a conversational way to access HR services."; "Tags" section — "Adding or removing BU tags will apply the changes immediately. These will be tracked in analytics." Tag field contains "HR" with "Manage tags" link. "Save and continue" button bottom-right.

> **[Screenshot: Twilio voice service integration configuration page]**
> The Communication channels step of the voice assistant configuration. Breadcrumb shows "New Assist Voice Deployment > Deployments > Voice Strat". Buttons top-right: Save, Test Assistant, Deactivate. Left sidebar stepper: Basic details (filled), Language and voice (filled), Communication channels (selected/active blue bar), Caller verification (empty), Safeguards (empty), Advanced settings (empty). Main content title "Select communication channels". Two tabs: "Telephony provider" (active) and "Web Real-Time Communication (WebRTC)". Form fields: "Provider application *" = "AI Voice Agent Provider Ap..." dropdown. "Communication channel *" — "WebSocket" dropdown. "CCaaS provider *" — "Twilio" dropdown. Authentication token field (obscured with dots) with copy icon. An info banner reads: "This integration must be completed in your telephony provider's account. Please follow the setup steps outlined in the product documentation. Product documentation ↗." "To link to this assistant, copy and paste the information to your provider's site." URL field shows: "https://.../com/twilio/voice/agent_operator?instance_name=kntestingsvo" with copy icon. "Unlink this provider" link at bottom-right.