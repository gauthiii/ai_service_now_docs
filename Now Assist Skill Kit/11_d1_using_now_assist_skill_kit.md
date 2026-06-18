## Using Now Assist Skill Kit

*Pages 20–42 of the source PDF*

c.Apply role restrictions to the skill.

Continue creating the skill. d.

Using Now Assist Skill Kit

Use Now Assist Skill Kit to create and publish prompts and custom skills for Now Assist.

Building a custom skill in Now Assist Skill Kit is a sequential process. The following steps take you from an empty skill through to activation, where end users can trigger it from the platform.

Create a skill

Create a skill or clone an existing base system skill. Clone a Now Assist skill if it's close to what you need but requires modification.

•Create a skill

•Clone and edit a ServiceNow skill

Build the prompt

A prompt is an instruction template sent to the AI model when the skill runs. Define what information the skill receives as inputs, write the prompt text, and optionally add tools that gather additional context before the prompt executes.

•Create a prompt

•Add a tool

•Add a retriever

•Add a web search

•Use prompt assistance

Test and evaluate

Before publishing, test your prompt against real records on your instance to verify the output. You can also run a formal evaluation, which measures output quality against expected results using correctness and faithfulness scores.

•Test a prompt

•Evaluate a prompt

Publish and activate

When your skill is ready, finalize the prompt and publish it. Publishing makes the skill visible to a Now Assist admin, who then activates it in Now Assist Admin to make it available to your users.

•Finalize and publish a skill

•Activate a skill

Call a skill from a script

After a skill is published, you can call it from a server-side script, allowing you to integrate the skill into automated workflows or business rules.

•Call a custom skill from a script

Create a skill

Create a custom skill for Now Assist. Creating a custom skill enables you to have greater flexibility with Now Assist's generative AI capabilities.

Before you begin Role required: sn_skill_builder.admin

Note: When you update Now Assist Skill Kit you should also update Generative AI Controller to ensure that your skills continue to perform correctly.

Procedure

1.Navigate to > > Home. All Now Assist Skill Kit

2. Select Create new skill.

3. On the form, fill in the fields.

New skill form

Default provider Available providers:

◦Now LLM Service

◦External LLM

You can use Now LLM Service, Now LLM Long Term Stable models (LTS), Azure OpenAI, Google Gemini or Anthropic Claude on AWS as the AI model provider for all Now Assist skills and AI agents. Use the Configuration Controls in AI Control Tower to define which options are available,

| Field | Description |
| --- | --- |
| Skill name | A name for the skill. |
| Description | A description of the skill. |

4.Select how you want to create the prompt for the skill.

◦Write from scratch

◦Choose one from library

| Field | Description |
| --- | --- |
|  | then set the skill-level preferences in the Now Assist Admin console. For more information, see Large language models on the ServiceNow AI Platform. ▪Spokes ▪Custom LLM For more information on setting up a custom large language model (LLM), see Configure a generic large language model (LLM) connector Available prebuilt spokes that enable you to connect with an external LLM: ◦Microsoft Azure OpenAI Generative AI Spoke ◦OpenAI Generative AI Spoke ◦Aleph Alpha ◦WatsonX ◦Google Gemini (MakerSuite and Vertex AI) Note: The spokes don't consume Integration Hub transactions. The spokes consume assists. |
| Provider API | The provider of the API for your chosen LLM. |
| User access | ◦Any authenticated user As long as a user is logged in, they can access and execute the skill. ◦Select roles Select the roles that a user must have to execute the skill. Note: If you select multiple roles, a user must only have one of the roles to execute the skill. |
| Role restrictions | Role restrictions define the specific roles under which a skill in ServiceNow executes. While ACLs determine which user roles are permitted to trigger the skill, role restrictions determine the roles the skill will operate with during execution. |

a.Find the prompt that you want to use.

b.Select View.

c.Select Use prompt.

◦Use an AI-generated prompt

Select Next. 5.

6.Optional: Add skill inputs and outputs.

7.Select Go to summary.

8.Select Finish.

What to do next After you create the skill, you must configure it. To learn more about configuring a skill, see Configure a skill prompt.

If you don't need to set any configurations for your skill, you can create your skill prompt and tools. To learn more, see Create a prompt and Add a tool.

Clone and edit a ServiceNow skill

Eligible skills provided in ServiceNow Now Assist applications can be cloned in Now Assist Skill Kit so that you can edit the prompt or change the AI service provider. Editing the prompt enables you to arrange the formatting and content of the LLM response.

Before you begin Role required: sn_skill_builder.admin

