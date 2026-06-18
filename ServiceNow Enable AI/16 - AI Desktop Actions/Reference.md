# Reference

## SOURCE INFORMATION

* SECTION NAME: AI Desktop Actions
* SUBSECTION NAME: Reference
* SOURCE FILE NAME: AI Desktop Actions.pdf
* PAGE RANGE: 1375-1383 (page 1383 split before next major TOC section Predictive Intelligence)
* EXTRACTION DATE: 2026-06-17

---

# CONTENT

> Source page: 1375

### AI Desktop Actions reference

Reference topics provide additional information about the roles and tables that are installed with
the AI Desktop Actions application.

#### Components installed with AI Desktop Actions

Several types of components are installed with activation of the sn_desktop_agents plugin,
including user roles and tables.

> Source page: 1376

#### Roles used

Role title [name]
Description
Contains roles
AI Agent Admin
Enables you to create,
• agent_role_config_admin
manage, and test
[sn_aia.admin]
• sn_skill_builder.admin
desktop actions in AI
Desktop Actions and
• connection_admin
deploy them as tools in
• flow_designer
AI Agent Studio.
• sn_aia.viewer
• sn_mcp_client.admin
• sn_ace.ace_user
Now Assist panel user
Enables you to trigger
sn_nowassist_admin.user
desktop actions from
[now_assist_panel_user]
Now Assist panel
and execute desktop
actions in the desktop
environment using
Execution workspace.
Desktop action user
Enables you to create
• sn_aia.admin
desktop actions using
[sn_desktop_core.desktop_action_user]
• sn_nowassist_admin.user
the Record with AI
feature in AI Desktop
Actions.

#### Tables installed

Table
Description
Desktop action
Stores details, such as input and output
parameters and number of screens for on-screen
[sn_desktop_core_action]
desktop actions.
Desktop action application
Stores the desktop application associated with
the desktop action.
[sn_desktop_core_action_application]
Desktop action execution
Stores the execution details of a desktop action,
such as request, response, tool execution, and
[sn_desktop_core_action_execution]
execution plan.
Desktop action parameter
Stores the desktop action parameter records as
parent records.
[sn_desktop_core_action_parameter]
Desktop action parameter value
Stores the desktop action parameter value
records as child records.
[sn_desktop_core_action_parameter_value]

> Source page: 1377

#### Plugins installed

Plugin
Description
AI Desktop Actions
Contains configuration of desktop action tool
used by AI Agent Studio to discover available
[com.sn_desktop_agents]
desktop actions while creating AI agents and
invoke desktop actions via AI agents during
execution.
AI Desktop Actions Core
Packages tables, custom functionality specific
to AI Desktop Actions application, and AI
[com.sn_desktop_core]
Desktop Actions download interface within a
scoped application.
Now Assist AI web agents
Contains system property, default AI agent
and agentic workflow named Web Automation
[sn_naa]
Agent and Web Automation respectively, and
functionality to perform adaptive automation
on web.

#### System properties installed

Property
Description
Makes Record with AI the default recording
sn_desktop_core.record_with_ai
option. Turn off this property to set the manual
recorder as the default recording option.
• Type: true | false
• Default: true
sn_desktop_core.max_action_events
Modifies the limit of maximum number of
events processed during a single Desktop
action execution in AI Desktop Actions.
• Type: Integer
• Default: 200
sn_naa.allowed_websites
Stores a list of websites that AI agents
configured with adaptive desktop actions are
permitted to open and perform tasks.
Type: String
sn_naa.keep_tab_open
Keeps the browser tabs that open during goal
execution open after the goal completes.
If you update the value, select the
ServiceNow Web Automation extension
icon, and select Save on the confirmation
message.

> Source page: 1378

Property
Description
• Type: true | false
• Default: true

#### System requirements and limitations in AI Desktop Actions

Be aware of system requirements and a few limitations when you’re using the AI Desktop Actions
application for defined desktop actions.

#### Note: These system requirements and limitations apply to only defined desktop actions

that are created in the AI Desktop Actions Windows application.

#### Hardware requirements

