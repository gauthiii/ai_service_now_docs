## Solving Installation and Configuration Issues with Now Assist


For more information about supported LLM models, see Large language models on the
ServiceNow AI Platform.
Variations in search
®
The ServiceNow AI Platform offers a variety of search tools, which may return different answers
for the same or similar searches. This disparity in results is expected. For more information, see
the following topics:
•Discrepancies when using different AI search tools
•Search result disparities between AI Search and Now Assist search features
Solving installation and configuration issues with Now Assist
Use this checklist to address issues or gaps in your Now Assist configuration.
Common issues by Now Assist feature
Feature Issue Solution
AI agents I can't find Install the Now Assist for Spokes application from the ServiceNow
agent spokes Store. For details, see Now Assist for Integration Hub .
AI Control No data Verify that the Conversation Evaluator [sn_na_conv_eval] plugin
Tower on the is active. Also verify that the Smooth Flowing Conversation Chat
Evaluations Eval skill is active in the Now Assist Admin console. (This skill
tab may appear in the Platform workflow or in the Other workflow,
depending on your instance.)
AI Search External You can use External Content Connectors to include other
content isn't sources in your search results. For details, see External Content
included in Connectors .
search results
AI Search Now Assist
1.Verify that AI Search and Now Assist in AI Search are installed
in AI Search
and configured.
Genius
results don't 2. To use Now Assist Q&A Genius Results in AI Search
appear applications, link the Now Assist Q&A Genius Result
configuration to your search profiles for those applications.
For details, see Link a Genius Result configuration to a search
profile .
3. Verify that all Now Assist plugins are up to date.
4.Try repairing the plugins.
Knowledge I can't
1.Verify that Now Assist in Knowledge Management is installed
articles generate a
and configured.
knowledge
article 2. Verify that all Now Assist plugins are up to date.
3. Verify that the knowledge generation skill is activated. For
details, see Activate a Now Assist skill.
4.Try repairing the plugins.
© 2026 ServiceNow, Inc. All rights reserved. 35
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **Feature** | **Issue** | **Solution** |
|---|---|---|
| AI agents | I can't find agent spokes | Install the Now Assist for Spokes application from the ServiceNow Store. For details, see Now Assist for Integration Hub . |
| AI Control Tower | No data on the Evaluations tab | Verify that the Conversation Evaluator [sn_na_conv_eval] plugin is active. Also verify that the Smooth Flowing Conversation Chat Eval skill is active in the Now Assist Admin console. (This skill may appear in the Platform workflow or in the Other workflow, depending on your instance.) |
| AI Search | External content isn't included in search results | You can use External Content Connectors to include other sources in your search results. For details, see External Content Connectors . |
| AI Search | Now Assist in AI Search Genius results don't appear | 1.Verify that AI Search and Now Assist in AI Search are installed and configured. 2. To use Now Assist Q&A Genius Results in AI Search applications, link the Now Assist Q&A Genius Result configuration to your search profiles for those applications. For details, see Link a Genius Result configuration to a search profile . 3. Verify that all Now Assist plugins are up to date. 4.Try repairing the plugins. |
| Knowledge articles | I can't generate a knowledge article | 1.Verify that Now Assist in Knowledge Management is installed and configured. 2. Verify that all Now Assist plugins are up to date. 3. Verify that the knowledge generation skill is activated. For details, see Activate a Now Assist skill. 4.Try repairing the plugins. |

