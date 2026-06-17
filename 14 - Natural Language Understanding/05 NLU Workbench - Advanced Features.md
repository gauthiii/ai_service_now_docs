# NLU Workbench - Advanced Features

_Source: ServiceNow Now Assist documentation, pages 1191-1233._

## Overview

NLU Workbench - Advanced Features expands the functionality of NLU Workbench to help you manage and improve your models.

The NLU Workbench - Advanced Features application includes the following features:

- **Multi-model Batch Testing** - Test large groups of utterances against your NLU models to see how the model predicts intents.
- **Cross-model Conflict Review** - Identify conflicting intents within or across models to improve model performance.
- **NLU Model Performance** - Use NLU Model Performance to see how well your models predicted intents in Virtual Agent based on end-user confirmation.
- **NLU Expert Feedback Loop for VA** - Provide feedback on Virtual Agent chat log utterances to help the system continuously learn and to better predict user input.
- **Irrelevance detection in NLU** - Train your Virtual Agent models to ignore utterances that are not relevant.
- **Issue Auto Resolution Tuning in NLU (Expert Feedback Loop for IAR)** - Provide feedback to your ITSM Issue Auto Resolution model to improve its predictions.

After the application is installed and activated, **Model Performance**, **Expert Feedback Loop for VA**, and **Expert Feedback Loop for IAR** appear under **All > NLU Workbench**. **Multi-model Batch Testing** and **Cross-model Conflict Review** appear under **All > NLU Workbench > NLU Advanced Features**.

NLU Workbench - Advanced Features is available from the ServiceNow Store. For instructions on how to purchase and download, see Install NLU Workbench - Advanced Features.

> **Note:** The available Intent Discovery ServiceNow Store application is installed separately from NLU Workbench - Advanced Features.

### Context note on publishing failures

Publishing a topic with a mapped intent fails for the following reasons:

- Model isn't trained, or training is in progress.
- The last trained model is already published with a VA topic.
- The intent is not enabled in the model.

## Features

The application bundles six advanced capabilities plus a separately installed companion application (Intent Discovery):

| Feature | Purpose |
| --- | --- |
| Multi-model Batch Testing | Test large groups of utterances against your NLU models to see how the model predicts intents. |
| Cross-model Conflict Review | Identify conflicting intents within or across models to improve model performance. |
| NLU Model Performance | See how well your models predicted intents in Virtual Agent based on end-user confirmation. |
| NLU Expert Feedback Loop for VA | Provide feedback on Virtual Agent chat log utterances so the system continuously learns and better predicts user input. |
| Irrelevance detection in NLU | Train your Virtual Agent models to ignore utterances that are not relevant. |
| Issue Auto Resolution Tuning in NLU (Expert Feedback Loop for IAR) | Provide feedback to your ITSM Issue Auto Resolution model to improve its predictions. |
| Intent Discovery (separate install) | Identify opportunities for incident deflection - for example, which Virtual Agent conversations to activate next. |

## Functionalities

### Required ServiceNow plugins

NLU Workbench - Advanced Features requires the following plugins. Ensure that these plugins are activated before you install NLU Workbench - Advanced Features.

| Plugin | Description |
| --- | --- |
| Predictive Intelligence (com.glide.platform_ml) | Enables various Predictive Intelligence and Machine Learning capabilities for training models. See Predictive Intelligence. |
| NLU Workbench - Core (com.glide.nlu) | Adds NLU Model capabilities. See Activate the NLU Workbench. |
| NLU Workbench (com.snc.nlu_studio) | Create and train NLU models. See Activate the NLU Workbench. |

The plugin ID for NLU Workbench - Advanced Features itself is **com.snc.nlu.workbench.advanced**.

### Tables installed with NLU Workbench - Advanced Features

Several types of components are installed with activation of the **com.snc.nlu.workbench.advanced** plugin, including tables.

> **Note:** The Application Files table lists the components that are installed with this application. For instructions on how to access this table, see Find components installed with an application.

| Table | Description |
| --- | --- |
| NLU Performance Ignored Clusters [nlu_performance_ignored_clusters] | Contains information on the ignored cluster. Filled when user clicks Ignore. |
| NLU Batch Test Result [nlu_batch_test_result] | Contains the parsed results of a batch test including each utterance and predicted intent. |
| NLU Conflict Execution [nlu_conflict_execution] | Stores the information related to each execution of a conflict analysis run for a given definition. |
| NLU Batch Test Run Definition [nlu_batch_test_run_definition] | Contains base information related to the batch test execution. |
| NLU Batch Test Run Execution [nlu_batch_test_run_execution] | Contains information related to each execution of the batch test. |
| NLU Conflict Result [nlu_conflict_result] | Stores the complete results of a conflict analysis execution. |
| NLU Batch Test Utterance [nlu_batch_test_utterance] | Contains the utterances used for a test set. Populated by the import set. |
| NLU Batch Test Set [nlu_batch_test_set] | Includes the information for the batch test. Referenced by the utterance record and run definition. |
| NLU Performance Utterance Trace [nlu_performance_utterance_trace] | Contains the information on the utterances added to an intent. |
| NLU Conflict Definition [nlu_conflict_definition] | Contains the details of the NLU model or pair of models used for the conflict. |
| NLU Model Analysis Definition [nlu_analysis_definition] | Supports IAR model tuning in NLU Workbench. |
| NLU Model Analysis Execution [nlu_analysis_execution] | Stores records for each instance of IAR model tuning in NLU Workbench. |
| ML Label User Feedback [ml_label_user_feedback] | Stores utterances that are marked Needs review. |

### Role installed

| Role | Description |
| --- | --- |
| NLU Feedback Admin [nlu_feedback_admin] | Data labelling (NLU feedback) Admin role - to manage data labelling across models, also ability to optimize models. |

### Multi-model Batch Testing components

Test multiple Natural Language Understanding (NLU) models against a large set of utterances to evaluate the performance of the models. Add test sets, test multiple models, and see test results.

- Use Multi-model Batch Testing to create and upload test sets comprised of utterances and their expected intents. You can then run tests against your NLU models.
- Multi-model Batch Testing works with models for all supported NLU languages. See NLU language support.
- Multi-model Batch Testing is part of the NLU Workbench - Advanced Features app available on the ServiceNow Store. To use it, ensure that the NLU Workbench - Advanced Features (com.snc.nlu.workbench.advanced) plugin is active on your instance.

**Test sets**

- Test sets are lists of utterances and matched intents. Create a test set by using a table in a CSV or XLSX (Excel workbook) file.
- The table should contain two columns: one for utterances, and one for the expected intent.
- Your test set can include up to **10,000 rows**.
- To get the most out of testing, your test sets should include utterances that the model is likely to encounter from your users. Test utterances should be in the same language as the model to be tested.
- The test set should also include utterances with no expected intents. Including utterances with no expected intent helps assess your model's ability to detect utterances which are irrelevant and shouldn't have any intent predicted.
- If your test set does not cover at least **60%** of the intents of the models, you can still run the test but the recommended threshold may not be optimal.

> **Note:** Certain test utterances are skipped during the test if their expected intent does not match any intents in the models.

**Test results**

- The Test results page lists your completed and in-progress tests. At a glance, the results page shows the models tested against, the number of utterances, and prediction percentages.
- To see the details of a test result, click the name of the test set.
- The **Overview** page shows summary information about the results and includes a graphic with a breakdown of predictions.
- The **Intents that need attention (Current model)** shows the top 5 missed and incorrect intents. Click the intent name to drill down into the test utterances that were predicted incorrectly. Use this information to improve the model.
- The **Detailed results** tab lists information about each utterance that was tested. From here, you can see the prediction outcome and confidence per model for each utterance. Filter the results by using the search bar or interacting with the filter tools and column headers.
- You can also export the test results to a CSV file by clicking **Export**. The file includes the same columns as the detailed results page.

### Cross-model Conflict Review components

Identify conflicting intents within or across models so you can take corrective actions, resolve such conflicts, and improve your NLU model performance.

- As the number of intents within a model increases, two intents may overlap in scope. This may occur when training utterances in one intent are almost identical to utterances in another intent. There may also be conflicting intents across models and even applications.
- Utterances may also be marked as **Not relevant**, meaning that no intent should be predicted. When these irrelevant utterances are too similar to utterances assigned to an intent, they are displayed in Conflict Review. For more information, see Irrelevance detection in NLU.
- Cross-model Conflict Review runs an analysis on your models. Use the analysis to identify and resolve these issues prior to model publication and deployment.
- Cross-model Conflict Review is part of the NLU Workbench - Advanced Features app available on the ServiceNow Store. To use it, ensure that the NLU Workbench - Advanced Features (com.snc.nlu.workbench.advanced) plugin is active on your instance.