Hardware requirements for AI Desktop Actions
Resource
Minimum
Recommended
CPU
Intel Processor (Core i5)
Intel Processor (Core i7)
RAM
4-GB RAM
8-GB RAM
Disk space
Minimum 20-GB free disk
Minimum 50-GB free disk
space after installing the OS,
space after installing the OS,
patches, and base software
patches, and base software

#### Software requirements

• Windows 11 operating system is used.
• A .NET 9.0 runtime v9.0.10 and .NET 9 Desktop Runtime v9.0.10 is installed.
• No extended monitors are connected.
• Add the end users who interact with the Execution workspace of AI Desktop Actions to the
Remote Desktop Users group on the target machine and provide Remote Desktop access
permissions for seamless automation execution.
If your organization uses Group Policy, add the end users to a Microsoft Active Directory group
that is permitted to use Remote Desktop through Group Policy on each target machine where
desktop actions run.
  ◦Local changes to the Remote Desktop Users group are temporary unless they align with
Microsoft Active Directory entitlements.
  ◦If the user is not entitled, Group Policy refresh automatically removes them from the group.
• Theme must match between the systems used for recording and execution.
• Confirm that your firewall allows bidirectional traffic between the AI Desktop Actions
application and your ServiceNow instance on the port 80 for HTTP and port 443 for HTTPs.
If your organization uses non-standard ports for HTTP or HTTPS, confirm the correct ports with
your IT administrator before proceeding.

> Source page: 1379

You must have full permissions to create and use system I/O communication pipes.
• If applicable, confirm that the snada:// custom URI protocol is registered to launch the AI
Desktop Actions application in the browser.

#### Note: Screen resolution and scaling must be the same between the systems used for

recording and execution of desktop actions that are created before AI Desktop Actions
v1.0.1.

#### Limitations

Limitations with AI Desktop Actions
Limit
Description
RPA Attended robot and AI Desktop Actions
To avoid conflicts, do not run the AI Desktop
parallel execution
Actions Execution workspace and RPA
Attended Desktop mode at the same time.
Pause for human input
If your automation requires manual inputs,
such as entering an OTP or CAPTCHA, you
must provide instructions to the AI Agent
to wait for user input during execution.
Otherwise, the automation can't proceed.
Single execution
The system supports one automation
execution at a time within the Execution
workspace.
Screen elements
During recording, auto-assignment accuracy
of screen elements depends heavily on the
target application’s technology and interface
characteristics. Applications with strong
accessibility support, such as well-defined
UI elements and controls, stable rendering
performance, and simple, consistent layouts
enable anchors to be detected more reliably.
In contrast, UI complexity, such as dynamic
elements, frequent layout shifts, animations,
or poor accessibility metadata can reduce
accuracy and may require manual anchor
configuration or additional tuning.
The Get Table step doesn’t convert ordinary
Getting table information
text to table data. For the step to capture table
data successfully, the data must already be in
the table form.
Browsers parallel execution
The Chrome or Edge browser must not be
used in parallel in the main session and the
desktop session on your system. You must
close the session in the main session to
execute automations that use the Chrome or
Edge browser in the Execution workspace.

> Source page: 1380

Limitations with AI Desktop Actions (continued)
Limit
Description
Sensitive information
The sensitive information isn’t masked during
recording. Confirm that you don’t record any
sensitive information.

#### AI Desktop Actions glossary

