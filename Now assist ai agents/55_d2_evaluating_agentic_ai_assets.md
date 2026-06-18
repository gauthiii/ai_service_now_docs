# Evaluating agentic AI assets

_Source pages: 201–223 | Depth: 2_

---

<!-- page 201 -->
Prioritize the evaluation metrics that most closely align with your business
objectives and user requirements. Not all metrics carry equal weight for your
specific use case.
Investigate unexpected results
When evaluation results differ significantly from expectations, investigate the
identified issues and their traces. This might reveal issues with the agentic AI asset
configuration, data quality, or evaluation setup.
General guidelines for effective evaluation
Follow these general guidelines to maximize the value of your agentic evaluation efforts and
ensure reliable results.
Establish baseline performance metrics
Create baseline measurements when you first deploy your agentic AI assets. These
baselines provide reference points for comparing future evaluation results and
tracking improvements.
Monitor evaluation performance over time
Track how your evaluation processes themselves perform over time. This
includes evaluation run times, resource usage, and the reliability of the evaluation
infrastructure.
Validate evaluation methods periodically
Periodically review and validate your evaluation methods to ensure they continue to
provide meaningful insights. Update methods as your agentic AI assets evolve and
requirements change.
Evaluating agentic AI assets
Find guidance for every stage of the agentic evaluation lifecycle, from initial setup to
reevaluation.
Overview of agentic evaluations
To evaluate your agentic AI at scale, follow the workflow described below:
1.Create your first automated evaluation run.
Get acquainted with the agentic evaluations homepage and the guided setup for an
automated evaluation.
2. Track and monitor progress.
In-progress automated evaluations can provide important information about agentic AI
performance. See any initial problems before all the results come through.
3. Review the result outputs.
a.See LLM-judged scores.
b.Identify consistent issues.
c.Trace issues back to their source.
d. Apply optimizations.
4.Create automated evaluation runs for other agentic workflows or AI agents.
5. Create custom metrics to evaluate against your specific business needs.

<!-- page 202 -->
Additional information
•Frequently asked questions about agentic evaluations
•Troubleshoot agentic evaluations
Getting started with agentic evaluations
Run your first agentic evaluation to assess the performance and effectiveness of your agentic AI
assets using automated metrics and datasets.
Before you begin
Before you start your first evaluation run, verify that you have the following:
•An agentic AI asset that has been built and saved in AI Agent Studio
•At least one version of the agentic AI asset
•Available dataset with a minimum number of test cases. You can create new datasets using
Now Assist Data Kit.
•You have the necessary permissions to run the agentic AI asset. You can verify whether you
have the right permissions by checking the user access settings of the agentic AI asset in AI
Agent Studio.
Role required: sn_aia.admin
About this task
Agentic evaluations help you measure the performance and reliability of your agentic AI assets
before deploying them in production environments. The evaluation process runs your agentic AI
asset against test datasets and measures various metrics such as overall completeness and tool
use.
You can use existing datasets, create new datasets from previous execution logs, or generate
new execution logs during the evaluation process. The system provides automated analysis and
optimization recommendations based on the evaluation results.
Procedure
1.Navigate to All > Now Assist Skill Kit > Agentic Evaluations.
The Agentic Evaluations page displays a list of existing evaluation runs and their status.
2. Select Create new evaluation run.
The Create Evaluation Run form opens with configuration options for your evaluation.
3. Complete the basic configuration fields.
Basic configuration form
Field Description
Name Descriptive name for the evaluation run. Use a name that identifies the purpose
and scope of the evaluation.
Agentic AI Select the agentic AI asset you want to evaluate from the list of available assets
Asset in your instance.
Version Select the specific version of the agentic AI asset to evaluate. Different versions
may have different performance characteristics.
Description Optional description providing additional context about the evaluation
objectives and scope.

<!-- page 203 -->
Example
For example, name your evaluation run "Customer Service Agent - Version 2.1 - Performance
Test" to clearly identify what you are testing.
See Version control for agentic AI for more information about maintaining different versions of
your agentic AI assets.
4.Select the metrics to evaluate.
Select multiple metrics to get a comprehensive evaluation of your agentic AI asset's
performance across different dimensions.
5. Configure the data for the evaluation run.
Data configuration options
Option Description
Use existing Select a pre-existing dataset that contains test cases and expected
dataset outcomes for evaluation.
Create dataset Generate a new dataset using previous execution logs of the agentic AI
from execution asset. This option evaluates the actual historical executions of the agentic
logs AI asset.
Generate new Create new execution logs as part of the evaluation run. The system
execution logs generates test scenarios and captures the agentic AI asset's responses.
The system validates your data configuration and displays the selection of test cases that will
be included in the evaluation.
6.Review the configuration summary and select Submit.
The configuration summary displays all selected options, including the agentic AI asset,
version, metrics, and data configuration. Verify that all settings are correct before submitting.
The evaluation run starts and appears in the Agentic Evaluations list with a status of "Running".
7.Monitor progress and review logs when prompted.
The evaluation process may take several minutes to hours depending on the size of your
dataset and complexity of your agentic AI asset. You can track progress in real-time and review
execution logs as they are generated.
8.Review results, issues, and traces once the run completes.
After the evaluation completes, analyze the detailed results including metric scores, identified
issues, and execution traces to understand your agentic AI asset's performance.
9.Apply recommended optimizations and trigger a re-evaluation.
Based on the evaluation results, the system may provide optimization recommendations.
Apply these recommendations to improve your agentic AI asset's performance and run
additional evaluations to measure improvements.
Result
You have successfully created and executed your first agentic evaluation run. The evaluation
results provide insights into your agentic AI asset's performance and areas for improvement.
You can use these results to optimize your agentic AI asset before deploying it in production
environments.
What to do next
After completing your first evaluation, consider the following next steps:

<!-- page 204 -->
•Schedule regular evaluations to monitor performance over time
•Create additional datasets to test different scenarios and use cases
•Share evaluation results with AI architects and leads
Frequently asked questions about agentic evaluations
Find answers to common questions about setting up and running evaluations.
Do I need to keep anything ready before an automated evaluation?
Before you begin, make sure you:
•Test your agent or workflow in the playground. Catch the obvious issues early—
automated evaluations are best for deeper validation.
•Ensure your table has all the required inputs if you're generating test scenarios or
using scenarios from previous agent or workflow runs during setup.
•Prep enough scenarios. We recommend at least 100. Your evaluation is only as
strong as the situations you put your agent through.
•Define what success means. Be clear on what the right output for your agent
should be.
How do I set up my first automated evaluation?
To set up an evaluation, follow the guided flow:
1.Select your agent or workflow and its version.
2. Choose your metrics—built-in or custom.
3. Use an existing dataset or decide how you want to build one.
That's it—you're ready to evaluate.
When should I create a custom metric?
Create a custom metric when you have unique evaluation criteria and want to
measure workflow or agent-specific behaviors that aren't covered by ServiceNow's
built in metrics. For example, you might want to:
•Check whether a particular phrase appears in the agent's response.
•Measure response length to assess verbosity or brevity.
How do I build a dataset for agentic evaluations?
There are two ways to build a dataset for agentic evaluations, but first, let's clarify
what a dataset is. Your dataset should include logs of executions that capture what
happens when your AI agent or workflow processes records like incidents, case, or
tasks. You can create a dataset by either:
•Using logs from previous agent or workflow runs, or
•Generating new logs by running the agent or workflow after setup.
What's next after an automated evaluation?
Review your evaluation results to:
•Identify configuration gaps in your agent or workflow
•Assess deployment readiness

<!-- page 205 -->
•Analyze tool performance for issues with inputs or descriptions
•Drill down into individual executions and metric scores
Return to AI Agent Studio to refine your configuration, then rerun evaluations to
track improvements.
How do I create a custom metric?
Create a custom metric in a few steps:
1.Name and describe your metric.
2. Define its evaluation scope—agentic workflow, agents, or both.
3. Specify what it measures, how it works, and its output format.
4.Add metric inputs and write your script-based metric.
5. Save and publish to make it available for use.
How do I interpret evaluation results?
Based on the metrics you select, each execution will display a score for every
metric. Refer to the "Metric guide" to understand what the scores mean. You can
also customize metric thresholds to align with your organization's definitions of
success and failure.
How do I track the progress of my evaluations?
Evaluations may take some time, but you don't need to stay on the page. From the
homepage, you can track all evaluations and even see if any action is required.
How is the parser tool used during custom metric creation?
When creating a custom metric for agentic evaluations, providing a metric input is
optional—we include the 'execution plan record sys_id' by default. We also provide a
parser tool that pulls structured data from your execution logs, so you won't need to
manually parse through the XML or JSON. You can access the parser tool's outputs
with tool output.
Execute an agentic evaluation run
Evaluate agentic AI assets against datasets to monitor performance and compare benchmarks.
Before you begin
Evaluation runs require execution log data of the agentic AI asset you want to evaluate. You can
create execution log data by testing in AI Agent Studio or triggering agentic AI in Now Assist. You
can also create execution log data after setting up your evaluation run.
For more information about testing agentic workflows, see Manually test the execution of an
agentic workflow.
For more information about getting started with agentic evaluations, see General guidelines for
agentic evaluation runs.
Role required: sn_aia.admin
Procedure
1.Navigate to All > Now Assist Skill Kit > Agentic Evaluations.
You can also start from the testing page of the AI Agent Studio. Navigate to All > AI Agent
Studio > Testing. Select Start automated evaluation to access the guided setup.

