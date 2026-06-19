## Exploring Now Assist Skill Kit

*Pages 3–13 of the source PDF*

accuracy, harm, and appropriateness for your use case, employ human oversight of output, and refrain from relying solely on AI-generated outputs for decision- making purposes. This is especially important if you choose to deploy this application in areas with consequential impacts such as healthcare, finance, legal, employment, security, or infrastructure. You agree to abide by ServiceNow’s AI Acceptable Use Policy , which may be updated by ServiceNow.

Data processing

This application requires data to be transferred from ServiceNow customers' individual instances to a centralized ServiceNow environment, which may be located in a different data center region from the one where your instance is, and potentially to a third-party cloud provider, such as Microsoft Azure. This data is handled

per ServiceNow's internal policies and procedures, including our policies available through our CORE Compliance Portal .

Data collection

ServiceNow collects and uses the inputs, outputs, and edits to outputs of this application to develop and improve ServiceNow technologies including ServiceNow models and AI products. Customers can opt out of future data collection at any time, as described in the Now Assist Opt-Out page.

Exploring Now Assist Skill Kit

Use the Now Assist Skill Kit plugin for Now Assist to create and activate custom prompts and skills for Now Assist.

Now Assist Skill Kit overview

Use Now Assist Skill Kit to create custom skills when base system Now Assist skills don't fit your needs. Custom skills enable you to have greater flexibility with Now Assist's generative AI capabilities.

Before you build a custom skill

Because you write and refine the prompts that drive your skills, you should be comfortable with the fundamentals of prompt engineering and with how a large language model (LLM) behaves.

Before you begin, you should understand:

•How an LLM produces output, including its probabilistic nature and the fact that the same prompt can produce different results on different models.

•How to write, test, and refine a prompt based on the output it produces, rather than on how you expect the model to interpret your wording.

•The use case you want to solve and the persona you're building the skill for.

Effective skill development depends on testing the prompt against representative data from your instance and refining it based on the results, not on a single example. For the full set of guidelines and the phases of building a skill, see General guidelines for Now Assist Skill Kit. For help defining requirements and outcomes before you build, see Scoping the skill.

Get Now Assist Skill Kit

To use Now Assist Skill Kit, you must update your Now Assist plugins in the Application Manager . For example, update your Now Assist for ITSM plugin to the latest available release.

You must also assign the sn_skill_builder.admin role to anyone who uses Now Assist Skill Kit.

Now Assist Skill Kit users

Now Assist Skill Kit Users

Now Assist Skill Kit workflow

The following diagram shows the user journey for Now Assist Skill Kit.

User journey for Now Assist Skill Kit

Define the provider

Understand the benefits and potential downsides of each large language model (LLM) that you're considering using.

Build the prompt

You must have an understanding of the architecture of your Now Assist instance and be able to define where input data should come from. You should also have an understanding of LLM fundamentals to build an effective prompt.

Test the prompt

Now Assist Skill Kit enables you to test your prompt from the editor.

Deploy the skill

Now Assist Skill Kit enables you to deploy your skill to Now Assist panel, Now Assist Context Menu, Virtual Agent, Flow Action, or a UI Action.

Now Assist Skill Kit benefits

Now Assist Skill Kit enables you to design your own custom generative AI functionality that is then easily deployed into the ServiceNow platform. Custom skills can augment workflows with generative AI to increase effectiveness and efficiency.

| User | Description |
| --- | --- |
| AI developer | Creates new skills, writes and refines the prompts, and configures the skill settings. This user must have the sn_skill_builder.admin role. Building an effective skill requires prompt engineering experience and an understanding of LLM behavior. |
| Now Assist admin | Reviews and activates published skills so that they're available at the configured touch points. This user must have the admin role. |

Now Assist Skill Kit benefits

What to explore next

To learn more about configuring and using Now Assist Skill Kit, see:

•Configuring Now Assist Skill Kit

•Using Now Assist Skill Kit

General guidelines for Now Assist Skill Kit

General guidelines are available to use Now Assist Skill Kit.

Now Assist Skill Kit guidelines overview