Learn about the terms and concepts that are unique to AI Desktop Actions.
A
Glossary terms are grouped alphabetically.
Action recorder
Recording feature in the Design workspace that auto-captures user interactions with
desktop applications to create automated workflows. The recorder captures clicks,
keystrokes, data entry, and visual and contextual information as screens and steps.
Adaptive path desktop action
A type of desktop action in which the AI agent dynamically determines the steps required
to complete a task based on a high-level goal you provide in the tool configuration.
Unlike defined path desktop actions, adaptive path desktop actions do not follow a fixed
sequence of steps. Instead, the AI agent checks the current state of the web page and
adjusts its approach at runtime. Because steps are determined dynamically, results may
vary between runs of the same task.
Example: Reviewing an open incident and routing it based on its current priority level,
where the next steps depend on the value the AI agent finds on the page.
AI agent
Set of large language model (LLM) instructions and tools in AI Agent Studio that can
process natural language inputs, generate execution plans, and run desktop actions
autonomously or semi-autonomously.
AI Agent Studio
ServiceNow platform interface for creating, managing, testing, and activating AI agents.
Desktop actions are published to AI Agent Studio as tools that AI agents can use during
execution.
Anchor
Reference point on a captured screen that helps the automation identify and interact
with nearby UI elements. During execution, the system uses computer vision to locate the
anchor and then identifies UI elements at a relative distance from it. Anchors improve the
stability and accuracy of steps when the target element location may shift or when the UI
layout varies across sessions.
Auto-capture
Method of creating desktop actions by recording user interactions with desktop
applications using the Action recorder. The recorder captures clicks, keystrokes, and data
entry along with visual and contextual information.
B
Glossary terms are grouped alphabetically.

> Source page: 1381

Background task
Type of desktop action that uses prebuilt connectors to interact with applications and
system components in the background without UI interaction. Supported applications
include Microsoft Excel, Microsoft Outlook, Microsoft Word, PDF, PowerShell, SQL, SSH,
and System Actions. Background task desktop actions can't be created by users.
C
Glossary terms are grouped alphabetically.
Confidence threshold
Accuracy level required for matching a captured image before the system performs a step.
A value of 1 defines a 100% match while 0.5 defines a 50% match. The default value is 0.95
(95% match).
D
Glossary terms are grouped alphabetically.
Defined path desktop action
Reusable automation that defines how AI agents interact with desktop and web
applications. Desktop actions consist of screens, anchors, and steps. There are two types:
On-screen task and Background task. For this desktop action, you design a fixed sequence
of steps in the AI Desktop Actions Windows application. The AI agent executes these steps
in the order you specified, without deviation. Defined path desktop actions support both
desktop applications and web-based applications, and do not require Google Chrome or a
browser extension.
Use defined path desktop actions for tasks that follow the same sequence every time and
involve predictable UI interactions. Contrast with adaptive path desktop actions.
Example: Automatically entering shipping data into a shipping management application
using a fixed form structure that does not change between executions.
Design workspace
Interactive no-code environment within Agentic Desktop for creating, configuring,
managing, and testing desktop actions. The workspace provides a visual canvas where you
can design multi-screen automation workflows that capture business processes across
different applications. Accessible to users with the AI Agent Admin (sn_aia.admin) role.
Desktop action application
Record that stores the association between a desktop action and the
desktop application it interacts with. Stored in the Desktop action application
[sn_desktop_core_action_application] table.
Desktop-in-Desktop (DiD) mode
Virtual environment within the Execution workspace where automations run in isolation
from the main desktop session. You can monitor the execution of desktop actions and how
they interact with desktop applications while continuing to work on other tasks.
Desktop session
Isolated Windows session within the Execution workspace where desktop actions run.
The desktop session launches automatically when you test a desktop action or trigger an
automation from the Now Assist panel.

> Source page: 1382

E
Glossary terms are grouped alphabetically.
Execution status
Current state of an automation in the Execution workspace. Statuses include Ready,
Initiated, Running, Success, Failed, and Canceled.
Execution workspace
Isolated desktop session where desktop actions run during testing or AI agent execution.
This workspace launches automatically when you test a desktop action from the Design
workspace or trigger an automation from the Now Assist panel. You do not open the
Execution workspace directly.
M
Glossary terms are grouped alphabetically.
Manual capture
Method of creating desktop actions by taking screen captures, inserting anchors, and
defining steps individually rather than recording interactions automatically.
N
Glossary terms are grouped alphabetically.
Now Assist panel
ServiceNow interface from which users trigger AI agent automations. When you provide
instructions through the Now Assist panel, the AI agent selects and runs the appropriate
desktop actions in the Execution workspace. Accessible to users with the Now Assist panel
user (now_assist_panel_user) role.
O
Glossary terms are grouped alphabetically.
On-screen task
Type of desktop action that simulates human interactions with UI elements on thick client
applications, legacy systems, or SaaS applications without APIs. Interactions include
clicking buttons, entering text, and selecting from menus. On-screen desktop actions are
created and managed in the Design workspace.
P
Glossary terms are grouped alphabetically.
Parameter record
Record created by an AI Agent Admin that stores a reference name for credentials such
as usernames or passwords. AI agents access these records during desktop action
execution to retrieve sensitive values securely. Currently supported only for SSH connector,
background task desktop actions.
Parameter Value record
Child record under a Parameter record that stores the actual credential value, such as
a username or password, for a specific user. Only one Parameter Value record can be
created per user for each Parameter record.