**Roles:** To access Cross-model Conflict Review, use the **nlu_admin** or **admin** role. When assigned to a model, the **nlu_editor** can resolve conflicts in that model.

**How analyses are structured**

- The Conflict Review screen shows a list view of all conflict reviews created in your instance. When a review is completed, it's added to a running list of reviews (for example, shown in the count as 1 of 1 reviews for the first review). As more conflicts arise over time, you will see multiple reviews in the list.
- Conflict reviews are analyzed on either one or two NLU models. When you run an analysis on a single model, the system shows intents and utterances that are only in that model. When you run an analysis on 2 models, the system shows intents and utterances that are in both models.
- Conflict reviews always run on the **last trained version** of the model(s) they analyze.
- Conflict reviews have two types: **Critical** and **Moderate**. The standard approach is to begin with the critical ones.

**Conflict resolution actions**

When a conflict is detected, you can use one of the following actions to resolve the conflict:

- Ignore the conflict
- Delete an identical or nearly identical utterance from one of the intents
- Edit the utterances to make them more distinct from each other

### NLU Model Performance components

Use NLU Model Performance to see how well your models predicted intents in Virtual Agent (VA) based on end-user confirmation.

- The NLU Model Performance application provides an analysis and report of how well your NLU models predict VA users' intents from their utterances. As NLU models for VA are updated, published, and deployed, you can use NLU Model Performance to review the efficacy of the intent predictions they make.
- If predictions are skipped, it's because they're unable to predict an intent with a high enough confidence score for the model. To improve VA topic prediction, the system groups unsupported VA utterances into clusters for an analysis and then generates a report that identifies the outcome of the analysis.
- To access this application, use the **nlu_admin** or **admin** role and navigate to **All > NLU Workbench > Performance**.

> **Note:** To use NLU Model Performance, you must first have at least **5,000 VA utterances** in your instance. With the nlu_admin role, you can modify this limit by resetting the `sn_nlu_workbench.glide.nlu.performance.min_clustering_records` property.

- NLU Model Performance is an application available on the ServiceNow Store. To use this application, ensure that the NLU Workbench - Advanced Features (sn_nlu_workbench) plugin is active on your instance.
- Because NLU Model Performance relies on data coming in from VA, ensure that the Glide Virtual Agent (com.glide.cs.chatbot) plugin is also active. See Activate Virtual Agent.

**UI parts**

The NLU Model Performance UI comprises the following parts:

- **The Performance tab** and its colored chart, which shows data describing scenarios that occur when users interact with VA. The chart is segmented in shades of three colors, each representing a user scenario. The rows in the chart that have text and percentages are referred to as the legend. The three scenarios in the first row of the legend have two outcome scenarios beneath them in the second row. The bars underneath the legend correspond to the colors of the scenarios above them and range in size based on the percentage value for each scenario.
  - Example: the dark blue bar shows that 10% of this batch of VA users confirmed that the system presented them the correct topic; the dark red bar shows 58% of the users confirmed the topic presented was incorrect; the dark brown bar (between the two) shows that 32% of users didn't make any confirmation at all.
  - Toggle the **Show all bars** filter back and forth at any time to see or hide the colored bars and their associated scenarios. When you first access NLU Model Performance, the default view shows only the first row of scenarios and the first row of bars.
  - When you click a scenario in the first row of the legend, the system hides the bars of the other two scenarios, partially isolating the scenario you're focusing on. These actions don't change any data; they only show different views of the legend and bars.
- **The Unsupported utterances tab**, which shows utterances grouped into clusters for use in the performance analysis. This section is where you can navigate to and return from the Expert Feedback Loop application, and where you can run the analysis. Unsupported utterances are different from irrelevant utterances - see Irrelevance detection in NLU.
- **The Performance Details section** located underneath the bar chart. This section has four columns: **Utterance**, **Predicted intent**, **Prediction model**, and **Prediction outcome**. The details shown in this section interact with the legend data and bar data above them.

**VA user scenario definitions**

In the legend section of the UI, the text and percentages are accompanied by Information icons. Point to an icon to invoke the definition for its user scenario.

| Scenario | Definition |
| --- | --- |
| User confirmed as correct | The correct topic was presented to the end user and the end user has confirmed it is correct. |
| Topic launched, user confirmed as correct | The topic was launched and the user confirmed it is the topic they needed. |
| Topic menu presented, user selected one | Multiple topics were shown as a menu to the user and the user chose one of the topics to address their need. |
| User made no confirmation | The topic was launched but the user did not confirm whether or not it met their need. |
| No prediction made, fallback topic launched | No predictions were made and the fallback topic was launched. |
| Topic launched, no user confirmation | The topic was launched but the user did not confirm whether it was correct. |
| User confirmed as incorrect | The topic(s) presented did not address the end user's needs, and the user has confirmed it is not correct. |
| Topic launched, user confirmed as incorrect | The topic was launched and the user confirmed it was not correct. |
| Topic menu presented, user selected none | Multiple topics were shown as a menu to the user and the user decided none of the topics were relevant and did not choose any topic. |

**Language and Model filters**

- On the Performance tab, you can see the **Language** and **Model** filters. Next to them you can also see the most recent Date range values you set above the legend and bars.
- Click the Language filter to see all languages that are available in NLU. Click the Model filter to see all prediction models available in your instance.
- Default setting for the Language filter is **All languages**; default for the Model filter is **All models**.
- The Language and Model filters interact with each other. For example, choosing French-fr in the Language filter automatically shows all prediction models in your instance that use the French language.
- If you select a specific model from the Model filter, the Language filter value updates to display the language of the selected model.
- If you select a specific language from the Language filter, the Model filter only displays models of that selected language.
- Underneath the filters, the **Include translated conversations** switch lets you include the performance of VA conversations that were translated to your primary language using dynamic language translation. Toggle the switch to the right so it changes color from grey to green; the bars in the chart's legend may also change position and colors. Manage dynamic language translation in the Conversational Interfaces Settings.

**Date range**

On the Performance tab, use the **Date range** to define how far back you want the system to pull VA data from. Choose **Past 30 days**, **Past 60 days**, **Past 90 days**, or **Custom range**. The further back you go, the more data you will have in your analysis.

### NLU Expert Feedback Loop components

Provide feedback on Virtual Agent chat log utterances to help the system continuously learn and to better predict user input.

- The Expert Feedback Loop takes data from your instance and provides it to you for feedback. This data comes from your users' Virtual Agent (VA) chat logs and includes utterances from those logs.
- Using the **nlu_admin** role, navigate to **All > NLU Workbench > Expert Feedback Loop** and mark each utterance in a model by confirming whether the utterance is correct (match) or incorrect (mismatch) to an intent. This feedback helps the model to continuously improve model performance.
- Expert Feedback Loop is part of the NLU Workbench - Advanced Features app available on the ServiceNow Store. To use it, ensure that the NLU Workbench - Advanced Features (sn_nlu_workbench) plugin is active.
- Because Expert Feedback Loop relies on data from VA chat logs, make sure the Glide Virtual Agent (com.glide.cs.chatbot) plugin is also active.

**Importing expert feedback loop data between instances**

- Before you start an import, make sure you have access to the data in your instance and have enough data to proceed with your feedback.
- If you're working in a sub-production instance, you must import the feedback data from the **open_nlu_predict_intent_feedback** table in your production instance to your sub-production instance. For guidance, see Importing from another ServiceNow instance.

Data scenarios regarding system behavior for the NLU models that house the feedback loop utterances:

- If you move a model to a different instance, the feedback data persists.
- If you upgrade the instance, the feedback data persists.
- If you clone an instance, the data does not persist, so you need to follow the import procedure to import the data onto the cloned instance.

**Feedback context and access**

- The Expert Feedback Loop provides a mechanism to improve NLU models deployed to VA through feedback you provide on a select subset of utterances. For each utterance, you are asked to confirm the predicted intent or to provide the correct intent it belongs to. After this feedback is complete, the data is used to tune the model performance, resulting in an improved model that can be redeployed to gather more end user data. This is an iterative cycle.
- Once every **30 days**, the system pulls up to **300 utterance samples** from VA chat logs to the Expert Feedback Loop. The utterances are selected for feedback based on how well they represent all the utterances in the logs. Every utterance sampled from VA chat logs has a predicted intent picked by the system.
- You can set the number of utterances pulled from VA chat logs by adjusting the `glide.mlpredictor.option.nlu.activeLearning.label_candidate_table.max_response` system property.
- As you review utterances, decide whether each utterance belongs to its predicted intent or should be moved to a different intent. If you aren't sure about the correct intent, the utterance can be marked to revisit. After you have marked at least **100 utterances** with your feedback, the system uses all the marked utterances to tune and improve the model.

