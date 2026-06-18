### Create a derived dataset

*Pages 7–8 of the source PDF*

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


> **[Screenshot: Now Assist Data Kit – Add to Instance Table & Create Derived Dataset Forms (page 7)]**
>
> **Top section** – "Add to Data Instance Table" button group: A teal outlined button "Add to data collection" with a dropdown arrow, and below it a green-highlighted button "Add to instance table".
>
> **Middle section** – "Add to table" panel with:
> - Orange warning banner: "The data you're mapping may be AI-generated or imported. Use a sub-production instance to keep evaluation data separate. Learn more"
> - "Target table *" — empty search field with magnifying glass
> - "Map columns from dataset" sub-section with header text: "You can select columns from the dropdown menu or use scripting for more complex columns, such as work notes or comments."
> - A six-row mapping table with columns: Dataset columns | Data type | Table columns:
>   - Short description | String | [empty dropdown] | Add script
>   - Description | String | [empty dropdown] | Add script
>   - State | Number | [empty dropdown] | Add script
>   - Priority | Number | [empty dropdown] | Add script
>   - Incident | Record | [empty dropdown] | Add script
>   - Target record | Record | [empty dropdown] | Add script
> - Teal "Add to Table" button bottom-right.