> Source page: 1383

S
Glossary terms are grouped alphabetically.
Screen
Captured image of an application window within a desktop action. Screens represent
the application states that the automation moves through during execution. Each screen
contains one or more anchors and associated steps.
Smart sizing
Display feature in the Execution workspace that automatically adapts the desktop session
to the display. Includes two options:
• Fit to window: Scales the session to fit within the Execution workspace.
• Original resolution: Displays the session at its native resolution with scroll bars if
necessary.
Step
Individual interaction within a desktop action, such as clicking a button, entering text, or
extracting data. Steps are positioned relative to an anchor.
• Input step types include Set Text, Click, Mouse Click, and Send Keys.
• Output step types include Get Text, Get Table, and OCR Read Text.
Step in / Step out
Manual control options in the Execution workspace. Step in transfers control to the user for
manual input such as entering an OTP or CAPTCHA. Step out returns control to the AI agent
to continue the automation.
T
Glossary terms are grouped alphabetically.
Tool
Desktop action that has been activated and added to an AI agent in AI Agent Studio. Tools
provide AI agents with the capabilities to complete specific tasks during execution. An AI
agent selects a tool based on its name and description.

## Boundary content appearing after the AI Desktop Actions section boundary

The following content begins the next major TOC section on source page 1383. It is captured for page completeness and is not treated as AI Desktop Actions content.

> Source page: 1383

## Predictive Intelligence

Predictive Intelligence is a powerful interface to train machine learning models. With Predictive
Intelligence, you can improve performance, efficiency, and flexibility to your systems across
multiple business units.

#### Get started with Predictive Intelligence

Administrators can harness the power of machine learning to improve productivity and efficiency
for their agents and fulfillers. Predictive Intelligence uses artificial intelligence to improve
processes across the platform. Predictive Intelligence enables you to do things such as the
following:
• Automatically populate fields during case creation.
• Categorize and route work based on how records have been handled in the past.
• Recommend resolutions to cases that are similar to previous ones.
• Identify major outages based on incoming incidents.


---

## IMAGE DESCRIPTIONS

### Repeated ServiceNow page header/logo

The ServiceNow-branded wordmark appears in the upper-left corner of reviewed source pages for this subsection. It is a recurring branding image, not a technical diagram. It contains the visible brand text `servicenow`, with green accenting in the `now` portion. Reviewed pages: 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383.

### Small UI icons and inline pictograms

No small non-logo icon/pictogram image blocks were detected within this subsection boundary.

No large embedded screenshot or diagram image blocks were detected within this subsection boundary.


---

## TABLES

### Source page 1376 — Table 1

**Nearby source context:** Roles used

| Role title [name] | Description | Contains roles |
| --- | --- | --- |
| AI Agent Admin<br>[sn_aia.admin] | Enables you to create,<br>manage, and test<br>desktop actions in AI<br>Desktop Actions and<br>deploy them as tools in<br>AI Agent Studio. | •agent_role_config_admin<br>•sn_skill_builder.admin<br>•connection_admin<br>•flow_designer<br>•sn_aia.viewer<br>•sn_mcp_client.admin<br>•sn_ace.ace_user |
| Now Assist panel user<br>[now_assist_panel_user] | Enables you to trigger<br>desktop actions from<br>Now Assist panel<br>and execute desktop<br>actions in the desktop<br>environment using<br>Execution workspace. | sn_nowassist_admin.user |
| Desktop action user<br>[sn_desktop_core.desktop_action_user] | Enables you to create<br>desktop actions using<br>the Record with AI<br>feature in AI Desktop<br>Actions. | •sn_aia.admin<br>•sn_nowassist_admin.user |

