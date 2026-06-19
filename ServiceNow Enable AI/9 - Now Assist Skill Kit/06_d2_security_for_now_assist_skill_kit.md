### Security for Now Assist Skill Kit

*Pages 14–14 of the source PDF*

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