**Utterance review values**

- Each page of the list shows approximately **20 utterances per page**.
- Mark each utterance with the **NLU_Match**, **Mismatch**, or **Unsure** value.
  - **NLU_Match** means you agree with the NLU prediction for that utterance.
  - **Mismatch** means the utterance belongs to a different intent; a dropdown of intents appears so you can select the correct intent.
  - **Unsure** means you aren't sure which intent is correct.
- Utterances marked and saved with NLU_Match or Mismatch are moved to the **Completed reviews** section.
- Utterances marked and saved with Unsure are moved to the **Needs further review** section.
- The **Showing** filter lets you group utterances by their value. The values are **All**, **NLU_Match**, and **Unsure**.

**Card view option**

- Expert Feedback Loop utterances appear in the To do section in a list view by default. You can choose a card view that shows each utterance framed within a card, in groups of five. While in the list view, click the **card icon**.
- Left and right arrows on either side of the page turn to the next or previous set of five cards. To switch back to the list view, click the **list icon** in the upper right corner.

**Changing an utterance value**

If you mark an utterance but change your mind on the value, click **MisMatch** and select another intent. Click **Save feedback** to save the change.

**Unsaved feedback**

If you finish and log out of a marking session but forget to save your changes, select **Unsaved changes** from the **Showing** prompt. This displays all the utterances you have given feedback for but haven't saved yet.

**System properties for procuring additional VA feedback data on demand**

- `glide.mlpredictor.option.nlu.activeLearning.va_chat_logs.max_row_limit` - 3000
- `glide.mlpredictor.option.nlu.activeLearning.label_candidate_table.max_data_size` - 10000
- `glide.mlpredictor.option.nlu.activeLearning.label_table.max_data_size` - 10000
- `glide.mlpredictor.option.nlu.activeLearning.label_candidate_table.max_response`

To see how these properties work within the context of other NLU properties, see NLU Workbench properties.

**Reviewing uncategorized utterances**

- As part of the feed from VA chat logs to the Expert Feedback Loop, the system collects and displays in a list any utterances in your instance that aren't part of a VA intent. Access these by selecting **Uncategorized** in the **Expert Feedback Loop for** prompt at the top of your screen.
- These utterances are shown in the Utterance column of the Uncategorized utterances section.

> **Important:** It is extremely important to provide feedback on this set of utterances because the system is suggesting there is no associated intent for them. By confirming this lack of association or by associating these utterances with an existing intent, you help the model learn correctly.

> **Note:** The Corrected Intent column enables you to search for and use all intents across all models in your instance.

- The **To do** section collects utterances that must be connected to an intent.
- The **Done** section shows utterances after you act on them.
- A vertical scroll bar to the far right of the screen lets you navigate the list; arrows at the bottom turn to the next or previous page.
- When you take action to make a connection, the **Save feedback** button (normally active by default) deactivates because the system recognizes your action and automatically saves your change.

**Expert Feedback Loop data in the Tune Model phase**

- The **Tune model** button in the Expert Feedback Loop is always enabled and supports moving utterances from the Expert Feedback Loop Done tab to the model and its test set. Use the **nlu_admin** role to click this button any time you need to tune or retune your model.
- After reviewing utterances, you can push a portion of the feedback data to the default test set of your model. These utterances are then directly added to the **Test utterances** tab of your model, helping you continuously maintain and update your test set with real end user utterances. The system tracks the source of the test utterances for visibility into whether they came from the Expert Feedback Loop or from another source.
- If you click **Tune model** before marking and saving at least 100 utterances, the screen reminds you that model performance increases in quality after you pass the 100-utterance feedback goal.
- As you keep marking and saving feedback data, the progress bar shows the ratio of reviewed utterances (in green) and those still available for review (in white).
- On the **Tune your model** screen, the default **60/40** percentage split applies for your model training set and test set. You can adjust these default values by selecting your own numbers in each of the two (%) boxes. Click the **Tune** button to tune your model based on the percentage values you chose.

> **Note:** If you click the **View feedback** caret, it takes you to an Expert Feedback Loop screen where you can continue reviewing, marking, and saving your feedback utterances.

**Active Learning job**

Scheduled jobs (also known as batch jobs or batch scheduling) are automated pieces of work performed at a specific time or on a recurring schedule. Three things you can do with the Active Learning job:

- Change the repeat frequency interval with which the Active Learning job will be set to run.
- Check when the next scheduled run is set for the Active Learning job.
- Execute the Active Learning job whenever you want (on demand).

Configurable fields on the Active Learning record:

- **Run field** - select one of eight Repeat Interval options for the job: Daily, Weekly, Monthly, Periodically, One, On Demand, Business Calendar:Entry Start, and Business Calendar:Entry End.
- **Repeat Interval field** - enter the number of days you want between now and the next repeat interval for the Active Learning job.
- **Starting field** - click the Calendar icon and choose the day and time for the next Active Learning job interval.
- Click **Update** to save your configurations or click **Execute Now** to start the Active Learning job run.

Detailed information about NLU's Active Learning job can be found in KB article **KB1633901** on the Support portal.

### Issue Auto Resolution (IAR) Tuning in NLU components

Use the NLU Workbench homepage to support Issue Auto Resolution (IAR) tuning in NLU.

**Roles**

- Use the **nlu_admin** or **admin** role to access IAR Tuning in the NLU Workbench.
- Accessing IAR Tuning in the NLU Workbench requires at least the **nlu_feedback_admin** role (the nlu_admin role contains the nlu_feedback_admin role).
- The **virtual_agent_admin** role contains the nlu_admin role.

**IAR Tuning workflow and model behavior**

- Selecting an IAR model name in the list takes you to tuning. For Issue Auto Resolution, you are not taken to a model overview page, so this behavior differs from Virtual Agent or AI Search models in the NLU Workbench.
- IAR admins begin their model tuning journey in the **IAR Admin Console**, then land in the NLU Workbench to tune their ITSM model. If they haven't trained the ITSM model in the console yet, the workflow sends them to the Expert Feedback Loop documentation under the **Boost your model performance** section of the NLU Workbench.
- Unlike the Virtual Agent and AI Search tabs, the IAR tab doesn't use a **Create new model** button. The IAR-ITSM model that IAR admins use is a **prebuilt model**. IAR models **can't be moved using update sets**.

**Exploring the NLU Workbench**

At the top of the NLU Workbench page are three tabs that group **Virtual Agent**, **Issue Auto Resolution**, and **AI Search** models separately. Below those tabs is a list of models colored gray. In the Model column, when you select the caret to the left of the model name, the model changes color from gray to white and opens to show the model's languages; status; usage; model type; number of enabled intents and mapped intents; and the date when the model was last modified or last published.

**IAR tuning goals**

By default, Issue Auto Resolution tuning in NLU Workbench optimizes for **precision**. Depending on your business requirements, you can also tune the model for other objectives. In the **Analyze** step, the tuning goals list enables you to adjust for **Precision**, **Automation**, or **Balance**. As you select an option, the projected **Match rate** and **IAR coverage** percentages change accordingly so you can compare possible outcomes.

- **Precision** - When tuned for precision, the IAR model makes predictions only when its confidence is relatively high. This results in lower error rates, but also in fewer incidents resolved. Precision is the recommended tuning option for the IAR ITSM model, so this option is selected by default.
- **Automation** - When tuned for automation, the IAR model makes predictions at a lower confidence threshold. This results in more predictions, so more incidents are resolved. However, higher error rates are possible.
- **Balance** - When tuned for balance, the IAR model attempts to strike a balance between precision and automation.

**Metrics**

- **Match rate** - the number of Incidents where the intent was predicted correctly, divided by the number of predictions for that intent. This ratio is averaged across all intents except for **NO_INTENT**.
- **IAR Coverage** - the percentage of Incidents that would be resolved because the model was able to make predictions above its confidence threshold. The predictions may contain some errors.

**Using tuning options**

- Select several different tuning options to compare projected results. Depending on the option you select, the system presents scenarios for projected Match rates and IAR coverage rates, and displays how much these rates change according to your selection.
- Review further information in the **Here's a detailed breakdown** section of Analyze. Here you can drill down into results that are specific for each intent in the model.
- Intents are grouped into **mapped** and **unmapped** intents, depending on whether they have been mapped to Virtual Agent topics. After providing feedback in IAR Tuning, to activate some intent-to-topic mappings, expand **See unmapped intents**, then select the **Map more intents** button. This opens the IAR Admin Console.
- When you have decided the optimum tuning option, select the **Save choice** button in the **Learn about tuning goals** window. Then select the **Tune and publish model** button to advance to the next step.

