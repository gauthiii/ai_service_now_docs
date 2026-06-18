# Exploring Now Assist Admin

_Source pages: 5–143 | Depth: 1_

---

<!-- page 5 -->
Exploring Now Assist Admin
Learn how Now Assist Admin brings generative AI capabilities to the ServiceNow AI Platform.
With Now Assist Admin, you can improve the productivity and efficiency in your organization,
deliver better self-service, recommend actions and provide answers, and empower your users to
search more effectively.
Now Assist Admin overview
Now Assist is a growing cross-platform family of generative AI features, which are tasks that a
large language model (LLM) can perform. Generative AI features are based on the initial training
and architecture.
A skill delivers a feature plus the use case to the user. An example of a skill is chat summarization
within a customer workspace. Now Assist products provide features and skills that are tailored to
meet the needs of users in different workflows.
Now Assist framework
The Now Assist framework is supported across the ServiceNow AI Platform. To use Now Assist
skills, activate one or more of the following Now Assist products.
Now Assist products
Workflow Business areas Available products
Technology The Technology workflow includes IT •
applications, such as IT services and
•Now Assist for Configuration
operations, managing your strategy
Management Database (CMDB)
to deliver products and services, and
platform security. •Now Assist for Enterprise
Architecture (EA)
•Now Assist for Operational
Sustainability Management
•Now Assist for Hardware Asset
Management (HAM)
•Now Assist for Integrated Risk
Management (IRM)
•Now Assist for IT Operations
Management (ITOM)
•Now Assist for IT Service
Management (ITSM)
•Now Assist for Operational
Technology Manager (OTM)
•Now Assist for Operational
Technology Service Management
(OTSM)
•Now Assist for Security Incident
Response
•Now Assist for Software Asset
Management (SAM)

<!-- page 6 -->
Now Assist products (continued)
Workflow Business areas Available products
•Now Assist for Strategic Portfolio
Management (SPM)
•Now Assist for Third-party Risk
Management (TPRM)
•Now Assist for Vulnerability
Response
Customer The Customer workflow includes
•Now Assist for Customer Service
applications that support
Management (CSM)
customer service, including
field service, financial services, •Now Assist for Field Service
telecommunications and media, and Management (FSM)
the public service sector.
•Now Assist for Financial Services
Operations (FSO)
•Now Assist for Order
Management
•Now Assist for Public Sector Digital
Services (PSDS)
•Now Assist for Sales Force
Automation (SFA)
•Now Assist for
Telecommunications, Media and
Technology (TMT)
Employee The Employee workflow supports
•Now Assist for Employee
HR Service Delivery and Employee
Experience
Experience features.
•Now Assist for Health and Safety
•Now Assist for HR Service Delivery
(HRSD)
•Now Assist for Legal Service
Delivery (LSD)
•Now Assist for Workplace Service
Delivery (WSD)
Creator The Creator workflow supports a Now Assist for Creator
variety of Platform tools and builders,
including the following:
•App Engine Studio
•ServiceNow AI Platform scripting
•Platform Analytics
•Service Catalog
•Workflow Studio

<!-- page 7 -->
Now Assist products (continued)
Workflow Business areas Available products
•RPA Hub
•Process Mining
Finance & Supply The Finance & Supply Chain
•Now Assist for Accounts Payable
Chain workflow supports purchase
Operations (APO)
requisitions, sourcing requests, and
request for products or services. •Now Assist for Supplier Lifecycle
Operations (SLO)
•Now Assist for Sourcing and
Procurement Operations (SPO)
App Engine The App Engine workflow supports Now Assist for App Engine
App Engine products and offerings
so that you can enhance your
custom applications with AI.
Vault The Vault workflow supports Now Assist for Vault
generating custom data patterns
from text descriptions to streamline
your workload, checking role access
for an encrypted column to monitor
your instance’s encryption access
posture, and scheduling Data
Discovery jobs to detect sensitive
data.
Other The Other workflow accommodates Now Assist for Zero Copy
additional plugins and skills that Connector
don't fit into any other workflow.
Now Assist products include some or all of the following foundational platform tools for Now
Assist. For more information, see Now Assist skills in the Platform workflow.
•Administrators install plugins, manage skills, and analyze usage and performance with the
Overview tab in Now Assist Admin.
•Users can take advantage of Now Assist skills by using the Now Assist panel on the instance.
•Use Now Assist in AI Search to generate answers for AI Search.
•Use Now Assist for Mobile to run generative AI skills in a mobile environment.
•Use Now Assist in Virtual Agent to create conversational catalog experiences and author
topics that use LLM topic discovery.
•Developers can use the Generative AI Controller to integrate generative AI features in custom
flows and conversations by using your own third-party large language model (LLM) licenses.
The following diagram shows what's available in the Now Assist framework.

<!-- page 8 -->
Now Assist framework
Now Assist benefits
Benefit Feature Users
Leverage the power of search with the Now Now Assist in AI Everyone
LLM generative AI model to answer questions Search
in user searches with actionable AI-generated
summaries of relevant knowledge articles.
Install and configure Now Assist applications Now Assist Admin Administrators
and the skills they provide. console
Choose which skills to turn on, and which Now Assist Admin Administrators
users can access them. console
Monitor the usage and performance of Now Assist Analytics Administrators
generative AI features and capabilities offered
under Now Assist.
Access generative AI skills in context through Now Assist panel Everyone
a user-friendly interface.
Use Now Assist skills on mobile devices. Now Assist for Everyone
Mobile
Customize your workflows and use your own Generative AI Administrators or
third-party LLM license. Controller developers
Use Now Assist in other platform features. Now Assist skills in the Administrators or
Platform workflow developers

<!-- page 9 -->
Benefit Feature Users
Monitor Now Assist consumption on your Monitoring Now Assist Administrators
instance. usage in Subscription
Management
Overview tab in Now Assist Admin
The Now Assist Admin console provides quick and effortless access to the important information
that you need to set up, configure, and monitor Now Assist applications and features.
x Now Assist Admin overview
Now Assist Admin overview tab
Begin your exploration of the Now Assist features and skills in the Now Assist Admin console.
This console contains everything that you need to install, configure, and learn about the different
generative AI features on the ServiceNow AI Platform.
The following example shows the Now Assist Admin Overview page.
Now Assist Admin Overview page
Now Assist Admin workflow
Take five steps to begin using the Now Assist Admin console.
1. Install plugins.
On the Available for you tab of the Settings page, you can review the available
plugins and install the ones that are relevant to your business needs. Each plugin
contains the skills that you can activate to enable generative AI features on your
instance. The following diagram shows the Available for you tab.

<!-- page 10 -->
Available for you tab on the Now Assist Admin Settings > Plugins
page
2. (Optional) Turn on the Now Assist panel.
The Now Assist panel integrates the Now Assist skills into the Next Experience UI.
By turning on the Now Assist panel directly from the Now Assist Admin console, you
enable agents to access skills from anywhere on the ServiceNow AI Platform.
For more information about the Now Assist panel, see Now Assist panel overview.
This step is optional because the skills can also display in-product in the Core UI
and in Workspaces.
You can turn the Now Assist panel on from the Now Assist Experiences page of the
Admin console.

<!-- page 11 -->
Now Assist Experiences page with Now Assist panel
3. Activate skills.
Skills are features that are created for a specific use case in a Now Assist
application. Use the Now Assist Skills page to explore the skills that are available
with your installed plugins. The following diagram shows the available features and
skills in the Technology workflow.
Available Now Assist features and skills in the Technology workflow
After deciding which skills best fit your business needs, you can activate them from
the console. Some skills require configuration so that you can customize the skill
to your needs, such as determining the skill inputs and triggers. You can select the
skills that you want to configure in the Now Assist Admin Features page.
The following example shows a step in the guided setup of the skill activation
process, which is choosing where to display the skill. Skills can be displayed in-
product, including the Core UI and Workspaces, or in the Now Assist panel. You can
choose either or both locations. The following diagram shows the process for chat
summarization activation in Now Assist Admin.

<!-- page 12 -->
Chat summarization activation in Now Assist Admin
4. Review your Now Assist account settings.
The Now Assist Admin console Settings page enables you to set up language
support, if you have Dynamic Translation enabled on your instance, and review your
account details. Get up-to-date information about what plugins are available to you
and the status of data sharing on your instance.
Now Assist Admin console account settings
5. Monitor and analyze skill performance.
Use the metrics available on the Overview page to review the summaries,
performance information, and issues that need your attention. The following
example shows the current plugin status, as well as the number of active skills.

<!-- page 13 -->
Plugin and Skills status on the Now Assist Admin Overview page
The Now Assist Admin console contains the Now Assist journey checklist with additional
instructions for implementing Now Assist on your instance.
Now Assist journey checklist
You can consult the following checklist from the Now Assist Admin console
Overview page at any time to guide your implementation of Now Assist applications,
features, and skills.
Learn more about the Now Assist journey
•Get an overview of the Now Assist framework.
•Discover the Now Assist panel.
•Explore the Now Assist skills available.
•Activate and configure a Now Assist skill using the Now Assist Admin console.
•Analyze and monitor Now Assist skill usage and performance.

<!-- page 14 -->
Now Assist Experiences
Explore Now Assist panel and Now Assist context menu under the Now Assist Experiences
tab of Now Assist Admin.
Now Assist panel
With the Now Assist panel, you can get assistance from generative AI experiences to solve
customer issues faster. Use this conversational interface to summarize a chat, case, or incident,
get help, or generate resolution notes so that you can get the context of this information more
quickly.
You must fulfill the following conditions to use the Now Assist panel:
•Next Experience must be enabled. For more information, see Considerations for activating
Next Experience .
•You must have the now_assist_panel_user role.
•Your role must be applied to at least one active Now Assist skill to use skills in the Now Assist
panel.
There are three versions of Now Assist panel chats: standard, enhanced, and premium. Select
one of the versions to learn more:
•Standard chat - provides conversational support assistance within a standard, static chat
window. To activate the Now Assist panel standard chat, see Activate the Now Assist panel
standard chat.
•Enhanced chat - provides conversational support assistance within a dynamic window that
gives a more intuitive and personalized experience. You must activate the Now Assist panel
enhanced chat and configure your Now Assist instance to use the enhanced chat. See
Activate Now Assist panel enhanced chat for more information.
•Premium chat - provides conversational support assistance within a fully agentic chat
experience that enables the assistant to reason across multiple sources and execute complex
workflows without leaving the conversation. You must activate the Now Assist panel premium
chat and configure your Now Assist instance to use the premium chat. See Display your
assistant on Platform or ServiceNow Studio for more information.
If you want to use assistants, you must activate them. See Configuring assistants overview for
information on activating assistants.
Note: Voice input is automatically activated when you activate the Now Assist panel. As
of the Zurich Patch 4 release, voice input is configured in the Configure Next Experience
accessibility preferences .
Standard chat
With the Now Assist panel standard chat, you can get assistance from generative AI experiences
to solve customer issues faster. Use this conversational interface to summarize a chat, case, or
incident, get help, or generate resolution notes so that you can get the context of this information
more quickly.
Note: Next Experience must be enabled to use the Now Assist panel. For more
information, see Considerations for activating Next Experience .
Now Assist panel overview
Agents can use the Now Assist panel to interact with and get assistance from generative AI. On
the Now Assist panel, you can increase your productivity and efficiency by using the generative
AI experience to summarize a chat, case, incident, or generate resolution notes.

<!-- page 15 -->
Conversational aspects of the Now Assist panel, such as skill detection, are powered by Now
LLM Service.
Note: Now Assist skills must be enabled to appear on the Now Assist panel. For more
information, see Now Assist skills.
Let's get started by selecting the Now Assist icon to display the Now Assist
panel.
If a number in a square appears, it indicates how many messages you missed when the Now
Assist panel was closed.
Now Assist panel

<!-- page 16 -->
The Now Assist panel includes:
Item number Description
Expands the chat into a 90% screen-size
1 - Enter modal button window.
Positions, or pins, the Now Assist panel to the
2 -
screen.
3 - Display chats button Displays the Chats window.
4 - Option buttons Displays the available options.
5 - Copy message button Copies the Now Assist panel message.
6 - Reply to Now Assist... field Enter actions.
Voice Input If Voice Input is activated, select the
microphone icon or the keyboard shortcut
to use your voice to interact with the Now
Assist panel. After you speak, there’s a pause
while the system transcribes the text and then
displays it on the screen. See Enable voice
input for Now Assist panel for information on
enabling Voice Input. See Next Experience
keyboard shortcuts for the Now Assist menu
(Voice Input mode) shortcuts for Microsoft and
macOS.
8 - Active chats All active chats display in the Active chats
section. in the Active chats section of the Now
Assist. You can create additional chats by
selecting the + icon in the heading.

<!-- page 17 -->
Item number Description
9 - Updates Displays important updates and reminders.
10 - Closed chats Displays all closed chats. If you select one
of the closed chats, you can see that chat's
history.
Now Assist panel is available on Next Experience and ServiceNow Studio. The following
screenshots show the Now Assist panel in a workspace and on Core UI screens under Next
Experience.
Now Assist panel
Next Experience Core UI
Navigating from the Now Assist panel
Navigate from the Now Assist panel without leaving the current conversation by entering a
navigation request in the Ask Now Assist to... field. If you enter "navigate me to active incidents,"
Now Assist displays a button that enables you to view the active incidents.
Chat summarization
Quickly learn the details of a chat by reading a chat summarization. The chat summarization
gives you enough details about the chat so that your requester doesn't have to repeat the same
information to you.
To generate a chat summarization from the Now Assist panel, select Chat Summarization or
enter summarize chat in the Ask Now Assist to field.
Note: You can also generate a chat summarization by using the /summarize quick
action in Agent Chat.
Case or incident summarization
Quickly learn the details of a case or incident by reading a case summarization. The
summarization gives you enough details about the interaction so that your requester doesn't
have to repeat the same information to you.