Procedure

1.Navigate to All > Now Assist Skill Kit > Home.

Select ServiceNow 2. skills

Select the ServiceNow skill that you want to clone. 3.

4.Select Clone Skill.

Fill in the fields on the form. 5.

Clone skill form

6.Select Clone.

Note: When you clone a skill, you can't change the skill outputs, tools, or deployment settings.

7.Select the edit or add icon to add skill inputs.

Add skill inputs form

| Field | Description |
| --- | --- |
| Skill name | A name for the skill. |
| Description | A description of the skill. |
| Default provider | Available providers: ◦Now LLM Service ◦External LLM ▪Spokes ▪Custom LLM For more information on setting up a custom large language model (LLM), see Configure a generic large language model (LLM) connector Available prebuilt spokes that enable you to connect with an external LLM: ◦Microsoft Azure OpenAI Generative AI Spoke ◦OpenAI Generative AI Spoke ◦Aleph Alpha ◦WatsonX ◦Google Gemini (MakerSuite and Vertex AI) Note: The spokes don't consume Integration Hub transactions. The spokes consume assists. |
| Provider API | The provider of the API for your chosen LLM. |

| Field | Description |
| --- | --- |
| Dataype | Select the datatype for the input. |
| Name | The name of the skill input. |
| Description | A description of the skill input. |
| Make input mandatory check box | Select this box if the input must be provided for the skill to run. |

Edit inputs form

8.Select input. Add skill

9.Optional: Select Clone prompt to edit the prompt. You will see all of the prompts that use the same supporting skill for each provider.

10.Add conditions. Prompt usage These are conditions that determine when a prompt will be executed.

To test the prompt, select and add test values. 11. Run test

Select the tab. 12. Skill settings

13.Optional: Select General information to change the default provider by selecting the toggle.

What to do next Create your skill prompt. To learn more about creating a prompt, see Create a prompt.

After you clone and edit the skill and prompt, you can evaluate your prompt.To learn more about evaluating a prompt, see Evaluate a prompt.

Create a prompt

After you create a custom skill, create a prompt. Creating a prompt enables you to choose what skill inputs to use, as well as the type of tool.

Before you begin Role required: sn_skill_builder.admin

Procedure

1.Navigate to > > Home. All Now Assist Skill Kit

Select the skill that you want to create a prompt for. 2.

Select the edit icon ( ) and name the prompt. 3.

4.Write the prompt.

5. Select Skill Inputs.

| Section | Description |
| --- | --- |
| Base input table fields | Each skill relies on a base input table and input fields with descriptions to provide context for the LLM to generate a response. |
| Rule conditions | Rule conditions determine when the input template is used. By default, record state determines which input template the LLM uses. |
| Additional input data sources | You can add input data sources like related tables, activity streams and relationships to provide more context to the LLM. You can also add rule conditions to these additional data sources. |

Skill input options

| Input type | Description |
| --- | --- |
| Datatype | ◦Record ◦String ◦Numeric ◦Boolean ◦Simple Array ◦JSON Object ◦JSON Array |
| Name | A name for the input. |
| Description | A description for the input. |
| Mandatory | The Mandatory option means that you must supply a value for the input when you run the skill. |
| Truncate | The Truncate option means that, if your prompt is too large, the prompt context is shortened to fit the model context length. |
| For Records |  |
| Table name | A name for the table. |
| Choose test record | The record that is used to test the prompt. |
| For Strings, Numeric. Boolean, Simple Array, JSON Object, JSON Array |  |

6.Select input. Add skill

7.Select Insert inputs. The input options change depending on what kind of data type you choose.

8.Search for the inputs that you want to use for the prompt. For example, you can search for the incident short description or priority.

9.If you're not ready to finalize the prompt and publish the skill, select or as. Save Save

Note: Skills can have multiple prompts. Usage conditions determine which prompt is executed. If no conditions are met, the default prompt is executed. To configure prompt usage conditions, see Configure a skill prompt.

What to do next After you have created a prompt, you must test it. To learn more about testing your prompt, see Test a prompt.

Add a tool

Add and manage tools visually in the Tools editor, including decision branching, to execute different tools for your skill. Adding decision branches between tools enables you to define the conditions that need to be met for a tool to run. If no conditions are met, the default branch's step is executed.

Before you begin Role required: sn_skill_builder.admin

About this task A tool is a utility that is configured to convert skill inputs into skill outputs. The tool outputs can be referenced in a prompt template to introduce context to a prompt. The input for a tool can be a skill input or the output of another tool.

