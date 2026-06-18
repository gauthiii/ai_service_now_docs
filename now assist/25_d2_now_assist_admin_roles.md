# Now Assist Admin roles

_Source pages: 182–182 | Depth: 2_

---

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