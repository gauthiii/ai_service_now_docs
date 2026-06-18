# Install Predictive Intelligence

## SOURCE INFORMATION

* SECTION NAME: Predictive Intelligence
* SUBSECTION NAME: Install Predictive Intelligence
* SOURCE FILE NAME: Predictive Intelligence.pdf
* PAGE RANGE: 1388-1389 (shared boundary pages split at source headings)
* EXTRACTION DATE: 2026-06-17

---

# CONTENT

> Source page: 1388

### Install Predictive Intelligence

Activate Predictive Intelligence on your instance and get started with basic configuration.

#### Before you begin

Role required: admin

#### About this task

The Predictive Intelligence plugin (com.glide.platform_ml) is included in the base system, but if
necessary you can use the following procedure to activate it.
Other related plugins and store applications are available. For example, Predictive Intelligence
for Field Service Management (com.snc.fsm_ml) provides solutions relevant to FSM. Some of
these plugins may require a separate license.
When you activate the Predictive Intelligence plugin for the first time on your instance, the
system launches a Homepage. The Homepage provides an overview of your solution definitions
in the classification, similarity, clustering, and regression frameworks. You can create, train,
and test solutions directly on the Homepage. A summary of the latest trained solution is also
available.

#### Procedure

1. Navigate to System Definition > Plugins.
2. Use the search bar to locate the Predictive Intelligence (com.glide.platform_ml) plugin.
3. Select Install and then in the Activate Plugin dialog box, select Activate.
When you activate a plugin, any dependent plugins are activated automatically.
4. Confirm that the activation has successfully created a sharedservice.worker user.
When training your solutions, Predictive Intelligence operates as this user.

#### Note: The sharedservice.worker user includes the following roles:

  ◦platform_ml_read
  ◦platform_ml_write
  ◦platform_ml_create
These roles are required to create, train, and view solutions. They are internal roles and
not meant to be edited or assigned to other users.

#### Implement Predictive Intelligence

Implement initial setup and configuration steps for Predictive Intelligence to train a machine-
learning (ML) algorithm to make predictions based on your past record data.

#### Before you begin

Role required: admin or ml_admin

#### About this task

The training process requires sending record data to a training service in the nearest datacenter.
Since every datacenter has its own dedicated training server and the data doesn't leave the
datacenter, this service is also available to customers who have data sovereignty requirements.
For more information on this process, see Explore Predictive Intelligence.
For frequently asked questions regarding initial configuration and setup, see KB0781894
.

> Source page: 1389

#### Procedure

1. Activate Predictive Intelligence on a non-production instance.
2. From your production instance, export the records that you want your Predictive Intelligence
solutions to process.
For example, export 12 months of incident records to a non-production instance.
3. On the non-production instance, import the records you exported.
4. On the non-production instance, review the default solution definition records to determine if
the filter, input fields, and output field are sufficient to predict your incident or task records.
If necessary, create a solution definition for each record set you want to predict.
5. On the non-production instance, train the solution definition records.
6. Test the solution predictions on the non-production instance by either creating test records or
importing more records from production.
7. For classification solutions, review the prediction reports to determine the accuracy and
coverage of your solution and individual classes.
8. For similarity solutions, review the similarity examples to update the similarity score threshold if
needed.
9. If necessary, update the solution definition filter to include more or different training records.
10. Retrain and retest any updated solution definition records.
11. When you are satisfied with your solutions, activate Predictive Intelligence on your production
instance.
12. Recreate any custom solution definition records and train the solution, or import the solution
from your non-production instance to your production instance.

#### Related topics

Create and train a classification solution
Create and train a similarity solution


---

## IMAGE DESCRIPTIONS

### Repeated ServiceNow page header/logo

The ServiceNow-branded wordmark appears in the upper-left corner of reviewed source pages for this subsection. It is a recurring branding image, not a technical diagram. It contains the visible brand text `servicenow`, with green accenting in the `now` portion. Reviewed pages: 1388, 1389.

### Small UI icons and inline pictograms

No small non-logo icon/pictogram image blocks were detected within this subsection boundary.

No large embedded screenshot or diagram image blocks were detected within this subsection boundary.


---

## TABLES

No source tables were detected within this subsection boundary.


---

## FIGURES

No figures, diagrams, screenshots, or table-layout visuals were detected within this subsection boundary.


---

## QUALITY ASSURANCE NOTES

* PAGES REVIEWED: 1388, 1389. Source page range: 1388-1389 (shared boundary pages split at source headings).
* IMAGES REVIEWED: 1 image blocks assigned/reviewed: 1 recurring header logo block(s), 0 small icon/pictogram block(s), and 0 large screenshot/diagram crop(s).
* TABLES REVIEWED: 0 table/grid region(s) converted to Markdown. Table pages: none.
* FIGURES REVIEWED: 0 large screenshot/diagram figure(s) plus 0 table/grid visual(s).
* OCR ISSUES FOUND: No unresolved OCR issues were identified in the main PDF text layer after cleanup. Embedded screenshot crops are preserved as source assets; automated image OCR was not applied in this pass to avoid inserting low-confidence text, and this is explicitly marked in each image record.
* OCR ISSUES CORRECTED: Removed recurring footer/page-number noise from the main content stream, normalized nonbreaking spaces and soft-hyphen/control artifacts, preserved bullets/numbering/property names, and converted detected tables to Markdown.
* SECTION MAPPING NOTES: Folder name is exactly `Predictive Intelligence`. File name and subsection name are exactly `Install Predictive Intelligence` from the TOC. Shared source pages were split at heading coordinates from the PDF text layer.
* PAGE FOOTERS REVIEWED: Reviewed recurring ServiceNow copyright/trademark footer and logical page numbers. Footer text reviewed: `© 2026 ServiceNow, Inc. All rights reserved. ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries. Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.`
* RECHECK PASSES COMPLETED: 12/12: page completeness, text extraction, table extraction, image extraction, diagram interpretation, section mapping, subsection mapping, file names, folder names, Markdown formatting, missed-content review, and OCR/text-layer cleanup.
* VERIFICATION ARTIFACTS: Large image crops and `image_inventory.csv` are stored in the `_assets` folder inside this section folder.