Think about the process of building a custom skill as having the following phases:

1.Scoping the skill

2. Collecting data and creating a dataset

Developing the prompt 3.

4.Conducting a performance evaluation

5. Deploying and monitoring the skill

The stages of building a custom skill

You should adopt a data-driven mindset while you build a skill. A data-driven mindset means emphasizing evidence-based decisions and minimizing speculation about how a large language model (LLM) can interpret the specific wording of a prompt.

Now Assist Skill Kit needs intermediate skills in prompt engineering. If you're not a developer, you should equip yourself with the relevant knowledge before working with this tool.

| Benefit | Feature | Users |
| --- | --- | --- |
| Create custom solutions by building a custom skill or workflow. | Create a skill | AI developer |
| Create and edit prompts for skills and configure where you want to bring in data from to augment your prompt. | Create a prompt | AI developer |
| Test and iterate on your skill before activating it. | Test a prompt | AI developer |

There’s information and helpful tooltips in many places throughout the product. Use this information to understand how to use the tool more effectively.

To ensure that there’s a proper segregation of duties, a developer or generative AI practitioner creates the skill and then publishes it. After the skill is published, a Now Assist Admin will activate the skill, so that it shows up at the configured touch points and is available to use.

Scoping the skill

Scoping the skill before you build it helps determine the requirements needed for the skill and the expected outcomes.

Before you begin

Before you start to build a custom skill with Now Assist Skill Kit, you should first review the base system skills that are available in the Now Assist Admin console. Use these pre-existing skills whenever possible.

User prerequisites

Now Assist Skill Kit is meant to be used by a developer or someone with experience using generative AI. Because you must write the initial prompt template, you should:

1.Be knowledgeable about prompt engineering, including:

◦Having familiarity with the development and testing of machine learning systems.

◦Having informed expectations about the behavior and capabilities of a prompted large language model (LLM). You should understand:

▪The fundamentally probabilistic nature of LLMs.

▪That performance can vary greatly across different LLMs and different target tasks.

◦Having experience or training with writing and evaluating prompts for LLMs.

Have an in-depth understanding of the use case that they’re trying to solve and the persona 2. that they’re building the skill for.

Design

Before you begin building a custom skill, you must think about the overall design and document the requirements. Consider the following:

1.What precisely do you want the skill to do?

◦What will be the inputs to the model?

◦What should be the outputs of the model? (Both content and format)

◦Who will be using the skill?

◦How can you characterize success?

2. What don't you want the model to do?

◦It’s useful to think about the possible risks and downsides of using generative AI outputs so that you can try to guard against them during development and testing.

◦It’s worth listing any specific model behaviors (LLM outputs) that would be detrimental or harmful in your specific use case.

Creating a dataset using Now Assist Skill Kit

Use these guidelines to create an effective dataset. Having an effective dataset provides better results for your prompt.

Now Assist Skill Kit dataset creation overview

A data-driven approach to skill development relies on the collection of a high-quality dataset to develop and test the skill. When you use Now Assist Skill Kit, you can also leverage the existing capabilities of the ServiceNow AI Platform to create a high-quality dataset.

When collecting data for this purpose, you should aim to create datasets that are:

1.Representative of the skill’s intended deployment environment. The data should:

◦Seek to reflect the expected distribution of inputs in the deployment environment.

◦Capture variance along several identified axes, for example, input length, urgency.

◦Include any examples of inputs that are known to be important to the use case.

◦Consider edge cases (which may be rare) but that are suspected to cause problems, for example, long examples.

Sized appropriately for the team’s risk appetite. 2.

◦It’s possible to develop and deploy a skill with little data. However, a lack of data creates more uncertainty about how the skill performs in deployment.

◦You should think like statisticians and produce confidence intervals for any associated performance scores and prompt comparisons.

3. Isolated from the data used for developing and writing the prompts.

◦You should split the data collected into development and testing sets. By splitting the data, you are protecting some data solely for evaluation purposes.

◦If you use all the data during the process of developing the prompt, your final evaluation of the skill is biased, meaning that it over-reports performance. This bias is because of a phenomenon known as prompt overfitting.

