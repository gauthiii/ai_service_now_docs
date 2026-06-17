# Predictive Intelligence references

## SOURCE INFORMATION

* SECTION NAME: Predictive Intelligence
* SUBSECTION NAME: Predictive Intelligence references
* SOURCE FILE NAME: Predictive Intelligence.pdf
* PAGE RANGE: 1496-1502 (page 1502 split before next major TOC section Now Assist in Document Intelligence)
* EXTRACTION DATE: 2026-06-17

---

# CONTENT

> Source page: 1496

### Predictive Intelligence references

Reference pages for components of Predictive Intelligence.

#### Domain separation and Predictive Intelligence

Domain separation is supported in the Predictive Intelligence application. Domain separation
enables you to separate data, processes, and administrative tasks into logical groupings called
domains. You can control several aspects of this separation, including which users can see and
access data.

#### Support level: Standard

• Includes all aspects of Basic level support.
• Application properties are domain-aware as needed.
• Business logic: The service provider (SP) creates or modifies processes per customer. The use
cases reflect proper use of the application by multiple SP customers in a single instance.
• The instance owner must configure the minimum viable product (MVP) business logic and data
parameters per tenant as expected for the specific application.
Sample use case: An Admin must be able to make comments required when a record closes for
one tenant, but not for another.
For more information on support levels, see Application support for domain separation
.

#### Overview of domain separation and Predictive Intelligence

With Predictive Intelligence, you can create machine learning solutions using historic datasets.
A machine learning solution is created and trained in the global domain, and that solution's
predictions can be applied in any domain on the instance.
Similarity solutions are domain-aware when applied in your forms and flows, so records from
other domains on the instance are not displayed to users. For more information, see KB article
Similarity prediction behavior in domain separated environment
on Now Support.

> Source page: 1497

#### How domain separation works in Predictive Intelligence

An instance owner can train a machine learning (ML) solution for each domain by creating a
solution definition for each domain and training those solutions. In this way each solution uses
data specific to the corresponding domain.
• Data can be domain separated
• Domain column is present for base system application tables
• Domain-specific configuration is managed by instance owner
• Tenant domains can manage their own application data
• Application properties are domain-aware when needed

#### Related topics

Domain separation for service providers

#### Data Encryption in Predictive Intelligence

Learn which types of encryption are supported for training Predictive Intelligence solutions.

#### Predictive Intelligence support for encrypted training data

#### Encryption type

#### Supported Notes

Field
Yes
Ensure the sharedservice.worker user has the same encryption
Encryption
module role that's been used for encryption.
Edge
No
None.
Encryption
FDE (Full Disc
Yes
None.
Encryption)

#### Predictive Intelligence language support

Predictive Intelligence provides international language support. Learn which languages are
available to Predictive Intelligence solutions.
When you create a Predictive Intelligence solution, you can choose the language you want the
system to use for processing your training records. English is the default language.
For an example of how to assign a language to a solution, see the Processing Language section
in Step 3 of the Create and train a classification solution documentation.
You can also create custom stopwords lists for a language. For more information, see Create a
custom stopwords list.

#### Language support coverage

The current available languages for Predictive Intelligence solutions and stopwords lists are
as follows: Brazilian Portuguese, Chinese (simplified), Danish, Dutch, English, Finnish, French,
French Canadian, German, Italian, Japanese, Korean, Norwegian, Polish, Portuguese, Spanish,
and Swedish.

> Source page: 1498

#### Predictive Intelligence properties

The properties for Predictive Intelligence control certain parameters of its machine-learning
solutions, solution training process, and caching.
Using the maint role, navigate to Predictive Intelligence > Configuration to review or edit.

#### Note: Most of the properties related to training require the maint role to review or edit.

Some properties may require other roles.

#### Predictive Intelligence properties

#### Property

#### Property Name

#### Description

Override
glide.platform_ml.override_training_lock
• True: Overrides
ml_solution_definition

#### the readonly state

record's readonly
during training,
state during training
enabling you to edit
ml_solution_definition.
• False:
ml_solution_definition
remains in the
readonly state.
Minimum number
glide.platform_ml.api.min_regression_records
Sets the minimum
of records for
number of records
Regression
required for Regression
solution training.
• Type: Integer
• Default value: 10000

#### Note: Support

for new regression
solutions is
deprecated as of
the Washington
DC release. You
can edit and
train any existing
solutions, but you
can't create new
ones.
Maximum number
glide.platform_ml.api.max_regression_records
Sets the maximum
of records for
number of records
Regression
that can be used in
Regression solution
training.
• Type: Integer
• Default value:
300000

> Source page: 1499

#### Predictive Intelligence properties (continued)

#### Property

#### Property Name

#### Description

#### Note: Support