### Source page 1376 — Table 2

**Nearby source context:** the Record with AI / Tables installed

| Table | Description |
| --- | --- |
| Desktop action<br>[sn_desktop_core_action] | Stores details, such as input and output<br>parameters and number of screens for on-screen<br>desktop actions. |
| Desktop action application<br>[sn_desktop_core_action_application] | Stores the desktop application associated with<br>the desktop action. |
| Desktop action execution<br>[sn_desktop_core_action_execution] | Stores the execution details of a desktop action,<br>such as request, response, tool execution, and<br>execution plan. |
| Desktop action parameter<br>[sn_desktop_core_action_parameter] | Stores the desktop action parameter records as<br>parent records. |
| Desktop action parameter value<br>[sn_desktop_core_action_parameter_value] | Stores the desktop action parameter value<br>records as child records. |

### Source page 1377 — Table 3

**Nearby source context:** Plugins installed

| Plugin | Description |
| --- | --- |
| AI Desktop Actions<br>[com.sn_desktop_agents] | Contains configuration of desktop action tool<br>used by AI Agent Studio to discover available<br>desktop actions while creating AI agents and<br>invoke desktop actions via AI agents during<br>execution. |
| AI Desktop Actions Core<br>[com.sn_desktop_core] | Packages tables, custom functionality specific<br>to AI Desktop Actions application, and AI<br>Desktop Actions download interface within a<br>scoped application. |
| Now Assist AI web agents<br>[sn_naa] | Contains system property, default AI agent<br>and agentic workflow named Web Automation<br>Agent and Web Automation respectively, and<br>functionality to perform adaptive automation<br>on web. |

### Source page 1377 — Table 4

**Nearby source context:** Description / System properties installed

| Property | Description |
| --- | --- |
| sn_desktop_core.record_with_ai | Makes Record with AI the default recording<br>option. Turn off this property to set the manual<br>recorder as the default recording option.<br>•Type: true \| false<br>•Default: true |
| sn_desktop_core.max_action_events | Modifies the limit of maximum number of<br>events processed during a single Desktop<br>action execution in AI Desktop Actions.<br>•Type: Integer<br>•Default: 200 |
| sn_naa.allowed_websites | Stores a list of websites that AI agents<br>configured with adaptive desktop actions are<br>permitted to open and perform tasks.<br>Type: String |

### Source page 1378 — Table 5

| Property | Description |
| --- | --- |
|  | •Type: true \| false<br>•Default: true |

### Source page 1378 — Table 6

**Nearby source context:** Hardware requirements / Hardware requirements for AI Desktop Actions

| Resource | Minimum | Recommended |
| --- | --- | --- |
| CPU | Intel Processor (Core i5) | Intel Processor (Core i7) |
| RAM | 4-GB RAM | 8-GB RAM |
| Disk space | Minimum 20-GB free disk<br>space after installing the OS,<br>patches, and base software | Minimum 50-GB free disk<br>space after installing the OS,<br>patches, and base software |

### Source page 1379 — Table 7

**Nearby source context:** Limitations / Limitations with AI Desktop Actions

| Limit | Description |
| --- | --- |
| RPA Attended robot and AI Desktop Actions<br>parallel execution | To avoid conflicts, do not run the AI Desktop<br>Actions Execution workspace and RPA<br>Attended Desktop mode at the same time. |
| Pause for human input | If your automation requires manual inputs,<br>such as entering an OTP or CAPTCHA, you<br>must provide instructions to the AI Agent<br>to wait for user input during execution.<br>Otherwise, the automation can't proceed. |
| Single execution | The system supports one automation<br>execution at a time within the Execution<br>workspace. |
| Screen elements | During recording, auto-assignment accuracy<br>of screen elements depends heavily on the<br>target application’s technology and interface<br>characteristics. Applications with strong<br>accessibility support, such as well-defined<br>UI elements and controls, stable rendering<br>performance, and simple, consistent layouts<br>enable anchors to be detected more reliably.<br>In contrast, UI complexity, such as dynamic<br>elements, frequent layout shifts, animations,<br>or poor accessibility metadata can reduce<br>accuracy and may require manual anchor<br>configuration or additional tuning. |
| Getting table information | The Get Table step doesn’t convert ordinary<br>text to table data. For the step to capture table<br>data successfully, the data must already be in<br>the table form. |
| Browsers parallel execution | The Chrome or Edge browser must not be<br>used in parallel in the main session and the<br>desktop session on your system. You must<br>close the session in the main session to<br>execute automations that use the Chrome or<br>Edge browser in the Execution workspace. |