Common issues by Now Assist feature (continued)
Feature Issue Solution
Knowledge The KB Now Assist in Knowledge Management formatters may
articles generation be missing from the form layout, possibly due to form
popup customizations. For details, see KB1710178 .
doesn't
appear in
Core UI
Now Assist I want to See Product subscriptions overview .
applications view my
subscriptions
Now Assist Can't access
•Verify that the skill is configured to display in the Now Assist
panel skills in the
panel. For details, see Edit a Now Assist skill.
Now Assist
panel •If you are using Now Assist in Virtual Agent, verify that search
sources were configured for the Now Assist panel. You can
specify search sources for a Now Assist panel assistant when
you set it up. Search sources are essential for the Now Assist
panel and Virtual Agent. Without them, they cannot discover or
rank skills and agentic workflows. For details, see Configuring
assistants overview and Assign search sources to a chat
assistant .
If Now Assist in Virtual Agent is not installed, the Now Assist
panel uses default search sources.
Now Assist Some users Many Now Assist skills require specific user roles. Verify that
panel don't get a there are active skills with the user's role. For details, see Activate
response to a a Now Assist skill.
question
Now Assist I don't want Disable the Now Assist panel when you configure the skill. For
panel skills to be details, see Edit a Now Assist skill.
available in
Now Assist
panel
Now Assist Options for The sn_nowassist_admin.user role provides read-only access
panel Now Assist only. To make configuration changes, the user must have the
panel are sn_nowassist_admin.nsa_admin role.
grayed out
in the Now
Assist Admin
console
Now Assist Errors after Try repairing affected plugins. For details, see Repair a
setup clone ServiceNow application .
Now Assist The Q&A Set up AI Search. For details, see Configuring AI Search .
setup results skill
is not in
the Now
Assist Admin
console
© 2026 ServiceNow, Inc. All rights reserved. 36
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **Feature** | **Issue** | **Solution** |
|---|---|---|
| Knowledge articles | The KB generation popup doesn't appear in Core UI | Now Assist in Knowledge Management formatters may be missing from the form layout, possibly due to form customizations. For details, see KB1710178 . |
| Now Assist applications | I want to view my subscriptions | See Product subscriptions overview . |
| Now Assist panel | Can't access skills in the Now Assist panel | •Verify that the skill is configured to display in the Now Assist panel. For details, see Edit a Now Assist skill. •If you are using Now Assist in Virtual Agent, verify that search sources were configured for the Now Assist panel. You can specify search sources for a Now Assist panel assistant when you set it up. Search sources are essential for the Now Assist panel and Virtual Agent. Without them, they cannot discover or rank skills and agentic workflows. For details, see Configuring assistants overview and Assign search sources to a chat assistant . If Now Assist in Virtual Agent is not installed, the Now Assist panel uses default search sources. |
| Now Assist panel | Some users don't get a response to a question | Many Now Assist skills require specific user roles. Verify that there are active skills with the user's role. For details, see Activate a Now Assist skill. |
| Now Assist panel | I don't want skills to be available in Now Assist panel | Disable the Now Assist panel when you configure the skill. For details, see Edit a Now Assist skill. |
| Now Assist panel | Options for Now Assist panel are grayed out in the Now Assist Admin console | The sn_nowassist_admin.user role provides read-only access only. To make configuration changes, the user must have the sn_nowassist_admin.nsa_admin role. |
| Now Assist setup | Errors after clone | Try repairing affected plugins. For details, see Repair a ServiceNow application . |
| Now Assist setup | The Q&A results skill is not in the Now Assist Admin console | Set up AI Search. For details, see Configuring AI Search . |