for new regression
solutions is
deprecated as of
the Washington
DC release. You
can edit and
train any existing
solutions, but you
can't create new
ones.
The time (in ms) an
glide.platform_ml.training_timeout
Sets the time-out time in
in-training solution
milliseconds for an in-
will wait without
training solution.
updates before timing
out
• Type: Integer
• Default value:
21600000 (ms)
Maximum model size
glide.platform_ml.api.model_size
Sets the maximum
number of records you
can use to train a model.
• Type: Integer
• Default value:
524288000
Maximum number
glide.platform_ml.api.csv_max_line
Sets the maximum
of records used in
number of records
training
that can be used in
Classification solution
training.
• Type: Integer
• Default value:
300000
Minimum number
glide.platform_ml.api.csv_min_line
Sets the minimum
of records used in
number of records
training
required for
Classification solution
training.
• Type: Integer
• Default value: 10000
Maximum number
glide.platform_ml.api.csv_split_days
Sets the maximum
of days worth of
number of days a single
records on request
request can retrieve
can retrieve
from your records.

> Source page: 1500

#### Predictive Intelligence properties (continued)

#### Property

#### Property Name

#### Description

• Type: Integer
• Default value: 30
Maximum number of
glide.platform_ml.api.max_wordcorpus_records
Sets the maximum
records per table for
number of records
word corpus
per table for Word
Corpus creation for
Similarity and Clustering
solutions.
• Type: Integer
• Default value:
300000

#### Note: With

the Washington
DC release,
classification,
clustering and
similarity solutions
use Workflow
solutions. These
are pre-trained
so a word corpus
isn't needed. The
Word Corpus field
is removed from
Workflow solution
forms.
Maximum number of
glide.platform_ml.api.max_similarity_window_records Sets the maximum
records for similarity
number of records that
window (to lookup
the Similarity Window
results)
can retrieve to look up
results.
• Type: Integer
• Default value: 100000
Maximum number of
glide.platform_ml.api.max_clustering_records
Sets the maximum
records for Clustering
number of records you
can include in a cluster.
• Type: Integer
• Default value: 100000

> Source page: 1501

#### Shared Service Scheduler

#### Property

#### Property Name

Shared service scheduler url
glide.shared_service_scheduler.url

#### Machine Learning Artifacts

#### Property

#### Property Name

Maximum number of artifacts cached
glide.cache.size.ml_object_cache
(in MB)
Artifact cache compression scheme
glide.platform_ml.artifact.cache_compression_scheme

#### Predictive Intelligence roles

Predictive Intelligence is installed with these roles.
To learn more about managing per-user subscriptions, see Managing per-user subscriptions in
Subscription Management
and contact your account representative.

#### ML Admin [ml_admin]

Can create, read, write or delete the ml_predictor_results table and the ml_predictor_results_task
table.

#### Contains Roles

List of roles contained within the role.
• pa_data_collector
• pa_viewer

#### Groups

List of groups this role is assigned to by default.
None.

#### Special considerations

Avoid granting an admin role when more specialized roles are available.

#### ML Labeler [ml_labeler]

Can create, read, write or delete the ml_label_candidate table.

#### Contains Roles

List of roles contained within the role.
• sn_ace.ace_user
• nlu_user

#### Groups

List of groups this role is assigned to by default.

> Source page: 1502

None.

#### Special considerations

None.

#### ML Report User [ml_report_user]

Can read the ml_predictor_results table and the ml_predictor_results_task table.

#### Contains Roles

List of roles contained within the role.
pa_viewer

#### Groups

List of groups this role is assigned to by default.
None.

#### Special considerations

None.

## Now Assist in Document Intelligence

## Boundary content appearing after the Predictive Intelligence section boundary

The following content begins the next major TOC section on source page 1502. It is captured for page completeness and is not treated as Predictive Intelligence content.

> Source page: 1502

With ServiceNow® Now Assist in Document Intelligence, you can use generative AI to get key
information from digital documents into your automation workflows.
https://player.vimeo.com/video/1164703930?
h=61afcd70f4&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479

#### Get started

#### Explore

#### Configure

Learn about the generative AI
Activate Now Assist in
skills that are available in Now
Document Intelligence and
Assist in Document Intelligence
configure the generative AI skills


---

## IMAGE DESCRIPTIONS

### Repeated ServiceNow page header/logo

The ServiceNow-branded wordmark appears in the upper-left corner of reviewed source pages for this subsection. It is a recurring branding image, not a technical diagram. It contains the visible brand text `servicenow`, with green accenting in the `now` portion. Reviewed pages: 1496, 1497, 1498, 1499, 1500, 1501, 1502.

### Small UI icons and inline pictograms

1 small non-logo icon/pictogram image blocks were reviewed on source pages 1502. These include information icons, external-link indicators, UI symbols, or small inline graphics. They support the surrounding text but do not contain standalone table data. Coordinates and classification are retained in `_assets/image_inventory.csv`.

