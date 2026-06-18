# Now Assist reference

_Source pages: 179–184 | Depth: 1_

---

<!-- page 179 -->
Now Assist reference
Reference topics include information about user roles, data usage, and domain separation for
Now Assist.
Default and target model version
Model version is the large language model version a skill uses to route requests to process users'
queries. Default model version is where all the requests route to by default. This is pre-set by
®
ServiceNow . A target model version is chosen to route your requests to a different version at
run-time, rather than using the default version.
Updating the target model version at the instance level
Note: A model version will not be available for selection as target model version, if it is in
deprecated, retired, in review or rejected state.
A default mapping of default and target model version is pre-configured. If you update the target
model version for a selected default model version, all the associated skills with this version
mapping at the current instance level, get impacted.

<!-- page 180 -->
Updating the target model version at the skill level
If you update the target model version for a selected default model version at the skill level,
the mapping is updated for that skill only. Customizing the model version for skills overrides
the instance-level model version currently assigned to each provider. This action is typically
reserved for specific situations.
Domain separation in the Now Assist Admin console
Domain separation is supported for the Now Assist Admin console. Domain separation enables
you to separate data, processes, and administrative tasks into logical groupings called domains.
You can control several aspects of this separation, including which users can see and access
data.
Support level: Basic
•Business logic: Ensure that data goes into the proper domain for the application’s service
provider use cases.
•The application supports domain separation at run time. The domain separation includes
separation from the user interface, cache keys, reporting, rollups, and aggregations.
•The owner of the instance must set up the application to function across multiple tenants.
Sample use case: When a service provider (SP) uses chat to respond to a tenant-customer’s
message, the customer must be able to see the SP's response.
For more information on support levels, see Application support for domain separation .
In the Now Assist Admin console, generative AI capabilities are organized into skills. Each skill
can be configured differently for each domain or you can create a variant of a skill for a domain.
By default, all skills exist in the global domain.
How domain separation works in the Now Assist Admin console
You must enable domain separation on your instance first before you can use it for Now Assist
skills.
Now Assist works with domain separation. When you use Now Assist in a domain-separated
environment, users are only able to access data within their domain. For example, if a user uses
the summarization skill, Now Assist only uses material that exists within the user's domain when
generating that summary. When a skill is domain separated, only users who are in that domain
can use the skill that you have configured for that scope.
If you're a service provider that hosts multiple clients in the same instance, you can set up
domain separation to separate tenant data, processes, and administrative tasks. However, Assist
consumption is tracked according to instance without differentiating between tenants. You can
track your Now Assist usage in the Subscription Management dashboard.
If you want a domain to have a different version of an existing skill, you can reconfigure and
activate the skill or create a variant in the preferred domain. See the section on granting access
to Now Assist skills to a domain.
Use cases
You can configure the inputs, roles, triggers, and prompts when you’re activating or editing a skill
or a later variant of the skill.

<!-- page 181 -->
Some use cases include the following examples:
•Use the Activity field as an input in the incident summarization in one domain but only use the
short description and description fields in another domain.
•Grant certain roles access to the Now Assist panel in one domain while another domain has no
role restrictions.
•Trigger the generative AI capabilities by using quick actions in Agent Chat in only one domain.
•Create a variant of a skill to test one prompt in one domain while another domain uses the
default prompt for the skill.
Granting a domain access to Now Assist skills
Domain separation is possible at the skill level and at the individual configuration level. When
using the guided setup in the Now Assist Admin console, each configuration option has its own
record that you can separate by domain. To create a record in a different domain, you must set up
the skill while in the scope of your preferred domain.
1.Navigate to the Now Assist Skill Config (sn_nowassist_skill_config) table.
2. Add the Domain field to the list. If it isn't present, select the gear icon at the top of the list and
add the Domain field into the Selected column, then select OK.
3. Find the skill that you want to enable on a domain-by-domain basis. Set Active to false on the
skill that is in the global scope. You might need to change the scope to edit the record.
4.Change your current domain to the domain that you want to enable the skill in.
5. Navigate to All > Now Assist Admin Console > Features.
6.Navigate to the skill that you want to activate according to domain and select Activate skill.
7.Configure the skill as usual. For more information, see Activate a Now Assist skill.
8.Return to the Now Assist Skill Config (sn_nowassist_skill_config) table. There should be a new
record in the current domain. Open the new record.
9.In a different browser tab, return to the Now Assist Skill Config table and open the deactivated
skill record in the global domain.
10.Compare the global skill record to the one created within your domain. Records on the related
list may not be present in the domain-specific skill. If they are not there, you must recreate
those records in your domain and attach them to the related list in your domain-specific skill.
11. Repeat the process for each skill and each domain where you want to have the skill available.
Related topics
Domain separation for service providers
Fetch end points in Now Assist Conversational Help skills
The Now Assist Conversational Help skills architecture solves latency by fetching answers
hosted at the nearest location, which is best suited to the user.
Fetching solutions hosted on multiple geographical location
The Now Assist Conversational Help skill displays as Get Help on the Now Assist panel. The
possible solutions to users queries posted on Now Assist Conversational Help skills are hosted
on three main locations: Japan, EMEA and the US.
Note: To preserve data privacy standards, end points support for Get Help skill is not
available in GCC/ NSC regulated markets.

