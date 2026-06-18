## Configuring Now Assist Skill Kit

*Pages 14–19 of the source PDF*

Activate the skill

After you test, finalize, and publish your skill, an admin must activate it in Now Assist Admin. To learn more about activating skills, see Activate a skill.

Security for Now Assist Skill Kit

Enable security controls for Now Assist skills and custom skills through access control lists (ACLs) and role restrictions.

Access control lists

The access control lists in Now Assist Skill Kit enhance the security of Now Assist skills and are set to determine users who can invoke a skill.

Configure ACLs in Now Assist Skill Kit

You can configure ACLs for Now Assist Skill Kit when you create or edit a skill or when you activate a skill from Now Assist Admin console.

ACLs configured in Now Assist Skill Kit for are Allow-If and role-based.

The Allow-If logic grants access to data or resources if any of the conditions in the ACL are met. The other type of ACL is Deny-Unless. Deny-Unless ACLs block access to data or resources unless a condition is met, even if there are other conditions like Allow-If ACLs that would normally grant someone access.

There are two possible options for ACLs created in Now Assist Skill Kit:

•Any authenticated user: Grants access to any user authenticated on the instance, regardless of role

•Select roles: Requires you to select the roles that grant access

Each skill must have its own unique ACL. You can't create a skill or save changes to a skill without an ACL. To configure an ACL for a skill, see Configure security controls for a skill.

Role restrictions

Role restrictions define the specific roles under which a skill in ServiceNow executes. While ACLs determine which user roles are permitted to trigger the skill, role restrictions determine the roles the skill will operate with during execution.

For example, if a skill has and ACL of itil-admin and a role restriction of itil, only users with the itil_admin role can trigger the skill. However, when the skill is executed, it will execute with the permissions and access of the itil role.

Role restrictions for skills enhances security by enabling users to limit their users during skill execution, verifying that skills run with least-access privileges.

To configure role restrictions for a skill, see Configure security controls for a skill.

Configuring Now Assist Skill Kit

Configure prompts and skills for Now Assist Skill Kit.

Configuration overview

To use Now Assist Skill Kit, you must update your Now Assist plugins in the Application Manager . For example, update your Now Assist for ITSM plugin to the Xanadu release.

After you install the plugin, there are two parts to configuring a skill in Now Assist Skill Kit. First, you must configure how to deploy the skill. Next, you must configure the prompt.

Configure a skill prompt

Configure your skill prompt to set the model that is used and the randomness and creativity of the response.

Before you begin Role required: sn_skill_builder.admin

Procedure

1.Navigate to All > Now Assist Skill Kit > Home.

Select the skill that you want to configure. 2.

Select Configurations. 3.

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

◦Now Assist Panel

◦UI Action

◦Flow action

◦Now Assist context menu

◦Virtual assistant

For more information about Now Assist in Virtual Agent, see Configuring assistants overview .

◦UI Builder

8.Select Save.

What to do next After you configure the skill settings, you can publish your skill. To learn more about publishing skills, see Finalize and publish a skill

Example deployment with Workflow Studio

As an AI developer, you can deploy custom skills with many integrations, including Workflow Studio.

Deploy a skill with Workflow Studio

Before you can deploy a skill, you must complete the following steps:

1.Create the skill.

Create the prompt. 2.

To deploy the skill:

1.Navigate to settings. Skill

Select settings. 2. Deployment

3. Select a workflow.

4.Select a product

Select a feature. 5.

6.Select where you want the admin to enable the skill from. For this example, select Workflow Studio.

Execute the skill

To execute the skill:

1.Finalize and publish the skill.

Activate the skill. 2.

3. Navigate to Workflow Studio.

4.Add the Execute Skill action .

Configure security controls for a skill

You must define an access control list (ACL) and role restrictions for all skills. An ACL enables you to restrict who is able to access and execute a skill to only users with the correct role. Role restrictions enable users to limit roles during skill execution.

About this task If you have an existing skill that does not have an ACL, the execution of the skill is not disrupted. However, if you edit the skill and republish it, you must add an ACL.

If you try to execute a skill when you don’t have permission, you see an error that you aren’t authorized.

Before you begin Role required: sn_skill_builder.admin

Procedure

1.Navigate to All > Now Assist Skill Kit > Home. A modal appears to explain ACLs. You can select or ACLs. Got it View skills without

2. Add an ACL and role restrictions to an existing skill.

a.Select the skill that you want to add an ACL to.

b.Select the tab and then select controls. Deployment and skill settings Security

c.Select Add ACL.

d. Select an option.

Options for ACL roles

e. Add role restrictions.

f.Select Apply.

Add an ACL to a new skill. 3.

a.Create a skill.

b.In the Configure security controls section, select an option for the access control list.

| Option | Description |
| --- | --- |
| Any authenticated user | As long as a user is logged in, they can access and execute the skill. |
| Select roles | Select the roles that a user must have to execute the skill. Note: If you select multiple roles, a user must only have one of the roles to execute the skill. |


> **[Screenshot: Now Assist Skill Kit – Configure Skill Prompt / Configurations Panel (page 15)]**
>
> (Same panel as described in the Example use case file.) Vertical Configurations panel with Provider = Now LLM Generic, Model = llm_generic, Temperature = 0.2, Max response tokens = 1000, Max request tokens = 6942. Usage conditions section at the bottom.

> **[Screenshot: Now Assist Skill Kit – Deployment Touch-Point Selector (page 17)]**
>
> A white section titled "Select where you'd like to let the admin activate the skill". A 2×3 grid of deployment option cards, each with a checkbox, a title, a greyscale/colour mini-UI mockup, and a short description:
>
> **Row 1:**
> - ☐ **Now Assist panel** — mockup: side panel with chat bubbles and a green sparkle panel icon. Description: "Allow this skill to be triggered through the Now Assist Panel"
> - ☐ **UI Action** — mockup: form with a teal/green highlighted button on the right of a page. Description: "Adds a UI action button to the core UI, to trigger the skill"
> - ☐ **Flow action** — mockup: a flow-diagram canvas with node icons and connectors. Description: "Allow the skill to be used from a flow action. Once activated, you can access the skill through 'Execute Skill' flow action."
>
> **Row 2:**
> - ☐ **Now Assist context menu** — mockup: a rich-text editor toolbar with a green plus/sparkle button in the margin. Description: "Make the skill available for activation and use through the Now Assist context menu."
> - ☐ **Virtual assistants** — mockup: a chat interface window with a sparkle/wand icon. Description: "Make the skill available for activation and use in various chat experiences with virtual assistants."
> - ☐ **UI Builder** — mockup: a page-builder canvas with component placeholders and blue dashed outline. Description: "Make the skill available for activation in experiences designed with the Now Experience UI Builder."

> **[Screenshot: Now Assist Skill Kit – Configure Security Controls / ACL Form (page 19)]**
>
> A white form section showing step 2d of ACL configuration. Header: "User access * ⓘ". Two radio buttons:
> - ○ Any authenticated user  ● Select roles (filled/selected)
>
> Below: "Roles *" — empty search field with magnifying glass icon. Light-grey note: "Users with these roles can discover and use this skill in UI displays. Once you save these roles, an access control list (ACL) will automatically be generated."
