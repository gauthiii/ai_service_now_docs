# Now Assist Experiences

_Source pages: 14–55 | Depth: 2_

---

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