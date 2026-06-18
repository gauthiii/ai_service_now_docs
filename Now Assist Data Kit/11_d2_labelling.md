### Labelling

*Pages 17–19 of the source PDF*

If there is sensitive data in your dataset, select the tab and select 5. Cleanse Data Cleanse data to remove it. You can also see the records that contain sensitive data by viewing the Data Insights tab. To learn more, see View data insights.

Labelling

Data labeling is the process of reviewing and annotating data records to prepare them for AI training or quality validation.

About data labeling

Labeled data helps AI systems to understand the data and learn from it. By providing labeled examples, we can teach AI systems how to recognize patterns, categories, features, or relationships in the data. For instance, if we want to train an AI system to identify animals in images, we need to provide it with labeled images of different animals. The AI system can then learn how to associate the labels with the visual features of the animals.

Labeling is important for AI because it enables us to train and evaluate AI systems effectively and accurately. Without labeled data, AI systems would not be able to learn from the data or make predictions based on it. Labeled data is essential for:

•Training:

Training is the process of feeding labeled data to an AI system so that it can learn from it and adjust its parameters accordingly. The more labeled data we provide, the more accurate and reliable the AI system becomes.

•Validation:

Validation is the process of using a subset of labeled data to check the performance of an AI system during training. Validation helps us to monitor the progress of the AI system and avoid overfitting or underfitting.

•Testing:

Testing is the process of using another subset of labeled data to measure the final performance of an AI system after training. Testing helps us to evaluate how well the AI system can generalize to new and unseen data.

Labeling in Now Assist Data Kit

In Now Assist Data Kit, labeling enables you to systematically review datasets, mark data quality, categorize information, and provide structured feedback on individual records.

To use data labeling, you must have one of the following roles:

•Data Kit Admin (sn_data_kit.admin): Full access to create projects, manage teams, configure layouts, and review all labeling work

•Analyst (sn_data_kit.analyst): Limited access to assigned projects only; can view and label tasks but cannot modify project configurations

Data foundation

•Datasets

Collections of records available for labeling (e.g., synthetic datasets from data curation teams)

•Data Collections

Packaged combinations of uploaded and AI-generated records (e.g., 100 uploaded records + 500 AI-augmented records = 600-record collection ready for labeling)

Create a labeling project from scratch

Create a labeling project to review datasets, mark data quality, categorize information, and provide structured feedback on individual records.

Before you begin Role required: sn_data_kit.admin or sn_data_kit.analyst

Procedure

1.Navigate to All > Now Assist Data Kit > Home.

From the Data labeling section, select project. 2. Create

3. Select whether to create a project from scratch or from a template and select Create project.

4.Fill in the fields for the project details.

Label project details form

Select Continue. 5.

6.Choose the data collection that you want to add to the labeling project.

7.Select Continue.

8.Optional: Add a preprocessor.

a.Display name

b.Subflow

c.Input source

9.Select Continue.

10.Select the project layout.

a.Select the number of columns for the layout.

b.For each column, select Add Component.

c.Add a component name and select a component type.

You can select the Read only component. d. Optional:

e. Select the input source.

f.Select Add.

| Field | Description |
| --- | --- |
| Project name | The name of the project. |
| Description | A description of the project. |
| Labeling instructions | Instructions for how the entries should be labeled. |
| Add labelers | The users the labeling tasks will be assigned to. |

Select Continue. 11.

Review the project summary and select Publish. 12.

Result After your labeling project is published, you can view the tasks related to that project by selecting it from the tab. Projects

Create labeling project from template

Templates enable you to create new labeling projects quickly by reusing pre-configured project settings.

Before you begin Role required: sn_data_kit.admin or sn_data_kit.analyst

About this task A saved template preserves:

•Project layout and field configurations

•Data field mappings

•Input field definitions

•Field properties

Procedure

1.Navigate to > > Home. All Now Assist Data Kit

There are two ways to create a labeling project from a template. 2.

◦a.From the Projects tab of the Data labeling section, select project. Create

b.Select Use template and then find the template that you want to use.

c.Select Create project.

◦a.From the Data labeling section, select the Templates tab.

b.Find and select the template that you want to use.

c.Select project. Create

3. Fill in the fields for the project details.

Label project details form

4.Select Continue.

Choose the data collection that you want to add to the labeling project. 5.

| Field | Description |
| --- | --- |
| Project name | The name for the project. |
| Description | A description for the project. |
| Labeling instructions | Instructions for how the entries should be labeled. |
| Add labelers | The users the labeling tasks will be assigned to. |