Developing the prompt

Use the guidelines to help create a prompt for your skill. A specific, clear, contextual prompt provides better results.

Prompt development overview

As a prompt engineer, you should make development decisions by looking at the model outputs that are generated in response to a prompt applied to many different inputs. However, there are still certain guidelines that may help users get started with prompt design.

1.Be specific

Define your desired outcome clearly. Be specific about the task that you want the model to fulfill. Clearly identify the inputs that you're providing to the model, and specify the output you’re expecting from the model (including formatting).

2. Include the right context

Provide background information and context relevant for fulfilling the task. This information can generate a more focused response.

3. Use clear language

Use precise and unambiguous language while writing the prompt.

4.Include demonstrations

If possible, experiment with providing completed examples, or demonstrations, in the prompt after the instructions to illustrate what you want the model to produce. Demonstrations are a powerful way to increase the likelihood of generating a desirable output. However, the performance changes depending on the demonstrations selected.

Start simple and test variations 5.

Break down complex tasks into smaller and clearer instructions. Have a controlled and iterative approach. Experiment with different structures.

Other considerations

•Subtle differences in wording can lead to substantial differences in performance. Trying to reason about how a large language model (LLM) may “interpret” the instructions in a prompt only gets you so far. Which specific choice of prompt-wording works best depends on the underlying model and should ideally be chosen based on evidence (that is, looking at lots of outputs).

•In data-constrained settings, you should iteratively develop several candidate prompts using the development data, then measure the performance of each candidate prompt on the test set, choosing the best one.

Evaluating the prompt

Evaluating the prompt is an ongoing process that occurs during and after prompt development and completion.

Prompt evaluation overview

To determine the effectiveness of your prompt, you should evaluate batches of test data. You should copy the model-generated responses and perform evaluations outside of Now Assist Skill Kit.

During prompt development

Ongoing, improvised evaluation should take place alongside the development of the prompt. This ongoing evaluation enables you to adapt the prompt based on observed model outputs. It may be tempting to test a change to a prompt against just one or two examples, however, to avoid reacting to noise, you should look at larger batches, and consider the statistical significance of the performance differences that you observed.

Final performance evaluation

Before you deploy a skill, you should test the prompt on a representative batch of data that was isolated from the development process, that is, “test” data. You want to use isolated test data because of a phenomenon known as prompt overfitting. Iteratively editing a prompt based on the model outputs generated on the same data that is used for testing can lead to significant over-estimates of performance. This result is because the prompt can become overspecialized to the specific examples used in development. Even though the effect is typically less dramatic than what occurs when fitting machine learn model parameters to a test dataset, it’s rooted in the same underlying principles, and should be avoided.

Evaluation metrics

Selecting the right metrics for evaluation is an important consideration. The following list provides a few approaches, each of which may be more or less appropriate depending on the use case.

•Classification-based assessment of short generations

This approach requires labeled records, and it works best when the labels are short, well- defined “right answers,” for example, true or false, multiple-choice, or category selection. In these cases, the model outputs can usually be parsed and formatted, then metrics like precision, recall, F1 scores, and so on can be directly calculated.

•Assessment of longer generations

Many of the most interesting generative AI use cases require longer model generations, and there are many possible “right answers.” In these cases, the output can be scored (by human evaluators) along several different axes, for example:

◦Faithfulness

Is the generated text faithful to the context provided in the skill prompt? (The opposite of faithfulness is hallucination, which is to say that the model injects out-of-context information.)

◦Correctness

Is the generated text correct relative to the skill instruction?

◦Helpfulness

Is the generated text helpful relative to the task that the skill wants to accomplish? (Helpfulness is subjective but it’s important to try to measure. Doing so properly requires a solid understanding of the needs of the people who will ultimately be using the skill.)

◦Fluency

Is the generated text grammatically correct? Does it have any typos, issues with coherency, and so on?

Note: It’s useful to score these properties on a scale, like 1-5, rather than with yes or no.

Deploying and monitoring the skill

After you evaluate the prompt, you can deploy the custom skill and monitor its effectiveness.

