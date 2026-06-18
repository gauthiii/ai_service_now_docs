## Using Now Assist Data Kit

*Pages 4–19 of the source PDF*

Configuring Now Assist Data Kit

Configure prompts and skills for Now Assist Data Kit.

Configuration overview

1.Create a skill

Create a skill in Now Assist Skill Kit.

2. Configure skill deployment settings

Configure the deployment settings for the skill that you create. The deployment settings enable you to choose where the admin can find the skill in Now Assist Admin.

Install Now Assist Data Kit

Install Now Assist Data Kit to create datasets for a data collection.

Before you begin Role required: admin or sn_data_kit.admin

Procedure

1.Navigate to All > System Definition > Plugins.

2. In the Store applications section, select Now Assist Data Kit.

3. Select Install.

Using Now Assist Data Kit

Use Now Assist Data Kit to add datasets to a data catalog to create collections for use in ServiceNow SDK.

Overview of Now Assist Data Kit

Now Assist Data Kit work flow

1.Create a skill

Create a custom skill for Now Assist. Creating a custom skill enables you to have greater flexibility with the Now Assist generative AI capabilities.

Configure skill deployment settings 2.

Configure the deployment settings for the skill that you create. The deployment settings enable you to choose where the administrator can find the skill in Now Assist Admin.

3. Navigate to Now Assist Data Kit to Add a dataset.

Add a dataset

Add the data from a table to a data catalog as a dataset through generative AI by using the Now Assist Data Kit application. Adding a dataset is required to create and publish a data collection.

Before you begin Role required: sn_data_kit.admin

Procedure

1.Navigate to > Now Assist Data Kit > Home. All

Navigate to Discover datasets and select started. 2. Get

3. On the Datasets tab, select New.

4.Select where to curate data from.

◦I'll import data from Instance table

◦I'll import data from my computer

5. On the Choose data form, select the table and columns. If a column does not appear as a possible selection, then the field is not a supported data type. For example, Watch List fields are the glide_list datatype, which is not supported, so Watch List is not a selectable field.

Select if you have columns, such as work notes or 6.Optional: Add column via scripting comments, that aren't stored in the table. This is an example script for adding worknotes.

| (function generate(current) { |
| --- |
| //Current is the Gliderecord object of current record. |
| // //Sample script for adding worknotes |
| // var gr = new GlideRecord("sys_journal_field"); |
| // gr.addQuery('name', current.getTableName()); |
| // gr.addQuery('element_id', current.getUniqueValue()); |
| // gr.query(); |
| // var records = []; |
| // while (gr.next()) { |
| // var obj = { |
| // "value": gr.getValue("value"), |
| // "type": gr.getValue("element"), |
| // "created": gr.getValue("sys_created_on"), |
| // "created_by": gr.getValue("sys_created_by") |
| // }; |
| // records.push(obj); |
| // } |

7.Select condition. Edit filter

8.Review the records and select Continue.

9.On the form, fill in the fields.

Add dataset info form

10.Add tags to identify the dataset.

11. Navigate to the Data governance section and select each check box.

◦I'm assuring to use data responsibly for AI Evaluation

◦Scan for personally identifiable or information sensitive data before creating datasets. You can turn this off if you prefer.

Note: If you opt in, your data is scanned for sensitive data like names or email addresses using . After the scan, records will be highlighted and give you an option to anonymize them. You can also choose to scan the dataset after it is generated.

Select dataset. 12. Generate Fields of any data type are stored as strings when converted to a data asset. The dataset is added to the data assets.

What to do next After your dataset is added to the data catalog, you can choose to create a smaller dataset by creating a derived dataset or adding a ground truth to your existing data set.

Add dataset to a table

You can write dataset records directly into an instance table. This enables you to populate target tables with optional column mapping and scripting.

| // return records; |
| --- |
| })(current); |

| Field | Description |
| --- | --- |
| Dataset name | Name of the dataset. |
| Dataset description | Description of the dataset. |

| vault service |  |
| --- | --- |

Before you begin Role required: sn_data_kit.admin

Procedure

1.Navigate to > Now Assist Data Kit > Home. All

2. Select a dataset.

3. Select Add to Data Instance Table.

4.Select the target table.

5. Map dataset columns to table columns.

6.Select Add to Table.

Create a derived dataset