No large embedded screenshot or diagram image blocks were detected within this subsection boundary.


---

## TABLES

### Source page 1497 — Table 1

**Nearby source context:** Related topics / Data Encryption in Predictive Intelligence / Predictive Intelligence support for encrypted training data

| Encryption type | Supported | Notes |
| --- | --- | --- |
| Field<br>Encryption | Yes | Ensure the sharedservice.worker user has the same encryption<br>module role that's been used for encryption. |
| Edge<br>Encryption | No | None. |
| FDE (Full Disc<br>Encryption) | Yes | None. |

### Source page 1498 — Table 2

**Nearby source context:** Using the maint role, navigate to Predictive Intelligence > Configuration to review or edit. / Note: Most of the properties related to training require the maint role to review or edit. / Predictive Intelligence properties

| Property | Property Name | Description |
| --- | --- | --- |
| Override<br>ml solution definition<br>_ _<br>record's readonly<br>state during training | glide.platform ml.override training lock<br>_ _ _ | • True: Overrides<br>the readonly state<br>during training,<br>enabling you to edit<br>ml solution definition.<br>_ _<br>• False:<br>ml solution definition<br>_ _<br>remains in the<br>readonly state. |
| Minimum number<br>of records for<br>Regression | glide.platform ml.api.min regression records<br>_ _ _ | Sets the minimum<br>number of records<br>required for Regression<br>solution training.<br>• Type: Integer<br>• Default value: 10000<br>Note: Support<br>for new regression<br>solutions is<br>deprecated as of<br>the Washington<br>DC release. You<br>can edit and<br>train any existing<br>solutions, but you<br>can't create new<br>ones. |
| Maximum number<br>of records for<br>Regression | glide.platform ml.api.max regression records<br>_ _ _ | Sets the maximum<br>number of records<br>that can be used in<br>Regression solution<br>training.<br>• Type: Integer<br>• Default value:<br>300000 |

### Source page 1499 — Table 3

**Nearby source context:** Predictive Intelligence properties (continued)

| Property | Property Name | Description |
| --- | --- | --- |
|  |  | Note: Support<br>for new regression<br>solutions is<br>deprecated as of<br>the Washington<br>DC release. You<br>can edit and<br>train any existing<br>solutions, but you<br>can't create new<br>ones. |
| The time (in ms) an<br>in-training solution<br>will wait without<br>updates before timing<br>out | glide.platform ml.training timeout<br>_ _ | Sets the time-out time in<br>milliseconds for an in-<br>training solution.<br>• Type: Integer<br>• Default value:<br>21600000 (ms) |
| Maximum model size | glide.platform ml.api.model size<br>_ _ | Sets the maximum<br>number of records you<br>can use to train a model.<br>• Type: Integer<br>• Default value:<br>524288000 |
| Maximum number<br>of records used in<br>training | glide.platform ml.api.csv max line<br>_ _ _ | Sets the maximum<br>number of records<br>that can be used in<br>Classification solution<br>training.<br>• Type: Integer<br>• Default value:<br>300000 |
| Minimum number<br>of records used in<br>training | glide.platform ml.api.csv min line<br>_ _ _ | Sets the minimum<br>number of records<br>required for<br>Classification solution<br>training.<br>• Type: Integer<br>• Default value: 10000 |
| Maximum number<br>of days worth of<br>records on request<br>can retrieve | glide.platform ml.api.csv split days<br>_ _ _ | Sets the maximum<br>number of days a single<br>request can retrieve<br>from your records. |

### Source page 1500 — Table 4

**Nearby source context:** Predictive Intelligence properties (continued)

| Property | Property Name | Description |
| --- | --- | --- |
|  |  | • Type: Integer<br>• Default value: 30 |
| Maximum number of<br>records per table for<br>word corpus | glide.platform ml.api.max wordcorpus records<br>_ _ _ | Sets the maximum<br>number of records<br>per table for Word<br>Corpus creation for<br>Similarity and Clustering<br>solutions.<br>• Type: Integer<br>• Default value:<br>300000<br>Note: With<br>the Washington<br>DC release,<br>classification,<br>clustering and<br>similarity solutions<br>use Workflow<br>solutions. These<br>are pre-trained<br>so a word corpus<br>isn't needed. The<br>Word Corpus field<br>is removed from<br>Workflow solution<br>forms. |
| Maximum number of<br>records for similarity<br>window (to lookup<br>results) | glide.platform ml.api.max similarity window records<br>_ _ _ _ | Sets the maximum<br>number of records that<br>the Similarity Window<br>can retrieve to look up<br>results.<br>• Type: Integer<br>• Default value: 100000 |
| Maximum number of<br>records for Clustering | glide.platform ml.api.max clustering records<br>_ _ _ | Sets the maximum<br>number of records you<br>can include in a cluster.<br>• Type: Integer<br>• Default value: 100000 |

