# Define the specialty of an AI agent

_Source pages: 61–62 | Depth: 2_

---

<!-- page 61 -->
Current location Navigation option
to see the most recently added or changed
agents.
Note: You see a list of the AI agents on­
ly when there's recent activity of the AI
agents on your instance.
Navigate to All > AI Agent Studio > Create
Anywhere else and manage, and then select the AI agents
tab.
2. View all AI agents, including those AI agents that were installed with Now Assist applications
by navigating to the AI agents tab.
Result
Navigating through any of the preceding options directs you to the AI agents that are available on
your AI Agent Studio instance.
Define the specialty of an AI agent
In the guided setup for an AI agent, write a clear description defining your agent and its role. You
can also configure supported LLMs, enable third-party access, and manage long-term memory.
Before you begin
Role required: sn_aia.admin
About this task
The first step of the guided setup enables you to define the fundamentals of the AI agent. The
description, AI agent role, and list of steps fields are used by the LLM to understand how to use
the AI agent, by itself or as part of an agentic workflow. Descriptions, AI agent roles, and list
of steps should be clear and well-defined. For guidelines for writing these fields, see Writing
effectively for agentic AI. For an example AI agent, see Example AI agent.

<!-- page 62 -->
Note: If you have the Off Glide Conversation Server plugin (com.glide.cs.offglide) installed
on your ServiceNow instance, then the Premium Chat experience may differ from the
standard experience. If you plan to use an AI agent in the Premium Chat mode, make sure
to test so it works as expected.
Procedure
1.Enter a name for the AI agent.
2. Craft an AI agent description.
The description should clarify the purpose of the AI agent, including its inputs, outputs, and
context.
3. Craft the AI agent role.

> **[Screenshot: Define the specialty — New AI Agent guided setup wizard]**
> Full-width screenshot of the AI Agent Studio guided setup for a new AI agent (type: Chat). Two warning banners at top (third-party data routing notice and Premium Chat notice). Navigation tab bar: Overview, Create and manage, Testing, Activity, Settings. An "Exit" button top-right.
>
> Left sidebar stepper shows seven steps: 1) Define the specialty (filled/active), 2) Add tools and information (empty circle), 3) Define security controls (expanded showing "Define user access" and "Define data access"), 4) Add triggers (empty), 5) Select channels and status (empty). All steps below current are empty circles.
>
> Main content area titled "Define the specialty". Instruction text: "Using clear, precise language, write the name, description, role, and list of steps this AI agent completes." A "Generate details" teal button and "View writing guidelines" link.
>
> Four form sections: "Give it a unique name and description" — "AI agent name *" field with placeholder "For example, Categorize ITSM Incident AI agent"; "AI agent description * ⓘ" with "Description for LLM" link, a multi-line text area containing sample description "Categorize ITSM Incident AI agent assigns appropriate category, subcategory and configuration item ICD to an incident." Character count: 2000.
>
> "Define the role and required steps" — "View versions ∧" link. "AI agent role * ⓘ" with "Instruction for LLM" link; text area with "You're an expert in analyzing Incidents and are tasked with assigning appropriate category, subcategory and configuration item ICS." Character count: 2000. "List of steps ⓘ" with "Instruction for LLM" link; text area showing "1.a Fetch the details of the given incident…"
>
> "Unsupported model providers" — "List any model providers that this AI agent does not support." LLM providers field with "Select unsupported LLMs" placeholder.
>
> Two toggle rows: "Allow third party to access this AI agent (RP)" – Off toggle; "Allow AI specialists to access this AI agent (RP)" – Off toggle.
>
> "Manage long-term memory" — "Specify categories for memories about user details." Categories field: "Select Categories". "Allow this AI agent to learn from past executions: No" toggle.
>
> Bottom-right: "Save and continue" button.