<!-- page 18 -->
You can generate a case or incident summarization from the Now Assist panel for Now Assist for
CSM, Now Assist for HRSD, or Now Assist for ITSM:
•For Now Assist for CSM, select Summarize record or enter summarize a record in the
Ask Now Assist to field.
•For Now Assist for HRSD, select Summarize record or enter summarize a record in the
Ask Now Assist to field.
•For Now Assist for ITSM, select Summarize incident or enter summarize an incident in
the Ask Now Assist to field.
Conversation Help
Get specific and accurate answers to your queries by using the Get Help skill option on the Now
Assist panel. This skill is available to everyone entitled to Now Assist capabilities.
For more information about the Now Assist Conversational Help skill which represents as Get
Help on the Now Assist panel, see Now Assist Conversational Help.
Resolution notes generation
Quickly learn the details of how an interaction was resolved by generating and reading resolution
notes.
To generate resolution notes from the Now Assist panel, select Generate resolutions notes or
enter generate resolutions notes in the Ask Now Assist to field.
Streaming responses
After you enter a question or request on the Now Assist panel, Now Assist gathers information
from Knowledge Base articles, external content, product documentation, catalog items, and
workflows and combines them into a synthesized, comprehensive answer. Instead of waiting for
the entire message to render, the synthesized response streams in real time and stops streaming
after the entire message has been delivered. An animated sparkle icon ( ) appears while the
response is generated and changes to the static sparkle icon after the response has fully loaded.
Enhanced chat
Now Assist panel enhanced chat is a conversational support experience within a dynamic
window that also includes the ability to have multiple active conversations and superior search
capabilities. Use Now Assist panel enhanced chat to improve your productivity and efficiency by
leveraging generative AI to perform tasks such as summarize a chat, case, or incident, request
help, generate resolution notes, among others.
Note: Please note these important considerations:
•Next Experience must be enabled to use the Now Assist panel. For more information, see
Considerations for activating Next Experience .
•To use the full capabilities of Now Assist panel enhanced chat, AI Search must be
enabled for your portal. Without it, Now Assist panel enhanced chat functions in a limited
capacity. Basic conversational interactions such as predefined topic flows and simple
questions and answers are available, but knowledge article retrieval, AI responses
grounded in instance content, and semantic search capabilities require AI Search. For
more information, see Enable and configure AI Search in Service Portal .
Agents can use the Now Assist panel enhanced chat to interact with and get assistance from
generative AI. You can move the chat window by selecting the header and dragging the chat

<!-- page 19 -->
window to the desired location. You can resize the chat window by using the window's edges to
resize to your desired size or use the toolbar icons.
Now Assist panel enhanced chat must be activated before you can use it. See Activate Now
Assist panel enhanced chat for more information.
Conversational aspects of the Now Assist panel, such as skill detection, are powered by Now
LLM Service.
Note: Now Assist skills must be enabled to appear on the Now Assist panel. For more
information, see Now Assist skills.
Let's get started by selecting the Now Assist icon to display the Now Assist panel.
Now Assist panel

<!-- page 20 -->
The Now Assist panel includes:
Item number Description
Expands the chat into a 90% screen-size
window. The 90% screen-size window can’t
1 -
be resized or moved. Selecting the icon again
resizes the chat back into the floating window.
Positions, or pins, the Now Assist panel to the
2 -
screen.
3 - Option buttons Displays the available options.
4 - Reply to Now Assist... Enter actions.
5 - Now Assist message Indicates that the answers are generated by
AI.
6 - Active chats All active chats display in the Active chats
section. in the Active chats section of the Now
Assist. You can create additional chats by
selecting the + icon in the heading.
7 - Closed chats Displays all closed chats. If you select a closed
chat, the chat's history displays.
The Now Assist subheader consists of these elements:

<!-- page 21 -->
Now Assist subheader elements
Element Description
1. Chats ( )
All chats appear.
Chats are organized with the most recent
conversations at the top. Selecting a chat
opens the chat in the conversation area. If
there are unread chats or notifications, a
badge number appears on the Chats icon
( ). Any unread chat or notification appears
with a red dot next to it and the chat title
appears in bold. Additionally, if you switch to a
new chat while another active chat is ongoing,
a pop-up message on the Chats icon ( )
appears: Your previous chat was
saved. You can revisit all of
your past chats and continue
ones that are still active. The
following list includes the chat sections that
you may see in the chats area.

<!-- page 22 -->
Now Assist subheader elements (continued)
Element Description
•Active: Chats where you can continue the
conversation. If applicable, active chats
move to the Closed chats section after two
hours of inactivity. This 2 hour time limit
can be configured within the Messaging
Channels {sys_cs_channel.list} table. To
change the inactivity time limit, from the
Messaging Channels {sys_cs_channel.list}
table, select the NASS record and populate
the Conversation Idle Timeout field with
your preferred active chat time limit. If you
have no active chats, No chatter at
the moment is displayed. If more than 12
active chats are running, a Show more link
appears to view more chats. Selecting Show
more displays an additional 10 chats.
•Closed: Closed chats can be configured
to display. A message closes when the
designated time has passed (2 hours of
inactivity) or you receive the following
response in the chat: It looks like
you're finished with this
chat, so I'll go ahead and
close it. Turn on closed chats by
selecting the Show closed chats check
box within Conversational Interfaces >
Assistants > [Selected Assistant Name]
> Chat experience > Closed chats. After
being turned on, closed chats are displayed
for as long as they’re available within the
Conversations (sys_cs_conversation)
table. Closed chats appear in a read-only
mode and can’t become active again. If
more than four closed chats are available,
a Show more link appears to view more
closed chats. Selecting Show more displays
an additional 10 closed chats. After a
conversation has closed, you can’t reopen
it. Hovering over a closed chat displays the
delete icon (). Confirm the chat deletion on
the Delete this chat? modal to permanently
delete the chat from the interface.
2. [Chat name]
The name of the conversation.
If you select a promoted asset or query, that
asset's title appears as the chat name. If
instead you enter an utterance into the Reply
to Now Assist field, your initial utterance
becomes the chat name. The chat name

<!-- page 23 -->
Now Assist subheader elements (continued)
Element Description
appears in both the Now Assist subheader
and Chats list > Active section.
3. New chat ( )
A new conversation begins.
You may be prompted with a greeting message
along with any promoted conversational
assets such as topics, subflows, and/or
actions, or suggested queries.
4. Feedback icons panel You can indicate if the response was helpful
by selecting the like thumbs up icon or if
the response wasn't helpful, you can select
the dislike thumbs down icon . You can
also copy the response by selecting the copy
message icon .
Now Assist panel is available on Next Experience and ServiceNow Studio. The following
screenshots show the Now Assist panel in a workspace and on Core UI screens under Next
Experience.
Now Assist panel
Next Experience Core UI
Response feedback
Each Virtual Agent response includes a feedback icons panel. The feedback icons panel
appears on the latest Virtual Agent response and whenever you hover over any Virtual Agent
response. You can indicate if the response was helpful by selecting the like thumbs up icon ( ).
If the response wasn't helpful, select the dislike thumbs down icon ( ). When you select the
thumbs up or thumbs down icon, you are prompted to provide detailed feedback by selecting
one or more reason check boxes. You can also select Other to add comments or suggestions (up
to 300 characters). After making your selection, select Submit to submit your feedback or select
X to close the dialog without submitting feedback. All submitted feedback is captured, stored,
and made available through analytic dashboards.

<!-- page 24 -->
Example of additional feedback panel from thumbs down icon
Depending on the context of the response, an additional go to search results icon ( ) may
appear in the feedback icons panel. This icon appears alongside synthesized responses in
Virtual Agent, clarifying questions in Virtual Agent, and regular search results or Virtual Agent
fallback topics whenever a synthesized response is unavailable. Selecting the go to search
results icon ( ) redirects you to the search results page and begins a search query using
the last five chat utterances you entered. Additionally, a copy message icon ( ) appears on
received Virtual Agent responses.
Agentic conversations
Note: Admins must first enable AI agents before end users can experience agentic
conversations. Now Assist panel discovers and executes agentic workflows. For more
information on agentic workflows, see Now Assist agentic workflows and Multiple
conversations in Now Assist AI agents.
When you ask a question to the Now Assist panel enhanced chat, the agent understands the
query and begins a flow. When you submit a message with multiple questions or requests, Now
Assist panel enhanced chat answers the multiple questions consecutively in its response. It can
reason, plan, and execute across AI agents, Now Assist panel topics, conversational actions and
subflows, catalogs, Knowledge Base articles, custom skills, and any Now Assist supported skills
to help you. You receive on-screen messages to let you know where the agent is in the agentic
processing flow prior to receiving the response. After the processing has completed its flow, a
View AI Steps section header appears, where the processing flow steps can be expanded and
viewed. You can stop the agentic processing flow at any time by selecting the End flow icon ( ).
After an action starts, it can't be stopped. Selecting the End flow icon only stops the proceeding
processing steps.
If your question is unclear or could apply to multiple topics, Now Assist evaluates your request
and may ask for clarification before responding. This helps you receive a focused, relevant
answer rather than an overwhelming list of results. If the assistant is confident it understands
your intent, it responds immediately without asking for clarification. If no relevant answer is
found, the assistant displays a message and suggests an alternative, such as contacting
support.
Processing messages are short status updates that appear on-screen while Now Assist works on
your request. They reflect what Now Assist is actively doing at each step, such as searching for

<!-- page 25 -->
information or analyzing a document, and update as each step completes. Processing messages
don’t appear for simple interactions such as greetings, which are handled instantly.
Navigating from the Now Assist panel
You can navigate from the Now Assist panel without leaving the current conversation by
entering a navigation request in the Ask Now Assist to... field. If you enter "navigate me to active
incidents," Now Assist displays a button that enables you to view the active incidents.
Chat summarization
Quickly learn the details of a chat by reading a chat summarization. The chat summarization
gives you enough details about the chat so that your requester doesn't have to repeat the same
information to you.
To generate a chat summarization from the Now Assist panel, select Chat Summarization or
enter summarize chat in the Ask Now Assist to field.
Note: You can also generate a chat summarization by using the /summarize quick
action in Agent Chat.
Case or incident summarization
Quickly learn the details of a case or incident by reading a case summarization. The
summarization gives you enough details about the interaction so that your requester doesn't
have to repeat the same information to you.
You can generate a case or incident summarization from the Now Assist panel for Now Assist for
CSM, Now Assist for HRSD, or Now Assist for ITSM:
•For Now Assist for CSM, select Summarize record or enter summarize a record in the
Ask Now Assist to field.
•For Now Assist for HRSD, select Summarize record or enter summarize a record in the
Ask Now Assist to field.
•For Now Assist for ITSM, select Summarize incident or enter summarize an incident in
the Ask Now Assist to field.
Conversation Help
Get specific and accurate answers to your queries by using the Get Help skill option on the Now
Assist panel. This skill is available to everyone entitled to Now Assist capabilities.
For more information about the Now Assist Conversational Help skill that represents as Get Help
on the Now Assist panel, see Now Assist Conversational Help.
Resolution notes generation
Quickly learn the details of how an interaction was resolved by generating and reading resolution
notes.
To generate resolution notes from the Now Assist panel, select Generate resolutions notes or
enter generate resolutions notes in the Ask Now Assist to field.
Streaming responses
After you enter a question or request on the Now Assist panel, Now Assist gathers information
from Knowledge Base articles, external content, product documentation, catalog items, and

<!-- page 26 -->
workflows and combines them into a synthesized, comprehensive answer. Instead of waiting for
the entire message to render, the synthesized response streams in real time and stops streaming
after the entire message has been delivered. An animated sparkle icon ( ) appears while the
response is generated and changes to the static sparkle icon after the response has fully loaded.
Fallback options
Note: For more information about where and how to enable fallback options, see Manage
an assistant chat experience .
A fallback state can occur whenever search results are unavailable. Scenarios where search
results are unavailable include when Now Assist didn't understand the query, complaint small
talk was found, or an error occurred. When search results are unavailable, the Search the web
fallback option may appear. If you select the Search the web fallback option, the web search
mode is triggered and uses the internet to search for the results.
Note: Only the last query entered into the conversation is considered when entering web
search mode via this Search the web fallback option.
Example of Search the web fallback option
Premium chat
Now Assist panel premium chat is an AI chat experience built into your ServiceNow environment
that lets you ask questions, get answers from your organization's knowledge, and take action on
records — all in one place. It supports file uploads, web search, and multi-step agentic tasks, so
you can handle more complex requests without leaving the panel.
Important:

<!-- page 27 -->
•Next Experience must be enabled to use the Now Assist panel. For more information, see
Considerations for activating Next Experience .
•Now Assist panel premium chat must be activated before you can use it. See Display your
assistant on Platform or ServiceNow Studio for more information.
•If you want to use assistants, you must activate them. See Configuring assistants overview for
information on activating assistants.
•To use the full capabilities of Now Assist panel premium chat, AI Search must be enabled for
your portal. Without it, Now Assist panel premium chat functions in a limited capacity. Basic
interactions such as predefined topic flows and simple questions and answers are available,
but knowledge article retrieval, AI responses grounded in instance content, and semantic
search capabilities require AI Search. For more information, see Enable and configure AI
Search in Service Portal .
•Now Assist skills must be enabled to appear on the Now Assist panel. For more information,
see Activate a Now Assist skill.
•Conversational aspects of the Now Assist panel, such as skill detection, are powered by Now
LLM Service.
To begin, select the Now Assist icon to display the Now Assist panel.
Now Assist panel
The Now Assist panel includes:
Item number Description
Expands the chat into a 90% screen-size
1 - Expand
window. The 90% screen-size window can’t
be resized or moved. Selecting the icon again

<!-- page 28 -->
Item number Description
resizes the chat back into the floating window.
You can also resize the chat window using the
window's edges.
Positions, or pins, the Now Assist panel to the
2 - Pin
screen.
Closes the Now Assist panel.
3 - Close
Displays the Chat History window. A red dot
4 - Chat history
appears on the icon if you have any unread
chats.
Chat history with unread chats
Starts a new Now Assist panel conversation.
5 - New conversation
6 - Input bar Enter your prompt or request.
If voice input is enabled, select the
7 - Voice input
microphone icon and speak your message.
Your speech is transcribed and appears in the
input bar in real time.
Note: Voice input must be enabled by
an administrator before it is available.
Administrators can enable or disable
voice input at the instance level.
Individual users can also turn voice input
on or off.
8 - Add files & images/Include Web Add files and images
Upload files during conversations to help
the assistant understand your request. The
assistant reads uploaded files and uses that
content to fill required fields and answer
questions.
You can also upload images to help the
assistant understand a visual situation. The
assistant analyzes the uploaded content and
can answer natural-language questions about
it, generate summaries, and recommend or
execute actions based on what it sees. For
example:
•Upload a screen shot of an error message
and ask, "What error is shown here?"
•Upload a photo of a damaged device and
ask Now Assist to create an incident

<!-- page 29 -->
Item number Description
When referencing visual content, the assistant
can identify specific image regions in its
response.
Uploaded files are retained only during your
active session and cleared automatically when
the session ends. Supported file formats are:
•PDF
•JPEG
•TXT
•CSV
•PNG
You can upload a maximum of 5 files per
conversation. You can change the model
provider at the instance level by navigating
to Now Assist Admin > Skills > Settings.
If the provider is set to anything other than
Azure, the Add files & images option will not be
visible.
Include Web
If you select the Include Web option, the
assistant's search is expanded to include
internet results alongside internal knowledge
base articles and catalog items. Your prior
conversation context carries over when
Include Web is enabled, though sensitive
personal information such as your name,
email address, and phone number is removed
before being shared externally. To help answer
location-aware or company-specific questions,
publicly available information such as your
location and company name may be included
in the web search. Responses indicate which
parts of the answer come from web sources,
and citations for web results show the page
title and web link. The Include Web setting is
preserved if you return to a past conversation
that had it enabled.
9 - Previously used prompts Prompts that you've previously entered.
10 - Now Assist message Indicates that the answers are generated by
AI.
If you select the Chat History icon , the Chat History window appears:

<!-- page 30 -->
Now Assist Chat History window
The Chat History panel displays the following:
Item Description
A - New Chat Start a new conversation.
You may be prompted with a greeting message
along with any promoted conversational
assets such as topics, subflows, and actions,
or suggested queries. If more than 6 promoted
topics are enabled, the first 6 topics appear
along with a View all topics option that
displays the complete list.
This record
Conversations related to the current record
you're viewing.
This section appears only when you're
viewing a specific record, such as an incident
or case. When you open the Now Assist
panel while on a record, the most recent
conversation associated with that record
is automatically displayed. Conversations

<!-- page 31 -->
Item Description
in this section are identified by the record
number prefix in the conversation title—for
example, INC0012345 — My laptop won't turn
on. The same conversation may appear in
both This record and Active sections if it's still
in progress. When you navigate to a different
record, the This record section updates to
show conversations for the new record. When
you navigate to a home page or list view, this
section is hidden.
B - Active Chats where you can continue the
conversation.
Unread chats are indicated with a red dot.
Active chats include both record-specific
conversations and general conversations.
Record-specific conversations may also
appear in the This record section if you're
currently viewing that record. Active chats
move to the Closed chats section after
two hours of inactivity. Configure this 2-
hour time limit in the Messaging Channels
[sys_cs_channel] table. To change the
inactivity time limit, select the NASS
record from the Messaging Channels
[sys_cs_channel] table and populate the
Conversation Idle Timeout field. If more than
12 active chats are running, a Show more link
appears. Selecting Show more displays an
additional 10 chats.
When you navigate to a record page, the
panel displays the most recent conversation
associated with that record in the This record
section of Chat History. If you navigate away
and return to the same record, the panel
restores that conversation automatically. If you
switch to a different record, the This record
section updates to show conversations for the
new record. Conversations tied to a specific
record are identified by the record number
prefix in the conversation title — for example,
INC0012345 — My laptop won't turn on.
C - Closed A message closes when the designated time
passes (2 hours of inactivity) or you receive
this response: It looks like you're
finished with this chat, so
I'll go ahead and close it. Turn
on closed chats by selecting the Show closed
chats check box in Conversational Interfaces
> Assistants > [Selected Assistant Name] >
Chat experience > Closed chats. After being

<!-- page 32 -->
Item Description
turned on, closed chats are displayed for as
long as they're available in the Conversations
[sys_cs_conversation] table. If more than four
closed chats are available, a Show more
link appears. Selecting Show more displays
an additional 10 closed chats. Closed chats
cannot be reopened. Hovering over a closed
chat displays the delete icon.
The Now Assist feedback icons panel consist of these elements:
Note: If search results involve personalized or user-specific information, you will not be
able to access more than 10 results even if they're available.
Now Assist feedback icons panel
Element Description
1 - [Chat name] The name of the conversation.
If you select a promoted asset or query, that
asset's title becomes the chat name. If instead
you enter a prompt into the Reply to Now
Assist field, your initial prompt becomes the
chat name. The chat name appears in both the
Now Assist subheader and Chats list > Active
section.
Select the thumbs up icon if the response was
2 - Thumbs up (like)
helpful, or the thumbs down icon if it wasn't.
Thumbs down (dislike)

<!-- page 33 -->
Now Assist feedback icons panel (continued)
Element Description
Copy the response.
3 - Copy
4 - Download Displays a menu with options to download the
conversation as a PDF or DOC file.
5 - Sources and more Opens a panel showing the sources used to
generate the response, along with related
content. From the panel you can select View
all results to navigate to the global search
page.
Now Assist panel is available on Next Experience and ServiceNow Studio. The following
screenshots show the Now Assist panel in a workspace and on Core UI screens under Next
Experience.
Now Assist panel
Next Experience Core UI
Response feedback
Each Virtual Agent response includes a feedback icons panel. The feedback icons panel
appears on the latest Virtual Agent response and whenever you hover over any Virtual Agent
response. You can indicate if the response was helpful by selecting the like thumbs up icon .
If the response wasn't helpful, select the dislike thumbs down icon . When you select the
thumbs up or thumbs down icon, you are prompted to provide detailed feedback by selecting
one or more reason check boxes. You can also select Other to add comments or suggestions (up
to 300 characters). After making your selection, select Submit to submit your feedback, or select

<!-- page 34 -->
X to close the dialog without submitting feedback. All submitted feedback is captured, stored,
and made available through analytic dashboards.
Example of additional feedback panel from thumbs down icon
Depending on the context of the response, an additional go to search results icon may
appear in the feedback icons panel. This icon appears alongside synthesized responses in
Virtual Agent, clarifying questions in Virtual Agent, and regular search results or Virtual Agent
fallback topics whenever a synthesized response is unavailable. Selecting the go to search
results icon redirects you to the search results page and begins a search query using the last
five chat utterances you entered. Additionally, a copy message icon ( ) appears on received
Virtual Agent responses.
Multi-intent requests
When your request combines information from both internal and external sources, Now Assist
breaks it into steps and handles each part separately before delivering a combined response.
For example, if you ask Now Assist to find a product online and then order it through your
company's catalog, Now Assist searches the web for the product information and executes the
catalog item as separate steps, then combines the results into a single cohesive answer. You
receive on-screen processing messages as each step completes.
Agentic conversations
Admins must first enable AI agents before end users can experience agentic conversations.
Now Assist panel discovers and executes agentic workflows. For more information on agentic
workflows, see Now Assist agentic workflows and Multiple conversations in Now Assist AI agents.
When you ask a question to the Now Assist panel premium chat, the agent understands the
query and begins a flow. When you submit a message with multiple questions or requests, Now
Assist panel premium chat answers them consecutively. It can reason, plan, and execute across
AI agents, Now Assist panel topics, conversational actions and subflows, catalogs, Knowledge
Base articles, custom skills, and any Now Assist supported skills to help you. You receive on-
screen messages showing where the agent is in the agentic processing flow prior to receiving
the response. After the processing completes, a View AI Steps section header appears where
you can expand and view the processing flow steps. You can stop the agentic processing flow at
any time by selecting the End flow icon ( ). After an action starts, it can't be stopped. Selecting
the End flow icon only stops the subsequent processing steps.

<!-- page 35 -->
If your question is unclear or could apply to multiple topics, Now Assist evaluates your request
and may ask for clarification before responding. This helps you receive a focused, relevant
answer rather than an overwhelming list of results. If the assistant is confident it understands
your intent, it responds immediately without asking for clarification. If no relevant answer is
found, the assistant displays a message and suggests an alternative, such as contacting
support.
You can explore a response in more depth without asking your original question again. Follow-
up requests such as "show more detail," "compare sources," "summarize by theme," or "what's
missing?" remain anchored to the same retrieved context. The context resets when you start a
new conversation. You can also start a follow-up conversation in the Now Assist panel directly
from a search result in workspace. When viewing a search result, select the follow-up option to
open the Now Assist panel with the result as context for your next question.
Processing messages are short status updates that appear on-screen while Now Assist works on
your request. They reflect what Now Assist is actively doing at each step, such as searching for
information or analyzing a document, and update as each step completes. Processing messages
don’t appear for simple interactions such as greetings, which are handled instantly.
When an agentic workflow requires your input before it can continue, the processing messages
pause and no loading indicator is displayed. After you provide the requested input, a new
processing message appears to indicate that Now Assist has resumed processing your request.
When you view search results in a workspace, you can continue exploring a topic by asking a
follow-up question in the Now Assist panel. Select Ask a follow-up from the search result to open
the Now Assist panel and then enter your follow-up question in the input bar.
Navigating from the Now Assist panel
You can navigate from the Now Assist panel without leaving the current conversation by
entering a navigation request in the Ask Now Assist to... field. If you enter "navigate me to active
incidents," Now Assist displays a button that enables you to view the active incidents.
Chat summarization
Quickly learn the details of a chat by reading a chat summarization. The chat summarization
gives you enough details about the chat so that your requester doesn't have to repeat the same
information.
To generate a chat summarization from the Now Assist panel, select Chat Summarization
or enter summarize chat in the Ask Now Assist to field. You can also generate a chat
summarization by using the /summarize quick action in Agent Chat.
Case or incident summarization
Quickly learn the details of a case or incident by reading a case summarization. The
summarization gives you enough details about the interaction so that your requester doesn't
have to repeat the same information.
You can generate a case or incident summarization from the Now Assist panel for Now Assist for
CSM, Now Assist for HRSD, or Now Assist for ITSM:
•For Now Assist for CSM, select Summarize record or enter summarize a record in the
Ask Now Assist to field.
•For Now Assist for HRSD, select Summarize record or enter summarize a record in the
Ask Now Assist to field.
•For Now Assist for ITSM, select Summarize incident or enter summarize an incident in
the Ask Now Assist to field.

<!-- page 36 -->
Resolution notes generation
Quickly learn the details of how an interaction was resolved by generating and reading resolution
notes.
To generate resolution notes from the Now Assist panel, select Generate resolutions notes or
enter generate resolutions notes in the Ask Now Assist to field.
Streaming responses
After you enter a question or request on the Now Assist panel, Now Assist gathers information
from Knowledge Base articles, external content, product documentation, catalog items, and
workflows and combines them into a synthesized, comprehensive answer. Instead of waiting for
the entire message to render, the synthesized response streams in real time and stops streaming
after delivery. An animated sparkle icon ( ) appears while the response is generated and
changes to the static sparkle icon after the response has fully loaded. Synthesized responses
include inline citations that identify the sources used to generate the answer. Up to three inline
citations appear within the response. Select a citation to open the source in a new browser
tab. To view all sources and related results, select Sources and more. External links, such as
those from web search results, open in a new browser tab. Your current tab and Now Assist
conversation are not affected.
Single search results
When your request returns a single result, Now Assist displays a card with the most relevant
fields for that record and fields with no information are hidden automatically. Fields with no
information are hidden automatically to keep the response easy to read. The fields displayed are
either configured by your administrator or determined automatically based on your query.
•People results: The card includes available contact and profile details. Select View profile to
open the full profile in interactive view or select the org chart icon to view the person's position
in the org chart.
•Records (such as incidents or assets): Select the link in the card to open the full record. The
record opens in the current tab and the Now Assist panel automatically collapses to pinned
mode. If the record can't open in the current tab, it opens in a new browser tab instead.
•Actions and topics: Select the card to launch the corresponding action or topic directly in the
chat.
•Catalog items: Select the card to open the catalog form. To open the form in the current tab,
select the pop-out icon. The Now Assist panel collapses to pinned mode. If the form can't open
in the current tab, it opens in a new browser tab instead. If the catalog form contains links to
additional content, selecting those links loads the new content within the same interactive
view and a back button appears. Select the back button to return to the previously viewed
content.
•Knowledge Base articles: Select the card to open the article. To open the article in the current
tab, select the pop-out icon. The Now Assist panel collapses to pinned mode. If the article can't
open in the current tab, it opens in a new browser tab instead. This works for both internal and
external knowledge base sources. If the article contains links to additional content, selecting
those links loads the new content within the same interactive view and a back button appears.
Select the back button to return to the previously viewed content.
When only one result is found, the View all link does not appear at the end of the response.
Records displayed in the response are not shown as citations in the sources panel.

<!-- page 37 -->
Switching between interactive views
When a conversation contains more than one interactive view — for example, a Knowledge Base
article and a catalog form opened during the same conversation — you can switch between them
using the drop-down selector in the interactive view header. The header always displays the
name of the most recently opened interactive view. The first time you open a second interactive
view in a conversation, a message appears letting you know you can use the drop-down selector
to switch between views. Each interactive view in the conversation is represented by a thumbnail
card in the chat. The thumbnail card for the currently visible view shows Hide. Selecting a
different view from the drop-down selector updates the thumbnail card statuses accordingly —
the newly visible view shows Hide, and the previous view shows Show.
Submitting catalog requests
You can submit catalog requests directly from the Now Assist panel without leaving the chat
experience.
To submit a catalog request:
1.Open the Now Assist panel.
2. Find a catalog item through chat.
3. Select the item and a catalog form opens inline in the interactive view.
4.Complete the required form fields.
5. Select Submit. A confirmation message appears and your request record is created.
Catalog submission confirmation
After you successfully submit a catalog item, a confirmation message appears with a View
Details button that opens your submitted request record.
The View Details button behaves in the following ways:
•In Now Assist panel: Select View Details to open the submitted request record in the current
tab. The Now Assist panel automatically shrinks to pinned mode.
•In pop-out windows: If you select the pop-out icon on a submitted catalog form, the new
window displays the submission confirmation page with your request details, not a blank form
to start over.
Unsaved catalog form changes
If you start filling out a catalog form in the Now Assist panel and navigate to other content before
submitting, such as selecting another catalog item or knowledge article, a confirmation modal
appears asking whether you want to stay or leave without saving.
•To continue working on the catalog form, select Stay. The modal closes, and you return to the
catalog form with your progress intact.
•To discard changes and view new content, select Leave without saving. The form closes, your
unsaved data is discarded, and the content you selected appears in the interactive view.
Note: The discard warning modal does not appear when you switch conversations
using Chat History. It only appears when navigating to different content within the same
conversation.

<!-- page 38 -->
Multiple search results
When your request returns multiple results from Knowledge Graph, Now Assist displays them
in a table. Empty columns are hidden automatically to keep the table easy to read. The columns
displayed are determined automatically based on your query.
•People results: Use the horizontal and vertical scrollbars to view additional rows or columns.
Select a person's name to open their profile in interactive view or select the org chart icon to
view their position in the org chart.
•Record results (such as incidents or assets): Select a record number to open the full record in
the current tab. The Now Assist panel automatically reverts to pinned mode. If the record can't
open in the current tab, it opens in a new browser tab instead.
A View all link appears at the end of the response. Selecting it opens a summary page showing
all records in the current tab and the Now Assist panel reverts to pinned mode. If the records
can't open in the current tab, they open in a new browser tab instead.
If your results include more than one type of record (for example, people and incidents), a
separate View all link appears for each record type. Records displayed in the response are not
shown as citations in the sources panel. When results include a mix of records and text content
(such as knowledge base articles), Now Assist may display both a table and bullet points or text
in the same response and related records appear above the Sources and more link. Select a
record group — such as users or assets — to open the corresponding list in the current tab.
Note: If you're using Now Assist in a portal, records and View all results open in a new
portal tab.
Fallback options
A fallback state can occur whenever search results are unavailable. Scenarios where search
results are unavailable include when Now Assist didn't understand the query, complaint small
talk was found, or an error occurred. When search results are unavailable, the Search the web
fallback option may appear. If you select the Search the web fallback option, the web search
mode is triggered and uses the internet to search for the results. Only the last query entered into
the conversation is considered when entering web search mode via this Search the web fallback
option. For more information about where and how to enable fallback options, see Manage an
assistant chat experience .
If Now Assist can't find relevant results for your query, or if an answer is based on limited
evidence, Now Assist displays a message to let you know. It may also suggest ways to improve
your results, such as rephrasing your query, broadening your search scope, or specifying a time
frame or source.
If Now Assist can't find relevant results in your organization's internal content, an Include the
Web button appears in the chat. Selecting it reruns your query with web results included and
turns on Include Web mode for the rest of the conversation. Unlike the Search the web fallback
option, which only applies to your most recent query, selecting Include the Web expands all
subsequent responses to include web results.

