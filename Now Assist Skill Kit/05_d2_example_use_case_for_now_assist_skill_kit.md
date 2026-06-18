### Example use case for Now Assist Skill Kit

*Pages 10–13 of the source PDF*

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


> **[Screenshot: Now Assist Skill Kit – Configurations Panel (page 11)]**
>
> A vertical side panel on white background titled "Configurations" (circular-arrow icon beside it). Sub-text: "Adjust prompt settings to change output quality."
>
> Read-only fields:
> - Provider: **Now LLM Generic**
> - Provider API: **Now LLM Generic**
>
> Editable fields:
> - Model ⓘ — dropdown showing **llm_generic** ▼
> - Temperature * ⓘ — text field: **0.2**
> - Maximum response tokens * ⓘ — text field: **1000**
> - Maximum request tokens * — text field: **6942**
> - Small ⓘ note below: "Maximum number of tokens allowed in request."
>
> Below a horizontal divider:
> - **Usage conditions [+]** — section header with a blue plus button
> - Grey sub-text: "Conditions determine when to use this prompt based on user inputs."

> **[Screenshot: Now Assist Skill Kit – New Skill Creation Modal (page 12)]**
>
> A white modal dialog titled **"New skill"** (✕ close button top-right). Form fields:
> - "Skill name *" — text field: **"Child Incident Summary"**
> - "Description" — textarea: **"Summarize child incidents"**
> - Unchecked checkbox: "Use the description above to recommend an AI generated prompt (powered by Now LLM Generic)"
> - "Default provider *" — dropdown: **"Now LLM Generic"** ▼
> - "Provider API *" — dropdown: **"Now LLM Generic"** ▼
> - Bottom-right buttons: grey **"Cancel"** | teal **"Create skill"**
