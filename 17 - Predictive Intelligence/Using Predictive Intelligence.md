# Using Predictive Intelligence

## SOURCE INFORMATION

* SECTION NAME: Predictive Intelligence
* SUBSECTION NAME: Using Predictive Intelligence
* SOURCE FILE NAME: Predictive Intelligence.pdf
* PAGE RANGE: 1464-1487 (shared boundary pages split at source headings)
* EXTRACTION DATE: 2026-06-17

---

# CONTENT

> Source page: 1464

### Using Predictive Intelligence

Train and use Predictive Intelligence solutions to accomplish various tasks and that integrate
with other ServiceNow products, such as Document Intelligence and Task Intelligence.

#### Overview of Predictive Intelligence

Predictive Intelligence is the interface by which you can train models on the ServiceNow AI
Platform. These models enable you to predict, estimate, and identify patterns that can be used to
route work, populate form fields, estimate wait times, and more.
• Show suggestions for relevant articles.
• Assign, categorize, and prioritize tasks.
• Detect major incidents.
• Recommend case resolutions.
• Prevent duplicate articles and ideas.
• Detect phishing attempts.
For more information about the different types of solutions available, see Explore Predictive
Intelligence.

#### Training your ML solutions

Predictive Intelligence enables you to train predictive models and machine-learning solutions
that you can apply using data on your instances. The solutions you create use the frameworks to
predict, recommend, and organize data. To get started, see Creating and training solutions.
You can also extend Predictive Intelligence to other processes and applications, such as:
• Incident categorization: Predicts the incident category based on the short description. See
Predictive Intelligence for Incident Management
.
• CSM case assignment: Predicts the case record assignment group based on the short
description. See Predictive Intelligence for case management
.
For more information, see ServiceNow apps and features that use Predictive Intelligence.

#### Testing and monitoring predictions

After creating and training your solutions, call on the Predictive Intelligence API to make a
solution prediction. Use the results to gauge the performance of the solution and make changes
as needed.
You can track the coverage and precision of deployed predictive models using the Solution
Statistics dashboard, which provides reporting on these prediction areas by default.

#### Report

#### Description

Average Prediction Coverage (last 30 days)
The percentage of predictions that yielded an
outcome out of the total number of predictions
attempted. Click the coverage score to see a
breakdown by class.
Daily Prediction Coverage
The percentage of records created on a given
day in which the solution was able to predict
an outcome.

> Source page: 1465

#### Report

#### Description

Average Prediction Precision (last 30 days)
The percentage of predictions in which the
predicted value was the same as the final
value of the field when the record closed. Click
the precision score to see a breakdown by
class.
Daily Prediction Precision
The percentage of records closed on a given
day in which the predicted field value was the
same as the final value.
For more information, see Testing and monitoring predictions.

#### Preparing your instance

For you to get the most out of Predictive Intelligence, you will want to prepare. You don't need to
write code or do calculations, but deciding what you hope to do with the solution definitions will
make implementation easier.
• Identify the problems that you want to solve with Predictive Intelligence.
• Have 30,000–300,000 high-quality records from which Predictive Intelligence can learn.
• Set your expectations.

#### Note: Inconsistencies or gaps in training data can cause incorrect or unreliable

predictions.

#### Implementation Process

Predictive Intelligence takes approximately 14 days to implement on a production instance.
• Day 1: Clone production instance over to a non-production instance.
• Days 2–10: Create a solution definition, train it on historical records, and validate that the
solution works as desired on the non-production instance.
• Days 11–13: Create import and update sets to move the solution to production, train and
validate on the new instance, and set the retraining frequency.
• Day 14 and on: Monitor the solution.
In general, non-production environments are where workflows can be tested and formatted
before being moved over to the production instance to further train models and test predictions.
For more information about getting started with Predictive Intelligence, see our guide on how to
get started with Predictive Intelligence.

#### Using Machine Learning APIs

Use ServiceNow Machine Learning (ML) APIs to train Machine Learning models and run
inferences.
ML APIs enable training solutions and managing solution versions. You can get and set active
versions, monitor training status, and more. The ML API also provides encoders, which enable
using term frequency–inverse document frequency (TF-IDF) as a word corpus. Predictability
estimates enable assessing the predictive value of table columns.

> Source page: 1466

#### Note: Predictive Intelligence APIs run with full privileges before the Vancouver Patch 7

Hotfix 2b and Washington DC Patch 7 releases. With later releases, grant access using
ACLs. For more information see Query ACLs
.

#### ML API class overview

This section briefly describes classes for training ML solutions and running inferences with
trained solutions.

#### Datasets

A dataset is a set of records including a table name, columns, and row selection
criteria to use as input for ML training algorithms. Datasets don't contain the actual
data.
For more information, see DatasetDefinition
.

#### ML objects – Solutions, Encoders, and Estimates

ML objects define a specific training configuration to apply on a dataset. Some
operations are common across ML objects. Solution objects include classification,
clustering, regression, and similarity.
Encoders are text processing objects that are either pre-trained or trained based on
the language datasets you provide. You can train encoders that determine how the
system interprets and processes text fields. For ML solutions that include text, you
can train an encoder to specify how to process text and use the trained encoder in a
solution.
PredictabilityEstimate objects estimate which fields in a dataset are predictable and
the features on which this predictability is based.
For more information, see:
• ClassificationSolution
• ClusteringSolution
• Encoder
• PredictabilityEstimate
• RegressionSolution
• SimilaritySolution

#### Stores

ML objects are maintained in a specific store for each object type. Each store class
includes methods for add, get, update, and delete operations.
For more information, see:
• ClassificationSolutionStore
• ClusteringSolutionStore
• EncoderStore
• PredictabilityEstimateStore
• RegressionSolutionStore
• SimilaritySolutionStore

