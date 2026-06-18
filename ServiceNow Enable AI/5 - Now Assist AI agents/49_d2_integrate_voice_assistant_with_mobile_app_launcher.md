# Integrate voice assistant with mobile app launcher

_Source pages: 172–172 | Depth: 2_

---

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