<!-- page 182 -->
For optimal performance, the central instance should be situated in the same geographic area
as the user's instance. To achieve this alignment, we utilize DISH service, a tool within the user's
instance, that helps identify the correct endpoint. The Now Assist Conversational Help skills uses
the Mimir lookup service feature, inside the different data centers.
The DISH service communicates with the Mimir lookup table to determine the end points
matching the user's location. Once we obtain this endpoint, it gets securely stored in the sys-
service table within the customer instance. Moving forward, all the users' queries are routed
through the specific endpoint, ensuring consistency and reliability. The Get Help skill uses the
endpoint present in the sys-property com.snc.get_help.endpoint.
Note: The Now Assist Conversational Help skill version is stored in
sn_ads_now_help.com.snc_now_help_skill.version, ensuring backward compatibility within
the conversational shared services.
Now Assist Admin roles
Certain roles are required to use Now Assist Admin functionality.
Now Assist Admin [sn_nowassist_admin.nsa_admin]
This user can create and update the Now Assist Admin experience by editing and configuring
skills.
Contains Roles
List of roles contained within the role.
ACE User [ace_user].
Groups
List of groups this role is assigned to by default.
None.
Special considerations
Avoid granting an admin role when more specialized roles are available.
Now Assist Admin console user [sn_nowassist_admin.user]
This user can access the console and view skills and their configurations, but cannot make edits.
Contains Roles
List of roles contained within the role.
None.
Groups
List of groups this role is assigned to by default.
None.
Special considerations
None.

<!-- page 183 -->
Now Assist panel user [now_assist_panel_user]
Users who have access to the Now Assist panel.
Contains Roles
List of roles contained within the role.
None.
Groups
List of groups this role is assigned to by default.
None.
Special considerations
None.
User data usage policy for Now Assist
Now Assist is designed to keep user data safe and secure. You can also mask sensitive data or
opt-out of sharing data for model improvements.
How your data is sent and stored
Your AI workloads are securely sent using Transport Layer Security (TLS) 1.2 from your
ServiceNow instance to one of three centralized ServiceNow compute hubs (datacenters
with GPUs for AI workloads), where the AI prediction processing takes place. The data used
to generate the response is deleted from the compute hubs after the response has been
generated. The result is then returned to the ServiceNow instance.
The input and output data isn’t cached or stored on the compute hub and is transient.
Your data isn’t commingled with other customer data when using Now LLM Service for generative
AI.
Also, there’s no commingling of data for domain-separated instances when you use Generative
AI services.
When appropriate, ServiceNow might leverage third-party endpoint services (for example Azure
OpenAI Service) to augment Now LLM Service to power Now Assist capabilities. Azure OpenAI
is a third-party model, but policies same as the company's, apply, as it's hosted in our compute
hubs.
Further, to confirm quality of service, ServiceNow might use Azure-hosted GPUs for Now LLM
Service capacity bursting in case of high customer demand. Data processed by third-party
endpoints isn’t subject to use or access by third-party providers and are operated within the
ServiceNow network boundary.
Mask sensitive data
Sensitive data can be masked before sending it to LLMs using Now Assist for Data Privacy. To
learn more, see Configuring Data Privacy for Now Assist .
After you enable the plugin, it’s designed to mask sensitive data before it’s sent to the LLM, but
could result in less accurate results because the specific data isn’t included within the prompt.

<!-- page 184 -->
Note: This plugin, within the context of generative AI products, doesn’t mask the sensitive
data that exists in records within your instance, nor does it help prevent new sensitive data
from being stored on the instance itself.
ServiceNow might use Retrieval Augmented Generation (RAG) for selected AI features (for
example NowAssist for AI Search) and passes information to the LLM based on what the
requester can access within the system. If a user searches for something in the portal using Now
Assist in AI Search, AI Search finds the article and then sends that to the LLM as a part of the
prompt. Because AI Search knows what the user has access to, it won't send an article that the
user isn't able to access.
Note: For some features, such as case summarization, the agent generating the summary
might have more permissions than other people who have access to the record. If they
choose to paste that summary to the work notes, the agent should check to confirm that the
data they're sharing in the work notes is appropriate to share with others who have access
to that record.
Opt out of data sharing
Data Sharing helps ServiceNow to continuously advance and improve its Now LLMs, based on
the latest customer usage. If you no longer want to participate in the customer data-sharing
program, you’re able to opt out.
To opt out, follow the instructions in Opt out of data sharing for Now Assist.
Troubleshoot a Now Assist skill
Run diagnostics for a skill on the Now Assist Admin console and get information about the status
of your skill configuration.
Before you begin
Role required: sn_nowassist_admin.nsa_admin
About this task
Certain skills have diagnostic scripts that you can run from the Now Assist Admin console. These
diagnostic scripts check for successful skill execution and setup of the underlying capability
definitions. If you've made a copy of a skill, you will not be able to run diagnostics on the skill
copy.
Procedure
1.Navigate to All > Now Assist Admin > Features.
If you’re already in the Now Assist Admin console, select the Now Assist Features tab.
2. In the navigation pane, select the workflow of the skill that you want to troubleshoot, such as
Technology or Customer.
3. On the feature card that contains the skill you want to troubleshoot, select View details.
4.In the All available skills or Active skills section, select the more options icon next to the
skill that you want to make a copy of and select Run diagnostics.
Run diagnostics is greyed out for skills where this option is not available or applicable.