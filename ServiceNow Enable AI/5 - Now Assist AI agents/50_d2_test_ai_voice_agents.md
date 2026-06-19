# Test AI voice agents

_Source pages: 173–176 | Depth: 2_

---

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