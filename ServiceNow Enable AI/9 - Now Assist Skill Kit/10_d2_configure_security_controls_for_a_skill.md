### Configure security controls for a skill

*Pages 18–19 of the source PDF*

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


> **[Screenshot: Now Assist Skill Kit – ACL Role Selection Form (page 19)]**
>
> A form section in the Configure Security Controls procedure showing step 2d. The "User access * ⓘ" field has two radio options: ○ Any authenticated user | ● Select roles. Below: a "Roles *" search field (empty, with magnifying glass). Below the field, grey helper text: "Users with these roles can discover and use this skill in UI displays. Once you save these roles, an access control list (ACL) will automatically be generated."