<!-- page 206 -->
2. On the evaluations home page, select New evaluation run to begin the guided setup.
3. In the modal, select Chat agent or workflow, then select Proceed.
The following steps are for chat agentic AI assets. If you are evaluating an AI voice agentic
asset, see Execute a run for an AI voice agentic asset. Many steps are similar, but there are
aspects specific to AI voice agentic assets that require special attention.
4.In the Add general info step, add a name and select the agentic AI asset that you want to
evaluate.
5. Select Continue to go to the next step.
Each time you navigate through a step, the evaluation run is saved automatically as a draft. At
any point, you can select Save as draft.
If you want to exit the guided setup, you can select Exit setup. You're redirected to the Agentic
Evaluations page.
◦If you select Save and exit, the evaluation run appears on the Agentic Evaluations page with
the status of Draft.
◦If you select Discard and exit, the evaluation run draft is deleted.
6.Select your evaluation metric.
Overall task completeness evaluation is selected by default. Running multiple evaluation
metrics provides a comprehensive overview of the agentic AI asset's performance.
To see more information about each plan, you can expand the card for each evaluation plan by
selecting the chevron icon .
Any custom metrics that you have published appear as options. If you don't see your custom
metric, verify that it's published. See Create a custom metric for more information.

<!-- page 207 -->
7.Configure your dataset.
a.Choose between generating new execution logs by running the agent or workflow or using
execution logs from previous runs.
b.To create a dataset by generating new execution logs, start by selecting a table.
Instead of making a new dataset from scratch, you can choose to use a past dataset that you
used in a different evaluation by selecting Select from a past dataset. Once you select a
dataset, you can review the details including source table, record count, and the last agentic
AI asset that used the dataset.
Note: If you're evaluating an agentic AI asset created with AI Agent Advisor, the
options for your dataset are automatically filled in for you. You can still make edits to the
values.
Configure dataset form for new execution logs
Field name Description
Table The source table for records that the agentic AI asset uses to perform tasks
and create executions.
Added Conditions for narrowing down the list of records for the agentic AI asset to
filters use to generate execution log data.
No. of The maximum number of records within the dataset for evaluation. If the
records to dataset contains more records than the maximum, additional records are
use ignored.
Task Utterance given to the agentic AI asset to execute. Use the pill picker to select
dynamic inputs for the task. For example, set the starting instruction to Help

<!-- page 208 -->
Field name Description
me resolve {{incident.number}}. Inputs from the record must be
written between double curly braces.
Additional Information given to the large language model (LLM) that supplements table
details record information. For example, a tuition reimbursement agentic workflow
about the requires the normal reimbursement allowance, which could be provided
agent or through a knowledge article.
workflow
Run as user The user associated with the table record to run the agentic AI asset. For
example, depending on your use case, you can run the user as the requester
or as the fulfiller.
Name Name for the dataset. This can be useful if you plan on using the same
dataset again.
Description Description of the records contained within the dataset. This can be useful if
you plan on using the same dataset again.
Note: If you're creating new execution logs, the user submitting the evaluation
must pass the ACLs of the agentic AI asset and its components. Without correct
role requirements, execution logs report access denial and the evaluation fails. See
Security for agentic AI for more information.

<!-- page 209 -->
Configure dataset form for existing execution logs
Field name Description
Added Conditions for narrowing down the AI execution log records you want to include
filters in the dataset.
Note: Filter conditions are not supported for creating datasets of AI
voice agent execution logs.
No. of The maximum number of records within the dataset for evaluation. If the
records dataset contains more records than the maximum, additional records are
to use ignored.
c.Select See preview to see a list of records based on the conditions you specified.
You can narrow down the records by selecting specific records in the preview list.
Unselected records won't be included in the dataset.
8.Review the agentic evaluation details in the last step of the guided setup.
If you want to make changes, you can select Back to go to a previous step, or you can select
the step in the sidebar.

<!-- page 210 -->
9.Select Start evaluation.
Result
Your evaluation run executes. Completion time varies, but after completion you can select the
evaluation from the Agentic Evaluations page to view results.
For more information on the metrics on the results page, see Agentic evaluation run results.
Execute a run for an AI voice agentic asset
Evaluate AI voice agentic assists against datasets to monitor performance and compare
benchmarks.
Before you begin
Evaluation runs require execution log data of the agentic AI asset you want to evaluate. You can
create execution log data by testing in AI Agent Studio or triggering agentic AI in Now Assist. You
can also create execution log data after setting up your evaluation run.
For more information about testing agentic workflows, see Manually test the execution of an
agentic workflow.
For more information about getting started with agentic evaluations, see General guidelines for
agentic evaluation runs.
Role required: sn_voice_aia.admin
Procedure
1.Navigate to All > Now Assist Skill Kit > Agentic Evaluations.
You can also start from the testing page of the AI Agent Studio. Navigate to All > AI Agent
Studio > Testing. Select Start automated evaluation to access the guided setup.
2. On the evaluations home page, select New evaluation run to begin the guided setup.
3. In the modal, select Voice agent or assistant, then select Proceed.
The following steps are for voice agentic AI assets. If you are evaluating an AI voice agentic
asset, see Execute a run for a chat AI agentic asset. Many steps are similar, but there are
aspects specific to AI voice agentic assets that require special attention.
4.In the Add general info step, add a name and description.

