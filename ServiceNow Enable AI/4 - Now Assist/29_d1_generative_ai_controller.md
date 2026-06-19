# Generative AI Controller

_Source pages: 185–220 | Depth: 1_

---

<!-- page 185 -->
5. After the diagnostics are complete, review the results of each test.
What to do next
If you have identified any problems with your skill configuration, you can edit the skill from the
Now Assist Admin console.
If editing the skill does not solve the issue, you can contact ServiceNow Support for additional
help.
Now Assist panel system properties
Use system properties to customize Now Assist panel. Some properties are available on a system
properties form, but some lesser-used properties are available only from the System Property
[sys_properties] table.
Property Description
sn_nowassist_va_enable_nap_aix_experience Enabled and integrated chat is available for
customers to choose from.
sn_nowassist_va_enable_nap_aix_experience Disabled, integrated chat is not available for
customers to choose from.
Generative AI Controller
Use Generative AI Controller to integrate third-party large language models (LLMs) with your
workflows.
Get started
Get started with Generative AI Controller to integrate directly with external LLMs. With Workflow
Studio and Virtual Agent Designer, you can create your own use cases for AI-generated text and
sentiment analysis, including advanced workflows and custom scripts.

<!-- page 186 -->
Explore Configure
Explore Generative AI Configure Generative AI
concepts and terminology. Controller provider capabilities.
Reference
Reference for Generative AI Controller.
Troubleshoot and get help
•ServiceNow Community
•Search the Known Error Portal for known error articles
•Contact Customer Service and Support
AI limitations
This application uses artificial intelligence (AI) and machine learning, which are rapidly evolving fields of study that generate predictions based on patterns
in data. As a result, this application may not always produce accurate, complete, or appropriate information. Furthermore, there is no guarantee that this
application has been fully trained or tested for your use case. To mitigate these issues, it is your responsibility to test and evaluate your use of this application for
accuracy, harm, and appropriateness for your use case, employ human oversight of output, and refrain from relying solely on AI-generated outputs for decision-
making purposes. This is especially important if you choose to deploy this application in areas with consequential impacts such as healthcare, finance, legal,
employment, security, or infrastructure. You agree to abide by ServiceNow’s AI Acceptable Use Policy , which may be updated by ServiceNow.
Data processing
This application requires data to be transferred from ServiceNow customers' individual instances to a centralized ServiceNow environment, which may be located
in a different data center region from the one where your instance is, and potentially to a third-party cloud provider, such as Microsoft Azure. This data is handled
per ServiceNow's internal policies and procedures, including our policies available through our CORE Compliance Portal .
Data collection
ServiceNow collects and uses the inputs, outputs, and edits to outputs of this application to develop and improve ServiceNow technologies including ServiceNow
models and AI products. Customers can opt out of future data collection at any time, as described in the Now Assist Opt-Out page.
Exploring Generative AI Controller
Learn more about generative AI concepts and how to integrate third-party generative AI into the
ServiceNow AI Platform to create content, summarize task records, and analyze user sentiment.

<!-- page 187 -->
Generative AI Controller overview
Complex algorithms and deep learning models learn patterns and use that knowledge to
generate new outputs. With Generative AI Controller, you can generate content directly within
the ServiceNow AI Platform.
Generative AI Controller integrates with external LLMs, including ones by OpenAI, Azure OpenAI,
Google Cloud (AI Studio and Vertex), Aleph Alpha, IBM watsonx, and Amazon Bedrock. These
capabilities are available in Workflow Studio flows, Virtual Agent topics, and scripting like
background scripts and business rules.
Generative AI Controller benefits
Benefit Feature
Integrate with third-party AI service providers to customize OpenAI, Azure OpenAI,
your AI experience Google AI, IBM watsonx and
Amazon Bedrock.
Get started with Generative AI Controller
•The Generative AI Controller application is installed with any Now Assist application.
•Sign up and create an account with a generative AI provider.
◦To sign up with OpenAI, go to their official platform website .
◦To get started with Azure OpenAI, go to their documentation .
◦To start using AI Studio with Gemini API, go to the AI Studio homepage .
◦To use Vertex AI on the Google Cloud, go to the Vertex AI homepage .
◦To get started with Aleph Alpha, go to their website and create an Aleph Alpha API account.
◦To get started with IBM watsonx, go to Getting started with IBM watsonx as a Service .
◦To get started with Amazon Bedrock, set up an IAM user with the correct permissions and
then explore the Converse API .
•Configure credentials for your preferred AI service provider for the Generative AI Controller
capabilities.
Domain separation and Generative AI Controller
Domain separation is supported for Generative AI Controller. Domain separation enables you to
separate data, processes, and administrative tasks into logical groupings called domains. You
can control several aspects of this separation, including which users can see and access data.
Support level: Standard
•Includes all aspects of Basic level support.
•Application properties are domain-aware as needed.
•Business logic: The service provider (SP) creates or modifies processes per customer. The use
cases reflect proper use of the application by multiple SP customers in a single instance.
•The instance owner must configure the minimum viable product (MVP) business logic and data
parameters per tenant as expected for the specific application.

<!-- page 188 -->
Sample use case: An Admin must be able to make comments required when a record closes for
one tenant, but not for another.
For more information on support levels, see Application support for domain separation .
Domain separation enables you to create partitions in the application data and administrative
processes. Because the generative AI tables are domain separated, Generative AI Controller
supports domain separation for OneExtend capabilities. The capabilities are the basic building
blocks for Virtual Agent Designer topics, components, flows, and scripts that use generative AI.
With domain separation, you can isolate the data and control access so that users in one domain
don’t have access to the capabilities of another domain.
For more details on domain separation and Virtual Agent, check out the documentation .
How domain separation works in Generative AI Controller
Domain separation is possible at the generative AI OneExtend capability level. Records that are
related to the execution and configuration of OneExtend capabilities, such as log tables that are
accessible to ServiceNow personnel, are also separated according to the capability's domain.
If you want to create a copy of an existing generative AI capability in a different domain, you
must create a record in the OneExtend Capabilities (sys_one_extend_capability) table. See the
reference for Generative AI Controller for more information about the OneExtend Capabilities
table.
You set the domain when the record is created. The domain is based on the domain that you're
in at the time that you create the record. When you're creating a capability record, you can use an
existing OneExtend Capability record as a blueprint to help confirm that the capability works as
intended.
After you create the OneExtend Capability record, you must create records for the following
attribute and config records in the new domain:
•OneExtend Capability Attribute records with the same values as the capability in the global
domain.
•A OneExtend Capability Definition that corresponds to the new capability.
•A OneExtend Definition Config definition record that includes the OneExtend Capability
Definition for the new domain.
You can also create these records by using the related lists in the OneExtend Capability record
default view.
Note: The OneExtend Capability Definition record that you add must be the same as
the capability that you want in the new domain. For example, if you’re creating a capability
in a new domain for sentiment analysis, you could add the Sentiment Analysis (OpenAI
Completion) record. Adding the Summarize (OpenAI Completion) Config could result in
unexpected behavior. The OneExtend Definition Config record that you select should
include the OneExtend Capability Definition record that you added.
Use cases
With domain-separated capabilities, you can build different Virtual Agent topics, flows with
Workflow Studio, or different background and business rule scripts that are also domain
separated.
Related topics
Domain separation for service providers

