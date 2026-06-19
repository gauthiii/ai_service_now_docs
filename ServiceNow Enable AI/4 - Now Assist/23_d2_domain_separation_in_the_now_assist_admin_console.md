# Domain separation in the Now Assist Admin console

_Source pages: 180–180 | Depth: 2_

---

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