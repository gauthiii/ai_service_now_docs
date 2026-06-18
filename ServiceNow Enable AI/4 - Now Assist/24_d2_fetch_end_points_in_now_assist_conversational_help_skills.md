# Fetch end points in Now Assist Conversational Help skills

_Source pages: 181–181 | Depth: 2_

---

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