You can use the Tool editor to configure tools and link them to each other.

Decision nodes enable you to execute different tools, based on the logic of the branch. A decision node can contain multiple branches but will always need one default branch.

Procedure

1.Navigate to All > Now Assist Skill Kit > Home.

2. Select the skill you want to add a tool to.

Select the tab. 3. Tool editor

4.Select (+) icon to add a node.

5. Select the type of node that you want to add.

Add a node

a.Select a tool type. Tool node b.Name the tool. Types of tool: c.Select a condition.

| Input type | Description |
| --- | --- |
| Test values | The values that are used to test the prompt. |

| Node type | Steps |
| --- | --- |

| Node type | Steps |
| --- | --- |
| ◦Script ◦SubFlow ◦Flow Action ◦Retriever ◦Skill ◦Web search Note: If you select Google as your web search tool provider, the web search tool leverages Grounding with Google Search , offered under a Global Standard deployment. Because grounding is not data resident , Google's global infrastructure routes traffic to a global data center for each web search request. This processing may be different than your data processing location chosen for your ServiceNow instance. Please consider your organization's data policies before enabling skills that have Google web search tools. ◦Predictive Intelligence |  |
| Decision node | a.Name the node. b.Select Add branch i. Name the branch. ii.Select a Destination node. iii. Set the conditions. c.Select a Destination node. |

| Grounding with Google Search |  |
| --- | --- |

| data resident |  |
| --- | --- |

6.Select Add.

7.Select to test the tools. Run tools

Add a retriever

Add a retriever to your prompt to augment and add context to your prompts with AI search results.

Before you begin Role required: sn_skill_builder.admin

About this task Using a retriever in a skill enhances the relevance and coherence of a response by pulling relevant information from a source and then feeding it to a large language model (LLM) to create the final output. This process leads to smoother conversational flow and better scalability as data grows, without requiring model fine-tuning.

A retriever enables the chatbot to access external knowledge by fetching relevant background information, resulting in more factual, in-depth, and informed responses.

Procedure

1.Navigate to All > Now Assist Skill Kit > Home.

2. Create a new skill or select the skill that you want to add a retriever to.

Select the tab. 3. Tool editor

4.Select (+) icon to add a node.

Select node. 5. Tool

6.Select Retriever from the drop-down menu.

7.Select Configure retriever.

8.On the form, fill in the fields.

Add tool form

9.Select Next.

10.Select an embedding model. To learn about embedding models, see Configuring an external or custom embedding model .

11. If you selected Hybrid or Semantic search criteria, select a semantic index. A semantic index enables you to search for data based on contextual meaning.

12. Optional: If you selected Hybrid or Semantic search criteria, select Advanced to change the document matching threshold. The document matching threshold is the threshold for semantic matching. The default value is 0. You can input any value from 0 to 1. You can get more precise results with a higher value.

13.Select Next.

| Field | Description |
| --- | --- |
| Name | The name for the retriever. |
| Search query | The information that you want to search for. It can be static text or a skill input. |
| Search space type | ◦Table-based ◦Search-profile-based |
| Search profile | A group of search sources. |
| Search sources | Tables in ServiceNow that have been indexed and can be used for search. |
| Fields returned | The fields that you want returned from the search sources and sent to the large language model (LLM). |
| Limit | The maximum number of results that are returned. |
| Search criteria | ◦Hybrid ◦Semantic ◦Keyword Note: If you choose Hybrid or Semantic, you can make selections for chunking and reranking. To learn more about chunking and reranking, see Retriever chunking and reranking. |

Note: If you selected or search criteria, see Retriever chunking and Hybrid Semantic reranking to complete setting up your retriever.

14.Review the retriever tool information.

15.Select Add tool.

Retriever chunking and reranking

When you’re building a skill prompt that uses a retriever you can use chunking and reranking to enhance the accuracy and relevance of your responses.

Before you begin Role required: sn_skill_builder.admin

About this task To set up the chunking and reranking options for a retriever, you must have a retriever tool added to your skill with the Hybrid or Semantic search criteria. The following steps come after the semantic configuration in Add a retriever.

Procedure

1.Navigate to All > Now Assist Skill Kit > Home.

2. Select the skill that you’re adding a retriever to.

Add a retriever. 3.

4.On the form, fill in the fields.

Chunking and reranking form

