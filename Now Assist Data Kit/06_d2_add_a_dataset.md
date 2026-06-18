### Add a dataset

*Pages 5–6 of the source PDF*

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


> **[Screenshot: Now Assist Data Kit – Add Dataset – Data Governance Checkboxes (page 6)]**
>
> A white form section on the "Add dataset" page showing the **Data Governance** section. A teal shield icon with a checkmark labels the section "Data governance". Inside a light-grey bordered panel:
>
> - ✅ Blue filled checkbox: "I'm assuring to use data responsibly for AI Evaluation"
> - ☐ Empty checkbox: "Scan for personally identifiable or information sensitive data before creating datasets. You can turn this off if you prefer"
>
> Below the second checkbox, indented info text: "If you opt in, we will scan this data for sensitive data like names or email addresses using vault service. After the scan, we will highlight the records and give you an option to anonymize them. You can also choose to scan the dataset after it is generated."