<!-- page 189 -->
Configuring Generative AI Controller
Configure Generative AI Controller providers and capabilities.
Configuration overview
Generative AI Controller enables you to choose between several AI providers or a generic
connector.
•Microsoft Azure OpenAI
•OpenAI
•Google AI Studio
•Google Vertex AI
•IBM watsonx
•Amazon Bedrock
Configure API credentials
Configure your large language model (LLM) credentials to use third-party
integrations with OpenAI, Azure OpenAI, Google Cloud, IBM watsonx, Amazon
Bedrock, and generic models to control the third-party integration.
Configure a generic LLM connector
Set up an external LLM to use generative AI capabilities to add finer control over
prompts and transformer scripts.
Configure an AI service provider for a capability
Set your preferred AI service provider for each capability and tailor generative AI
content to suit your business needs.
Enable recursive summarization for large inputs
Enable recursive summarization to retain context for large inputs in LLM calls.
Enable Dynamic Translation for generative AI capabilities
Use Dynamic Translation for in-product generative AI capabilities to support users
who speak different languages.
Installing Generative AI Controller
You can install the Generative AI Controller application (sn.generative.ai) with Now Assist
applications if you have the admin role.
Installation requirements
You must be on Vancouver patch 2 or later.
Generative AI Controller is included as a dependency for all Now Assist applications. It is not
recommended to install the application by itself. Instead, you can install Now Assist applications
from the Now Assist Admin console or directly from the ServiceNow Store. For details, see Install
Now Assist plugins.

<!-- page 190 -->
Now Assist Admin console plugin installation
Configuring API credentials for generative AI capabilities
Configure the credentials and connections for your preferred generative AI service provider to
integrate third-party generative AI on the ServiceNow AI Platform.
You can use several different models and generative AI service providers to integrate into your
custom flows, scripts, and topics.
•Amazon Bedrock
•Azure OpenAI
•Google - AI Studio
•Google - Vertex AI
•IBM watsonx
•OpenAI
•Generic third-party LLM
Configure API Credentials for Amazon Bedrock
Configure your API credentials to use AWS Bedrock in custom workflows and Virtual Agent
Designer topics.
Before you begin
You must have an AWS account and the IAM user needs permission to access the
bedrock:InvokeModel action.
Role required: admin
About this task
To use Amazon Bedrock as your LLM provider for Generative AI Controller capabilities, you must
have an active connection configured.
Procedure
1.Navigate to All > Connections & Credentials > Connections & Credential Aliases.
2. Open the record for Amazon Bedrock.

<!-- page 191 -->
3. Select the Create New Connection & Credential related link.
4.Enter your Region, such as us-east-1.
5. Enter your API key.
For more information, see AWS documentation on generating API keys .
6.Select Create.
Result
You can use Amazon Bedrock as your provider for Generative AI Controller capabilities in Flow
Designer, Virtual Agent Designer, and scripts to create custom experiences with generative AI.
Configure API credentials for Azure OpenAI
Configure your API credentials to use Azure OpenAI in custom workflows and Virtual Agent
Designer topics.
Before you begin
You must have access to the supported Azure OpenAI models through Now Assist Admin, or
an active Azure OpenAI account and a valid API key to securely connect ServiceNow to Azure
OpenAI.
Role required: admin
About this task
Enable Generative AI Controller capabilities by connecting ServiceNow to Azure OpenAI model
with your API key. This involves configuring your API credentials for secure access to Azure
OpenAI models.
For end-to-end configuration of Azure OpenAI in ServiceNow using your API key (BYOK),
establish a secure connection that enables customized AI capabilities while maintaining
flexibility, control, and conformance. For more information, see KB2663518 article in the Now
Support Knowledge Base.
Procedure
1.Navigate to All > Connections & Credentials > Connections & Credential Aliases.
2. Open the Generative AI provider record for Azure OpenAI.

<!-- page 192 -->
3. Select the Create New Connection & Credential related link.
4.Edit the Connection URL to include your resource name.
For Azure OpenAI, your Connection URL is in the form https://{your-resource-
name}.openai.azure.com. See the Azure OpenAI documentation for more information.
5. In the API key field, enter the API key for the provider.
Note: The characters in the API key field are masked in the user interface.
6.Create a connection by selecting Create.
Result
You can now use capabilities labeled with Azure OpenAI in Flow Designer, Virtual Agent
Designer, and scripts like background scripts and business rules to create custom experiences
with generative AI.
What to do next
If you want to use generative AI capabilities through your MID Server, open the new Connection
record, select the Use MID server check box, and save the record.

<!-- page 193 -->
Configure API credentials for Google AI Studio
Configure your API credentials to use Google AI Studio in custom workflows and Virtual Agent
Designer topics.
Before you begin
You must have a Google account to use AI Studio.
Role required: admin
About this task
In order to use Google AI Studio as your LLM provider for Generative AI Controller capabilities,
you must have an active connection configured.
Procedure
1.Navigate to All > Connections & Credentials > Connections & Credentials Aliases.
2. Open the record for Google Bard MakerSuite.
3. Select the Create New Connection & Credential related link.
4.Enter your API key.
You can find your API key in AI Studio by selecting Get API Key from the navigation menu.
5. Select Create.
Result
You can now use AI Studio (Google Cloud Completion) and AI Studio (Google Cloud Chat
Completion) in Flow Designer, Virtual Agent Designer, and scripts to create custom experiences
with generative AI.
Create API credentials for Google Vertex AI
Configure your API credentials to use Google Vertex AI in custom workflows and Virtual Agent
Designer topics.
Before you begin
You must have a Google Cloud project and the permissions to generate new OAuth credentials.
Role required: admin
About this task
In order to use Google Vertex AI as your LLM provider for Generative AI Controller capabilities,
you must have an active connection configured.
Procedure
1.Navigate to All > Connections & Credentials > Connections & Credentials Aliases.
2. Open the record for Google Bard Vertex AI.
3. Select the Create New Connection & Credential related link.
4.Fill in the required fields.
Google OAuth Connection
Field Value
Project ID The Project ID found in the Google Cloud console