Now Assist Skill Kit deployment and monitoring overview

You should build and evaluate the skill in a subproduction instance. After you’re satisfied with the final performance evaluation on a batch of test data in subproduction, you can begin to move a skill toward deployment.

1.Identify the touch points where the skills can be surfaced to be available for the end user. Configure the deployment settings accordingly.

2. Perform end-to-end user testing in subproduction for a while and with different users and inputs.

3. After the results are acceptable, deploy the skill to the production instance.

4.Monitor the skill.

Example use case for Now Assist Skill Kit

As an AI developer, you can create custom skills with Now Assist Skill Kit. For this example, create a custom skill for child incident summarization.

As an AI developer, you must create a skill for child incident summarization. Creating this skill can help you organize and understand multiple incidents that are related to the same parent.

Create and configure the skill

To create the skill:

1.Navigate to All > Now Assist Skill Kit > Home.

2. Select Create new skill.

On the form, fill in the fields. The following information is used to fill in the form for this 3. example:

◦Skill name: Child incident summarization

◦Description: Summarization of child incidents

◦Default provider: Now LLM Generic

◦Provider API: Now LLM Generic

4.Select skill. Create

After you create the skill, you must configure the skill settings.

1.Select Configurations.

2. Select the model that you want to use. For this example, you can select llm_generic.

3. Select a temperature between 0-1 to determine the randomness and creativity of the output, such as 0.2.

Develop the prompt

After you create the skill and configure the settings, you must develop the prompt. To follow this example, you can use the following prompt:

You are a customer service representative. Summarize the child incidents of the below given parent incident. The summary should contain key issues and impact across the child incidents, highlighting any patterns, recurring problems, or significant outliers. When summarizing, please consider the following: Parent incident short description: {{incident.short_description}} Parent incident description: {{incident.description}} Here are the child incident details: {{ChildIncidents.output}}

Select the for the skill. For this example, the record is selected as the input. Inputs

Select insert inputs for the prompt.

For this example, the following is used:

Select the tools for the skill. For this example, select Flow Action and the IncidentDetailsFetcher flow resource.

| Parent incident short description: {{incident.short_description}} |
| --- |
| Parent incident description: {{incident.description}} Here are |
| the child incident details: {{ChildIncidents.output}} |

Configure the skill deployment options

The next step is to configure the skill deployment options. These options enable you to choose where to find the skill in Now Assist Admin.

1.Select the tab. Skill settings

2. Select Deployment Settings.

3. Enable the admin to enable the skill from the Core UI by selecting the UI Action check box.

4.Select Save.

Test and publish the skill

It is important to test your skill prompt to ensure that the correct type of data is being pulled in.

1.Select tests. Run

2. Choose a record or incident.

3. Select Run test.

Look at the response.

To see the data that was brought into the prompt from your skill inputs and tools, you can look at the grounded prompt tab.

If everything looks good, select prompt. After you finalize the prompt and you are ready Finalize to implement it, select Publish.


> **[Diagram: Now Assist Skill Kit – User Journey (4-Step Horizontal Banner), page 4]**
>
> Horizontal four-column workflow banner. Columns left-to-right with progressively lighter backgrounds:
>
> - **Column 1 (dark teal)**: "1. Define provider" — Icon: stacked layers with a green checkmark. Sub-text: "Select which LLM to use:" with bullets: "Now LLM Service", "3rd-party LLM", "Spokes: Azure OpenAI, WatsonX, etc."
> - **Column 2 (medium teal)**: "2. Build" — Icon: human head silhouette with a gear/wrench overlay. Sub-text: "Develop your skill by configuring:" with bullets: "Input sources", "Prompt", "Prompt setting (temperature, etc.)"
> - **Column 3 (lighter teal/grey)**: "3. Test" — Icon: checklist with two green tick marks. Sub-text: "Use data from your instance to test the prompt"
> - **Column 4 (light grey-green)**: "4. Deploy" — Icon: padlock with a wrench. Sub-text: "Make your skills available to users (Core UI and Workspace)"
>
> Right-pointing arrows connect each column.