### Intent Discovery components

Use the Intent Discovery application to help identify opportunities for incident deflection. For example, you can use it to identify which Virtual Agent conversations to activate next.

- For applications that consume NLU, such as Virtual Agent and AI Search, Intent Discovery helps you better understand which prebuilt intents you can benefit from, and which custom intents would be useful to create.
- Intent Discovery provides an analysis that you run on historic incident data or other task data. You can also group the run's remaining records into different clusters so you can manually add utterances to NLU intents. You can also use specific clusters to create new intents in a model.
- Intent Discovery is available from the ServiceNow Store (plugin ID **sn_nlu_discovery**). After it is installed and activated, it appears under **All > NLU Workbench > NLU Advanced Features**.

> **Note:** Although organized under NLU Advanced Features in the navigation pane, Intent Discovery is a separate application that is not included when installing NLU Workbench - Advanced Features.

**Intent Discovery report details**

- When **Taxonomy** is selected, the generated report contains intent recommendations against the selected taxonomy. A taxonomy is a prebuilt library of intents in a specific domain. While you don't have access to the underlying intents, when you run Intent Discovery against a specific taxonomy, data that maps to any intent in the taxonomy will be identified.
- **Unmatched records** are the utterances which couldn't match to any intent in the taxonomy.
- **Recommended intents** are the intents which are found from utterances that data was run on.
- The percentage of **Unmatched records (clustered)** are the records that aren't classified (records that don't belong to any of the recommended intents).
- The percentage of unmatched records and the number of recommended intents don't need to match. It's a coincidence if they match.

**Intent Discovery configuration fields (Create new screen)**

- **Data Source** - the table to analyze (for example, Incident [incident]).
- **Filter by** - filter conditions (for example, [Created] [on] [This quarter]).
- **Field to analyze** - the field to run analysis against (for example, Short description [short_description], a highly used string field that references words that can help the system identify an intent).
- **Taxonomy** - tells the system to run classification processing. It has 3 options: **Classification**, **ITSM**, or blank, which defaults as Classification.
- **Cluster unmapped utterances by keywords...** - check box. When checked, the system groups incident records that weren't classified into clusters.
- **Report name** - automatically defaults to Incident <month/day/year>. You can edit the name.

**Analysis status values**

During the analysis, the subsequent status values appear in order: **Preparing to run**, **Work in progress**, **Clustering**, and **Done**. The run can take from 5 minutes to 30 minutes to complete. The fewer the records in a cluster, the less time it takes. Turning clustering off can also speed up the process.

**Tables installed with Intent Discovery**

Several types of components are installed with activation of the **sn_nlu_discovery** plugin, including tables.

| Table | Description |
| --- | --- |
| Discovery Report [sn_nlu_discovery_report] | Reference table for discovery clusters and intents. |
| Discovery Message [sn_nlu_discovery_processed_message] | Contains flexible references to the source record and field that was used for analysis. |
| Discovery Report Trace [sn_nlu_discovery_report_trace] | Contains the information on the utterances added to intents. |
| Discovery Intent [sn_nlu_discovery_intent] | Contains the intents for a report. |
| Discovery Cluster | Contains the clusters for a report. |

## Instructions / Procedures

### Install NLU Workbench - Advanced Features

You can install the NLU Workbench - Advanced Features application (com.snc.nlu.workbench.advanced) if you have the admin role.

**Before you begin**

- Confirm that the application and all of its associated ServiceNow Store applications have valid ServiceNow entitlements. For more information, see Get entitlement for a ServiceNow product or application.
- Review the NLU Workbench - Advanced Features application listing in the ServiceNow Store for information on dependencies, licensing or subscription requirements, and release compatibility.
- NLU Workbench - Advanced Features requires the following plugins to be activated before installation: Predictive Intelligence (com.glide.platform_ml), NLU Workbench - Core (com.glide.nlu), and NLU Workbench (com.snc.nlu_studio).

**Role required:** admin

**About this task:** Tables are installed with NLU Workbench - Advanced Features. For more information, see Components installed with NLU Workbench - Advanced Features.

**Procedure**

1. Navigate to **All > System Applications > All Available Applications > All**.
2. Find the NLU Workbench - Advanced Features application (com.snc.nlu.workbench.advanced) using the filter criteria and search bar. You can search for the application by its name or ID. If you cannot find the application, you might have to request it from the ServiceNow Store. Visit the ServiceNow Store website to view all available apps and for information about submitting requests to the store. For cumulative release notes information for all released apps, see the ServiceNow Store version history release notes.
3. In the Application installation dialog box, review the application dependencies. Dependent plugins and applications are listed if they will be installed, are currently installed, or need to be installed. If any plugins or applications need to be installed, you must install them before you can install NLU Workbench - Advanced Features.
4. Select **Install**.

**What to do next:** The following available ServiceNow Store application is installed separately from NLU Workbench - Advanced Features:

- **Intent Discovery** - Discover user intents from requests, incidents, or cases to help maximize deflection with Virtual Agent and NLU. For more information, see Install Intent Discovery.

### Create a test set (Multi-model Batch Testing)

To create or add to an NLU test set, you can upload a file of test utterances matched with correct intents. Use the test set to assess the performance of your model.

**Before you begin**

- Ensure that the NLU Workbench - Core plugin, NLU Workbench plugin, NLU Workbench - Advanced Features plugin, and Predictive Intelligence plugin are all installed and activated.
- You can use test sets with NLU models for Virtual Agent and AI Search.
- Role required: **nlu_editor**, **nlu_admin**, or **admin**. The editor must be assigned to the model.

**About this task**

- Your CSV or XLSX (Excel Workbook) file should contain a table that pairs your test utterances with the intents you expect for them. Your file can contain up to **10,000 utterances**. Ensure that the file has columns titled "Utterance" and "Expected intent".

> **Note:** For test sets in languages other than English, you must add the `glide.import.csv.charset` system property with the value **UTF-8**. See Import sets properties.

- For the most accurate test results, include utterances the model is likely to encounter from your users, covering all the intents in your model.
- Aim to include about **10%** of test utterances with no expected intents. Including utterances with no expected intent helps assess your model's ability to detect irrelevant utterances that should not have any intent predicted.

> **Note:** To indicate that a test utterance in your file has no expected intent, the value for "Expected intent" should be empty.

**Example test set table**

| Utterance | Expected intent |
| --- | --- |
| Let me have a burger | Order |
| I want to pay | Payment |
| Get me something sweet | Order |
| Is the restaurant open | |
| Something wrong with my payment | Order, Payment |
| Total cost | Payment |

**Procedure**

1. Navigate to **All > NLU Workbench > NLU Advanced Features > Multi-model Batch Testing**.
2. Click **Test sets**.
3. Click **Create test set**.
4. Choose a name for the test set.
5. Choose a language.
6. Click **Select file** and choose a CSV or XLSX (Excel Workbook) file.
7. Click **Create**. Your test set appears in the list.

**What to do next:** Use the test set to run a test on your models. See Test your model or Run a multi-model batch test.

**Adding more utterances to a test set**

After you have created a test set, you can add more utterances to it:

1. When viewing a test set, click **Import utterances**.
2. Select a CSV or XLSX (Excel Workbook) file with your additional utterances to import.
3. Click **Import**. The system adds your utterances to the test set. After importing, rerun any tests that use the test set.

### Run a multi-model batch test

Test multiple Natural Language Understanding (NLU) models against a test set. Evaluate the quality of your models and refine them to improve intent prediction.

**Before you begin**

- Make sure the NLU Workbench - Core plugin, NLU Workbench plugin, NLU Workbench - Advanced Features plugin, and Predictive Intelligence plugin are all installed and activated.
- Have one or more trained models for Virtual Agent or AI Search.
- Have a test set containing test utterances with expected intents. See Create a test set or Test set creation and management.
- Role required: **nlu_admin** or **admin**. When assigned to a model, the **nlu_editor** role can run tests and modify test utterances for that model.

**About this task**

- In Multi-model Batch Testing, you can use a test set that is not the model's default test set.
- You can test up to **ten models** at one time. However, tests with fewer models run more quickly.
- When testing multiple models, your test set must cover at least **25%** of the total intents of all the models. Use test sets that contain utterances the models are likely to encounter in Virtual Agent or AI Search.

> **Note:** If an expected intent in your test set doesn't match any intent in your models, that expected intent and its test utterances are skipped. They aren't counted or displayed in test results.

