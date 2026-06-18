# Now Assist Skill Kit

*Pages 1–45 of the source PDF*

Contains Roles

List of roles contained within the role.

None.

Groups

List of groups this role is assigned to by default.

None.

Special considerations

None.

Now Assist Data Kit roles (sn_data_kit.admin)

This user can create, update, and publish datasets in Now Assist Data Kit. This role is mandatory to use Now Assist Data Kit.

Contains Roles

List of roles contained within the role.

None.

Groups

List of groups this role is assigned to by default.

None.

Special considerations

None.

Now Assist Skill Kit

® Use ServiceNow Now Assist Skill Kit to create and publish custom prompts and skills for Now Assist. Creating custom skills and prompts enables you to have greater flexibility with Now Assist's generative AI capabilities.

https://player.vimeo.com/video/985874233? h=2ccc18794b&badge=0&autopause=0&app_id=58479

Get started

Important:

•Not all model providers are available for customers with in-country SKUs, and some Now Assist products/features are currently unavailable for in-country customers. For more information, see the KB1584492 article in the Now Support Knowledge Base. Be sure to check for model provider availability updates in future releases.

•Some Now Assist products/features are currently unavailable for customers in the FedRAMP, NSC DOD IL5, or Australia IRAP-Protected data centers, self-hosted customers, or in other restricted environments. For more information, see the KB0743854 article in the Now Support Knowledge Base. Be sure to check for availability updates in future releases.

•Some Now Assist products/features are currently available only for customers in some regions. Be sure to check for availability updates in future releases.

•Some AI products and skills are not available in Regulated Markets. For more information, see KB2593939: Regulated Markets AI Products/Skills Not Available . Be sure to check for availability updates in future releases.

Troubleshoot and get help

•Ask questions and explore other resources for Now Assist Skill Kit in the ServiceNow Community

•Search the Known Error Portal for known error articles

•Contact Customer Service and Support

AI limitations

This application uses artificial intelligence (AI) and machine learning, which are rapidly evolving fields of study that generate predictions based on patterns in data. As a result, this application may not always produce accurate, complete, or appropriate information. Furthermore, there is no guarantee that this application has been fully trained or tested for your use case. To mitigate these issues, it is your responsibility to test and evaluate your use of this application for

| Explore Learn more about Now Assist Skill Kit and creating effective prompts. | Configure Configure Now Assist Skill Kit prompt and deployment settings. |
| --- | --- |
| Use Use Now Assist Skill Kit to create custom skills. |  |

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

Activate the skill

After you test, finalize, and publish your skill, an admin must activate it in Now Assist Admin. To learn more about activating skills, see Activate a skill.

Security for Now Assist Skill Kit

Enable security controls for Now Assist skills and custom skills through access control lists (ACLs) and role restrictions.

Access control lists

The access control lists in Now Assist Skill Kit enhance the security of Now Assist skills and are set to determine users who can invoke a skill.

Configure ACLs in Now Assist Skill Kit

You can configure ACLs for Now Assist Skill Kit when you create or edit a skill or when you activate a skill from Now Assist Admin console.

ACLs configured in Now Assist Skill Kit for are Allow-If and role-based.

The Allow-If logic grants access to data or resources if any of the conditions in the ACL are met. The other type of ACL is Deny-Unless. Deny-Unless ACLs block access to data or resources unless a condition is met, even if there are other conditions like Allow-If ACLs that would normally grant someone access.

There are two possible options for ACLs created in Now Assist Skill Kit:

•Any authenticated user: Grants access to any user authenticated on the instance, regardless of role

•Select roles: Requires you to select the roles that grant access

Each skill must have its own unique ACL. You can't create a skill or save changes to a skill without an ACL. To configure an ACL for a skill, see Configure security controls for a skill.

Role restrictions

Role restrictions define the specific roles under which a skill in ServiceNow executes. While ACLs determine which user roles are permitted to trigger the skill, role restrictions determine the roles the skill will operate with during execution.

For example, if a skill has and ACL of itil-admin and a role restriction of itil, only users with the itil_admin role can trigger the skill. However, when the skill is executed, it will execute with the permissions and access of the itil role.

Role restrictions for skills enhances security by enabling users to limit their users during skill execution, verifying that skills run with least-access privileges.

