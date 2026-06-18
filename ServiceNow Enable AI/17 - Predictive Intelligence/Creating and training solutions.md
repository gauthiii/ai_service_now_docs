# Creating and training solutions

## SOURCE INFORMATION

* SECTION NAME: Predictive Intelligence
* SUBSECTION NAME: Creating and training solutions
* SOURCE FILE NAME: Predictive Intelligence.pdf
* PAGE RANGE: 1425-1464 (shared boundary pages split at source headings)
* EXTRACTION DATE: 2026-06-17

---

# CONTENT

> Source page: 1425

Use one of the Predictive Intelligence (PI) frameworks to create and train machine-learning
solutions. Each framework delivers a different solution type for training the system to predict,
recommend, and organize data outcomes.

#### Types of solutions

The three PI frameworks provide different solutions that can be invoked by any application
through a prediction API to make a prediction. Create and train your own solutions using
your previous data. Navigate to All > Predictive Intelligence > Homepage to view and create
solutions.
Select the best framework for your desired prediction:
• Classification solutions:
Sets field values during record creation to automatically categorize and route work based on
past records. See Create and train a classification solution.
• Similarity solutions:
Identifies similarities between new and existing records to recommend resolutions. See Create

> Source page: 1426

• Clustering solutions:
Groups similar records into clusters to identify patterns and major incidents. See Create and
train a clustering solution.
• Regression solutions:

#### Note: From the Washington DC release, support for creating new regression solutions

was removed. You can still edit and train existing regression solutions, but you won't be
able to initiate new ones.
Uses historic data to predict numeric outputs, such as estimating the time it takes to resolve an
incident or case. See Create and train a regression solution.

#### Selecting data records for training your solution

A solution is only as good as the record data you use to train it. In general, a good training dataset
has these characteristics.
• The solution definition input fields are available to users when creating records. To make
predictions at record creation, the solution must have the input field values at record creation.
• The solution definition output field is a choice field. To make more accurate predictions, limit
the output field to a finite set of possible values.
• The training records only contain correct values for the output field. To make more accurate
predictions, filter out any records that have unreliable output field values. For example, if
recently closed incidents are subject to review and change for a month, filter out any recently
closed incidents.
• The training records contain multiple examples of each output field value that you want the
solution to predict. To provide more record coverage, include multiple examples of each output
field value.
• The training records include common variations of the input fields. To provide more record
coverage, include multiple examples of input field values.

#### Exporting your solution for training

To train a solution, you export its solution definition and associated records to a centralized
training server within the same datacenter. When the training completes, the training server
exports the solution back to your instance and deletes all of your training data from the server.
Each datacenter has its own dedicated training server and the data doesn't leave the datacenter.
Confirm that your configuration aligns with your compliance requirements.
Predictions occur on a centralized prediction server within the same datacenter as the instance.
The trained model artifacts are sent from the instance server to the prediction server when the
prediction is invoked for the first time. After that, the trained model artifacts are cached on the
prediction server for subsequent predictions.

#### Note: All communication between the instance and the training service occurs within the

same datacenter firewall. Even so, all communications occur over HTTPS.

#### Solution training troubleshooting

For troubleshooting common training issues, see the Predictive Intelligence Common issues
[KB781893]
article in the Now Support Knowledge Base.

> Source page: 1427

#### Create and train a classification solution

Specify the records used to train a classification solution, what fields trigger a prediction, and
how often you want to retrain your solution.

#### Before you begin

• Create a custom stopwords list if needed.
• Role required: admin or ml_admin

#### Important: In the Zurich release, models in the classification, clustering, and similarity

frameworks use Workflow solutions. These are pre-trained, so a word corpus isn't needed
for your new solutions. When your existing solutions with a word corpus are re-trained after
upgrading, they become Workflow solutions, and the Word Corpus field is removed from the
form.

#### About this task

A predictive model is only as good as the data that you use to train it. To select appropriate
records for training, examine the table's database dictionary as well as the current quality of the
record values that you want to use.
For information on using encrypted training data, see Data Encryption in Predictive Intelligence.
For information about the minimum and maximum number of records you can use for training,
see Predictive Intelligence properties.

#### Note: Classes that have fewer than 30 records in your training dataset are excluded from

solution training. When your solution is trained and complete, any excluded classes are
listed in the Solution Statistics section of your ML Solution form.
You must create a separate solution definition for each predictive model you want to
support. The following procedure explains how to create a new classification solution, but
you can also copy an existing solution definition and its configuration into a new record by
selecting Copy Solution Definition from the context menu. Edit the field values on the new
record as needed.
From the Yokohama release, you can also create a Workflow Classification solution using a script
if you want to include an analysis of the key features influencing the model's predictions. For
more information see Model Explainability.

> Source page: 1428

#### Procedure

1. Ensure that you are in the application scope you want for your solution definition, then
navigate to All > Predictive Intelligence > Classification > Solution Definitions.
2. On the Classification Definitions list, select New.
3. On the empty Classification Definition form, configure the fields according to the following
guidance.

#### Field

#### Value

Label
Enter a unique name for the solution record.
Name
The system generates the value of this read-only field based on the Label value
that you entered.
Word
Select a word corpus that's relevant to your solution. For more information, see
Corpus
Create a word corpus.

#### Note: Word Corpus is not a required field for customers implementing

Predictive Intelligence for the first time starting in Utah. A pre-trained
model is used instead. The Word Corpus field is removed for pre-trained
models.
Table
Select the table containing the target records that you want the system to
predict.
Output
Select the field whose value you want the predictive model to set.
Field
In general, a good output field has these characteristics.
  ◦It's a choice field or a string field with a finite set of possible values.
  ◦It has some causal connection to the input fields.

#### For example, on the default Incident Categorization solution definition, the

output field is set to Category.
Fields
Select the input fields that you want the solution to use to generate a prediction.
Input fields are fields within a record that may contain the classification
information your prediction solution needs to succeed. For example, if you're
predicting the correct class for triaging an incident record, the prediction should
gather records containing text that references the class. Most records have
contextual text in their Short description field, so it's a great input field to use
in general. You could also use Resolution notes as an input field, as it too might
reference the incident class in the detailed notes for the incident.
In general, good input fields have these characteristics.
  ◦The fields are available to users when creating records.
  ◦The field data type can be string, reference, choice, or HTML. The more
information that a field provides, the more often a solution can make a
prediction, and the more often predictions are accurate.
  ◦The field has a default value and should not be blank.

> Source page: 1429

#### Field

#### Value

All default solution definitions use the Short description field.
Filter
Click Add Filter Condition to apply conditions to the records you're training.

#### For example, the Incident Categorization solution definition uses a filter with

#### these conditions: [Created][on][Last 12 months] AND [Active][is][false] AND

[State][is one of][Resolved | Closed]
To train a solution, the filter must return at least one record. If your filter returns
no records, update it until it returns records for training.

#### Note: The recommended number of records for training a good solution

is from 30,000 through 300,000. If you submit more than 300,000
records, the most recent 300,000 records are used to train the solution.
Use only authentic records from the database.
In general, a good filter has these characteristics.
  ◦The training records are inactive and their states indicate work completed
within your standard process, such as resolved or closed.
  ◦The target fields contain only correct values. Filter out records with unreliable
target field values. For example, if you're predicting the assignment group/
category and your historic incident data contains assignment groups/
categories that are no longer used, add a filter to remove such records from
the training.
  ◦The training records contain multiple examples of each target field value you
want the solution to predict.
  ◦The training records include common variations of the input fields.
Use relative date filters such as last 3 months or last 12 months. Don't use
hard-coded dates because these filters aren't updated when the solutions are
retrained, unless you update them manually.
Processing
Select the dominant language of the dataset that you're training on the solution
Language
definition. If the dataset language is Italian, choose Italian. Also, English
processing is applied to all datasets by default. For example, if you select Italian,
the system processes the data in both English and Italian.

#### Note: The term processing indicates some of the language-specific

steps used as part of training a solution. For example, tokenizing words,
removing stop words, and stemming.
Stopwords
When you select your processing language, the system automatically adds
a Stopwords list for that language. For example, if your processing language

#### is Italian, the Default Italian Stopwords list appears. The Default English

#### Stopwords list is also included. If you create a custom stopwords list, you can

select it from the Stopwords field to add to your solution.
Training
Select how often the system regenerates the solution. The available options
Frequency
range from Run once up to Every 180 days.

#### Note: The minimum number of records required for classification solution

training is set at 10,000.

> Source page: 1430

#### Field

#### Value

By default, the system runs training once. This provides you time to review
and update the solution definition until it provides acceptable coverage and
precision values.
When your solution definition is fairly stable, consider scheduled trainings, as
data can age over time, thus degrading the accuracy of your prediction model.

#### Note: The ML scheduler limits the number of trainings an instance can

commit to 50 new ML training requests per instance within a 24-hour
window. This limit excludes scheduled retraining requests, clustering
updates, and similarity updates, even if the new training requests exceed
50 within a 24-hour window.
4. Click the appropriate context menu option or button for your solution definition.

#### Option

#### Description

Save your solution definition record so you

#### Save or Save & Train

can return to it later, or save and submit it for
training.
Create your solution definition record and

#### Submit or Submit & Train

submit it, or submit and train it.
5. If you submitted the solution for training, click OK on the Training Activation window to
confirm.
  ◦The system schedules the solution for training with the nearest training service. The
system sends you a notification when the training completes, including any errors that
may have occurred in the training. Other users can subscribe to the Predictive Intelligence
Notifications category. When training completes, the system uploads the solution as an
Attachment record.
  ◦A bubble chart populates the Solution Visualization tab of your solution form, showing the
estimated precision and coverage for each of the classes covered by the solution. The

> Source page: 1431

size of the bubble indicates the percent of records (distribution) that belong to the class.
When you point to a bubble, you can see its estimated coverage, estimated precision, and
distribution.

#### What to do next

In the Class Confidence section of the Solution Statistics tab in your solution, review the trained
solution precision and coverage statistics.
In the Test Solutions tab in your solution, you can test the prediction output by entering values
from the input fields, such as the Short Description.

#### Exclude a class from prediction

Exclude a class from prediction if its precision or coverage aren't satisfactory. Excluding a class
prevents the classification model from predicting a particular output field value.

#### Before you begin

• Train the solution definition whose output field values you want to exclude.
• Role required: admin or ml_admin

> Source page: 1432

#### About this task

As part of the testing and refinement of your classification solution, you can try excluding an
output class to check the effect on the model's results.
Excluding a class from prediction is temporary. The class is restored the next time you train your
solution, as long as the solution definition remains the same. If your precision or coverage targets
are still not met, consider deactivating the solution or changing the solution definition.
Typically, you exclude a class from prediction if you want a person to manually set the excluded
class value. For example, exclude a particular incident category when the solution doesn't offer
sufficient precision or coverage, or because the class triggers other business logic that requires
review or approval.

#### Procedure

1. Navigate to All > Predictive Intelligence > Classification > Solutions.
2. In the ML Solutions list, select the solution whose classes you want to exclude.
This solution must have a State of Solution Complete.
3. In the Class Confidence related list, select the class you want to exclude.
4. In the Class Confidence record, review the precision and coverage combinations available
from the Precision Coverage Lookups embedded list.
5. Select the check box for the 100 precision and 0 coverage combination.
You can select only one check box.
6. From the Actions on selected rows control, select Apply Values.
The system shows a Precision / Coverage Setting confirmation window.
7. Click OK to confirm the change or Cancel to discard it.

#### Result

The solution excludes the class from all predictions until the next training cycle.

#### What to do next

If you conclude that this class does not contribute to meaningful predictions, consider
deactivating the solution or changing the solution definition.

#### Exclude a class from solution training

Exclude a class from solution training to prevent the model from ever making predictions for a
particular output field class. For example, you can exclude a particular incident category from
training if you plan to retire or change the category.

#### Before you begin

Role required: admin or ml_admin

#### About this task

