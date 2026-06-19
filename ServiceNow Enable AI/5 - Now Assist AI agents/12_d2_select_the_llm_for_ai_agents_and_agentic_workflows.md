# Select the LLM for AI agents and agentic workflows

_Source pages: 34–34 | Depth: 2_

---

<!-- page 34 -->
Note: You can switch the detection impact from Log to Block and log or from
Block and Log to Log at any time.
iii. Select Save.
▪Export: Exports the offensiveness-based logs as a .CSV file. Logs can be analyzed for the
types of content that are being identified so you can take other preventive measures, such
as changing conversational questions.
2. Configure Prompt Injection for AI agents.
a.In the AI Agent Studio, navigate to Settings > Prompt Injection and select Configure.
You’re directed to the Now Assist Admin page to configure the Prompt Injection.
Note: For more information about configuring the Prompt Injection, see Configure
prompt injection attack protection.
When you configure the Prompt Injection for an agentic workflow by using the required
instructions, the system is designed to detect harmful content and block the conversation.
Select the LLM for AI agents and agentic workflows
Choose the large language model (LLM) service provider for Now Assist AI agents in AI Agent
Studio.
Before you begin
Role required: sn_aia.admin
About this task
LLMs are part of the foundation of agentic AI. Different LLMs can provide slightly different
performance and responses. You can select which LLM to use at a global level for agentic AI from
the AI Agent Studio to help adjust the response quality to best fit your agentic workflows.
Note: If you already have agents built and you change the global LLM, then you must
test the agents after making the change. You can test the models in the skill kit without
changing the LLM provider for all Now Assist AI agent skills. Outside of the Skill kit, skills
use whichever provider is set as default for the AI AGent SKills group.
Depending on your region, you may have to consent to using a different service provider.
Procedure
1.Navigate to All > AI Agent Studio > Settings.
2. Navigate to the Model provider tab.