> Source page: 1467

#### Versions

Each trained object results in a new version that you can run tasks on. Use the
version API to get any solution version and run tasks on it.
For more information, see:
• ClassificationSolutionVersion
• ClusteringSolutionVersion
• EncoderVersion
• PredictabilityEstimateVersion
• RegressionSolutionVersion
• SimilaritySolutionVersion

#### Putting it together: ML API flows

You can use the following flow to configure and train solutions, encoders, and predictability
estimates:
1. Define a dataset (DatasetDefinition)
2. Create an ML object (Solution/Encoder/PredictabilityEstimate)
3. Add to store (Store)
4. Train (Solution/Encoder/PredictabilityEstimate)

#### Note: The encoder definitions support multiple dataset definitions, but have the same

training flow.
To train a solution with an encoder, create the encoder first, then include the encoder in the
solution configuration.
1. Create an encoder (Encoder)
2. Define a dataset (DatasetDefinition)
3. Create solution specifying encoder (Solution)
4. Add to store (SolutionStore)
5. Train (Solution)
ML object encoder requirements:
• Required in similarity API solutions.
• Required in clustering API solutions, unless using the Levenshtein distance algorithm, in which
case encoders are optional.
• Optional for classification and regression solutions.
• Unavailable for predictability estimates.

#### Getting started with ML API solution training

Follow this example procedure to learn how to configure and train a solution.

#### Configure and train a solution

> Source page: 1468

1. Define a dataset using the DatasetDefinition
API.
var myData = new sn_ml.DatasetDefinition({
'tableName' : 'incident',
'fieldNames' : ['assignment_group',
'short_description', 'description'],
'encodedQuery' : 'activeANYTHING'
});
2. Use the constructor to define the solution, including the dataset in the
configuration.
var mySolution = new sn_ml.ClassificationSolution({
'label': "my solution definition",
'dataset' : myData,
'predictedFieldName' : 'assignment_group',
'inputFieldNames':['short_description']
});
  ◦ClassificationSolution()
  ◦ClusteringSolution()
  ◦Encoder()
  ◦PredictabilityEstimate()
  ◦RegressionSolution()
  ◦SimilaritySolution()
3. Add the solution definition to the store using the add() method.
var my_unique_name =
sn_ml.ClassificationSolutionStore.add(mySolution);
  ◦ClassificationSolutionStore - add()
  ◦ClusteringSolutionStore – add()
  ◦EncoderStore - add()
  ◦PredictabilityEstimateStore - add()
  ◦RegressionSolutionStore - add()
  ◦SimilaritySolutionStore - add()
4. Train the solution using the submitTrainingJob() method. After training is
complete, you can manage the trained solution using a solution version API. A
solution can be retrained multiple times. Each training results in a new solution
"version" on which you can run inferences.
var myClassifierVersion =
mySolution.submitTrainingJob();

> Source page: 1469

  ◦ClassificationSolution - submitTrainingJob()
  ◦ClusteringSolutionVersion – submitTrainingJob()
  ◦Encoder - submitTrainingJob()
  ◦PredictabilityEstimate - submitTrainingJob()
  ◦RegressionSolution - submitTrainingJob()
  ◦SimilaritySolution - submitTrainingJob()

#### View all classification solutions in a store

You can use the store getAllNames() method to see a list of all solutions that
have been added to the store.
gs.print(JSON.stringify(JSON.parse(sn_ml.Classification
SolutionStore.getAllNames()), null, 2));
In the output, the system has named the solution
ml_x_snc_global_global_my_solution_definition. Use this name in
subsequent examples to get version information.
*** Script: [
"ml_incident_assignment",
"ml_x_snc_global_global_my_solution_definition",
"ml_incident_categorization"
]
• ClassificationSolutionStore - getAllNames()
• ClusteringSolutionStore – getAllNames()
• EncoderStore - getAllNames()
• PredictabilityEstimateStore - getAllNames()
• RegressionSolutionStore - getAllNames()
• SimilaritySolutionStore - getAllNames()

#### Getting started with ML API solution versions

Follow these example breakdowns to learn how to manage trained solution versions.

#### Check training status