<!-- page 194 -->
Field Value
Credential The name of your credential, such as Google OAuth Credential
Name
OAuth The name of your OAuth authentication, such as Google Registry
Name
OAuth To get the OAuth Client ID, create OAuth Client ID with the Google Cloud console
Client ID with the following attributes:
a.Application type: Web application
b.Authorized redirect URI: URL in the OAuth Redirect URL field, usually
<instance>.service-now.com/oauth_redirect.do
For more information, see the Google documentation for creating OAuth client
IDs . Once you have created the OAuth client, a pop-up window will have the
Client ID and Client secret for you to copy into your clipboard.
OAuth Client secret from your OAuth Client ID found in the Google Cloud console
Client
Secret
5. In the pop-up window, log in to a Google Account with access to the project.
6.When prompted for Google Cloud access for gsuite spokes, select Allow.
Result
You can now use Completions – Vertex AI and Chat Completions – Vertex AI in Flow Designer,
Virtual Agent Designer, and scripts to create custom experiences with generative AI.
Configure API credentials for IBM watsonx
Configure your API credentials to use IBM watsonx Granite models in custom workflows and
Virtual Agent Designer topics.
Before you begin
To use IBM watsonx large language models (LLMs), you must configure your credentials to use
the Generative AI Controller capabilities.
Role required: admin
About this task
To use models with IBM watsonx as your LLM provider for Generative AI Controller capabilities,
you must have an active connection configured.
Procedure
1.Navigate to All > Connections & Credentials > Connections & Credential Aliases.
2. Open the record named IBM watsonx.
3. Select the Create New Connection & Credential related link.
4.In the API key field, enter your API key.
For more information about generating an API key, see IBM's documentation for generating API
keys for authentication .
5. Create a connection by selecting Create.

<!-- page 195 -->
Result
You can now use capabilities labeled with IBM watson in Flow Designer, Virtual Agent Designer,
and scripts like background scripts and business rules to create custom experiences with
generative AI.
What to do next
If you want to use generative AI capabilities through your MID Server, open the new Connection
record, select the Use MID server check box, and save the record.
Configure API credentials for OpenAI
Configure your API credentials to use OpenAI in custom workflows and Virtual Agent Designer
topics.
Before you begin
To use the OpenAI and Azure OpenAI large language models (LLMs), you must configure your
credentials to use the Generative AI Controller capabilities.
Role required: admin
About this task
To use models with Azure OpenAI as your LLM provider for Generative AI Controller capabilities,
you must have an active connection configured.
Procedure
1.Navigate to All > Connections & Credentials > Connections & Credential Aliases.
2. Open the Generative AI provider record for OpenAI.
3. Select the Create New Connection & Credential related link.
4.In the API key field, enter the API key.
For OpenAI, see your OpenAI API keys for the credentials information.
5. Create a connection by selecting Create.
Result
You can now use capabilities labeled with OpenAI in Flow Designer, Virtual Agent Designer, and
scripts like background scripts and business rules to create custom experiences with generative
AI.

<!-- page 196 -->
What to do next
If you want to use generative AI capabilities through your MID Server, open the new Connection
record, select the Use MID server check box, and save the record.
Configure API credentials for a generic large language model (LLM) connector
Use a generic LLM connector to connect the ServiceNow AI Platform with an external AI provider
to use generative AI capabilities in custom Virtual Agent topics, Flows, or scripts, like background
and business rule scripts.
Before you begin
You must have access to the API of an external LLM in order to configure the credentials.
Role required: admin
About this task
You can connect an external LLM to the ServiceNow AI Platform by creating a connection alias to
the model, create a model record that points to the alias, create a prompt record for the model,
and then create a transformer record to transform the request or response from the LLM.
Procedure
1.Navigate to All > Connections & Credentials > Credentials.
2. Select API Key Credentials
3. In the Name field, give your API credential a name.
Including the name of the model in the API Key Credential makes it easier to identify later.
4.In the API Key field, enter your model's API key.
5. Select Submit to create the Credential.

<!-- page 197 -->
At this step, you have the API key information for the external LLM configured.
6.Navigate to All > Connections & Credentials > Connections & Credential Aliases.
7.Select New.
8.In the Name field, enter a name for the credential alias.
You do not need to change any other field values.
9.Select Submit.
10.After you are redirected to the List view, find and open the record you just created.
11. Select New in the Connections related list to create a new Connection record.
12. Enter the name of the connection in the Name field.
13.In the Credential field, select the Credential record you created with the model's API key.
You can search the list of Credentials by typing the name of the Credential in the field. You can
also select the lookup icon to open a modal with the full list.
14.In the Connection alias field, select the alias record you created.
15.For the Connection URL, enter the endpoint URL for the model.
For example, a model from Hugging Face might start with "https://api-
inference.huggingface.co". You can leave the remaining fields as they are.
16. Select Submit.
Result
You have the connection and credential alias to use for connecting a generic
LLM to use generative AI capabilities on the ServiceNow AI Platform. You can
confirm this by navigating to All > Connections & Credentials > Connections &

<!-- page 198 -->
Credential Aliases and confirming that the connection appears in the related list.
What to do next
For more information on configuring a generic LLM, see configure a generic LLM connector
Configure a generic large language model (LLM) connector
Connect an external LLM to the ServiceNow AI Platform by using a generic LLM connector. With a
connector, you can write your own prompts to send to the LLM and create your own generative AI
capabilities.
Before you begin
You must configure API credentials for your LLM before setting up the connector. For more
information, see configure API credentials for a generic LLM.
Role required: admin
About this task
Generative AI Controller offers several base system connections to popular AI service
providers such as Azure OpenAI and Google Vertex. However, you might want to incorporate an
industry LLM, a case-specific LLM into your custom workflows, or an LLM that adheres to your
organization's data handling policies.
Note: Generative AI Controller only supports text generation.
Procedure
1.In the navigation filter, go to the Generative AI Model
Configuration [sys_generative_ai_model_config] table by entering
sys_generative_ai_model_config.list.
2. Select New.
3. In the Model field, enter the name of the model.
If you are using Azure OpenAI, then the model name is the deployment name of your resource.
4.In the Provider field, select Custom LLM.
5. In the Connection and Credential Alias field, select the alias that you created when you set up
your credentials.