To test a single model against its default test set, use the **Test and publish your model** phase on the model's overview page.

**Procedure**

1. Navigate to **All > NLU Workbench > NLU Advanced Features > Multi-model Batch Testing**.
2. Click **Run a test**.
3. In the Run new batch test window, select your models from the list.
4. Select a test set from the list.
5. Click **Run**. Your new test shows in the Test results list with a **Testing...** Status.

**What to do next:** When the batch test is finished, its Status changes to **Done**. Click the name of the test set to view the test results. Use the results to adjust and improve your models, then run the test again to assess the performance. Batch testing may affect confidence threshold recommendations. For more information, see NLU model settings.

### Run a Cross-model Conflict Review analysis (example scenario)

This procedure resolves a conflict where two different intents contain the exact same utterance.

1. Navigate to **All > NLU Workbench > NLU Advanced Features > Cross-model Conflict Review**.
2. Select **Run analysis**.
3. In the **Model(s)** field on the "Choose one or two models to analyze for conflicts" screen, select two NLU models for the analysis. In this example, you choose the **demo_hardware_issue** and **demo_it_request** models.
4. Select **Run Analysis**. The Conflict Review screen refreshes to show the analysis, including the two selected models, the counts of Critical and Moderate conflicts under review, the number of completed reviews, and the run date. Pointing to the far right column shows options to rerun the analysis or delete it and start over.
5. In the **Model(s)** column, select your two paired models to drill down into the review. The screen refreshes to show the details (summary of the two chosen models, their latest training dates, the types of conflicts they hold, and the version time stamp). The **0 of 1** count indicates this is the first conflict review created in the instance.
   - If you determine the utterances are fine as they are, click **Ignore**, which marks the review as reviewed and moves on. In this scenario you do not ignore, because intents that share the same utterance are a conflict worthy of review.
6. Select **laptop_not_working**. The #laptop_not_working Intent screen appears showing its current 3 utterances. You decide to delete the "laptop is really slow" utterance from the #laptop_not_working intent.
7. Click the **Delete this utterance** trash can icon. The Confirm Delete screen appears.
8. Select **Delete**. The Confirm Delete screen disappears, and the Utterances count drops from 3 to 2.
9. Select **Train**. A banner appears on the Intent screen, confirming the model is successfully trained.
10. Select **Conflict Review** in the navigator.

**Result:** The Conflict Review list screen appears, showing your conflict review analysis is complete and that it's been reviewed.

### Configure Conversational Interfaces settings for ServiceNow NLU

To help with tracking NLU performance, you must first configure the Conversational Interfaces (CI) settings in Virtual Agent.

1. Navigate to the top of the NLU Model Performance for Virtual Agent landing page and click **Conversational Interfaces Settings**. This takes you to the CI settings page in Virtual Agent.
2. To configure the settings, use the **virtual_agent_admin** or **admin** role. For configuration guidance, see Implement NLU in Virtual Agent and Enable NLU languages in Virtual Agent settings.

### Run an NLU Model Performance analysis

1. Click the **Unsupported utterances** tab. This section shows rows of expandable clusters containing VA utterances where NLU didn't make a topic prediction, or where the VA end-user confirmed that the predicted topic was incorrect.
2. Click **Expert Feedback Loop**. This takes you to the NLU Expert Feedback Loop application where you review and provide feedback on the utterances pulled in from VA.
3. When you leave the Expert Feedback Loop application and return to NLU Model Performance, click the **caret icon** in any cluster to open it. Within the cluster you can see the top most representative VA utterances.
4. Click **Run analysis** or **Rerun analysis**, whichever is available. Each time you run an analysis, the system pulls the most recent VA utterances into the analysis.

### Review your VA chat log utterances (Expert Feedback Loop, example scenario)

1. At the top of the Expert Feedback Loop screen, select a model to review in the **Expert Feedback Loop for** prompt. In this example, you select the **IT Model** model, which has five intents and many utterances within each. The number of utterances to review is shown next to the name of the predicted intent. The intents are listed in the **Predicted intents** column. It's a better idea to complete reviews consecutively in the order the intents first appear (for example, begin with the **ad_password_change** intent).
2. Click the **ad_password_change** intent so it loads its utterances into the **To do** section.
3. Review the 15 utterances in the intent. In this scenario you start by correctly marking the "I want to change my AD password" utterance as a match to the ad_password_change intent.
4. Click **Save feedback**. The system moves the marked utterance to the **Done** section. The count of To do utterances drops from 15 to 14, while the count on the Done section rises from 0 to 1. If you also marked another utterance with the Unsure value and saved it, the count in the **Needs further review** section would rise from 0 to 1.

> **Note:** If you don't know which intent best matches the utterance, mark it with the **Unsure** value to move it to the Needs further review section, giving you time to mark easier utterances first. You can always return to the Needs further review section.

5. Repeat steps 1 through 4 as you move through the remaining intents in the Predicted intents column.

When you finish reviewing the utterances in the predicted intent and click **Save feedback**, the screen refreshes to highlight the next predicted intent in the model.

### Connect an uncategorized utterance to an intent

1. In the **Utterance** column, select an utterance from the list.
2. In the **Corrected Intent** column, search and select an intent and its model from the prompt that you think is the best match for the utterance. (Example pairing: the "Can I trade my ESPP?" utterance with the **401kBenefitsInquiry** intent.)

### Procure additional VA feedback data on demand

1. Use the **nlu_admin** role and navigate to **All > System Definition > Scheduled Jobs > Active Learning**.
2. Click **Active Learning**.
3. Click **Execute Now**.
4. Increase or set the values in the following four NLU system properties:
   - `glide.mlpredictor.option.nlu.activeLearning.va_chat_logs.max_row_limit` - 3000
   - `glide.mlpredictor.option.nlu.activeLearning.label_candidate_table.max_data_size` - 10000
   - `glide.mlpredictor.option.nlu.activeLearning.label_table.max_data_size` - 10000
   - `glide.mlpredictor.option.nlu.activeLearning.label_candidate_table.max_response`

To see how these properties work within the context of other NLU properties, see NLU Workbench properties.

### Configure and use the Active Learning job

1. Using the **nlu_admin** role, navigate to the **All** field and type **sysauto_script.list**, then press the return key. The screen refreshes to show the Schedule page, which lists all scheduled jobs.
2. On the Schedule page, click **Active Learning**. A record for the Active Learning job appears.
3. On the Active Learning record, configure the following fields:
   - In the **Run** field, select one of the eight Repeat Interval options (Daily, Weekly, Monthly, Periodically, One, On Demand, Business Calendar:Entry Start, Business Calendar:Entry End).
   - In the **Repeat Interval** field, enter the number of days between now and the next repeat interval.
   - In the **Starting** field, click the Calendar icon and choose the day and time for the next interval.
   - Click **Update** to save your configurations or click **Execute Now** to start the run.
   - To verify when the next job runs, navigate to the **All** field and type **sys_trigger.list**, then press the return key. The Schedule page appears. Click **Active Learning**. The Schedule Item/Active Learning record appears and populates the **Next action** field with the date and time for the next run.

Detailed information about NLU's Active Learning job can be found in KB article **KB1633901** on the Support portal.

### Access the Analyze step of IAR tuning

Using the **nlu_admin** role:

1. Navigate to **All > NLU Workbench > Models**.
2. Select the **Issue Auto Resolution** tab, then select the model name. The tuning experience opens to step 1 (**Feedback**) initially.
3. Provide feedback, then select the **Analyze** button. Step 2 (**Analyze**) opens.
4. In the section "Here are your tuning options and projected results," using the list "You can tune for precision, automation, or balance," select options to see projected scenarios. You can also select the link **Learn about tuning goals** to open the tuning goals window.

When you have decided the optimum tuning option, select **Save choice** in the Learn about tuning goals window, then select **Tune and publish model** to advance to the next step.

### Create an Intent Discovery report

1. Using the **admin** or **nlu_admin** role, navigate to **All > NLU Workbench > NLU Advanced Features > Intent Discovery**.
2. Select either **Run analysis** or **Find recommendations**.

### Run an analysis on the report (Intent Discovery example)

1. Configure the following fields on the Intent Discovery > Create new screen:
   - **Data Source:** Select the Incident (incident) table.
   - **Filter by:** [Created] [on] [This quarter]
   - **Field to analyze:** Short description (short_description).
   - **Taxonomy:** Select ITSM (options: Classification, ITSM, or blank which defaults to Classification).
   - **Cluster unmapped utterances by keywords...:** Select the check box to group unclassified incident records into clusters.
   - **Report name:** Defaults to Incident <month/day/year>; you can edit it (example: Incident 12/16/2020 - SF Test).
