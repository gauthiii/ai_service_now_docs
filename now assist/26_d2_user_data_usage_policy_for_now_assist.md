# User data usage policy for Now Assist

_Source pages: 183–183 | Depth: 2_

---

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