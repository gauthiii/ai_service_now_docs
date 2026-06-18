# Configure disambiguation

_Source pages: 154–154 | Depth: 2_

---

<!-- page 154 -->
voice input for the Now Assist panel. See Configure Next Experience accessibility preferences
for more information about setting personal accessibility preferences.
Voice-to-text input can help users with mobility impairments access generative AI skills without
using a keyboard. This feature can also be useful to blind or low-vision users, neurodivergent
users, non-native language speakers, and mobile users on the go, such as field service agents.
The voice input feature is not supported in regulated markets.
Procedure
1.Navigate to All > Now Assist Admin > Now Assist Experiences.
If you’re already in the Now Assist Admin console, navigate to the Now Assist Experiences
page.
2. Go to the Now Assist panel tab.
3. In the Settings section, turn on the toggle for Voice Input.
Result
Users can choose whether they can use their voice to interact with the Now Assist panel in their
Next Experience accessibility preferences.
Configure disambiguation
Configure the disambiguation property that controls when the assistant asks clarifying questions
before responding to a Now Assist in Virtual Agent or Now Assist panel user request.
Before you begin
Role required: admin
About this task
Disambiguation or clarification helps the Now Assist assistant handle situations where the
user's request is ambiguous. Rather than returning an overwhelming list of results, the assistant
evaluates the request using a confidence scoring system and asks clarifying questions if
needed.
Procedure
1.In the filter navigator field, enter sys_properties.list.
2. In the selection fields, select Name from the drop-down list and enter type_2_disamb in
the Search field.
3. Configure the disambiguation property:
If you have
◦Now Assist in Virtual Agent or
◦Now Assist panel (standard chat, enhanced chat, or premium chat)
then use this configuration:
Property Possible values Default value Definition
sn_aia.type_2_disamb off/low/high off
◦off - clarification
is disabled. The
assistant responds