2. Select **Run analysis**. Your report appears on the Intent Discovery screen, showing its status as the analysis begins (Preparing to run, Work in progress, Clustering, Done). This can take from 5 to 30 minutes.

> **Note:** If you want to delete the report and start over, point to the right of the Status column to invoke the Delete report icon.

3. Select the **Name** of your report. The screen refreshes, showing the analyzed incident records and the remaining incident records that were not classified.

### Import recommended intents to new or existing custom models

Before importing intents to an NLU model, ensure you are in the same application scope as the model. See Select an application from the application picker.

1. On the **Records covered by recommendations** section of the screen, select the caret icon on a recommended intent you want to add to a custom model. The details of the recommended intent appear so you can review them.
2. Select **Add to Model**.
3. On the **Select a destination model** screen, choose a model to add the recommended intent to. If you can't find an appropriate model, create a new one, return to the report, and add the new model.

> **Note:** The model you choose must have the same application scope as your current scope.

4. Select **Save**. A banner appears confirming the intent is added to the target model. The recommended intent also appears on the Model screen of the target model.

### Add clustered utterances to an intent and its model

1. On the **Remaining records** section of the intent discovery records screen, select and open a cluster of utterance and short description data you want to add to an intent and its associated model. As you build out new intents from these clusters, click the **Ignore** icon to remove any unwanted intents from the report. The **Show Additional** filter shows or hides the added intents and the ignored intents.
2. Select **Add to intent**.
3. In the **Add this cluster to an intent and model** screen, select an intent and model pair to associate to this cluster.
4. Enter a few utterance examples into the open text field. Select **Add** each time you complete your entry to save it. Use the pencil icon or the trash can icon respectively to edit or delete your entry.
5. Select **Save**. The records screen appears with a banner confirming you added new utterances to the target intent and its associated model. The model and intent pair appears in the **Added To** column.

Use the **Show Additional** filter to show or hide the clusters that have added intents and the clusters that are ignored.

### Run another analysis on your Intent Discovery report

1. Select **Run Again**. The new run begins. When in progress, the option to cancel the run appears. When the run completes, a new banner appears stating you have a new version of the report.
2. Select the new version, then select **Run Again**. The time stamp you selected for the most recent run appears in the **Run date** column of the Intent Discovery screen.

### Install Intent Discovery

You can install the Intent Discovery application (sn_nlu_discovery) if you have the admin role.

**Before you begin**

- Confirm that the application and all of its associated ServiceNow Store applications have valid ServiceNow entitlements. See Get entitlement for a ServiceNow product or application.
- Review the Intent Discovery application listing in the ServiceNow Store for information on dependencies, licensing or subscription requirements, and release compatibility.
- Intent Discovery requires the following plugins to be activated before installation:
  - **Predictive Intelligence (com.glide.platform_ml)** - Enables various Predictive Intelligence and Machine Learning capabilities for training models. See Install Predictive Intelligence.
  - **NLU Workbench - Core (com.glide.nlu)** - Adds NLU Model capabilities. See Activate the NLU Workbench.

**Role required:** admin

**About this task:** Tables are installed with Intent Discovery. For more information, see Components installed with Intent Discovery.

**Procedure**

1. Navigate to **All > System Applications > All Available Applications > All**.
2. Find the Intent Discovery application (sn_nlu_discovery) using the filter criteria and search bar. You can search by name or ID. If you cannot find the application, you might have to request it from the ServiceNow Store. Visit the ServiceNow Store website to view all available apps and for submitting requests. For cumulative release notes, see the ServiceNow Store version history release notes.
3. In the Application installation dialog box, review the application dependencies. Dependent plugins and applications are listed if they will be installed, are currently installed, or need to be installed. If any need to be installed, you must install them before you can install Intent Discovery.
4. Select **Install**.

## Figures, Diagrams & Screenshots

**Figure (p.1191):** ServiceNow documentation page header with the **servicenow** logo (top left). The page introduces "NLU Workbench - Advanced Features" with a bulleted feature list (Multi-model Batch Testing, Cross-model Conflict Review, NLU Model Performance, NLU Expert Feedback Loop for VA, Irrelevance detection in NLU, Issue Auto Resolution Tuning in NLU). The feature names appear as blue hyperlinks. A blue "Note" callout box describes that the Intent Discovery ServiceNow Store application is installed separately. No screenshots on this page - it is text-only with an "Install NLU Workbench - Advanced Features" heading at the bottom.

**Figure (p.1192):** Text-only documentation page covering the "Before you begin" prerequisites and installation procedure. It lists the "Required ServiceNow plugins" (Predictive Intelligence, NLU Workbench - Core, NLU Workbench) and the numbered install steps. A "What to do next" section describes the separately installed Intent Discovery application. No image screenshots.

**Figure (p.1193):** Table screenshot - "Components installed with NLU Workbench - Advanced Features." A two-column table (Table | Description) listing tables installed with the application: NLU Performance Ignored Clusters, NLU Batch Test Result, NLU Conflict Execution, NLU Batch Test Run Definition, NLU Batch Test Run Execution, NLU Conflict Result, NLU Batch Test Utterance, NLU Batch Test Set, NLU Performance Utterance Trace, NLU Conflict Definition, NLU Model Analysis Definition, and NLU Model Analysis Execution. Each row shows the table label, its bracketed internal name, and a description. A blue "Note" callout above the table references the Application Files table.

**Figure (p.1194):** Continuation of the components table showing the final two installed tables ([nlu_analysis_execution] row and ML Label User Feedback [ml_label_user_feedback]). Below it is a "Role installed" table with one row: NLU Feedback Admin [nlu_feedback_admin] and its description (Data labelling Admin role). The remainder of the page is the "Multi-model Batch Testing" text overview (Summary usage, Installation, Test sets). No UI screenshots.

**Figure (p.1195):** "Batch Test" UI screenshot - the Test results list page. A green success banner appears at the top ("Your test set is in/created" style notification). The page shows two tabs (**Test results** / **Test sets**) and a "Run a test" button (top right). A table lists test results with columns including the test set Name, Type (Virtual Agent), number of Utterances, Models predicted, Models, prediction percentages, the run date/created date, and a **Status** column. Several rows show completed tests. The screenshot illustrates how completed and in-progress tests appear at a glance with prediction percentages.

**Figure (p.1196):** "Create new test set" modal dialog screenshot. The modal contains a **Test set name** text field, a **Language** dropdown (showing "English - en"), a **Test set file** field with a "Select file" control, and a small preview area showing the expected two-column format ("Utterance" / "Expected intent"). Cancel and Create buttons appear at the bottom right. Above the screenshot is the "Example test set table" (Utterance/Expected intent pairs such as "Let me have a burger" -> Order). The figure illustrates the test set creation form.

**Figure (p.1197):** Two screenshots on this page. (1) "Test set page with import utterances button" - shows a test set named "HR VA Test" with summary tiles (Utterances 924, Language English-en, Last updated, Status "Uploaded a month ago") and a highlighted **Import utterances** button (outlined in a box). Below is a Test utterance / Expected intent list (e.g., "I need to update my phone number for HR" -> UpdatePhoneNumber). (2) "Import utterances window" - a modal titled "Import a list of utterances paired with correct intents" with a Select file control, a preview of the Utterance/Expected intent columns, and Cancel/Import buttons. The figures illustrate adding more utterances to an existing test set.

**Figure (p.1198):** "Run a new batch test" modal dialog screenshot. The modal is titled "Run a new batch test" with helper text about selecting models. It contains a **Select model(s)** dropdown (showing a placeholder), a **Select a test set** dropdown, and Cancel/Run buttons at the bottom right. The figure illustrates selecting models and a test set to launch a multi-model batch test.

**Figure (p.1199):** "Batch Test" results screenshot - shows the Test results list with a newly running test. A green notification banner appears at top. The table includes a row whose **Status** column reads "Testing..." (with a spinner/progress indicator), demonstrating an in-progress test. Other columns show the test name, models, utterance counts, and percentages. The lower portion of the page is the "Cross-model Conflict Review" text overview (Summary usage, Installation, Roles).

**Figure (p.1200):** "Running conflict analysis" screenshot - the "Conflict Review" application showing the modal/panel "Choose one or two models to analyze for conflicts." A **Model(s)** field is shown with two NLU models selected (rendered as chips/tags such as demo_hardware_issue and demo_it_request) connected by a diagram-like flow, and a highlighted **Run Analysis** button (lower right, outlined). The figure illustrates selecting two models and starting a conflict analysis.

