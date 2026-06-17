# AI voice agent reference

_Source pages: 177–195 | Depth: 2_

---

<!-- page 177 -->
▪Tool status (success or failure)
▪Tool response
The Analysis tab displays a turn-by-turn breakdown of AI voice agents invoked, tools executed,
and tool execution latency for the conversation.
4.Select Restart to start a new voice conversation or close the browser window to exit testing.
Selecting Restart clears the current conversation and resets the testing session.
Result
You have tested your voice assistant using the voice testing interface. Use the analysis results to
identify issues with agent routing, tool execution, or voice assistant performance, and refine your
assistant configuration as needed.
Test a voice agent from AI Agent Studio
Test your AI voice agent directly from AI Agent Studio by launching the voice testing interface
from the agent's channel configuration page.
Before you begin
At least one voice assistant must be linked to the AI voice agent. Without a linked voice assistant,
you cannot test the voice agent.
Role required: sn_aia.admin
Procedure
1.Navigate to All > Conversational Interfaces > AI Agent Studio.
2. Find the AI voice agent that you want to test and select it to open the agent configuration.
3. Select the Select channels and status page from the guided setup navigation.
4.Select Test in assistant and select the voice assistant you want to test from the dropdown.
The voice testing interface opens. See Test a voice assistant from Assistant Designer for
details on using the testing interface.
Result
The AI voice agent is tested from AI Agent Studio. Use the analysis results to identify gaps in
agent routing or tool execution and refine your voice agent configuration as needed.
AI voice agent analytics
The Voice dashboard page in the Analytics tab of Assistant Designer helps you monitor the
usage and performance metrics for AI voice agents.
Accessing AI voice agent analytics
To view the dashboard, navigate to All > Assistant Designer > Analytics and select the Voice
tab. See Voice page in assistant analytics for more information.
AI voice agent reference
Reference information for AI voice agents.
AI voice agent roles
The following table lists the roles installed with the Voice for Now Assist plugin.

<!-- page 178 -->
Roles Description
sn_voice_aia.admin Provides access to agents configuration flow
sn_voice_aia.guest Enables employees to use AI voice agents
without authentication
sn_voice_aia.integration Enables access to integrations such as Oracle
AI voice agent attributes
The AI voice agent attributes enable you to configure the authentication functionality for AI voice
agents. Navigate to All > System Definition > Tables and search for Now Assist Deployment
Config Attributes table to view the attributes.
The following table lists the attributes related to AI voice agent configuration.
Attribute Description
voice_max_retries The maximum number of retries allowed for
successful authentication before the user
account is locked. The default value is 3.
voice_minutes_account_is_locked The number of minutes the user account is
locked for, following maximum retries. The
default value is 1440 minutes.
persist_context_data Controls whether interaction context data is
persisted to Glide after a call. Set to true to
enable context data storage, which is required
for Amazon Connect integrations. The default
value is false. This attribute is scoped per
voice assistant deployment.
AI voice agent system properties
The following table consists of system properties to set up AI voice agents.
Property Description
sn_aia.enable_voice_agent_setup The system property to enable AI voice
agents. Set the value of the property to true to
enable AI voice agents on the instance.
glide.voice.authenticate.mfa_mandatory Controls whether multi-factor authentication
is required for caller verification. Set to false
to enable single factor authentication. Default
value is true.
Configuration for custom AI voice agent provider
The following table captures the required configurations on your instance to support AI voice
agents. These configurations are required only if you’re creating a new messaging channel,
provider channel, and provider channel identity for AI voice agents.

<!-- page 179 -->
Field Value
Messaging channel
Type Phone
Synchronous True
Provider Channel
Provider attributes action sn_va_as_service.virtual_agent__bot_to_bot_provider_attributes
Sender subflow sn_va_as_service.virtual_agent__bot_to_bot_contextual_action
Contextual action sn_va_as_service.virtual_agent__bot_to_bot_contextual_action
Allow account linking True
Account linking type Verification question
Automatic link action sn_va_as_service.virtual_agent__bot_to_bot_auto_link_account
Rich control mappings
Control type DefaultAction
Outbound transformer action sn_va_as_service.virtual_agent__bot_to_bot_action_outbound_transformer
Provider Channel Identity
Message auth Name of the message authentication that you
created as part of
Provider Identity properties
allow_storing_history_in_ongoing_conversation True
AI voice agent analytics indicators details
The following table maps the visualizations to the indicator sources and the calculation behind
the metrics shown in the dashboard.
AI voice agent analytics indicator details
Indicator Available
Visualization Calculation Frequency Unit Precision
type breakdowns
Total voice Automated Count of all None Daily 0
conversations voice calls
Calls Automated Count of None Daily 0
completed voice calls
without a where
live agent Agent
chat=false
ConversationsA utomated Count of None Daily 0
transferred voice calls
to a live where
agent Agent
chat=true

