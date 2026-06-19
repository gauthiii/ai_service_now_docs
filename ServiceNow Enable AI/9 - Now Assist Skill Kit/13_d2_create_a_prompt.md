### Create a prompt

*Pages 25–35 of the source PDF*

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


> **[Screenshot: Now Assist Skill Kit – Add Skill Input Form (page 26)]**
>
> White form titled "Add skill input":
> - "Datatype * ⓘ" dropdown: "Record" ▼
> - "Table name * ⓘ" search field: "Incident" 🔍
> - "Name * ⓘ" text field: "Incident"
> - "Description" — empty text field
> - ☐ Mandatory, ☐ Truncate checkboxes
> - "Choose test record ⓘ" search field: "INC00XXXX" 🔍
> - Buttons: "Cancel" (grey) | "Add skill input" (teal/blue)

> **[Screenshot: Now Assist Skill Kit – Tool Editor Canvas with Decision Node (page 29)]**
>
> Four-tab interface: Prompt editor | **Tool editor** (active, teal underline) | Evaluations | Skill settings.
>
> **Left sidebar** — "Tools" section: two entries:
> - "myFlowAction1" [Flow Action] (teal badge)
> - "myscripttool1" [Script] (grey badge)
>
> **Right canvas** — Vertical flow diagram with blue "Run tools" button top-right and layout expand icon:
> 1. Teal filled circle: **"⊙ Start"**
> 2. Grey arrow ↓
> 3. Teal-outlined diamond: **"◇ Decision / mydecisionNode1"** (✏ × controls, (+) add branch)
> 4. Arrow branches left and right:
>    - Left → grey rectangle: **"□ Script / myscripttool1"** (✏ ×)
>    - Right → grey rectangle: **"⊡ Flow Action / myFlowAction1"** (✏ ×)
> 5. Both converge ↓ to purple-outlined box: **"🗂 Skill prompt / Prompt name"**
> 6. Arrow ↓ to dark circle: **"⊙ End"**
>
> Bottom-right: zoom/pan minimap with fit-to-view and zoom controls.

> **[Screenshot: Now Assist Skill Kit – Add Web Search as a Tool Modal (page 33)]**
>
> A 5-step wizard modal titled "Add web search as a tool" (✕ close). Step tracker: ① General info ✓ (green) → **② Tool inputs** (dark, current) → ③ Tool outputs → ④ Tool conditions (Optional) → ⑤ Summary.
>
> "Tool inputs" section:
> - **Search result type** radio buttons:
>   - ● **AI answers** – "Generates a single response to your search query using OpenAI, Perplexity or Gemini. Requires configuration key of a OpenAI or Gemini or Perplexity API." (selected)
>   - ○ **Searching and scraping** – "Generates multiple responses to your search query using Now LLM. Requires configuration of a scraping API. Default search is Bing, configuration is required for Google."
> - **AI Search Providers** — empty dropdown ▼
> - **Search query * ⓘ** — empty text field with 👁 and </> icons
> - **Sites or Domains ⓘ** — empty text field with 👁 and </> icons
> - **Max tokens ⓘ** — text field: "1000" with 👁 icon
> - **Filter attachments:** — label only (no field shown)
> - Buttons: "Cancel" | "Back" | "Continue" (disabled/grey)

> **[Screenshot: Now Assist Skill Kit – Add Predictive Intelligence as a Tool Modal (page 35)]**
>
> A 5-step wizard modal titled "Add predictive intelligence as a tool" (✕). Step tracker: **① General info** (active, green circle) → ② Tool inputs → ③ Tool outputs → ④ Tool conditions (Optional) → ⑤ Summary.
>
> "General info" section:
> - **Name ***: text field with value "PI"
> - **Type of solution** — dropdown (open) showing four options in a white dropdown list:
>   - Workflow Classification
>   - Workflow Similarity
>   - Classification
>   - **Similarity** (last item, no highlight)

> **[Screenshot: Now Assist Skill Kit – Add Document Intelligence as a Tool Modal (page 36)]**
>
> A 5-step wizard modal titled "Add document intelligence as a tool" (✕). Step tracker: **① General info** (active) → ② Tool inputs → ③ Tool outputs → ④ Tool conditions (optional) → ⑤ Summary.
>
> "General info" section:
> - **Name ***: text field: "Summarize"
> - Small helper text: "Use a short name to quickly identify the tool in the flow diagram"
> - **Action \*** — dropdown (open, green outline) showing three options:
>   - **Ask a Question** — "Ask a question about the file content"
>   - **Extract information** — "Pull structured data and insights from file content"
>   - **Summarize files** ✓ (highlighted teal) — "Generate a summary of the file content"