**Figure (p.1201):** Two screenshots. (1) "Conflict review" - the Conflict Review list/summary screen showing the two analyzed models with their Trained on dates, **Conflicts** column (Critical/Moderate tags), and a **Version** dropdown with a time stamp; a "Rerun analysis" button at right; and a "0 of 1" reviewed count. (2) "Reviewing conflict details" - a detail card titled "We found overlapping utterances in these two intents" displaying the two conflicting intent names side by side with their shared/identical utterances, plus an **Ignore** option. The figures illustrate drilling into a detected conflict.

**Figure (p.1202):** Two large screenshots. (1) "Reviewing overlapping utterances" - the Conflict Review screen with the model summary table at top (demo_hardware_issue and demo_it_request rows, Trained on dates, Conflicts Critical/Moderate, Version time stamp 2021-01-19...), filter controls on the left ("Show Moderate," "Hide reviewed"), and a central card "We found overlapping utterances in these two intents" showing **laptop_issue** and **laptop_not_working** intents (the latter highlighted with a purple arrow pointing to it) and the shared utterance "laptop is really slow." (2) "Reviewing the target utterance" - the **#laptop_not_working** Intent screen ("Trained 11 hours ago"), with tabs Utterances (3) / Associated Entities (1) / Settings, Delete/Train/Test/Publish buttons, an Add field, and the three utterances listed: "laptop is really slow," "@laptop display stopped," "@laptop not working." Step 7 instructs clicking the Delete this utterance trash can icon. These figures illustrate locating and targeting the duplicate utterance for deletion.

**Figure (p.1203):** Three screenshots showing the conflict-resolution sequence. (1) "Resolving conflicts" - the #laptop_not_working Intent screen with the trash can (Delete) icon for "laptop is really slow" highlighted (outlined box, far right). (2) "Deleting conflicts" - a **Confirm Delete** modal overlaid on the intent screen asking to confirm deletion, with a Delete button. (3) "Confirmation of deleting an utterance" - the intent screen after deletion, where the Utterances count has dropped from 3 to 2 and "laptop is really slow" is gone; the Train button is highlighted. The figures walk through deleting the conflicting utterance and confirming.

**Figure (p.1204):** "Confirmation of successfully training a model" screenshot - the #laptop_not_working Intent screen displaying a green success banner confirming the model was successfully trained, with the left navigation pane visible (Conflict Review highlighted). Below the screenshot, the page transitions to the "NLU Model Performance" text overview (Summary usage, Installation) including a blue Note callout about the 5,000-VA-utterance minimum and the min_clustering_records property.

**Figure (p.1205):** "Natural Language Understanding (NLU)" Conversational Interfaces Settings screenshot (in Virtual Agent). The form shows NLU configuration controls including an enable/select NLU service area, a primary NLU language dropdown, toggle switches for NLU options, and a **Supported NLU Languages** section listing languages with enabled status and a "set per page" control. The figure illustrates the CI settings page reached via the Conversational Interfaces Settings link. Surrounding text covers configuring CI settings and "Reviewing the user interface (UI)."

**Figure (p.1206):** "NLU Model Performance for Virtual Agent" landing-page screenshot (the main dashboard). It shows the **Performance** tab with Language and Model filters, a Date range control, an "Include translated conversations" switch, and the colored stacked **legend/bar chart** with three scenario columns displaying percentages (e.g., dark blue ~10% correct, brown ~32% no confirmation, dark red ~58% incorrect) each with an information icon. Below the chart is the **Performance Details** table with columns Utterance, Predicted intent, Prediction model, and Prediction outcome. Below the screenshot begins the "Scenario Definitions" table (User confirmed as correct; Topic launched, user confirmed as correct; Topic menu presented, user selected one; User made no confirmation).

**Figure (p.1207):** Two items. (1) The continuation of the "Scenario Definitions (continued)" table (No prediction made fallback topic launched; Topic launched no user confirmation; User confirmed as incorrect; Topic launched user confirmed as incorrect; Topic menu presented user selected none). (2) A filter-interaction screenshot showing the **Language** filter set to "French - fr" and the **Model** dropdown expanded to list all French-language prediction models (e.g., "All models for French (FR)," "HR NLU for VA Copy5 FR," "HR NLU for VA FR," "ITSM NLU for Virtual Agent FR," "NLU Common Entities FR," "Setup Topics Model FR," "test german FR"). The figure illustrates how the Model filter automatically narrows to the selected language's models.

**Figure (p.1208):** Two screenshots. (1) A **Date range** dropdown expanded showing options: Past 30 days, Past 60 days, Past 90 days (highlighted/checked), and Custom range, with the date range shown as "2022-03-19 - 2022-06-17," plus a "Show all bars" toggle. (2) "Reviewing unsupported utterances" - the **NLU Model Performance for Virtual Agent** screen on the **Unsupported utterances** tab, showing rows of expandable clusters of VA utterances and the **Expert Feedback Loop** link/button used to jump to the feedback application. The figures illustrate setting the date range and launching a performance analysis.