| Field | Description |
| --- | --- |
| Max number of chunks per document | The maximum number of chunks that you want returned per document. The default value is 10. |
| Chunking strategy | ◦Fixed size Fixed size breaks down the full text into smaller passages. You can choose the passage size limit in number of words or number of sentences. ◦Small to big Small to big enables you to choose the top K best matched indexed chunks and expand them to include surrounding chunks. Then the expanded chunks are linked together into a large text and broken into smaller passages. Don’t use the small to big chunking strategy if you’re using full text or truncate index chunking configuration. |

Select Next. 5.

6.Select the type of condition that you want to be evaluated when the tool is executed.

7.Select Next.

8.Review the selections that you made for the tool and select tool. Add

Add a web search

Add a web search as a tool in Now Assist Skill Kit. Adding a web search as a tool enables you to add search results to your prompt.

Before you begin Role required: sn_skill_builder.admin or admin.

To use web search as a tool, you must bring your own search engine API key and configure it on the ServiceNow AI Platform.

Procedure

1.Navigate to All > Now Assist Skill Kit > Home.

Create a skill or select the skill that you want to add web search to. 2.

3. Select the Tool editor tab.

4.Select the (+) icon to add a node.

5. Select Tool node, and then Add.

6.Select in the field. Web Search Tool type

7.Select Configure tool.

8.On the General info form, enter a Name and select Web Search for the Resource field.

9.Select Continue.

10.On the Tool inputs form, fill in the fields.

| Field | Description |
| --- | --- |
| Chunking unit | ◦Words ◦Sentences |
| Chunk size | The size of the chunks that are returned. The default value for word size is 750. The default value for sentence size is 40. |
| Expanded snippet size | The size of the expanded chunks that are included when you select the small to big chunking strategy. |
| Top K results | The number of chunks the reranker returns. If you leave this field empty, the default number of chunks that are returned will be the limit you entered. |

Web search configuration form

AI search providers The AI search provider used to perform the search.

| Field | Description |
| --- | --- |
| Search result type | AI answers is the type of result that you want from the search. AI answers generates a single response to the search using either Perplexity, OpenAI, or Gemini. |

11. Select Continue.

12. On the Tool outputs form, select Continue.

13.On the Tool conditions (optional) form, select Continue.

14.On the Summary screen, select tool. Add

Add Predictive Intelligence

Add predictive intelligence as a tool in Now Assist Skill Kit. Predictive intelligence models enable you to predict, estimate, and identify patterns that can be used to route work, populate forms, estimate wait times, and more.

Before you begin Role required: sn_skill_builder.admin

Procedure

1.Navigate to All > Now Assist Skill Kit > Home.

2. Create a skill or select the skill that you want to add predictive intelligence to.

Select the tab. 3. Tool editor

| Field | Description |
| --- | --- |
|  | Note: If you select Perplexity or OpenAI, you must complete the API key setup in the AI Search answers OneExtend capability table. For more information on that process, see Configure AI Search answers capability for web search. Although Azure Open AI is an option to select, Azure Open AI doesn't support web search. If you select Google as your web search tool provider, the web search tool leverages Grounding with Google Search , offered under a Global Standard deployment. Because grounding is not data resident , Google's global infrastructure routes traffic to a global data center for each web search request. This processing may be different than your data processing location chosen for your ServiceNow instance. Please consider your organization's data policies before adding a web search tool with Google as the provider. |
| Search query | The word, words, or phrase you’re searching for. |
| Sites or domains | This field appears but it's not supported. |
| Max tokens | This field appears but it's not supported. |

4.Select (+) icon to add a node.

Select node. 5. Tool

6.Select Predictive Intelligence.

7.On the form, fill in the fields.

Predictive intelligence form

8.Add tool inputs.

9.Add tool outputs.

Select tool conditions. 10.Optional:

Select tool. 11. Add

Add Document Intelligence

Add Document Intelligence as a tool in Now Assist Skill Kit to extract structured data from documents as part of your skill's execution flow

Before you begin Role required: sn_skill_builder.admin

Procedure

1.Navigate to > > Home. All Now Assist Skill Kit

Create a skill or select the skill that you want to add document intelligence to. 2.

3. Select the 2. Add tools tab.

| Field | Description |
| --- | --- |
| Name | The name of the tool |
| Type of solution | ◦Workflow classification ◦Workflow similarity ◦Classification ◦Similarity |

4.Select (+) icon to add a node.

Select node. 5. Tool

6.Select Document Intelligence.

7.On the form, fill in the fields.

Add document intelligence form

8.Add tool inputs.

9.Add tool outputs.

10.Optional: Select tool conditions.

Select tool. 11. Add

Use prompt assistance

Use prompt assistance to get a jump start with your prompt development by selecting an example from the prompt library or using Now Assist to generate one.