### Source page 1501 — Table 5

**Nearby source context:** Shared Service Scheduler

| Property | Property Name |
| --- | --- |
| Shared service scheduler url | glide.shared service scheduler.url<br>_ _ |

### Source page 1501 — Table 6

**Nearby source context:** Property / Property Name / Machine Learning Artifacts

| Property | Property Name |
| --- | --- |
| Maximum number of artifacts cached<br>(in MB) | glide.cache.size.ml object cache<br>_ _ |
| Artifact cache compression scheme | glide.platform ml.artifact.cache compression scheme<br>_ _ _ |

### Source page 1502 — Table 7

**Boundary note:** This table appears after the Predictive Intelligence section boundary and is captured only for page completeness.

**Nearby source context:** Special considerations / Now Assist in Document Intelligence / Get started

| Explore<br>Learn about the generative AI<br>skills that are available in Now<br>Assist in Document Intelligence | Configure<br>Activate Now Assist in<br>Document Intelligence and<br>configure the generative AI skills |
| --- | --- |


---

## FIGURES

| Figure / visual | Source page | Asset or location | Analysis |
|---|---:|---|---|
| Markdown-converted table/grid 1 | 1497 | TABLES section | Source table/grid region converted into Markdown; nearby context: Related topics / Data Encryption in Predictive Intelligence / Predictive Intelligence support for encrypted training data |
| Markdown-converted table/grid 2 | 1498 | TABLES section | Source table/grid region converted into Markdown; nearby context: Using the maint role, navigate to Predictive Intelligence > Configuration to review or edit. / Note: Most of the properties related to training require the maint role to review or edit. / Predictive Intelligence properties |
| Markdown-converted table/grid 3 | 1499 | TABLES section | Source table/grid region converted into Markdown; nearby context: Predictive Intelligence properties (continued) |
| Markdown-converted table/grid 4 | 1500 | TABLES section | Source table/grid region converted into Markdown; nearby context: Predictive Intelligence properties (continued) |
| Markdown-converted table/grid 5 | 1501 | TABLES section | Source table/grid region converted into Markdown; nearby context: Shared Service Scheduler |
| Markdown-converted table/grid 6 | 1501 | TABLES section | Source table/grid region converted into Markdown; nearby context: Property / Property Name / Machine Learning Artifacts |
| Markdown-converted table/grid 7 | 1502 | TABLES section | Source table/grid region converted into Markdown; nearby context: Special considerations / Now Assist in Document Intelligence / Get started |


---

## QUALITY ASSURANCE NOTES

* PAGES REVIEWED: 1496, 1497, 1498, 1499, 1500, 1501, 1502. Source page range: 1496-1502 (page 1502 split before next major TOC section Now Assist in Document Intelligence).
* IMAGES REVIEWED: 7 image blocks assigned/reviewed: 6 recurring header logo block(s), 1 small icon/pictogram block(s), and 0 large screenshot/diagram crop(s).
* TABLES REVIEWED: 7 table/grid region(s) converted to Markdown. Table pages: 1497, 1498, 1499, 1500, 1501, 1502.
* FIGURES REVIEWED: 0 large screenshot/diagram figure(s) plus 7 table/grid visual(s).
* OCR ISSUES FOUND: No unresolved OCR issues were identified in the main PDF text layer after cleanup. Embedded screenshot crops are preserved as source assets; automated image OCR was not applied in this pass to avoid inserting low-confidence text, and this is explicitly marked in each image record.
* OCR ISSUES CORRECTED: Removed recurring footer/page-number noise from the main content stream, normalized nonbreaking spaces and soft-hyphen/control artifacts, preserved bullets/numbering/property names, and converted detected tables to Markdown.
* SECTION MAPPING NOTES: Folder name is exactly `Predictive Intelligence`. File name and subsection name are exactly `Predictive Intelligence references` from the TOC. Shared source pages were split at heading coordinates from the PDF text layer.
* BOUNDARY NOTE: Source page 1502 contains the next major TOC section, `Now Assist in Document Intelligence`, after the Predictive Intelligence roles content; next-section content is captured as boundary content only.
* PAGE FOOTERS REVIEWED: Reviewed recurring ServiceNow copyright/trademark footer and logical page numbers. Footer text reviewed: `© 2026 ServiceNow, Inc. All rights reserved. ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries. Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.`
* RECHECK PASSES COMPLETED: 12/12: page completeness, text extraction, table extraction, image extraction, diagram interpretation, section mapping, subsection mapping, file names, folder names, Markdown formatting, missed-content review, and OCR/text-layer cleanup.
* VERIFICATION ARTIFACTS: Large image crops and `image_inventory.csv` are stored in the `_assets` folder inside this section folder.
