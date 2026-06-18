### Create a skill

*Pages 21–24 of the source PDF*

Create a skill

Create a custom skill for Now Assist. Creating a custom skill enables you to have greater flexibility with Now Assist's generative AI capabilities.

Before you begin Role required: sn_skill_builder.admin

Note: When you update Now Assist Skill Kit you should also update Generative AI Controller to ensure that your skills continue to perform correctly.

Procedure

1.Navigate to > > Home. All Now Assist Skill Kit

2. Select Create new skill.

3. On the form, fill in the fields.

New skill form

Default provider Available providers:

◦Now LLM Service

◦External LLM

You can use Now LLM Service, Now LLM Long Term Stable models (LTS), Azure OpenAI, Google Gemini or Anthropic Claude on AWS as the AI model provider for all Now Assist skills and AI agents. Use the Configuration Controls in AI Control Tower to define which options are available,

| Field | Description |
| --- | --- |
| Skill name | A name for the skill. |
| Description | A description of the skill. |

4.Select how you want to create the prompt for the skill.

◦Write from scratch

◦Choose one from library

| Field | Description |
| --- | --- |
|  | then set the skill-level preferences in the Now Assist Admin console. For more information, see Large language models on the ServiceNow AI Platform. ▪Spokes ▪Custom LLM For more information on setting up a custom large language model (LLM), see Configure a generic large language model (LLM) connector Available prebuilt spokes that enable you to connect with an external LLM: ◦Microsoft Azure OpenAI Generative AI Spoke ◦OpenAI Generative AI Spoke ◦Aleph Alpha ◦WatsonX ◦Google Gemini (MakerSuite and Vertex AI) Note: The spokes don't consume Integration Hub transactions. The spokes consume assists. |
| Provider API | The provider of the API for your chosen LLM. |
| User access | ◦Any authenticated user As long as a user is logged in, they can access and execute the skill. ◦Select roles Select the roles that a user must have to execute the skill. Note: If you select multiple roles, a user must only have one of the roles to execute the skill. |
| Role restrictions | Role restrictions define the specific roles under which a skill in ServiceNow executes. While ACLs determine which user roles are permitted to trigger the skill, role restrictions determine the roles the skill will operate with during execution. |

a.Find the prompt that you want to use.

b.Select View.

c.Select Use prompt.

◦Use an AI-generated prompt

Select Next. 5.

6.Optional: Add skill inputs and outputs.

7.Select Go to summary.

8.Select Finish.

What to do next After you create the skill, you must configure it. To learn more about configuring a skill, see Configure a skill prompt.

If you don't need to set any configurations for your skill, you can create your skill prompt and tools. To learn more, see Create a prompt and Add a tool.

Clone and edit a ServiceNow skill

Eligible skills provided in ServiceNow Now Assist applications can be cloned in Now Assist Skill Kit so that you can edit the prompt or change the AI service provider. Editing the prompt enables you to arrange the formatting and content of the LLM response.

Before you begin Role required: sn_skill_builder.admin

Procedure

1.Navigate to All > Now Assist Skill Kit > Home.

Select ServiceNow 2. skills

Select the ServiceNow skill that you want to clone. 3.

4.Select Clone Skill.

Fill in the fields on the form. 5.

Clone skill form

6.Select Clone.

Note: When you clone a skill, you can't change the skill outputs, tools, or deployment settings.

7.Select the edit or add icon to add skill inputs.

Add skill inputs form

| Field | Description |
| --- | --- |
| Skill name | A name for the skill. |
| Description | A description of the skill. |
| Default provider | Available providers: ◦Now LLM Service ◦External LLM ▪Spokes ▪Custom LLM For more information on setting up a custom large language model (LLM), see Configure a generic large language model (LLM) connector Available prebuilt spokes that enable you to connect with an external LLM: ◦Microsoft Azure OpenAI Generative AI Spoke ◦OpenAI Generative AI Spoke ◦Aleph Alpha ◦WatsonX ◦Google Gemini (MakerSuite and Vertex AI) Note: The spokes don't consume Integration Hub transactions. The spokes consume assists. |
| Provider API | The provider of the API for your chosen LLM. |

| Field | Description |
| --- | --- |
| Dataype | Select the datatype for the input. |
| Name | The name of the skill input. |
| Description | A description of the skill input. |
| Make input mandatory check box | Select this box if the input must be provided for the skill to run. |


> **[Screenshot: Now Assist Skill Kit – New Skill Modal (page 21)]**
>
> White modal dialog titled "New skill" (✕ top-right). Fields:
> - "Skill name *" — "Child Incident Summary"
> - "Description" — "Summarize child incidents"
> - Unchecked checkbox: "Use the description above to recommend an AI generated prompt (powered by Now LLM Generic)"
> - "Default provider *" dropdown: "Now LLM Generic"
> - "Provider API *" dropdown: "Now LLM Generic"
> Buttons: "Cancel" (grey) | "Create skill" (teal)

> **[Screenshot: Now Assist Skill Kit – Create Skill Prompt Source Selection (page 23)]**
>
> A white form section showing the prompt creation selection step. Three radio options horizontally: ○ Write from scratch | ● Choose one from library (selected) | ○ Use an AI-generated prompt.
>
> Below: a search bar ("🔍 Search") and a "Providers: Now LLM Generic ▼" filter.
>
> Two prompt library cards shown side by side:
> - **Left card**: "Record Summarization" | badge "Now LLM Generic" (teal) | Title: "Record Summarization New Improved" | Status badge: "Published" (green) | Author: "Abel Tuter" | Modified: 2025-01-10 06:56:58 | Preview text snippet | **"View"** button
> - **Right card**: "Essential Prompt Templates" | badge "Now LLM Gen..." (truncated) | Title: "Chain of thought prompt" | Status badge: "Finalized" (grey) | Author: "System Administrator" | Modified: 2024-09-18 07:16:54 | ▶ expand button | Preview text snippet | **"View"** button
>
> Footer note: "The library prompt is based on your skill details. You can use it now or explore more options later in the 'Prompt assistance' section."
