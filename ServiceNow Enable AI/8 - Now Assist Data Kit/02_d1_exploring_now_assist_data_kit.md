## Exploring Now Assist Data Kit

*Pages 2–3 of the source PDF*

AI limitations

This application uses artificial intelligence (AI) and machine learning, which are rapidly evolving fields of study that generate predictions based on patterns in data. As a result, this application may not always produce accurate, complete, or appropriate information. Furthermore, there is no guarantee that this application has been fully trained or tested for your use case. To mitigate these issues, it is your responsibility to test and evaluate your use of this application for accuracy, harm, and appropriateness for your use case, employ human oversight of output, and refrain from relying solely on AI-generated outputs for decision- making purposes. This is especially important if you choose to deploy this application in areas with consequential impacts such as healthcare, finance, legal,

employment, security, or infrastructure. You agree to abide by ServiceNow’s AI Acceptable Use Policy , which may be updated by ServiceNow.

Data processing

This application requires data to be transferred from ServiceNow customers' individual instances to a centralized ServiceNow environment, which may be located in a different data center region from the one where your instance is, and potentially to a third-party cloud provider, such as Microsoft Azure. This data is handled

per ServiceNow's internal policies and procedures, including our policies available through our CORE Compliance Portal .

Data collection

ServiceNow collects and uses the inputs, outputs, and edits to outputs of this application to develop and improve ServiceNow technologies including ServiceNow models and AI products. Customers can opt out of future data collection at any time, as described in the Now Assist Opt-Out page.

Exploring Now Assist Data Kit

The Now Assist Data Kit plugin for Now Assist enables you to add datasets to a data catalog and create collections for use in ServiceNow SDK.

Now Assist Data Kit overview

If the base system Now Assist skills don't fit your needs, you can use Now Assist Data Kit to create custom datasets and data collections that can be used in Now Assist Skill Kit for evaluation.

Now Assist Data Kit users

Users

Now Assist Data Kit workflow

The following diagram shows the user journey for Now Assist Data Kit.

| User | Description |
| --- | --- |
| AI practitioner | AI practitioners manage data set creation in Now Assist Data Kit. They develop and evaluate skills and other technical solutions for various use cases. |
| Analyst | Analysts confirm data quality for AI development and evaluation. They work with AI practitioners to follow data curation guidelines set for specific AI use cases. |

User journey for Now Assist Data Kit

1.Create a skill in Now Assist Skill Kit

2. Create an evaluation dataset in Now Assist Data Kit

3. Add table data to the catalog as a dataset

4.Create a data collection

5. Add the dataset

6.Publish the data collection

7.Return to Now Assist Skill Kit and select the data collection to use in the evaluation tool

8.Run the evaluation and review the results to see if you must iterate upon the prompt

9.Publish the skill

Now Assist Data Kit benefits

Now Assist Data Kit benefits

What to explore next

To learn more about configuring and using Now Assist Skill Kit, see:

•Configuring Now Assist Skill Kit

•Using Now Assist Skill Kit

| Benefit | Feature | Users |
| --- | --- | --- |
| Addition of datasets to a data catalog. | Add a dataset | AI developer |
| Create smaller datasets from existing datasets. | Create a derived dataset | AI developer |
| Merge multiple datasets and create a collection that can be used by Now Assist Skill Kit. | Activate a skill | AI developer |



> **[Diagram: Now Assist Data Kit – User Journey Workflow]**
>
> A circular flow diagram on white background. Left: large teal circle labelled "AI Practitioner / Administrator" with a seated-person icon. Right: smaller dark-navy circle labelled "Analyst" with a bar-chart/monitor icon. Centre: seven white rounded-rectangle process boxes connected top-to-bottom by grey arrows:
> 1. Purple sparkle icon → "Creates a skill in Skill Kit"
> 2. Teal spreadsheet icon → "Adding evaluation data"
> 3. Teal open-book icon → "Adds table data to catalog as dataset"
> 4. Teal filter/table icon → "Filters dataset to shortlist required records (Optional)" — dashed arrow right to Analyst: "Manually adds Ground Truth to each dataset record"
> 5. Teal review/eye icon → "Collaborates with analyst to add Ground Truth (Optional)" / "Review Ground Truth (Optional)"
> 6. Teal book/collection icon → "Creates a data collection" / "Adds dataset to Data Collection" / "Apply Random Sampling Technique (Optional)" / "Publishes the Data collection"
> 7. Purple monitor icon → "Returns to Skill Kit and selects data collection"
> The AI Practitioner circle connects via curved lines to all seven boxes.


> **[Diagram: Now Assist Data Kit – User Journey Workflow (page 3)]**
>
> A circular flow diagram on a white background showing the complete Now Assist Data Kit user journey.
>
> **Left circle** (large, teal): Labelled "AI Practitioner / Administrator" — icon shows a seated person at a desk with a small wrench/tool badge.
>
> **Right circle** (smaller, dark navy): Labelled "Analyst" — icon shows a bar-chart on a monitor with a green upward-trend line and a small person badge.
>
> **Centre flow** — Seven white rounded-rectangle process boxes connected top-to-bottom by grey arrows, branching from the AI Practitioner circle:
>
> 1. Purple scissors/sparkle icon → box: **"Creates a skill in Skill Kit"**
> 2. Teal spreadsheet icon → box: **"Adding evaluation data"**
> 3. Teal open-book icon → box: **"Adds table data to catalog as dataset"**
> 4. Teal filter/grid icon → box: **"Filters dataset to shortlist required records (Optional)"** — dashed horizontal arrow leads right to a separate small box: **"Manually adds Ground Truth to each dataset record"** (connected to the Analyst circle)
> 5. Teal review/eye icon → box with two bullet lines: **"Collaborates with analyst to add Ground Truth (Optional)"** / **"Review Ground Truth (Optional)"**
> 6. Teal book/collection icon → box with four bullet lines: **"Creates a data collection"** / **"Adds dataset to Data Collection"** / **"Apply Random Sampling Technique (Optional)"** / **"Publishes the Data collection"**
> 7. Purple monitor/return icon → box: **"Returns to Skill Kit and selects data collection"**
>
> Curved lines flow from the left AI Practitioner circle outward to each of the seven boxes.