<!-- page 180 -->
AI voice agent analytics indicator details (continued)
Indicator Available
Visualization Calculation Frequency Unit Precision
type breakdowns
Number Automated Count of None Daily 0
of tickets Interaction
created Related
Records
where
Agent chat
= false and
Interaction
Virtual
agent =
true and
Interaction
Type =
Phone and
Interaction
AI Voice =
true
ConversationsA utomated Count of None Daily 0
disconnected voice calls
where
State=Closed
Abandoned
Inferred sn_na_analytiAcsv_eirnasgieg hts None Daily 1
customer table of session
satisfaction CSAT
(CSAT):
average
score (out
of 5)
Average Formula [[AI Agent- None Daily Minutes 0
voice Summed
conversation duration
duration of calls]] /
[[AI Agents-
Total Calls]]
Number of sn_na_analytiCcso_uinnts iogfh ts None Daily 0
deflected table voice calls
conversations where
per AI agent Resolved is
Yes
AI voice agent transcript and logs tables
The following tables contain details of the voice calls, from initiation and conversation details to
agent actions and tool executions.

<!-- page 181 -->
AI voice agent transcript and log tables
Table Details
sn_aia_execution_plan The sn_aia_execution_plan table stores
execution plans associated with voice
calls. Each record in this table represents a
single execution plan and contains detailed
information about the interactions and actions
that occurred during the call.
sn_aia_tools_execution The sn_aia_tools_execution table logs
information related to tool executions during
a voice call. Each record represents a single
tool execution and captures details about the
agent, the tool used, and the outcome of that
execution.
sys_cs_conversation The sys_cs_conversation table stores the
conversation record created at the start of
a voice call. Its creation timestamp marks
the beginning of the call. This table contains
metadata and transcripts associated with
the conversation, like state, device type, and
transcripts from the call.
Note: Personally Identifiable
Information (PII) data is redacted from
transcripts before it is stored.
Interactions The Interactions table is similar to
sys_cs_conversation and is created at the
same time as the conversation record. It
contains much of the same information related
to the voice call.
sys_generative_ai_log The sys_generative_ai_log table stores
general-purpose logs for generative AI
interactions during a voice call. If an agent
uses an LLM (Large Language Model) during
the call, this table records the relevant details
such as prompt, response, and errors.
Amazon Connect Lambda function code
Use the following Lambda function code when creating the Lambda function for the Amazon
Connect and ServiceNow voice assistant integration. Copy this code into the Lambda function
code editor. All dynamic values are read from environment variables set on the Lambda function.
const https = require('https');
const { getParameter, setParameter } =
require('@aws-lambda-powertools/parameters/ssm');
// Structured logger
────────────────────────────────────────────────────────
function log(level, message, context = {}) {
console[level === 'ERROR' ? 'error' : level === 'WARN' ? 'warn' : 'log'](

<!-- page 182 -->
JSON.stringify({ level, message, ...context })
);
}
// HTTP helper
──────────────────────────────────────────────────────────────
function sendHttpsRequest(options, postData) {
return new Promise((resolve, reject) => {
const req = https.request(options, (res) => {
let body = '';
res.on('data', (chunk) => { body += chunk; });
res.on('end', () => {
if (res.statusCode >= 200 && res.statusCode < 300) {
resolve(body);
} else {
reject(new Error(`HTTP ${res.statusCode} for
${options.method} ${options.hostname}${options.path}`));
}
});
});
req.on('error', reject);
if (postData) req.write(postData);
req.end();
});
}
// SSM
───────────────────────────────────────────────────────────────
───────
async function writeSsmParam(name, value) {
log('INFO', 'Writing SSM parameter', { param: name });
try {
await setParameter(name, { value, overwrite: true });
log('INFO', 'SSM parameter written successfully', { param: name });
} catch (err) {
// Non-fatal: token was fetched; caching failure is logged but not re-thrown
log('WARN', 'SSM write failed — token will not be cached', { param: name,
error: err.message });
}
}
// JWT
───────────────────────────────────────────────────────────────
───────
function getJwtExpiryMs(jwt) {
try {
const parts = jwt.split('.');
const payload =
JSON.parse(Buffer.from(parts[1], 'base64url').toString('utf8'));
if (typeof payload.exp !== 'number') throw new Error('exp claim is missing or
not a number');
return payload.exp * 1000;
} catch (e) {
throw new Error(

<!-- page 183 -->
`Failed to parse JWT exp claim — OAuth provider must issue
JWT access tokens: ${e.message}`
);
}
}
// OAuth
───────────────────────────────────────────────────────────────
─────
function fetchOauthToken(clientId, clientSecret) {
const payload = new URLSearchParams({
grant_type: 'client_credentials',
client_id: clientId,
client_secret: clientSecret
}).toString();
const options = {
hostname: process.env.now_instance_host_name,
path: '/oauth_token.do',
method: 'POST',
headers: {
'Content-Type': 'application/x-www-form-urlencoded',
'Content-Length': Buffer.byteLength(payload),
'Accept': 'application/json'
}
};
return sendHttpsRequest(options, payload);
}
async function fetchClientIDSecret(basePath, voiceServiceId) {
const clientIdPath =
`${basePath}/${voiceServiceId}/client_id`;
const clientSecretPath =
`${basePath}/${voiceServiceId}/client_secret`;
try {
const [clientId, clientSecret] = await Promise.all([
getParameter(clientIdPath, { decrypt: true }),
getParameter(clientSecretPath, { decrypt: true })
]);
return { clientId, clientSecret };
} catch (err) {
throw new Error(
`Failed to fetch client credentials from SSM at
${basePath}/${voiceServiceId}: ${err.message}`
);
}
}
async function getAccessToken(basePath, voiceServiceId) {
// 1. Try cache
──────────────────────────────────────────────────────────
const paramPath = `${basePath}/${voiceServiceId}/access_token`;
let cachedRaw;
try {

<!-- page 184 -->
cachedRaw = await getParameter(paramPath, { decrypt: true,
maxAge: 10 });
} catch (e) {
log('WARN', 'SSM cache read failed — treating as cache miss', { param:
paramPath, error: e.message });
}
if (cachedRaw) {
try {
const { access_token, expires_at } = JSON.parse(cachedRaw);
const ttlMs = expires_at - Date.now();
if (access_token && expires_at && ttlMs > 0) {
log('INFO', 'Using cached access token', { expiresInMs: ttlMs });
return access_token;
}
log('INFO', 'Cached token expired — refreshing', { expiresInMs: ttlMs });
} catch (e) {
log('WARN', 'Cached token parse failed — refreshing', { error:
e.message });
}
}
// 2. Fetch fresh token
──────────────────────────────────────────────────
const { clientId, clientSecret } = await
fetchClientIDSecret(basePath, voiceServiceId);
let body;
try {
body = await fetchOauthToken(clientId, clientSecret);
} catch (err) {
throw new Error(`OAuth token request failed: ${err.message}`);
}
let access_token;
try {
access_token = JSON.parse(body).access_token;
} catch (err) {
throw new Error(`Failed to parse OAuth response:
${err.message}`);
}
if (!access_token) throw new Error('OAuth response is missing access_token');
const expires_at = getJwtExpiryMs(access_token);
await writeSsmParam(paramPath, JSON.stringify({ access_token,
expires_at }));
return access_token;
}
// Call context
─────────────────────────────────────────────────────────────
function getCallContext(accessToken, contactData, voiceServiceId)
{
const payload = JSON.stringify({
call_correlation_id: contactData.ContactId,
voice_service_id: voiceServiceId,

<!-- page 185 -->
ani: contactData.CustomerEndpoint?.Address ?? '',
instance_name: process.env.now_instance_name
});
const options = {
hostname: process.env.voice_service_host_name,
path: process.env.call_context_api_path,
method: 'POST',
agent: new https.Agent({ rejectUnauthorized: false }),
headers: {
'Content-Type': 'application/json',
'Authorization': `Bearer ${accessToken}`,
'Content-Length': Buffer.byteLength(payload)
}
};
log('INFO', 'Requesting call context', { contactId:
contactData.ContactId, voiceServiceId });
return sendHttpsRequest(options, payload);
}
// Interaction context
──────────────────────────────────────────────────────
function getInteractionContext(accessToken, ccaasCallId) {
const path =
`/api/now/table/interaction_context` +
`?sysparm_query=interaction.client_session_id%3D
${ccaasCallId}%5Ename%3Dbot_context_data` +
`&sysparm_fields=name%2Cvalue` +
`&sysparm_limit=1`;
const options = {
hostname: process.env.now_instance_host_name,
path,
method: 'GET',
headers: {
'Authorization': `Bearer ${accessToken}`,
'Accept': 'application/json'
}
};
log('INFO', 'Requesting interaction context', { ccaasCallId });
return sendHttpsRequest(options, null);
}
// Handler
───────────────────────────────────────────────────────────────
───
exports.handler = async (event) => {
const contactData = event.Details?.ContactData;
const operation = event.Details?.Parameters?.operation;
const voiceServiceId =
event.Details?.Parameters?.voice_service_id;
const basePath = process.env.ssm_oauth_path;

<!-- page 186 -->
if (!basePath) {
log('ERROR', 'Missing required env var: ssm_oauth_path');
return { statusCode: 500, body: JSON.stringify({ error: 'Missing
env var ssm_oauth_path' }) };
}
// Obtain access token
───────────────────────────────────────────────────
let accessToken;
try {
accessToken = await getAccessToken(basePath, voiceServiceId);
} catch (e) {
log('ERROR', 'Failed to obtain access token', { error: e.message });
return { statusCode: 500, body: JSON.stringify({ error:
e.message }) };
}
// getCallContext
────────────────────────────────────────────────────────
if (operation === 'getCallContext') {
if (!voiceServiceId) {
log('ERROR', 'Missing voice_service_id for getCallContext');
return { statusCode: 400, body: JSON.stringify({ error: 'Missing
voice_service_id in event Parameters' }) };
}
let callContextResponse;
let dnis, tracing_id;
try {
callContextResponse = await getCallContext(accessToken,
contactData, voiceServiceId);
({ dnis, tracing_id } = JSON.parse(callContextResponse));
log('INFO', 'Call context retrieved', { contactId:
contactData.ContactId });
} catch (e) {
log('ERROR', 'getCallContext request failed', { error: e.message,
contactId: contactData?.ContactId });
return { statusCode: 502, body: JSON.stringify({ error:
`getCallContext failed: ${e.message}` }) };
}
return { statusCode: 200, dnis, tracing_id };
}
// getInteractionContext
─────────────────────────────────────────────────
if (operation === 'getInteractionContext') {
let interactionContextName = null;
let interactionContextValue = null;
let interactionId = null;
let snTransferReason = null;
try {
const contextResponse = await
getInteractionContext(accessToken, contactData.ContactId);

<!-- page 187 -->
const record = JSON.parse(contextResponse).result?.[0] ??
null;
interactionContextName = record?.name ?? null;
interactionContextValue = record?.value ?? null;
if (interactionContextValue) {
const valueObj = JSON.parse(interactionContextValue);
interactionId = valueObj?.interactionId ?? null;
snTransferReason =
valueObj?.sessionVariables?.snTransferReason ?? null;
}
if(!interactionId) {
throw new Error("Interaction context failed to retrive");
}
log('INFO', 'Interaction context retrieved', { contactId:
contactData.ContactId, interactionId });
} catch (e) {
// Non-fatal: return nulls so the contact flow can handle the missing data gracefully
log('ERROR', 'Failed to fetch or parse interaction context', { error:
e.message, contactId: contactData?.ContactId });
return { statusCode: 500, interactionId: null };
}
return {
statusCode: 200,
interactionContextName,
interactionContextValue,
interactionId,
snTransferReason,
body: JSON.stringify({ interactionContextName,
interactionContextValue, interactionId, snTransferReason })
};
}
// Unknown operation
─────────────────────────────────────────────────────
log('ERROR', 'Unknown or missing operation', { operation });
return { statusCode: 400, body: JSON.stringify({ error: `Unknown
operation: ${operation}` }) };
};
Amazon Connect Lambda Identity and Access Management (IAM) policy
Replace the Lambda execution role permissions policy with the following. Replace <region>,
<account-id>, and <lambda-function-name> with your values before applying.
{
"Version": "2012-10-17",
"Statement": [
{
"Action": [
"kms:Decrypt",
"kms:Encrypt"
],
"Resource": "*",
"Effect": "Allow",

<!-- page 188 -->
"Sid": "InlinePolicy0"
},
{
"Action": [
"logs:CreateLogStream",
"logs:PutLogEvents",
"ssm:PutParameter",
"ssm:GetParameter",
"ssm:GetParametersByPath"
],
"Resource": [
"arn:aws:logs:<region>:<account-id>:log-group:/aws/lambda/<lambda-function-name>:l
og-stream:*",
"arn:aws:ssm:<region>:<account-id>:parameter/com.servicenow.cti/*"
],
"Effect": "Allow",
"Sid": "InlinePolicy1"
}
]
}
Amazon Connect Voice AI inbound flow
Import the following JSON to create the Voice AI inbound contact flow in Amazon Connect.
Replace <region>, <account-id>, <lambda-function-name>, <instance-id>,
<queue-id>, and <voice-service-sys-id> with your values before importing.
{
"Version": "2019-10-30",
"StartAction": "ed95af7d-fab7-4df3-86f0-e5b4226101eb",
"Metadata": {
"entryPointPosition": {
"x": 40,
"y": 40
},
"ActionMetadata": {
"ed95af7d-fab7-4df3-86f0-e5b4226101eb": {
"position": {
"x": 188.8,
"y": 39.2
}
},
"08f00810-b884-4af5-99d2-cb8c18afaf8a": {
"position": {
"x": 2362.4,
"y": 40.8
}
},
"590a4c69-3afc-41ee-9421-e2dc55166991": {
"position": {
"x": 2603.2,
"y": 48.8
}
},
"642abbac-6c23-441f-94a6-48e67082fa47": {
"position": {

<!-- page 189 -->
"x": 2136.8,
"y": 42.4
},
"parameters": {
"QueueId": {
"displayName": "BasicQueue"
}
},
"queue": {
"text": "BasicQueue"
}
},
"36c1da1b-e95b-4685-bd6c-3cf4d22b06b7": {
"position": {
"x": 2608,
"y": 243.2
}
},
"0e65ca4c-6e0c-4cf5-ae90-91bb10a2c311": {
"position": {
"x": 440.8,
"y": 44.8
}
},
"ad63da6d-da3f-4ef2-ba91-31f8e8eb4238": {
"position": {
"x": 1911.2,
"y": 42.4
},
"conditions": [],
"conditionMetadata": [
{
"id": "93edeb32-3c74-4ffe-9716-1e4642038881",
"operator": {
"name": "Equals",
"value": "Equals",
"shortDisplay": "="
},
"value": "user_requested"
}
]
},
"04052d59-7bba-4ca4-9aa6-597ee230c262": {
"position": {
"x": 1704.8,
"y": 43.2
},
"dynamicParams": []
},
"4940e566-4c7a-4bb4-b938-305c7498cdbe": {
"position": {
"x": 1509.6,
"y": 46.4
},
"parameters": {
"LambdaFunctionARN": {
"displayName": "<lambda-function-name>"

<!-- page 190 -->
}
},
"dynamicMetadata": {
"operation": false
}
},
"8f634a38-6e73-45b5-8db9-0235190f33af": {
"position": {
"x": 2848.8,
"y": 231.2
}
},
"33608cd6-6e7a-47b9-8380-6977b3dcf123": {
"position": {
"x": 672,
"y": 42.4
},
"parameters": {
"LambdaFunctionARN": {
"displayName": "<lambda-function-name>"
}
},
"dynamicMetadata": {
"operation": false,
"voice_service_id": false
}
},
"8ea17f75-2185-4a68-af81-e9f6908c47fb": {
"position": {
"x": 1292,
"y": 39.2
},
"parameters": {
"ThirdPartyPhoneNumber": {
"countryCode": "",
"useDynamic": true
}
}
},
"a7ea0786-08fa-41c7-aabb-0b2bdda36c64": {
"position": {
"x": 876.8,
"y": 43.2
},
"dynamicParams": []
},
"fa2af8ef-be9d-4685-8bc5-f37166a06c0e": {
"position": {
"x": 1512.8,
"y": 342.4
}
},
"d0a02e42-281e-4068-91d5-ec81ef07f655": {
"position": {
"x": 1086.4,
"y": 43.2
},

<!-- page 191 -->
"conditionMetadata": [
{
"id": "3e23d991-b5f1-48e8-a2be-76408086206c",
"operator": {
"name": "Equals",
"value": "Equals",
"shortDisplay": "="
},
"value": "200"
}
]
}
},
"Annotations": [],
"name": "Voice AI inbound flow",
"description": "",
"type": "contactFlow",
"status": "published",
"hash": {}
},
"Actions": [
{
"Parameters": {
"SkipWhenDTMFBufferEnabled": "false",
"Text": "Hi Welcome to ServiceNow"
},
"Identifier": "ed95af7d-fab7-4df3-86f0-e5b4226101eb",
"Type": "MessageParticipant",
"Transitions": {
"NextAction": "0e65ca4c-6e0c-4cf5-ae90-91bb10a2c311",
"Errors": [
{
"NextAction": "0e65ca4c-6e0c-4cf5-ae90-91bb10a2c311",
"ErrorType": "NoMatchingError"
}
]
}
},
{
"Parameters": {},
"Identifier": "08f00810-b884-4af5-99d2-cb8c18afaf8a",
"Type": "TransferContactToQueue",
"Transitions": {
"NextAction": "590a4c69-3afc-41ee-9421-e2dc55166991",
"Errors": [
{
"NextAction": "590a4c69-3afc-41ee-9421-e2dc55166991",
"ErrorType": "QueueAtCapacity"
},
{
"NextAction": "590a4c69-3afc-41ee-9421-e2dc55166991",
"ErrorType": "NoMatchingError"
}
]
}
},
{

<!-- page 192 -->
"Parameters": {
"SkipWhenDTMFBufferEnabled": "false",
"Text": "Failed to connect to an agent"
},
"Identifier": "590a4c69-3afc-41ee-9421-e2dc55166991",
"Type": "MessageParticipant",
"Transitions": {
"NextAction": "8f634a38-6e73-45b5-8db9-0235190f33af",
"Errors": [
{
"NextAction": "8f634a38-6e73-45b5-8db9-0235190f33af",
"ErrorType": "NoMatchingError"
}
]
}
},
{
"Parameters": {
"QueueId": "arn:aws:connect:<region>:<account-id>:instance/<instance-id>/queue/<que
ue-id>"
},
"Identifier": "642abbac-6c23-441f-94a6-48e67082fa47",
"Type": "UpdateContactTargetQueue",
"Transitions": {
"NextAction": "08f00810-b884-4af5-99d2-cb8c18afaf8a",
"Errors": [
{
"NextAction": "590a4c69-3afc-41ee-9421-e2dc55166991",
"ErrorType": "NoMatchingError"
}
]
}
},
{
"Parameters": {
"SkipWhenDTMFBufferEnabled": "false",
"Text": "Call completed, thank you"
},
"Identifier": "36c1da1b-e95b-4685-bd6c-3cf4d22b06b7",
"Type": "MessageParticipant",
"Transitions": {
"NextAction": "8f634a38-6e73-45b5-8db9-0235190f33af",
"Errors": [
{
"NextAction": "8f634a38-6e73-45b5-8db9-0235190f33af",
"ErrorType": "NoMatchingError"
}
]
}
},
{
"Parameters": {
"FlowLoggingBehavior": "Enabled"
},
"Identifier": "0e65ca4c-6e0c-4cf5-ae90-91bb10a2c311",
"Type": "UpdateFlowLoggingBehavior",

<!-- page 193 -->
"Transitions": {
"NextAction": "33608cd6-6e7a-47b9-8380-6977b3dcf123"
}
},
{
"Parameters": {
"ComparisonValue": "$.Attributes.snTransferReason"
},
"Identifier": "ad63da6d-da3f-4ef2-ba91-31f8e8eb4238",
"Type": "Compare",
"Transitions": {
"NextAction": "36c1da1b-e95b-4685-bd6c-3cf4d22b06b7",
"Conditions": [
{
"NextAction": "642abbac-6c23-441f-94a6-48e67082fa47",
"Condition": {
"Operator": "Equals",
"Operands": [
"user_requested"
]
}
}
],
"Errors": [
{
"NextAction": "36c1da1b-e95b-4685-bd6c-3cf4d22b06b7",
"ErrorType": "NoMatchingCondition"
}
]
}
},
{
"Parameters": {
"Attributes": {
"snTransferReason": "$.External.snTransferReason",
"interactionId": "$.External.interactionId"
},
"TargetContact": "Current"
},
"Identifier": "04052d59-7bba-4ca4-9aa6-597ee230c262",
"Type": "UpdateContactAttributes",
"Transitions": {
"NextAction": "ad63da6d-da3f-4ef2-ba91-31f8e8eb4238",
"Errors": [
{
"NextAction": "8f634a38-6e73-45b5-8db9-0235190f33af",
"ErrorType": "NoMatchingError"
}
]
}
},
{
"Parameters": {
"LambdaFunctionARN": "arn:aws:lambda:<region>:<account-id>:function:<lambda-functi
on-name>",
"InvocationTimeLimitSeconds": "3",

<!-- page 194 -->
"InvocationType": "SYNCHRONOUS",
"LambdaInvocationAttributes": {
"operation": "getInteractionContext"
},
"ResponseValidation": {
"ResponseType": "STRING_MAP"
}
},
"Identifier": "4940e566-4c7a-4bb4-b938-305c7498cdbe",
"Type": "InvokeLambdaFunction",
"Transitions": {
"NextAction": "04052d59-7bba-4ca4-9aa6-597ee230c262",
"Errors": [
{
"NextAction": "8f634a38-6e73-45b5-8db9-0235190f33af",
"ErrorType": "NoMatchingError"
}
]
}
},
{
"Parameters": {},
"Identifier": "8f634a38-6e73-45b5-8db9-0235190f33af",
"Type": "DisconnectParticipant",
"Transitions": {}
},
{
"Parameters": {
"LambdaFunctionARN": "arn:aws:lambda:<region>:<account-id>:function:<lambda-functi
on-name>",
"InvocationTimeLimitSeconds": "3",
"InvocationType": "SYNCHRONOUS",
"LambdaInvocationAttributes": {
"operation": "getCallContext",
"voice_service_id": "<voice-service-sys-id>"
},
"ResponseValidation": {
"ResponseType": "STRING_MAP"
}
},
"Identifier": "33608cd6-6e7a-47b9-8380-6977b3dcf123",
"Type": "InvokeLambdaFunction",
"Transitions": {
"NextAction": "a7ea0786-08fa-41c7-aabb-0b2bdda36c64",
"Errors": [
{
"NextAction": "fa2af8ef-be9d-4685-8bc5-f37166a06c0e",
"ErrorType": "NoMatchingError"
}
]
}
},
{
"Parameters": {
"ThirdPartyPhoneNumber": "$.Attributes.pstnNumber",
"ThirdPartyConnectionTimeLimitSeconds": "30",

<!-- page 195 -->
"ContinueFlowExecution": "True"
},
"Identifier": "8ea17f75-2185-4a68-af81-e9f6908c47fb",
"Type": "TransferParticipantToThirdParty",
"Transitions": {
"NextAction": "4940e566-4c7a-4bb4-b938-305c7498cdbe",
"Errors": [
{
"NextAction": "fa2af8ef-be9d-4685-8bc5-f37166a06c0e",
"ErrorType": "CallFailed"
},
{
"NextAction": "fa2af8ef-be9d-4685-8bc5-f37166a06c0e",
"ErrorType": "ConnectionTimeLimitExceeded"
},
{
"NextAction": "fa2af8ef-be9d-4685-8bc5-f37166a06c0e",
"ErrorType": "NoMatchingError"
}
]
}
},
{
"Parameters": {
"Attributes": {
"pstnNumber": "$.External.dnis",
"statusCode": "$.External.statusCode"
},
"TargetContact": "Current"
},
"Identifier": "a7ea0786-08fa-41c7-aabb-0b2bdda36c64",
"Type": "UpdateContactAttributes",
"Transitions": {
"NextAction": "d0a02e42-281e-4068-91d5-ec81ef07f655",
"Errors": [
{
"NextAction": "fa2af8ef-be9d-4685-8bc5-f37166a06c0e",
"ErrorType": "NoMatchingError"
}
]
}
},
{
"Parameters": {
"SkipWhenDTMFBufferEnabled": "false",
"Text": "Failed to connect"
},
"Identifier": "fa2af8ef-be9d-4685-8bc5-f37166a06c0e",
"Type": "MessageParticipant",
"Transitions": {
"NextAction": "8f634a38-6e73-45b5-8db9-0235190f33af",
"Errors": [
{
"NextAction": "8f634a38-6e73-45b5-8db9-0235190f33af",
"ErrorType": "NoMatchingError"
}
]