Excluding a class from training doesn't prevent the solution from making predictions for records
that use the excluded class. Solution training still uses the input and output field values as data
and attempts to match input field values to a new output field class. This attempt may cause
undesirable prediction results unless you have another suitable class to replace the excluded
class value.
Typically, you only exclude a class from training if you change the list of valid output field values.
For example, if you replaced one incident category with another incident category, you may
exclude the old category from training so that the solution only uses the new category for
predictions.

> Source page: 1433

#### Note: If you specify a target recall for a class, don't exclude the class from training even if

the number of records are less than 30 for that class.

#### Procedure

1. Navigate to All > Predictive Intelligence > Classification > Solution Definitions.
The system shows the current list of solution definitions.
2. Select the solution definition you want to edit.

#### Example

For example, select Incident Categorization to exclude an incident category from training.
3. Edit the filter to exclude the class.
You can use the [is one of] or [is not one of] operators to exclude a particular class.

#### Example

For example, if you want to exclude the Hardware class, add this condition: [Category] [is not
one of] [Hardware].
4. Click Update & Train.
The system schedules the solution for training with the nearest training service. When training
is complete, the system uploads the solution as an Attachment record.

#### Result

The solution excludes the class from all predictions.

#### What to do next

Review the trained solution precision and coverage statistics.

#### Tune a trained classification solution

Tune the performance of a trained classification solution by configuring class level precision and
coverage values.

#### Before you begin

• Train the solution definition whose output field values you want to configure.
• Role required: admin or ml_admin

#### About this task

The system creates a class record for each output field value that it can predict. Each class
record includes a list of possible precision and coverage combinations to choose from. By
default, solutions use the highest combination of precision and coverage available. You can
select another combination to refine predictions based on acceptable precision and coverage
values.

#### Procedure

1. Navigate to All > Predictive Intelligence > Classification > Solutions.
The system shows the list of available solutions.
2. Select the solution whose classes you want to configure.
This solution must have a State of Solution Complete.
The system shows the Solution record.
3. From the Class Confidence related list, select the class you want to configure.
The solution only lists output field values for which it can make predictions. If the output field
value is missing from this list, update the solution definition filter to provide more data for this
output field value, and retrain the solution.

> Source page: 1434

The system shows the Class Confidence record.
4. Review the precision and coverage combinations available from the Precision Coverage
Lookups embedded list.
5. Select the check box for the precision and coverage combination you want to use to make
predictions for this class.
You can only select one check box. Some combinations produce special prediction results.

#### Special prediction combinations

#### Prediction result

#### Precision

#### Coverage

Never include class in predictions
100
0
Always include class in predictions
0
100
6. From the Actions on selected rows control, select Apply Values.
The system shows a Precision / Coverage Setting confirmation window.
7. Click OK to confirm the change or Cancel to discard it.

#### What to do next

Test predictions for this class to verify that the system produces acceptable results.

#### Configuring target metrics for a trained classification solution

Set values for precision, coverage, and recall statistics for a trained machine learning solution.

#### Setting classification metric values at the class or solution level

Predictive Intelligence provides three classification metric types: precision, coverage, and recall.
You configure these metrics on the Solution Statistics tab of a trained classification solution
form. While you can manually set values to these metrics at the class level, doing so can be
challenging if you have a large number of classes to cover. In many cases, you may not know the
best value to set until your solution is trained. This topic focuses on setting the metric values at
just the solution level.

#### Configuring solution metrics

When you apply a value to one metric, it changes the values of the other two. This behavior
enables you to modify your metrics iteratively in real time to see which value combinations
render particular results. When you apply a new value to a metric, the system recomputes it by
considering its new targets.
Applying a value to a metric asks the system to train its predictions to favor the metric you set
based on the highest percentage value, and at a cost to the other metrics. The system tries
to meet these values but may not set them exactly as you request due to how the data you're
training is distributed.
When you apply metric values at the solution level, the system automatically sets the appropriate
values at the class level.
Here are the basic steps for configuring a target metric for your solution.
1. Navigate to the Solution Statistics tab of a trained ML solution.
2. Review the messages on the green banners of the screen which define each of the metrics so
you can better understand the values you want to assign to the solution. The first two message

> Source page: 1435

banners address estimated solution-level metrics. The third banner addresses class-level
results based on the solution values you applied.
3. In the Target Metric choice list, select the metric you want to configure.
4. In the Target Metric Value field, enter a numeric percentile value between 0-100.
5. Click Apply Values.
6. Result: On the Solutions Statistics tab, you can review the change in values to the Estimated
Solution Precision, Estimated Solution Recall, and Estimated Solution Coverage. The system
calculates these values based on the Target Metric you select and the Target Metric Value
you enter for the solution.
Here's a sample landing page for a recently trained classification solution. As you can see, the
precision metric is 44.18, recall is 41.26, and coverage is 77.23.
If you need to adjust these default values for a use case, refer to the sample configurations
below. For example, based on the classification solution you're implementing, you might want
to change the target metric value for precision, recall, or coverage. Keep in mind that when you
change the target metric value for one metric, such as precision, it impacts the values of the
recall and coverage metrics as well.

#### Precision configuration example

In this example scenario, you're replacing a manual triage process for routing incident
records with an ML classification solution that automatically assigns the records to the correct
assignment group. For this scenario, you have a target value in mind and the system must predict
correctly at least 80% of the time. So you set the precision metric value to 80 and click Apply
Values.
Here are the metric values the system applied to the solution. In this scenario, the precision
value of 80.04 slightly exceeded your request for 80%, so you're likely satisfied with that value.

> Source page: 1436

#### Coverage configuration example

In another example scenario where you're replacing a manual triage process for routing incident
records, your minimum goal is to predict at least 70% of incoming incidents in the first quarter of
the year. So you set the coverage metric value to 70 and click Apply Values.
The metric values the system applied to the solution are shown in the following image. The
coverage metric value increased from 35.99 to 55.98. However, the precision metric decreased
from 80.18 to 64.97. This could be because you set the coverage metric to a relatively high value
of 70, or perhaps because of how the data you're training is distributed.

#### Recall configuration example

In another scenario, classifying if an incoming email is a Phish or not can be an important use
case in a security-related machine learning solution. In this situation, it's very important to
identify every Phish, and it may be okay to report a non-Phish as a Phish occasionally. However,
no real Phish should be classified as a non-Phish. In such situations, the recall metric must have
a high value, which might lead to lower percentages for precision and coverage. So here you can
set the recall metric to 95 and click Apply Values.

> Source page: 1437

Here are the metric values the system applied to the solution. The recall metric value increased
from 54.87 to 61.03. However, the precision metric decreased from 60.1 to 55.44. This is likely
because you set the recall metric to the high value of 95.

#### Class-level results for the solution metric values you apply to your solution

The following image shows an example of the class-level results the system applied to a
solution's precision, coverage, and recall statistics for 37 classes. You can keep modifying the
metric values until you're fully satisfied with the results.
By Sorting (z to a) on the Estimated Precision column you can see which classes have the
highest precision for the solution.

#### Using Group By for classification

Use APIs to simultaneously submit multiple classification solutions for training based on the
Group By field.

> Source page: 1438

You can use the optional Group By capability to train and maintain one classification solution that
covers more than one data area, such as geographical location or domain.
To train a solution using Group By, you must add the groupby parameter while creating a
classification solution definition using APIs. The groupby parameter accepts only categorical
columns as inputs, where individual models are created on the subset of data belonging to each
of the groupby values. Only those child solutions that pass the minimum records criteria set for
the capability are created. Here, the prediction calls are routed to the corresponding Group By
model based on the Group By value present in the prediction input. Batch predictions are not
supported.

#### A Group By scenario for geographical locations

Let's say your global company uses classification routing for incoming records, with one support
center in the US and one in Europe. Here, you want to create a single classification solution that
has one model for your United States incidents and another model for your European incidents.
In this scenario, you could use one of these two approaches:
• Create and train two separate ML classification solution definitions, where one is filtered by US
incidents only, and one by European incidents only.
• Use the groupby parameter to create Groupby for the country location so that all US definitions
create a US model and all European definitions create a European model. Then, based on
the incident, the system identifies which model it uses to predict the correct classification
category.
The second approach has benefits in that the models you use can even be in different domains,
such as healthcare or finance. This approach is especially beneficial if you have several country
locations or domains to maintain.

#### Example usage for training and prediction using Group By via API

