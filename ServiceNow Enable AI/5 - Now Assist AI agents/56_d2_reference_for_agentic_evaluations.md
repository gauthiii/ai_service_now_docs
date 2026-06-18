# Reference for agentic evaluations

_Source pages: 224–230 | Depth: 2_

---

<!-- page 224 -->
After you have run at least one test, you can select the Run test drop-down button and select
Run test history to open a new sidebar with past test results. You can filter test runs by the
user who executed the test.
9.Select Publish metric to save your script and activate the metric.
Before publishing, verify that your output matches the metric output template. If not, your
metric may not work as expected or display correctly on the evaluation run results page.
Result
You have a new custom metric that can be used for evaluating agentic AI assets.
What to do next
Execute an evaluation run and select your custom metric in the guided setup. See Evaluate
agentic AI for more information on executing an evaluation run.
If you don't see your custom metric in the guided setup for an evaluation run, make sure that you
have published it.
Reference for agentic evaluations
Find technical reference material for roles, metrics, and output formats of agentic evaluations.
Available metrics
Standard metrics available
Ground truth
Metric What it measures
required
Task Whether the agentic AI asset fully addresses the user need. Optional
completeness
Response Whether the agentic AI asset's response is factually accurate Recommended
accuracy
Groundedness Whether the agentic AI asset's response is grounded in the No
specific context of the task
Coherence Whether the agentic AI asset's response is logically No
structured and clear
Tool use Whether the agentic AI asset selected and used the correct Optional
accuracy tool to execute its tasks
Goal Whether the agentic AI asset stayed within its defined scope No
adherence and instructions

<!-- page 225 -->
Issue types
Issues are broken down by behavior. Each metric has its own issues identified separately.
Issue categories
Category Agentic AI asset behavior
Incomplete Response failed to address the user's full request
response
Factual error Response contained content that isn't factually correct
Hallucination Response contained content not grounded in the specific context of the
request
Incoherent output Response was disorganized or difficult to understand
Incorrect tool use Selected the wrong tool or passed incorrect parameters to a tool
Scope violation Responded to a request outside its defined operating scope
Data requirements
Data requirements for datasets in agentic evaluations
Requirement Description
Minimum test A minimum number of test cases is required per run. The specific metrics
cases you are using for the run may have their own minimum test cases. Ensure
that your dataset meets the requirements for all metrics.
Supported formats CSV and structured JSON are supported.
Ground truth field If you're using a ground truth, it must be provided as a separate field in
the dataset. The ground truth field must be aligned to each test case
individually.
Data Datasets should reflect all of the tasks that the AI agent or agentic
representativeness workflow will handle. Include edge cases and failure-prone scenarios to
help ensure that you're testing against common real-world scenarios.
Agentic evaluation parser tool
Use the outputs of the agentic evaluation parser tool in your scripts for custom metrics to
customize the criteria for effective AI agents and agentic workflows.