### Source page 1380 — Table 8

**Nearby source context:** Limitations with AI Desktop Actions (continued)

| Limit | Description |
| --- | --- |
| Sensitive information | The sensitive information isn’t masked during<br>recording. Confirm that you don’t record any<br>sensitive information. |


---

## FIGURES

| Figure / visual | Source page | Asset or location | Analysis |
|---|---:|---|---|
| Markdown-converted table/grid 1 | 1376 | TABLES section | Source table/grid region converted into Markdown; nearby context: Roles used |
| Markdown-converted table/grid 2 | 1376 | TABLES section | Source table/grid region converted into Markdown; nearby context: the Record with AI / Tables installed |
| Markdown-converted table/grid 3 | 1377 | TABLES section | Source table/grid region converted into Markdown; nearby context: Plugins installed |
| Markdown-converted table/grid 4 | 1377 | TABLES section | Source table/grid region converted into Markdown; nearby context: Description / System properties installed |
| Markdown-converted table/grid 5 | 1378 | TABLES section | Source table/grid region converted into Markdown; nearby context:  |
| Markdown-converted table/grid 6 | 1378 | TABLES section | Source table/grid region converted into Markdown; nearby context: Hardware requirements / Hardware requirements for AI Desktop Actions |
| Markdown-converted table/grid 7 | 1379 | TABLES section | Source table/grid region converted into Markdown; nearby context: Limitations / Limitations with AI Desktop Actions |
| Markdown-converted table/grid 8 | 1380 | TABLES section | Source table/grid region converted into Markdown; nearby context: Limitations with AI Desktop Actions (continued) |


---

## QUALITY ASSURANCE NOTES

* PAGES REVIEWED: 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383. Source page range: 1375-1383 (page 1383 split before next major TOC section Predictive Intelligence).
* IMAGES REVIEWED: 8 image blocks assigned/reviewed: 8 recurring header logo block(s), 0 small icon/pictogram block(s), and 0 large screenshot/diagram crop(s).
* TABLES REVIEWED: 8 table/grid region(s) converted to Markdown. Table pages: 1376, 1377, 1378, 1379, 1380.
* FIGURES REVIEWED: 0 large screenshot/diagram figure(s) plus 8 table/grid visual(s).
* OCR ISSUES FOUND: No unresolved OCR issues were identified in the main text layer after cleanup.
* OCR ISSUES CORRECTED: Removed recurring footer/page-number noise from the main content stream, normalized nonbreaking spaces and soft-hyphen/control artifacts, preserved bullets/numbering/property names, converted detected tables to Markdown, and OCR-processed large non-logo embedded images.
* SECTION MAPPING NOTES: Folder name is exactly `AI Desktop Actions`. File name and subsection name are exactly `Reference` from the TOC. Shared source pages were split at heading coordinates from the PDF text layer.
* BOUNDARY NOTE: Source page 1383 contains the next major TOC section, `Predictive Intelligence`, after the final AI Desktop Actions glossary terms; next-section content is captured as boundary content only.
* PAGE FOOTERS REVIEWED: Reviewed recurring ServiceNow copyright/trademark footer and logical page numbers. Footer text reviewed: `© 2026 ServiceNow, Inc. All rights reserved. ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries. Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.`
* RECHECK PASSES COMPLETED: 12/12: page completeness, text extraction, table extraction, image extraction, diagram interpretation, section mapping, subsection mapping, file names, folder names, Markdown formatting, missed-content review, and OCR/text-layer cleanup.
* VERIFICATION ARTIFACTS: Large image crops and `image_inventory.csv` are stored in the `_assets` folder inside this section folder.