<!-- page 39 -->
Example of Search the web fallback option
Now Assist context menu
The Now Assist context menu uses generative AI to help agents summarize, create, and edit
written content, thus streamlining their writing tasks.
Agents produce various types of content, including emails and chat replies. The Now Assist
context menu uses generative AI to assist agents in summarizing, creating, and editing emails
and chat replies. Agents can preview AI generated content, scroll through previously created
content, and refine the text using the AI. The Now Assist context menu can be triggered from any
application or field in a ServiceNow workspace where the Now Assist context menu is enabled.
The Now Assist context menu unlocks the power of generative AI and is available in Next
Experience for:
•Customer Service Management (CSM)
•Human Resources (HR)
•IT Service Management (ITSM)
•Strategic Portfolio Management (SPM)
•IT Operations Management (ITOM)
The Now Assist context menu isn’t available with Core UI.

<!-- page 40 -->
Using the Now Assist context menu
The Now Assist context menu is available on any field where the floating Now Assist button ( )
appears. If you start typing in the field, a menu appears with the available Now Assist context
menu actions. The Now Assist context menu helps you summarize, create or modify existing
documentation.
You can configure the Advanced filter to hide or show the Now Assist Context Menu quick
actions option using the wwna_quick_actions table. To view more variable set configuration
options, see unique_130.
Chat window using the Now Assist context menu
You can use the Now Assist context menu when communicating with users in Agent
Chat:
If it takes too long to generate text or the Now LLM Service isn't available, an error
message appears.
Change request risk explanation using the Now Assist context menu
The Now Assist context menu makes the change request risk explanation available
on the workspace and on UI16 after assessment and calculation.
When the risk is assessed and calculated, you’ll see the Explain risk button with the
Now Assist icon on the workspace showing the risk explanation in a dialogue
box in the Record information section.

<!-- page 41 -->
When the risk is assessed and calculated, you’ll see the Now Assist icon against
the Risk field on UI16, showing the risk explanation in a dialogue box.
Note: The risk explanation that is presented in the dialogue box is assessed
and calculated on the change request form.
For more information about risk assessment and calculation, see Risk
assessment .
Content editing in Knowledge Base articles using the Now Assist content menu

<!-- page 42 -->
The Now Assist context menu enables generative AI assisted content editing
capabilities for Knowledge Base authoring and to provide resolution notes in
workspaces and UI16.
When you open a knowledge article and select the content in it, you’ll see the Now
Assist icon pop-up and float along with your mouse device.
When you hover over the Now Assist icon, you’ll see the following menu options to
help you edit the content:
•Elaborate: Generative AI details the selected text.
•Shorten: Generative AI shortens the selected text.
You can insert the generative AI elaborated or shortened content into the
Knowledge Base articles, using the Insert button and update or publish them.

<!-- page 43 -->
For more information about generating Knowledge Base articles using the Now
Assist context menu, see Edit an article using the Now Assist context menu .
Change Tone using Now Assist context menu
The Now Assist context menu enables users to change the tone of their content.
Users can choose between casual, formal, and sympathetic tone to enhance their
content further, using the generative AI capabilities.
When you hover over the Now Assist icon or select Refine menu, you see Change
Tone menu option.
You can further choose a preferred tone and select Formal, Casual, and
Sympathetic. Review the changes and select Insert to finalize the new text.

<!-- page 44 -->
Note: If you do not see the change tone option for your application or
product, reach out to ServiceNow.
Limit the number of content refinement calls using the Now Assist context menu
Configure and limit the number of content refinements to the skill per session using
the Now Assist context menu. By default, the maximum number of refinements isn’t
set and you can configure to limit it.
You can configure the refinement calls limitation at the Recommendations Dialog
Props field in the Limit refinements record using the refineCount property.
Note: The Limit refinements record is available in the Now Assist config var
set record in the Now Assist Skill context menu application.
You can set the refineCount as follows:
•The default value of the property is -1. If the value is less than 0, then the number
of refinements to the skill are unlimited.
•If you provide 0 as the value, then the refine button will be disabled and the You
reached the limit for refining content. message is displayed.

<!-- page 45 -->
•If you configure it with a value greater than 0, you’ll be able to refine the content
according to the set value. For example, if you set the refineCount to 2, then you
will be able to refine the content only twice.
Create knowledge article with open prompt
Use NAcm to create inline knowledge article using open prompts. See Generate KB
article with Now Assist context menu.
Set the minimum word count for the Now Assist icon
You can set a minimum word count required for the Now Assist icon to appear, to
control when the icon is displayed based on content length. To set the minimum
word count, update the value for the minSelectedWordCount property.
Email recommendations using the Now Assist context menu
Use the Now Assist context menu to compose or respond to emails with recommendations from
Now Assist with generative AI template suggestions. The Now Assist context menu enables users
to generate email response recommendations in new, forward, reply, or reply all scenarios.
Compose email
While you compose a new email, you see the Now Assist context menu icon ( )
that displays the message Use Now Assist to generate a message.
When you select the icon, generative AI generates a message recommendation.

<!-- page 46 -->
You can refine the generated text either by selecting the Elaborate or Shorten
context menu options on the Now Assist Admin model. You can also copy the new
text or Insert the generated text into the email body.
Complete draft emails
You can use the Now Assist context menu to finish your drafted emails. You can
enter some text and use generative AI to help you with complete your drafts by
selecting the Now Assist context menu icon ( ) that displays the message Use
Now Assist to generate a message. When you select the icon, you see
that generative AI is generating the message for you.

<!-- page 47 -->
You can further refine the generated text by selecting Elaborate or Shorten context
menu options on the Now Assist admin model. You can also copy the new text or
select Replace to replace the generated text into the email body.
View inline citations
You can select the LLM response and view the all the related information sources
like KB articles, emails, related records, etc.
Select the numbered citations to view details along with the link to the source. You
can also select the Show sources option to view the list of all the related resource
links.
Select Replace to add the source information in the email body as plain text. The
numbered citation and all the source links will not be copied.
You can also select a record from the Now Assist Context Menu inline citation
to navigate directly to the record page, where the referenced section will be
highlighted for easy identification.
Summarize records with the Now Assist context menu
Use the Now Assist context menu to generate a record summary for the page, using Generative
AI application assisted summarization capabilities in workspaces and UI16. The Now Assist

<!-- page 48 -->
context menu can generate a new summary, expand or collapse the summary card, share the
summary to work notes, regenerate, or copy the summary.
Go to any record page to access the Now Assist context menu icon ( ) with the message
Incident Summary by Now Assist. Select Summarize to use generative AI to generate
a record summary.
You can use the Share to work notes button to share the summary to work
notes. You can also expand or collapse the summary card as required.
To provide feedback, use the feedback icons ( ) or ( ) If you're not satisfied with the
provided summary, use the regenerate icon ( ) to regenerate the summary. You can also copy
the summary to the clipboard using the copy icon ( )
Improve Docs content in Strategic Portfolio Management with Now Assist context menu
Use the Now Assist context menu to start conversations and raise queries, using generative AI
capabilities and custom built in skills in Strategic Portfolio Management.
You can now interact with Now Assist directly from the docs section in Strategic Portfolio
Management, Strategic Planning Workspace, Portfolio Planning Workspace, and Project
Workspace to ask open-ended queries, create new content, add context, or improve existing
sections. This helps you draft faster, refine ideas, and keep your work relevant without leaving the
page.
To access this feature, go to any doc page within Strategic Portfolio Management, Portfolio
Planning Workspace or Project Workspace.
Select the Now Assist icon ( ) and enter your query.

<!-- page 49 -->
The query response is generated in a new Now Assist window. You can use the input field to
provide follow-up query responses and instructions.
You can also select the Now Assist icon ( ) and use the Summarize option from the drop-down
menu to use generative AI for generating a record summary.
The Now Assist icon ( ) along with the text input field is also displayed when you select any
text from the docs page.
You can also see the option to Summarize, shorten, elaborate, or change tone for the selected
content.
Related topics
Generate and improve Docs content with Now Assist for Strategic Portfolio Management
(SPM)
Generate KB article with Now Assist context menu
Use the Now Assist context menu to generate Knowledge Base articles in Knowledge
Management.

<!-- page 50 -->
Before you begin
Role required: admin
Procedure
1.Navigate to All > Knowledge > Knowledge Center.
2. Select the list menu icon, to view all the KB articles.
3. Select a KB article from the list.
The KB article details page is displayed with an open prompt inline option for KB generation.
4.Enter the instructions for generating content, such as Generate an article for
password reset.
5. Select the Source type and Language.
6.Press enter to start the KB article generation.
The KB article preview is displayed.
Review the generated article. You can edit the content, check grammar, and make the article
easy to read. Select Regenerate to recreate the article based on your prompt.
7.Select the text to further refine the content with Now Assist Context Menu pop-over variant.

<!-- page 51 -->
8.Type or select a menu option and press enter.
Using the Now Assist Context Menu open prompt inline and pop-over variant you can quickly
produce high-quality, accurate, and lucid knowledge articles, saving time and improving
support in Knowledge Management.
Now Assist context menu usage dashboard
Use the Now Assist Context Menu dashboard to monitor the use of Now Assist context menu
across the different applications.
The Now Assist context menu usage dashboard provides insights into usage patterns,
frequency, and effectiveness of the context menu actions for the users and helps you refine the
functionalities accordingly. The dashboard contains indicators that reveal:
•Usage metrics
•Usage based on application
•Usage based on skills
•Capacity distribution
•Responses by feedback
The Now Assist context menu usage dashboard enables you to filter the data based on the
usage date. You can choose from the standard options or provide a custom range and select
apply to filter the data.

<!-- page 52 -->
You have an option to refresh, duplicate, edit, create, and export a dashboard.
You can also select the info icon () to view the dashboard-related information.
Key features
Usage matrix: The count or number of times, Now Assist context menu has been used during
the selected duration. You have the option to refresh this matrix, view insights, or suggestion
available and filter this data further based on the date.
Implicit feedback duration: The breakdown of feedback based on whether the response is
inserted and closed during the selected time range. You have the option to refresh this matrix,
view insights, or suggestion available and filter this data further based on the date.
Usage trend by skill: The total usage distribution based on the skills that use the Now Assist
context menu. You have the option to refresh this matrix, view insights, or suggestion available
and filter this data further based on the date.
Capacity Distribution: The capacity distribution based on the different applications that use the
Now Assist context menu. You have the option to refresh this matrix, view insights, or suggestion
available and filter this data further based on the date.
Response by feedback: The feedback field based on the Generative AI logs. The options are
accepted, rejected, or ignored. You can also refresh this matrix, view insights, or suggestion
available and filter this data further based on the date.