| Field | Description |
| --- | --- |
| Name | A name to identify the tool. |
| Action | ◦Ask a Question Ask a question about the file content. ◦Extract information Pull structured data and insights from file content. ◦Summarize files Generate a summary of the file contents. |

Before you begin Role required: sn_skill_builder.admin

Procedure

1.Navigate to > > Home. All Now Assist Skill Kit

2. Create a new skill or select the skill that you want to use prompt assistance for.

3. Select the prompt assistance icon.

4.Select the Library tab to search for a prompt from the prompt library.

5.

6.Select the AI generated tab to have AI help you create a prompt based on your needs.

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

14.Select Save & Next.

15.Review the evaluation choices that you made.

Select Evaluate. 16. Save &

17. Optional: Give a human evaluation.

a.Select Human evaluation.

b.Select a record to use in the evaluation.

c.Expand the prompt and read the result.

d. Select the thumbs up or thumbs down icon to give your evaluation.

e. Add more information and select Submit.

Finalize and publish a skill

When you’re satisfied with your prompt, you can publish your custom skill. Publishing the skill enables a Now Assist admin to activate it.

Before you begin Role required: sn_skill_builder.admin

Procedure

1.Navigate to > > Home. All Now Assist Skill Kit

2. Select the skill that you want to publish.

| Evaluation method | Metric | Description |
| --- | --- | --- |
|  |  | You can rate the response with a thumbs up or thumbs down, based on your satisfaction. You also have the option to provide more detailed feedback to explain your evaluation choice. |
| Automated | Correctness | The correctness metric assesses the generated response's accuracy, completeness, pertinence, and writing quality relative to the given instruction. This metric helps to check that the text accurately reflects the instruction, covers all important points, remains relevant, and is well written. |
| Automated | Correctness with Golden Response | The correctness with golden response metric uses a predefined reference to assess the generated response's accuracy, completeness, pertinence, and writing quality relative to the given instruction. This metric helps to check that the text accurately reflects the instruction, covers all important points, remains relevant, and is well written. You should use this metric whenever possible. |
| Automated | Faithfulness | The faithfulness metric assesses whether a generated response accurately reflects the information and context provided in the given instruction. This metric helps to check that the text contains no hallucinations, fabricated facts, or unsupported conclusions, maintaining alignment with the source material. |

Make any necessary changes to the prompt. 3.

4.If you have changed the prompt, test it.

5. When you're satisfied with your prompt, select Finalize prompt.

6.Select Publish.

What to do next A Now Assist admin must activate the skill. To learn more about how to activate a skill, see Activate a skill.

Activate a skill

After you create and publish a custom skill, you must activate it in Now Assist Admin. Activating the skill enables you to trigger the skill within the UI.

Before you begin Role required: admin

Procedure

1.Navigate to All > Now Assist Admin > Features.

Find the custom skill that you created. 2.

Select skill. 3. Activate Make sure you are in the correct application scope when you activate the skill. To learn more about application scopes, see Application scope .

Note: Some skills might need to be reviewed and approved by a data steward before you can activate it.

What to do next You can enable Now Assist Guardian for your skills. To learn more about Now Assist Guardian, see Now Assist Guardian

Call a custom skill from a script

You can use a script to call a custom skill.

Before you begin Role required: admin

Procedure

1.Navigate to > > Actions. All System UI UI

2. Create a UI action. For more information on creating UI actions, see Create a UI action .

Add your script. 3.

The following script is an example. You can replace the variables with your data.

| var inputsPayload = {}; |
| --- |
|  |
| // create the payload to deliver input data to the skill |
|  |
| inputsPayload[‘input name’] = { |
|  |
| tableName: 'table name', |
|  |
| sysId: 'sys_id', |
|  |
| queryString: '' |
|  |
| }; |
|  |
| //create the request by combining the capability sys ID and the skill config sys ID |
|  |
| var request = { |
|  |
| executionRequests: [{ |
|  |
| payload: inputsPayload, |
|  |
| capabilityId: ‘capability sys id’, |
|  |
| meta: { |
|  |
| skillConfigId: ‘skill config sys id’ |
|  |
| } |
|  |
| }], |
|  |
| mode: 'sync' |
|  |
| }; |
|  |
| //run the custom skill and get the output in a string format |
| try { |
| var output = sn_one_extend.OneExtendUtil.execute(request)['capabilities'][r equest.executionRequests[0].capabilityId]['response']; |
| var LLMOutput = JSON.parse(output).model_output; |
| } catch(e) { |
| gs.error(e); |
