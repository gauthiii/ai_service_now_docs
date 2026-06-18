# Install Now Assist AI voice agents

_Source pages: 139–139 | Depth: 2_

---

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