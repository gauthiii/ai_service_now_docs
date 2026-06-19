# Explore agentic evaluations

_Source pages: 197–200 | Depth: 2_

---

<!-- page 197 -->
Automated evaluations for agentic AI are a structured quality assurance capability for agentic
AI assets built in AI Agent Studio. Each evaluation run tests your agents against a defined
dataset, applies LLM-powered judges to score key quality dimensions, and surfaces issues with
recommended fixes. Use automated evaluations to get objective, explainable evidence that your
agentic AI is ready to deploy.
Helpful resources
Some ServiceNow resources that can provide you with helpful information are:
ServiceNow Community
ServiceNow Community
Developer
developer.servicenow.com
Impact
http://impact.servicenow.com
ServiceNow University
ServiceNow University
Best Practices
Best Practices
Partner
https://www.servicenow.com/partners.html
ServiceNow
http://servicenow.com
ServiceNow Store
http://servicenow.com
Support
•https://support.servicenow.com/now
•Known Error Portal
Explore agentic evaluations
Automated evaluations test your agentic AI assets and help determine when they're ready for
production. Learn more about how evaluations work, who they’re designed for, and the benefits
they deliver.
Agentic evaluations overview
Automated agentic evaluations help give AI agent builders the confidence to deploy with
objective, explainable evidence that their agents are ready for production. They remove the
guesswork from quality assurance by running your agent against a defined dataset and applying
LLM-powered judges to score quality, such as task completeness, response accuracy, and
tool use. From there, the system generates recommended optimizations you can apply before
triggering a re-evaluation to confirm improvements.

<!-- page 198 -->
Building agentic AI assets like AI agents and agentic workflows is an iterative process. Agentic
evaluations are designed to verify the quality of the AI asset with in a structured way to help
speed up the process. Because you're testing against representative datasets, you can be more
confident in the performance of your agentic AI asset to handle real-world situations.
Agentic evaluations can be run in non-production environments and don't require live
deployment. They can be run during testing phases of agentic AI assets to help ensure that they
can be deployed to a production environment while meeting your benchmarks and standards.
Agentic evaluations users
Users
User Description
Agent builder Developer or configurator who builds agents in AI Agent
Studio. Automated evaluations are designed so agent builders
can run rigorous evaluations at scale.
Platform administrators Platform administrators who govern which agents are
approved for production can use automated evaluation results
for evidence of quality before deployment.
AI leads and architects AI leads and architects can use automated evaluation results
for audit trails and quality metrics across multiple agents.
Automated evaluations workflow
1.Configure an evaluation run with a name, selected agentic AI asset and its version, metrics,
and dataset.
2. Execute the run and track progress as the LLM judges agentic responses.
3. Analyze the run results, including the judge scores and identified issues and traces.
4.Optimize the agentic AI asset with targeted recommendations, then trigger reevaluations.
5. Validate the quality of future runs or other changes to the agentic AI asset.
Automated evaluations benefits
Automated evaluations benefits
Benefit Feature Users
Evaluate specific versions of agentic AI assets Execute an evaluation Agent builders
for quality run
Set your own standards for agentic AI Custom metrics Agent builders,
responses and performance Platform
administrators, AI
leads, and architects
Track evaluations as they progress In-progress results Agent builders
Identify issues and trace them back to the Evaluation outputs Agent builders, AI
source leads, AI architects
Optimize agentic AI assets based on System-generated Agent builders
evaluation results optimization
recommendations

<!-- page 199 -->
What to explore next
To learn more about configuring and using agentic evaluations, see:
•Evaluating agentic AI assets
•Reference for agentic evaluations
General guidelines for agentic AI asset evaluation
Learn about agentic evaluation runs and different recommendations for evaluating your agentic
AI assets against datasets to check for completion, performance, and tool execution.
Overview of agentic evaluation runs
Agentic evaluations help you verify that your agentic AI assets perform as expected across
different scenarios and data sets. Regular evaluation helps maintain quality and identify areas for
improvement as you develop your agentic AI assets.
The evaluation process uses automated testing to measure how well your agentic AI assets
performs. Metrics for evaluation include complete tasks, execute tools correctly, and maintain
performance standards. You can also create your own custom metrics to evaluate agentic AI
asset responses and tasks in other ways.
When to run agentic evaluations
Run agentic evaluations at key points in your development and maintenance cycle to verify
performance and catch issues early.
Run after you have manually tested basic execution
Before running an automated evaluation, manually test the execution of an AI agent
or agentic workflow. Manual testing helps you identify obvious issues and verify that
the basic functionality works before investing time in automated evaluation.
Run agentic evaluations when you make significant changes
After making updates to the agentic workflow, execute an agentic evaluation run
to track the efficacy of the new version. This includes changes to prompts and tool
configurations that might affect performance.
Run evaluations before deploying to production
Evaluate your agentic AI assets in a test environment before deploying them to
production. This helps verify that changes work correctly and maintain expected
performance levels.
Run periodic evaluations for ongoing monitoring
Schedule regular evaluation runs to monitor the ongoing performance of your
agentic AI assets. This helps detect performance degradation over time and
ensures consistent quality.
Run evaluations after data source changes
When the underlying data sources or schemas change, run evaluations to verify
that your agentic AI assets continue to function correctly with the new data
structure.
Choosing an evaluation method
Select evaluation methods based on what aspects of your agentic AI asset performance you
want to measure. Different methods provide insights into different aspects of functionality.
Review the evaluation method options

<!-- page 200 -->
The agentic evaluation guided setup provides information about each evaluation
method, including what they're measuring and how they work. You can also review
the common questions in the sidebar for answers about the available metrics. Take
time to understand each method before selecting which ones to use.
Use multiple evaluation methods at a time
Choosing multiple evaluation methods can provide a better overall picture of the
agentic AI asset's performance. Different methods measure different aspects, such
as task completion rates, response accuracy, and tool execution success.
Consider task completion metrics for workflow validation
Task completion metrics help you verify that your agentic workflows successfully
complete their intended tasks and validate end-to-end workflow functionality.
Apply tool execution metrics for technical validation
Tool execution metrics verify that your agentic AI assets correctly use the tools and
APIs they're configured to access. This method helps ensure that integrations work
as expected.
Creating a dataset
Create targeted datasets that represent the scenarios and data your agentic AI assets will
encounter in production. Well-designed datasets provide more meaningful evaluation results.
Use filters to target the right data
Add filters to the execution logs to control exactly what you're measuring your
agentic workflow against. You can select See preview to see a list of records. You
can also use the check boxes to select individual records to measure against.
Generate new execution data for your evaluation run
When going through the agentic evaluation guided setup, you can create new
execution logs on multiple records before the evaluation begins. Use this option to
reduce time and ensure you have fresh data for evaluation.
Include diverse scenarios in your dataset
Create datasets that include various scenarios your agentic AI assets might
encounter, including edge cases and error conditions. Comprehensive datasets
help identify potential issues before they affect users.
Maintain dataset quality and relevance
Regularly review and update your evaluation datasets to ensure they remain
relevant to current use cases. Remove outdated scenarios and add new ones that
reflect changing requirements or data patterns.
Consider data volume for meaningful results
Include sufficient data volume in your datasets to generate statistically meaningful
results. Small datasets might not reveal performance patterns or issues that
become apparent with larger data sets.
Interpreting evaluation results
Understanding evaluation results helps you make informed decisions about improving your
agentic AI assets and identifying areas that need attention.
Analyze trends across multiple evaluation runs
Compare results from multiple evaluation runs to identify trends in performance.
Look for patterns that indicate improving or declining performance over time.
Focus on metrics that align with business objectives