<!-- page 199 -->
If you haven't already configured your API credentials, see configure
API credentials for a generic large language model to learn how.
6.Create the model configuration by selecting Submit.
The model configuration is associated with the API key of the external model.
7.In the navigation filter, go to the Generative AI Configuration [sys_generative_ai_config] table
by entering sys_generative_ai_config.list.
8.Select New.
9.Select the list lookup icon next to the Definition field.
10.In the Select the document modal, select a capability that you want to configure with the
Custom LLM provider.
For example, if you're configuring a Summarize capability, select Summarize (Custom LLM).
11. Select OK to save your selection and close the modal.
12. In the Model field, choose the model configuration that you created in step 6.
After you select a Definition, the Model field changes into a drop-down menu with options
that use the Custom LLM provider. The model configuration that you made should appear in
this list. If it doesn't, go back to step 1 and make sure that your model configuration has the
Provider field set to Custom LLM.
13.In the Prompt template field, enter the prompt for the capability.
The prompt template is the instruction that is sent to the LLM to execute a capability. Use two
braces around the capability attribute names to incorporate them into the prompt template.
For example, if you're configuring a Summarize capability, your prompt template could be
Summarize the following for me in a friendly and helpful tone:
{{textToSummarize}}. To learn which attributes are available to include in the prompt,
go to the OneExtend Capability [sys_one_extend_capability] table, find the record for the
capability you're configuring, and look at the OneExtend Capability Attributes related list.