<!-- page 211 -->
5. Select whether the AI voice agentic asset is an agent or an assistant, then select the agentic AI
asset that you want to evaluate.
AI voice agents must be part of a voice assistant to evaluate them. To evaluate an AI voice
assistant, it must be active.
6.Select Continue to go to the next step.
Each time you navigate through a step, the evaluation run is saved automatically as a draft. At
any point, you can select Save as draft.
If you want to exit the guided setup, you can select Exit setup. You're redirected to the Agentic
Evaluations page.
◦If you select Save and exit, the evaluation run appears on the Agentic Evaluations page with
the status of Draft.
◦If you select Discard and exit, the evaluation run draft is deleted.
7.Select your evaluation metric.
Overall task completeness evaluation is selected by default. Running multiple evaluation
metrics provides a comprehensive overview of the agentic AI asset's performance.
To see more information about each plan, you can expand the card for each evaluation plan by
selecting the chevron icon .
Any custom metrics that you have published appear as options. If you don't see your custom
metric, verify that it's published. See Create a custom metric for more information.
8.Configure your dataset.
◦Generate new conversations from scenarios, or
◦Use conversations from previous runs.
a.Choose between Generate new conversations from scenarios or Use conversations from
previous runs.
Instead of making a new dataset from scratch, you can choose to use a past dataset that you
used in a different evaluation by selecting Select from a past dataset. Once you select a
dataset, you can review the details including source table, record count, and the last agentic
AI asset that used the dataset.
If you choose to use existing execution logs, you must add a filter before records will display
in the preview.
Note: If you're evaluating an agentic AI asset created with AI Agent Advisor, the
options for your dataset are automatically filled in for you. You can still make edits to the
values.
Configure dataset form for existing execution logs
Field name Description
Added Conditions for narrowing down the AI execution log records you want to include
filters in the dataset.

<!-- page 212 -->
Field name Description
Note: Filter conditions are not supported for creating datasets of AI
voice agent execution logs.
No. of The maximum number of records within the dataset for evaluation. If the
records dataset contains more records than the maximum, additional records are
to use ignored.
b.Select See preview to see a list of records based on the conditions you specified.
You can narrow down the records by selecting specific records in the preview list.
Unselected records won't be included in the dataset.
9.Review the agentic evaluation details in the last step of the guided setup.
If you want to make changes, you can select Back to go to a previous step, or you can select
the step in the sidebar.
When evaluating an AI voice agentic asset, you can choose a run mode in this step of the
guided setup. Select Pause to review to stop after each stage and review results before
continuing, or Run continuously to get your results without intermediary steps.
10.Select Start evaluation.
Result
If you choose to generate new conversations from scenarios, you can track the progress of
scenario generation after you select Start evaluation. If you choose Pause to review, you
can select Start simulation after scenario generation is complete to create the conversation
simulation execution logs. After the conversations have been simulated, select Start evaluation
to begin the actual evaluation of the execution logs.
Note: If you chose the Run continuously run mode, the evaluation will run from scenario
generation to evaluation end to end without additional input.
Completion time varies, but after completion you can select the evaluation from the Agentic
Evaluations page to view results.
For more information on the metrics on the results page, see Agentic evaluation run results.
Generate new conversations from scenarios
Create execution log data for AI voice agentic assets By creating new conversations from typical
scenarios you configure.
Before you begin
The following steps are for the second step of the guided setup for executing an AI voice agentic
asset evaluation. For more information about how to access the guided setup, see Execute a run
for an AI voice agentic asset.
To create conversation logs for your AI voice agentic asset, it must run before the judges can
evaluate it. Ensure that you have the correct permissions to run the AI voice agentic asset. For
more information, see Security for agentic AI.
Role required: sn_voice_aia.admin

<!-- page 213 -->
About this task
The scenarios you generate are the context for creating new execution logs for your AI voice
agentic asset. For the evaluation to reflect real performance, choose scenarios that are
representative of the work the agentic asset will actually handle.
Procedure
1.Select either Generate scenarios or Add scenarios manually.
If you're choosing to add scenarios manually, skip to step 8.
2. Download the reference template for scenario generation.
The reference template includes all of the information necessary to automatically generate
scenarios in the correct format for the automated evaluation.
The template includes:
◦Domain knowledge, capabilities, and available tools
◦Authentication, error handling, and forbidden behaviors
◦Voice channel conventions, conversation length targets, and recap and read back rules
◦Topic taxonomy, follow-up question strategy, and status lifecycle
◦Reference data and entities
3. Fill in the template according to the specifics of your AI voice agentic asset.
You can use as many aspects of the default template as you like. For example, the phonetic
alphabet or time expressions in the template are general enough that they may serve most use
cases for English-speaking AI voice agentic assets.
4.Select Add file, then select Upload.
If there are any validation errors in the uploaded file, the modal displays a warning.
5. Choose the number of scenarios to generate based on the information in the template.
The number of scenarios affects generation time. As a reference, generating 100 scenarios
typically takes about 5 minutes.
6.Select Continue.
Once you select Continue, a sparkle animation appears and the scenarios are generated in
the background.
After generation is complete, view their details by selecting View scenarios. You can delete or
edit any individual scenario.
You can proceed to the next step in the guided setup as soon as at least one scenario is
generated. You don't need to wait for all scenarios to finish.
7.If you generated scenarios, skip to step 11.
8.Select records manually by either uploading a file or using a guided form.
If you're choosing to add scenarios with a guided form, skip to step 10.
9.If you choose to upload a file, select the option and press continue.

