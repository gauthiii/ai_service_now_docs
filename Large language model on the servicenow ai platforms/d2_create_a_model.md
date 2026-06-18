# Create a model

*Source: document pages 127–129 (PDF chunk pages 27–29)*

---



<!-- doc page 127 -->

For more information on differences in ServiceNow AI results, see Search result disparities
between AI Search and Now Assist search features .
Example: Now LLM Service response vs. Azure response
The difference in responses by Now LLM Service and Azure for information about
tuition reimbursement
Providers and Models
You can bring your own large language model (LLM) provider and API to use with Now Assist.
Bringing your own large language model enables:
•Data Privacy & Compliance: Keep sensitive data within your own environment and meet
regulatory requirements.
•Customization: Fine-tune models for domain-specific needs and control behavior.
•Integration Flexibility: Connect easily with existing infrastructure and preferred cloud providers.
•Cost Control: Use existing contracts and optimize resource usage to avoid extra charges.
•Strategic Autonomy: Maintain vendor neutrality and avoid lock-in for future-proofing.
Create a model
You can create a custom large language model (LLM) using ServiceNow models or models from
different providers.
Before you begin
Role required: sn_skill_builder.sb_model_admin
Procedure
1.Navigate to All > Now Assist Skill Kit > Providers and Models.
2. Select Add model.
3. On the form, fill in the fields.

ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.


<!-- doc page 128 -->

Add a model form
Field Description
Model name A name for the model
Max tokens Max response + max request tokens
Supported languages The languages that are supported
Provider The provider of the LLM
API The API you are using from the provider
4.Select Continue.
5. Enter credential details
Add credentials form options
Model Steps
Custom LLM provider
a.Select Create.
i. Connection name
ii.Connection URL
iii. Credential type
iv.API key
b.Select Select from database and select
from the dropdown menu.

ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| Field | Description |
| --- | --- |
| Model name | A name for the model |
| Max tokens | Max response + max request tokens |
| Supported languages | The languages that are supported |
| Provider | The provider of the LLM |
| API | The API you are using from the provider |


| Model | Steps |
| --- | --- |
| Custom LLM provider | a.Select Create. i. Connection name ii.Connection URL iii. Credential type iv.API key b.Select Select from database and select from the dropdown menu. |



<!-- doc page 129 -->

Model Steps
Add the connection URL and API key.
◦IBM Watson
◦Now LLM Service
◦Open AI
◦Perplexity
6.Select Continue.
7.If you created a custom LLM provider, add transformer information.
Transformer information form
Option Steps
Existing Select a transformer template:
◦Default
◦Hugging face
◦Google Gemini
◦Claude
Create Add transformer request and response
information for your model.
Note: If you didn't select a custom LLM provider, request and response transformers are
set by the system.

ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| Model | Steps |
| --- | --- |
| ◦IBM Watson ◦Now LLM Service ◦Open AI ◦Perplexity | Add the connection URL and API key. |


| Option | Steps |
| --- | --- |
| Existing | Select a transformer template: ◦Default ◦Hugging face ◦Google Gemini ◦Claude |
| Create | Add transformer request and response information for your model. |
