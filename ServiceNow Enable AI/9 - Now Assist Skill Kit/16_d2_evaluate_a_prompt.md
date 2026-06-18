### Evaluate a prompt

*Pages 38–39 of the source PDF*

Test a prompt

After you create a prompt for your custom skill, test the prompt template before you finalize it. Testing the prompt verifies that you’re seeing the expected prompt results before it’s activated.

Before you begin Role required: sn_skill_builder.admin

Procedure

1.Navigate to > > Home. All Now Assist Skill Kit

Select the skill that you created the prompt for. 2.

3. In the Test prompt section, select Run tests.

4.Choose a test incident or record.

Select test. 5. Run

Note: Testing your skill consumes an assist.

Prompt results

If the skill is deployed as a flow, disable the system property 6.Optional: com.glide.oneapi.fdih.async.quick.mode, and then enable flow reporting. This property allows the generation of flow execution details when running flows, subflows, and actions from a custom skill. You can use flow execution details to test and troubleshoot your flow, subflow, or action. For more information about the system property, see Workflow Studio flow system properties .

7.Optional: Refine the prompt if you want, and repeat testing as necessary.

8.Optional: Select the run test history icon to see the results from your previous run tests.

What to do next After you test your prompt, you must finalize and publish it. To learn more about publishing a skill, see Finalize and publish a skill.

If you have not configured the deployment settings for your skill, see Configure skill deployment settings.

Evaluate a prompt

Use the Now Assist Skill Kit evaluation tools to evaluate the effectiveness of your skill prompts.

Before you begin Role required: sn_skill_builder.admin

| Tab | Description |
| --- | --- |
| Response | The response is the result that the large language model (LLM) sends back from the prompt. |
| Grounded prompt | The grounded prompt enables you to see the data that was brought into the prompt from your skill inputs and tools. With this view, you can see if your skill inputs and tools are returning the correct data. |

Procedure

1.Navigate to > > Home. All Now Assist Skill Kit

2. Select the skill that you want to evaluate.

3. Select the Prompt performance tab.

4.Select the tab. Evaluation runs

5. Create a dataset from a table or data collection.

Create a data set

6.Select the add icon for Evaluation Runs.

7.Give the evaluation run a name and description.

8.Select one or more prompts that you want to evaluate.

9.Select Save & Next.

10.Select a dataset.

Select Next. 11. Save &

Expand the tab. 12. Quality

13.Select the metrics that you want to evaluate.

Evaluation metrics

Human Human Feedback Human evaluation is the default option available for all prompt executions that generate a response.

| Method | Steps |
| --- | --- |
| Create a dataset from a table | a.Give the dataset a name and description. b.Select Table. c.Find the table that you want to use. d. Select the maximum number of records that you want to use. e. Add conditions. f.Select Generate Preview. g.Select the mappings. h.Select Create. |
| Create a dataset from a data collection | a.Give the dataset a name and description. b.Select Data Collection. c.Select a data collection that you created in Now Assist Data Kit. d. Select Generate Preview. e. Select the mappings. f.Select Create. |

| Evaluation method | Metric | Description |
| --- | --- | --- |