<!-- page 214 -->
a.Download the template for the scenario details.
If you have previously uploaded a scenario file, you can select it from the list of attachments.
b.Fill in the information in the CSV file.
The CSV file requires four comma-separated values: the scenario description, the opening
message (how the user starts the conversation), the expected output (a description of the
full conversation), and the end goal (what the AI voice agentic asset needs to accomplish).
You can include as many scenarios in a single file as you want.
Using special characters in the CSV file content can cause problems during the upload
process.
When uploading a new attachment, the previous attachment is still shown. You must delete
the existing attachment via the UI action before uploading a new one.
c.Select Add file, then select your completed template.
d. Select the attachment you added, then select Upload.
10.If you choose to use a guided form, select the option and press continue.
a.Enter a description of the scenario.
The description provides context for how the AI voice agentic asset is used, which an LLM
uses to generate scenarios. Make sure the description is thorough enough for the LLM to
accurately interpret the asset and produce relevant scenarios.
b.Craft an opening message.
The opening message represents what a user says at the start of an interaction with the AI
voice agentic asset. When creating multiple scenarios, vary the opening messages to cover
the range of inputs the asset is likely to encounter.
c.Describe the expected output.
The expected output field should describe the full conversation between a user and the
AI voice agentic asset. The clearer and more specific this description is, the better the
generated scenarios will be.
d. Select Create to add the scenario.
e. Repeat for additional scenarios.
11. Name your dataset.
Choosing a descriptive name for your dataset makes it easier to find if you want to use it again.
12. Select Continue to move to the next step of the guided setup.
What to do next
After generating your scenarios, you can move on to the final step of the guided setup. See step
9 of Execute a run for an AI voice agentic asset.

<!-- page 215 -->
Track and monitor agentic evaluation progress
Monitor the status of an active evaluation run to catch errors early and confirm when results are
ready to review.
Before you begin
You must have an active evaluation run to monitor. For information about creating evaluation
runs, see Execute an agentic evaluation run.
Role required: admin
About this task
Agentic evaluations can take time to complete, especially for large datasets. Monitoring progress
helps you identify issues early and determine when results are ready for review.
Procedure
1.Navigate to All > Now Assist Skill Kit > Agentic Evaluations.
2. Select an evaluation with a trackable status.
You can find evaluations to track in two locations:
◦Quick overview section: Recent in-progress evaluations appear in the In-progress
evaluations card
◦Automated evaluations section: All evaluations, including older ones
Evaluations you can track have a Run status of In progress or Action needed.
3. Select the evaluation you want to monitor.
The evaluation monitoring details page opens, showing the current status and progress
information.
4.Optional: If the status is Action needed, review the generated execution logs.
(Optional) The most common reason for the Action needed status is when execution logs have
been generated but require approval before the evaluation phase can begin.
a.Examine the dataset artifacts to understand how the agentic AI performed on specific
records.
You can open individual incidents or other records to see how the agentic AI asset
interacted with them during the test.
b.Select execution records to view detailed performance information.
This opens the execution details in AI Agent Studio, where you can review the complete
conversation between the simulated user and the agentic AI, including reasoning and
processing messages from agents and tools.
c.Review conversation records and timestamps to understand the interaction flow.
The start phrase and conversation records provide detailed information about how the AI
agent interacted with the simulated user, including timestamps for each message.
5. Optional: If you reviewed the execution logs and they meet your expectations, start the
evaluation phase by selecting Start evaluation.
(Optional) After you approve the logs, the LLM judging and scoring phase begins. This phase
analyzes the execution logs and provides quantitative scores for the AI agent's performance.
The evaluation status changes to In progress and the LLM evaluation begins.

<!-- page 216 -->
6.Optional: Monitor the progress of the LLM evaluation phase.
(Optional) During this phase, you can track:
◦Number of records evaluated
◦Estimated time remaining
◦Any errors or warnings that occur during evaluation
7.Optional: Check for completion notifications or status updates.
When the evaluation completes, the status changes to Completed and results become
available for review.
Result
You can monitor the evaluation progress and take action when required. When the evaluation
completes successfully, you can review the detailed results to understand your agentic AI's
performance.
What to do next
After the evaluation completes, review the results to identify areas for improvement in your
agentic AI configuration. For information about analyzing evaluation results, see Review the
results of an agentic evaluation.
Review agentic evaluation outputs
Assess your agent's overall performance after a run completes, including per-metric scores
and issue counts. Use the results as your starting point for diagnosing quality issues and
opportunities for improvement before deployment.
Before you begin
You must have a completed agentic evaluation.
Role required: sn_aia.admin or admin
About this task
Automated evaluations include scores and recommendations across the different metrics you
chose. Each output provides information you can use to make decisions about development
and deployment of the agentic AI asset. The evaluation results help you identify performance
patterns, quality issues, and optimization opportunities before deploying your agent to
production.
Procedure
1.Navigate to All > Now Assist Skill Kit > Agentic Evaluations.
2. Select the automated evaluation you want to review the results of.
The evaluation details page opens, displaying the overall results and performance metrics.
3. Review the evaluation summary section to understand the overall performance.
The summary provides a high-level overview of your agent's performance across all evaluated
metrics. Key information includes:
◦Agentic AI asset information such as name and version
◦Total number of test cases evaluated
◦Average scores across all metrics
◦Number of issues identified by severity level
4.Review the overall LLM-judged scores for each metric.

