### Web search custom skill

*Pages 44–45 of the source PDF*

The following table is provided to help clarify questions regarding how such custom skills can be created and deployed in each customer environment.

Expected field of use

Web search custom skill

The web search custom skill performs an internet search to answer a query. Web search is used whenever the LLM and AI Search are unable to provide results or whenever web search mode is activated.

The web search custom skill is based on a prebuilt topic block in Virtual Agent Designer, and is available when you turn on Now Assist in Virtual Agent. This feature is automatically triggered when both AI Search and the LLM can't find information to answer an end user's query. This feature can also be manually triggered whenever end users select the Web search results icon

( ) to enter into web search mode. Once web search activates, a third-party AI performs the search and returns with an answer.

|  |  |
| --- | --- |
| Workflow Extensibility | Now Assist Skill Kit enables customers to supplement their use of licensed, pre-built Now Assist skills, like example Incident Summarization. Now Assist Skill Kit also enables customers to create new workflow related skills within the scope of their Now Assist purchases. For example, within ITx for ITSM Pro/Enterprise Plus, within ITx and HR for customers with ITSM, and HRSD Pro/ Enterprise Plus. |
| Non-duplicative | Refer to the Now Assist Overview to see the pre-built skills that are currently available exist for purchase in ServiceNow Now Assist packages. Customers must build from the purchased skills instead of attempting to create duplicative versions of licensable ServiceNow skills without purchase. |
| Leveraging custom tables | Custom skills can be built using Now Assist Skill Kit to enable generative AI functionality on the custom tables that are provided in a customer’s licenses. |

For more information about the web search mode end-user display and functionality, see Web search .

Web Search AI choices are available in the OneExtend Definition Configs related list within the AI Search answers entry in the OneExtend Capabilities [sys_one_extend_capability_list] table. Select one of the AI definitions there, such as Perplexity, and set its value to true. Activate a matching AI credential by navigating to ALL > Connections & credentials > Credentials, and setting the matching API key (such as Perplexity API key active value to true).

For more information on how to work with the AI Search answers OneExtend capability, see Configure AI Search answers capability for web search.

For more information on how to add web search as a tool in the Now Assist Skill Kit, see Add a web search.


> **[Screenshot: ServiceNow – Web Search AI Capability Configuration (3-panel composite, page 45)]**
>
> Three vertically stacked screenshots:
>
> **TOP — "OneExtend Capabilities" list view:**
> Columns: Name | Active | Description | External | Metadata | Short description | Domain | Type.
> Visible rows: "AI search" | "AI Search answers" (Active = true, highlighted row) | "NLQ for AI Search" | "VA Now Assist AI Search Result Filter". The "AI Search answers" row is selected/highlighted.
>
> **MIDDLE — "OneExtend Capability – AI Search answers" detail record:**
> Short description and Description fields both read: "This capability allows users to search in platform using third party AI search models like google Gemini AI." Type = Websearch, Domain = global, External = unchecked, Metadata = Si (small icon). At the bottom: three related list tabs: "OneExtend Capability Attributes (9)" | "OneExtend Capability Definitions (4)" | **"OneExtend Definition Configs (4)"** (active tab).
>
> **BOTTOM — "Credentials" list view:**
> Columns: Name | User name | Type | Order | Active. Notable rows:
> - Google gemini API key — API Key — 100 — true
> - Google API key — API Key — 100 — true
> - Microsoft Bing API key — API Key — 100 — true
> - OpenAI responses credentials — API Key — 100 — true
> - **Perplexity API key** — API Key — 100 — **true** (row highlighted light blue)
> - servicenow api key — API Key — 100 — true
> - Windows MID Server Service Account — Windows — 99,999 — true
>
> The Perplexity API key row is highlighted to indicate it must be set to Active = true to enable Perplexity web search.