Get the classification solution from the store, choose a version, and check its
training status. The methods used for checking training status are applicable to all
ML object types.
1. Get the solution from the classification solution store using the get() method.
// Get the solution created in the previous example
from the classification solution store
var mlSolution =
sn_ml.ClassificationSolutionStore.get('ml_x_snc_globa
l_global_my_solution_definition');
  ◦ClassificationSolutionStore - get()
  ◦ClusteringSolutionStore – get()

> Source page: 1470

  ◦EncoderStore - get()
  ◦PredictabilityEstimateStore - get()
  ◦RegressionSolutionStore - get()
  ◦SimilaritySolutionStore - get()
2. Access the most recent solution version using the getLatestVersion()
solution method and get its training status using the getStatus() version
method.
// Access the latest version of the solution and print
its training status
gs.print(JSON.stringify(JSON.parse(mlSolution.getLates
tVersion().getStatus(), null, 2)));
Output when training is complete:
*** Script:
{"state":"solution_complete","percentComplete":"100",
"hasJobEnded":"true"}

#### getLatestVersion()

#### getStatus()

ClassificationSolution -
ClassificationSolutionVersion
getLatestVersion()
- getStatus()
ClusteringSolution –
ClusteringSolutionVersion
getLatestVersion()
– getStatus()
Encoder -
EncoderVersion -
getLatestVersion()
getStatus()
PredictabilityEstimate -
PredictabilityEstimateVersion
getLatestVersion()
- getStatus()
RegressionSolution -
RegressionSolutionVersion
getLatestVersion()
- getStatus()
SimilaritySolution -
SimilaritySolutionVersion
getLatestVersion()
- getStatus()

#### Get predictions using a solution version

After the solution has been trained, get the trained version and run a prediction on
it. Get the solution you created from the store. Next, choose the trained version and
predict the trained version.

#### Note: Predictions cannot be made on encoders and predictability estimates.

1. Get the solution from the classification solution store using the get() method.
// Get the solution created in the first example from
the classification solution store
var mlSolution =
sn_ml.ClassificationSolutionStore.get('ml_x_snc_globa
l_global_my_solution_definition');

> Source page: 1471

2. Use the GlideRecord
API get() method to provide a record from the Incident
[incident] table.
// single GlideRecord input
var input = new GlideRecord("incident");
input.get("<sys_id>");
3. Optional. Configure the ClassificationSolutionVersion –
predict() method options parameter to return the top three results and
return all results.
// configure optional parameters
var options = {};
options.top_n = 3;
options.apply_threshold = false;
4. Declare a variable called results and assign it to the prediction job.
To run the prediction job, get the most recent solution version using the
ClassificationSolution – getLatestVersion() method and call
the ClassificationSolutionVersion – predict() method on it.
var results =
mlSolution.getLatestVersion().predict(input,
options);
  ◦ClassificationSolutionVersion - predict()
  ◦ClusteringSolutionVersion – predict()
  ◦RegressionSolutionVersion - predict()
  ◦SimilaritySolutionVersion - predict()
5. Print the predicted results output.
gs.print(JSON.stringify(JSON.parse(results), null,
2));
Predicted results example output:
*** Script: {
"<sys_id>": [
{
"confidence": 99,
"threshold": 24.75,
"predictedValue": "Email",
"predictedSysId": ""
},
{
"confidence": 5.88210244009169,
"threshold": 100,
"predictedValue": "Email (I/f)",
"predictedSysId": ""
},
{
"confidence": 2.3461203499840932,
"threshold": 14.81,
"predictedValue": "Authentication",

> Source page: 1472

"predictedSysId": ""
}
]
}

#### Reviewing your ML solution training jobs

Use the ML Solutions (ML Training Jobs view) module to monitor the training status and progress
for Predictive Intelligence solutions. The module displays training jobs for both user interface and
API solutions.

#### Background and usage

When you submit an ML solution or ML solution definition for training, it goes to a ServiceNow
data center for processing to predict and deliver a data outcome. Depending on the solution size,
the training can take hours or sometimes days to complete. The ML Training Jobs view helps you
stay on top of all in-progress and completed ML solution training jobs in your instance.
To access this view, you use the admin or ml_admin role and the following navigation path:
Predictive Intelligence > Training Jobs.

#### Note: The ML scheduler limits the number of trainings an instance can commit to 50 new

ML training requests per instance within a 24 hour window. This excludes scheduled re-
training requests. In addition, clustering and similarity updates are also excluded from this
limit, even if the new training requests exceed 50 within a 24 hour window.

#### ML Training Jobs view summary

The view shows all ML training jobs grouped by the four Predictive Intelligence capability
frameworks: classification, similarity, clustering, and regression.
Each record displays values such as solution name, version, training state, and training
completion percentage.
If you don't have any training jobs for a particular capability, the list doesn't display a group for
that capability. For example, in this scenario, there is no group for regression because you don't
have any regression solutions that you've submitted for training yet.
Select the Solution Name to see the details of the ML solution, as demonstrated in the images

> Source page: 1473

#### Use Predictive Intelligence in Workflow Studio with ML actions

Use Predictive Intelligence actions in Workflow Studio to create flows that incorporate your model
predictions.

#### Before you begin

• Make sure the following plugins are activated in your instance: Predictive
Intelligence (com.glide.platform_ml) and Predictive Intelligence for Workflow Studio
(com.snc.ml_flowdesigner).
• Create or use an existing trained Predictive Intelligence solution.
• Roles required: ml_admin or admin, and flow_designer or delegated_developer.

#### About this task

Workflow Studio enables you to automate complex processes. The first thing to identify is what
process you want to automate. In this example scenario, you're automating the assignment of a
Category to an incident record. When you complete the flow, the next incident record created

> Source page: 1474

in your instance updates the Category field in the record based on the text entered in the Short
description field.
You can deploy any active and trained classification, similarity, or regression ML solution in your
flow, as appropriate for your use case.

#### Note: The regression framework is deprecated in the Zurich release. You can continue to

use existing regression solutions but you can't create new ones.
In this example procedure, you create a flow that implements the ml_incident_categorization
solution in a Workflow Studio action. You can find this solution by searching on the ML Solutions
[ml_solution] table, as shown in the image below. Confirm that the solution you use has been
trained and its Active value is set to true.
For more information on how to use Flow Designer in Workflow Studio, see Exploring flows
. For
information about the Actions included in Predictive Intelligence for Workflow Studio, see the
Spoke actions table in Machine Learning solutions for Flow Designer
.

#### Procedure

1. Navigate to All > Process Automation > Workflow Studio.
2. Select New > Flow.
3. On the Let's get the details for your flow screen, configure the following fields.
Expand Show additional properties to view all fields.

#### Field

#### Description

Flow Name
Provide a name for the flow. In this scenario,
you enter Auto-assign Category to
Incident.

> Source page: 1475

#### Field

#### Description

Description
Enter a brief summary description of what
the flow delivers. For example, you enter
the following: When an incident
is created, it automatically
triggers this flow, which
uses ML Solutions to predict
the correct Category for the
incident.
Select Global.
Application

#### Select --None-- or Read-only. In this

Protection
scenario, you select --None--.
Select User who initiates session.
Run As
Run with role(s)
Leave blank.
Flow priority default
Medium (default).
4. Select Build flow.

> Source page: 1476

The Flow screen appears, showing the Auto-assign Category to Incident name you assigned to
the flow. If a Getting started screen appears, select Skip tour.
5. In the TRIGGER section of the Flow screen, configure the following fields to create a trigger for
the flow.
a. Select a Trigger: Select Record, then from the list of possible options for Record, select
Created.
b. Table: Select Incident [incident].

#### Note: After you configure both the Trigger and Table fields, record data pills appear

in the Data section of the screen so you can use them in your flow.

> Source page: 1477

c. Condition: Select Add filters if you want to add any conditions to the flow.
d. Optional: Open the Advanced Options panel to view additional conditions you can apply to
the flow.
e. Optional: To close the panel, select Advanced Options.
f. Select Done.
6. In the ACTIONS section of the screen, configure the following fields to create a Classification
Prediction action.
a. Action tab: Select Action > Predictive Intelligence > Classification Prediction.

> Source page: 1478

Select the information icon (
) to see the description of a Classification Prediction.
b. Solution [ML Solution]: Select ml_incident_categorization.
c. Top N: Enter 3 for the example scenario.
When you enter a number, such as 3, the system uses the top three ML predictions that have
the highest prediction confidence score. If you don't enter anything, the system sets the
default value to 1.
d. Input Record: Drag and drop your Trigger → Incident Record data pill into the Input Record
field.
The Action, Solution Name, Top N, and Input Record values provide a base for the Category
prediction.

#### Note: The data pill you drop into this record must also be a record. For example, don't

try to drop a table pill or a date/time pill into the Input Record field.
e. Select Done.
Result: The Classification Prediction action is completed in the flow and its data pills appear
in the Data section of the screen.

> Source page: 1479

7. In the ACTIONS section of the screen, use the following steps to create actions and flow logic
for the incident's Prediction Results.

#### Note: Although you can use a loop to iterate through every prediction result, the

scenario shown in this documentation uses a relatively small number of actions. For more
advanced flow configurations, see the Flow Designer
.
a. For each item in list of items: Drag and drop the Prediction Results data pill into the Items
field.

#### Note:

In order to access the list of items in the Regression Prediction action, you don't need
the For Each Item in flow logic.
(The regression framework is deprecated in the Zurich release. You can continue to use
existing regression solutions but you can't create new ones.)
b. Select Done.
Result: The Prediction Results action is started in the flow and its data pills appear in the
Data section of the screen.
8. In the ACTIONS section of the screen, select Action > Predictive Intelligence > PI Confidence
Check.
The PI Confidence Check is a tool you can use to compare values in a flow. In this use case, it
compares prediction result values, and the output from the check is either True or False.

> Source page: 1480

9. Drag and drop the confidence data pill into the Predicted Number from Predictive
Intelligence field.
10. Enter 50 in the Comparison Threshold field.
In this example scenario, you enter the number 50, which tells the system to use predictions
that have a confidence score above 50%.
11. Select Done.
12. Select Flow Logic > If to add a condition to the flow.

> Source page: 1481

13. Configure the following fields to define the first part of the condition flow logic.
  ◦Condition: Enter a name for the condition that defines what it does. In this example scenario,
you enter Confidence greater than 50.
  ◦Condition 1: Drag and drop the Confidence To Predict data pill into the field. Select is, and
enter the value True. This step completes the first part (the antecedent) of the condition
flow logic.
  ◦Select Done.
14. Select Action and enter worknote into the search field.
15. Select ITSM > Add Worknote to add a work note as the second part (the conclusion) of the
condition.

> Source page: 1482

16. Configure the following fields to define the second and final part of the condition flow logic.
  ◦Action: As a result of Step 14 above, Add Worknote appears automatically in this field.
  ◦task [task]: Drag and drop the Incident Record data pill into the field.
  ◦work note: Drag and drop the predicted_value data pill into the field. This step completes
the condition flow logic conclusion.
  ◦Select Done.
17. Select Action and enter update record into the search field.
18. Select Update Record.

> Source page: 1483

19. Configure the following fields to update the Incident Record.
  ◦Action: As a result of Step 16 above, Update Record appears automatically in this field.
  ◦Record: Drag and drop the Incident Record data pill into this field.
  ◦Table: Select Incident [incident].
  ◦Fields: Select Category. Then drag and drop the predicted_value data pill into this field,
next to the Category value.
  ◦Select Done.
20. Select Save.
21. Select Activate.

#### Result

> Source page: 1484

  ◦Your Auto-assign Category to Incident flow is activated and complete.
  ◦It also appears as published in the Flows column on the Workflow Studio home screen.
22. Navigate to Incidents.
23. Select New to create a test incident record in the Incidents table.
In this example scenario, you create record INC0010011.
24. In the record you created, note in the following image that the Category value is set to Inquiry /
Help.
25. In the Short description field, enter Email not working.
26. Select Submit.

> Source page: 1485

#### Result

The system updates the incident record to show that its Category value has changed from
Inquiry / Help to Email.
  ◦
  ◦

#### Related topics

Machine Learning solutions for Flow Designer

> Source page: 1486

#### Using MLSolutionFactory scriptable objects

MLSolutionFactory scriptable objects enable defining ML functionality. You can use the APIs to
compose data-driven functionality, such as subclustering large clusters or clusters with multiple
PRBs attached.
You can use scriptable objects in a scripted extension point to modify the Predictive Intelligence
REST API method to address unique business use cases.
ServiceNow applications on the NOW platform can call scriptable objects and script includes.
External applications can call scripted REST APIs. By default, the Predictive Intelligence REST
API - Prediction for multiple solutions (GET) method uses the MLSolutionUtil scripted extension
point to take a list of active solution names, run predictions on them given the input, and return
results. The MLSolutionUtil extension point enables creating custom implementations for specific
usage scenarios, for example, running a second solution prediction only after the condition of a
first solution prediction is satisfied.
Here's the high-level process for creating a custom usage scenario.
1. Developers customize a MLSolutionUtil scripted extension point implementation using the
MLSolutionFactory scriptable object.
  ◦Listed as global.MLSolutionUtil in the Extension Point [sys_extension_point] table
  ◦See Register a custom script include
2. The MLSolutionUtil scripted extension point implementation uses MLSolutionFactory to
get the scriptable object, and invokes prediction methods on that object.
3. The Predictive Intelligence REST API - Prediction for multiple solutions (GET) method invokes
the MLSolutionUtil extension point implementation, depending on the scope of
the request.
4. Applications call the Predictive Intelligence REST API - Prediction for multiple solutions (GET)
end point from a script include form.
For more information, see
• Predictive Intelligence REST API
• MLSolutionFactory - Global

#### Preserve ML solutions during a system clone

Save your trained machine-learning (ML) solution data during a system clone.

#### Before you begin

Role required: clone_admin or admin

#### About this task

The system stores trained ML solutions as Attachment records. These records include your
solution artifacts, such as solution definitions, template records, and predictive model statistics,
all of which are required components of the Predictive Intelligence prediction functionality. To
preserve these records, follow the high-level steps below each time you run a system clone.

#### Note:

For troubleshooting common issues with cloning solutions, see the Predictive Intelligence
Common issues [KB0781893]
article in the Now Support Knowledge Base.

> Source page: 1487

#### Procedure

1. Enter sys_properties.list in the application navigator to access the System Properties
list.
2. Ensure the glide.platform_ml.clone_artifacts system property is set to True.
3. If you want to preserve only the ML solution records and not the numerous other records in the
sys_attachments table, exclude the sys_attachments table from your clone run.
4. Request a system clone.
The system preserves your ML solution records during the system clone.


---

## IMAGE DESCRIPTIONS

### Repeated ServiceNow page header/logo

The ServiceNow-branded wordmark appears in the upper-left corner of reviewed source pages for this subsection. It is a recurring branding image, not a technical diagram. It contains the visible brand text `servicenow`, with green accenting in the `now` portion. Reviewed pages: 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487.

### Small UI icons and inline pictograms

1 small non-logo icon/pictogram image blocks were reviewed on source pages 1478. These include information icons, external-link indicators, UI symbols, or small inline graphics. They support the surrounding text but do not contain standalone table data. Coordinates and classification are retained in `_assets/image_inventory.csv`.

### Source page 1472 — Image 1

![Source page 1472 image 1](_assets/p1472_image01.png)

* **Bounding box:** x=72.0, y=502.2, width=432.0 pt, height=211.1 pt.
* **Nearby source context:** Predictive Intelligence > Training Jobs. / Note: The ML scheduler limits the number of trainings an instance can commit to 50 new / ML Training Jobs view summary
* **What is shown:** This embedded source image appears near the source context `Predictive Intelligence > Training Jobs. / Note: The ML scheduler limits the number of trainings an instance can commit to 50 new / ML Training Jobs view summary`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1472_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1473 — Image 2

![Source page 1473 image 2](_assets/p1473_image01.png)

* **Bounding box:** x=72.0, y=39.0, width=432.0 pt, height=211.1 pt.
* **Nearby source context:** No nearby heading text was detected.
* **What is shown:** This embedded source image appears near the source context `No nearby heading text was detected.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1473_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1473 — Image 3

![Source page 1473 image 3](_assets/p1473_image02.png)

* **Bounding box:** x=72.0, y=263.4, width=432.0 pt, height=253.3 pt.
* **Nearby source context:** No nearby heading text was detected.
* **What is shown:** This embedded source image appears near the source context `No nearby heading text was detected.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1473_image02.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1474 — Image 4

![Source page 1474 image 4](_assets/p1474_image01.png)

* **Bounding box:** x=72.0, y=206.3, width=432.0 pt, height=115.5 pt.
* **Nearby source context:** description field. / Note: The regression framework is deprecated in the Zurich release. You can continue to / trained and its Active value is set to true.
* **What is shown:** This embedded source image appears near the source context `description field. / Note: The regression framework is deprecated in the Zurich release. You can continue to / trained and its Active value is set to true.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1474_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1474 — Image 5

![Source page 1474 image 5](_assets/p1474_image02.png)

* **Bounding box:** x=112.0, y=449.5, width=432.0 pt, height=146.8 pt.
* **Nearby source context:** Procedure / 1. Navigate to All > Process Automation > Workflow Studio. / 2. Select New > Flow.
* **What is shown:** This embedded source image appears near the source context `Procedure / 1. Navigate to All > Process Automation > Workflow Studio. / 2. Select New > Flow.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1474_image02.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1475 — Image 6

![Source page 1475 image 6](_assets/p1475_image01.png)

* **Bounding box:** x=112.0, y=312.9, width=432.0 pt, height=432.7 pt.
* **Nearby source context:** scenario, you select --None--. / Select User who initiates session. / 4. Select Build flow.
* **What is shown:** This embedded source image appears near the source context `scenario, you select --None--. / Select User who initiates session. / 4. Select Build flow.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1475_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1476 — Image 7

![Source page 1476 image 7](_assets/p1476_image01.png)

* **Bounding box:** x=122.0, y=145.5, width=432.0 pt, height=384.9 pt.
* **Nearby source context:** 5. In the TRIGGER section of the Flow screen, configure the following fields to create a trigger for / a. Select a Trigger: Select Record, then from the list of possible options for Record, select / Created.
* **What is shown:** This embedded source image appears near the source context `5. In the TRIGGER section of the Flow screen, configure the following fields to create a trigger for / a. Select a Trigger: Select Record, then from the list of possible options for Record, select / Created.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1476_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1477 — Image 8

![Source page 1477 image 8](_assets/p1477_image01.png)

* **Bounding box:** x=122.0, y=39.0, width=432.0 pt, height=208.1 pt.
* **Nearby source context:** No nearby heading text was detected.
* **What is shown:** This embedded source image appears near the source context `No nearby heading text was detected.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1477_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1477 — Image 9

![Source page 1477 image 9](_assets/p1477_image02.png)

* **Bounding box:** x=122.0, y=454.9, width=432.0 pt, height=279.7 pt.
* **Nearby source context:** f. Select Done. / 6. In the ACTIONS section of the screen, configure the following fields to create a Classification / a. Action tab: Select Action > Predictive Intelligence > Classification Prediction.
* **What is shown:** This embedded source image appears near the source context `f. Select Done. / 6. In the ACTIONS section of the screen, configure the following fields to create a Classification / a. Action tab: Select Action > Predictive Intelligence > Classification Prediction.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1477_image02.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1478 — Image 10

![Source page 1478 image 10](_assets/p1478_image01.png)

* **Bounding box:** x=122.0, y=201.3, width=432.0 pt, height=196.2 pt.
* **Nearby source context:** b. Solution [ML Solution]: Select ml_incident_categorization. / c. Top N: Enter 3 for the example scenario. / d. Input Record: Drag and drop your Trigger → Incident Record data pill into the Input Record
* **What is shown:** This embedded source image appears near the source context `b. Solution [ML Solution]: Select ml_incident_categorization. / c. Top N: Enter 3 for the example scenario. / d. Input Record: Drag and drop your Trigger → Incident Record data pill into the Input Record`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1478_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1478 — Image 11

![Source page 1478 image 11](_assets/p1478_image02.png)

* **Bounding box:** x=122.0, y=536.2, width=432.0 pt, height=189.8 pt.
* **Nearby source context:** Note: The data pill you drop into this record must also be a record. For example, don't / e. Select Done. / Result: The Classification Prediction action is completed in the flow and its data pills appear
* **What is shown:** This embedded source image appears near the source context `Note: The data pill you drop into this record must also be a record. For example, don't / e. Select Done. / Result: The Classification Prediction action is completed in the flow and its data pills appear`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1478_image02.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1479 — Image 12

![Source page 1479 image 12](_assets/p1479_image01.png)

* **Bounding box:** x=122.0, y=170.9, width=432.0 pt, height=150.0 pt.
* **Nearby source context:** 7. In the ACTIONS section of the screen, use the following steps to create actions and flow logic / Note: Although you can use a loop to iterate through every prediction result, the / a. For each item in list of items: Drag and drop the Prediction Results data pill into the Items
* **What is shown:** This embedded source image appears near the source context `7. In the ACTIONS section of the screen, use the following steps to create actions and flow logic / Note: Although you can use a loop to iterate through every prediction result, the / a. For each item in list of items: Drag and drop the Prediction Results data pill into the Items`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1479_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1480 — Image 13

![Source page 1480 image 13](_assets/p1480_image01.png)

* **Bounding box:** x=112.0, y=39.0, width=432.0 pt, height=235.9 pt.
* **Nearby source context:** No nearby heading text was detected.
* **What is shown:** This embedded source image appears near the source context `No nearby heading text was detected.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1480_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1480 — Image 14

![Source page 1480 image 14](_assets/p1480_image02.png)

* **Bounding box:** x=112.0, y=390.4, width=432.0 pt, height=214.7 pt.
* **Nearby source context:** Intelligence field. / 10. Enter 50 in the Comparison Threshold field. / 11. Select Done.
* **What is shown:** This embedded source image appears near the source context `Intelligence field. / 10. Enter 50 in the Comparison Threshold field. / 11. Select Done.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1480_image02.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1481 — Image 15

![Source page 1481 image 15](_assets/p1481_image01.png)

* **Bounding box:** x=112.0, y=39.0, width=432.0 pt, height=217.5 pt.
* **Nearby source context:** No nearby heading text was detected.
* **What is shown:** This embedded source image appears near the source context `No nearby heading text was detected.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1481_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1481 — Image 16

![Source page 1481 image 16](_assets/p1481_image02.png)

* **Bounding box:** x=112.0, y=390.3, width=432.0 pt, height=229.3 pt.
* **Nearby source context:** ◦Condition: Enter a name for the condition that defines what it does. In this example scenario, / ◦Condition 1: Drag and drop the Confidence To Predict data pill into the field. Select is, and / ◦Select Done.
* **What is shown:** This embedded source image appears near the source context `◦Condition: Enter a name for the condition that defines what it does. In this example scenario, / ◦Condition 1: Drag and drop the Confidence To Predict data pill into the field. Select is, and / ◦Select Done.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1481_image02.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1482 — Image 17

![Source page 1482 image 17](_assets/p1482_image01.png)

* **Bounding box:** x=112.0, y=39.0, width=432.0 pt, height=225.4 pt.
* **Nearby source context:** No nearby heading text was detected.
* **What is shown:** This embedded source image appears near the source context `No nearby heading text was detected.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1482_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1482 — Image 18

![Source page 1482 image 18](_assets/p1482_image02.png)

* **Bounding box:** x=112.0, y=391.5, width=432.0 pt, height=222.6 pt.
* **Nearby source context:** ◦task [task]: Drag and drop the Incident Record data pill into the field. / ◦work note: Drag and drop the predicted_value data pill into the field. This step completes / ◦Select Done.
* **What is shown:** This embedded source image appears near the source context `◦task [task]: Drag and drop the Incident Record data pill into the field. / ◦work note: Drag and drop the predicted_value data pill into the field. This step completes / ◦Select Done.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1482_image02.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1483 — Image 19

![Source page 1483 image 19](_assets/p1483_image01.png)

* **Bounding box:** x=112.0, y=39.0, width=432.0 pt, height=220.0 pt.
* **Nearby source context:** No nearby heading text was detected.
* **What is shown:** This embedded source image appears near the source context `No nearby heading text was detected.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1483_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1483 — Image 20

![Source page 1483 image 20](_assets/p1483_image02.png)

* **Bounding box:** x=122.0, y=404.3, width=432.0 pt, height=220.8 pt.
* **Nearby source context:** ◦Fields: Select Category. Then drag and drop the predicted_value data pill into this field, / next to the Category value. / ◦Select Done.
* **What is shown:** This embedded source image appears near the source context `◦Fields: Select Category. Then drag and drop the predicted_value data pill into this field, / next to the Category value. / ◦Select Done.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1483_image02.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1484 — Image 21

![Source page 1484 image 21](_assets/p1484_image01.png)

* **Bounding box:** x=122.0, y=67.2, width=432.0 pt, height=228.4 pt.
* **Nearby source context:** ◦Your Auto-assign Category to Incident flow is activated and complete.
* **What is shown:** This embedded source image appears near the source context `◦Your Auto-assign Category to Incident flow is activated and complete.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1484_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1484 — Image 22

![Source page 1484 image 22](_assets/p1484_image02.png)

* **Bounding box:** x=122.0, y=337.2, width=432.0 pt, height=148.6 pt.
* **Nearby source context:** ◦Your Auto-assign Category to Incident flow is activated and complete. / ◦It also appears as published in the Flows column on the Workflow Studio home screen.
* **What is shown:** This embedded source image appears near the source context `◦Your Auto-assign Category to Incident flow is activated and complete. / ◦It also appears as published in the Flows column on the Workflow Studio home screen.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1484_image02.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1484 — Image 23

![Source page 1484 image 23](_assets/p1484_image03.png)

* **Bounding box:** x=112.0, y=558.1, width=432.0 pt, height=95.1 pt.
* **Nearby source context:** 22. Navigate to Incidents. / 23. Select New to create a test incident record in the Incidents table.
* **What is shown:** This embedded source image appears near the source context `22. Navigate to Incidents. / 23. Select New to create a test incident record in the Incidents table.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1484_image03.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1485 — Image 24

![Source page 1485 image 24](_assets/p1485_image01.png)

* **Bounding box:** x=112.0, y=39.0, width=432.0 pt, height=166.5 pt.
* **Nearby source context:** No nearby heading text was detected.
* **What is shown:** This embedded source image appears near the source context `No nearby heading text was detected.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1485_image01.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1485 — Image 25

![Source page 1485 image 25](_assets/p1485_image02.png)

* **Bounding box:** x=122.0, y=282.0, width=432.0 pt, height=168.8 pt.
* **Nearby source context:** Result / Inquiry / Help to Email.
* **What is shown:** This embedded source image appears near the source context `Result / Inquiry / Help to Email.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1485_image02.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```

### Source page 1485 — Image 26

![Source page 1485 image 26](_assets/p1485_image03.png)

* **Bounding box:** x=122.0, y=479.9, width=432.0 pt, height=212.7 pt.
* **Nearby source context:** Result / Inquiry / Help to Email.
* **What is shown:** This embedded source image appears near the source context `Result / Inquiry / Help to Email.`. It is a ServiceNow product screenshot, UI form, list view, report/dashboard visual, setup screen, dialog, or instructional figure supporting the surrounding procedure. Objects may include application headers, navigation breadcrumbs, form fields, related links, buttons, tabs, lists, result rows, charts, and highlighted controls. Its business purpose is to make the Predictive Intelligence setup, training, testing, monitoring, or reference procedure easier to follow. Its technical purpose is to identify the exact ServiceNow screen state, field, UI region, or configuration control referenced by the same-page instructions.
* **Objects/components present:** ServiceNow interface elements, icons, labels, fields, controls, lists, charts, or instructional blocks visible in the crop as applicable. The exact crop is preserved in `_assets/p1485_image03.png` for long-term verification.
* **Relationships / arrows / flow / labels:** The relationships are UI relationships visible inside the screenshot: fields belong to a form, buttons and links trigger actions, rows belong to lists/tables, charts summarize records, tabs separate panels, and highlighted areas identify the intended target. No separate network topology, architecture component boundary, or security zone is labeled unless visible in the asset.
* **Business purpose:** Supports the reader in performing or understanding the Predictive Intelligence operation described by the surrounding source page.
* **Technical purpose:** Preserves the UI state or conceptual visual needed to reproduce, verify, or interpret the procedure.
* **Visible text captured from image:**

```text
[No separate OCR text recorded for this crop; source asset is retained for visual verification.]
```


---

## TABLES

### Source page 1464 — Table 1

**Nearby source context:** • Incident categorization: Predicts the incident category based on the short description. See / • CSM case assignment: Predicts the case record assignment group based on the short / Testing and monitoring predictions

| Report | Description |
| --- | --- |
| Average Prediction Coverage (last 30 days) | The percentage of predictions that yielded an<br>outcome out of the total number of predictions<br>attempted. Click the coverage score to see a<br>breakdown by class. |
| Daily Prediction Coverage | The percentage of records created on a given<br>day in which the solution was able to predict<br>an outcome. |

### Source page 1465 — Table 2

| Report | Description |
| --- | --- |
| Average Prediction Precision (last 30 days) | The percentage of predictions in which the<br>predicted value was the same as the final<br>value of the field when the record closed. Click<br>the precision score to see a breakdown by<br>class. |
| Daily Prediction Precision | The percentage of records closed on a given<br>day in which the predicted field value was the<br>same as the final value. |

### Source page 1474 — Table 3

**Nearby source context:** 2. Select New > Flow. / 3. On the Let's get the details for your flow screen, configure the following fields. / Expand Show additional properties to view all fields.

| Field | Description |
| --- | --- |
| Flow Name | Provide a name for the flow. In this scenario,<br>you enter Auto-assign Category to<br>Incident. |

### Source page 1475 — Table 4

| Field | Description |
| --- | --- |
| Description | Enter a brief summary description of what<br>the flow delivers. For example, you enter<br>the following: When an incident<br>is created, it automatically<br>triggers this flow, which<br>uses ML Solutions to predict<br>the correct Category for the<br>incident. |
| Application | Select Global. |
| Protection | Select --None-- or Read-only. In this<br>scenario, you select --None--. |
| Run As | Select User who initiates session. |
| Run with role(s) | Leave blank. |
| Flow priority default | Medium (default). |


---

## FIGURES

| Figure / visual | Source page | Asset or location | Analysis |
|---|---:|---|---|
| Embedded screenshot or instructional image 1 | 1472 | `_assets/p1472_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 2 | 1473 | `_assets/p1473_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 3 | 1473 | `_assets/p1473_image02.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 4 | 1474 | `_assets/p1474_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 5 | 1474 | `_assets/p1474_image02.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 6 | 1475 | `_assets/p1475_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 7 | 1476 | `_assets/p1476_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 8 | 1477 | `_assets/p1477_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 9 | 1477 | `_assets/p1477_image02.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 10 | 1478 | `_assets/p1478_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 11 | 1478 | `_assets/p1478_image02.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 12 | 1479 | `_assets/p1479_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 13 | 1480 | `_assets/p1480_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 14 | 1480 | `_assets/p1480_image02.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 15 | 1481 | `_assets/p1481_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 16 | 1481 | `_assets/p1481_image02.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 17 | 1482 | `_assets/p1482_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 18 | 1482 | `_assets/p1482_image02.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 19 | 1483 | `_assets/p1483_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 20 | 1483 | `_assets/p1483_image02.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 21 | 1484 | `_assets/p1484_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 22 | 1484 | `_assets/p1484_image02.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 23 | 1484 | `_assets/p1484_image03.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 24 | 1485 | `_assets/p1485_image01.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 25 | 1485 | `_assets/p1485_image02.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Embedded screenshot or instructional image 26 | 1485 | `_assets/p1485_image03.png` | Detailed image analysis is provided in IMAGE DESCRIPTIONS; crop asset retained for visual verification. |
| Markdown-converted table/grid 1 | 1464 | TABLES section | Source table/grid region converted into Markdown; nearby context: • Incident categorization: Predicts the incident category based on the short description. See / • CSM case assignment: Predicts the case record assignment group based on the short / Testing and monitoring predictions |
| Markdown-converted table/grid 2 | 1465 | TABLES section | Source table/grid region converted into Markdown; nearby context:  |
| Markdown-converted table/grid 3 | 1474 | TABLES section | Source table/grid region converted into Markdown; nearby context: 2. Select New > Flow. / 3. On the Let's get the details for your flow screen, configure the following fields. / Expand Show additional properties to view all fields. |
| Markdown-converted table/grid 4 | 1475 | TABLES section | Source table/grid region converted into Markdown; nearby context:  |


---

## QUALITY ASSURANCE NOTES

* PAGES REVIEWED: 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487. Source page range: 1464-1487 (shared boundary pages split at source headings).
* IMAGES REVIEWED: 50 image blocks assigned/reviewed: 23 recurring header logo block(s), 1 small icon/pictogram block(s), and 26 large screenshot/diagram crop(s).
* TABLES REVIEWED: 4 table/grid region(s) converted to Markdown. Table pages: 1464, 1465, 1474, 1475.
* FIGURES REVIEWED: 26 large screenshot/diagram figure(s) plus 4 table/grid visual(s).
* OCR ISSUES FOUND: No unresolved OCR issues were identified in the main PDF text layer after cleanup. Embedded screenshot crops are preserved as source assets; automated image OCR was not applied in this pass to avoid inserting low-confidence text, and this is explicitly marked in each image record.
* OCR ISSUES CORRECTED: Removed recurring footer/page-number noise from the main content stream, normalized nonbreaking spaces and soft-hyphen/control artifacts, preserved bullets/numbering/property names, and converted detected tables to Markdown.
* SECTION MAPPING NOTES: Folder name is exactly `Predictive Intelligence`. File name and subsection name are exactly `Using Predictive Intelligence` from the TOC. Shared source pages were split at heading coordinates from the PDF text layer.
* PAGE FOOTERS REVIEWED: Reviewed recurring ServiceNow copyright/trademark footer and logical page numbers. Footer text reviewed: `© 2026 ServiceNow, Inc. All rights reserved. ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries. Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.`
* RECHECK PASSES COMPLETED: 12/12: page completeness, text extraction, table extraction, image extraction, diagram interpretation, section mapping, subsection mapping, file names, folder names, Markdown formatting, missed-content review, and OCR/text-layer cleanup.
* VERIFICATION ARTIFACTS: Large image crops and `image_inventory.csv` are stored in the `_assets` folder inside this section folder.
