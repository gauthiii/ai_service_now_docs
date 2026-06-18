# Troubleshoot a Now Assist skill

_Source pages: 184–184 | Depth: 2_

---

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