Create a smaller dataset from an existing dataset through generative AI by using the Now Assist Data Kit application. A derived dataset enables you to choose a smaller dataset.

Before you begin Role required: sn_data_kit.admin

About this task After you add a dataset to the data catalog, you can create a smaller dataset or derived dataset from the Create derived dataset page.

Procedure

1.Select the dataset where you want to create a derived dataset.

Add information for the new derived dataset. 3.

New derived dataset info form

4.Navigate to the Choose records section and select a data selection method for your user. You can select records manually or use a sampling method to choose the data. If you select a sampling selection, use the drop-down menu and then enter a number in the sample size box.

5. Select Run.

| Field | Description |
| --- | --- |
| Dataset name | Name of the dataset. |
| Dataset description | Description of the dataset. |
| Tags | Tags to identify the dataset. |

6.Preview the record results and select dataset. Create The derived dataset is added to the data catalog as a separate dataset.

What to do next After the derived dataset is completed, you can add the ground truth.

Generate synthetic data

Create synthetic data with a sample dataset and a prompt through generative AI by using the Now Assist Data Kit application. You can use synthetic data to create training for a test model or an evaluation dataset.

Before you begin Role required: sn_data_kit.admin

Procedure

1.Navigate to All > Now Assist Data Kit > Home.

2. Select the Synthetic datasets tab.

Select dataset. 3. Generate

4.Choose how you want to generate data.

Way to generate synthetic data

5. On the Add job info page, fill in the fields.

Add job info form

6.Navigate to Define data .

7.Optional: Select a template.

| Method | Description |
| --- | --- |
| Standard data generator | The standard data generator creates flat records based on a fixed schema with files like name, description, and short description. By providing a few examples, the model learns the structure and generates consistent, realistic data, making it suitable for typical use cases. These configurations can also be saved as templates for easy reuse. |
| Multi-table data generator | A multi-table data generator creates realistic test data for several related tables at once. It automatically figures out the right order, groups linked records into meaningful scenarios, and fulls in details using rules or AI. This enables you to use the data generated for testing or demos. |

| Field | Description |
| --- | --- |
| Job name | Name of the generated data. |

Synthetic data templates

8.Select the language for the data generation.

9.On the form, fill in the rest of the fields.

Define data form

| Template | Description |
| --- | --- |
| Catalog item | Service Catalog is a user-friendly interface that allows end-users to browse, request, and manage services and products offered by the organization, streamlining self-service and improving operational efficiency. |
| Incident data | Information Technology Service Management is a business function that involves managing IT services and processes to meet business needs effectively. |

| Field | Description |
| --- | --- |
| Name | Department or industry where the data belongs. |
| Type | Data that you want to generate. |

Note: If you have sample data available, you can navigate to Select the sample data to enhance the accuracy of the generated data. If you don't have sample data, refer to the in-product help for guidance.

10.Select Continue.

Add your sample data by navigating to Define columns to generate data. 11. The columns are populated when you add the sample data. If no sample data is available, you must manually populate the columns with data.

12. Select Continue.

13.Optional: Add additional rules to improve generated data.

14.Select the number of records to generate for testing.

15.Select generation. Start

Use multi-table data generator

The multi-table data generator enables you to create synthetic test data across multiple related ServiceNow tables in a single run. It automatically maintains referential integrity between tables and generates semantically consistent data based on scenarios you define.

Before you begin Role required: sn_data_kit.admin

Procedure

1.Navigate to All > Now Assist Data Kit > Home.

2. From the Synthetic datasets tab, selectGenerate dataset.

Select generator. 3. Multi-table data

4.Configure the dataset.

a.Name the dataset.

b.Enter the industry or department the data is being generated for.

Select Continue. 5.

6.Select the tables and columns.

| Field | Description |
| --- | --- |
| Category | Data that has been categorized with keywords. |
| Count | Number of records to generate. |

7.Select next.

8.Configure the tables. For each selected table, fill in the form fields.

Selected table form fields

9.Select next.

10.Define scenarios.

Scenarios guide the content of the generated data. The system generates records that are semantically consistent with the scenario you describe across all related tables.

| Field | Description |
| --- | --- |
| Data type | Select Transaction for records that change over time. Select Master for reference data that rarely changes. |
| Generation method | Synthetic generates new records. Existing pulls records already in the system. Use Existing for tables where you want to reference real users rather than create new ones. |
| Filter conditions | Optional. Narrows the existing records to pull from. For example, active = true or department = IT. |
| Record count | The number of records to generate for this table. The system supports up to 15 tables and 100 records per table per run. |

