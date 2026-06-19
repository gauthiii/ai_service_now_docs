### Generate synthetic data

*Pages 9–14 of the source PDF*

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


> **[Screenshot: Now Assist Data Kit – Create Derived Dataset Form (page 8)]**
>
> A white form page titled **"Create derived dataset"** with subtitle "Create a derived dataset by choosing records from this dataset". Top-right counter badge: "Selected records: 92".
>
> **"Add dataset Info"** section (inside bordered card):
> - "Dataset name *" — blue-outlined text field with value "Derived Dataset"
> - "Dataset description" — text area with value "This data is derived from - Recasted Data - HR - INC0158087"
> - "Tags" — empty text field
>
> **"Choose records"** section:
> - Sub-text: "Select records manually or use a sampling method to get a sample of the dataset. A minimum of 10 records need to be selected."
> - Selection method radio buttons: ● Manual Selection ○ Sampling Selection (Manual selected)
> - "Records 92" counter with a circular refresh icon
> - Table header row: ☐ | Record ID | Updated | Sys ID (no data rows visible)
> - Teal "Create dataset" button bottom-right.

> **[Screenshot: Now Assist Data Kit – Multi-Table Data Generator – Select Tables (page 12)]**
>
> A 3-step wizard header: ①Select tables (active) → ②Configure tables → ③Define records.
>
> Main panel: "Select tables to generate data". Message: "We'll also use the tables you select to suggest other related tables." "+ Add tables" button top-right.
>
> An expanded table card for **Incident**:
> - Delete and collapse icons top-right of card
> - "Select table *" — text field: "incident"
> - "Describe the table *" — text field: "This is an incident table"
> - "Columns / reference fields" — multi-select tag chips: Active ×, Activity due ×, AI Resolution Plan ×, Approval ×, Approval set ×, Assigned to ×, Assignment group ×, Business duration ×, Business impact ×, Service ×, Business resolve time ×, Duration ×, Resolve time ×
>
> Far right: a small circular diagram node showing an "incident Table" icon (person/link icon in a teal circle) with +/−/expand controls.

> **[Screenshot: Now Assist Data Kit – Multi-Table Generator – Describe Scenarios (page 13)]**
>
> A white form section titled **"Describe scenarios"** with sub-text "A scenario is a specific real-world condition or data need that the generated dataset should represent."
>
> An AI suggestion banner (light blue): "✦ Here are some AI-generated scenarios you can explore based on the tables you've configured." — with "Add all" button and "Generate scenarios" button and collapse (∧) control.
>
> Four scenario suggestion cards in a horizontal carousel (3 visible + partial 4th):
> - "Incident linked to an underlying problem record" + "Add scenario" link
> - "Incident caused by a change request" + "Add scenario" link
> - "Incident resolved and closed by assigned staff" + "Add scenario" link
> - Partially visible 4th card with right-arrow navigation (>)
>
> Four dot pagination indicators (first dot filled dark, rest empty).
>
> Below: "1 scenario | Expand all | Collapse all" + "+ Add scenario" button.
>
> An expanded scenario card: "∧ Scenario 1" with a required field "Describe the scenario which you want to generate dataset for *" — text area containing: "Incident escalated to a higher support group".