**Figure (p.1209):** "Reviewing the top representative utterances in a cluster" screenshot - the NLU Model Performance for Virtual Agent screen with an expanded cluster row revealing its top most representative VA utterances in a list, and **Run analysis**/**Rerun analysis** controls (highlighted at top right). The figure shows the contents of an opened unsupported-utterance cluster. Below the screenshot, the page transitions to the "NLU Expert Feedback Loop" text overview (Summary usage, Installation, Importing expert feedback loop data between instances).

**Figure (p.1210):** Text-only documentation page (Expert Feedback Loop). Covers data persistence scenarios (move/upgrade/clone), "Feedback context and access" (30-day pull of up to 300 utterance samples; the label_candidate_table.max_response property; the 100-utterance tuning threshold), and "Reviewing your VA chat log utterances" (NLU_Match / Mismatch / Unsure values; ~20 utterances per page; Completed reviews vs. Needs further review). No screenshots.

**Figure (p.1211):** "Marking utterances as matched or mismatched to a VA intent" screenshot - the **Expert Feedback Loop for** screen with a model selected at top, the **Predicted intents** column on the left (e.g., ad_password_change with a count of utterances to review), the **To do** section listing utterances with NLU_Match / Mismatch / Unsure radio/toggle controls per utterance, a **Done** count, and a **Save feedback** button. A "Showing" filter is visible. The figure illustrates the core utterance-marking workflow described in steps 1-5.

**Figure (p.1212):** Two screenshots demonstrating the view toggle. (1) The list-view Expert Feedback Loop screen with the **card icon** highlighted (to switch views). (2) The **card view** - utterances rendered as individual cards (groups of five) with left/right page arrows and a **list icon** in the upper right to switch back. The text covers "Using the card view option" and "Changing an utterance value." The figures illustrate the alternative card presentation of utterances.

**Figure (p.1213):** "Active Learning" scheduled jobs screenshot. (1) A list/grid of scheduled jobs (the Scheduled Script Executions list) with columns Name, Active, Class, Updated; the **Active Learning** row is highlighted (outlined box). (2) Implicitly the navigation to All > System Definition > Scheduled Jobs > Active Learning. Step 3 ("Click Execute Now") is referenced. The figure illustrates locating the Active Learning scheduled job to procure additional VA feedback data on demand.

**Figure (p.1214):** Active Learning record screenshot - the **Scheduled Script Execution / Active Learning** form. Visible fields include Name (Active Learning), Active checkbox, Application, Run (Repeat Interval), Repeat Interval (days), Starting (date/time with calendar), and a script field with the job's Run this script code. Update/Execute Now buttons appear in the header. Step 4 lists the four NLU system properties to set. Below the screenshot begins the "Reviewing uncategorized utterances" text with an Important callout. The figure shows the Active Learning job configuration record.

**Figure (p.1215):** "Pairing an uncategorized utterance with an intent and its model" screenshot - the **Expert Feedback Loop for** screen set to **Uncategorized**. It shows the **Utterance** column (To do section, e.g., 120 utterances) and the **Corrected Intent** column with a searchable dropdown to pick an intent and model pair (example: "Can I trade my ESPP?" paired with 401kBenefitsInquiry). A **Done** section (empty), a right-side vertical scroll bar, page arrows, and a **Save feedback** button (deactivated after auto-save) are described. The figure illustrates connecting uncategorized utterances to intents.

**Figure (p.1216):** Two screenshots (Tune model phase). (1) The Expert Feedback Loop for screen with the **Predicted intents** column, a Reviewed/available **progress bar**, and a **Tune model** button. (2) A modal/popup reminding the user that model performance increases in quality after passing the 100-utterance feedback goal (shown when Tune model is clicked before 100 utterances are saved). The text covers pushing feedback data to the model's default test set and tracking the test-utterance source. The figures illustrate the pre-tuning state and the 100-utterance reminder.

**Figure (p.1217):** "Tune your model" screenshot - a modal showing the default **60/40 percentage split** for the model training set and test set, with two editable (%) boxes, a **View feedback** caret, and a **Tune** button. The Expert Feedback Loop predicted-intents panel is visible behind it. Below the screenshot begins the "Using the Active Learning job" text (scheduled jobs overview and the three things you can do with the job). The figure illustrates configuring the train/test split before tuning.

**Figure (p.1218):** Two screenshots (Active Learning job configuration). (1) The **Schedule** page reached via sysauto_script.list - a list of all scheduled jobs with the **Active Learning** row highlighted (Name, columns, Updated dates). (2) The **Active Learning** record/form opened from the Schedule page, showing configurable fields: Run (with the eight Repeat Interval options), Repeat Interval, Starting (calendar widget expanded showing a date picker), and the script body. The figures illustrate steps 1-3 for configuring the Active Learning job's schedule.

**Figure (p.1219):** "Schedule Item / Active Learning" record screenshot - the sys_trigger record (reached via sys_trigger.list) showing the **Next action** field populated with the date and time of the next Active Learning job run, plus Update/Execute Now buttons. Below the screenshot, the page transitions to the "Issue Auto Resolution Tuning in NLU" text (Summary usage and roles, The IAR Tuning workflow, How IAR models differ from NLU models). The figure illustrates verifying the next scheduled run.

**Figure (p.1220):** "Exploring the NLU Workbench" screenshot - the **NLU Workbench** models homepage. Three tabs across the top group **Virtual Agent**, **Issue Auto Resolution**, and **AI Search** models. Below the tabs is a list of models (gray rows) in a **Model** column; expanding a model via the caret reveals its languages, status, usage, model type, number of enabled/mapped intents, and last modified/published date. The figure illustrates the workbench landing experience for IAR tuning. Below it begins the "Issue Auto Resolution tuning options" text.

**Figure (p.1221):** "What do you want to tune for?" modal screenshot (the Learn about tuning goals window). It displays three selectable option cards side by side: **Precision** (marked Recommended, **Match rate 71%**, **IAR coverage 58%**, Change values shown), **Automation** (**Match rate 62%**, **IAR coverage 76%**, Change values), and **Balance** (**Match rate 67%**, **IAR coverage 65%**, Change values). Cancel and Done buttons appear at the bottom right. Below the screenshot, definitions for Precision, Automation, Balance, and Match rate are given. The figure illustrates comparing projected tuning outcomes.

**Figure (p.1222):** Text-only documentation page. Covers "IAR Coverage" and "Using tuning options" (comparing projected results; the "Here's a detailed breakdown" section; mapped vs. unmapped intents; the "Map more intents" button opening the IAR Admin Console; Save choice and Tune and publish model). Then begins the "Intent Discovery" overview (Summary usage, Installation) with a blue Note about Intent Discovery being a separate application. No UI screenshots.

**Figure (p.1223):** "Intent Discovery landing page" screenshot - a welcome/empty-state page featuring an illustration of an astronaut/robot mascot floating beside a rocket (decorative graphic). Centered text invites the user to "See which of your users' queries can be matched to an intent" with a **Find recommendations** call-to-action button (highlighted). A **Run analysis** button is highlighted at the top right. The figure illustrates the Intent Discovery starting screen. Surrounding text covers "Intent Discovery report details" and the start of "Creating an Intent Discovery report."

**Figure (p.1224):** "Selecting data sources in Intent Discovery for a run analysis" screenshot - the **Intent Discovery > Create new** form. Visible fields include **Data Source** (table picker), **Filter by** condition builder ([Created] [on] [This quarter]), **Field to analyze** (Short description), **Taxonomy** dropdown (highlighted, with ITSM selectable), a **Cluster unmapped utterances by keywords** check box, and a **Report name** field, plus a **Run analysis** button. A small flow diagram/illustration accompanies the form on the right. The figure illustrates configuring an Intent Discovery run.

**Figure (p.1225):** Two screenshots. (1) "An ongoing run analysis" - the Intent Discovery list showing a report row whose **Status** column reads "Preparing to run"/"Clustering"/in-progress, with columns for Data Source, Field analyzed, Recommended intents, Unmatched records, Taxonomy, Run date, and Status. (2) "A completed run analysis" - the same list with the report's Status now **Done** and the metric columns populated; the report Name is a link to open it. A Delete report icon is referenced at the right of the Status column. The figures illustrate the analysis progressing from running to complete.

**Figure (p.1226):** Two screenshots (report detail). (1) "Reviewing a recommended intent" - the report detail page titled "Incident 12/16/2020 - SF Test" with summary tiles (e.g., **21%** unmatched/clustered, **73%** records covered by recommendations) and a "Records covered by recommendations" table listing recommended intents with confidence/record counts; one intent is expanded via its caret. (2) "Adding a recommended intent to a model" - the same detail view with an **Add to Model** button highlighted (outlined) on an expanded recommended-intent row. The figures illustrate reviewing and adding a recommended intent.

**Figure (p.1227):** Two screenshots. (1) "Saving a recommended intent to a model" - the **Add this <intent> to a custom model** modal with a **Select a destination model** dropdown and a **Save** button (highlighted). (2) "Confirmation of adding a recommended intent to a target model" - the report detail page ("Incident 12/16/2020 - SF Test," 21% / 73% tiles) showing a success banner confirming the intent was added to the target model. The figures illustrate choosing a destination model and confirming the add.

**Figure (p.1228):** "View a recommended intent in the target model" screenshot - the target model screen (e.g., "Intent Disco custom model") showing the newly added recommended intent now listed among the model's intents, with model-management controls (Train/Test/Publish, tabs). Below the screenshot, the text covers "Adding clustered utterances to an intent and its model" (steps 1-3, the Ignore icon, the Show Additional filter, Add to intent). The figure confirms the recommended intent appears in the destination model.

**Figure (p.1229):** Two screenshots. (1) "Adding a cluster to an intent and model" - a modal titled "Add this cluster to an intent and model" with an intent/model pair selector dropdown listing candidate intents and a free-text field. (2) "Adding paraphrased utterances to an intent" - the same modal with an open text field for entering utterance examples, an **Add** button, pencil/trash icons to edit/delete entries, and a **Save** button. The figures illustrate associating a remaining-records cluster with an intent and adding example utterances.

**Figure (p.1230):** Two screenshots. (1) "Confirmation of adding paraphrased utterances to an intent" - the report records screen ("Incident 12/16/2020 - SF Test," 21% / 73% tiles) with a success banner confirming two new utterances were added to the target intent and model; the model/intent pair appears in the **Added To** column. (2) "Viewing or hiding clusters and ignored clusters" - the same screen with the **Show Additional** filter dropdown expanded (options to show/hide added-intent clusters and ignored clusters). The figures illustrate the post-add confirmation and the Show Additional filter.

**Figure (p.1231):** Two screenshots (re-running analysis). (1) "Selecting the version of the analysis to run" - the report detail ("Incident 12/16/2020 - SF Test," 21% / 73% tiles) with a **Run Again** control and a version selector. (2) "The Cancel Run option" - the report while a new run is in progress, showing a **Cancel Run** option (highlighted). The figures illustrate starting and optionally cancelling another analysis run.

**Figure (p.1232):** Two screenshots. (1) "Selecting the new version of the report" - a version dropdown/selector showing the new report version, with a **Run Again** button. (2) "View the new time stamp of the Intent Discovery report" - the Intent Discovery list with the most-recent run's time stamp now shown in the **Run date** column. Below the screenshots begins the "Install Intent Discovery" text (Before you begin, Required ServiceNow plugins: Predictive Intelligence and NLU Workbench - Core). The figures illustrate selecting and confirming a new report version.

**Figure (p.1233):** Text and table page. Covers the "Install Intent Discovery" procedure (Role required: admin; About this task; numbered install steps) and "Components installed with Intent Discovery." A blue Note callout references the Application Files table. The "Tables installed" table (Table | Description) lists: Discovery Report [sn_nlu_discovery_report] - Reference table for discovery clusters and intents; Discovery Message [sn_nlu_discovery_processed_message] - Contains flexible references to the source record and field used for analysis; Discovery Report Trace [sn_nlu_discovery_report_trace] - Contains the information on the utterances added to intents; Discovery Intent [sn_nlu_discovery_intent] - Contains the intents for a report; Discovery Cluster - Contains the clusters for a report.