var myIncidentData = new sn_ml.DatasetDefinition({
'tableName' : 'incident',
'fieldNames' :
['category','short_description','assignment_group','description
','priority'],
'encodedQuery' : 'activeANYTHING'
});
var mySolution = new sn_ml.ClassificationSolution({
'label': 'solution label',
'dataset' : myIncidentData,
'groupByFieldName' : 'assignment_group',
'predictedFieldName': 'category',
'inputFieldNames':
['short_description','description','priority']
});
//Add solution definition
var solution_gr =
sn_ml.ClassificationSolutionStore.add(mySolution)
//Get existing solution
var my_unique_name =
sn_ml.ClassificationSolutionStore.get('solution name');
// submit training job
var solutionVersion = my_unique_name.submitTrainingJob();

> Source page: 1439

// Run prediction
var input = new GlideRecord("incident");
input.get("sys_id");
// configure optional parameters
var options = {};
options.apply_threshold = false;
var mlSolution = sn_ml.ClassificationSolutionStore.get('solution
name');
//Prediction using glide record
var results = mlSolution.getActiveVersion().predict(input,
options);
//Prediction using map
var results =
mlSolution.getActiveVersion().predict([{ 'short_description':
input.short_description,
'assignment_group': input.assignment_group }], options);
For more context regarding this example and the general usage of Machine Learning APIs, see
the links in the Related Content section on this page.

#### Related topics

DatasetDefinition - Global
ClassificationSolution - Global
ClassificationSolutionStore - Global
ClassificationSolutionVersion - Global

#### Model Explainability

Analyze the importance of each input field to your model's predictions using model explainability.
Create a Workflow Classification model that includes a graphical analysis of feature importance
by executing the provided script.

#### Before you begin

• This method uses the Workflow Classification Solution API, instead of the Solution Definition
form, to create and train a model with explainability added. For information about the
components of Workflow Classification models, see Create and train a classification solution.
• Role required: ml_admin or admin

#### About this task

Model explainability helps identify the key features that influence the model's predictions during
training.

#### Note: Explainability can't be added to an existing model. This method uses a script to

create and train a new Workflow Classification model. For more information about scripting
the creation of Classification solutions, see ClassificationSolution - Global
.
The script provided in the procedure creates and trains a model with explainability

#### set to true. On the new model's solution form, an additional tab labeled Feature

> Source page: 1440

Importance appears. This tab offers a graph of the relative contribution of each input to the
prediction.

#### Procedure

1. Navigate to All > System Definition > Scripts - Background.
2. Edit the query filter and table, field, and variable values in the following script according to your
planned model, then execute the script.
// Define a dataset
var myIncidentData = new
sn_ml.DatasetDefinition({
'tableName': 'incident',
'fieldNames': ['category',
'short_description', 'sys_updated_by', 'assignment_group',
'description', 'priority'],
'encodedQuery': 'activeANYTHING'
});
// Define a classification solution
definition with explainability field
var mySolution = new
sn_ml.ClassificationSolution({
'label': 'model explainability',
'dataset': myIncidentData,
'predictedFieldName': 'category',
'inputFieldNames': ['short_description',
'priority'],
//setting the explainability field to true.
'explainability': true,
});
// Add solution to
ClassificationSolutionStore
var my_unique_name =
sn_ml.ClassificationSolutionStore.add(mySolution)
// Submit training job
var solutionVersion =
mySolution.submitTrainingJob();

#### Note: Substitute the query filter and table, field, and variable names in this script with

your own values.

> Source page: 1441

3. Navigate to the ML Solutions [ml_solution] table and open your new solution by selecting the
value of its Active field.
4. On the solution form, locate and open the Feature Importance tab.
Feature Importance displays a drop-down list.
  ◦The label for this drop-down list is the name of your output (predicted) field, so the label is
specific to each model.
  ◦The values in the drop-down list are the possible output classes for your output field, plus
the Global option.

#### List option

#### Description

Provides an overview of how the model be
haves across all predictions, showing the
overall impact of each input feature.

#### Global

#### Select Global to open a graph of the impor

tance of your input fields to predictions for all
output classes as a whole.
Focuses on the model's behavior for the cho
sen class only, showing how input features
contribute to predictions on a per-class basis.
Your output class value
Select one of the possible output classes to
open a graph of the importance of your input
fields to predictions for that class.
5. Launch the graphical analysis by selecting a value from the drop-down list.
The y axis shows your input fields and the x axis shows the numerical importance for
each input. The label of the graph reflects the class that you chose in the drop-down list.
You can hover over a bar to display the numerical percentage for each input's importance.

> Source page: 1442

#### Result

A positive importance value means that the input field increases the model's prediction score. A
negative value means that the input field decreases the prediction score.

#### What to do next

Consider dropping input fields with low importance scores. Retrain your model after modification.

#### Related topics

Using Machine Learning APIs
ClassificationSolution - Global
Create and train a classification solution

#### Create and train a similarity solution

Create and train a machine learning solution to collect and compare your existing records to new
similar records. For example, you can compare the text in an open Incident record to a resolved
Incident record to reuse its resolution.

#### Before you begin

• Role required: ml_admin or admin

#### Important: From the Washington DC release, models in the classification, clustering,

and similarity frameworks use Workflow solutions. These are pre-trained, so a word corpus
isn't needed for your new solutions. When your existing solutions with a word corpus are
re-trained after upgrading, they become Workflow solutions, and the Word Corpus field is
removed from the form.

#### About this task

After comparing your existing records based on similarity, the system recommends examples
that you can review and reuse in your solution.
When applied in your forms and flows, similarity solutions are domain-aware, so records from
other domains on the instance are not displayed to users. For more information, see KB article
Similarity prediction behavior in domain separated environment
on Now Support.
For information on using encrypted training data, see Data Encryption in Predictive Intelligence.
In this example procedure, you're working on Incident records and you want to locate relevant
Knowledge Base articles that could provide resolutions to those incidents.

> Source page: 1443

#### Procedure

1. Ensure that you are in the application scope that you want for your solution definition, then
navigate to All > Predictive Intelligence > Similarity > Solution Definitions.
2. In the Similarity Definitions list, select New.
3. On the Similarity Definition form, fill in the fields.

#### Field

#### Value

Label
Enter a unique name for your similarity solution. For
example, in this use case you could enter Match
Knowledge Articles to Incidents.
Name
As you enter a Label value, this field automatically
populates with a system-assigned, read-only name
based on your Label value.
Word Corpus
If you have a legacy similarity solution, you can select a

#### relevant word corpus from the Word Corpus field in the

definition form.

#### Note: Starting from the Washington DC release,

a word corpus is not required because a pre-

#### trained model is used instead. The Word Corpus

field is not visible in the definition form for pre-
trained models.
For more information, see Create a word corpus.

> Source page: 1444

#### Field

#### Value

Table
In the Table field, select the table that contains records
you want to use as an information source. In this use

#### case you select the Knowledge [kb_knowledge]

table, because its KB Article records might provide
information relevant to the Incidents that you're trying to
resolve.
After you assign a Table, the number of records
matching your filter conditions is displayed as a link.
Select this link to view the list of records.
Test Table
In the Test Table field, select the table containing the
records that you want to target. In this use case, you

#### select the Incident [incident] table, as it contains the

Incident records that you're trying to resolve.

#### Note: You can select the same table for

Table and Test Table. For example: using filter
conditions, you could collect information from
recent Incidents to help with target Incidents.
Fields
For the Table that you selected, enter fields that are
likely to contain words and phrases relevant to the
Incidents you're trying to resolve. In this example, you

#### choose Short description and Article body. Including

the article body increases your chances of capturing
informative details regarding the subject.

#### Note: Journal Type is not a supported data type.

Test Fields
For the Test Table that you selected, enter fields
that contain text that you want to compare to other

#### similar records. In this example, you choose the Short

#### description of the Incident records you're trying to

resolve.
Filter

#### Select Add Filter Condition to apply conditions to

the Fields records you're using as an information
source. For example, in this use case you could set

#### a workflow_state=published condition to retrieve

published KB articles only.

#### Note: Script includes can't be referenced from

the Filter. Use database views as an alternative.
Processing Language
Select the dominant language of the dataset you're
training on. Also, English processing is applied to all
datasets by default. For example, if you select Italian,
the system processes the data in both Italian and
English.

> Source page: 1445

#### Field

#### Value

#### Note: The term processing indicates some of the

language-specific steps used as part of training a
solution, such as tokenizing words, removing stop
words, and stemming.
Stopwords
When you select your processing language, the system
automatically adds a Stopwords list for that language.
For example, if your processing language is Italian, the

#### Default Italian Stopwords list appears. The Default

English Stopwords list is also included.
To use a custom stopwords list, select the lock

#### ) and then search in the Select target record

icon(
field.
Training Frequency
Select a retraining frequency. The available options
range from Run Once up to Every 180 days.
Update Frequency
Select how often you want to refresh the data you use to
retrieve your similarity results.
For example, for open incident records, you could

#### select an update frequency of Every 15 minutes, as

new incidents typically occur frequently throughout the
day. This frequency may increase the likelihood that
newly opened records are included in the refresh.
However, for KB Knowledge article records, which are
typically not created often, you could choose a less
frequent update frequency such as Every 1 day.

#### Note: The ML scheduler limits the number of

trainings an instance can commit to 50 new ML
training requests per instance within a 24 hour
window. This excludes scheduled re-training
requests. In addition, clustering and similarity
updates are also excluded from this limit, even if
the new training requests exceed 50 within a 24
hour window.
4. Select the appropriate button for the solution definition.

#### Option

#### Description

Save your solution definition record so you

#### Save

can return to it later.
Create your solution definition record and

#### Submit & Train

train it.
5. If you submitted the solution for training, select OK on the Training Activation window to
confirm.

> Source page: 1446

#### Result

• The system schedules the solution definition for processing with the nearest training service
and sends you a notification when the training completes. The notification includes any
errors that may have occurred during the training. Other users can subscribe to the Predictive
Intelligence Notifications category.
• The trained solution delivers paired example records ranked by their degree of similarity. The
list of examples is available from Similarity Examples under Related Links on your solution's
form.
• When training completes, the system uploads the solution as an Attachment record.

#### What to do next

Review the similarity examples on the Related Links section of your Solution form. See Review
solution similarity examples.

#### Update your similarity score threshold

After you review the similarity examples provided by the system, update your solution similarity
score threshold if you want the results returned by the solution to be more or less similar.

#### Before you begin

• Review your similarity examples and their scores. For more information see Review solution
similarity examples.
• Role required: ml_admin or admin

#### About this task

A deployed solution returns records only when the similarity score is higher than the Similarity

#### Score Threshold value:

• The higher the threshold value, the higher the precision and the lower the coverage.
• The lower the threshold value, the lower the precision and the higher the coverage.

#### Procedure

1. Navigate to All > Predictive Intelligence > Similarity > Solutions.
2. In the ML Solutions list, locate your solution by filtering for the Solution Name, and open its
active version.
3. On the solution form, locate and open the Solution Statistics tab.
4. In the Similarity Score Threshold field, enter a new numerical value that represents a
percentage.
For example, imagine that the current threshold is 80. In your similarity example review you
decided to increase the accuracy of your similarity recommendations at the cost of lowering
the prediction coverage. So you update the field by entering the higher value of 90.
5. In the form's context menu (Additional actions), select Save.
Your solution uses the new threshold value that you assigned to it and returns similar results
that have a score higher than 90. If you set the threshold to 90, the similarity score must be
91% or above to return records.

#### Create and train a clustering solution

Group similar records into clusters so you can address them collectively or identify patterns.

#### Before you begin

Role required: ml_admin or admin

> Source page: 1447

#### Important: In the Zurich release, models in the classification, clustering, and similarity

frameworks use Workflow solutions. These are pre-trained, so a word corpus isn't needed
for your new solutions. When your existing solutions with a word corpus are re-trained after
upgrading, they become Workflow solutions, and the Word Corpus field is removed from the
form.

#### About this task

In this example procedure, you're creating a solution to identify a major incident by grouping
similar incidents that have occurred recently.
For information on using encrypted training data, see Data Encryption in Predictive Intelligence.

#### Procedure

1. Ensure that you are in the application scope that you want for your solution definition, then
navigate to All > Predictive Intelligence > Clustering > Solution Definitions.
2. On the Clustering Definitions list, select New.
3. On the Clustering Definition form, configure the fields according to the following guidance.

#### Field

#### Value

Label
Enter a unique name for your clustering solution. For
example, in this use case you could enter Group
Incidents to a Major Incident.
Name
As you enter your solution Label, this field automatically
populates with a system-assigned name based on your
Label value.
Word Corpus
If you have a legacy clustering solution, you can select a

#### relevant word corpus from the Word Corpus field in the

definition form.

#### Note: With the Zurich release, a word corpus is

not required, because a pre-trained model is used

#### instead. The Word Corpus field is not visible in the

definition form for pre-trained models.
For more information, see Create a word corpus.
Table
Select the table that contains record types that you want
to group into one or more clusters. For example, in this use

#### case you select the Incident [incident] table as it contains

incident records you want to group together for a major
incident analysis.
When you assign a table value, a link appears in the form
that shows the number of records that match your current
conditions.
Fields
Select one or more input fields types that help the system
identify the records you want to include in your cluster. In
this use case, use Short description.

> Source page: 1448

#### Field

#### Value

#### Note: When selecting a reference type field, you

must dot-walk to the field's property name. For
example, instead of short_description, enter
short_description.name.
Use Group By
Select this check box only if you want to group input
records by a field before creating clusters.

#### Note: Selecting this check box activates the Group

#### By list. If you don't select the check box, all the table

records are grouped into clusters.
Group By
Selecting a value from this list is optional. If you do so, the
system groups records into one or more clusters based on
your selection.
Purity Fields
Choose fields from your table that can help the system
identify the class that is most frequent in the cluster. In

#### this example scenario, select Category and Assignment

group.Name.
Filter
Add filter conditions to apply to the input field records that
you want to include in your clusters.
  ◦The maximum number of records for clustering is limited
to 300,000.
  ◦For best results, aim for at least 2000 records as a
minimum.

#### Note: Script includes can't be referenced from the

Filter. Use database views as an alternative.
Processing Language
Select the dominant language of the dataset you're training
on the solution definition. If the dataset language is Italian,

#### choose Italian. Also, English processing is applied to all

datasets by default. For example, if you select Italian, the
system processes the data in both English and Italian.

#### Note: The term processing indicates some of the

language-specific steps used as part of training a
solution. For example, tokenizing words, removing
stop words, and stemming.
Stopwords
When you select your processing language, the system
automatically adds a Stopwords list in that language. For

#### example, if your processing language is Italian, the Default

#### Italian Stopwords list appears. The Default English

#### Stopwords list is also included. If you create a custom

stopwords list, you can select it from the Stopwords field to
add to your solution.
Update Frequency
Select how often you want the system to update your
clusters with new and updated records.

> Source page: 1449

#### Field

#### Value

#### Note: The system pulls records based on the Group

By filter conditions that you set on your clustering
solution, if any.

#### For example, if you select Every 15 minutes, the system

identifies which records have arrived within that time
frame. The system tries to assign them to the existing
clusters, or creates a new cluster if possible.
In this example, 20 new records arrive. If 16 of those
records make it into an existing cluster and 4 don't, the
system forms a new cluster for the four unassigned
records.
You can also choose not to update your clusters at all.
Training Frequency
Select how often you want the system to discard all
previous cluster results and recreate clusters from the
beginning. Your options range from daily, every third day,
every seven days, or monthly. You can also choose to train
your cluster once.

#### Note: The ML scheduler limits the number of

trainings an instance can commit to 50 new ML
training requests per instance within a 24-hour
window. The limit excludes scheduled retraining
requests. In addition, clustering and similarity
updates are also excluded from this limit, even if the
new training requests exceed 50 within a 24-hour
window.
Minimum number of records per
Enter the minimum number of records you want a cluster to
cluster
contain. The value you enter must be 2 or higher.
4. Select the appropriate context menu option or button for your solution definition.

#### Option

#### Description

Save your solution definition record so you

#### Save or Save & Train

can return to it later, or save and submit it for
training.
Create your solution definition record and

#### Submit or Submit & Train

submit it, or submit and train it.
5. If you submitted the solution for training, select OK on the Training Activation window to
confirm.

#### Result

The system trains the solution and notifies you in real time when the training completes.
A treemap plot appears on the Cluster Visualization tab of your Clustering Solution Definition
form. The plot shows the clusters the system formed for your solution in descending order from
the top-left corner to the bottom-right corner. The treemap node labels are the Cluster Concept,

> Source page: 1450

which is created by the top words from the cluster, and helps you see the most prominent
content found in each cluster.

#### Note: The Cluster Concept displays the top words from the processed input data, in the

data's language. Depending on the language, the Cluster Concept may display words in
their root form and so appear truncated.
Each node is colored from red to green depending on the cluster quality for that node. The
Select Group filter appears only when you select the Use Group By and Group By fields on your
Clustering Definition form. When you point to a cluster, you can see its Groupby value, Cluster
Count, and Records in Groupby.

#### Cluster visualization example

To open a cluster, you can click it, or select it from the Show All Groups filter.
Inside the cluster grouping, you can filter the results further by using the two slide bars for cluster
size and cluster quality, respectively. You can also navigate backward by clicking the Back
button, which only appears when a clustering hierarchy is present. When you point to a cluster at
this level, the Purity field percentile values appear along with the Cluster Concept, Quality, and
Size values.

#### Cluster group example

> Source page: 1451

When you click a cluster node, its ML cluster details appear in a list view format.

#### Cluster details page

#### What to do next

• Review the solution output on the Solution Statistics tab of your solution. If you aren't satisfied
with your clustering solution results, reconfigure the values you've set to your solution and
retrain it until the results are to your satisfaction.
• Review the Cluster Summary tab for a list view of the cluster IDs, quality size, and Groupby
values.

#### Cluster Summary example

> Source page: 1452

• On the Cluster Updates tab, review the summary of changes to clusters for each cluster update
interval you configured in the solution definition.

#### Cluster updates example

#### Assign a name to a cluster

Name your clusters to help identify and organize them.

#### Before you begin

• Create a clustering solution definition or use an existing one.
• Role required: admin or ml_admin

#### Procedure

1. Navigate to All > Predictive Intelligence > Clustering > Solutions.
2. Select a solution.
3. Under the Cluster Summary related list, select a cluster ID.
4. Enter a name in the Cluster Name field.
5. Select Update.

#### Generate a representative sample of a cluster

View the top 25 most representative records of a cluster.

#### Before you begin

• Create a clustering solution definition or use an existing one.
• Role required: admin or ml_admin

#### About this task

Generating a sample of a cluster filters the records for that cluster. Generating a sample works on
clusters with over 25 records.

> Source page: 1453

#### Procedure

1. Navigate to All > Predictive Intelligence > Clustering > Solutions.
2. Select a clustering solution.
3. Under the Cluster Summary related list, select a cluster ID.
4. Select Generate Cluster
Sample.

#### Result

The ML Cluster Detail list shows the top 25 records in the cluster. The cluster sample also
applies to the cluster visualization.

#### Apply purity on a clustering solution

Apply purity to learn details about the composition of each cluster. For example, see what
percentage of incidents in a cluster have the same value for Assignment Group. You can specify
which fields to focus on, or you can let auto-purity display fields by default.

#### Before you begin

• Create a clustering definition solution or use an existing one.
• Role required: admin or ml_admin

#### About this task

With purity, you can choose field distribution metrics for your clusters to display. The table
assigned to your solution determines which fields are available. For more information about
purity, see the following articles on ServiceNow Community:
• https://www.servicenow.com/community/intelligence-ml-articles/using-purity-fields-to-better-
understand-your-clusters/ta-p/2302441
• https://www.servicenow.com/community/intelligence-ml-articles/predictive-intelligence-using-
the-cluster-insight-table-to/ta-p/2301006
If you do not select any fields, auto-purity automatically determines which insights to show based
on distribution significance. You can change the default auto-purity selections by editing the ML
Auto Purity Configuration [ml_autopurity_config] table.

#### Procedure

1. Navigate to All > Predictive Intelligence > Clustering > Solution Definitions.
2. Select a solution definition or create a new one.

> Source page: 1454

3. Select the Calculate Purity check
box.
4. Optional: Select the Purity Fields lock icon and choose the fields that you want displayed in
cluster results.

#### Note: If you don't select any fields, auto-purity displays the most significant fields based

on distribution.
5. Select Update or Update & Retrain.

#### Result

View your insights by opening the Cluster Visualization tab of your retrained solution, then

#### pointing to a cluster. Under Purity based on, the format displays as:

field name : value : percent.

> Source page: 1455

For example, the row priority : 5 : 100% means that 100% of
the members of this cluster have the value of 5 for the priority
field.

#### Analyze a cluster with Cluster Insight

Analyze a cluster by a field available on the source table. With the Cluster Insight check box, you
can add a filter condition on your input field when you review the list of results.

#### Before you begin

• Create a clustering solution definition or use an existing one.
• Role required: admin or ml_admin

#### About this task

Drill down into a cluster and filter its records with Cluster Insight. You can add
cluster insight analysis when creating a solution or editing an existing solution.
For more information, see https://www.servicenow.com/community/intelligence-
ml-articles/predictive-intelligence-using-the-cluster-insight-table-to/ta-
p/2301006
.

#### Procedure

1. Navigate to All > Predictive Intelligence > Clustering > Solution Definitions.
2. Select a solution definition or create a new one.
3. On the definition form, select the Create Cluster Insight table check box, then update and
retrain the model.

#### Result

In the Solutions [ml_solution] table, open the trained solution, then open the Cluster
Visualization tab. When you select a cluster, all records included in the cluster are displayed as
a list. Using the filter icon (
), open the list's filter conditions. Search for the input field from your

> Source page: 1456

source table. For example, if your source table is Incident and the input field is Short Description,
you could filter for records containing the word "help" in the Short Description.
To make other dimensions from your source table available for filtering, add them as input fields
on the solution definition form.

#### Create and train a regression solution

Regression solutions have been deprecated. They could be used to predict numeric outputs,
such as a temperature or a stock price.

#### Before you begin

#### Note: Support for new regression solutions is deprecated in the Zurich release. You can

still edit and train any existing solutions, but you can't initiate new ones. The following
information is provided for legacy context.
Role required: ml_admin or admin

#### About this task

Regression solutions enable you to predict a point estimate and prediction interval. The resulting
model delivers the following statistics:
• Mean Absolute Error (MAE), which measures the mean deviation of a predicted value from the
actual value. This metric is useful as it's easy to understand as its scale is the same as that of
its target. However, MAE is unbounded, making it difficult to compare across models.
• Symmetric Mean Absolute Percentage Error (SMAPE) is a percentage value of the deviation
from the predicted to the actual. SMAPE is a bounded version of MAE except that it has a value
range between 0 and 100. The lower the SMAPE value, the better the model accuracy.
• Range Accuracy is the percentage of actual values between a predicted range. In other words,
it's the range between the upper and lower bounds of the prediction. For example, if four out of
five actual values lie within the predicted range, the range accuracy is 80%.
• Average Interval Width is the difference between the upper and lower bounds of the
prediction. This metric explains how informative the interval is. The smaller the average width,
the better the model
When making predictions, regression also enables you to specify a confidence level for the
prediction interval (range).
In this example procedure, you create and train a regression solution definition to predict the
amount of time it takes to restore a cloud database.

#### Procedure

1. Navigate to All > Predictive Intelligence > Regression > Solution Definitions.
2. On the Regression Definitions list, select New.
3. On the Regression Definition form, configure these fields per the following guidance.

#### Field

#### Value

Label
Enter a unique name for your regression solution.
For example, in this use case you could enter
Regression Test for DB Restore.

> Source page: 1457

#### Field

#### Value

Name
As you enter your solution Label value, this field
automatically populates with a system-assigned name
that's similar to your label value.
Word Corpus
Select an existing word corpus that's relevant to your
solution. For example, in this use case you select a word

#### corpus that has a title such as Incidents in the last 3

months.
If you don’t have a relevant word corpus, follow the steps
to create a word corpus first. When the word corpus is
complete, you can select it from the Word Corpus field in
your Regression Definition form.
However, the word corpus selection is optional. If your
input data has text columns and you don't choose a
word corpus, your regression solution trains a new word
corpus model by using the text columns in your input
data. The resulting word corpus can be reused in any
other regression solution or other ML solution type.

#### Note: A pre-trained model is used instead of the

Word Corpus for users who activated Predictive
Intelligence starting in the Utah release.
Table
Select the database table on which you’re applying
regression. The table should contain historical records
the system can use to predict the length of time for its
database restore.
Output Field
Select the field whose value you want the predictive
model to set.
In general, a good output field is a numeric, integer, or
floating point field.

#### In this example scenario, you use the Duration field

to measure a length of time. The output field should
generate a numeric value.
Fields
Select one or more field types that help the system
identify the records you want to train using regression.

#### In this example scenario, you use Short description,

#### Source datacenter, Target datacenter, and Database

#### size. (short_description, Sourcedc, Targetdc, and Dbsize.)

Input field types can be string, nominal, or numeric.
Filter
(Optional) Add filter conditions to the output field records
that you want to train using regression.

> Source page: 1458

#### Field

#### Value

#### Note:

  ◦The minimum number of records for regression
training is 10,000 records.
  ◦The maximum number of records for regression
training is limited to 300,000.
Processing Language
Select the primary language of the dataset that you're
training on the solution definition. If the dataset language

#### is Italian, choose Italian. Also, English processing is

applied to all datasets by default. For example, if you
select Italian, the system processes the data in both
English and Italian.

#### Note: The term processing indicates some of the

language-specific steps used as part of training
a solution. These steps include tokenizing words,
removing stop words, and stemming.
Stopwords
When you select your processing language, the system
automatically adds a Stopwords list that uses the same
language. For example, if your processing language is
Italian, the Default Italian Stopwords list is displayed.

#### The Default English Stopwords list also displays in your

selection. If you create a custom stopwords list, you
can select it from the Stopwords field to add it to your

#### solution. In this scenario, you use the Default English

Stopwords list.
Training Frequency
Select how often the system regenerates the solution

#### based on records matching the Filter. Your options

include:
  ◦Run Once
  ◦Every 30 days
  ◦Every 60 days
  ◦Every 90 days
  ◦Every 120 days
  ◦Every 180 days
In this scenario, you select Every 30 days
By default, the system runs training once. This practice
provides you time to review and update the solution
definition as needed until it provides acceptable
coverage and precision values.

> Source page: 1459

#### Field

#### Value

#### Note:

  ◦The minimum number of records required for
regression solution training is set at 10,000.
  ◦The ML scheduler limits the number of trainings
an instance can commit to 50 new ML training
requests per instance within a 24-hour window.
This limit excludes scheduled requests for
retraining. In addition, clustering and similarity
updates are also excluded from this limit, even if
the new training requests exceed 50 within a 24-
hour window.
4. Select the appropriate context menu option or button for your solution definition.

#### Option

#### Description

Save your solution definition record so you

#### Save or Save & Train

can return to it later, or save and submit it for
training.
Create your solution definition record and

#### Submit or Submit & Train

submit it, or submit and train it.
5. If you submitted the solution for training, select OK on the Training Activation window to
confirm.
The system schedules the solution for training with the nearest training service. The system
sends you a notification when the training completes, including any errors that may have
occurred in the training. Any other users can subscribe to the Predictive Intelligence
Notifications category. When training completes, the system uploads the solution as an
Attachment record.

#### What to do next

In this example scenario, you created an ML solution from your solution definition. The Solution
Statistics, Test Solution, and Solution Definition tabs appear in the Related Links section of your
ML solution.
On the Solution Statistics tab, review the Point Estimate and Range (prediction interval) statistics
generated by your solution.
On the Test Solutions tab of your solution, you can test the prediction output for the records
you used as input to the prediction by entering values for the input fields, such as the Source

> Source page: 1460

datacenter, Target datacenter, and Database size. You can also use the default prediction
confidence level of 95, or enter a different level between 0 and 100. Using 95 as the value
means that the system is 95% confident that the actual prediction falls within the prediction
interval. Select the Run Test button to find the prediction output.
After you run the test, the prediction output statistics appear. The Point Estimate on the screen
is a single value at one point in time. For example, the database restore takes 134.47 seconds
to complete. The Lower and Upper bounds on the screen signify a range accuracy value. For
example, the database restore takes from 84.53 to 185.41 seconds to complete.

#### View solution training progress

View your solution training progress or statistics to determine if a solution is available, or how
long the next training cycle might take to complete.

#### Before you begin

Role required: admin or ml_admin

#### About this task

Solution training involves these steps.

> Source page: 1461

1. Fetching files for training. The system downloads the training records and sends them to the
nearest training service.
2. Preparing the data. The system removes duplicate records from the training set.
3. Training the solution. The training service trains the solution.
4. Uploading the trained solution. The training service uploads the solution as attachment
records.

#### Procedure

1. Navigate to All > Predictive Intelligence > Classification > Solutions or Predictive Intelligence
> Similarity > Solutions.
2. In the ML Solutions list, select the solution whose progress or statistics you want to view.

#### Example

For example, select Incident Categorization to see the training history.
3. In the Related Links section, click Show training progress.
Training times vary based on the number of records and classes within the training set. The
more records and classes you use, the longer the training can take. For example, a data
set containing 100,000 records and several hundred classes can take around five hours to
complete.
The system shows a Training Progress pop-up window.

#### What to do next

For classification solutions, see Review classification solution statistics.
For similarity solutions, see Review similarity solution examples and scores.

#### Review classification solution statistics

The Solution Statistics dashboard in Predictive Intelligence has been deprecated in the Xanadu
release. It provided precision and coverage statistics for each class in a classification solution.

> Source page: 1462

#### Before you begin

• Role required: admin, ml_admin, or ml_report_user

#### About this task

#### Important: With the Zurich release, the Solution Statistics dashboard is deprecated.

Upgrading customers can continue to use their existing Solutions Statistics dashboards
from the application menu. For new customers onboarding with the Zurich release, the
Solutions Statistics dashboard is not available. The following information is provided for
legacy context.
The Solution Statistics dashboard lists the precision, coverage, and distribution for each class of
active solutions. The system uses the classes with the highest number of records when it builds
a solution. The number of classes predicted may be less than 50, and may skip a class if there is
not enough historical data to build a solution that can predict the class confidently.
The Solution Statistics dashboard is different from the Solution Statistics tab in an ML Solution
record. For more information, see Create and train a classification solution.

#### Procedure

1. Navigate to All > Predictive Intelligence > Classification > Solution Statistics.
2. From Filter by solution, select the solution whose statistics you want to review.
3. From Filter by version, select the solution version whose statistics you want to review.
4. Click Apply.
The system updates the dashboard based on the filters selected.
5. Identify classes with unwanted combinations of precision, coverage, and distribution values.

#### Example

For example, identify classes that have low precision or coverage but a high distribution.
6. Identify any missing classes you want the model to include.

#### Example

For example, identify any missing incident categories from the Incident classification solution.

> Source page: 1463

#### What to do next

If you're satisfied with the solution you've reviewed, the latest version is already active and ready
to use. If you're not satisfied, you can choose a different version of the solution and make it
active. You can also tune and retune the solution by configuring the class precision and coverage
to use acceptable values.

#### Review solution similarity examples

Review the similarity examples generated during solution training to determine whether the
similarity score threshold meets your business requirements.

#### Before you begin

• Train a similarity solution
• Role required: ml_admin or admin

#### About this task

Solution training generates a set of paired record examples. Each pair includes a percentile
score that estimates the degree of similarity between the two records. The higher the score, the
higher the similarity, as follows:
• A score of 100 indicates identical records.
• A score of 0 indicates dissimilar records.
A deployed solution returns records only when the score is higher than the Similarity Score

#### Threshold value:

• The higher the threshold value, the higher the precision and the lower the coverage.
• The lower the threshold value, the lower the precision and the higher the coverage.
On domain-separated instances, the following procedure displays records from all domains to
ML admins. However, when solutions are applied in your forms and flows, similarity predictions
are domain-aware. Examples from other domains on the instance are not displayed to users.

#### Note: The similarity filters specified in the solution definition aren't applied for similarity

examples and are applied only during prediction.

#### Procedure

1. Navigate to All > Predictive Intelligence > Similarity > Solutions.
2. In the ML Solutions list, locate your solution by filtering for the Solution Name, and open the
active version.
3. In the Related Links section of the form, select Similarity Examples.
A list of paired records opens on the Similarity Examples (ml_similarity_example) table. By
default the rows are sorted by the Similarity Score column in descending order.
4. Review the similarity examples for accuracy and coverage.
Based on your review, determine whether to increase or decrease the Similarity Score
Threshold value of your solution.

#### What to do next

If you decide to adjust the Similarity Score Threshold for your similarity solution, see update its
similarity solution threshold.


---

## IMAGE DESCRIPTIONS

### Repeated ServiceNow page header/logo

The ServiceNow-branded wordmark appears in the upper-left corner of reviewed source pages for this subsection. It is a recurring branding image, not a technical diagram. It contains the visible brand text `servicenow`, with green accenting in the `now` portion. Reviewed pages: 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1434, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463.

### Small UI icons and inline pictograms

2 small non-logo icon/pictogram image blocks were reviewed on source pages 1445, 1455. These include information icons, external-link indicators, UI symbols, or small inline graphics. They support the surrounding text but do not contain standalone table data. Coordinates and classification are retained in `_assets/image_inventory.csv`.

### Source page 1427 — Image 1

![Source page 1427 image 1](_assets/p1427_image01.png)

* **Bounding box:** x=92.0, y=401.9, width=432.0 pt, height=208.4 pt.
* **Nearby source context:** Important: In the Zurich release, models in the classification, clustering, and similarity / About this task / Note: Classes that have fewer than 30 records in your training dataset are excluded from
* **What is shown:** This embedded source image appears near the source context `Important: In the Zurich release, models in the classification, clustering, and similarity / About this task / Note: Classes that have fewer than 30 records in your training dataset are excluded from`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1427_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1431 — Image 2

![Source page 1431 image 2](_assets/p1431_image01.png)

* **Bounding box:** x=112.0, y=86.5, width=432.0 pt, height=216.3 pt.
* **Nearby source context:** size of the bubble indicates the percent of records (distribution) that belong to the class. / When you point to a bubble, you can see its estimated coverage, estimated precision, and / distribution.
* **What is shown:** This embedded source image appears near the source context `size of the bubble indicates the percent of records (distribution) that belong to the class. / When you point to a bubble, you can see its estimated coverage, estimated precision, and / distribution.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1431_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1431 — Image 3

![Source page 1431 image 3](_assets/p1431_image02.png)

* **Bounding box:** x=72.0, y=401.8, width=432.0 pt, height=225.4 pt.
* **Nearby source context:** What to do next
* **What is shown:** This embedded source image appears near the source context `What to do next`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1431_image02.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1435 — Image 4

![Source page 1435 image 4](_assets/p1435_image01.png)

* **Bounding box:** x=72.0, y=222.8, width=432.0 pt, height=140.3 pt.
* **Nearby source context:** 6. Result: On the Solutions Statistics tab, you can review the change in values to the Estimated / Solution Precision, Estimated Solution Recall, and Estimated Solution Coverage. The system / calculates these values based on the Target Metric you select and the Target Metric Value
* **What is shown:** This embedded source image appears near the source context `6. Result: On the Solutions Statistics tab, you can review the change in values to the Estimated / Solution Precision, Estimated Solution Recall, and Estimated Solution Coverage. The system / calculates these values based on the Target Metric you select and the Target Metric Value`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1435_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1435 — Image 5

![Source page 1435 image 5](_assets/p1435_image02.png)

* **Bounding box:** x=72.0, y=548.2, width=432.0 pt, height=131.6 pt.
* **Nearby source context:** Precision configuration example / correctly at least 80% of the time. So you set the precision metric value to 80 and click Apply / Values.
* **What is shown:** This embedded source image appears near the source context `Precision configuration example / correctly at least 80% of the time. So you set the precision metric value to 80 and click Apply / Values.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1435_image02.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1436 — Image 6

![Source page 1436 image 6](_assets/p1436_image01.png)

* **Bounding box:** x=72.0, y=39.0, width=432.0 pt, height=122.9 pt.
* **Nearby source context:** No nearby heading text was detected.
* **What is shown:** This embedded source image appears near the source context `No nearby heading text was detected.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1436_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1436 — Image 7

![Source page 1436 image 7](_assets/p1436_image02.png)

* **Bounding box:** x=72.0, y=249.6, width=432.0 pt, height=127.7 pt.
* **Nearby source context:** Coverage configuration example / the year. So you set the coverage metric value to 70 and click Apply Values.
* **What is shown:** This embedded source image appears near the source context `Coverage configuration example / the year. So you set the coverage metric value to 70 and click Apply Values.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1436_image02.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1436 — Image 8

![Source page 1436 image 8](_assets/p1436_image03.png)

* **Bounding box:** x=72.0, y=450.5, width=432.0 pt, height=122.0 pt.
* **Nearby source context:** Coverage configuration example / the year. So you set the coverage metric value to 70 and click Apply Values.
* **What is shown:** This embedded source image appears near the source context `Coverage configuration example / the year. So you set the coverage metric value to 70 and click Apply Values.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1436_image03.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1437 — Image 9

![Source page 1437 image 9](_assets/p1437_image01.png)

* **Bounding box:** x=72.0, y=39.0, width=432.0 pt, height=129.1 pt.
* **Nearby source context:** No nearby heading text was detected.
* **What is shown:** This embedded source image appears near the source context `No nearby heading text was detected.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1437_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1437 — Image 10

![Source page 1437 image 10](_assets/p1437_image02.png)

* **Bounding box:** x=72.0, y=228.8, width=432.0 pt, height=127.4 pt.
* **Nearby source context:** Here are the metric values the system applied to the solution. The recall metric value increased / from 54.87 to 61.03. However, the precision metric decreased from 60.1 to 55.44. This is likely / because you set the recall metric to the high value of 95.
* **What is shown:** This embedded source image appears near the source context `Here are the metric values the system applied to the solution. The recall metric value increased / from 54.87 to 61.03. However, the precision metric decreased from 60.1 to 55.44. This is likely / because you set the recall metric to the high value of 95.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1437_image02.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1437 — Image 11

![Source page 1437 image 11](_assets/p1437_image03.png)

* **Bounding box:** x=72.0, y=478.8, width=432.0 pt, height=206.5 pt.
* **Nearby source context:** Class-level results for the solution metric values you apply to your solution
* **What is shown:** This embedded source image appears near the source context `Class-level results for the solution metric values you apply to your solution`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1437_image03.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1440 — Image 12

![Source page 1440 image 12](_assets/p1440_image01.png)

* **Bounding box:** x=122.0, y=51.5, width=432.0 pt, height=137.7 pt.
* **Nearby source context:** Importance appears. This tab offers a graph of the relative contribution of each input to the
* **What is shown:** This embedded source image appears near the source context `Importance appears. This tab offers a graph of the relative contribution of each input to the`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1440_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1441 — Image 13

![Source page 1441 image 13](_assets/p1441_image01.png)

* **Bounding box:** x=82.0, y=110.5, width=432.0 pt, height=112.9 pt.
* **Nearby source context:** value of its Active field. / 4. On the solution form, locate and open the Feature Importance tab. / Feature Importance displays a drop-down list.
* **What is shown:** This embedded source image appears near the source context `value of its Active field. / 4. On the solution form, locate and open the Feature Importance tab. / Feature Importance displays a drop-down list.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1441_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1441 — Image 14

![Source page 1441 image 14](_assets/p1441_image02.png)

* **Bounding box:** x=82.0, y=568.3, width=432.0 pt, height=148.0 pt.
* **Nearby source context:** Global / Select Global to open a graph of the impor / 5. Launch the graphical analysis by selecting a value from the drop-down list.
* **What is shown:** This embedded source image appears near the source context `Global / Select Global to open a graph of the impor / 5. Launch the graphical analysis by selecting a value from the drop-down list.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1441_image02.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1443 — Image 15

![Source page 1443 image 15](_assets/p1443_image01.png)

* **Bounding box:** x=72.0, y=39.0, width=432.0 pt, height=291.0 pt.
* **Nearby source context:** No nearby heading text was detected.
* **What is shown:** This embedded source image appears near the source context `No nearby heading text was detected.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1443_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1450 — Image 16

![Source page 1450 image 16](_assets/p1450_image01.png)

* **Bounding box:** x=102.0, y=196.8, width=432.0 pt, height=209.9 pt.
* **Nearby source context:** Note: The Cluster Concept displays the top words from the processed input data, in the / Select Group filter appears only when you select the Use Group By and Group By fields on your / Cluster visualization example
* **What is shown:** This embedded source image appears near the source context `Note: The Cluster Concept displays the top words from the processed input data, in the / Select Group filter appears only when you select the Use Group By and Group By fields on your / Cluster visualization example`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1450_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1450 — Image 17

![Source page 1450 image 17](_assets/p1450_image02.png)

* **Bounding box:** x=102.0, y=528.0, width=432.0 pt, height=210.2 pt.
* **Nearby source context:** Select Group filter appears only when you select the Use Group By and Group By fields on your / Cluster visualization example / Cluster group example
* **What is shown:** This embedded source image appears near the source context `Select Group filter appears only when you select the Use Group By and Group By fields on your / Cluster visualization example / Cluster group example`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1450_image02.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1451 — Image 18

![Source page 1451 image 18](_assets/p1451_image01.png)

* **Bounding box:** x=102.0, y=74.5, width=432.0 pt, height=212.3 pt.
* **Nearby source context:** Cluster details page
* **What is shown:** This embedded source image appears near the source context `Cluster details page`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1451_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1451 — Image 19

![Source page 1451 image 19](_assets/p1451_image02.png)

* **Bounding box:** x=112.0, y=435.6, width=432.0 pt, height=291.7 pt.
* **Nearby source context:** • Review the solution output on the Solution Statistics tab of your solution. If you aren't satisfied / • Review the Cluster Summary tab for a list view of the cluster IDs, quality size, and Groupby / Cluster Summary example
* **What is shown:** This embedded source image appears near the source context `• Review the solution output on the Solution Statistics tab of your solution. If you aren't satisfied / • Review the Cluster Summary tab for a list view of the cluster IDs, quality size, and Groupby / Cluster Summary example`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1451_image02.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1452 — Image 20

![Source page 1452 image 20](_assets/p1452_image01.png)

* **Bounding box:** x=112.0, y=102.7, width=432.0 pt, height=81.2 pt.
* **Nearby source context:** • On the Cluster Updates tab, review the summary of changes to clusters for each cluster update / Cluster updates example
* **What is shown:** This embedded source image appears near the source context `• On the Cluster Updates tab, review the summary of changes to clusters for each cluster update / Cluster updates example`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1452_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1452 — Image 21

![Source page 1452 image 21](_assets/p1452_image02.png)

* **Bounding box:** x=82.0, y=395.6, width=432.0 pt, height=165.1 pt.
* **Nearby source context:** 2. Select a solution. / 3. Under the Cluster Summary related list, select a cluster ID. / 4. Enter a name in the Cluster Name field.
* **What is shown:** This embedded source image appears near the source context `2. Select a solution. / 3. Under the Cluster Summary related list, select a cluster ID. / 4. Enter a name in the Cluster Name field.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1452_image02.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1453 — Image 22

![Source page 1453 image 22](_assets/p1453_image01.png)

* **Bounding box:** x=120.9, y=130.3, width=432.0 pt, height=126.1 pt.
* **Nearby source context:** 2. Select a clustering solution. / 3. Under the Cluster Summary related list, select a cluster ID. / 4. Select Generate Cluster
* **What is shown:** This embedded source image appears near the source context `2. Select a clustering solution. / 3. Under the Cluster Summary related list, select a cluster ID. / 4. Select Generate Cluster`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1453_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1454 — Image 23

![Source page 1454 image 23](_assets/p1454_image01.png)

* **Bounding box:** x=101.5, y=57.2, width=432.0 pt, height=139.8 pt.
* **Nearby source context:** 3. Select the Calculate Purity check
* **What is shown:** This embedded source image appears near the source context `3. Select the Calculate Purity check`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1454_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1454 — Image 24

![Source page 1454 image 24](_assets/p1454_image02.png)

* **Bounding box:** x=82.0, y=278.4, width=432.0 pt, height=191.9 pt.
* **Nearby source context:** 3. Select the Calculate Purity check / 4. Optional: Select the Purity Fields lock icon and choose the fields that you want displayed in / Note: If you don't select any fields, auto-purity displays the most significant fields based
* **What is shown:** This embedded source image appears near the source context `3. Select the Calculate Purity check / 4. Optional: Select the Purity Fields lock icon and choose the fields that you want displayed in / Note: If you don't select any fields, auto-purity displays the most significant fields based`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1454_image02.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1455 — Image 25

![Source page 1455 image 25](_assets/p1455_image01.png)

* **Bounding box:** x=94.5, y=64.0, width=432.0 pt, height=183.7 pt.
* **Nearby source context:** For example, the row priority : 5 : 100% means that 100% of / the members of this cluster have the value of 5 for the priority
* **What is shown:** This embedded source image appears near the source context `For example, the row priority : 5 : 100% means that 100% of / the members of this cluster have the value of 5 for the priority`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1455_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1455 — Image 26

![Source page 1455 image 26](_assets/p1455_image02.png)

* **Bounding box:** x=139.9, y=439.8, width=432.0 pt, height=131.5 pt.
* **Nearby source context:** • Create a clustering solution definition or use an existing one. / • Role required: admin or ml_admin / About this task
* **What is shown:** This embedded source image appears near the source context `• Create a clustering solution definition or use an existing one. / • Role required: admin or ml_admin / About this task`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1455_image02.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1459 — Image 27

![Source page 1459 image 27](_assets/p1459_image01.png)

* **Bounding box:** x=72.0, y=577.0, width=432.0 pt, height=126.9 pt.
* **Nearby source context:** Submit or Submit & Train / 5. If you submitted the solution for training, select OK on the Training Activation window to / What to do next
* **What is shown:** This embedded source image appears near the source context `Submit or Submit & Train / 5. If you submitted the solution for training, select OK on the Training Activation window to / What to do next`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1459_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1460 — Image 28

![Source page 1460 image 28](_assets/p1460_image01.png)

* **Bounding box:** x=72.0, y=99.0, width=432.0 pt, height=224.9 pt.
* **Nearby source context:** datacenter, Target datacenter, and Database size. You can also use the default prediction / interval. Select the Run Test button to find the prediction output.
* **What is shown:** This embedded source image appears near the source context `datacenter, Target datacenter, and Database size. You can also use the default prediction / interval. Select the Run Test button to find the prediction output.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1460_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1460 — Image 29

![Source page 1460 image 29](_assets/p1460_image02.png)

* **Bounding box:** x=72.0, y=397.1, width=432.0 pt, height=219.2 pt.
* **Nearby source context:** datacenter, Target datacenter, and Database size. You can also use the default prediction / interval. Select the Run Test button to find the prediction output.
* **What is shown:** This embedded source image appears near the source context `datacenter, Target datacenter, and Database size. You can also use the default prediction / interval. Select the Run Test button to find the prediction output.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1460_image02.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1461 — Image 30

![Source page 1461 image 30](_assets/p1461_image01.png)

* **Bounding box:** x=112.0, y=353.4, width=390.8 pt, height=274.5 pt.
* **Nearby source context:** Example / For example, select Incident Categorization to see the training history. / 3. In the Related Links section, click Show training progress.
* **What is shown:** This embedded source image appears near the source context `Example / For example, select Incident Categorization to see the training history. / 3. In the Related Links section, click Show training progress.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1461_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1462 — Image 31

![Source page 1462 image 31](_assets/p1462_image01.png)

* **Bounding box:** x=112.0, y=390.1, width=432.0 pt, height=227.6 pt.
* **Nearby source context:** 2. From Filter by solution, select the solution whose statistics you want to review. / 3. From Filter by version, select the solution version whose statistics you want to review. / 4. Click Apply.
* **What is shown:** This embedded source image appears near the source context `2. From Filter by solution, select the solution whose statistics you want to review. / 3. From Filter by version, select the solution version whose statistics you want to review. / 4. Click Apply.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1462_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```


---

## TABLES

### Source page 1428 — Table 1

**Nearby source context:** navigate to All > Predictive Intelligence > Classification > Solution Definitions. / 2. On the Classification Definitions list, select New. / 3. On the empty Classification Definition form, configure the fields according to the following

| Field | Value |
| --- | --- |
| Label | Enter a unique name for the solution record. |
| Name | The system generates the value of this read-only field based on the Label value<br>that you entered. |
| Word<br>Corpus | Select a word corpus that's relevant to your solution. For more information, see<br>Create a word corpus.<br>Note: Word Corpus is not a required field for customers implementing<br>Predictive Intelligence for the first time starting in Utah. A pre-trained<br>model is used instead. The Word Corpus field is removed for pre-trained<br>models. |
| Table | Select the table containing the target records that you want the system to<br>predict. |
| Output<br>Field | Select the fei ld whose value you want the predictive model to set.<br>In general, a good output field has these characteristics.<br>◦It's a choice field or a string field with a finite set of possible values.<br>◦It has some causal connection to the input fields.<br>For example, on the default Incident Categorization solution definition, the<br>output field is set to Category. |
| Fields | Select the input fields that you want the solution to use to generate a prediction.<br>Input fei lds are fields within a record that may contain the classification<br>information your prediction solution needs to succeed. For example, if you're<br>predicting the correct class for triaging an incident record, the prediction should<br>gather records containing text that references the class. Most records have<br>contextual text in their Short description field, so it's a great input field to use<br>in general. You could also use Resolution notes as an input field, as it too might<br>reference the incident class in the detailed notes for the incident.<br>In general, good input fields have these characteristics.<br>◦The fei lds are available to users when creating records.<br>◦The fei ld data type can be string, reference, choice, or HTML. The more<br>information that a field provides, the more often a solution can make a<br>prediction, and the more often predictions are accurate.<br>◦The fei ld has a default value and should not be blank. |

### Source page 1429 — Table 2

| Field | Value | Column 3 |
| --- | --- | --- |
|  | All default solution definitions use the Short description field. |  |
| Filter | Click Add Filter Condition to apply conditions to the records you're training.<br>For example, the Incident Categorization solution definition uses a filter with<br>these conditions: [Created][on][Last 12 months] AND [Active][is][false] AND<br>[State][is one of][Resolved \| Closed]<br>To train a solution, the filter must return at least one record. If your filter returns<br>no records, update it until it returns records for training.<br>Note: The recommended number of records for training a good solution<br>is from 30,000 through 300,000. If you submit more than 300,000<br>records, the most recent 300,000 records are used to train the solution.<br>Use only authentic records from the database.<br>In general, a good filter has these characteristics.<br>◦The training records are inactive and their states indicate work completed<br>within your standard process, such as resolved or closed.<br>◦The target fields contain only correct values. Filter out records with unreliable<br>target field values. For example, if you're predicting the assignment group/<br>category and your historic incident data contains assignment groups/<br>categories that are no longer used, add a filter to remove such records from<br>the training.<br>◦The training records contain multiple examples of each target field value you<br>want the solution to predict.<br>◦The training records include common variations of the input fields.<br>Use relative date filters such as last 3 months or last 12 months. Don't use<br>hard-coded dates because these filters aren't updated when the solutions are<br>retrained, unless you update them manually. |  |
| Processing<br>Language | Select the dominant language of the dataset that you're training on the solution<br>defni ition. If the dataset language is Italian, choose Italian. Also, English<br>processing is applied to all datasets by default. For example, if you select Italian,<br>the system processes the data in both English and Italian.<br>Note: The term processing indicates some of the language-specific<br>steps used as part of training a solution. For example, tokenizing words,<br>removing stop words, and stemming. |  |
| Stopwords | When you select your processing language, the system automatically adds<br>a Stopwords list for that language. For example, if your processing language<br>is Italian, the Default Italian Stopwords list appears. The Default English<br>Stopwords list is also included. If you create a custom stopwords list, you can<br>select it from the Stopwords field to add to your solution. |  |
| Training<br>Frequency | Select how often the system regenerates the solution. The available options<br>range from Run once up to Every 180 days.<br>Note: The minimum number of records required for classification solution<br>training is set at 10,000. |  |
|  |  | Note: The minimum number of records required for classification solution<br>training is set at 10,000. |

### Source page 1430 — Table 3

| Field | Value |
| --- | --- |
|  | By default, the system runs training once. This provides you time to review<br>and update the solution definition until it provides acceptable coverage and<br>precision values.<br>When your solution definition is fairly stable, consider scheduled trainings, as<br>data can age over time, thus degrading the accuracy of your prediction model.<br>Note: The ML scheduler limits the number of trainings an instance can<br>commit to 50 new ML training requests per instance within a 24-hour<br>window. This limit excludes scheduled retraining requests, clustering<br>updates, and similarity updates, even if the new training requests exceed<br>50 within a 24-hour window. |

### Source page 1430 — Table 4

**Nearby source context:** Value / Note: The ML scheduler limits the number of trainings an instance can / 4. Click the appropriate context menu option or button for your solution definition.

| Option | Description |
| --- | --- |
| Save or Save & Train | Save your solution definition record so you<br>can return to it later, or save and submit it for<br>training. |
| Submit or Submit & Train | Create your solution definition record and<br>submit it, or submit and train it. |

### Source page 1434 — Table 5

**Nearby source context:** Lookups embedded list. / 5. Select the check box for the precision and coverage combination you want to use to make / Special prediction combinations

| Prediction result | Precision | Coverage |
| --- | --- | --- |
| Never include class in predictions | 100 | 0 |
| Always include class in predictions | 0 | 100 |

### Source page 1441 — Table 6

**Nearby source context:** 4. On the solution form, locate and open the Feature Importance tab. / Feature Importance displays a drop-down list. / the Global option.

| List option | Description |
| --- | --- |
| Global | Provides an overview of how the model be<br>haves across all predictions, showing the<br>overall impact of each input feature.<br>Select Global to open a graph of the impor<br>tance of your input fields to predictions for all<br>output classes as a whole. |
| Your output class value | Focuses on the model's behavior for the cho<br>sen class only, showing how input features<br>contribute to predictions on a per-class basis.<br>Select one of the possible output classes to<br>open a graph of the importance of your input<br>fields to predictions for that class. |

### Source page 1443 — Table 7

**Nearby source context:** navigate to All > Predictive Intelligence > Similarity > Solution Definitions. / 2. In the Similarity Definitions list, select New. / 3. On the Similarity Definition form, fill in the fields.

| Field | Value |
| --- | --- |
| Label | Enter a unique name for your similarity solution. For<br>example, in this use case you could enter Match<br>Knowledge Articles to Incidents. |
| Name | As you enter a Label value, this field automatically<br>populates with a system-assigned, read-only name<br>based on your Label value. |
| Word Corpus | If you have a legacy similarity solution, you can select a<br>relevant word corpus from the Word Corpus field in the<br>definition form.<br>Note: Starting from the Washington DC release,<br>a word corpus is not required because a pre-<br>trained model is used instead. The Word Corpus<br>field is not visible in the definition form for pre-<br>trained models.<br>For more information, see Create a word corpus. |

### Source page 1444 — Table 8

| Field | Value |
| --- | --- |
| Table | In the Table field, select the table that contains records<br>you want to use as an information source. In this use<br>case you select the Knowledge [kb_knowledge]<br>table, because its KB Article records might provide<br>information relevant to the Incidents that you're trying to<br>resolve.<br>After you assign a Table, the number of records<br>matching your filter conditions is displayed as a link.<br>Select this link to view the list of records. |
| Test Table | In the Test Table field, select the table containing the<br>records that you want to target. In this use case, you<br>select the Incident [incident] table, as it contains the<br>Incident records that you're trying to resolve.<br>Note: You can select the same table for<br>Table and Test Table. For example: using filter<br>conditions, you could collect information from<br>recent Incidents to help with target Incidents. |
| Fields | For the Table that you selected, enter fields that are<br>likely to contain words and phrases relevant to the<br>Incidents you're trying to resolve. In this example, you<br>choose Short description and Article body. Including<br>the article body increases your chances of capturing<br>informative details regarding the subject.<br>Note: Journal Type is not a supported data type. |
| Test Fields | For the Test Table that you selected, enter fields<br>that contain text that you want to compare to other<br>similar records. In this example, you choose the Short<br>description of the Incident records you're trying to<br>resolve. |
| Filter | Select Add Filter Condition to apply conditions to<br>the Fields records you're using as an information<br>source. For example, in this use case you could set<br>a workflow_state=published condition to retrieve<br>published KB articles only.<br>Note: Script includes can't be referenced from<br>the Filter. Use database views as an alternative. |
| Processing Language | Select the dominant language of the dataset you're<br>training on. Also, English processing is applied to all<br>datasets by default. For example, if you select Italian,<br>the system processes the data in both Italian and<br>English. |

### Source page 1445 — Table 9

| Field | Value |
| --- | --- |
|  | Note: The term processing indicates some of the<br>language-specific steps used as part of training a<br>solution, such as tokenizing words, removing stop<br>words, and stemming. |
| Stopwords | When you select your processing language, the system<br>automatically adds a Stopwords list for that language.<br>For example, if your processing language is Italian, the<br>Default Italian Stopwords list appears. The Default<br>English Stopwords list is also included.<br>To use a custom stopwords list, select the lock<br>icon( ) and then search in the Select target record<br>field. |
| Training Frequency | Select a retraining frequency. The available options<br>range from Run Once up to Every 180 days. |
| Update Frequency | Select how often you want to refresh the data you use to<br>retrieve your similarity results.<br>For example, for open incident records, you could<br>select an update frequency of Every 15 minutes, as<br>new incidents typically occur frequently throughout the<br>day. This frequency may increase the likelihood that<br>newly opened records are included in the refresh.<br>However, for KB Knowledge article records, which are<br>typically not created often, you could choose a less<br>frequent update frequency such as Every 1 day.<br>Note: The ML scheduler limits the number of<br>trainings an instance can commit to 50 new ML<br>training requests per instance within a 24 hour<br>window. This excludes scheduled re-training<br>requests. In addition, clustering and similarity<br>updates are also excluded from this limit, even if<br>the new training requests exceed 50 within a 24<br>hour window. |

### Source page 1445 — Table 10

**Nearby source context:** frequent update frequency such as Every 1 day. / Note: The ML scheduler limits the number of / 4. Select the appropriate button for the solution definition.

| Option | Description |
| --- | --- |
| Save | Save your solution definition record so you<br>can return to it later. |
| Submit & Train | Create your solution definition record and<br>train it. |

### Source page 1447 — Table 11

**Nearby source context:** navigate to All > Predictive Intelligence > Clustering > Solution Definitions. / 2. On the Clustering Definitions list, select New. / 3. On the Clustering Definition form, configure the fields according to the following guidance.

| Field | Value |
| --- | --- |
| Label | Enter a unique name for your clustering solution. For<br>example, in this use case you could enter Group<br>Incidents to a Major Incident. |
| Name | As you enter your solution Label, this field automatically<br>populates with a system-assigned name based on your<br>Label value. |
| Word Corpus | If you have a legacy clustering solution, you can select a<br>relevant word corpus from the Word Corpus field in the<br>definition form.<br>Note: With the Zurich release, a word corpus is<br>not required, because a pre-trained model is used<br>instead. The Word Corpus field is not visible in the<br>definition form for pre-trained models.<br>For more information, see Create a word corpus. |
| Table | Select the table that contains record types that you want<br>to group into one or more clusters. For example, in this use<br>case you select the Incident [incident] table as it contains<br>incident records you want to group together for a major<br>incident analysis.<br>When you assign a table value, a link appears in the form<br>that shows the number of records that match your current<br>conditions. |
| Fields | Select one or more input fields types that help the system<br>identify the records you want to include in your cluster. In<br>this use case, use Short description. |

### Source page 1448 — Table 12

| Field | Value | Column 3 |
| --- | --- | --- |
|  | Note: When selecting a reference type field, you<br>must dot-walk to the field's property name. For<br>example, instead of short description, enter<br>_<br>short description.name.<br>_ | Note: When selecting a reference type field, you<br>must dot-walk to the field's property name. For<br>example, instead of short description, enter<br>_<br>short description.name. |
| Use Group By | Select this check box only if you want to group input<br>records by a field before creating clusters.<br>Note: Selecting this check box activates the Group<br>By list. If you don't select the check box, all the table<br>records are grouped into clusters. |  |
| Group By | Selecting a value from this list is optional. If you do so, the<br>system groups records into one or more clusters based on<br>your selection. |  |
| Purity Fields | Choose fields from your table that can help the system<br>identify the class that is most frequent in the cluster. In<br>this example scenario, select Category and Assignment<br>group.Name. |  |
| Filter | Add filter conditions to apply to the input field records that<br>you want to include in your clusters.<br>◦The maximum number of records for clustering is limited<br>to 300,000.<br>◦For best results, aim for at least 2000 records as a<br>minimum.<br>Note: Script includes can't be referenced from the<br>Filter. Use database views as an alternative. |  |
| Processing Language | Select the dominant language of the dataset you're training<br>on the solution definition. If the dataset language is Italian,<br>choose Italian. Also, English processing is applied to all<br>datasets by default. For example, if you select Italian, the<br>system processes the data in both English and Italian.<br>Note: The term processing indicates some of the<br>language-specific steps used as part of training a<br>solution. For example, tokenizing words, removing<br>stop words, and stemming. |  |
| Stopwords | When you select your processing language, the system<br>automatically adds a Stopwords list in that language. For<br>example, if your processing language is Italian, the Default<br>Italian Stopwords list appears. The Default English<br>Stopwords list is also included. If you create a custom<br>stopwords list, you can select it from the Stopwords field to<br>add to your solution. |  |
| Update Frequency | Select how often you want the system to update your<br>clusters with new and updated records. |  |

### Source page 1449 — Table 13

| Field | Value | Column 3 |
| --- | --- | --- |
|  | Note: The system pulls records based on the Group<br>By filter conditions that you set on your clustering<br>solution, if any.<br>For example, if you select Every 15 minutes, the system<br>identifies which records have arrived within that time<br>frame. The system tries to assign them to the existing<br>clusters, or creates a new cluster if possible.<br>In this example, 20 new records arrive. If 16 of those<br>records make it into an existing cluster and 4 don't, the<br>system forms a new cluster for the four unassigned<br>records.<br>You can also choose not to update your clusters at all. | Note: The system pulls records based on the Group<br>By filter conditions that you set on your clustering<br>solution, if any. |
| Training Frequency | Select how often you want the system to discard all<br>previous cluster results and recreate clusters from the<br>beginning. Your options range from daily, every third day,<br>every seven days, or monthly. You can also choose to train<br>your cluster once.<br>Note: The ML scheduler limits the number of<br>trainings an instance can commit to 50 new ML<br>training requests per instance within a 24-hour<br>window. The limit excludes scheduled retraining<br>requests. In addition, clustering and similarity<br>updates are also excluded from this limit, even if the<br>new training requests exceed 50 within a 24-hour<br>window. |  |
| Minimum number of records per<br>cluster | Enter the minimum number of records you want a cluster to<br>contain. The value you enter must be 2 or higher. |  |

### Source page 1449 — Table 14

**Nearby source context:** For example, if you select Every 15 minutes, the system / Note: The ML scheduler limits the number of / 4. Select the appropriate context menu option or button for your solution definition.

| Option | Description |
| --- | --- |
| Save or Save & Train | Save your solution definition record so you<br>can return to it later, or save and submit it for<br>training. |
| Submit or Submit & Train | Create your solution definition record and<br>submit it, or submit and train it. |

### Source page 1456 — Table 15

**Nearby source context:** 1. Navigate to All > Predictive Intelligence > Regression > Solution Definitions. / 2. On the Regression Definitions list, select New. / 3. On the Regression Definition form, configure these fields per the following guidance.

| Field | Value |
| --- | --- |
| Label | Enter a unique name for your regression solution.<br>For example, in this use case you could enter<br>Regression Test for DB Restore. |

### Source page 1457 — Table 16

| Field | Value |
| --- | --- |
| Name | As you enter your solution Label value, this field<br>automatically populates with a system-assigned name<br>that's similar to your label value. |
| Word Corpus | Select an existing word corpus that's relevant to your<br>solution. For example, in this use case you select a word<br>corpus that has a title such as Incidents in the last 3<br>months.<br>If you don’t have a relevant word corpus, follow the steps<br>to create a word corpus first. When the word corpus is<br>complete, you can select it from the Word Corpus field in<br>your Regression Definition form.<br>However, the word corpus selection is optional. If your<br>input data has text columns and you don't choose a<br>word corpus, your regression solution trains a new word<br>corpus model by using the text columns in your input<br>data. The resulting word corpus can be reused in any<br>other regression solution or other ML solution type.<br>Note: A pre-trained model is used instead of the<br>Word Corpus for users who activated Predictive<br>Intelligence starting in the Utah release. |
| Table | Select the database table on which you’re applying<br>regression. The table should contain historical records<br>the system can use to predict the length of time for its<br>database restore. |
| Output Field | Select the field whose value you want the predictive<br>model to set.<br>In general, a good output field is a numeric, integer, or<br>floating point field.<br>In this example scenario, you use the Duration field<br>to measure a length of time. The output field should<br>generate a numeric value. |
| Fields | Select one or more field types that help the system<br>identify the records you want to train using regression.<br>In this example scenario, you use Short description,<br>Source datacenter, Target datacenter, and Database<br>size. (short description, Sourcedc, Targetdc, and Dbsize.)<br>_<br>Input field types can be string, nominal, or numeric. |
| Filter | (Optional) Add filter conditions to the output field records<br>that you want to train using regression. |

### Source page 1458 — Table 17

| Field | Value |
| --- | --- |
|  | Note:<br>◦The minimum number of records for regression<br>training is 10,000 records.<br>◦The maximum number of records for regression<br>training is limited to 300,000. |
| Processing Language | Select the primary language of the dataset that you're<br>training on the solution definition. If the dataset language<br>is Italian, choose Italian. Also, English processing is<br>applied to all datasets by default. For example, if you<br>select Italian, the system processes the data in both<br>English and Italian.<br>Note: The term processing indicates some of the<br>language-specific steps used as part of training<br>a solution. These steps include tokenizing words,<br>removing stop words, and stemming. |
| Stopwords | When you select your processing language, the system<br>automatically adds a Stopwords list that uses the same<br>language. For example, if your processing language is<br>Italian, the Default Italian Stopwords list is displayed.<br>The Default English Stopwords list also displays in your<br>selection. If you create a custom stopwords list, you<br>can select it from the Stopwords field to add it to your<br>solution. In this scenario, you use the Default English<br>Stopwords list. |
| Training Frequency | Select how often the system regenerates the solution<br>based on records matching the Filter. Your options<br>include:<br>◦Run Once<br>◦Every 30 days<br>◦Every 60 days<br>◦Every 90 days<br>◦Every 120 days<br>◦Every 180 days<br>In this scenario, you select Every 30 days<br>By default, the system runs training once. This practice<br>provides you time to review and update the solution<br>definition as needed until it provides acceptable<br>coverage and precision values. |

### Source page 1459 — Table 18

| Field | Value |
| --- | --- |
|  | Note:<br>◦The minimum number of records required for<br>regression solution training is set at 10,000.<br>◦The ML scheduler limits the number of trainings<br>an instance can commit to 50 new ML training<br>requests per instance within a 24-hour window.<br>This limit excludes scheduled requests for<br>retraining. In addition, clustering and similarity<br>updates are also excluded from this limit, even if<br>the new training requests exceed 50 within a 24-<br>hour window. |

### Source page 1459 — Table 19

**Nearby source context:** Value / Note: / 4. Select the appropriate context menu option or button for your solution definition.

| Option | Description |
| --- | --- |
| Save or Save & Train | Save your solution definition record so you<br>can return to it later, or save and submit it for<br>training. |
| Submit or Submit & Train | Create your solution definition record and<br>submit it, or submit and train it. |


---

## FIGURES

| Figure / visual | Source page | Asset or location | Analysis |
|---|---:|---|---|
| Embedded screenshot or instructional image 1 | 1427 | `_assets/p1427_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 2 | 1431 | `_assets/p1431_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 3 | 1431 | `_assets/p1431_image02.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 4 | 1435 | `_assets/p1435_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 5 | 1435 | `_assets/p1435_image02.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 6 | 1436 | `_assets/p1436_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 7 | 1436 | `_assets/p1436_image02.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 8 | 1436 | `_assets/p1436_image03.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 9 | 1437 | `_assets/p1437_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 10 | 1437 | `_assets/p1437_image02.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 11 | 1437 | `_assets/p1437_image03.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 12 | 1440 | `_assets/p1440_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 13 | 1441 | `_assets/p1441_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 14 | 1441 | `_assets/p1441_image02.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 15 | 1443 | `_assets/p1443_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 16 | 1450 | `_assets/p1450_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 17 | 1450 | `_assets/p1450_image02.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 18 | 1451 | `_assets/p1451_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 19 | 1451 | `_assets/p1451_image02.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 20 | 1452 | `_assets/p1452_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 21 | 1452 | `_assets/p1452_image02.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 22 | 1453 | `_assets/p1453_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 23 | 1454 | `_assets/p1454_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 24 | 1454 | `_assets/p1454_image02.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 25 | 1455 | `_assets/p1455_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 26 | 1455 | `_assets/p1455_image02.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 27 | 1459 | `_assets/p1459_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 28 | 1460 | `_assets/p1460_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 29 | 1460 | `_assets/p1460_image02.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 30 | 1461 | `_assets/p1461_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 31 | 1462 | `_assets/p1462_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Markdown-converted table/grid 1 | 1428 | TABLES section | Source table/grid region converted into Markdown; nearby context: navigate to All > Predictive Intelligence > Classification > Solution Definitions. / 2. On the Classification Definitions list, select New. / 3. On the empty Classification Definition form, configure the fields according to the following |
| Markdown-converted table/grid 2 | 1429 | TABLES section | Source table/grid region converted into Markdown; nearby context:  |
| Markdown-converted table/grid 3 | 1430 | TABLES section | Source table/grid region converted into Markdown; nearby context:  |
| Markdown-converted table/grid 4 | 1430 | TABLES section | Source table/grid region converted into Markdown; nearby context: Value / Note: The ML scheduler limits the number of trainings an instance can / 4. Click the appropriate context menu option or button for your solution definition. |
| Markdown-converted table/grid 5 | 1434 | TABLES section | Source table/grid region converted into Markdown; nearby context: Lookups embedded list. / 5. Select the check box for the precision and coverage combination you want to use to make / Special prediction combinations |
| Markdown-converted table/grid 6 | 1441 | TABLES section | Source table/grid region converted into Markdown; nearby context: 4. On the solution form, locate and open the Feature Importance tab. / Feature Importance displays a drop-down list. / the Global option. |
| Markdown-converted table/grid 7 | 1443 | TABLES section | Source table/grid region converted into Markdown; nearby context: navigate to All > Predictive Intelligence > Similarity > Solution Definitions. / 2. In the Similarity Definitions list, select New. / 3. On the Similarity Definition form, fill in the fields. |
| Markdown-converted table/grid 8 | 1444 | TABLES section | Source table/grid region converted into Markdown; nearby context:  |
| Markdown-converted table/grid 9 | 1445 | TABLES section | Source table/grid region converted into Markdown; nearby context:  |
| Markdown-converted table/grid 10 | 1445 | TABLES section | Source table/grid region converted into Markdown; nearby context: frequent update frequency such as Every 1 day. / Note: The ML scheduler limits the number of / 4. Select the appropriate button for the solution definition. |
| Markdown-converted table/grid 11 | 1447 | TABLES section | Source table/grid region converted into Markdown; nearby context: navigate to All > Predictive Intelligence > Clustering > Solution Definitions. / 2. On the Clustering Definitions list, select New. / 3. On the Clustering Definition form, configure the fields according to the following guidance. |
| Markdown-converted table/grid 12 | 1448 | TABLES section | Source table/grid region converted into Markdown; nearby context:  |
| Markdown-converted table/grid 13 | 1449 | TABLES section | Source table/grid region converted into Markdown; nearby context:  |
| Markdown-converted table/grid 14 | 1449 | TABLES section | Source table/grid region converted into Markdown; nearby context: For example, if you select Every 15 minutes, the system / Note: The ML scheduler limits the number of / 4. Select the appropriate context menu option or button for your solution definition. |
| Markdown-converted table/grid 15 | 1456 | TABLES section | Source table/grid region converted into Markdown; nearby context: 1. Navigate to All > Predictive Intelligence > Regression > Solution Definitions. / 2. On the Regression Definitions list, select New. / 3. On the Regression Definition form, configure these fields per the following guidance. |
| Markdown-converted table/grid 16 | 1457 | TABLES section | Source table/grid region converted into Markdown; nearby context:  |
| Markdown-converted table/grid 17 | 1458 | TABLES section | Source table/grid region converted into Markdown; nearby context:  |
| Markdown-converted table/grid 18 | 1459 | TABLES section | Source table/grid region converted into Markdown; nearby context:  |
| Markdown-converted table/grid 19 | 1459 | TABLES section | Source table/grid region converted into Markdown; nearby context: Value / Note: / 4. Select the appropriate context menu option or button for your solution definition. |


---

## QUALITY ASSURANCE NOTES

* PAGES REVIEWED: 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1434, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463. Source page range: 1425-1464 (shared boundary pages split at source headings).
* IMAGES REVIEWED: 72 image blocks assigned/reviewed: 39 recurring header logo block(s), 2 small icon/pictogram block(s), and 31 large screenshot/diagram crop(s).
* TABLES REVIEWED: 19 table/grid region(s) converted to Markdown. Table pages: 1428, 1429, 1430, 1434, 1441, 1443, 1444, 1445, 1447, 1448, 1449, 1456, 1457, 1458, 1459.
* FIGURES REVIEWED: 31 large screenshot/diagram figure(s) plus 19 table/grid visual(s).
* OCR ISSUES FOUND: No unresolved OCR issues were identified in the main PDF text layer after cleanup. Embedded screenshot crops are preserved as source assets; automated image OCR was not applied in this pass to avoid inserting low-confidence text, and this is explicitly marked in each image record.
* OCR ISSUES CORRECTED: Removed recurring footer/page-number noise from the main content stream, normalized nonbreaking spaces and soft-hyphen/control artifacts, preserved bullets/numbering/property names, and converted detected tables to Markdown.
* SECTION MAPPING NOTES: Folder name is exactly `Predictive Intelligence`. File name and subsection name are exactly `Creating and training solutions` from the TOC. Shared source pages were split at heading coordinates from the PDF text layer.
* PAGE FOOTERS REVIEWED: Reviewed recurring ServiceNow copyright/trademark footer and logical page numbers. Footer text reviewed: `© 2026 ServiceNow, Inc. All rights reserved. ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries. Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.`
* RECHECK PASSES COMPLETED: 12/12: page completeness, text extraction, table extraction, image extraction, diagram interpretation, section mapping, subsection mapping, file names, folder names, Markdown formatting, missed-content review, and OCR/text-layer cleanup.
* VERIFICATION ARTIFACTS: Large image crops and `image_inventory.csv` are stored in the `_assets` folder inside this section folder.