To configure role restrictions for a skill, see Configure security controls for a skill.

Configuring Now Assist Skill Kit

Configure prompts and skills for Now Assist Skill Kit.

Configuration overview

To use Now Assist Skill Kit, you must update your Now Assist plugins in the Application Manager . For example, update your Now Assist for ITSM plugin to the Xanadu release.

After you install the plugin, there are two parts to configuring a skill in Now Assist Skill Kit. First, you must configure how to deploy the skill. Next, you must configure the prompt.

Configure a skill prompt

Configure your skill prompt to set the model that is used and the randomness and creativity of the response.

Before you begin Role required: sn_skill_builder.admin

Procedure

1.Navigate to All > Now Assist Skill Kit > Home.

Select the skill that you want to configure. 2.

Select Configurations. 3.

4.On the form, fill in the fields.

Configurations form

5. Add Usage conditions to determine when to use the prompt.

What to do next After you configure your skill settings, you can test your skill. To learn more about testing skills, see Test a prompt.

To learn more about configuring the skill, including models and tokens, see Now Assist Skill Kit FAQs on the ServiceNow Community.

Configure skill deployment settings

Configure the deployment settings for the skill that you create. The deployment settings enable you to choose where the admin can find the skill in Now Assist Admin.

Before you begin Role required: sn_skill_builder.admin

Procedure

1.Navigate to > > Home. All Now Assist Skill Kit

2. Select the skill that you want to configure.

| Field | Description |
| --- | --- |
| Model | The model is the large language model (LLM) that you want to use for the prompt. |
| Temperature | The temperature determines the randomness and creativity of the output. A higher value increases the randomness. The value must be between 0-1. |
| Thinking mode | Thinking mode controls how much reasoning effort a large language model applies when it generates a response. Higher levels improve output quality but increase latency. You can select thinking mode when you use llm_generic_small_v2 or llm_generic_large_v2. |
| Maximum response tokens | The maximum number of tokens the model can return. If you’re using Now LLM Service, the maximum is 1000. |
| Maximum request tokens | The maximum number of tokens allowed in a request. |
| Structured output | Structured outputs return prompt responses in a consistent JSON format. Note: Only Google Gemini and Azure OpenAI support structured output. |

Select the tab. 3. Skill settings

4.Select information. General This section shows the information that you added when you created the skill. You can edit the skill name and description here.

5. Select Deployment Settings.

6.On the form, fill in the fields.

Deployment settings form

7.Select where you want the admin to enable the skill from.

| Field | Description |
| --- | --- |
| Workflow | The high-level category that this skill pertains to, such as Technology, Employee, Creator, or Platform. You can also select Other if none of the categories fit. The workflow that you choose is where the skill appears in the Now Assist Admin console. |
| Product | The specific product that this skill operates within, such as ITSM, ITOM, HR Service Delivery, Now Assist Admin. |
| Feature | The feature that the skill is used on, such as Agent Chat, Knowledge, Virtual Agent. You can also define a custom feature if necessary. |
| Name | The name of the feature. |
| Description | A description of the feature. |

◦Now Assist Panel

◦UI Action

◦Flow action

◦Now Assist context menu

◦Virtual assistant

For more information about Now Assist in Virtual Agent, see Configuring assistants overview .

◦UI Builder

8.Select Save.

What to do next After you configure the skill settings, you can publish your skill. To learn more about publishing skills, see Finalize and publish a skill

Example deployment with Workflow Studio

As an AI developer, you can deploy custom skills with many integrations, including Workflow Studio.

Deploy a skill with Workflow Studio

Before you can deploy a skill, you must complete the following steps:

1.Create the skill.

Create the prompt. 2.

To deploy the skill:

1.Navigate to settings. Skill

Select settings. 2. Deployment

3. Select a workflow.

4.Select a product

Select a feature. 5.

6.Select where you want the admin to enable the skill from. For this example, select Workflow Studio.

Execute the skill

To execute the skill:

1.Finalize and publish the skill.

Activate the skill. 2.

3. Navigate to Workflow Studio.

4.Add the Execute Skill action .

Configure security controls for a skill

You must define an access control list (ACL) and role restrictions for all skills. An ACL enables you to restrict who is able to access and execute a skill to only users with the correct role. Role restrictions enable users to limit roles during skill execution.