<!-- page 226 -->
Parser tool overview
The agentic evaluation parser tool extracts structured execution data from the execution logs
of an agentic workflow or AI agent. You can use the information gathered by the tool to create
custom metrics that use scripts to evaluate agentic workflows.
The parser tool returns structured AI agent or agentic workflow execution data within the
output.payload object, which contains the following:
•executionInputs: A JSON object that contains initial workflow setup information, such as
the names and instructions of agents and tools and the initial user utterance
•executionOutputs: A JSON object with AI agent actions and tool execution results
•executionMessages: A JSON object array of user-facing conversation flow and system
responses
•executionPlanDetails: A JSON object of execution metadata, such as status, sys_ids,
and configuration values
{
"output": {
"payload": {
"executionInputs": { ... },
"executionOutputs": { ... },
"executionMessages": [ ... ],
"executionPlanDetails": { ... }
}
}
Accessing the parser tool's output
To view the complete parser tool output for testing and development, perform the following
steps.
•Navigate to the Script Editor view in your custom metric guided setup.
•Select Run Test.
•Wait for the test to complete.
•View the complete JSON output in the Tools section of the test results.
Reviewing the parser tool's output before designing your custom metric enables you to inspect
the data structure before implementing any specific logic.
executionInputs data structure
The executionInputs attribute contains a JSON object with the following structure:
"executionInputs": {
"agenticWorkflow": "(name of agentic workflow)",
"description": "(descriptions for agentic workflow)",
"instructions": "(list of steps for agentic workflow)",
"utterance": "(initial user utterance)",
"agents": [
{
"name": "(AI agent name)",
"instructions": "(list of steps for AI agent)",
"tools": [

<!-- page 227 -->
{
"name": "(tool name)",
"description": "(tool description)",
"executionMode": "(execution mode, either Autonomous or
Supervised)",
"inputs": { ... }
},
{ ... }, ...
]
},
{ ... }, ...
]
}
executionOutputs data structure
The executionOutputs attribute contains a JSON object with the following structure:
"executionOutputs": {
"agents": [
{
"name": "(AI agent name)",
"subTask": { ... },
"tools": [
{
"name": "(tool name)",
"inputs": { ... },
"output": { ... }
}
]
},
{ ... }, ...
]
}
executionMessages data structure
The executionOutputs attribute contains an array of JSON objects with the following structure:
"executionMessages": [
{
"role": "(Message sender, either 'agent' or 'user')",
"message": "(Content of message)",
"order": "(Sequence number indicating order of message in the
conversation)"
},
{ ... }, ...
]
executionPlanDetails data structure
The executionPlanDetails attribute contains a JSON object with the following structure:
"executionPlanDetails": {
"state": "(Current execution status)",
"runType": "(Type of execution)",

<!-- page 228 -->
"conversationId": "(sys_id of conversation)",
"relatedTask": "(sys_id of the associated task or record)",
"relatedTaskTable": "(Table name where the related task is
stored)",
"context": { ... } (May be null)
"builtInTools": [ { ... } ]
}
This section provides execution metadata for tracking workflow performance, debugging issues,
and correlating executions with specific tasks or conversations.
The possibilities for runType include the following:
•API
•Chat
•Evaluation
•Testing
•Trigger
Using parser tool output in metric scripts
The parser tool data is available in your metric script through the context parameter. Access
the structured data using the following code:
// Access the parser tool output from context
var parserToolOutput =
context['AgenticExecutionParserTool.output'];
if (typeof parserToolOutput == "string") {
parserToolOutput = JSON.parse(parserToolOutput);
}
var parserToolPayload = parserToolOutput.payload;
var parserToolStatus = parserToolOutput.status;
// Extract individual sections from payload
var inputs = parserToolPayload.executionInputs;
var outputs = parserToolPayload.executionOutputs;
var messages = parserToolPayload.executionMessages;
var planDetails = parserToolPayload.executionPlanDetails;
Agentic evaluation run results
Learn about agentic evaluation runs and the meaning behind different evaluation scores from
the agentic evaluation results page.
Agentic evaluations overview
Agentic evaluations measure how well AI agents and agentic workflows are accomplishing
their objectives. A Now LLM Service model judges the AI agent or agentic workflow based on
the execution logs. The results page of an evaluation run shows multiple metrics and scores
measuring task completeness and tool use.
If you run an overall task completion evaluation, the results page shows recommended actions
for the AI agent or agentic workflow. Recommended actions give you suggestions for deployment

<!-- page 229 -->
or improvement to help verify that the agentic workflows that you deploy are performing up to
your standards.
After you've reviewed your evaluation results, you can archive your evaluation or copy it to run
another evaluation with the same parameters and dataset.
You can export the evaluation results as a report. The report is formatted as a .csv file that
includes the individual sys_ids of the execution records and the metric scores for each.
For more information on AI agent usage and other analytics, you can review the AI Agent
Analytics dashboard in the AI Agent Studio.
Evaluation results overview
For each evaluation method that you execute, the results page displays an overall score for the
agentic workflow with a percentage of successful record evaluations and a label of Excellent,
Good, Moderate, or Poor. You can change the metric thresholds for each label by selecting
Customize metric thresholds.
In addition to the overall task completeness results, you can review a summary of the results of
the other metrics.
Overall task completeness evaluation run results
Default
Label Description Recommended action
threshold
Excellent Tasks were consistently performed at a high Proceed with 90%–
standard. The agentic workflow or AI agent is confidence 100%
working well.
Good Most tasks were performed successfully, but Deploy with caution 70%–
some performance inconsistencies suggest areas 89%
for improvement.
Moderate A significant number of tasks weren't fully Investigate the root 50%–
completed. Performance is below the desired causes of poor task 69%
level. completion
Poor The agentic workflow is consistently failing to Do not deploy 0%–
complete tasks adequately. Major issues are 49%
present.
Individual record metric scores
Evaluations are run against the log tables of agentic workflow executions. Each record is
individually scored for each evaluation plan that you run. Individual record evaluations are
scored according to the following metrics.

<!-- page 230 -->
Overall task completeness record metric scores
The overall task completeness metric assesses whether an AI agent
successfully completes its assigned task. It evaluates the execution logs of the
agent, ensuring that all required steps were taken and the task was logically
and effectively completed.
Number Score Description
3 Successful The main task was fully completed. All subtasks were resolved, and the
steps followed a logical sequence with no critical errors.
2 Partially The task was partially completed. Some subtasks remain unresolved or
successful inefficiencies affected the process.
1 Unsuccessful The task wasn't completed. Critical subtasks were abandoned or
unresolved or the execution failed entirely.
Tool performance record metric scores
The tool performance evaluation metric assesses an AI agent's ability to select
the most appropriate tool for each step while completing a task.
Number Score Description
1 True The right tool was chosen for the action in the plan.
0 False The right tool wasn't chosen.
Tool calling records metric scores
The tool calling evaluation metric assesses whether an AI agent correctly
constructs tool calls by validating the accuracy, completeness, and formatting
of the inputs it provides.
Number Score Description
1 True Input key completeness, input value correctness, and input format correctness
are all successful.