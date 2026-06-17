# Configure Group Action Framework

_Source pages: 39–43 | Depth: 2_

---

<!-- page 39 -->
Procedure
1.Navigate to All > AI Agent Studio > Create and manage > AI agents.
2. Navigate to the Define the specialty page of an AI agent form.
Note: You can add map the categories for a new or existing AI agent.
3. In the manage long-term memory section, select categories that you want to map to your AI
agent.
You will see the list of categories that were created in the AI Agent Memory Categories page.
For more information, see Create long-term memory category.
4.Select Save and continue.
Result
The selected categories are mapped to your AI agent.
Configure Group Action Framework
Set up Group Action Framework (GAF) to improve the response quality, recall speed, and
consistency of AI agents.
Before you begin
There must be a ml_platform read ACL for GAF to be configured. If there is no read ACL
present, you must create it and grant the appropriate role access, such as admin, ml_admin, or
sn_aia.admin. This is required for GAF to access Machine Learning tables and services. If your
ACL is not configured correctly, you may see the error "Failed to initialize pipeline: Failed to load
message_content dataset. No columns to parse from file."
To access GAF's optimized prediction feature, you can enable Now Assist in AI Search. For more
information, see Setup AI Search for Group Action Framework.
Role required: sn_aia.admin
About this task
You can activate GAF to have AI agents use indexed clusters that perform LLM executions on
representative records rather than all records. GAF is used by some AI agents and agentic
workflows to work optimally. For more information about GAF and how it works, see Group Action
Framework.
You can have different GAF configurations for different agentic workflows and Now Assist
applications. You must configure each agentic workflow or application separately.

<!-- page 40 -->
Important: Setting up GAF can take some time, between 10 minutes up to an hour,
depending on the number of records in the grouping. The script runs in the background.
Procedure
1.Navigate to All > System Definition > Scripts - Background.
2. Paste the following code into the text area.
Do not run the script until the groupSkillID and the actionSkillID variables have values. The
values are acquired in the following steps.
var groupSkillId = "";
var actionSkillId = "";
var topicSkillId = "43bce9e477e012103f075cea5b5a998f";
new sn_gaf.GAFUtils().activate(groupSkillId, topicSkillId,
actionSkillId, "run_once");
The topicSkillId is the same for all GAF setups.
3. In a new browser tab, navigate to the Now Assist Skill Config [sn_nowassist_skill_config] table
by entering sn_nowassist_skill_config.list in the filter navigator.
4.In the Name field, enter *grouping and search to see the grouping records that are
associated with your agentic workflows and Now Assist applications.
5. Open the grouping record for the agentic workflow or application that you want to configure.
6.In the Now Assist Config Var Set related list, open the Grouping inputs record.
7.Confirm that the filters for the grouping include all the records you want to index.
If you want to add filters to change what records are included in the GAF setup, do so here.
The more records that you include means that you have a longer setup time, but they can
help increase the quality of your results. You should have at least 2000 records for successful
clustering.
Note: Your current scope should be Group-Action Framework to make changes.

<!-- page 41 -->
8.Return to the Now Assist Skill Config Grouping record and copy the sys_id.
You use this sys_id and two other sys_ids in the background script function call.
9.In the browser tab with the background script, paste the sys_id in the script between the
quotation marks for the groupSkillId variable.
Your groupSkillId variable should be in the same format as the topicSkillId variable.
10.In the tab with the Now Assist Skill Config record, return to the Now Assist Skill Config table and
search for *action strategy to find the action strategy skill config for the application.
Make sure that the record is for the same application. If you pasted the sys_id of the GAF ITSM
grouping, you must open the GAF ITSM action strategy.
11. Open the action strategy record for the application that you’re configuring.
12. Copy the sys_id of the action strategy record.
13.In the browser tab with the background script, paste the sys_id in the script between the
quotation marks for the actionSkillId variable.
Your actionSkillId variable should be in the same format as the groupSkillId and
topickillId variables.
14.Run the background script by selecting Run script.
Running this background script creates a scheduled job called GAF - Run Offline Flow. You can
view the scheduled job on the Scheduled Script Executions [sysauto_script] table.

<!-- page 42 -->
Result
GAF is configured on your instance for that Now Assist application and can be used by AI agents
to find related records.
What to do next
To verify that grouping and action outputs have been generated, go to the ML Solution
[ml_solution] table to check if the clustering solution is running or completed. If it is complete,
check the following tables to see records for groups, clustered records, and down-sampled
records per group are present.
•GAF record group [sn_gaf_record_group]
•GAF record group detail [sn_gaf_record_group_detail]
•GAF action strategy result [sn_gaf_action_strategy_result]
You can repeat this procedure for additional agentic workflows and Now Assist applications.
You may see the error "Failed to initialize pipeline: Failed to load message_content dataset. No
columns to parse from file." when trying to configure GAF. This could be because your instance
lacks data on the table or filters you configured excluded records from the table. You can reach
out to Now Support for additional assistance if you cannot resolve this error.
Set up AI Search for GAF
Configure AI Search to enable Group Action Framework (GAF) to improve quality and
consistency of agentic AI and Now Assist generative AI on the Now Platform.
Before you begin
Role required: admin
About this task
GAF is a feature on the Now Platform that clusters and indexes related records and executes
actions on them in agentic AI and Now Assist generative AI. See Group Action Framework for
more information about GAF's role in intelligent experiences and how it works.
Now Assist in AI Search is the foundation for GAF's optimized prediction feature. AI Search is the
backup search for certain workflows, and if it is not enabled and ready, GAF will not return any
results.
You must index every table for each workflow or application you'd like to configure GAF for. For
example, if you are configuring GAF for Now Assist for IT Service Management (ITSM), you must
index the Incident and related tables.
Procedure
1.Navigate to All > AI Search > AI Search Status.
If you see “AI Search is ready,” proceed. If not, request AI Search installation, which can take 2–
24 hours.
2. Install Now Assist for AI Search by installing a Now Assist application.
For more information, see Install Now Assist in AI Search .
3. Navigate to the Now Assist Skill Config [sn_nowassist_skill_config] table by entering
sn_nowassist_skill_config.list in the filter navigator.
4.Search the Now Assist Skill Config table for action strategy skills by searching Name is
*action strategy, and select the action strategy skill for the application you want to
configure.

<!-- page 43 -->
For example, if you are configuring GAF for Now Assist for ITSM, select the GAF ITSM action
strategy record.
5. In the related list, select the Now Assist Skill Config Var Set record.
6.Set Semantic Index Name to the appropriate field for your table.
To find the field for your table, go to the Semantic Index
Configuration [ais_semantic_index_configuration] table by entering
ais_semantic_index_configuration.list in the filter navigator, filter the
Indexed Source for the table you want to index, and use the value in the Name field. For
example, the value is body for the Incident table.
7.Navigate to the Semantic Index Configuration [ais_semantic_index_configuration] table by
entering ais_semantic_index_configuration.list in the filter navigator, filter the
Indexed Source for the table you want to index and the Semantic Index Name you
configured in the previous step, and set Active to true to activate the embedding model.
8.Navigate to All > AI Search > AI Search Index > Indexed Source, filter the list so that the Name
is the name of the table you are configuring, and select the record.
9.Select Index All Tables.
Result
The tables for Now Assist in AI Search for your Now Assist application is indexed based on the
appropriate field.
What to do next
To confirm that indexing has occurred successfully, check the Indexed Source History related
list and ensure that both the Keyword Ingestion State and Semantic Ingestion
State are both set to Indexed.
Once your tables have been indexed, you can continue to Configure Group Action Framework to
set up GAF for each application.