Select next. 11.

Select preview. 12. Generate

13.Select Review summary.

14.Select Start generation.

15.Select Start.

Select the sample data

Add the available sample data to enhance the accuracy and relevancy of the generated data in the Now Assist Data Kit application. The sample data can be curated, added into the data collection, or published.

Before you begin Role required: sn_data_kit.admin

Procedure

1.Navigate to data. Select sample

2. In the Select table and columns pop-up window, select an existing dataset in the Data collection field.

3. Navigate to Continue to select up to three records. The data is populated in the different columns.

4.Enter the descriptions for each column that you want to generate the data for. Describe the columns for the large language model (LLM) to generate values accordingly.

5. Set the key column toggle switch on one column. The key column is required and used as a baseline for creating the data in the other columns.

6.Navigate to Test generation to preview a small number of records before generating a full dataset. When previewing a small number of records, you can make adjustments before generating a full dataset.

7.Select the records to generate for testing.

8.Select testing. Start You see the preview generation data results page. If you want more refined results, select or to update the criteria. Define data Select sample data

9.If you're satisfied with the preview results, select for all the data. Start generation The generated data is completed.

Define columns to generate data

Provide detailed definitions to preview a test for each column that you want the data to generate the results for.

Before you begin Role required: sn_data_kit.admin

About this task For better quality data, use fewer than 20 columns.

Procedure

1.Enter a description for each column that you want to generate data for. Describe the columns for the large language model (LLM) to generate values accordingly. This description can include a range and any rules or limitations to be considered.

Enable one column as the key column. 2. The key column is required and used as a baseline for creating data in other columns.

3. Select Continue. The test generation page opens.

4.Navigate to Test generation to preview a small number of records before generating a full dataset.

Select the records to generate for testing. 5.

6.Select Start testing. You see the preview generation data results page. If you want more refined results, navigate to Define data or Select sample data to update the criteria.

7.Select Start generation. The generated data is completed.

Synthetic data generation skills

You can use ServiceNow skills in Now Assist Skill Kit to generate data in Now Assist Data Kit.

ServiceNow skills for data generation

There are three ServiceNow skills that you can use in Now Assist Skill Kit to generate data for Now Assist Data Kit. The three skills are:

•Subcategory scenario generation

•New column data generation

•Complete record generation

You should configure these skills with one model and one provider.

Note: If you deactivate one of these skills, the synthetic data generation feature may not function correctly.

For more information on using ServiceNow skills, see Clone and edit a ServiceNow skill.

View data insights

You can view data insights to see metrics for your generated data and data collections.

Before you begin Role required: sn_data_kit.admin

Procedure

1.Navigate to All > Now Assist Data Kit > Home.

2. Select the dataset or data collection that you want to see data insights for.

Select the tab. 3. Data insights

Data insight metrics for datasets

| Metric | Description |
| --- | --- |
| Data volume | This metric identifies rows with unusually low character count or significantly fewer words compared to the dataset average. |
| Semantic similarity to seed | This metric is LLM-based and measures how closely each record’s meaning matches a given reference (seed). |
| Data hygiene | This metric is LLM-based and checks that fields follow the correct types and formats. |
| Missing/Empty values | This metric identifies fields that are null, empty, or contain placeholder values without valid justification. |
| Temporal consistency | This metric is LLM-based and ensures that data remains logically correct over time. |

Data insight metrics for data collections

Find and cleanse sensitive data

You can scan your datasets for sensitive data, like personally identifiable information (PII). If you find sensitive data, then you can cleanse it from your datasets.

Before you begin Role required: admin

Plugins required: sn_data_discovery, sn_dp_store_app, com.glide.data_privacy.

Procedure

1.Navigate to All > Now Assist Data Kit > Home.

2. From the Dataset tab, select the dataset that you want to scan.

3. Select the Scan and cleanse data icon .

4.From the tab, select data. Scan Data Scan

| Metric | Description |
| --- | --- |
| Data volume | Identifies rows with unusually low character count or significantly fewer words compared to the dataset average. |
| Missing/empty values | Identifies fields that are null, empty, or contain placeholder values. |

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