<!-- page 53 -->
Insights: View insights and suggestions for Now Assist usage.
`
Use Now Assist context menu for custom skill deployment
Use the Now Assist context menu to deploy the custom skills created using Now Assist skill kit.
AI practitioners can use Now Assist skill kit to create a custom skill to provide custom solutions,
with Now Assist's generative AI capabilities.
Now Assist allows the administrators to choose the custom skills for deployment. Use Now Assist
context menu as a preferred channel to deploy a custom skill, when you configure deployment
setting in Now Assist skill kit. For more information, see Configure skill deployment settings.
You must also select Now Assist context menu as a display option when you activate the skill in
Now Assist Admin. For more information, see Activate a Now Assist skill.
To complete the activation process, create a new Now Assist context menu configuration. For
more information, see Create Now Assist context Menu configuration
Create Now Assist context Menu configuration
Create a new Now Assist context Menu configuration to deploy and activate a custom skill.
Before you begin
To configure custom skills in action, ensure that the skill is activated in Now Assist.
Role required: sn_skill_builder.admin
Procedure
1.Navigate to All > Now Assist Admin > Now Assist Experiences > Now Assist Context Menu.
2. Select Configurations tab in the Now Assist context menu home page.
3. Select Create New.
4.Enter values for the following fields on the Configure Now Assist context menu form.
◦Workflow
◦Product
◦Name
5. Select Start Configuration.
6.Provide the following details in the General details page, on the configuration form:
◦Name
◦Description
◦Table name
7.Select a location where you want to add the trigger for the Now Assist context menu.
The options are:
◦Record form field: Select this option to add the trigger on UI16 form
◦Custom location: Select this option to add the trigger on any other desired location.
8.If you select Record form fields, add the form fields where you want the Now Assist context
menu icon.
Note: Now Assist context menu can only be set up at the table level. Currently, it doesn’t
support filtering or configuring options based on specific record conditions.

<!-- page 54 -->
9.If you select Custom location, choose the context menu display type.
Choose between the following options of display:
◦Modeless window: A draggable and resizable dialog box.
◦Embedded card: A fixed window displayed on the page.
If you select Custom location, ensure that you have completed the UIB Now Assist context
menu component configurations. For setup information see Now Assist context menu UIB
Setup .
10.Select Save and continue.
You will land on the Configure experience page.
11. Select options for the following fields on the Configure experience page:
◦Actions
◦Refinement actions
◦Turn on to prevent access refinement action
◦Maximum refinements
◦Actions for generated content
◦Enable users to provide feedback on the recommendations
Provide the same information for each of the form fields you have selected.
If you proceed without providing the required values for each form field, system will prompt you
to provide configuration.
12. Optional: When prompted, select Yes, apply on the Apply Configurations prompt if you want
to apply the same configurations.
13.Select Save and continue once you review and edit the values, if required.
You will land on the Review and activate page.
14.Select an option from the Select a record to test the configurations drop-down menu.
15.Select Preview and Done.
Create multiple Now Assist context menu skill configurations
Create multiple Now Assist context menu configuration for the same field and table.
Before you begin
You can now have multiple Now Assist context menu configurations on the same record form and
field. You just have to create the required configuration and add to the form or field.
Role required: admin
Procedure
1.Navigate to All > Now Assist Admin > Now Assist Experiences > Now Assist Context Menu.
2. Select Configurations tab in the Now Assist context menu home page.
3. Select Create New.
4.Enter values for the following fields on the Configure Now Assist context menu form.
◦Workflow
◦Product
◦Name

<!-- page 55 -->
5. Select Start Configuration.
6.Provide the following details in the General details page, on the configuration form:
◦Name
◦Description
◦Table name
The UI now allows you to add multiple configurations to the same field without any errors. This
is applicable only if you select Record form field.
7.Select Record form field as the location, to add the trigger for the Now Assist context menu on
the UI16 form.
8.Add and select one or multiple form fields in the Form Fields field.
9.Select Save and continue.
You will land on the Configure experience page. You will see a table that lists the skill
configurations along the order value, for the selected record field. The precedence is always
given to the configuration with the lowest order value.
Note:
◦In case there is a conflict due multiple configurations to the same field in a table,the
precedence is give to the configuration with the lowest order value.
◦In case there are multiple configurations, but the order value is same, the configuration
with the most recently modified date is applied to field.
10.Select options for the following fields on the Configure experience page:
◦Default Action
◦Actions
◦Refinement actions
◦Turn on to prevent access refinement action
◦Maximum refinements
◦Actions for generated content
◦Enable support for extended tables.
Provide the same information for each of the form fields you have selected.
Note:
◦To disable the inheritance model for child tables, toggle off the Enable support for
extended tables button. This model applies the parent table's configurations to a child
table if the child table does not have its own configuration.
◦Do not merge configurations. Use only the child table configuration and retrieve
configurations from the child table.
◦Apply the merging logic to use the lowest value configuration for the fields.
If you proceed without providing the required values for each form field, system will prompt you
to provide configuration.
11. Select Save and continue once you review and edit the values, if required.
You will land on the Review and activate page.

<!-- page 56 -->
12. Select an option from the Select a record to test the configurations drop-down menu.
13.Select Preview and Done.
Analyzing Now Assist performance
Use the Now Assist Analytics dashboard to monitor the usage and performance of generative AI
features and capabilities offered under Now Assist.
https://player.vimeo.com/video/1063716199?
h=247ef99aa4&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479
Get started
Explore Configure
Learn more about Now Assist Analytics Configure Now Assist Analytics
Use Reference
Use Now Assist Analytics Learn about user roles
in Now Assist Analytics
Troubleshoot and get help
•Ask questions and explore other resources for in the ServiceNow Community
•Search the Known Error Portal for known error articles
•Contact Customer Service and Support
AI limitations
This application uses artificial intelligence (AI) and machine learning, which are rapidly evolving fields of study that generate predictions based on patterns
in data. As a result, this application may not always produce accurate, complete, or appropriate information. Furthermore, there is no guarantee that this
application has been fully trained or tested for your use case. To mitigate these issues, it is your responsibility to test and evaluate your use of this application for
accuracy, harm, and appropriateness for your use case, employ human oversight of output, and refrain from relying solely on AI-generated outputs for decision-
making purposes. This is especially important if you choose to deploy this application in areas with consequential impacts such as healthcare, finance, legal,
employment, security, or infrastructure. You agree to abide by ServiceNow’s AI Acceptable Use Policy , which may be updated by ServiceNow.

<!-- page 57 -->
Data processing
This application requires data to be transferred from ServiceNow customers' individual instances to a centralized ServiceNow environment, which may be located
in a different data center region from the one where your instance is, and potentially to a third-party cloud provider, such as Microsoft Azure. This data is handled
per ServiceNow's internal policies and procedures, including our policies available through our CORE Compliance Portal .
Data collection
ServiceNow collects and uses the inputs, outputs, and edits to outputs of this application to develop and improve ServiceNow technologies including ServiceNow
models and AI products. Customers can opt out of future data collection at any time, as described in the Now Assist Opt-Out page.
Exploring Now Assist Analytics
Learn how Now Assist Analytics enables users with the Now Assist Analytics Viewer or Now
Assist Analytics Admin role to monitor the usage, value, and performance of generative AI
features and capabilities offered under Now Assist.
Now Assist Analytics overview
The Now Assist Analytics dashboard is built on the Platform Analytics experience. The
dashboard contains indicators and breakdowns that provide actionable insights into the usage,
value, and performance of your Now Assist implementation, including Now Assist Guardian, Now
Assist context menu, and search.
Now Assist Analytics users
Users
User Description
Now Assist Analytics Admin Now Assist Analytics admins monitor usage, value, and
performance of the Now Assist implementation, including Now
Assist Guardian, Now Assist context menu, and search. They
also configure skill-dashboard mappings to view individual skill
usage and performance indicators.
Now Assist Analytics Viewer View the dashboard pages to monitor usage and performance
indicators.
Now Assist Analytics benefits
Now Assist Analytics benefits
Benefit Feature Users
Monitor usage, value, and adoption of Now Assist Analytics
•Usage and adoption
Now Assist, skill performance, Now Assist Admin or Now Assist
•
Guardian, Now Assist context menu, and Analytics Viewer
search. •Skills performance
•Now Assist
Guardian analytics
•Now Assist context
menu analytics
•User search
analyzer

<!-- page 58 -->
What to explore next
To learn more about configuring and using Now Assist Analytics, see:
•Configuring Now Assist Analytics
•Using Now Assist Analytics
•Now Assist Analytics reference
Configuring Now Assist Analytics
Configure the Now Assist Analytics dashboard to view the usage, value, and performance
indicators of Now Assist.
Configuration overview
Now Assist Analytics requires at least one Now Assist application, for example, Now Assist for
Customer Service Management (CSM), to be installed and configured on your instance. See
Installing Now Assist Analytics for more information.
The following is an optional configuration task used to map a Now Assist skill to a dashboard.
Map a skill to a dashboard to view skill usage and performance indicators.
Domain Separation
Now Assist Analytics supports domain separation only for indicators using the following data
collection jobs.
•[GenAI Analytics] Daily Data Collection
•[GenAI Analytics] Historical Data Collection
•[Now Assist Analytics] Daily Data Collection
•[Now Assist Analytics] Historical Data Collection
See Approaches to Performance Analytics with domain separation for more information on
applying domain separation configuration.
Note: Be sure to check the Run as field in the data collection job records has a valid user.
Installing Now Assist Analytics
You can install the Now Assist Analytics application (sn_na_analytics) with Now Assist
applications if you have the admin role.
Installation requirements
You must be on Zurich Patch 0 or later.
Now Assist Analytics is included as a dependency for all Now Assist applications. It is not
recommended to install the application by itself. Instead, you can install Now Assist applications
from the Now Assist Admin console or directly from the ServiceNow Store. For details, see Install
Now Assist plugins.

<!-- page 59 -->
Now Assist Admin console plugin installation
Compatibility matrix
Now Assist Analytics has a dependency on Now Assist Admin. Be sure to have the compatible
version of the Now Assist Admin console based on the following compatibility matrix.
Now Assist Admin console
Now Assist Analytics version Release
version
Now Assist Analytics 2.0.14 Now Assist Admin 5.0.7 Zurich Patch 1
Now Assist Analytics 1.1.11 Now Assist Admin 4.1.16 Zurich Patch 0
Map a skill to a dashboard
Map a Now Assist skill to a dashboard to view skill performance indicators and skill details.
Before you begin
Be sure to map a dashboard with a skill in the same domain.
Note: You can only map a skill to a dashboard. Mapping a feature (that consists of multiple
skills) is currently not supported.
If you're mapping a skill to a custom dashboard, be sure to share appropriate access to the
dashboard. See Share a Platform Analytics dashboard for more information.
Roles required: sn_na_analytics.admin and sn_nowassist_admin.nsa_admin
Procedure
1.Navigate to the All menu and enter sn_na_analytics_configuration.list.
The Now Assist Analytics Configuration [sn_na_analytics_configuration] table
appears.
2. Create a new mapping by selecting New
3. On the form, fill in the fields.

<!-- page 60 -->
Now Assist Analytics Configuration record form
Field Description
Dashboard The Dashboard that you want to map to a
skill. Use the lookup icon ( ) to search for
and select the dashboard.
Application The application that contains the record.
Document Table Table that contains configured skills.
Use the lookup icon ( ) to search for
and select the Now Assist Skill Config
[sn_nowassist_skill_config] table.
Document Id The Skill that you want to map to the
dashboard. Use the lookup icon ( ) to
search for and select the skill that you want to
map to the dashboard.
Active Check box used to enable or disable the
mapping.
Order Order to set that determines the priority of
the mapping in cases where multiple skills
are mapped to the same dashboard.
4.Select Submit.
What to do next
After you've completed the mapping, go to the Skill details page and select the skill from the
drop-down list to verify that the mapped dashboard is displayed.
Using Now Assist Analytics
The Now Assist Analytics dashboard provides indicators and breakdowns that help monitor the
performance of generative AI features, capabilities, and skills active on your instance.
Access the dashboard by navigating to All > Now Assist Admin > Analytics. You must
have Now Assist Analytics Admin [sn_na_analytics_admin] or Now Assist Analytics Viewer
[sn_na_analytics_viewer] role to view the dashboard. The following sections explain the
dashboard pages in more detail.
Usage and adoption
The Usage and adoption dashboard page contains key usage and performance indicators that
help you evaluate the adoption of Now Assist in your organization.
The Usage and adoption dashboard page is the landing page for the dashboard. The Usage
and adoption dashboard page contains two tabs that provide insights on usage summary and
adoption.
The Usage summary page includes indicators on total and daily Now Assist actions, skill
distribution and engagement trend, and daily unique users who have engaged with Now Assist.
The Adoption page tracks the departments with the highest Now Assist usage, comparison of
actions by department, and feedback and error details. Use the date range, channel, and product
filters to view usage and adoption indicators for the selected period, Now Assist channel, and
product, respectively. The default date range is 30 days.

<!-- page 61 -->
Usage and adoption dashboard page
The indicators on the Usage and adoption dashboard page provide the following insights. See
Now Assist Analytics dashboard indicator details for information on data source and calculations
behind each indicator on the page.
•Skills engagement trend for a selected period can reveal skills that have been used more
frequently or less frequently.
•Total and daily actions for a selected period can reveal the scale of Now Assist actions
executed. The trend line in the visualization shows periods of increased or declining
engagement.
•Average and daily unique users can reveal user engagement with Now Assist.
Usage summary indicators
Total Now Assist actions
This area of the dashboard shows the total number of Now Assist actions in the
selected date range. A single use of a Now Assist skill represents an action. Select
a filter combination to view the number of actions by products or Now Assist
channels. For example, you can view the number of Now Assist actions executed
through the Now Assist in Virtual Agent channel for Now Assist for Customer Service
Management (CSM) product.

<!-- page 62 -->
Total Now Assist actions indicator
Daily Now Assist actions
This area of the dashboard shows the number of Now Assist actions executed per
day in the selected date range.
Daily Now Assist actions indicator
Average daily unique users engaging with Now Assist
This area of the dashboard shows the average number of daily unique users who
engaged with Now Assist actions in the selected date range. Average number of
daily unique users is an indicator of the level of Now Assist engagement across
selected Now Assist products and channels.

<!-- page 63 -->
Average number of unique users per day who triggered actions
indicator
Daily unique users engaging with Now Assist
This area of the dashboard shows the daily unique users who engaged with Now
Assist actions in the selected date range.
Daily unique users engaging with Now Assist indicator
Skill group distribution
This area of the dashboard shows the skill usage in a trend chart for the selected
filters. The visualization is interactive. Use the Group by filter to apply predefined
breakdowns. Hover over the trend lines to see the number of times that each skill
was used. Selecting one or more items in the legend removes the trend line for
those items. You can compare and contrast skill usage distribution in a date range
to understand in-demand skills, and skills that are low on usage and need further
analysis.

<!-- page 64 -->
Skill group distribution indicator
Daily usage comparison by workflow
This area of the dashboard shows the number of Now Assist actions executed per
day against each workflow in the selected date range. Hover over a bar to view the
count of Now Assist actions executed for a workflow on that day.
Daily usage comparison by workflow indicator
Skill engagement trend
This area of the dashboard shows the skill usage in a trend chart for the selected
filters. The visualization is interactive. Hover over the trend lines to see the number
of times that each skill was executed. Selecting one or more skills in the legend
removes the trend line for those skills. You can compare and contrast skill usage
levels in a date range to understand in-demand skills, and skills that are low on
usage and need further analysis.
Skills engagement trend indicator
Adoption indicators
Departments with highest usage
This area of the dashboard shows the departments with the highest usage of Now
Assist actions in the selected date range. Hover over the horizontal bars to view the
count of actions for a particular department.

<!-- page 65 -->
Departments with highest usage indicator
Now Assist actions comparison by user department
This area of the dashboard shows the number and type of Now Assist actions
executed against each department in the selected date range.
Now Assist actions comparison by user department indicator
Feedback details
This area of the dashboard shows the number of Now Assist actions, number of
feedback provided by users of Now Assist actions, and number of Now Assist
actions with positive feedback in the selected date range.
Feedback details indicator
Error details
This area of the dashboard shows the number of Now Assist actions and the
number of Now Assist actions resulting in errors.
Error details indicator

<!-- page 66 -->
Skills performance
Use the Skills performance dashboard page to view usage and performance indicators of one or
more Now Assist skills that are active.
The Skills performance dashboard page contains indicators that help you analyze the usage
and performance of active skills. Use the Date range, Product, and Skills filters to break down
by date range, Now Assist product, and skill, respectively. The filter selection applies to all
visualizations on the page. See Now Assist Analytics dashboard indicator details for information
on the data and calculations behind each indicator.
Skill Performance dashboard page
The indicators on the Skills performance dashboard page provide the following insights. See
Now Assist Analytics dashboard indicator details for information on the data and calculations
behind each indicator.
•Skills usage trend visualization for a selected period can reveal skills that have been used
more frequently or less frequently.
•The Number of actions visualization for a selected period can reveal the scale of Now Assist
skill executions. The trend line comparison shows the increasing or decreasing trend from the
previous period.
•The Total daily active users indicator shows a breakdown of daily active users by product and
skill.
Select the View skill details button to view the usage and performance indicators of skills
mapped to a dashboard.
Skills performance indicators
Skills engagement trend
This area of the dashboard shows the skill usage in a trend chart for the selected
filters. The visualization is interactive. Hover over the trend lines to see the number

<!-- page 67 -->
of times that each skill was used. Selecting one or more skills in the legend removes
the trend line for those skills. You can compare and contrast skill usage levels in
a date range to understand in-demand skills, and skills that are low on usage and
need further analysis.
Skills usage trend indicator
Number of actions
This area of the dashboard shows the number of Now Assist actions for the selected
date range, product, and skill. A single use of a skill represents an action. The
headline number is an indicator of the scale of skill usage across products. The
trend line comparison shows the increase or decrease in the number of actions
from the previous period.

<!-- page 68 -->
Number of actions indicator
Total daily active users
This area of the dashboard shows the cumulative number of daily active users
who have used Now Assist products with one or more active skills. Select a filter
combination to see skill usage patterns. For example, you can visualize the number
of users who have used the Chat Summarization skill across all products in the last
month.

<!-- page 69 -->
Total daily active users indicator
Total daily active users by skills
This area of the dashboard shows the number of daily active users who have used
Now Assist skills in the selected date range. When you hover over a date in the
visualization, a pop-over shows all active skills with the count of users against each
skill. Select a filter combination to visualize patterns in user activity.
Total daily active users by skills indicator
Skill details
Use the Skill details dashboard page to view usage and performance indicators of a skill.

<!-- page 70 -->
The Skill details dashboard page contains indicators pertaining to a specific skill. The indicators
provide insight into skill usage and performance. Select a skill from the drop-down list to view
the indicators. The drop-down lists both active and inactive skills. Each skill has a subtitle that
identifies the skill family that it belongs to, for example, ITSM, HR, and so on. Use the date range
filter to view skill usage and performance over a certain period. The date range filter selection
applies to all visualizations on the page. See Now Assist Analytics dashboard indicator details for
information on the data and calculations behind each indicator.
Skill details dashboard page
The indicators on the Skill details dashboard page provide the following insights. See Now Assist
Analytics dashboard indicator details for information on the data and calculations behind each
indicator.
•Skill engagement trend visualization for a selected period can reveal patterns in skill usage.
•Acceptance rate visualization shows how well the skill met the requirements of users who
used the skill. A high acceptance rate for a skill is an indicator of good performance. A low
acceptance rate among skill users indicates that the skill doesn’t meet the requirements either
fully or partially.
•The number of actions visualization for a selected period can reveal the scale of the skill
executions. The trend line comparison shows the increasing or decreasing trend from the
previous period.
•The daily active users visualizations show a breakdown of daily active users by skill to help you
see user activity on the skill.
Skill details indicators
The indicators on skill details pages might differ based on the skill selected. For example,
summarization skills might have different set of indicators compared to generation skills because
each skill is mapped to its own dashboard that contains a set of indicators related to the skill.
The Now Assist Analytics dashboard comes with some default skill-to-dashboard mappings to
get you started. The default dashboards are visible to users with the Now Assist Analytics Viewer
[sn_na_analytics.viewer] role. You can create your own dashboards and map them to skills. See
Create a dashboard with the in-line editor and Map a skill to a dashboard for more information
on creating custom dashboards and mapping them to skills, respectively.
The following indicators are for the Flow Generation skill.

<!-- page 71 -->
Skill usage trend indicator
This area of the dashboard shows the Flow Generation skill usage in a trend chart
for the selected filters. The visualization is interactive. Hover over the trend lines to
see the number of times the Flow Generation skill was used.
Skill usage trend indicator
Total Flow Generation actions indicator
This area of the dashboard shows the number of flow generation actions for the
selected date range. A single use of the Flow Generation skill represents an action.
The headline number is an indicator of the scale of flow generation skill usage
across products. The trend line comparison shows the increase or decrease in the
number of actions from the previous period.
Total flow generation actions indicator
Accepted flow generation actions indicator
This area of the dashboard shows the number of flow generation actions, that is, the
number of flow generation skill executions that resulted in flows that were accepted
by the users.

<!-- page 72 -->
Accepted flow generation actions indicator
Acceptance rate indicator
This area of the dashboard shows the acceptance rate of Flow Generation skill
based on user acceptance of the flow. The percentage is calculated using the
formula: (Total number of accepted flow generation actions/Total number of flow
generation actions) x 100.
Acceptance rate indicator
Custom skill details
Use the Custom skill details dashboard page to view usage and performance indicators of
custom skills.

<!-- page 73 -->
The Custom skill details dashboard page contains indicators pertaining to a custom skill. The
indicators provide insight into skill usage and performance. Select a skill from the Skills drop-
down list to view the indicators. The drop-down lists both active and inactive skills. Each skill has
a subtitle that identifies the skill family that it belongs to, for example, ITSM, HR, and so on. Use
the date range filter to view skill usage and performance over a certain period. The date range
filter selection applies to all visualizations on the page. See Now Assist Analytics dashboard
indicator details for information on the data and calculations behind each indicator.
Custom skill details dashboard page
The indicators on the Custom skill details dashboard page provide the following insights. See
Now Assist Analytics dashboard indicator details for information on the data and calculations
behind each indicator.
•Skill engagement trend visualizations for a selected period can reveal patterns in skill usage
across workflows, products, and features.
•The daily unique users visualization shows a breakdown of daily unique users by the selected
skill to help you see user activity and engagement with the skill.
•Acceptance rate visualization shows how well the skill met the requirements of users who
used the skill. A high acceptance rate for a skill is an indicator of good performance. A low
acceptance rate among skill users indicates that the skill doesn’t meet the requirements either
fully or partially.
•Skills feedback visualization shows that the feedback recorded based on user response to
each skill execution in the selected date range.
Skill details indicators
The Custom skill details page contains a common set of indicators that give you insights into
custom skills. Only those skills where the skill family is Other or the category is Custom are
shown in the skills filter on the page.
The following indicators are common across all custom skills.
Number of custom skills created
This area of the dashboard shows the number of custom skills created by the users
in the selected date range.

<!-- page 74 -->
Number of custom skills created indicator
Number of custom skills activated
This area of the dashboard shows the number of custom skills activated by the
users in the selected date range.

<!-- page 75 -->
Number of custom skills activated indicator
Number of prompts in active custom skills
This area of the dashboard shows the number of prompts in active custom skills in
the selected date range.
Number of prompts in active custom skills indicator
Number of Assists consumed by custom skills

<!-- page 76 -->
This area of the dashboard shows the number of Assists consumed by custom skills
in the selected date range.
Number of Assists consumed by custom skills indicator
Count of invocations
This area of the dashboard shows the count of invocations for the custom skills in
the selected date range.
Count of invocations indicator
Daily unique users engaging with the skill
This area of the dashboard shows the number of unique users per day who
engaged with the skill in the selected date range. The bar chart shows a trend of
increase or decrease in the number of unique users to help you understand periods
of high and low skill engagement.

<!-- page 77 -->
Daily unique users engaging with the skill indicator
Skill engagement trend by workflows
This area of the dashboard shows the skill usage across workflows in a bar chart for
the selected date range. The visualization is interactive. Hover over the bars to see
the number of times the skill was used in each of the workflows.
Skill engagement trend by workflows indicator
Skill engagement trend by products
This area of the dashboard shows the skill usage across Now Assist products in a
bar chart for the selected date range. The visualization is interactive. Hover over the
bars to see the number of times the skill was used in each of the products.
Skill engagement trend by products indicator
Skill engagement trend by features
This area of the dashboard shows the skill usage across Now Assist features in a
bar chart for the selected date range. The visualization is interactive. Hover over the
bars to see the number of times the skill was used in each of the features.
Skill engagement trend by features indicator

<!-- page 78 -->
Executed successfully
This area of the dashboard shows the acceptance rate of the selected skill based
on user feedback. The percentage is calculated using the formula: (Total number of
accepted skill executions/Total number of skill executions) x 100.
Executed successfully indicator
Skills feedback
This area of the dashboard shows the feedback recorded for each execution of the
selected skill. User feedback is categorized into the following:
•Accepted (edited & non-edited): The user accepted the skill output with or without
further edits to the output.
•Rejected: The user rejected the skill output.
•Canceled: The user canceled the skill execution.
•Ignored: The user didn't take any action based on the skill output.
Skills feedback indicator

<!-- page 79 -->
Now Assist Guardian analytics
Monitor the performance of guardrails enabled through Now Assist Guardian.
The Now Assist Guardian analytics dashboard helps admins monitor and evaluate the
effectiveness of offensive content and prompt injection guardrails in tracking and analyzing
requests sent to large language models (LLM) and their responses.
Now Assist Guardian dashboard page
The indicators on the Now Assist Guardian dashboard page provide the following insights.
•Average latency as a result of active offensive content and prompt injection guardrails. High
latency could mean increased guardrail activity in the period.
•Count and percentage of offensive content and prompt injection occurrences.
•Skills where offensive content and prompt injection occurrences were detected.
Apply the filters on the dashboard to view guardrail activity for skills in a date range. See Now
Assist Analytics dashboard indicator details for information on the data and calculations behind
each indicator.
Offensive content indicators
Guardrail-added latency
This area of the dashboard shows the average latency as a result of the active
offensive content guardrail for the selected skills and date range.

<!-- page 80 -->
Guardrail-added latency indicator
Percentage flagged as offensive
This area of the dashboard shows the percentage of requests and responses to and
from the LLM service that are flagged for offensive content.
Percentage flagged as offensive indicator
Total offensive content occurrences
This area of the dashboard shows the total number of offensive content
occurrences for the selected skills and date range.

<!-- page 81 -->
Total offensive content occurrences indicator
Categories of offensive content
This area of the dashboard shows a breakdown of offensive content occurrences by
the categories. If content is deemed to be offensive under more than one category,
for example, toxic and defamatory, the occurrence is counted individually toward
both the categories. For more information on offensive content categories, see Now
Assist Guardian.
Categories of offensive content indicator
Offensive content occurrences by skill
This area of the dashboard shows the number of offensive content occurrences
over time by the skills in which the content is detected.
Offensive content occurrences by skill indicator

<!-- page 82 -->
Prompt injection indicators
Guardrail-added latency
This area of the dashboard shows the average latency as a result of the active
prompt injection guardrail for the selected skills and date range.
Guardrail-added latency indicator
Percentage flagged as prompt injection
This area of the dashboard shows the percentage of requests and responses to and
from the LLM service that are flagged for offensive content.
Percentage flagged as prompt injection indicator
Total prompt injection occurrences
This area of the dashboard shows the total number of offensive content
occurrences for the selected skills and date range.

<!-- page 83 -->
Total prompt injection occurrences indicator
Prompt injection occurrences by skill
This area of the dashboard shows the number of prompt injection occurrences over
time by the skills where prompt injection attempts were detected.
Prompt injection occurrences by skill indicator
User search analyzer
Gain insights into user search queries and results provided by Now Assist.
The User search analyzer dashboard page contains indicators that help admins understand the
effectiveness of search in enhancing the self-service experience. Equipped with insights from
the dashboard, Knowledge admins can improve Knowledge content and availability for search.

<!-- page 84 -->
User search analyzer dashboard page
The indicators on the User search analyzer dashboard page provide the following insights. See
Now Assist Analytics dashboard indicator details for information on the data and calculations
behind each indicator.
•Search queries that yielded Knowledge Base articles and catalog items as Genius Result.
•Distribution of search queries by the source that they originated from, for example, Now Assist
in Virtual Agent, Service Portal.
•List of the most common queries that did or didn’t yield genius results.
User search analyzer indicators
Queries with Genius Results
This area of the dashboard total number of search queries that had a Genius Result
returned by Now Assist.
Note: A query can have more than one genius result.

<!-- page 85 -->
Queries with Genius Results indicator
Genius Result Engagement
This area of the dashboard shows the number of genius results returned by Now
Assist that covers the interactions like "Ask a follow up" or "Show full answer", and
clicking on citations within the result card.
Genius Result engagement indicator
Genius Result response time

<!-- page 86 -->
This area of the dashboard shows the average response time taken for a Genius
Result to load.
Genius Result response time indicator
Genius Result to chat handoff
This area of the dashboard shows the number of times users clicked the Ask a
follow-up button within the synthesized Genius Result.
Genius Result to chat handoff indicator
Genius Results citation engagement

<!-- page 87 -->
This area of the dashboard shows the number of interactions with citations within
Genius Result returned by Now Assist.
Genius Results citation engagement indicator
Feedback (Thumbs up)
This area of the dashboard shows the count for positive feedback for Genius Result
returned by Now Assist.
Feedback (Thumbs up) indicator
Feedback (Thumbs down)

<!-- page 88 -->
This area of the dashboard shows the count for negative feedback for Genius Result
returned by Now Assist.
Feedback (Thumbs down) indicator
Genius Results with Knowledge Base
This area of the dashboard shows the number of search queries where Now Assist
returned Knowledge Base articles as Genius Result for the users to review.
Genius Results with Knowledge Base indicator
Genius Results with Catalog Item
This area of the dashboard shows the number of search queries where Now Assist
returned catalog items as Genius Result for the users to review.

<!-- page 89 -->
Genius Results with Catalog Item indicator
Top 10 queries with Knowledge Base Genius Result
This area of the dashboard shows the top ten search queries where Now Assist
returned Knowledge Base as Genius Result, with respective query count.

<!-- page 90 -->
Top 10 queries with Knowledge Base Genius Result
Top 10 queries with Catalog Item Genius Result
This area of the dashboard shows the top ten search queries where Now Assist
returned catalog items as Genius Result, with respective query count.

<!-- page 91 -->
Top 10 queries with Catalog Item Genius Result indicator
Now Assist context menu analytics
Monitor the usage and performance of the Now Assist context menu.
The Now Assist context menu dashboard helps admins to evaluate the effectiveness of context
menu actions in assisting agents with summarizing, creating, and editing emails and chat replies.

<!-- page 92 -->
Now Assist context menu dashboard page
The indicators on the Now Assist context menu dashboard page provide the following
insights. See Now Assist Analytics dashboard indicator details for information on the data and
calculations behind each indicator.
•Count and distribution of context menu actions in a date range. This indicator reveals the scale
of usage, and the most and least used actions.
•Acceptance and feedback on context menu actions. This indicator reveals actions that were
accepted or rejected by the users with a positive or negative feedback.
•Usage trend chart reveals patterns in usage of context menu actions over a date range.
Now Assist context menu indicators
Usage in this period
This area of the dashboard shows the total number of Now Assist context menu
actions used in the selected date range.
Usage in this period indicator
Acceptance distribution

<!-- page 93 -->
This area of the dashboard shows the distribution of Now Assist context menu
actions by their acceptance.
•Accepted: The user has inserted the context menu response into their workspace.
•Not Accepted: The user has closed the window or dialog box containing the
context menu response.
Acceptance distribution indicator
Usage trend by skill
This area of the dashboard shows the usage trend of Now Assist context menu
actions in the selected date range.
Usage trend by skill indicator
Capability distribution
This area of the dashboard shows the usage distribution of various Now Assist
context menu actions in the selected date range.
Capability distribution indicator
Responses by feedback

<!-- page 94 -->
This area of the dashboard shows a breakdown of Now Assist context menu
responses by the user feedback received.
•Accepted: The user gave a thumbs up on the context menu response.
•Rejected: The user gave a thumbs down on the context menu response.
Responses by feedback indicator
Now Assist Analytics reference
Now Assist Analytics reference topics include information about user roles and details of the
indicators on the dashboard.
Now Assist Analytics roles
Now Assist Analytics requires the following roles to view and manage the dashboard
functionality.
Now Assist Analytics Viewer [sn_na_analytics.viewer]
Users with the Now Assist Analytics Viewer role can view the Now Assist Analytics dashboard in
the Now Assist Admin console, and have read access to data source tables.
Contains Roles
List of roles contained within the role.
None.
Groups
List of groups that this role is assigned to by default.
None.
Special considerations
None.
Now Assist Analytics Admin [sn_na_analytics.admin]
Users with Now Assist Analytics Admin role can view the Now Assist Analytics dashboard in the
Now Assist Admin console, and read and write to some data source tables.

<!-- page 95 -->
Contains Roles
List of roles contained within the role.
Now Assist Analytics Viewer [sn_na_analytics.viewer].
Groups
List of groups this role is assigned to by default.
None.
Special considerations
Avoid granting an admin role when more specialized roles are available.
Now Assist Analytics dashboard indicator details
Indicator details help you understand the data and calculations behind an indicator that is
presented in the form of a visualization on the dashboard.
Now Assist Analytics indicators contain the following details: indicator type, data source,
calculation, available breakdowns, unit, and so on.
To access these indicators, navigate to Platform Analytics Administration > Indicators.
You must have the Now Assist Analytics Admin [sn_na_analytics_admin] role to access the
indicators.
These indicators collect data at a daily frequency. Data is only available for dates before the
current date. If you want to see results from the current day, you must wait until the next day.
Note: The Generative AI Usage Log [sys_gen_ai_usage_log] table is maint-only.
Usage and adoption indicator details
Indicator Available
Visualization Indicator source table Calculation Frequency Unit Precision
type breakdowns
Total AutomatedGenerative AI Usage Count By Daily 0
Now Log[sys_gen_ai_usageo_fl oagll ] Gen AI
Assist actions Feature,
actions By
Generative
AI Skill
Execution
Modality,
By Skill
Family,
By Skills
Config,
By Skills
Config,
By
Workflow
Daily AutomatedGenerative AI Usage Count By Daily 0
Now Log[sys_gen_ai_usageo_fl odga]ily Gen AI
Assist actions Feature,
actions By

<!-- page 96 -->
Indicator Available
Visualization Indicator source table Calculation Frequency Unit Precision
type breakdowns
Generative
AI Skill
Execution
Modality,
By Skill
Family,
By Skills
Config,
By Skills
Config,
By
Workflow
Average AutomatedGenerative AI Usage Average By Daily 0
daily Log[sys_gen_ai_usageo_fl odga]ily Gen AI
unique unique Feature,
users users By Skills
engaging Config,
with Now By Skill
Assist Family,
By
Generative
AI Skill
Execution
Modality
Daily AutomatedGenerative AI Usage Count By Daily 0
unique Log[sys_gen_ai_usageo_fl odga]ily Gen AI
users unique Feature,
engaging users By Skills
with Now Config,
Assist By Skill
Family,
By
Generative
AI Skill
Execution
Modality
Skill AutomatedGenerative AI Usage Count By Daily 0
group Log[sys_gen_ai_usageo_fl odga]ily Gen AI
distribution skill Feature,
executionBs y
grouped Generative
By AI Skill
Gen AI Execution
Feature, Modality,
By By Skill
GenerativFea mily,
AI Skill By Skills
ExecutionC onfig,
Modality, By Skills
By Skill Config,
Family, By
By Workflow

<!-- page 97 -->
Indicator Available
Visualization Indicator source table Calculation Frequency Unit Precision
type breakdowns
Skills
Config,
By
Skills
Config
Daily AutomatedGenerative AI Usage Count By Daily 0
usage Log[sys_gen_ai_usageo_fl og] Gen AI
comparison actions Feature,
by grouped By
workflow by Generative
workflowsAI Skill
Execution
Modality,
By Skill
Family,
By Skills
Config,
By Skills
Config,
By
Workflow
Skill AutomatedGenerative AI Usage Count By Daily 0
engagement Log[sys_gen_ai_usageo_fl og] Gen AI
trend actions Feature,
grouped By
by skill Generative
AI Skill
Execution
Modality,
By Skill
Family,
By Skills
Config,
By Skills
Config,
By
Workflow
DepartmenAtsu tomatedGenerative AI Usage Count By Daily 0
with Log[sys_gen_ai_usageo_fl og] Department,
highest actions By Skills
usage grouped Config
by user
department
and
sorted
by
descending
order
Now AutomatedGenerative AI Usage Count By Daily 0
Assist Log[sys_gen_ai_usageo_fl og] Department,
actions actions By Skills
comparison grouped Config

<!-- page 98 -->
Indicator Available
Visualization Indicator source table Calculation Frequency Unit Precision
type breakdowns
by user by user
department department
Feedback AutomatedGen AI Log Count By Skill Daily 0
details Metadata[sys_gen_ai_olof g_metaFdaamtai]ly,
actions By Skills
grouped Config
by Skill
Family
AutomatedGen AI Log Count By Daily 0
Metadata[sys_gen_ai_olof g_metaFdeaetad]back,
actions By Skill
with Family,
feedback By Skills
grouped Config
by Skill
Family
Formula Gen AI Log (Count By Skill Daily % 2
Metadata[sys_gen_ai_olof g_metaFdaamtai]ly,
actions By Skills
with Config
feedback/
Total
count of
actions)
x 100
grouped
by Skill
Family
AutomatedGen AI Log Count By Skill Daily 0
Metadata[sys_gen_ai_olof g_metaFdaamtai]ly,
actions By Skills
where Config,
By By
FeedbackF eedback
is
Accepted
grouped
by Skill
Family
Formula Gen AI Log (Count By Skills Daily % 2
Metadata[sys_gen_ai_olof g_metaCdaotnafi]g,
actions By Skill
where Family
By
Feedback
is
Accepted/
Total
count of
actions
with

<!-- page 99 -->
Indicator Available
Visualization Indicator source table Calculation Frequency Unit Precision
type breakdowns
feedback)
x 100
grouped
by Skill
Family
Error AutomatedGen AI Log Count By Skill Daily 0
details Metadata[sys_gen_ai_olof g_metaFdaamtai]ly,
actions By Skills
grouped Config
by Skill
Family
AutomatedGen AI Log Count By Gen Daily 0
Metadata[sys_gen_ai_olof g_metaAdIa Ltao]g
actions Metadata
with Status ,
error By Skill
status Family,
grouped By Skills
by Skill Config
Family
Formula Gen AI Log (Count By Skill Daily % 2
Metadata[sys_gen_ai_olof g_metaFdaamtai]ly,
actions By Skills
with Config
error
status/
Total
count of
generative
AI
metadata
records)
x 100
grouped
by Skill
Family
Skill performance indicator details
Indicator
Indicator Available
Visualization source Calculation Frequency Unit Precision
type breakdowns
table
Skill Automated Generative Count By Gen AI Daily 0
engagement AI Usage of skill Feature,
trend Log[sys_gene_xaei_cuustiaognes_ lBoyg ]
grouped Generative
by skill AI Skill
Execution
Modality,
By Skill

<!-- page 100 -->
Indicator
Indicator Available
Visualization source Calculation Frequency Unit Precision
type breakdowns
table
Family,
By Skills
Config, By
Workflow
Number of Automated Generative Count of By Gen AI Daily 0
actions AI Usage all skill Feature,
Log[sys_gene_xaei_cuustiaognes_lBoyg ]
Generative
AI Skill
Execution
Modality,
By Skill
Family,
By Skills
Config, By
Workflow
Total daily Automated Generative Count By Gen AI Daily 0
active AI Usage of daily Feature,
users Log[sys_genu_naiiq_uuesa ge_lBoyg ]Skills
users Config,
By Skill
Family, By
Generative
AI Skill
Execution
Modality
Total daily Automated Generative Count By Gen AI Daily 0
active AI Usage of daily Feature,
users by Log[sys_genu_naiiq_uuesa ge_lBoyg ]Skills
skills users Config,
grouped By Skill
by Skills Family, By
Config Generative
AI Skill
Execution
Modality
Skill details indicator details
Indicator
Indicator Available
Visualization source Calculation Frequency Unit Precision
type breakdowns
table
Skill Automated Generative Count By Gen AI Daily 0
engagement AI Usage of skill Feature,
trend Log[sys_gene_xaei_cuustiaognes_ lBoyg ]
grouped Generative
by Skills AI Skill
Config Execution
Modality,

<!-- page 101 -->
Indicator
Indicator Available
Visualization source Calculation Frequency Unit Precision
type breakdowns
table
By Skill
Family,
By Skills
Config, By
Workflow
Total skill Automated Generative Count By Gen AI Daily 0
actions AI Usage of skill Feature,
Log[sys_gene_xaei_cuustiaognes_lBoyg ]
Generative
AI Skill
Execution
Modality,
By Skill
Family,
By Skills
Config, By
Workflow
Accepted Automated Gen Count By Daily 0
skill AI Log of skill Feedback,
actions Metadata[syesx_egceunt_ioani_sl oBgy_ metadata]
where response
Feedback accepted
is without
Accepted edits,
By Skills
Config,
By Skill
Family
AcceptanceF ormula Gen (Count By Skills Daily % 0
rate AI Log of skill Config
Metadata[syesx_egceunt_ioani_sl og_metadata]
where
Feedback
is
Accepted/
Count
of skill
executions)x100
Daily Automated Generative Count By Gen AI Daily 0
active AI Usage of daily Feature,
users Log[sys_genu_naiiq_uuesa ge_lBoyg ]Skills
users Config,
By Skill
Family, By
Generative
AI Skill
Execution
Modality

<!-- page 102 -->
Custom skills indicator details
Indicator
Indicator Available
Visualization source Calculation Frequency Unit Precision
type breakdowns
table
Skill Automated Generative Count of By Daily 0
engagement AI Usage custom Custom
trend by Log[sys_gens_kailil_ usage_lSokgi]ll
workflows executions (Workflow
grouped Type), By
by Custom
workflows Skill
(Feature
Type), By
Custom
Skill
(Product
Type), By
Custom
Skill
Completion
Status,
By Skills
Config
Skill Automated Generative Count of By Daily 0
engagement AI Usage custom Custom
trend by Log[sys_gens_kailil_ usage_lSokgi]ll
products executions (Workflow
grouped Type), By
by Custom
products Skill
(Feature
Type), By
Custom
Skill
(Product
Type), By
Custom
Skill
Completion
Status,
By Skills
Config
Skill Automated Generative Count of By Daily 0
engagement AI Usage custom Custom
trend by Log[sys_gens_kailil_ usage_lSokgi]ll
features executions (Workflow
grouped Type), By
by Custom
features Skill
(Feature
Type), By
Custom
Skill

<!-- page 103 -->
Indicator
Indicator Available
Visualization source Calculation Frequency Unit Precision
type breakdowns
table
(Product
Type), By
Custom
Skill
Completion
Status,
By Skills
Config
Daily Automated Generative Count of By Skills Daily 0
unique AI Usage unique Config
users Log[sys_genu_saei_rsu swahgoe _log]
engaging executed
with the custom
skill skills
Executed Formula Generative (Count of By Skills Daily % 2
successfully AI Usage custom Config
Log[sys_gens_kailil_ usage_log]
executions
with
status
Completed/
Count of
custom
skill
executions)x100
Skills Automated Generative Count By Daily 0
feedback AI Usage Feedback,
Log[sys_gen_ai_usage_lBoyg ]Skills
Config
Now Assist Guardian offensive content guardrail indicator details
Indicator
Indicator Available
Visualization source Calculation Frequency Unit Precision
type breakdowns
table
Guardrail- Automated Generative Average By Skills Daily Milliseconds0
added AI time taken Config
latency Metric[sys_gbeyn tehrea tive_ai_metric]
guardrail
to
evaluate
offensive
content
Percentage Formula Generative (Count of By Skills Daily % 0
flagged as AI offensive Config
offensive Metric[sys_gceonneteranttiv e_ai_metric]
occurrences/
Total
number

<!-- page 104 -->
Indicator
Indicator Available
Visualization source Calculation Frequency Unit Precision
type breakdowns
table
of LLM
calls for
which the
guardrail
was
enabled)x100
Total Automated Generative Count of By Gen Daily 0
offensive AI offensive AI metric
content Metric[sys_gceonneteranttiv e_avi_amlueet,r ic]
occurrences occurrencesBy Skills
Config
Categories Automated Generative Count of By Daily 0
of AI offensive Offensiveness
offensive Metric[sys_gceonneteranttiv e_aTi_ympee,t ric]
content occurrencesB y Skills
grouped Config
by
categories
Offensive Automated Generative Count of By Gen Daily 0
content AI offensive AI metric
occurrences Metric[sys_gceonneteranttiv e_avi_amlueet,r ic]
by skill occurrencesB y Skills
grouped Config
by skill
Now Assist Guardian prompt injection guardrail indicator details
Indicator
Indicator Available
Visualization source Calculation Frequency Unit Precision
type breakdowns
table
Guardrail- Automated Generative Average By Skills Daily Milliseconds0
added AI time taken Config
latency Metric[sys_gbeyn tehrea tive_ai_metric]
guardrail
to
evaluate
prompt
injection
Percentage Formula Generative (Count of By Skills Daily % 0
flagged AI prompt Config
as prompt Metric[sys_ginejneecrtaiotinv e_ai_metric]
injection occurrences/
Total
number
of LLM
calls for
which the
guardrail

<!-- page 105 -->
Indicator
Indicator Available
Visualization source Calculation Frequency Unit Precision
type breakdowns
table
was
enabled)x100
Total Automated Generative Count of By Gen Daily 0
prompt AI prompt AI metric
injection Metric[sys_ginejneecrtaiotinv e_avi_amlueet,r ic]
occurrences occurrencesBy Skills
Config
Prompt Automated Generative Count of By Gen Daily 0
injection AI prompt AI metric
occurrences Metric[sys_ginejneecrtaiotinv e_avi_amlueet,r ic]
by skill occurrencesB y Skills
grouped Config
by skill
User search analyzer indicator details
Indicator
Indicator Available
Visualization source Calculation Frequency Unit Precision
type breakdowns
table
Queries Automated Search Count of AIS Daily 0
with Event[sys_sesaeracrhc_he vent]Search
Genius queries Application
Results where
Genius
Result
Displayed
= true
Genius Automated Genius Count of AIS Daily 0
Result Result genius Search
engagement Event results Application
Action[sys_swehaercrhe _genius_result_event_action]
Card Type
= Now
Assist
Multi-
Content
Response
and
Action
Type =
Show Full
Answer
or Action
Type =
Ask a
Follow Up
or Action
Type =
uxf_client_action

<!-- page 106 -->
Indicator
Indicator Available
Visualization source Calculation Frequency Unit Precision
type breakdowns
table
Genius Automated Search Average AIS Daily Seconds 0
Result Signal (Genius Search
response Event[sys_seRaerscuhl_t signalA_pevpelincta]tion
time Response
Time in
Seconds)
Genius Automated Genius Count of AIS Daily 0
Result Result queries Search
to chat Event where Application
handoff Action[sys_sCeaarrdch T_ygpeen ius_result_event_action]
= Now
Assist
Multi-
Content
Response
and
Action
Type =
Ask a
Follow Up
Genius Automated Genius Count of AIS Daily 0
Results Result queries Search
citation Event where Application
engagement Action[sys_sCeaarrdch T_ygpeen ius_result_event_action]
= Now
Assist
Multi-
Content
Response
and
Action
Type =
uxf_client_action
Feedback Automated Genius Count of AIS Daily 0
(Thumbs Result queries Search
up) Event where Application
Action[sys_sCeaarrdch T_ygpeen ius_result_event_action]
= Now
Assist
Multi-
Content
Response
and
Action
Type =
Feedback
and
Action
Value =
Helpful

<!-- page 107 -->
Indicator
Indicator Available
Visualization source Calculation Frequency Unit Precision
type breakdowns
table
Feedback Automated Genius Count of AIS Daily 0
(Thumbs Result queries Search
down) Event where Application
Action[sys_sCeaarrdch T_ygpeen ius_result_event_action]
= Now
Assist
Multi-
Content
Response
and
Action
Type =
Feedback
and
Action
Value
= Not
Helpful
Genius Automated Search Count of AIS Daily 0
Results Signal queries Search
with KB Genius where Application
Result Source
Triggered Table =
Event[sys_sekabr_ckhn_oswiglnedalg_egenius_result_triggered_event]
Genius Automated Search Count of AIS Daily 0
Results Signal queries Search
with Genius where Application
Catalog Result Source
Item Triggered Table =
Event[sys_sesacr_ccha_t_siitgenmal_genius_result_triggered_event]
Top 10 Automated Search Top 10 Not Daily Not Not
queries Signal queries Applicable Applicable Applicable
with KB Genius with count
Genius Result of genius
Result Triggered results
Event where
[sys_search_Ssoigunrcael_ genius_result_triggered_event]
Table =
kb_knowledge
Top 10 Automated Search Top 10 Not Daily Not Not
queries Signal queries Applicable Applicable Applicable
with Genius with count
Catalog Result of genius
Item Triggered results
Genius Event where
Result [sys_search_Ssoigunrcael_ genius_result_triggered_event]
Table =
sc_cat_item

<!-- page 108 -->
Now Assist context menu analytics indicator details
Indicator
Indicator Available
Visualization source Calculation Frequency Unit Precision
type breakdowns
table
Usage Automated Generative Count of By NAcm Daily 0
in this AI actions implicit
period Log[sys_genwehraetrieve _ai_lofege]dback,
Source By Skills
is Now Config, By
Assist Feedback,
context By Status,
menu By Skill
Capability
AcceptanceA utomated Generative Count of By NAcm Daily 0
distribution AI actions implicit
Log[sys_genwehraetrieve _ai_lofege]dback,
content By Skills
generated Config, By
by Now Feedback,
Assist By Status,
context By Skill
menu Capability
grouped
by
Accepted
or Not
Accepted
Usage Automated Generative Count of By NAcm Daily 0
trend by AI context implicit
skill Log[sys_genmereantiuv e_ai_lofege]dback,
actions By Skills
grouped Config, By
by Now Feedback,
Assist By Status,
skills By Skill
Capability
Capability Automated Generative Count of By NAcm Daily 0
distribution AI context implicit
Log[sys_genmereantiuv e_ai_lofege]dback,
actions By Skills
grouped Config, By
by Feedback,
capability By Status,
By Skill
Capability
Responses Automated Generative Count of By NAcm Daily 0
by AI actions implicit
feedback Log[sys_genwehraetrieve _ai_lofege]dback,
feedback By Skills
for the Config, By
content Feedback,
generated By Status,

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

> **[Screenshot: Now Assist Admin Overview Page]**
> Full-width ServiceNow Next Experience screenshot of the Now Assist Admin console Overview page. Top navigation bar shows: "servicenow" logo, All, Favorites, History, Workspaces, Admin menus, a centred "Now Assist Admin ★" badge, search bar, and icon toolbar. Below the nav, a secondary tab bar shows: Overview (active), Now Assist Skills, Now Assist Experiences, Performance, Settings.
>
> Main content area is split into two columns. Left/centre column shows a "Now Assist Summary" card with two sub-panels: "Plugin status" (donut chart showing 4 installed in teal vs 27 not installed in orange, with a "Review now" link) and "Skills status" (donut chart with 139 total skills broken down: Not started 64, Draft 9, Inactive 3, Active 63). Below these panels is a "Skill usage" card with date filter "All skills / Date range" and two KPI tiles: "Number of actions: 0" and "Avg number of unique users per day who triggered action: 0".
>
> Right sidebar shows a red "Needs Attention" banner with the count "109" in large text, followed by four expandable items: "Plugins not installed (27)", "Skills inactive (3)", "Skills in draft state (10)", "Skills not started (69)". Below this is a "Now Assist Journey Checklist" card with a teal "View checklist" button.

> **[Screenshot: Available for you tab on the Now Assist Admin Settings > Plugins page]**
> Screenshot of the Plugins settings page. Breadcrumb reads "Settings > Plugins". Page title is "Plugins" with subtitle "List of all Now Assist AI plugins available per product." Two tabs shown: "Available for you" (selected) and "Installed". A workflow dropdown filter on the right reads "Workflow: All". Below, "All available plugins (11)" header appears.
>
> Three plugin cards visible in a 3-column grid: 1) "Now Assist for Security Operations (SecOps)" – with a colourful circular icon, description "GenAI related features for Security Operations that are powered by Now Assist", and a "Get plugins" button. 2) "Now Assist for HR Service Delivery (HRSD)" – similar layout, "GenAI related features for HR Service Delivery that are powered by Now Assist", "Get plugins" button. 3) "Now Assist for Creator" – book/document icon, "Helping creators build with the power of Generative AI", "Get plugins" button. A partial fourth row of cards is visible at bottom.

> **[Screenshot: Now Assist Experiences page with Now Assist panel]**
> Two-part screenshot. Upper portion shows the Now Assist Experiences page in the Admin console. Left sidebar lists items: "Now Assist panel" and "Now Assist context menu". Main area shows a card titled "Now Assist panel – Included in license" with product touchpoint metadata and a summary paragraph. A "Manage" sidebar on the right shows "Now Assist panel is turned on for your users" with a green "Turn off" button. A "Settings" section shows "Voice Input OFF" with a toggle.
>
> Lower portion shows the Now Assist Skills page for Technology workflow. Left nav shows a tree of workflows: Technology (expanded showing Risk & Sustainability, ITSM, CMDB, Security Operations, SAM, ITOM, CWM, SPM, OTSM, EA), Customer, Employee, Creator, App Engine, Platform. Main area titled "Now Assist skills for ITSM" shows a table with columns: Name, Status, Skill type, LLM Provider, Displayed On, Last updated, Action. Rows include: Incident sentiment analysis (Draft, Out-of-box, Now LLM Service, Jul 18 2025, Activate button), Email recommendation (Draft, Out-of-box, Nov 11 2024), Incident assist (Not started, Out-of-box), Change request risk explanation (Not started, Now LLM Service, Sep 4 2024), KB generation (Draft, Out-of-box, May 15 2025), Incident summarization (Active green badge, Out-of-box, In-product Now Assist panel, Oct 28 2025, Deactivate), Role Masking (Draft, Custom, Now LLM Service, Oct 7 2025, Activate), Clone of Incident summarization (Not started, Out-of-box, Sep 16 2025, Turn on).

> **[Screenshot: Chat summarization activation wizard in Now Assist Admin]**
> Guided activation wizard for the "Chat summarization" skill (labelled "CSM" in a small badge). An "Exit" button is in the top-right. Left sidebar shows four steps in a vertical stepper: 1) Define trigger (filled circle – complete), 2) Choose Input (filled), 3) Select display (filled), 4) Review and activate (filled). Main content area for step 1 "Define trigger" shows the prompt "Choose when and how the skill will be triggered" with an "Explain this" link. Four toggle rows, all currently OFF: "Virtual Agent to Live Agent handoff" (summary created when conversation moves from virtual to live agent), "Live Agent to Live Agent handoff" (conversation moves from live to live agent), "Quick action" (agents can use summarize quick action), "Chat wrap-up" (chat summary field auto-populates after conversation ends). Bottom-right has "Back" and a teal "Save and continue" button.
>
> **[Screenshot: Now Assist Admin console account settings]**
> Settings > Account page in the Now Assist Admin console. Left sidebar shows navigation items: Plugins, Multilingual service, Data sharing and process…, Now Assist Guardian, Manage AI models, Manage Integration, Account (selected/highlighted). Main area shows "Account" heading with subtitle "View your account license information and manage data sharing." An "Account details" card shows "Version 12.0.3-6" and "Your license includes:" with an "All included in license" badge. Two bullet items with green check icons: "Now Assist panel – Empower users with a personal generative AI assistant..." and "Now Assist skills – Unlock Now Assist skills you can configure to improve user productivity."

> **[Screenshot: Plugin and Skills status on the Now Assist Admin Overview page]**
> Close-up of the "Now Assist Summary" card. Left panel: "Plugin status" donut chart showing 2 installed (small teal slice) vs 11 not installed (large orange slice) with a "Review now" link below. Right panel: "Skills status" donut chart showing 128 total skills. Legend below the chart: Not started 96 (dark blue), Draft 2 (medium blue), Inactive 3 (light grey), Active 27 (teal).
>
> **[Screenshot: Now Assist checklist modal]**
> A modal overlay titled "Now Assist checklist" with an X close button. Subtitle reads "The following steps make up your Now Assist journey and will allow you to get the most out of generative AI skills." Five numbered circle steps: 1) Install Now Assist plugins – "Visit the store to install the plugin specific to the product workflows. Browse all available plugins." 2) Turn on Now Assist panel – "After a plugin is installed, return to this console to turn on the Now Assist panel…" 3) Activate Now Assist skills – "Once the panel is turned on, configure and customise information sources..." 4) Review account settings – "Review account information and manage data sharing." 5) Analyze Now Assist skills – "Track and monitor the progress of your Now Assist skills." A teal "Done" button is at the bottom-right.

> **[Screenshot: Now Assist panel icon in the Next Experience navigation bar]**
> Close-up of the ServiceNow Next Experience top navigation bar, highlighting the Now Assist icon (a star/spark shape labelled "+*") with a blue square showing the number "2" indicating 2 missed messages.
>
> **[Screenshot: Now Assist panel open and expanded]**
> The Now Assist panel displayed as a narrow sidebar overlay on the right side of the screen. Panel header shows "Now Assist" title, three icons (settings/options, pin, X close). Below the header: a hamburger menu icon (1) on the left; two numbered buttons (2) for something and (3) for chats. Chat area shows a greeting: "Hi! How can I help you with your work today?" and a second message: "To give you an idea of what I do really well, try asking me to:" followed by four bullet points: Generate resolution notes, Get Help, Summarize a record, Summarize conversation. Four quick-action option boxes arranged 2×2 (4): Generate resolution notes, Summarize a record, Summarize conversation, Get Help. A copy icon (5) is shown. At the bottom, a text input field (6) labelled "Reply to Now Assist..." with a send arrow, and a disclaimer (7): "Some answers generated by AI. Be sure to check for accuracy."

> **[Screenshot: Now Assist panel – Chats section]**
> The Now Assist panel showing the Chats history view. Header "≡ Chats" with a + icon. Three sections: "Active ⊙ (8)" showing "Summarize conversation" button; "Updates ⊙ (9)" showing "You're all caught up"; "Closed ⊙ (10)" showing "No chatter from the moment."

> **[Screenshot: Now Assist panel displayed in both Next Experience workspace and Core UI]**
> Side-by-side comparison labelled "Next Experience" (left) and "Core UI" (right). Both show the ServiceNow platform interface with an active incident record open and the Now Assist panel visible as a right sidebar. The Now Assist panel in both views shows a chat conversation with AI-generated suggestions including: summarize the record, generate resolution notes, summarise conversation. The workspace view (left) shows a full incident workspace with related tabs (Details, Test SLAs, Affected CIs, Impacted Services CIs, Child Incidents, Interactions CSM, Record History). The Core UI (right) shows a classic incident form with fields for Number, Company, Location, Status, Category, Subcategory, Configuration Item, Impact, Urgency, Priority, Assignment Group, Assignee, and a Description field.

> **[Screenshot: Now Assist panel showing case/incident summarization result]**
> The Now Assist panel displaying an AI-generated summary of a case or incident. The summary appears as a formatted response in the chat area listing key details from the record. A copy button is visible below the summary text.

> **[Screenshot: Now Assist Get Help experience]**
> The Now Assist panel showing a "Get Help" interaction. A user has typed a help request and Now Assist has returned a response with relevant documentation links and a step-by-step answer. The response includes clickable blue hyperlinks to knowledge articles.

> **[Screenshot: Now Assist Admin console plugin installation page]**
> The "Install product plugins" page showing three workflow category cards in a horizontal row: Technology (stylised people/chart icon, "Use Now Assist to elevate day-to-day operations and increase employee agility", "Browse plugins" button), Customer (stylised person icon, "Use Now Assist to improve customer experiences and deepen brand loyalty", "Browse plugins" button), Employee (stylised person icon, "Use Now Assist to boost employee engagement and strengthen morale", "Browse plugins" button). Background is white.
>
> **[Screenshot: Now Assist Analytics Configuration table]**
> ServiceNow list view of the "Now Assist Analytics Configurations [sn_na_analytics_configuration]" table. Table columns: Active, Dashboard, Document Id, Document Table, Order, Domain. Two visible rows: Row 1 – Active: true, Dashboard: Flow Generation, Document Id: Generative AI Feature Mapping: Flow Generation, Document Table: Generative AI Feature Mapping [sys_gen_ai_feature_mapping], Order: 100, Domain: global. Row 2 – Active: true, Dashboard: Case summarization, Document Id: Generative AI Feature Mapping: Case summarization, same Document Table, Order: 100, Domain: global.

> **[Screenshot: Usage and adoption dashboard page in Now Assist Analytics]**
> Full-width screenshot of the Now Assist Analytics "Usage and Adoption" dashboard. Left sidebar navigation shows: Usage and Adoption (selected, expanded showing Usage Summary and Adoption sub-items), Self-Service Performance, Skill Performance, Now Assist Guardian, User Search Analyser, Now Assist Context Menu, Value Insights. Main area shows "Usage Summary" and "Adoption" tabs (Usage Summary active). Filter bar: Date "2025-02-0…", Channels "Select", Products "Select".
>
> Four KPI/chart widgets in a 2×2 grid: Top-left: "Total Now Assist actions" showing "3232" in large bold text with upward trend indicator "↑ 3228 (90700.0%) since previous period Jan 7 – Jan 31", line chart below showing spike around Feb 10–13, label "Sum for Feb 1 – Feb 25". Top-right: "Daily Now Assist actions" line chart with y-axis up to 4000 counts, x-axis labels Feb 1 through Feb 25, single large spike visible around Feb 10. Bottom-left: "Average daily unique users engaging with Now Assist" showing "828" in large bold text, "↑ 28 (23033.3%) since previous period", line chart with matching spike pattern, label "Avg for Feb 1 – Feb 25". Bottom-right: "Daily unique users engaging with Now Assist" line chart, same time axis, spike visible.

> **[Screenshot: Multi-language support – Microsoft Azure OEM Translator Configuration form]**
> ServiceNow form record for a Translator Configuration named "Microsoft Azure OEM". Form fields: Name: "Microsoft Azure OEM", Version: "v4", Active: checked. Two tabs: "Preferences" (active) and "Language Code Mappings". Under Preferences: "Choose a translate subflow" with "Translate Text" selected and a search icon; "Mark as default for translation" checkbox (unchecked). "Choose a detect subflow" with "Detect Language V4" and a search icon; "Mark as default for detection" checkbox (unchecked). Bottom buttons: Update, Delete.