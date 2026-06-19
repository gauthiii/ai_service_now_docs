# Default and target model version

_Source pages: 179–179 | Depth: 2_

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