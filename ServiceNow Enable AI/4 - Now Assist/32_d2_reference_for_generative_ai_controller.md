# Reference for Generative AI Controller

_Source pages: 214–216 | Depth: 2_

---

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