# Agentic evaluation run results

_Source pages: 260–262 | Depth: 2_

---

<!-- page 260 -->
Data visualizations on the AI Agent Analytics dashboard security page (continued)
Name Type Description
AI agents running as AI user List List of AI agents running as an AI user.
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

<!-- page 261 -->
Overall task completeness evaluation run results (continued)
Default
Label Description Recommended action
threshold
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

<!-- page 262 -->
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
•Input key completeness: 1 - True – All required parameters are
present with exact name matches, and no unexpected parameters are
included.
•Input value correctness: 1 - True – Tool input values are correctly
mapped.
•Input format correctness: 1 - True – Tool inputs are in the correct
format.
0 False One or more of input key completeness, input value completeness, or input
format completeness wasn't successful.
•Input key completeness: 0 - False – A mandatory parameter is either
missing, its name doesn't match exactly, or an unexpected parameter was
found.
•Input value correctness: 0 - False – Tool input values are not
correctly mapped.
•Input format correctness: 0 - False – Tool inputs are not in the
correct format.
Note: The values of the sub-metrics are aggregated using an AND operator. If any one
value is 0, then the entire tool calling records metric score will be 0.