About this task If you have an existing skill that does not have an ACL, the execution of the skill is not disrupted. However, if you edit the skill and republish it, you must add an ACL.

If you try to execute a skill when you don’t have permission, you see an error that you aren’t authorized.

Before you begin Role required: sn_skill_builder.admin

Procedure

1.Navigate to All > Now Assist Skill Kit > Home. A modal appears to explain ACLs. You can select or ACLs. Got it View skills without

2. Add an ACL and role restrictions to an existing skill.

a.Select the skill that you want to add an ACL to.

b.Select the tab and then select controls. Deployment and skill settings Security

c.Select Add ACL.

d. Select an option.

Options for ACL roles

e. Add role restrictions.

f.Select Apply.

Add an ACL to a new skill. 3.

a.Create a skill.

b.In the Configure security controls section, select an option for the access control list.

| Option | Description |
| --- | --- |
| Any authenticated user | As long as a user is logged in, they can access and execute the skill. |
| Select roles | Select the roles that a user must have to execute the skill. Note: If you select multiple roles, a user must only have one of the roles to execute the skill. |

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

Now Assist Skill Kit reference

Reference topics for Now Assist Skill Kit

Now Assist Skill Kit roles

Certain roles are required to use Now Assist Skill Kit functionality.

Skill kit admin (sn_skill_builder.admin)

This user can create, update, and publish skills in Now Assist Skill Kit. This role is mandatory to use Now Assist Skill Kit.

Contains Roles

List of roles contained within the role.

None.

Groups

List of groups this role is assigned to by default.

None.

Special considerations

None.

Skill Kit model admin (sn_skill_builder.sb_model_admin)

This user can create and update custom large language models.

Contains Roles

List of roles contained within the role.

None.

Groups

List of groups this role is assigned to by default.

None.

Special considerations

None.

Field of use for Now Assist Skill Kit

Now Assist Skill Kit is included in various Now Assist packages that cover a given customers’ ability to build Now Assist skills.

| gs.addErrorMessage('Something went wrong while executing the skill.'); |
| --- |
| } |
| action.setRedirectURL(current); |

The following table is provided to help clarify questions regarding how such custom skills can be created and deployed in each customer environment.

Expected field of use

Web search custom skill

The web search custom skill performs an internet search to answer a query. Web search is used whenever the LLM and AI Search are unable to provide results or whenever web search mode is activated.

The web search custom skill is based on a prebuilt topic block in Virtual Agent Designer, and is available when you turn on Now Assist in Virtual Agent. This feature is automatically triggered when both AI Search and the LLM can't find information to answer an end user's query. This feature can also be manually triggered whenever end users select the Web search results icon

( ) to enter into web search mode. Once web search activates, a third-party AI performs the search and returns with an answer.

|  |  |
| --- | --- |
| Workflow Extensibility | Now Assist Skill Kit enables customers to supplement their use of licensed, pre-built Now Assist skills, like example Incident Summarization. Now Assist Skill Kit also enables customers to create new workflow related skills within the scope of their Now Assist purchases. For example, within ITx for ITSM Pro/Enterprise Plus, within ITx and HR for customers with ITSM, and HRSD Pro/ Enterprise Plus. |
| Non-duplicative | Refer to the Now Assist Overview to see the pre-built skills that are currently available exist for purchase in ServiceNow Now Assist packages. Customers must build from the purchased skills instead of attempting to create duplicative versions of licensable ServiceNow skills without purchase. |
| Leveraging custom tables | Custom skills can be built using Now Assist Skill Kit to enable generative AI functionality on the custom tables that are provided in a customer’s licenses. |

For more information about the web search mode end-user display and functionality, see Web search .

Web Search AI choices are available in the OneExtend Definition Configs related list within the AI Search answers entry in the OneExtend Capabilities [sys_one_extend_capability_list] table. Select one of the AI definitions there, such as Perplexity, and set its value to true. Activate a matching AI credential by navigating to ALL > Connections & credentials > Credentials, and setting the matching API key (such as Perplexity API key active value to true).

For more information on how to work with the AI Search answers OneExtend capability, see Configure AI Search answers capability for web search.

For more information on how to add web search as a tool in the Now Assist Skill Kit, see Add a web search.
