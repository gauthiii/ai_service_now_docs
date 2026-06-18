### General guidelines for Now Assist Skill Kit

*Pages 5–9 of the source PDF*

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


> **[Diagram: Now Assist Skill Kit – 5-Stage Skill Build Pipeline (page 5)]**
>
> Horizontal five-step pipeline on a white background showing the ordered stages of building a custom skill. Five dark teal/navy rounded rectangles connected by grey right-pointing arrows:
>
> 1. **"Scope the skill"** — sparkle/wand icon (white on dark teal)
> 2. **"Create a dataset"** — cylinder/database icon
> 3. **"Develop the prompt"** — document with pencil icon
> 4. **"Evaluate the prompt"** — magnifying glass with document icon
> 5. **"Deploy and monitor the skill"** — upward arrow in circle icon
>
> A soft lavender-purple gradient band runs behind all five boxes. Below the pipeline: a colourful collaborative illustration showing three people — one seated at a laptop (teal), one standing pointing at a display (purple), one standing listening (gold/yellow) — suggesting a team discussion.

> **[Chart + Table: Prompt Accuracy Distribution & Evaluation Sample-Size Probability (page 9)]**
>
> **LEFT** — Histogram titled "Distribution of Observed Test Accuracies". X-axis: 40–100 labelled "Observed Accuracy with N=100". Y-axis: frequency (unlabelled). Two overlapping bell-shaped distributions: **blue = Prompt A** (peak ≈70) and **orange = Prompt B** (peak ≈85). A vertical dashed line sits between the peaks labelled "True Acc. Gap = 15%".
>
> **RIGHT** — Probability lookup table titled "Chance of Seeing Better Performance from the Worse of Two Prompts". Column headers (True Underlying Accuracy Gap): **5% | 10% | 15% | 20%** (10% and 15% columns highlighted yellow). Row labels (Data used in evaluation): N=10, N=25, N=50, N=100, N=250, N=500.
>
> Values:
> - N=10:  30% | 21% | 14% | 9%
> - N=25:  28% | 16% | 8%  | 3%
> - N=50:  24% | 10% | 3%  | 0.6%
> - N=100: 18% | 4%  | 0.5%| 0.02%
> - N=250: 9%  | 0.4%| <0.01%| <0.001%
> - N=500: 3%  | 0.01%| <0.001%| <0.0001%
>
> Caption: "The approximate probability of observing better performance from the less accurate prompt among two (2) candidates, tabulated as a function of the evaluation dataset size (N) and the 'true' underlying accuracy gap between the prompts (as measured on 'infinite' data)."