<!-- page 217 -->
General LLM-judged scores for each metric demonstrate overall patterns and trends across
the metrics you have evaluated against. These scores provide general recommendations for
deployment based on the current version of the agentic AI asset. Detailed results include:
◦Numerical score
◦Performance rating (Excellent, Good, Moderate, or Poor)
◦Individual record evaluations
5. Investigate any issues and their associated traces.
If problems with the agentic AI asset's performance are found, they are categorized by
severity level, metric, and use case. Issues can be tracked down to their sources in specific
interactions, called "traces." Review issues and their traces to diagnose underlying issues.
Issues are classified by severity level:
◦Critical: Issues that can prevent the agent from functioning correctly, resulting in a poor user
experience
◦High: Significant problems that impact user experience or accuracy
◦Medium: Moderate issues that may affect performance in some scenarios
◦Low: Minor issues that have minimal impact on overall functionality
6.Apply optimizations based on the findings.
The automated evaluation can include recommended optimizations to address issues found
in the evaluation. After you have applied the optimization, you can rerun the evaluation to see
the changes in behavior and performance. Track improvements by comparing results across
evaluation runs.
Result
You have a comprehensive review of your agent's performance across all evaluated metrics.
Use these insights to make informed decisions about deployment readiness or identify areas
requiring additional development work.
Review issues discovered in agentic evaluations
Identify and prioritize specific quality failures detected during an evaluation run, organized by
severity. Use issue severity and metric relevance to decide which failures to address before
deployment.
Before you begin
Role required: sn_aia.admin
Procedure
1.Navigate to All > Now Assist Skill Kit > Agentic Evaluations.
2. From the list, select the automated evaluation you want to review.
The evaluation details page opens, displaying the overall results and performance metrics.
3. If any issues are identified, select Review and optimize to view details.
The optimization guided setup opens for that agentic AI asset.
Each issue is associated with a specific tool or agentic AI asset.
4.From the issues list, select an issue to review.

<!-- page 218 -->
Each issue has a description of what the issue is, a root cause analysis, traces associated with
it, and a space for adding notes about the analysis.
Section Description
Issue score Brief overview of the identified issue and its impact on the agentic AI asset
and short
description
Description More detailed information about the identified issue than the short description
Root cause Insights into the cause of the symptoms seen in the agentic AI asset. Identifies
analysis specific components of the issue and which metric discovered it.
Traces with Specific execution logs where the issue is seen. You can analyze traces to
this issue understand how the issue manifests.
Analysis Space for you to add details about the analysis and what you want to
notes communicate to others about the issue. These notes aren't considered when
applying optimizations. See Apply optimizations for more information.
5. Optional: Analyze the traces of the issue.
6.After reviewing the identified issues, select Start optimization to see the LLM-recommended
fixes.
Result
Issues associated with the metrics for different components of the agentic AI asset are reviewed,
analyzed, and documented.
What to do next
Proceed to the next step to apply optimizations to fix identified issues.
Analyze traces found in agentic evaluation run results
Investigate the full record of an agentic interaction to diagnose the root cause of a quality failure.
Trace each step the agent took, including tool calls and outputs, to pinpoint where things went
wrong.
Before you begin
You must have a completed agentic evaluation with issues identified.
Role required: sn_aia.admin
About this task
If you are already in the flow for identifying issues, skip to step 5.
Procedure
1.Navigate to All > Now Assist Skill Kit > Agentic Evaluations.
2. Select the automated evaluation you want to review the results of.

<!-- page 219 -->
The evaluation details page opens, displaying the overall results and performance metrics.
3. If any issues are identified, select Review and optimize to view details.
The optimization guided setup opens for that agentic AI asset.
Each issue is associated with a specific tool or agentic AI asset.
4.Select an issue to review.
5. Select Show traces.
Each execution plan where the issue occurred can be reviewed node-by-node with the inputs
and outputs of each node displayed. You can navigate between nodes by selecting them in
the center section.
6.Close the traces modal.
What to do next
Select Apply optimization to look at LLM-generated suggestions for optimizations to fix the
issues.
Apply optimizations to agentic AI assets and reevaluate
Review and accept system-generated recommendations to improve agent quality based on
detected issues. Apply optimizations before triggering a re-evaluation to confirm that changes
resolved the failures.
Before you begin
You must have a completed agentic evaluation with issues identified.
Role required: admin
About this task
If issues are identified by the LLM judges, they can generate suggestions for possible fixes to
address the issues. After reviewing the issue, you can select Start optimization to check the
recommendations before applying them and starting a reevaluation.
If you are already in the flow for identifying issues, skip to step 6.
Procedure
1.Navigate to All > Now Assist Skill Kit > Agentic Evaluations.
2. Select the automated evaluation you want to review the results of.
The evaluation details page opens, displaying the overall results and performance metrics.
3. If any issues are identified, select Review and optimize to view details.
The optimization guided setup opens for that agentic AI asset.
Each issue is associated with a specific tool or agentic AI asset.
4.Select an issue to review.
5. Go over the issue, including analyzing issue traces.
6.Select issues to optimize, then select Start optimization.
You can choose to optimize for as many issues as you want. It is possible to generate specific
changes to an agentic AI asset that address multiple issues at once.
7.Select Yes to generate the optimization suggestions.