<!-- page 200 -->
You might need to experiment with different prompts to determine what works best for your use
cases.
14.Create the new Generative AI Configuration by selecting Submit.
15.In the navigation filter, go to the Generative AI Custom LLM Transformer
[sys_generative_ai_custom_llm_transformer] table by entering
sys_generative_ai_custom_llm_transformer.
16. Select New.
17. Write transformer scripts.
To have Generative AI Controller understand the format of the inputs and outputs of your
custom LLM, you must write transformer scripts. When you create a transformer record, code
and comments are provided for you to use as a guide while you edit. These scripts depend on
the expected request and response objects that are interpreted by your model.
For example, the Azure OpenAI request structure looks like the following script:
{"messages": [{"role":"user", "content":"Summarize the
following text: <<content>>"}], "max_tokens": 800,
"temperature": 0.7}
The request transformer script for that request structure is the following script:
(function(inputs) {
/* write code here to construct the request body and any
custom headers needed using the inputs object.
inputs structure: {
prompt_data: object,
request_data: object
} */
var requestData = inputs.request_data;
var promptData = inputs.prompt_data;
var prompt = promptData.prompt;
var model = promptData.model;
// construct body using the inputs
var body = {
messages: [{
"role": "user",
"content": prompt

<!-- page 201 -->
}],
max_tokens: parseInt(promptData.max_tokens),
temperature: parseInt(promptData.temperature)
};
//construct headers using the inputs
var headers = {};
return {
body: body,
headers: headers
};
})(inputs);
The response structure from Azure OpenAI looks like this script:
{
"choices": [{
"finish_reason": "stop",
"index": 0,
"message": {
"content": "<<response>>",
"role": "assistant"
}
}],
"created": 1714994995,
"id": "chatcmpl-9LqpXeLVXDAi6kciPfLeIDjmALeea",
"model": "gpt-35-turbo-16k",
"object": "chat.completion",
"usage": {
"completion_tokens": 47,
"prompt_tokens": 70,
"total_tokens": 117
}
}
Because of that response structure, the response transformer script looks like this script:
(function(inputs) {
/* write code here to transform the llm response into an
array of text responses, using the inputs object
inputs structure: {
prompt_data: object,
request_data: object,
response_body: string,
response_headers: string
} */
var requestData = inputs.request_data;
var promptData = inputs.prompt_data;
var responseBody = JSON.parse(inputs.response_body);
gs.info("response : " + inputs.response_body);
var responseTexts = [];
// write code here to populate the responseTexts array.
responseTexts.push(responseBody.choices[0].message.content);
return responseTexts;

<!-- page 202 -->
})(inputs);
18. Create the transformer scripts by selecting Submit.
Result
Your external LLM is connected to Generative AI Controller. You can use the AI service provider
for generative AI capabilities on the ServiceNow AI Platform.
What to do next
After you connect the LLM, you can set a provider for the generative AI capabilities of Generative
AI Controller. The capabilities are Generic Prompt, Generate Content, Sentiment Analysis, and
Summarize. For more information on choosing a provider, see Set a provider for a generative AI
capability.
Related topics
Bring your own key for third-party AI provider integration
Configure a custom resource path for BYOK models
Set a provider for a generative AI capability
Determine which AI provider to use for each of the generative AI capabilities of Generative AI
Controller.
Before you begin
Configure your credentials for your preferred provider. See Configuring API credentials for
generative AI capabilities for more details.
Role required: admin
About this task
Generative AI Controller comes with four capabilities by default. You can only configure a
provider for the capabilities listed in the table in step 2. If you have installed other Now Assist
applications, you may see other capabilities on the OneExtend Capability table. Those other
capabilities use the Now LLM Service as their provider and can't be reconfigured.
Procedure
1.In the navigation filter, search for the OneExtend Capability table by entering
sys_one_extend_capability.list.
2. Open the record for the capability that you would like to configure, such as Sentiment Analysis.
Generative AI Controller capabilities
Capability Definition
Generate Generate texts about a given topic with Workflow Studio and Virtual Agent
Content Designer.
Generic Prompt Create your own use case and prompt.
Sentiment Analyze user sentiment with Workflow Studio and Virtual Agent Designer.
Analysis

<!-- page 203 -->
Capability Definition
Summarize Create summaries of topics with Workflow Studio and Virtual Agent
Designer.
3. In the OneExtend Definition Configs related list, set Default to true for your preferred
capability provider.
Note: By default, you can choose only one provider for a capability. For example, if
Default is true for Sentiment (OpenAI Completion), you must set Default to false
before changing Default to true for Sentiment (Azure OpenAI).
Model Options
You have the option to choose between several different models for each
capability.
Capability Definition Model
◦OpenAI Completion
GPT-3
◦Azure OpenAI Completion
◦OpenAI Chat Completion
GPT-3.5
◦Azure OpenAI Chat Completion

<!-- page 204 -->
Capability Definition Model
◦GPT4 (OpenAI Chat Compl)
GPT-4
◦GPT4 (Azure OpenAI Chat Compl)
◦AI Studio (Google Cloud Completion)
Google Gemini
◦AI Studio (Google Cloud Chat Completion)
◦Vertex AI (Google Cloud Completion)
◦Vertex AI (Google Cloud Chat Completion)
IBM watsonx Granite
Result
Flows, topics, and scripts that use the generative AI capability use the provider you've specified.
Related topics
Bring your own key for third-party AI provider integration
Configure a custom resource path for BYOK models
Select a model for Amazon Bedrock
Choose which large language model (LLM) to use with Amazon Bedrock for custom skills.
Before you begin
You must have the latest version of Generative AI Controller and the Amazon Bedrock spoke
installed on your instance. You must also set up your API credentials. For more information, see
Configure API credentials for Amazon Bedrock.
Role required: admin
About this task
You may have multiple models configured to use with Amazon Bedrock. By default, the settings
use Amazon's Titan model, but you can configure the spoke to use a different model by changing
the Generative AI Model Config record.
Procedure
1.In the filter navigator, navigate to the Generative AI Model Config table by entering
sys_generative_ai_model_config.list.
2. Search in the Provider field column for Amazon Bedrock, then open the resulting record.
3. In the Model field, enter the ID of the model that you want to use.
You can find the model ID on the Foundation models > Base models page on Amazon
Bedrock.
4.Select Save to update the record.
5. Map the chosen model to a custom skill.
a.In the filter navigator, go to the Generative AI Config table by entering
sys_generative_ai_config.list.
b.Search for the custom skill you've created that uses Amazon Bedrock as the service
provider, and open the record.

<!-- page 205 -->
The Definition should be OneExtend Capability Definition: <Name of Skill>.
c.Set the Model field to the model ID you entered in step 3.
Result
Your chosen model with the Amazon Bedrock provider will be used for custom skills.
What to do next
You can create custom skills with the Amazon Bedrock provider in Now Assist Skill Kit and
perform step 6 to set the new model.
Configure small talk filters
Redirect users to different Virtual Agent topics if small talk, such as greetings, expressions of
gratitude, complaints, or requests to close, are detected in conversations.
Before you begin
Role required: admin
About this task
When engaging with generative AI, many people send conversational messages that are
ultimately unhelpful for the Virtual Agent when determining how to help the user achieve their
goals. You can configure small talk filters that catch these conversational messages. When a user
is sending a message such as a greeting or expressing complaints about the conversation, you
can redirect them to serve their needs.
Procedure
1.In the navigator, go to the Generative AI Filter [sys_gen_ai_filter] table by entering
sys_gen_ai_filter.list.
2. Open the record for the small talk filter that you want to configure or select New to create one.
By default, the four available filters for small talk are Greetings, Gratitude, Complaint, and
Closure. If you see other filters, those filters are sensitive topic filters that can be set up
with the Now Assist Admin console. See Configure subject filters for generative AI for more
information.
3. If creating a filter, add a Name and Description for the filter.
4.Choose the Filter Error Topic that you want to redirect users to when the small talk filter is
detected.
By default, the user is redirected to the Small Talk Response Processor topic.
5. For the Order field, choose the order to apply the filters.
Filters are processed by lowest order to highest. A filter with order 100 is processed before a
filter with order 200.
6.Optional: In the Filter Configurations field, use the name "portal" to determine where the filter
should be run, such as setting "portal" to value "sp" to apply only the filter on the sp portal.
Use a comma-separated list to select multiple values.

<!-- page 206 -->
(Optional)
7.Select Submit.
8.In the navigator, go to the Generative AI Filter Sample [sys_gen_ai_filter_sample] table by
entering sys_gen_ai_filter_sample.list.
9.Optional: Review the sample phrases for each filter.
Statements that match these sample phrases activate the selected filter. You can create
sample phrases manually by creating records on the table or by using generative AI to
generate samples for you.
a.To create a sample manually, select New.
b.In the Sample text field, enter the sample text of what you want to be caught by the filter.
c.In the Filter field, select the filter you want the sample to be applied to.
d. If you want to generate more sample phrases with generative AI, open a record for a sample
phrase for the desired filter.
An example might be the "Thanks for your assistance with my task" sample filter for the
Gratitude filter.
(Optional)
e. Select Submit to create additional example statements to trigger the filter.
The more sample statements that you provide, the more likely that the filter aligns with your
expectations of its behavior.
Result
When engaging in conversations with generative AI, users are redirected to a new topic when
filtered subjects or sentiments are detected.

<!-- page 207 -->
Configure AI Search answers capability for web search
AI web search is a OneExtend capability that enables end users to perform web searches and
receive AI-powered answers. The capability supports multiple AI providers and integrates with
virtual assistants and workflows.
Before you begin
When web search is turned on, Gemini is the default AI provider. To switch AI providers, admins
must configure the AI Search answers OneExtend capability. The instance or skills default AI
provider that is set in Now Assist Admin can differ from the web search AI provider. For more
information on the default instance or skills AI provider, see Manage model providers.
Some of the AI providers require API keys whereas others don’t require API keys because they
use OEM. The following table highlights the four AI providers and whether they use API keys or
OEM.
AI providers that require API keys AI providers that use OEM
OpenAI Gemini
Note: Gemini is the default web search
AI provider in the AI Search answers
OneExtend capability. If you selected
Gemini as the LLM provider in Now Assist
Admin and you want to use Gemini as
your web search AI provider, you don’t
need to configure the AI Search answers
OneExtend capability.
Perplexity Azure
Note: Azure doesn’t currently support
web search.
Role required: admin
Procedure
1.In the navigator filter, go to the OneExtend Capability list by entering
sys_one_extend_capability.list.
2. Search for the AI Search answers OneExtend capability.
3. Select the AI Search answers record.
4.In the OneExtend Definition Configs related list, view the Default column.
When the AI provider's Default column is set to true, that is the AI search provider used for
the web search. Gemini defaults to true. To change the AI search provider to an AI provider
that requires the use of API keys, such as Perplexity or OpenAI, continue with the following
steps.
Note: Although Azure OpenAI answer is an option for an AI search provider, Azure
doesn't support web search and should remain set to false.
5. In the OneExtend Capability Definitions related list, select the value in the Connection And
Credential Alias column for the AI Search provider you want to use.

<!-- page 208 -->
For example, if you want to switch the web search AI provider to OpenAI, select
sn_openai.OpenAI from the Connection And Credential Alias column.
The Connection & Credential Alias form opens. If no connections are available within the
Connections related list, you must create a connection.
6.Complete one of the following actions based on the following scenarios.
Scenario Action required
If a connection is already available within the
Connection is available Connections related list, continue to the next
step.
a.Select New within the Connections related
list to create a connection.
b.In the Name field, enter the connection
name.
For example, Open AI connection.
Note: For more information about
the fields on the HTTP(s) Connec­
tions New record form, see Create an
.
c.Select the Lookup using list icon next to
Credential.
d. Select New to create a credential for your
connection.
Note: You may see an existing
credential that you can select from
the Credentials list, but some AI
Connection isn’t available and must be cre­
providers, like OpenAI, do not come
ated
with default credentials.
e. Select API Key Credentials.
f.Enter a name in the Name field.
For example, Open AI key.
g.Enter the API key in the API key field.
Note: For more information about
the fields on the API Key Credentials
New record form, see API key creden­
.
h.Select Submit.
You’re redirected back to the HTTP(s) Con­
nections new record form.
i. Enter the connection URL in the Connec­
tion URL field.

<!-- page 209 -->
Scenario Action required
For example, enter https://api.ope­
nai.com for Open AI.
j. Select Submit.
a.In the OneExtend Definition Configs related list, set the existing default AI provider from
true to false.
b.In the OneExtend Definition Configs related list, set the AI provider that you want to use from
false to true.
7.Select Update.
The AI provider for web search is now updated.
Result
End users can now perform an internet search to answer a query whenever in web search mode.
For more information about web search mode for end users, see Web search .
What to do next
If you switched the AI provider to Perplexity, you must work with the
sn_ai_websearch.perplexity_model_name system property. For more information on
this system property, see Now Assist in Virtual Agent system properties .
Enable recursive summarization for large inputs
Use recursive summarization to break down the requests to the large language models (LLMs)
into smaller pieces so that you can maintain the context for generative AI capabilities.
Before you begin
Role required: admin
About this task
LLMs have a maximum number of tokens that can be processed in a single request. Certain
fields, such as activity fields, can have more information than can fit in within those restrictions.
Recursive summarization breaks the information given to an LLM into chunks, summarizes each
chunk individually, and then processes the original request with the summarized chunks. The
chunks are organized with overlaps between the pieces so that the context is retained across
every piece.
Note: Enabling recursive summarization may cause the capabilities to process large
inputs more slowly because they must make multiple calls to the LLM instead of just one
call.
Procedure
1.In the navigator filter, go to the OneExtend Capability list by entering
sys_one_extend_capability.list.
2. Open the record for the OneExtend capability that you want to change.
3. In the OneExtend Definition Config related list, set Enable Large Input Support to true for the
OneExtend Definition that you want to enable recursive summarization for.
4.In the OneExtend Capability Attributes related list, set Contains Large Input to true for the
fields that you want to add recursive summarization in.
The fields that are most likely to contain a large amount of data, such as an activities field,
should have their values set to true. You can also select the Contains Large Input check box
on the OneExtend Capability Attribute record and save the record to set the value to true.

<!-- page 210 -->
Result
Recursive summarization is enabled for the OneExtend Capability for the fields specified in this
procedure.
Enable Dynamic Translation for capabilities in Generative AI Controller
Use Dynamic Translation to add multiple language support for generative AI capabilities to
support users who speak languages other than English.
Before you begin
You must have the Dynamic Translation and Conversational Dynamic Translation plugins
installed and enabled on your instance. For more information on setting up Dynamic Translation,
see configuring Dynamic Translation .
You must have a default Translation Configuration set in the Translation Configuration table
(sn_dt_translator_configuration).
Role required: genai_admin
About this task
By default, Dynamic Translation is inactive for capabilities with Generative AI Controller.​
Dynamic Translation isn't available for capabilities in Virtual Agent or Now Assist panel.
Procedure
1.Navigate to the OneExtend Capability (sys_one_extend_capability) table by entering
sys_one_extend_capability.listin the navigator.
2. Open the record for the capability that you want to enable Dynamic Translation for.
3. In the OneExtend Capability Attributes related list, open the record for the attribute you would
like to be translated, such as response.
4.Select Translate to enable translation.
If you don't see the field on the form, you must edit the form to display the Translate. One way
of adding the field to the form is by selecting the menu icon by the table name of the form and
choosing Configure > Form Layout. Add the Translate field to the Selected list. Then, select
Save to save the form. You're then redirected back to the record with the field available to
select.
5. Select Submit to save the record.
Result
Dynamic Translation is installed for your generative AI capability on the attribute that you
selected.
Disable Dynamic Translation for LLM Virtual Agent conversations
Enable dynamic translation of chat messages into English before they are sent to the
®
ServiceNow large language model (Now LLM) in generative AI topics to support users who
speak other languages.
Before you begin
You must have Dynamic Translation for Virtual Agent installed and active for your Virtual Agent.
For more information, check out .
Role required: admin
About this task
Dynamic Translation is enabled by default.

<!-- page 211 -->
There are certain limitations of Dynamic Translation for Virtual Agent. Catalog item names are
not automatically translated, and only languages configured for language detection will be
recognized.
Procedure
1.Navigate to the System Properties table by entering sys_properties.list in the
navigator.
2. Search for select the sn_generative_ai.disable_dynamic_translation system
property.
3. Set the property value to true.
4.Select Save to save the record.
Result
Chat requester utterances are translated into English before being sent to Now LLM and output
messages are translated back into the requester's preferred language.
Configure rate limiting for providers
Configure rate limiting to control the traffic flow to the one_extend request by restricting the
number of requests that can be made within a certain time frame.
Before you begin
Role required: admin
About this task
To rate limit the one_extend request, you must define the rate limit rules for the incoming
requests. You can create your own rule in the One Extend Rate Limit Rules table.
Procedure
1.On your ServiceNow instance, navigate to the One Extend Rate Limit Rules
[sys_one_extend_rate_limit_rules] table and select New.
2. On the form, fill in the fields.
One Extend Rate Limit Rule form
Field Description
Name Name of the rate limit rule. Identify the rate
limit rule with a name.
Application Application scope that must be set to Global.
Resource Resources to select for your rate limit rule.
Use one of the following resources for your
rate limit rule:
◦LLM Provider: For the LLM Provider, select
the generative AI provider mapping.
◦Capability Definition: For the Capability
Definition, select the One Extend
Capability Definition.
◦All Capabilities: Applies to all providers
and all capability definitions.
Rule Type Rule type for the rate limit rule.

<!-- page 212 -->
Field Description
Define the rule type using the following
options:
◦Instance: Accumulates data from all the
users of that instance.
◦User: Keeps the count of the requests per
user.
Request limit per hour Maximum number of requests to be received
per hour.
Active Status of the rate limit rule.
3. Select Submit.
Bring your own key for third-party AI provider integration
The bring your own key (BYOK) feature enables you to use your own API credentials from
supported cloud AI providers, such as Azure OpenAI, Amazon Bedrock, and Google Gemini, to
run Now Assist skills and AI agents.
When BYOK is enabled, Now Assist sends model requests through your cloud AI provider
account instead of ServiceNow AI Platform infrastructure. This approach lets you maintain
ownership of your AI configuration, security controls, and data processing environment while
continuing to use Now Assist capabilities.
BYOK supports the same AI models that the ServiceNow AI Platform supports. After you
configure your API credentials, Now Assist uses your provider resources to process requests
instead of using the default ServiceNow AI provider. BYOK keeps your keys under your control
and AI workloads running within your cloud environment.
Note: Using your organization’s cloud AI provider account might result in additional
charges from that provider. Review the provider’s pricing and terms of service before
enabling BYOK.
ServiceNow integrated model providers
BYOK supports the following cloud AI providers:
•Azure OpenAI
•Anthropic Claude on AWS, which is accessible through Amazon Bedrock
•Google Gemini
Configuring a BYOK connection with a cloud AI provider
To use your cloud AI provider resources within your ServiceNow instance, configure a connection
between ServiceNow and your provider. Configuration steps vary by provider, but follow a similar
high-level configuration workflow as the following steps:
1.Create connection and credentials for the provider, such as endpoint, API key, and region.
2. Enable BYOK for the provider in Now Assist Admin.
3. Map ServiceNow model aliases to provider model versions. For example, map
gemini_large → 2.5 Pro.

<!-- page 213 -->
4.Optionally, override variants in each skill in Version Management.
5. Validate that requests are using your AI provider account by reviewing outbound HTTPS logs.
For step-by-step instructions for each supported cloud AI provider, see Configure Bring Your
Own Key (BYOK) for Now Assist and AI Agents [KB2666298] article in the Now Support
Knowledge Base.
Example: High-level BYOK configuration for Azure OpenAI
1.Set up Azure OpenAI connection with your own key to use Azure OpenAI within your
ServiceNow instance.
For more information, see Configure API credentials for Azure OpenAI.
2. Configure your Azure OpenAI model and deployment name in Generative AI Controller so your
ServiceNow instance can recognize and use it.
For more information, see Create a custom embedding model .
3. Modify the prompt configuration to write your own prompts to send to the Azure OpenAI LLMs.
For more information, see Configure a generic large language model (LLM) connector.
4.Switch providers to use BYOK for AI processing.
For more information, see Manage Integration.
Related topics
Configure a custom resource path for BYOK models
Configure a custom resource path for BYOK models
Enter a custom resource path in your bring your own key (BYOK) model configuration so that
Generative AI Controller can connect to your Azure OpenAI deployment using the correct
endpoint.
Before you begin
•Bring your own key (BYOK) must be configured for your instance. For more information, see
Bring your own key for third-party AI provider integration.
•You must have an active connection and credential alias for your Azure OpenAI service. For
more information, see Configure API credentials for Azure OpenAI.
Role required: admin
About this task
When you configure a bring your own key (BYOK) model in Generative AI Controller, it uses the
connection and credential alias to send requests to your third-party AI service provider. The alias
contains the base URL and API key for your provider. Some AI providers, such as Azure OpenAI,
use a resource path prefix that is different from the default one that Generative AI Controller
provides. This increases flexibility when you're configuring a BYOK provider, as you can tailor the
resource path to your specific needs.
You configure that resource path prefix in the Chat Completions Resource Path connection
attribute of the Azure OpenAI connection alias record.
Note: The custom resource path configuration is supported for Azure OpenAI only.

<!-- page 214 -->
Procedure
1.Navigate to All > Connections & Credentials > Connections & Credential Aliases.
2. Open the connection alias record for Azure OpenAI.
3. In the Connections Attributes related list, select the Chat Completions Resource Path
attribute.
4.In the Default value field, update the existing value to match your resource path prefix.
The resource path prefix is the segment of your endpoint URL between the hostname and your
deployment name.
For example, given the Azure OpenAI endpoint URL:
https://<your-resource-name>.openai.azure.com/openai/deploymen
ts/<your-deployment-name>
The resource path prefix is:
/openai/deployments
Enter the following resource path prefix in the Default value field:
/openai/deployments/
Note: You can find your resource name in the Azure portal. The base URL (https://<your-
resource-name>.openai.azure.com) is already configured in your Connection URL field.
Do not include the deployment name in this field.
5. Select Update.
Result
Generative AI Controller uses the resource path prefix you entered to send requests to your
Azure OpenAI deployment. Your agentic AI skills are ready to use this provider.
Reference for Generative AI Controller
Reference topics provide information about Generative AI Controller tables, and properties.
Tables installed
Name Table Description
OneExtend sys_one_extend_capability Generative AI Controller capabilities that
Capability include Summarize, Record Summarization,
Generate Content, and Generic Prompt.
OneExtend sys_one_extend_capability_definition Attribute configuration for input and output
Capability variables for Workflow Studio subflows.
Definition
OneExtend sys_one_extend_definition_attribute Input and output variables for Workflow
Capability Studio subflows. Variable names can't
Definition be changed if the capability is active and
Attribute used on the instance. You can check
whether a capability is used by going to the
OneExtend Usages table.

<!-- page 215 -->
Name Table Description
OneExtend sys_one_extend_builder_config Determines which capability and provider
Builder is related to each builder component
Config for Workflow Studio and Virtual Agent
Designer.
OneExtend sys_one_extend_builder_capability Definitions for a capacity and its provider
Builder for builder components.
Capability
OneExtend sys_one_extend_usage Each usage of a capability in a Workflow
Usage Studio or Virtual Agent Designer topic, as
well as any scripts such as business rules
or UI actions.
Gen AI Log sys_gen_ai_log_metadata Logs data about requests to the LLMs,
Metadata including information about definition,
errors, user, and feedback provided.
AI-generated content can be tracked for
a duration beyond six months with Now
Assist configuration option. You can export
historical data by writing a script to copy it
into a different table without deleting the
information.
Generative sys_generative_ai_metric Logs various metrics to evaluate LLM
AI Metric response performance and accuracy,
including edit score, edit distance,
guardrail activity, and LLM model details.
It also records sensitive topic triggers and
their scores for safety monitoring.
Gen AI sys_gen_ai_model_version_mapping Maintains mappings between AI model
Model versions, their providers, and configuration
Version details, providing a clear understanding of
Mapping how source models map to target models.
It also includes associated metadata,
such as skill type, model type, resource
associations, and provider information.
Generative sys_generative_ai_log Logs Generative AI prompts, responses,
AI Log and edited responses for debugging
LLM calls. HR-related logs are exclusively
restricted to HR Administrators, ensuring
sensitive information remains protected.
For more information, see Generative AI
Controller tables.
Properties
Generative AI Controller properties
Property Description
com.sn.generative.ai.provider Default provider when capability definition has
no default.

<!-- page 216 -->
Generative AI Controller properties (continued)
Property Description
Type: choice list
No default value
com.sn.generative.ai.ais.message Message that is displayed when AI Search
fails to find an answer to a query.
Type: string
Default value: No answer found.
com.sn.generative.ai.log_prompt Prompt that determines whether generative AI
API calls are logged.
Type: true | false
Default value: true
com.sn.generative.ai.moderation.message Message that is displayed if the OpenAI
or Azure OpenAI moderation tools identify
the content that goes against their terms of
service.
Type: string
Default value: The response cannot be
displayed as it’s deemed inappropriate by
OpenAI.
com.glide.one.extend.token.buffer Buffer that checks the request for the number
of tokens before a OneExtend capability is
executed. The maximum allowed request
tokens are calculated based on the maximum
tokens that are permitted by the AI provider's
API minus the response token and buffer value
that is specified in this system property.
Type: integer
Default value: 250
domain.llm.usage.entitled Determines if a specific domain has
permission to use the Now Assist features and
whether to use the Large Language Model
(LLM) to process data for that domain or
restrict its use.
Type: true | false
Default value: true

<!-- page 217 -->
Generative AI Controller properties (continued)
Property Description
Note: Setting
domain.llm.usage.entitled to
false, prevents a domain and its child
domains from using Now Assist.
External links
Provider Data policy Usage policy
Amazon Bedrock Data protection AWS Service Terms
Google Cloud Google Cloud Platform Terms Google Cloud Platform Terms
of Service of Service
IBM watsonx Keeping your data secure and Foundation model terms of
compliant use in watsonx.ai
Microsoft Azure OpenAI Data, privacy, and security for Code of conduct for Azure
Azure OpenAI Service OpenAI Service
OpenAI API data usage policies Usage policies
Generative AI Controller tables
Generative AI Controller use dedicated tables to log AI activities and track Now Assist usage
across Now Assist capabilities.
Generative AI Log [sys_generative_ai_log] table
Logs generative AI prompts, responses, and edited responses for debugging LLM calls. Log
entries related to HR are restricted to HR administrator to protect sensitive information.
Generative AI Log [sys_generative_ai_log]
Column Data type Description
Additional Data String Contains concatenated values
for actions performed on the
generated LLM response,
such as copied or edited. This
field is populated through the
feedback API.
Caller String Contains information about
the calling application that
generated the log entry.
Completed At Date/Time Timestamp when the
generative AI execution
completed.
Conversation Reference Reference to the conversation
this log is part of.

<!-- page 218 -->
Generative AI Log [sys_generative_ai_log] (continued)
Column Data type Description
Created Date/Time Date and time when the log
entry was created.
Created By String Contains user information that
initiated the execution or flow.
Definition Reference Reference to the capability
definition responsible for
generating the log entry.
Derived Scope Reference Associated scope of the
application that generated the
log entry.
Domain Domain ID Domain associated with the
execution that generated the
log entry.
Domain Path Domain Path Path associated with the
domain from where the
capability is executed. When
domain separation is enabled,
this column is automatically
populated by the platform.
Edited Response String Captures the edited version
of the response when a user
modifies it.
Error String Error message, if the request
encountered an error.
Error Code String Error code associated with the
error message.
External True/False Error code associated with the
error message.
Feedback Choice Feedback on the LLM
response. Possible values:
Accepted, Rejected,
Ignored, SlightlyPositive,
SlightlyNegative,
LikelyPositive.
Feedback Timestamp Date/Time Timestamp when the
feedback was submitted.
Gen AI Usage Log Reference Reference to the Gen AI
Usage Log.
Metadata Document Document ID Document ID for metadata
used for the requested
execution, if only a single
document is used.
Metadata Documents Glide List Document IDs for metadata
used for the requested

<!-- page 219 -->
Generative AI Log [sys_generative_ai_log] (continued)
Column Data type Description
execution, if multiple
documents are used.
Metadata Table Table Name Table name for the metadata.
Model Name String Name of the model used for
processing the generative AI
request, such as gpt_large,
claude_small, or gemini_small.
Model Version String Version of the ServiceNow
LLM model used.
Output Metadata String Metadata received from the
model or LLM, including
tokens, processing time, and
response time.
Prompt String Final prompt passed to the
model.
Prompt Config Reference Reference to the prompt
configuration, which contains
settings such as model and
temperature used in the
request to the LLM.
Prompt Token Count Integer Number of tokens used in the
prompt.
Response String The response generated by
the LLM.
Response Token Count Integer Number of tokens in the
response.
Skill Config Id Reference Reference to the skill
configuration.
Source String Source feature responsible
for the execution, such as
ChatSummary, Now Assist in
AI Search, or WWNA: Refine.
Started At Date/Time Timestamp when the
generative AI execution
started.
Status String Status of the AI log. Possible
values: Success, Error.
Target Language String Target language for the AI log.
Time Taken Integer Time taken for the AI log
process.
Untranslated Prompt String The untranslated version of
the prompt.

<!-- page 220 -->
Generative AI Log [sys_generative_ai_log] (continued)
Column Data type Description
Updated Date/Time Date and time when the log
entry was last updated.
Updated By String User who made updates to the
log.
Updates Integer Number of updates made to
the log record.
Gen AI Usage Log [sys_gen_ai_usage_log] table
Tracks each use of a Now Assist capability triggered from Workflow Studio, Virtual Agent
Designer topics, or scripts such as business rules and UI actions.
Gen AI Usage Log [sys_gen_ai_usage_log]
Column Data Type Description
Assists Integer Number of assists used or
consumed.
Created Date/Time Date and time when the log
entry was created.
Created By String Contains user information that
initiated the execution or flow.
Document Document ID Document ID for metadata
used for the requested
execution.
Document Table String Table name for the document
table.
Domain Domain ID Domain associated with the
execution that generated the
log entry.
Domain Path Domain Path Path associated with the
domain from where the
capability is executed.
Execution Type Choice Type of execution. Possible
values: Test, Evaluation, Auto
Prompt Tuning.
Feature Reference Source feature for the assist
usage.
Line Item Name String License line item name
associated with the assist
usage.
License Name String License name associated with
the assist usage.

> **[Screenshot: Generative AI Controller overview page]**
> The Generative AI Controller section within the ServiceNow AI platform documentation. Shows an introduction to the controller's role in managing connections to third-party LLM providers.

> **[Screenshot: Now Assist Admin console plugin installation page – repeated context]**
> Same three-card plugin selection layout (Technology, Customer, Employee) as shown on page 59.
>
> **[Screenshot: Configuring API credentials for generative AI capabilities – provider list]**
> A bulleted list of supported generative AI provider integrations: Amazon Bedrock, Azure OpenAI, Google – AI Studio, Google – Vertex AI, IBM watsonx, OpenAI, Generic third-party LLM. Each item is a blue hyperlink.

> **[Screenshot: Amazon Bedrock connection configuration procedure steps]**
> Step-by-step instructions visible in the documentation showing numbered steps for configuring Amazon Bedrock credentials in ServiceNow Connections & Credential Aliases.

> **[Screenshot: Azure OpenAI credential alias configuration]**
> Form or procedure screenshot showing Azure OpenAI credential configuration fields including endpoint URL, API key, and deployment name fields in the ServiceNow credential alias interface.