Common issues by Now Assist feature (continued)
Feature Issue Solution
Now Assist Features/
•Verify that all of your Now Assist plugins are up to date.
setup skills are
For details, see Install an update to a ServiceNow Store
missing or
application .
generally not
working •Verify that version and dependency requirements are
met. For details, see Evaluating version requirements and
dependencies .
•For skills, verify that they are active in the Now Assist Admin
console. For details, see Activate a Now Assist skill.
•Verify that the user has the correct role for the skill.
•Try clearing the cookies and cache in the web browser.
•Try repairing Generative AI Controller. For details, see Repair a
ServiceNow application .
Now Assist Can't edit a
setup skill Verify that you have the Now Assist Admin role:
sn_nowassist_admin.nsa_admin.
You can edit a skill or make a copy of a skill to edit. For details,
see Edit a Now Assist skill and Make a copy of a Now Assist skill.
Now Assist Missing
•Verify that all of your Now Assist plugins are up to date.
setup entries, fields,
For details, see Install an update to a ServiceNow Store
and errors
application .
•Try repairing the application. For details, see Repair a
ServiceNow application .
•Try repairing Generative AI Controller. For details, see Repair a
ServiceNow application .
Now Assist Problems
•Verify that you have a license for the application.
setup upgrading
Now Assist •If the application was not previously installed, request it from
applications the ServiceNow Store (Opt In).
•If the application was previously installed, you may need to
procure it from the ServiceNow Store again. For details, see
Updating applications .
Now Assist Skills not Now Assist skills are not available in Legacy Workspace. Upgrade
setup working in to Service Operations Workspace to use Now Assist.
Legacy Agent
Workspace
© 2026 ServiceNow, Inc. All rights reserved. 37
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **Feature** | **Issue** | **Solution** |
|---|---|---|
| Now Assist setup | Features/ skills are missing or generally not working | •Verify that all of your Now Assist plugins are up to date. For details, see Install an update to a ServiceNow Store application . •Verify that version and dependency requirements are met. For details, see Evaluating version requirements and dependencies . •For skills, verify that they are active in the Now Assist Admin console. For details, see Activate a Now Assist skill. •Verify that the user has the correct role for the skill. •Try clearing the cookies and cache in the web browser. •Try repairing Generative AI Controller. For details, see Repair a ServiceNow application . |
| Now Assist setup | Can't edit a skill | Verify that you have the Now Assist Admin role: sn_nowassist_admin.nsa_admin. You can edit a skill or make a copy of a skill to edit. For details, see Edit a Now Assist skill and Make a copy of a Now Assist skill. |
| Now Assist setup | Missing entries, fields, and errors | •Verify that all of your Now Assist plugins are up to date. For details, see Install an update to a ServiceNow Store application . •Try repairing the application. For details, see Repair a ServiceNow application . •Try repairing Generative AI Controller. For details, see Repair a ServiceNow application . |
| Now Assist setup | Problems upgrading Now Assist applications | •Verify that you have a license for the application. •If the application was not previously installed, request it from the ServiceNow Store (Opt In). •If the application was previously installed, you may need to procure it from the ServiceNow Store again. For details, see Updating applications . |
| Now Assist setup | Skills not working in Legacy Agent Workspace | Now Assist skills are not available in Legacy Workspace. Upgrade to Service Operations Workspace to use Now Assist. |

Common issues by Now Assist feature (continued)
Feature Issue Solution
Now Assist Don't
•Verify that the skill is active. For details, see Activate a Now
for Code see code
Assist skill.
suggestions
•Verify that the user has the appropriate role. Any authenticated
builder can use the related active skill.
•Verify that autocomplete is enabled. For details, see Generate
code with autocomplete .
Now Assist Skills not
•Verify that the skill is active in the Now Assist Admin console.
for Creator available or
not working •Verify that the user has the appropriate role. Any authenticated
builder can use the related active skill.
Now Assist Now Assist
•Verify that you have at least one Now Assist product installed.
Skill Kit Skill Kit is not
For details, see Install Now Assist plugins.
visible on my
instance •Verify that the sn_skill_builder.admin role is assigned to the
user.
Now Assist Skills are Verify that the sn_skill_builder.admin role is assigned to the user.
Skill Kit read-only
Now Assist Topic not
•Verify that the Virtual Agent topic is in the Active state and is
in Virtual returning as
published. For details, see Publish a Virtual Agent topic .
Agent expected
•Verify that the topics are using LLM topic discovery. NLU/
keyword topics cannot be used in a portal that is using Now
Assist in Virtual Agent. You can migrate NLU/keyword topics to
LLM, however. For details, see Migrating NLU/keyword Virtual
Agent topics to LLM topics .
Now Assist Can't add Verify that the topics are using LLM topic discovery. NLU/keyword
in Virtual topics to the topics cannot be added to a portal that is using Now Assist in
Agent portal Virtual Agent. You can migrate these topics to LLM, however. For
details, see Migrating NLU/keyword Virtual Agent topics to LLM
topics .
Now Assist Configuration
1.Verify that the plugin is up to date. For details, see Install an
in Virtual issues
update to a ServiceNow Store application .
Agent
2. Follow the guided setup to install and configure it. For details,
see Configuring assistants overview .
Now Assist Unable to If you're using a custom fallback topic, this option may be
in Virtual choose unavailable in guided setup. For details, see KB1760362: Now
Agent fallback Assist Chat Setup Not Allowing to Set Fallback Option . You may
options in need to log in to view the article.
setup
© 2026 ServiceNow, Inc. All rights reserved. 38
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **Feature** | **Issue** | **Solution** |
|---|---|---|
| Now Assist for Code | Don't see code suggestions | •Verify that the skill is active. For details, see Activate a Now Assist skill. •Verify that the user has the appropriate role. Any authenticated builder can use the related active skill. •Verify that autocomplete is enabled. For details, see Generate code with autocomplete . |
| Now Assist for Creator | Skills not available or not working | •Verify that the skill is active in the Now Assist Admin console. •Verify that the user has the appropriate role. Any authenticated builder can use the related active skill. |
| Now Assist Skill Kit | Now Assist Skill Kit is not visible on my instance | •Verify that you have at least one Now Assist product installed. For details, see Install Now Assist plugins. •Verify that the sn_skill_builder.admin role is assigned to the user. |
| Now Assist Skill Kit | Skills are read-only | Verify that the sn_skill_builder.admin role is assigned to the user. |
| Now Assist in Virtual Agent | Topic not returning as expected | •Verify that the Virtual Agent topic is in the Active state and is published. For details, see Publish a Virtual Agent topic . •Verify that the topics are using LLM topic discovery. NLU/ keyword topics cannot be used in a portal that is using Now Assist in Virtual Agent. You can migrate NLU/keyword topics to LLM, however. For details, see Migrating NLU/keyword Virtual Agent topics to LLM topics . |
| Now Assist in Virtual Agent | Can't add topics to the portal | Verify that the topics are using LLM topic discovery. NLU/keyword topics cannot be added to a portal that is using Now Assist in Virtual Agent. You can migrate these topics to LLM, however. For details, see Migrating NLU/keyword Virtual Agent topics to LLM topics . |
| Now Assist in Virtual Agent | Configuration issues | 1.Verify that the plugin is up to date. For details, see Install an update to a ServiceNow Store application . 2. Follow the guided setup to install and configure it. For details, see Configuring assistants overview . |
| Now Assist in Virtual Agent | Unable to choose fallback options in setup | If you're using a custom fallback topic, this option may be unavailable in guided setup. For details, see KB1760362: Now Assist Chat Setup Not Allowing to Set Fallback Option . You may need to log in to view the article. |