<!-- page 220 -->
8.Review the suggested optimizations.
Optimizations occur at the prompt level for tool or agentic AI asset descriptions and lists of
steps.
If an optimization is to a description or list of steps, you can toggle to see the current
instructions by itself next to the suggestion for the optimized version. You can also toggle to
show the differences between the current and suggested version or to see just the optimized
version by itself.
If you want to make edits to the suggested texts, you can toggle Edit mode to enter your own
text or change the contents of the generated text.
To open the tool or agentic AI asset in AI Agent Studio, select the open link icon. The
associated agentic AI asset opens in a new browser tab.
You can see the issues that the optimization is trying to address by selecting Contributing
issues. You can select an issue to review all of the details, including the root cause analysis.
9.Select Continue to re-evaluate if you want to re-evaluate without applying the optimization or
Review and apply if you want to make the suggested changes.
10.Review the details for reevaluation.
The optimization summary includes the list of issues that are being trying to be addressed by
the optimization.
You can name your evaluation and select the version of the agentic AI asset. Because this is a
reevaluation, the evaluation metrics and dataset are the same as the original run and can't be
changed.
11. Select Start re-evaluation to begin the new agentic evaluation run.
You can go back to a previous step in the issue-optimization flow by selecting Back to
evaluation setup.
Result
A new evaluation run begins with any changes you applied to the agentic AI asset.
What to do next
You can track and monitor your agentic evaluation while the reevaluation is in-progress. After the
evaluation is complete, you can review and compare the results against the original evaluation
and make further optimizations if necessary.
Troubleshoot agentic evaluations
Find solutions to common evaluation errors, including run failures, data ingestion issues, and
unexpected results.
When using agentic evaluations, you may see unexpected execution results or errors. The
following discusses situations you could encounter and some of the reasons why those
situations occur.
Evaluation run failed
There are a few different reasons why an evaluation run may fail to execute properly.
Agent version unavailable

<!-- page 221 -->
Verify that the selected agent version still exists in AI Agent Studio. The version
does not have to be the one currently active, but deleted or archived versions can't
be evaluated.
User permissions
Confirm that your User record has the permissions required to execute evaluation
runs in general and to use the specific AI asset. To check whether a certain user has
access, you can perform an access test. See Test user access to an AI agent and
Test user access to an agentic workflow.
Data format errors
Verify that the dataset conforms to the required format. Malformed records can
cause the evaluation to fail. See Data requirements for agentic evaluations for the
supported data types.
Metric and data mismatch
Confirm that all selected metrics have the required data inputs. Metrics that require
ground truth will fail if the ground truth field is missing from the dataset.
Agentic AI asset underperformance despite no issues found
If the evaluation found no issues, but the specific agentic AI asset is still not performing to
acceptable standards, consider the following:
Dataset coverage
The evaluation dataset may not include the types of inputs or scenarios that
expose the agent's weaknesses. Review the dataset for any coverage gaps and add
representative edge cases to more closely align what is being evaluated with real-
world scenarios.
Metric selection
The selected metrics may not be measuring where the agentic AI asset is
failing. Review whether additional or different metrics would better capture the
performance gap. You can create custom metrics to evaluate other dimensions of
the agentic AI asset responses or actions, such as length of response or whether a
response meets certain formatting requirements.
Scoring thresholds
The pass threshold for a metric may be set at a level that does not reflect your
requirements. Review threshold settings in the metrics configuration to redefine
success and failure.
Optimization applied, but re-evaluation didn't improve
If the re-evaluation scores did not improve after applying optimizations, try the following:
•Review trace details for the issues that were targeted. The optimization may have only
alleviated surface-level symptoms without resolving the underlying root cause.
•Check whether the optimization introduced a regression in a different metric. Score
improvements in one area can sometimes degrade another, lowering the final scores.
•If the optimization was applied to the list of steps of an agentic AI asset, verify that the updated
list of steps was applied to the version you're evaluating.
Data processing errors
If the data can't be processed because it doesn't meet data requirements, the evaluation can't
execute properly. The following describes common causes of data processing errors:

<!-- page 222 -->
Incorrect file format
The accepted file formats are CSV and structured JSON. Other file formats can't be
processed.
Missing required fields
Datasets must include the fields required by the selected metrics. Check for missing
or misnamed columns. If you're using a ground truth, you must include it in the
dataset.
Encoding issues
Files must be UTF-8 encoded. Files with non-standard encoding may fail to be
processed.
File size
Very large files or datasets may time out during processing. If this occurs, reduce
the dataset size or contact your Platform administrator.
Create a custom metric for evaluating agentic workflows
Create a custom metric for evaluating AI agents and agentic workflows to test the outputs against
expected responses.
Before you begin
Role required: sn_aia.admin
About this task
Custom metrics enable you to choose how you measure your AI agents and agentic workflows
for effectiveness. You can create custom metrics that apply to one agentic AI asset or multiple
ones. After you create them, you can select custom metrics in the guided setup for agentic
evaluations. You can select both or either custom metrics and metrics installed with Now Assist
applications. Examples of custom metrics include:
•Testing that a certain phrase is in the response
•Measuring the length of a response to test verbosity
When writing the script, you have access to the output of a parser tool. See agentic evaluation
parser tool for more details on how it works.
Procedure
1.Navigate to All > Now Assist Skill Kit > Agentic Evaluations.
2. Go to the Evaluation metrics tab and select Create metric.
3. In the General information step, enter a name and short description for your custom metric.
You can navigate between steps in the guided setup with the Continue and Back buttons.
After entering a name for your custom metric, you can skip directly to writing your script by
selecting Skip to Script Editor. You can fill out the details later from the Metric settings tab in
the Script Editor.
4.Optional: In the Metric details step, add information about the evaluation metric, how it works,
and what the output format of the metric is.
(Optional) If you select Use this content, then the details you provide are displayed along with
the option in the guided setup for an agentic evaluation run.

<!-- page 223 -->
You don't have to fill in details, but you have the option to provide useful information and
context to aid the custom metric development process. You can also add metric details from
the Metric settings tab of the Script Editor.
5. After reviewing your metric information in the Summary step of the guided setup, select Finish
setup to be redirected to the Script Editor.
6.Optional: Add metric inputs.
(Optional) By default, the execution plan record sys_id is included as a metric input.
The parser tool enables you to access content from the execution plan log without having to
parse through the XML or JSON content yourself. You can access the parser tool's outputs with
tool.output.
a.In the Metric inputs section, select the plus icon to open the Add metric input modal.
b.Complete the form.
Field Description
Input List to choose what data type and format the input is
datatype
Name Short, user-friendly name for the input
Description Description of the input. You can view the description of any input by
selecting it in the Metric inputs section of the Script Editor.
Test values Default input values used for testing your script in the Script Editor
Mandatory Determines whether providing the input is necessary for the evaluation to run
c.Select Add.
7.Write your script-based metric.
The default code block in the Script Editor contains commented code that can guide you
through the script-writing process.
At any time, you can select Metric output template to see the code necessary for the output
to display correctly when looking at the evaluation run results in Skill Kit. This content is also
included in the default code block when you first open the Script Editor. If necessary, you can
copy the template and paste it into the script. Be sure to change the values to the results of
your custom metric.
You can review the details of the custom metric from the guided setup from the Metric settings
tab.
After you make changes, you can select the Save button to save your changes.
Important: Even if you save, the metric will not be available to use in agentic evaluation
runs until you publish it.
8.Select Run test to open the Run test modal, enter your metric test inputs, and run the test.
After you have run at least one test, you can review the response and request of both the
overall execution and the parser tool.

> **[Screenshot: New auto evaluation guided setup — Add general info step]**
> The "New auto evaluation" wizard with breadcrumb "< New auto evaluation". Left sidebar stepper: "Set up automated evaluation" (expanded): "Add general info" (filled circle, step 1 active), "Select evaluation metrics" (empty, step 2), "Configure data" (empty, step 3), "Review summary" (empty, step 4). Main content title "Add general info". Instruction: "Enter a unique name and description to identify the evaluation and its purpose. Then, select an agent or workflow to evaluate." Fields: "Name *" = "Tool performance evaluation - custom categorize ITSM incident". "Description" = "This run will evaluate the tool performance of the customized Categorize ITSM incident AI agent, including tool choice and tool calling." Note badge: "This description is for internal reference only. It has no impact on the automated evaluation." "Select an AI agent or workflow *" = "Custom Categorize ITSM incident AI agent". "Select version *" = "1 – V1 (Active)" dropdown. "Go to agent guided setup ↗" link. "AI agent description" = "Categorize ITSM incident AI agent assigns appropriate category and subcategory to an incident."

> **[Screenshot: Select evaluation metrics step — core and custom metrics]**
> The evaluation wizard on "Select evaluation metrics" step. Left sidebar shows step 2 as active (filled circle). Main content: "Consider what you want to measure for your agent or workflow, and select the metrics that matter most." "Core metrics from ServiceNow" section: "Built-in metrics that assess your agent or workflow — from task completion to tool performance." Three metric cards with checkboxes: 1) "Overall task completeness evaluation" (checked ✓, expanded with ∨) – "Evaluates whether the AI agent or workflow successfully completed its assigned task and followed instructions." 2) "Tool choice accuracy" (checked ✓, expanded with ∨) – "Evaluates whether the AI agent selected the correct tool at each execution step based on its goal and instructions." 3) "Tool calling correctness" (checked ✓, expanded with ∨) – "Evaluates whether the AI agent correctly invoked a tool at each execution step." "Custom metrics" section below: "Metrics that you created to assess agentic evaluations." One unchecked item: "Correct format" (with ∨ expand arrow).