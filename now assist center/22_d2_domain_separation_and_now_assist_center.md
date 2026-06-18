## Domain separation and Now Assist Center

> **Source document:** Now Assist Center  
> **Pages:** 71–71


Now Assist Center tables
Label Name
AI Tool
nac_aitool
Navigation Item nac_navigation_item
Now Assist Center Promoted Skill nac_promoted_skill
Now Assist Center Promoted Skills State nac_promoted_skill_state

### Domain separation and Now Assist Center

Domain separation is supported for Now Assist Center.
Domain separation allows you to separate data, processes, and administrative tasks into logical
groupings called domains. You can then control several aspects of this separation, including
which users can see and access data.

### Support level: Basic

- Business logic: Ensure data goes into the proper domain for the application’s service provider
(SP) use cases.
- In the application, the user interface, cache keys, reporting, rollups, aggregations, and so on,
all use domain at production run time.
- The owner of the instance must be able to set up the application to function across multiple
tenants.
For more information on support levels, see Application support for domain separation .

### Domain separation uses in Now Assist Center

- The system supports domain separation for skills and instructions.
- Ability to view domain-based skills in the actionable use cases on the home page.
- Ability to duplicate skills for different domains.
- Now Assist Center analytics data contains records from multiple domains.

### Tables

The following Now Assist Center tables contain domain-separated fields:
- nac_promoted_skill
- nac_promoted_skill_state

### Fields

The following domain-separated fields are supported:
- sys_domain
Associates the state record with a specific domain.
- sys_domain_path

| Label | Name |
| --- | --- |
| AI Tool | nac_aitool |
| Navigation Item | nac_navigation_item |
| Now Assist Center Promoted Skill | nac_promoted_skill |
| Now Assist Center Promoted Skills State | nac_promoted_skill_state |