Common issues by Now Assist feature (continued)
Feature Issue Solution
Now Assist Chat is not
•Verify that all of your Now Assist plugins are up to date.
in Virtual showing
For details, see Install an update to a ServiceNow Store
Agent search results
application .
•Verify that AI Search and Now Assist in AI Search are set up
and configured. For details, see Configuring AI Search and
Install Now Assist in AI Search .
•Verify that search sources were configured for the Virtual Agent
assistant. You can specify search sources for an assistant
when you set it up. Search sources are essential for Virtual
Agent and the Now Assist panel. Without them, they cannot
discover or rank skills and agentic workflows. For details, see
Configuring assistants overview and Assign search sources
to a chat assistant .
Now Assist Error when Verify that you have the correct role, either virtual_agent_admin
in Virtual attempting or sn_vad_genai.topic_migration_admin. For more information,
Agent to migrate see Migrate NLU topics to LLM topics .
Virtual
Agent NLU
conversations
to LLM
Now Assist AI assets
The Now Assist AI experience includes generative AI skills, AI agents, and AI agentic workflows.
These components work alone or in combination to help achieve efficiencies and results on your
instance.
© 2026 ServiceNow, Inc. All rights reserved. 39
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| **Feature** | **Issue** | **Solution** |
|---|---|---|
| Now Assist in Virtual Agent | Chat is not showing search results | •Verify that all of your Now Assist plugins are up to date. For details, see Install an update to a ServiceNow Store application . •Verify that AI Search and Now Assist in AI Search are set up and configured. For details, see Configuring AI Search and Install Now Assist in AI Search . •Verify that search sources were configured for the Virtual Agent assistant. You can specify search sources for an assistant when you set it up. Search sources are essential for Virtual Agent and the Now Assist panel. Without them, they cannot discover or rank skills and agentic workflows. For details, see Configuring assistants overview and Assign search sources to a chat assistant . |
| Now Assist in Virtual Agent | Error when attempting to migrate Virtual Agent NLU conversations to LLM | Verify that you have the correct role, either virtual_agent_admin or sn_vad_genai.topic_migration_admin. For more information, see Migrate NLU topics to LLM topics . |