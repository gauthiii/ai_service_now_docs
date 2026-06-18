### Configure skill deployment settings

*Pages 16–17 of the source PDF*

4.On the form, fill in the fields.

Configurations form

5. Add Usage conditions to determine when to use the prompt.

What to do next After you configure your skill settings, you can test your skill. To learn more about testing skills, see Test a prompt.

To learn more about configuring the skill, including models and tokens, see Now Assist Skill Kit FAQs on the ServiceNow Community.

Configure skill deployment settings

Configure the deployment settings for the skill that you create. The deployment settings enable you to choose where the admin can find the skill in Now Assist Admin.

Before you begin Role required: sn_skill_builder.admin

Procedure

1.Navigate to > > Home. All Now Assist Skill Kit

2. Select the skill that you want to configure.

| Field | Description |
| --- | --- |
| Model | The model is the large language model (LLM) that you want to use for the prompt. |
| Temperature | The temperature determines the randomness and creativity of the output. A higher value increases the randomness. The value must be between 0-1. |
| Thinking mode | Thinking mode controls how much reasoning effort a large language model applies when it generates a response. Higher levels improve output quality but increase latency. You can select thinking mode when you use llm_generic_small_v2 or llm_generic_large_v2. |
| Maximum response tokens | The maximum number of tokens the model can return. If you’re using Now LLM Service, the maximum is 1000. |
| Maximum request tokens | The maximum number of tokens allowed in a request. |
| Structured output | Structured outputs return prompt responses in a consistent JSON format. Note: Only Google Gemini and Azure OpenAI support structured output. |

Select the tab. 3. Skill settings

4.Select information. General This section shows the information that you added when you created the skill. You can edit the skill name and description here.

5. Select Deployment Settings.

6.On the form, fill in the fields.

Deployment settings form

7.Select where you want the admin to enable the skill from.

| Field | Description |
| --- | --- |
| Workflow | The high-level category that this skill pertains to, such as Technology, Employee, Creator, or Platform. You can also select Other if none of the categories fit. The workflow that you choose is where the skill appears in the Now Assist Admin console. |
| Product | The specific product that this skill operates within, such as ITSM, ITOM, HR Service Delivery, Now Assist Admin. |
| Feature | The feature that the skill is used on, such as Agent Chat, Knowledge, Virtual Agent. You can also define a custom feature if necessary. |
| Name | The name of the feature. |
| Description | A description of the feature. |


> **[Screenshot: Now Assist Skill Kit – Deployment Touch-Point Selector 2×3 Grid (page 17)]**
>
> The 2×3 deployment activation grid (same as in file 07). Six cards with checkboxes: Now Assist panel | UI Action | Flow action (row 1); Now Assist context menu | Virtual assistants | UI Builder (row 2). Each card shows a mini UI illustration and a one-line description.
