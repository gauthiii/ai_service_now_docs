# Model Management

_Source: ServiceNow Now Assist documentation, pages 1084-1174._

## Overview

Model management is the practice of guiding a Natural Language Understanding (NLU) model through its life cycle in the NLU Workbench. Model management phases lead you through the iterative process of building, testing, and publishing your model. Bringing an NLU model from creation to deployment requires multiple steps, separated into phases. You can return to earlier phases when you want to adjust and maintain your model.

You create NLU models for consumption by the ServiceNow applications **Virtual Agent** or **AI Search**. For **Issue Auto Resolution (IAR)**, a prebuilt model is provided for you to configure.

The phases available for your model depend on the model's application. The system displays a phase, button, or function only when it applies to your model's application. There are three phases on a Virtual Agent model's overview page:

- **Build and train your model**
- **Test and publish your model**
- **Tune your model**

These phases guide you as you build and improve your model.

To use the model management phases, ensure you have all the necessary NLU plugins. Resources to consult:

- Activate the NLU Workbench
- Install NLU Workbench - Advanced Features
- Install Intent Discovery

> **Note:** NLU Workbench - Advanced Features and Intent Discovery are available from the ServiceNow Store. NLU model testing and performance monitoring require **NLU Workbench - Advanced Features**.

### NLU models for AI Search

- There is one prebuilt model for AI Search. You can copy this model as the basis for a custom model.
- The **Show Prebuilt Models** toggle is on by default.
- The **Create new model** button is available.
- The **Boost your model performance** section displays two cards for functions available to AI Search.

To learn more about model content and the model life cycle, see Model management.

## Features

- **Three-phase model life cycle** — Build and train, Test and publish, and Tune your model phases on the model overview, displayed according to the model's application.
- **Multiple model creation methods** — Use a prebuilt model, import data from a CSV, or start from blank.
- **Model content components** — Intents, entities, vocabulary, and a default test set.
- **Five user-defined entity types** — Simple, mapped, pattern, system-derived, and open-ended, in addition to system entities (DATE, TIME, LOCATION, and so on).
- **Vocabulary items and sources** — Regular and pattern vocabulary items, plus list and table vocabulary sources, including pre-built ServiceNow vocabulary for software and hardware terms.
- **Regular expression (regex) support** — Java regex used in pattern entities and pattern vocabulary items.
- **Intent issue detection** — Issue cards for low utterance count, low test utterance count, critical conflicts, and intents needing review.
- **Train and try** — Iterative training plus a Try model test panel with confidence scores and thumbs-up/thumbs-down feedback.
- **Test set creation and management** — A default test set per model, with Test Coverage scoring.
- **Batch testing** — Multi-model Batch Testing for testing one or more models against test sets.
- **Publishing** — Publish a model to make it available to consuming applications such as Virtual Agent.
- **Draft vs. published comparison** — The test panel compares trained (draft) and published model predictions.
- **Irrelevance detection** — Mark utterances as Not relevant so the model avoids predicting an intent for them (Virtual Agent models only).
- **Tune your model** — Expert Feedback Loop incorporates actual user utterances from Virtual Agent chat logs.
- **Model settings** — Edit name, description, business area, ignore-punctuation behavior, and confidence threshold.
- **Portability** — Duplicate a model, export a model as CSV, and add a model to an update set (including parent-child/batch update sets) to move models across instances.

## Functionalities

### Create a model

To create a model for Virtual Agent or AI Search, navigate to **NLU Workbench > Models**. The **Virtual Agent** tab opens by default. Select the appropriate tab for the model you want to create. Before starting, set your scope to the application scope you want for your new model.

You can choose different ways to create a model:

- **Use prebuilt model:** Copy one of the included read-only models, and add content specific to your business.
- **Import data from CSV:** Upload a CSV file that contains training utterances and matched intents.
- **Start from blank:** Go through the process of setting up a new model from scratch.

When you select the **Create new model** button, a modal opens to display your model creation options. Start by selecting one of the icons:

- **Create an NLU model using a pre-built model:** Copy a prebuilt model and its contents as a starting point for your new model.
- **Create an NLU model from a CSV file:** Upload a CSV file containing a list of intents and corresponding utterances.
- **Create an NLU model from blank:** Build a model from scratch and add intents and utterances as you go.

After creating, add content (intents, utterances, entities, and vocabulary) to improve the model's ability to interpret natural language.

### Model management phases

After creating a model, access its management phases by navigating to **NLU Workbench > Models**. Select the tab for your model's application, then the name of the model to open the **Model details** page on the model overview.

- **Build and train your model** — Add and manage content (intents, entities, vocabulary, test set) and train the model with realistic utterances.
- **Test and publish your model** — Test the model to gauge performance and identify areas for improvement, then publish it. Model testing requires the NLU Workbench - Advanced Features store application.
- **Tune your model** — If NLU Workbench - Advanced Features is installed and the model is created for Virtual Agent, this phase uses Expert Feedback Loop to incorporate actual user utterances. If the model is created for Issue Auto Resolution, selecting the model name in the IAR tab takes you to IAR Tuning.

### Duplicating, exporting, and updating

With the NLU Workbench, you can perform the following actions with your models:

- **Duplicate an NLU model:** Copy a model to create a model with the same content (including the default test set).
- **Export an NLU model:** Export a model as a CSV file containing the associated utterances and intents. Share the model or use it to create one.
- **Add an NLU model to an update set:** Add a model and its artifacts to an update set to transfer the model across instances.

### Model content

Models are made up of the following content:

- **Intents:** An action the user wants to do, or wants the application to do.
- **Entities:** Object or context for an action.
- **Vocabulary:** Helps the model understand the range of words in your users' utterances.
- **Test set:** Test utterances and the intents you expect to be predicted, used to assess model performance.

To access model content, navigate to **NLU Workbench > Models**, select the tab for your model's application, then the name of the model. In the **Build and train your model** card, select **View phase**.

### Intents

When your model receives user input, it uses an intent to perform a system action. For example, a user types `I have a critical issue with a slow laptop`. The model matches the utterance to the intent TroubleshootSlowComputer. If the intent is linked to a Virtual Agent topic, it triggers further action.

Intents contain training utterances — examples of user inputs that would trigger the system action. The quality of training utterances affects the accuracy of your model.

Key facts about intents:

- A model can contain up to **750 intents**. However, models with over **300 intents** or **4,500 utterances** (whichever comes first) take longer to train, test, and publish.
- It is recommended to create at least five intents in a model before you start proper testing, because intents can impact each other when tested in a larger environment.
- The **Enabled** column shows whether the intent is active in predictions. An NLU admin can deactivate an individual intent but keep it in the model. After changing the Enabled status, retrain the model.
- If an intent is mapped to a published Virtual Agent topic, you cannot deactivate or delete the intent.

#### Utterances

Each intent in a model has its own utterances. When trained, the model learns to recognize similar utterances from your users and then responds with the matching intent.

Considerations when adding utterances to intents:

- A model must have at least 1 intent, with a minimum of 5 utterances in each intent.
- An intent needs at least 5 utterances to begin training.
- The system supports utterances up to **25 words or 200 characters**. Utterances that exceed that limit fail to return an intent prediction.
- The system supports up to **20,000 utterances** in a single model.
- Models with more than 4,500 utterances take longer to train, test, and publish.
- Use the `@` symbol when adding an utterance to call on a vocabulary source.
- After adding utterances, you can edit, copy, move, or delete them using the icons in the right column. Select multiple utterances using the box on the left and use the **Perform action on selected rows** button.

When you create an intent, the system adds a hashtag to the intent name (for example, `#PayDiscrepancy`).

#### Associated entities

Your model uses entities to provide additional context and meaning when predicting user input. You add entities to the training utterances of your intent. The entities then become associated to that intent, giving you the Associated Intents number.

#### Intent issues

Building large models increases the chance that intents overlap, conflict, or fail to contain enough training utterances. If your model has issues or conflicts, the Intents page displays cards showing the number of intents affected. The cards display these issues:

- **intents have low utterance count:** Intent does not contain the required minimum of 5 training utterances. Also displays when the intent contains fewer than the recommended 15 utterances.
- **intents have low test utterance count:** The default test set does not have enough test utterances for the intent (below the recommended 15).
- **intents have critical conflicts:** Intent contains training utterances that overlap with utterances in another intent.
- **intents need review:** Intent was translated but must be reviewed by an nlu_admin or nlu_editor.

> **Note:** Utterances marked as Not relevant may also conflict with utterances assigned to intents. See Irrelevance detection in NLU.

The issue cards are hidden when:

- The model is a pre-built model.
- The model is in a draft state and not trained.
- The model contains no conflicts.
- A successful conflict report doesn't exist for the latest trained version.
- The NLU Workbench - Advanced Features plugin isn't installed.

#### Reusing intents from prebuilt NLU models

Prebuilt Virtual Agent NLU models provide language understanding for chatbot conversation flows in ITSM, CSM, and HR topics. Each NLU intent in these models maps to a single Virtual Agent conversation topic created in Virtual Agent Designer. The prebuilt models are read-only, but contain validated intents that you can reuse in your NLU models.

The NLU that processes prebuilt-model language is built from a **word corpus of 3 million words**, and is context-aware of general linguistic patterns and both ServiceNow and user-defined vocabularies.

Product documentation references:

- ITSM context: ITSM Virtual Agent.
- HR context: Virtual Agent for HR Service Delivery.
- CSM context: Customer Service Virtual Agent conversations.

To access prebuilt Virtual Agent models in the NLU Workbench, install and activate the relevant plugins using the **admin** role:

| Plugins | Descriptions |
| --- | --- |
| CSM Virtual Agent conversations [com.sn_csm.virtualagent]; Human Resources Scoped App: Virtual Agent Conversations [com.sn_hr_virtual_agent]; ITSM Virtual Agent conversations [com.snc.itsm.virtualagent] | Enables Pre-built Virtual Agent topics, topic blocks, and ServiceNow NLU models for the Customer Service Management, HR Service Delivery, and IT Service Management applications. Requires the Glide Virtual Agent (com.glide.cs.chatbot) plugin to be activated. Automatically activates the NLU Workbench (com.snc.nlu_studio) plugin. |

NLU models and their intents and entities are associated to an application scope. The scope can't be changed later, so verify your target application scope before you begin.

### Entities

Entities provide your model with additional context when receiving user input. Think of entities as the object of the action the user wants to perform. For example, for the utterance `I have a critical issue with a slow laptop`, the system predicts the intent TroubleshootSlowComputer and identifies these entities:

- HARDWARE (entity) - laptop (value)
- urgency (entity) - High (value)

NLU entities fall into two categories:

- **System entities** such as DATE, TIME, and LOCATION are available by default in your instance.
- **User-defined entities** are entities you create to provide context relevant to your business.

There are five types of user-defined entities:

- **Simple entity** — Words or phrases whose value can be extracted, identified based on context.
- **Mapped entity** — Mapped to a vocabulary source or a manually created list of values.
- **Pattern entity** — Created from words/phrases with repeatable patterns (such as email addresses, phone numbers, incident numbers) using regex.
- **System-derived entity** — Derived from a default system entity such as date, time, duration, or location.
- **Open-ended entity** — Tells the model to focus on the context of the entity rather than the entity itself.

All entities are reusable across other NLU models, but you must add them to a training utterance for each model to use them.

#### Model availability

When you create an entity, you can choose to make it available for reuse by other intents in the model by selecting the **Model availability** box. If you check the box, the entity shows in the **Associated Entities** tab. If you didn't select it when creating the entity, you can edit the entity afterward. On the Model details page, select **Entities**, select the entity name to open the entity details page, then select the **Settings** tab.

#### Entity fields (mapped entity form)

| Field | Description |
| --- | --- |
| Entity Name | Name for the entity. |
| Type | Type of entity. |
| Model availability | Select this option if you want this entity to be included in all intents in your model. |
| Source | Source of the entity values. |
| Provide values for this entity | Values used to provide context for the model. |

#### Mapped entity source options

- **Manual list of values:** Manually enter a list of values for the entity (for example, a `priority` entity with values High, Medium, and Low).
- **Table vocabulary source:** Use a ServiceNow table that has the values you want (for example, `@Location` with city and country values).
- **List vocabulary source:** Use a list you define when you don't have a suitable ServiceNow table (for example, `@mouse` with values for various hand-held computer devices).

#### System-derived entities

System entities (DATE, TIME, DATE_TIME, and so on) are enabled by default and appear in the Entities section of the Model screen. You can disable and re-enable them by clicking **Enable**. System-derived entities extend system entities to extract more information (for example, `startdate` and `enddate` derived from DATE, or `FromLocation` and `ToLocation` derived from LOCATION). When creating one, set the **Parent Entity**.

#### Open-ended entities

When you mark a word or phrase as open-ended, the system skips the entity and predicts the intent from the context that precedes or follows the entity. Constraints:

- You can use only **one open-ended entity per intent**.
- You can't annotate a vocabulary source (referenced by `@vocab_source`) as an open-ended entity. A vocabulary source can only be annotated as a simple entity or a mapped entity.

#### Regular expressions in entities

Pattern entities use regular expressions (regex) to match any pattern of text, such as the format of an email address, phone number, or incident/case ID.

> **Note:** ServiceNow uses and supports **Java regex** exclusively, not other vendor options such as Perl regex.

Regex examples:

| Type | Format | Regex code |
| --- | --- | --- |
| Knowledge base article | KB1234567 | `KB\d{7}` (KB = knowledge base record, `\d{7}` = 7 digits) |
| Case number | CS1234567 | `CS\d{7}` (CS = case record, `\d{7}` = 7 digits) |
| Email address | name@servicenow.com | `\b[a-zA-Z0-9&*/_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\b` (supports name@servicenow.com and name@servicenow.co.in) |
| Phone number (US) | 555-123-4567 | `\d{10}|(?:\d{3}-){2}\d{4}|\(\d{3}\)\d{3}-?\d{4}` (supports 5108882062, 510-888-2062, (510)888-2062) |

Regex resources (external links): Java Regular Expressions, Java Regular Expression Tester, Pattern (Java Platform SE7), Java regex match abbreviations.

### Vocabulary

Vocabulary helps your model handle the various words and phrases it may encounter from your users. Vocabulary items are mapped to synonyms that you provide, for intent prediction.

#### Vocabulary item types

| Type | Definition |
| --- | --- |
| Regular | A word or phrase that is not commonly known, such as a business or industry-specific term or acronym. Regular vocabulary is case insensitive, so all case variations are captured. See Create a regular vocabulary item. |
| Pattern | A regular expression (regex) that can capture specific formats such as email addresses and phone numbers. See Create a pattern vocabulary item. |

#### Vocabulary sources

Vocabulary items and vocabulary sources differ in usage:

- Use a **vocabulary item** for an individual word, phrase, or pattern that can easily be mapped to a single synonym.
- Use a **vocabulary source** to reference a ServiceNow table or list so the values can all be replaced by the single synonym you define. Vocabulary sources can be reused across all your NLU models.

Once you create and save these sources, use the `@` symbol to specify them in training utterances. You can also use these sources as entity values.

#### Vocabulary usage in relation to an intent

> **Note:** In NLU vocabulary, the synonym replaces the vocabulary that appears in the utterance.

Example with intent **OrderSoftware**:

| Utterance | Issue and Solution |
| --- | --- |
| "I need to access sfcrm" | Issue: the system doesn't recognize the acronym `sfcrm`, so can't accurately predict the intent. Solution: Add `sfcrm` as a regular vocabulary item, and provide a synonym such as `CRM software`. |
| "I need to install Word" | Issue: The term `word` is very common and does not necessarily indicate a software product. Solution: Create a pattern vocabulary item with a regex for capitalized `Word`, so the system can recognize it as a software product. (To extract the specific software name for a Virtual Agent topic, annotate it as an entity.) |

Use a single word or short phrase as a synonym for best results. You can map multiple vocabulary items to one synonym. Do not map one vocabulary item to multiple synonyms.

#### Regex example for a pattern vocabulary item

To identify the acronym `IT` and map it to the synonym `information technology`: regular vocabulary items are case-insensitive and would match both `IT` and `it`, so use a pattern vocabulary item. The pattern `\bIT\b` uses a word boundary marker `\b` to avoid matching ITSM or JIT, and the default case sensitivity of pattern vocabulary items means `\bIT\b` would not match the common word `it`.

Regex details: turn off case sensitivity using `(?i)`, and end that mode using `(?-i)`. For example, `(?i)te(?-i)st` should match both `test` and `TEst`, but not `teST` or `TEST`.

#### List vocabulary source fields

| Field | Description |
| --- | --- |
| Handle | Name for the vocabulary source. Used to refer to it in an utterance. |
| Language | Language of the vocabulary source. Synonym must be in the same language. |
| Synonym | Word or phrase the model uses during intent prediction. Choose a commonly-occurring word in the same language as your model. |
| Enable Fuzzy Matching | Check this box if you want the items on the list to match when a user utterance has slight misspellings. |
| Make case sensitive | Check this box to make the values in the list case sensitive. Utterances with wrong cases won't match. |

> **Note:** During intent prediction, the synonym you provide replaces the value. During entity prediction, the actual value is used as the entity if the actual value or one of the alternate values is detected in the utterance.

#### Table vocabulary source

Add a ServiceNow table to be used as a vocabulary source. Select one or more source fields, then provide a synonym. The **Reference** field is not supported as a source field. When you create and sync a table vocabulary source, the values from the table are extracted and a vocabulary source is created in the NLU Service.

Table vocabulary source configuration includes:

- **Table, Handle, Synonym** — The table to reference, a system-generated handle (such as `@Location`), and a synonym (such as `Location`).
- **Field name / Options** — Select fields to refer to (such as Country and City). Click **Options** and select **Use this field to look up values** to allow either field's value in an utterance. You can use multiple comma-separated values in this field (for example, NYC, New York, New York City).
- **Fields can appear together** — Typically used in an NLU Search model, where users can enter words next to each other to find a record (for example, "Pierre Development").
- **Language** — Language of the source.
- **Filter by** — Use the condition builder to filter values in the source table.
- **Refresh** — Schedule (for example, Every 7 days) for getting new values from the table.
- **Enable Fuzzy matching** — Allows matching even with slightly misspelled words or partial words. May return false matches; use sparingly and test the model first.
- **Make case sensitive** — If fuzzy matching is not enabled, makes values case sensitive.

> **Note:** Do not create multiple vocabulary sources that reference the same table and fields, as this causes confusion and interferes with prediction quality.

You don't need to retrain the model after updating a table vocabulary source.

#### Sync a table vocabulary source

When you reference a vocabulary source in an utterance, it pulls the values at the time the model is trained. You can select a schedule to automatically refresh the vocabulary values used by NLU, and you can also manually sync.

> **Note:** If an utterance references a table vocabulary source that has never been synchronized, the model fails to train. Check the source's current status and sync manually if **Never synced**.

The **Last refresh** and **Current status** columns reflect the current status of the vocabulary source. For sync errors, see article KB1588239 in the Now Support Knowledge Base.

#### Pre-built vocabulary

Your NLU models contain pre-built vocabulary settings for software and hardware terms, whether expressed in slang or professional usage, and can also recognize product misspellings. When the system recognizes a pre-built vocabulary item, the term has a **blue line** under it. When you click the word, a window appears with two options:

- A pre-built suggested definition for the word.
- An option to add a synonym.

If you select the first option and click **Confirm**, the system uses the pre-built suggested definition and the blue line disappears. If you select the second option, enter a synonym, and click **Confirm**, the word and synonym are added to the model vocabulary. Selecting either option and clicking **Ignore** removes the blue line and leaves the word as it was.

### Test set

Each NLU model contains a default test set used to evaluate the model's performance. Initially the test set is empty, ready to be populated. Add test utterances and their expected intents to build the test set.

Test utterance sources:

- **Manual** — Added manually (typed) or imported from a CSV file or other models.
- **Expert Feedback** — Added from Virtual Agent chat logs via the Expert Feedback Loop feature.

#### Access your default test set

- Navigate to **All > NLU Workbench > Models**, select the tab and model, find the **Build and Train your model** card, select **View phase**, then select the **Test set** tab.
- Navigate to **All > NLU Workbench > Models**, select the tab and model, then select the **Test Coverage** tile.
- Navigate to **All > Multi-model Batch Testing > Test sets** tab and find your model. Default test sets are labeled as **Default**.

#### Test Coverage

The **Test Coverage** score is the percentage of a model's enabled intents that have test utterances in the default test set. Before testing, ensure at least **60% coverage**, with at least **5 test utterances per intent**, so the system can provide an optimal confidence threshold during batch testing. The higher the score, the more accurate the performance testing results.

Aim to have about **10 percent** of a model's test utterances marked as "not relevant" (no intent associated). This helps assess how the model handles irrelevant utterances.

#### Characteristics of default test sets

- When an instance is upgraded, default test sets are created for any existing models that don't already have them.
- When you copy a model using **Duplicate this model**, the original's default test set is copied into the new model.
- The utterances in the test set shouldn't be the same as the utterances in the training set.
- Default test sets can't be deleted separately from their models.
- Test set utterances should be in the same language as their model.
- Test sets are available for Virtual Agent or AI Search models.

#### Downloading or moving default test sets

- Default test sets can be separately downloaded in CSV format using **Download test set** (test utterances and expected intents, but not the sources).
- Default test sets can be moved with update sets (including test utterances, expected intents, and sources).
- The **Export model as CSV** function in the All existing models table does **not** include the default test set.

### Test panel (Train and try)

Access the test panel by clicking **Train model** or **Try model** in the Build and train your model phase. Training incorporates new content into your model. With **Try model**, you can manually enter individual utterances to test what intents the model predicts. You can also provide feedback (thumbs up/down) on predictions to help improve intent prediction.

The mid-conversation responses of Dialog Acts can't be tried or tested in NLU Workbench.

#### Test panel feedback

When a model is trained and tested for an utterance and returns an intent prediction, you can provide a thumbs up or thumbs down rating. Marking a different intent prediction as correct adds the utterance to the corrected intent. All other feedback is captured for continual learning. This feature requires the **nlu_admin** role; NLU editors can also access the test panel if assigned to it by an NLU admin.

When you click the **Thumbs Down** icon, the **Provide feedback to improve this prediction** section expands with options:

- **Its correct intent should be:** — Choose a more appropriate intent for the test utterance.
- **I'm not sure what the correct intent is** — The system shows the next best intent predictions.
- **No intent should be predicted** — When chosen and saved, the utterance is removed from all intents it is part of.
- **Exclude this model's predictions for this utterance** — Directly notify the system that the utterance is irrelevant to the model, then click **Save changes**.

Your feedback data is stored in the `ml_labeled_data` table, which is also used by other ServiceNow products and can house multiple sources (such as Virtual Agent chat logs).

### Test and publish your model

Test your Virtual Agent or AI Search model against its default test set to see how the model responds.

> **Note:** Testing requires the **Multi-model Batch Testing** feature, available with the **NLU Workbench - Advanced Features** application from ServiceNow Store.

The Test and publish your model phase opens on the **Overview** page by default, with buttons for **Run new test** and **Publish model**. Overview provides information about a previous test run with bar charts summarizing results. View earlier runs by selecting from the **Test run date** list. To drill into the results table, select the **Detailed results** tab; each test utterance is listed with its prediction.

#### Understanding test results

The bar chart shows the prediction percentages for correct, correct among multiple, missed, and incorrect:

| Percentage | Description |
| --- | --- |
| Correct | The percentage of utterances for which your model correctly predicted the intent. When the model predicts no intent for utterances marked as Not relevant, that result is counted as Correct. |
| Correct among multiple | For utterances that had more than one intent predicted. The percentage of utterances for which the model correctly predicted the intent(s), but also predicted intents that did not belong to the utterance. |
| Missed | The percentage of utterances for which your model did not predict an intent, even though there was an expected intent. |
| Incorrect | The percentage of utterances for which your model predicted an intent that was not correct. |

Testing can affect the model's confidence threshold. The Overview tab also displays a list of the top 5 incorrect intents and the top 5 missed intents.

#### Publish model

The **Publish model** button makes the current version of the model available to other applications such as Virtual Agent.

> **Note:** If the model has not been trained, the **Publish model** button is unavailable. Return to the Build and train your model phase to train the model before publishing.

Button states: If the model hasn't been tested, the button is white; if tested, the button is green; if the last trained model is already published, the button is unavailable.

#### Multi-model Batch Testing

With Multi-model Batch Testing, you can test against other test sets, test multiple models at once, and see your test results. Navigate to **NLU Workbench > NLU Advanced Features > Multi-model Batch Testing**.

### Compare draft and published versions

When you try an utterance against an NLU model:

- If the model is trained and never published, the test panel shows only **trained model** results.
- If the model is trained and published, the test panel shows only **published model** results.
- If you've made changes to a published model and trained it, the panel shows both **trained model** and **published model** results for comparison.

### Irrelevance detection in NLU

The Irrelevance detection feature improves the prediction accuracy of NLU models by training them to ignore certain utterances. To prevent the model from predicting an intent when it should not, mark utterances as **Not relevant**. These are included in model training. When the published model encounters similar utterances, no intent is matched or predicted.

**Roles / availability:** Use the **nlu_admin** or **admin** role to access Irrelevance Detection. The **nlu_editor** role can also access it but must be assigned to a model to edit that model's contents. Irrelevance Detection is available for **Virtual Agent models only**.

Navigation: **All > NLU Workbench > Models** (Virtual Agent tab) > scroll to **Boost your model performance** > scroll horizontally to the **Keep chats focused** card > select **Go to irrelevance detection**. The instance URL for this feature is `<instance-name>.servicenow.com/now/nlu-workbench/irrelevant-utterances`.

**Methods for adding utterances to Irrelevance detection:**

- **Virtual Agent chat log** (via Expert Feedback Loop) — Mark an utterance as Not relevant; the system asks whether it should be irrelevant to a particular model or to all models. Source = **VA Chat Logs**.
- **Manual input** — Type your utterance in the Type utterances here field, then select **Add**. Source = **Manual**.
- **Importing** — When importing training utterances from a CSV or XLSX file, indicate irrelevant utterances by leaving the **Intent** column empty. Source = **Manual**.

**Behavior of irrelevant utterances:**

- Two types: associated to one specific model, or irrelevant to any model.
- A model can have a maximum of **200 irrelevant utterances** associated to it.
- When a model is submitted for training, at most 200 irrelevant utterances are submitted: first those directly associated to that model, then those designated not relevant to any model.
- If a model has 200 irrelevant utterances and a new one is added, the oldest is dropped.
- A model cannot have more irrelevant utterances than normal training utterances.

**Conflict review:** Irrelevant utterances take precedence over training utterances. Because they impact predictions, they are displayed as conflicts when they overlap with training utterances. Conflicts are highlighted in two locations:

- The **Cross-model Conflict Review** module (available with NLU Workbench - Advanced Features).
- The **Conflicts** tab of an intent.

For the purpose of reviewing conflicts, irrelevant utterances are displayed as though they are in their own intent, named **NO_INTENT**. Irrelevant utterances cannot be edited or deleted on the conflict page; copy them to the Irrelevance detection page to modify or delete.

Additional behavior:

- When testing models against test sets, results are considered Correct if no intent is predicted for an irrelevant utterance.
- Utterances marked Not relevant can be re-assigned later (for example, to a new intent) via the **Corrected intent** column; select **Save feedback** and retrain.
- Utterances marked as not relevant to any model are submitted as part of the training data for each model.
- Model training is necessary to incorporate Not relevant utterances. Training any model adds newly marked utterances to all models.
- Irrelevant utterances should have content different from utterances associated to an intent.

### Tune your model

The **Tune your model** phase on your model's overview takes you to the **NLU Expert Feedback Loop** feature, which collects data from Virtual Agent chat logs and provides it to you for feedback.

> **Note:** The ServiceNow Store application **NLU Workbench - Advanced Features** must be installed to view Tune your model. The Virtual Agent plugin is also required.

When the Expert Feedback Loop has feedback waiting for your review, **You have utterances that need feedback** is highlighted on the card.

### NLU model settings

Access settings by navigating to **All > NLU Workbench > Models**, selecting the tab and your model's name, then the **Model settings** (Settings) tab.

**Model settings (upper section):** Change the model's **name**, **short description**, and **business area**. You **cannot** change the model's **language**, **purpose**, or **scope**. By default, the **Ignore punctuation** check box is active, which reduces variance between predicted intents and confidence scores for utterances with slightly different punctuation. Keep it active for best results.

**Model threshold settings:** A threshold is a confidence score represented by a percentage. The confidence threshold determines what intents will be predicted for a given utterance. For example, if the model threshold is 65%, an intent is predicted only when it has a confidence score of at least 65%. A threshold too low may increase false positives; a threshold too high may filter out intents you want predicted. There are two types of model threshold settings (the page shows **Automatic (Optimal)** and **Manual** options).

### Roles summary

| Action | Role(s) |
| --- | --- |
| Create a model (blank, CSV, prebuilt) | nlu_admin or admin |
| Duplicate a model | nlu_admin or admin |
| Export a model as CSV | nlu_editor, nlu_admin, or admin |
| Add a model to an update set | admin |
| Delete a model | admin or nlu_admin |
| Create an NLU intent | admin or nlu_admin |
| Import an NLU intent | nlu_editor, nlu_admin, or admin |
| Resolve intent issues | nlu_admin or admin (nlu_editor when assigned to the model) |
| Create entities (simple, mapped, pattern, system-derived, open-ended) | nlu_editor, nlu_admin, or admin (editor assigned to model) |
| Import entities | nlu_editor, nlu_admin, or admin (editor assigned to model) |
| Create regular / pattern vocabulary item | nlu_editor, nlu_admin, or admin (editor assigned to model) |
| Create a list vocabulary source | admin, nlu_admin, or nlu_editor |
| Create / sync a table vocabulary source | admin or nlu_admin |
| Train and try a model | nlu_editor, nlu_admin, or admin (editor assigned to model) |
| Test a model | nlu_editor, nlu_admin, or admin (editor assigned to model) |
| Publish a model | admin or nlu_admin |
| Compare draft and published versions | nlu_editor, nlu_admin, or admin (editor assigned to model) |
| Access Irrelevance Detection | nlu_admin or admin (nlu_editor assigned to model to edit) |

### Tables and resources referenced

- `sys_nlu_model` — NLU model records (Display name vs. system-given Model name).
- `sys_nlu_intent` — NLU intent records (the `origin` field references the source intent/model).
- `sys_update_set` — Update set records (parent/child, Batch Base, State, Application scope columns).
- `cmn_location` — Example ServiceNow Location table used as a table vocabulary source.
- `ml_labeled_data` — Stores test panel feedback data, shared with other ServiceNow products.

### Plugins commonly required

NLU Workbench plugin, NLU Workbench - Core plugin, NLU Workbench - Advanced Features plugin, NLU Common Model plugin, and Predictive Intelligence plugin (specific procedures require different subsets, as noted in each procedure's prerequisites). Glide Virtual Agent (com.glide.cs.chatbot) is required for prebuilt Virtual Agent models.

## Instructions / Procedures

### Create an NLU model from blank

**Before you begin**

- Ensure the NLU Workbench plugin, NLU Workbench - Core plugin, and Predictive Intelligence plugin are installed and activated.
- You can create NLU models for Virtual Agent and AI Search.
- Role required: nlu_admin or admin.

**Procedure**

1. Set your scope to the application scope you want for your model.
2. Navigate to **All > NLU Workbench > Models**. The Virtual Agent tab opens by default.
3. Select the tab for the type of model you want to create, such as AI Search.
4. Select the **Create new model** button.
5. In the **Add some details** window, select the **Start from blank** button.
6. In the define details page, enter a unique **Name** and **Short description**. (Example: `HR Model for Virtual Agent` for the name, `Natural language for Human Resources user requests` for the description.)
7. Select the language and purpose from the drop-down lists. (Example: English and Virtual Agent.)
8. Optional: Select a business area for your model.
9. Select **Next**. Your model starts building. When complete, select **View model** to open the Model details page.

**What to do next:** Your new model contains no content. Select **Add content** to begin adding intents, entities, and vocabulary. Add test utterances and intents to build the default test set.

### Create an NLU model from a CSV file

**Before you begin**

- Ensure the NLU Workbench plugin, NLU Workbench - Core plugin, and Predictive Intelligence plugin are installed and activated.
- You can create NLU models for Virtual Agent and AI Search.
- Role required: admin or nlu_admin.

**Sample CSV setup** (two columns: Intent, Utterance), for example:

| Intent | Utterance |
| --- | --- |
| schedule | when is my next meeting |
| schedule | what time is my next meeting |
| schedule | schedule a meeting for 11am |
| schedule | cancel my 4:30 meeting |
| holiday | when is the next holiday |
| holiday | do we get Black Friday off |
| timeoff | request friday off |
| timeoff | how many PTO days do i have |

Notes for CSV import:

- A model needs at least 1 intent with a minimum of 5 training utterances in each intent. For optimum performance, aim to have 15 training utterances per intent.
- Utterances should not contain a comma.
- Importing with a CSV file does not preserve entities. Annotate utterances as needed after importing.

**Procedure**

1. Set your scope to the application scope you want for your new model.
2. Navigate to **All > NLU Workbench > Models**. The Virtual Agent tab opens by default.
3. Select the tab for the type of model you want to create, such as AI Search.
4. Select the **Create new model** button.
5. In the **How do you want to create your model?** window, select **Import data from a CSV**.
6. In the **Add some details** window, add the **Name** and **Short description**. (Example: `Calendar Model` and `Model for answering and performing calendar requests`.)
7. Select the language and purpose from the drop-down lists. (Example: English and Virtual Agent.)
8. Select **Next**.
9. On the **Import CSV** screen, select **Select file**.
10. Choose the CSV or XLSX (Excel Workbook) file from the pop-up.
11. Select **Next**. Your model starts building. After completion, select **View model**.

**What to do next:** Add intents and training utterances, then entities and vocabulary, then test utterances and intents.

### Create an NLU model using a pre-built model

**Before you begin**

- Ensure the NLU Workbench plugin, NLU Workbench - Core plugin, and Predictive Intelligence plugin are installed and activated.
- You can create NLU models for Virtual Agent and AI Search.
- Role required: nlu_admin or admin.

Your new model contains intents, entities, and vocabulary from the prebuilt model, plus an empty default test set.

**Procedure**

1. Set your scope to the application scope you want for your new model.
2. Navigate to **All > NLU Workbench > Models**. The Virtual Agent tab opens by default.
3. Select the tab for the type of model you want to create, such as AI Search.
4. Select the **Create new model** button.
5. In the **How do you want to create your model?** window, select **Use prebuilt model**.
6. On the **Add some details** window, fill in the **Name** and **Short description**. (Example: `Human Resources VA Model` and `Virtual Agent Model for responding to HR Requests`.)
7. Select the language and purpose from the drop-down lists. (Example: English and Virtual Agent.)
8. Optional: Select the business area for the model. (Example: HR.)
9. Click **Next**.
10. Select the prebuilt model from the drop-down list. (Example: HR NLU for VA.)
11. Select **Next**.
12. On the **Select intents** screen, select the prebuilt intents to add to your model. (You can select all by checking the **Intent** box at the top of the list.)
13. Select **Next**. Your model starts building. After completion, select **View model**.

### Duplicate an NLU model

**Before you begin**

- Ensure the NLU Workbench plugin, NLU Workbench - Core plugin, and Predictive Intelligence plugin are installed and activated.
- Identify an existing NLU model to copy from with the language and purpose you want.
- Role required: nlu_admin or admin.

**Procedure**

1. Set your scope to the scope of the model you want to create. After creation, these settings cannot be changed: language, purpose, scope.
2. Navigate to **All > NLU Workbench > Models**.
3. On the far right column of the model list, select the **More options** menu for the model you want to duplicate.
4. Select **Duplicate this model**.
5. In the **Duplicate this Model** window, enter a name and description. (Example: `NLU for Access Requests Copy1`.)
6. Click **Duplicate**. The system duplicates the model and the Model details page loads for your new model.

To duplicate an entire model group or one of the models in a group, see Multilingual model management.

### Export an NLU model

**Before you begin**

- Ensure the NLU Workbench plugin, NLU Workbench - Core plugin, and Predictive Intelligence plugin are installed and activated.
- Role required: nlu_editor, nlu_admin, or admin.

Exporting creates a CSV file containing utterances and matched intents from the Utterances tab for each intent. The file does **not** contain the sources of the utterances, and does **not** transfer entities or vocabulary. To export all model data, use an update set.

**Procedure**

1. Navigate to **All > NLU Workbench > Models**. The Virtual Agent tab opens by default.
2. Select the tab for your model's application and find your model in the list.
3. Scroll to the far right column of your model's row and select the more options menu.
4. Click **Export model as CSV**. The model CSV file downloads to your browser.

### Add an NLU model to an update set

**Before you begin**

- Ensure the NLU Workbench plugin, NLU Workbench - Core plugin, and Predictive Intelligence plugin are installed and activated.
- Applies to NLU models for Virtual Agent and AI Search.
- Role required: admin.

The target instance must already have the same scope as the model's scope in the source instance. Adding a model to an update set includes: model content (intents, utterances, entities, annotations, vocabulary, and the default test set), associated vocabulary sources, the corresponding latest active ML solution, ML model artifacts, and the ML solution and definition (last three runs, provided one of them was successful).

For optimum portability, add your NLU model to a new, dedicated update set rather than a system Default update set. If the model contains records from multiple scopes, its update set must have a parent-child (batch) structure. When models are moved using update sets, their training and publishing state remains the same after transfer (no retraining or republishing required).

**Procedure**

1. Select **All** and enter `sys_nlu_model.list` into the navigator.
2. Select the **Model Name** of the model. (The Display name is what you gave the model; the Model name is system-given.)
3. Optional: If Global is your current application, follow the prompt at the top to edit the record.
4. In the **Related Links** section, click **Add model to current update set**. If all records are in one scope, the model is added (found in `sys_update_set`). If the designated scope is Default, the system displays an error; continue with the following steps.
5. If the system displays the error "You are attempting to add a record to the system default update set," select the **New Local Update Set** link in the error banner to create a non-Default update set. (For a parent-child update set, the parent is created first in the model's scope.)
6. For the new update set record, provide a name, review values including Application scope, then select **Submit and Make Current**. The screen re-opens to the model's record in `sys_nlu_model`.
7. In the model's record, select **Add model to current update set** under Related Links. (When the model's records are in multiple scopes, this creates child update sets with Global scope.)
8. If the model is in a non-Global scope: In the `sys_update_set` table, locate the parent (value `(empty)` in the Parent column) and its child update sets (parent's name in the Parent column, Global in the Application column; both share the same Batch Base value).
9. Open the parent's record and set the **State** field to **Complete**. Select **Yes** to confirm. This sets the parent and all child update sets to Complete.
10. To migrate the update set file, select **Export Update Set Batch to XML** in the parent's record.

**What to do next:** On the target instance, navigate to **Retrieved Update Sets** and select **Import Update Sets from XML**. Open the parent and select **Preview Update Set Batch**. If a referenced record is missing on the target, you may select **Accept remote update** on failed records to commit anyway.

### Delete an NLU model

**Before you begin:** Role required: admin or nlu_admin.

You cannot delete a model if it is pre-built or contains at least one intent mapped to a Virtual Agent topic.

> **Warning:** Deleting a model cannot be undone.

**Procedure**

1. Set your scope to the scope of the model you want to delete.
2. Navigate to **All > NLU Workbench > Models**.
3. On the far right column of the model list, select the **More options** menu for the model.
4. Select the option to **Delete this model**.
5. Select the check box to acknowledge that all references to this model will be deleted.
6. Select **Delete model**. The system deletes your model and reloads the page.

### Create an NLU intent

**Before you begin**

- Ensure the NLU Workbench plugin, NLU Workbench - Core plugin, NLU Workbench - Advanced Features plugin, NLU Common Model plugin, and Predictive Intelligence plugin are installed and activated.
- Ensure you are in the same application scope as your model.
- You can create intents for Virtual Agent and AI Search models.
- Role required: admin or nlu_admin.

Do not include unrealistic terms (such as "OrderLaptop" or "sfsdfasdfas") in training utterances. Training utterances and user utterances have a limit of 25 words or 200 characters.

**Procedure**

1. Set your application scope to your model's scope.
2. Navigate to **All > NLU Workbench > Models**. The Virtual Agent tab opens by default.
3. Select the tab for your model's application, then select the model name. (Example: HR Model for Virtual Agent.)
4. In the **Build and train your model** card, select **View phase**.
5. Select **Intents**.
6. Select **New Intent**.
7. In the **Create an intent** window, add a name and description for the intent. (Example: `PayDiscrepancy`.) When you create an intent, the system adds a hashtag to the intent name.
8. Select **Add intent**. The intent screen appears with sections for utterances, associated entities, and settings; the intent draft status appears in the upper right corner.
9. In the **Utterances** tab, enter training utterance examples relevant to the intent. Utterance examples must be unique and contain fewer than 25 words or 200 characters. Aim to add at least 15 utterances with as much variety as possible; add at least 5 to begin training.

### Import an NLU intent

**Before you begin**

- Ensure the NLU Workbench plugin, NLU Workbench - Core plugin, and Predictive Intelligence plugin are installed and activated.
- You can import intents for Virtual Agent and AI Search models.
- Verify the application scope of your source model and target model are the same.
- Role required: nlu_editor, nlu_admin, or admin.

When you import an intent, training utterances (with entity annotations) and entities are also imported. **Not** included: test utterances in the default test set, and regular and pattern vocabulary. You cannot import intents when the model already has an intent with the same name, or an entity with the same name but different attributes.

**Procedure**

1. Ensure you are in the target application scope, and navigate to **All > NLU Workbench > Models**. The Virtual Agent tab opens by default.
2. Select the tab for your model's application, then select the model name.
3. In the model overview page, find the **Build and train your model** phase and select **View phase**.
4. In the **Intents** tab, select **Import intents**.
5. Locate the intents you want to import and select their check boxes. (Example: select the OpenITTicket intent in the ITSM NLU Model for Virtual Agent Conversations model.)
6. Select **Import**. (Example result: the #OpenITTicket intent appears in the target model's intents list, adding 29 training utterances.)

**What to do next:** Review the annotations of newly imported training utterances and add vocabulary annotation if needed. Train your model.

### Resolve intent issues

**Before you begin**

- Ensure the NLU Workbench plugin, NLU Workbench - Core plugin, NLU Workbench - Advanced Features plugin, and Predictive Intelligence plugin are installed and activated.
- You can resolve conflicts for Virtual Agent and AI Search models.
- Role required: nlu_admin or admin (nlu_editor when assigned to a model).

**Resolution table:**

| Issue | Resolution |
| --- | --- |
| intents have low utterance count | Add more training utterances. Intents need at least 5; recommended at least 15. |
| intents have low test utterance count | Add more test utterances to the model's default test set. Recommended at least 15. |
| intents have critical conflicts | Remove or edit utterances so that each applies to only one intent. |
| intents need review | Have an nlu_admin or nlu_editor review the intent. See Enable or disable a secondary model intent. |

**Procedure (resolving critical conflicts)**

1. Ensure you are in the same application scope as your model, and navigate to **All > NLU Workbench > Models**. The Virtual Agent tab opens by default.
2. Select the tab for your model's application, then the model name.
3. In the **Build and train your model** card, click **View phase**.
4. On the intents tab, click the **intents have critical conflicts** card. The list filters to intents with critical conflicts.
5. Click the intent name to resolve. (Example: GeneralHRInquiry.)
6. Click the **Conflicts** tab. The current intent's utterances show on the left; conflicting utterances for the other intent appear on the right. You can hide moderate conflicts and ignore conflicts, but fix all conflicts for best performance.
7. Point to the utterance you want to edit or remove. (Example: click the trash icon to remove the utterance from the CreateHRGeneralInquiryCase intent.) Changes save automatically.

**What to do next:** Irrelevant utterances appear as conflicts in their own NO_INTENT intent but cannot be edited or deleted in Conflicts; copy them to the Irrelevance Detection module. Continue to resolve all conflicts, then train your model.

### Create a simple entity

**Before you begin**

- Ensure the NLU Workbench plugin, NLU Workbench - Core plugin, NLU Common Model plugin, and Predictive Intelligence plugin are installed and activated.
- Create or use an existing NLU model and intent.
- Role required: nlu_editor, nlu_admin, or admin (editor assigned to the model).

**Procedure**

1. Navigate to **All > NLU Workbench > Models**. The Virtual Agent tab opens by default.
2. Select the tab for your model's application, then the model name. (Example: NLU for Access Requests.)
3. In the **Build and train your model** card, click **View phase**.
4. In the intents tab, click the intent name. (Example: SubmitAccessRequest.)
5. Click a word in one of the utterances to bring up the entity window. (Example: `parking garage`.)
6. Click **Create New Entity**.
7. In the **Create a new entity** screen, enter a name and select the **Simple** entity type. (Example: `buildingaccess`.) Select **Model availability** to make the entity available to every intent in the model.
8. Click **Save**. The entity saves and the words in the utterance remain highlighted.

**What to do next:** Your utterances can reference a vocabulary source by using the `@` handle. You can annotate the `@` handle as a simple entity to extract a list of values rather than repeating the utterance for all values.

### Create a mapped entity

**Before you begin**

- Ensure the NLU Workbench plugin, NLU Workbench - Core plugin, NLU Common Model plugin, and Predictive Intelligence plugin are installed and activated.
- Create or use an existing NLU model and intent.
- Role required: nlu_editor, nlu_admin, or admin (editor assigned to the model).

**Procedure**

1. Navigate to **All > NLU Workbench > Models**. The Virtual Agent tab opens by default.
2. Select the tab for your model's application, then the model name.
3. On the model details page, select the **Intents** tab.
4. Select an intent name. (Example: #SubmitRequest.)
5. In the **Utterances** tab, select a word in an utterance. (Example: the word `urgent` in `I have an urgent request`.)
6. Select **Mapped entities**.
7. Select **Create New Entity**.
8. On the form, configure the fields (Entity Name, Type, Model availability, Source, Provide values for this entity). (Example: Entity Name `priority`, Type Mapped, Model availability checked, Source = a table or list, Mapped values high, medium, low.)
9. Click **Save**. The entity appears on the **Associated entities** tab.

### Create a pattern entity

**Before you begin**

- Ensure the NLU Workbench plugin, NLU Workbench - Core plugin, NLU Common Model plugin, and Predictive Intelligence plugin are installed and activated.
- Create or use an existing NLU model and intent.
- Role required: nlu_editor, nlu_admin, or admin (editor assigned to the model).

> **Note:** Pattern entities use regular expressions (regex). The regex field value is a Java regular expression.

**Procedure**

1. Navigate to **All > NLU Workbench > Models**. The Virtual Agent tab opens by default.
2. Select the tab for your model's application, then the model name.
3. On the model details page, select **Intents**.
4. Select an intent name. (Example: #CheckITTicketStatus.)
5. Select one of the words of an utterance. (Example: `INC1234567`.)
6. Select **Create New Entity**.
7. In the **Create a new entity** window, configure the fields. (Example: Entity Name `incidentnumber`, Type Pattern, Model Availability optional, Regex `INC\d{7}`.)
8. Click **Save**. The pattern entity saves and appears in the **Associated Entities** tab.

### Create a system-derived entity

**Before you begin**

- Ensure the NLU Workbench plugin, NLU Workbench - Core plugin, NLU Common Model plugin, and Predictive Intelligence plugin are installed and activated.
- Create or use an existing NLU model and intent.
- Role required: nlu_editor, nlu_admin, or admin (editor assigned to the model).

**Procedure**

1. Navigate to **All > NLU Workbench > Models**. The Virtual Agent tab opens by default.
2. Select the tab for your model's application, then the model name.
3. In the model details page, select **Intents**.
4. Select the intent name. (Example: #FlightBooking.)
5. On the **Utterances** tab, select a word or phrase. (Example: utterance `book a flight from San Diego to San Francisco`; click `from San Diego`.)
6. Select **Create New Entity**.
7. In the **Create a new entity** screen, configure the fields. (Example: Entity Name `FromLocation`, Type System-derived, Model Availability optional, Parent Entity LOCATION.)
8. Select **Save**.
9. On the same utterance, select another word or phrase. (Example: `to San Francisco`.)
10. Select **Create New Entity**. (Example: Entity Name `ToLocation`, Type System-derived, Parent Entity LOCATION.)
11. Select **Save**. The two system-derived entities appear in the entity window.

**What to do next:** Train your model. Try the model to test (for example, Select **Try model**, enter `book a flight from Dallas to San Jose`, select **Go**). The model predicts the intent and shows the entities used.

### Create an open-ended entity

**Before you begin**

- Ensure the NLU Workbench plugin, NLU Workbench - Core plugin, NLU Common Model plugin, and Predictive Intelligence plugin are installed and activated.
- Create or use an existing NLU model and intent.
- Role required: nlu_editor, nlu_admin, or admin (editor assigned to the model).

> **Note:** You can use only one open-ended entity per intent. You can't annotate a vocabulary source (referenced by @vocab_source) as an open-ended entity.

**Procedure**

1. Navigate to **All > NLU Workbench > Models**. The Virtual Agent tab opens by default.
2. Select the tab for your model's application, then the model name.
3. On the Model details page, click **Intents**.
4. Select the intent name. (Example: OrderMerch.)
5. In the **Utterances** tab, select a word or phrase to bring up the entities window. (Example: `a hoodie`.)
6. Select **Create New Entity**.
7. On the **Create a new entity** screen, configure the fields. (Example: Entity Name `merch`, Type Open-Ended.)
8. Select **Save**. The merch open-ended entity is annotated in the Utterances section and persists as a reusable entity in all other NLU models in your instance.

**What to do next:** Train your model. Test (for example, Select **Try Model**, enter `I want to order a polo`, select **Go**). The model predicts the intent and shows it used the merch entity for the `a polo` value.

### Import entities

**Before you begin**

- Ensure the NLU Workbench plugin, NLU Workbench - Core plugin, NLU Common Model plugin, and Predictive Intelligence plugin are installed and activated.
- Create or use an existing NLU model, intents, and entities.
- Role required: nlu_editor, nlu_admin, or admin (editor assigned to the model).

> **Note:** All models include several system entities by default.

**Procedure**

1. Navigate to **All > NLU Workbench > Models**. The Virtual Agent tab opens by default.
2. Select the tab for your model's application, then the model name.
3. In the **Build and train your model** phase, select the **Entities** tab.
4. Select **Import entity**.
5. In the **Import Entity** window, select the entities you want to import. (Example: click the drop-down arrow for Application: HR Service Delivery NLU Model for Virtual Agent Conversations, then select four entities.) Importing entities does **not** import any utterances annotated with those entities.
6. Click **Import**. The entities appear under **User Defined Entities** in the Entities tab; by default, Model Availability is enabled.

**What to do next:** Annotate the model's utterances using the imported entities and train your model.

### Create a regular vocabulary item

**Before you begin**

- Ensure the NLU Workbench plugin, NLU Workbench - Core plugin, NLU Common Model plugin, and Predictive Intelligence plugin are installed and activated.
- Create or use an existing NLU model for Virtual Agent or AI Search.
- Role required: nlu_editor, nlu_admin, or admin (editor assigned to the model).

> **Note:** Choose a synonym that is a commonly-occurring word in the same language as your model.

**Procedure**

1. Navigate to **All > NLU Workbench > Models**. The Virtual Agent tab opens by default.
2. Select the tab for your model's application, then the model name.
3. On the **Model details** tab of the model overview, select the **Vocabulary** card.
4. In the **Vocabulary** tab, select **Add a vocabulary**.
5. In the **Add a vocabulary** window, select **Regular** as the Type.
6. Add a vocabulary word or phrase and then the synonym the model should use. (Example: `credentials` as the vocabulary and `password` as the synonym.)
7. Select **Save**.

**What to do next:** To deploy the new item, train and publish your model again.

### Create a pattern vocabulary item

**Before you begin**

- Ensure the NLU Workbench plugin, NLU Workbench - Core plugin, NLU Common Model plugin, and Predictive Intelligence plugin are installed and activated.
- Create or use an existing NLU model for Virtual Agent or AI Search.
- Role required: nlu_editor, nlu_admin, or admin (editor assigned to the model).

**Procedure**

1. Navigate to **All > NLU Workbench > Models**. The Virtual Agent tab opens by default.
2. Select the tab for your model's application, then the model name.
3. On the **Model details** tab, select the **Vocabulary** card.
4. Click **Add a vocabulary**.
5. In the **Type** field of the **Add a vocabulary** window, select **Pattern**.
6. Add a regular expression that covers words or phrases, and a synonym. (Example: a regex covering several variations of "mfa authentication," replaced with the synonym `multi-factor authentication`.)
7. Click **Save**. The pattern vocabulary item appears in the Vocabulary section.

### Create a list vocabulary source

**Before you begin**

- Ensure the NLU Workbench plugin, NLU Workbench - Core plugin, NLU Common Model plugin, and Predictive Intelligence plugin are installed and activated.
- Role required: admin, nlu_admin, or nlu_editor.

**Procedure**

1. Navigate to **All > NLU Workbench > Vocabulary Sources**.
2. Click the **My lists** tab.
3. Click **Create new list**.
4. In the **Create a new list to refer to** window, configure the fields (Handle, Language, Synonym, Enable Fuzzy Matching, Make case sensitive). (Example: Handle `@meetingroom`, Language English - en, Synonym `meeting room`, Enable Fuzzy Matching selected, Make case sensitive clear.) _Note: the source's example text gives the synonym as `meeting room`, but the accompanying screenshot (p.1142) shows `conference room`; this discrepancy is present in the source documentation._
5. Click **Create**. Your list vocabulary source draft appears in the My lists section.
6. Click the name of the list vocabulary source.
7. Click **Add list item**.
8. Enter a value for the list and click the green check mark. (Example: `Everest`.)
9. Double-click the area under **Alternate values** to add alternatives separated by a comma.
10. Train the model to make the list vocabulary source available.

**What to do next:** Add the rest of the names and alternatives. You must retrain the model after updating a list vocabulary source. Use the `@` symbol with the handle to refer to the source in a training utterance.

### Create a table vocabulary source

**Before you begin**

- Ensure the NLU Workbench plugin, NLU Workbench - Core plugin, NLU Common Model plugin, and Predictive Intelligence plugin are installed and activated.
- Role required: admin or nlu_admin.

> **Note:** The Reference field is not supported as a source field. Do not create multiple vocabulary sources that reference the same table and fields.

**Procedure**

1. Navigate to **All > NLU Workbench > Vocabulary Sources**.
2. Click **ServiceNow Tables**.
3. Click **Add another table**.
4. On the **Add another table to refer to** page, configure the fields:
   a. Select the table, handle, and synonym. (Example: Table Location (cmn_location), Handle `@Location`, Synonym `Location`.)
   b. Select the fields to refer to from the source table. (Example: Country and City; click **Options** and select **Use this field to look up values** for both; leave **Fields can appear together** empty.) To add multiple fields, select the plus icon.
   c. Configure advanced options: Language (English - en), Filter by (condition builder, left empty), Refresh (Every 7 days), Enable Fuzzy matching, Make case sensitive.
5. Click **Save**. The `@Location` table vocabulary source appears and begins to sync with its source table.
6. If the sync doesn't start immediately, select the **Sync Lookup** icon on the far right. When the sync completes, you can use the source in your models (no retraining needed after updating a table vocabulary source).

**What to do next:** Add the source to a model by annotating an utterance using the `@` symbol.

### Sync a table vocabulary source

**Before you begin**

- Ensure the NLU Workbench plugin, NLU Workbench - Core plugin, NLU Common Model plugin, and Predictive Intelligence plugin are installed and activated.
- Role required: admin or nlu_admin.

> **Note:** If an utterance references a table vocabulary source that has never been synchronized, the model fails to train. Sync manually if **Never synced**.

**Procedure**

1. Navigate to **All > NLU Workbench > Vocabulary Sources**.
2. In the **ServiceNow Tables** tab, point just to the right of the Refresh column to invoke the **Sync lookup** icon.
3. Select **Sync**. The vocabulary source starts synchronization. (Example: manually syncing the @AccessRoles vocabulary source to the Catalog Item table.)

**What to do next:** The operation can take time depending on the source table size. The **Last refresh** and **Current status** columns reflect the current status. Proceed to train your model.

### Test set creation and management

> **Note:** To test your model, install the ServiceNow Store application **NLU Workbench - Advanced Features**.

**Add content to your default test set:**

- **Manually** — From the model's overview page navigate to **Build and train your model > Test set** tab. Type your input into the **Type a test utterance here** field, select an appropriate intent, then select **Add**. Source = Manual.
- **Import** — From the **Test set** tab, select **Import test utterances** (from a CSV file or other models). Source = Manual.
- **Expert Feedback Loop** — Add actual user utterances from Virtual Agent chat logs. Source = Expert Feedback.

### Train and try your NLU model

**Before you begin**

- Ensure the NLU Workbench - Core plugin, NLU Workbench plugin, and Predictive Intelligence plugin are installed and activated.
- Create an NLU model, one or more intents, and associated entities.
- If any utterance references a table vocabulary source, ensure the source has been synchronized.
- Role required: nlu_editor, nlu_admin, or admin (editor assigned to the model).

> **Note:** To run a test against a list of test utterances, see Test and publish your model. The mid-conversation responses of Dialog Acts can't be tried or tested in NLU Workbench.

**Procedure**

1. Navigate to **All > NLU Workbench > Models**. The Virtual Agent tab opens by default.
2. Select the tab for your model's application, then the model name.
3. In the **Model details** tab, make sure there is enough content in Intents, Entities, and Vocabulary.
4. On the **Build and train your model** card, select **View phase**.
5. When the phase opens, ensure the **Train model** tab is selected. The tab displays the last time the model was trained and summarizes content changes since the last training.
6. Select the **Train** button. A progress bar displays during training. When finished, the system displays one of two recommendations:
   - When **less than 60%** of intents are covered in the default test set, the system recommends adding more test utterances (Add to test set).
   - When **over 60%** of intents are covered, the system recommends proceeding to testing (Test model).
7. To manually try individual utterances, select the **Try model** tab.
8. In the text field under **Enter an utterance to test**, type an utterance and select **Go**.

**Result (example):** Entering `I need to update my home address`:
1. The system displays the model's confidence threshold (76% in this example).
2. Under **Top prediction(s)**, the system displays all intents predicted with a confidence score greater than the threshold.
3. The intent UpdateAddress is predicted with a confidence score of 97%, greater than the threshold of 76%.

The Try model results also display thumbs-up and thumbs-down icons for feedback.

### Test panel feedback (procedure)

In all scenarios, use these four steps:
1. In the **Build and train your model** phase, select **Try model** to open the test panel.
2. In the **Enter an utterance to test** field, enter a brief utterance similar to a training utterance.
3. Click **GO**. The system returns predictions in the **Top Predictions(s)** section.
4. Click the **Thumbs Up** icon (if the predicted intent is correct) or the **Thumbs Down** icon (in all other cases, which opens the **Provide feedback to improve this prediction** section).

- **Scenario 1:** Enter `help with hr`; confident the prediction is correct, so click **Thumbs Up**. (Example correct intent: #CreateHRGeneralInquiryCase.)
- **Scenario 2:** A different user enters the same utterance but isn't sure, so clicks **Thumbs Down**. The panel expands with two options: **Its correct intent should be:** (choose a more appropriate intent, for example Retrieve Work Location) or **I'm not sure what the correct intent is** (system shows next best predictions).
- **Scenario 3:** A user submits gibberish or mixes languages, so no prediction is returned. The user clicks **Give feedback**, then selects **No intent should be predicted** (which removes the utterance from all intents it is part of).
- **Scenario 4:** Click **Exclude this model's predictions for this utterance**, then **Save changes**. A banner confirms the feedback is saved.

### Test your model

**Before you begin**

- Ensure the NLU Model Builder - Core plugin, NLU Model Builder plugin, NLU Workbench - Advanced Features plugin, and Predictive Intelligence plugin are installed and activated.
- Have a trained model for Virtual Agent or AI Search, and a test set.
- Role required: nlu_editor, nlu_admin, or admin (editor assigned to the model).

Notes: If an expected intent in your test set does not correspond to any intent in the model, those utterances are not used for testing. When the model returns no prediction for utterances marked as Not relevant, that result is counted as Correct. If your test set does not cover at least 60% of intents, the system will not recommend a confidence threshold, but you can still run the test.

**Procedure**

1. Navigate to **All > NLU Workbench > Models**. The Virtual Agent tab opens by default.
2. Select the tab for your model's application, then the model name.
3. On the model overview's **Model details** tab, locate the **Test and publish your model** card and click **View phase**.
4. Select **Run new test**. (Other phases are unavailable during a test.)
5. The **Confirm run new test** dialog box opens; select **OK**. The test begins and the "Testing is in progress..." page loads.

**Result:** When finished, the page reloads. The **Test run date** field reflects the date and time. The **Overview** tab displays a chart plus the top 5 incorrect and top 5 missed intents. The **Detailed results** tab lists all test utterances and their prediction outcomes. View previous results via **view the test history** or **Batch Testing > Test results**.

### Publish your NLU model

**Before you begin**

- Ensure the NLU Workbench - Core plugin, NLU Workbench plugin, and Predictive Intelligence plugin are installed and activated.
- Have a trained and tested NLU model.
- Role required: admin or nlu_admin.

If your model is already published, you can publish it again, but you must train the model again before republishing.

**Procedure**

1. Navigate to **All > NLU Workbench > Models**. The Virtual Agent tab opens by default.
2. Select the tab for your model's application, then the model name.
3. On the Model overview page, locate **Test and publish your model**, then select **View phase**. (If the model hasn't been built or trained, this phase is not available.)
4. On the **Test and publish your model** screen, select **Run new test** to assess the model using its default test set. (Testing can be skipped, but model performance may not be optimal; a confirmation message displays.)
5. Click **Publish model**. (Button states: white if not tested, green if tested, unavailable if the last trained model is already published.)

**Result:** The most recent version of your NLU model is published, active, and available for use in other ServiceNow applications, replacing any older versions in use.

### Compare draft and published versions of your NLU model

**Before you begin**

- Ensure the NLU Workbench plugin, NLU Workbench - Core plugin, NLU Workbench - Advanced Features plugin, and Predictive Intelligence plugin are installed and activated.
- Role required: nlu_editor, nlu_admin, or admin (editor assigned to the model).

**Procedure**

1. Navigate to **All > NLU Workbench > Models**. The Virtual Agent tab opens by default.
2. Select the tab for your model's application, then the name of your published model.
3. From the model's overview page, locate the **Build and train your model** card and click **View phase**.
4. Make a change to the intents, utterances, entities, or vocabulary. (Example: add training utterances to the UpdateEmail intent.)
5. Train and try the changed model:
   a. On the **Train model** tab, click **Train**.
   b. When training is finished, the system displays "The model has been successfully trained."
   c. In the **Try model** tab, enter `wrong email address`.
   d. Click **Go**. The panel displays prediction results for both the published model and the trained model for comparison.

### Add utterances to Irrelevance detection

1. Navigate to **All > NLU Workbench > Models**. The Virtual Agent tab opens by default.
2. Scroll down the list of Virtual Agent models to the **Boost your model performance** section.
3. Scroll horizontally to locate the card **Keep chats focused**, and select its button **Go to irrelevance detection**.

To re-assign an utterance in Irrelevance detection, expand the list in the **Corrected intent** column and select the appropriate intent. Select **Save feedback**, then retrain the model.

### Access model settings

Navigate to **All > NLU Workbench > Models**, select the tab and your model's name, then the **Model settings** tab. Edit the name, short description, and business area (language, purpose, and scope cannot be changed); toggle **Ignore punctuation**; and adjust **Model threshold settings**.

## Figures, Diagrams & Screenshots

**Figure (p.1084):** Documentation page describing "NLU Models for AI Search" and introducing "Model management." Decorative ServiceNow logo at top. No substantive screenshot; text-only page covering AI Search prebuilt model behavior and the model-management overview.

**Figure (p.1085):** Screenshot of the **NLU Workbench > Models** landing page. Shows three tabs — **Virtual Agent models** (active), **Issue Auto Resolution (IAR)**, and **AI Search**. Below is a search bar, a **Show Prebuilt Models** toggle, an **All Languages** filter, and a model list table with columns Model, Status, Used in VA, Model Type, Enabled Intents, and Mapped Intents. One row shows "ITSM model for Virtual Agent (English)" with Status "Draft Saved," Model Type "Custom," and counts. The **Create new model** button (upper right) is highlighted with a purple box. Illustrates how to begin creating a model and the model-list layout.

**Figure (p.1086):** Two stacked screenshots of the **Model management phases** cards on the model overview. The first card, **Build and train your model**, lists sub-items (Add or remove utterances; Configure entities; Build and maintain the default test set; Provide synonyms) with a **View phase** button. The second card, **Test and publish your model**, and a third card, **Tune your model**, are also shown. Illustrates the three-phase life cycle.

**Figure (p.1087):** Screenshot repeating the **NLU Workbench > Models** page with the **Virtual Agent models** tab, search/toggle/filter controls, the model-list table, and the highlighted **Create new model** button (purple box). Reinforces the navigation entry point for creating models.

**Figure (p.1088):** Documentation text page on "Duplicating, exporting, and updating" and the start of "Create an NLU model from blank." No UI screenshot; bulleted lists and a numbered procedure.

**Figure (p.1089):** Screenshot of the **START FROM BLANK** model-creation form titled "First, let's fill out some model details." Fields: **Name** (highlighted with a red box, value "HR Model for Virtual Agent"), **Short description** ("Natural language for Human Resources user requests"), **What is the primary language?** (Select... drop-down), **What are you creating this for?** ("Virtual Agent"), and **What business area is this for? (optional)** ("-- Not specified --"). **Cancel** and **Next** buttons at lower right. Illustrates step 6 of creating a blank model.

**Figure (p.1090):** Screenshot of the **Model details** page for a newly created model "HR Model for Virtual Agent." Shows content tiles with large zero counts (Intents 0, Entities 0, Vocabulary 0) and a modal "This model doesn't have any content" prompting to add content. Below is a "Sample CSV setup" table (Intent/Utterance columns with `schedule` rows). Illustrates an empty new model and the CSV format.

**Figure (p.1091):** Screenshot of the **IMPORT DATA FROM CSV** form "First, let's fill out some model details" for the Calendar Model. Fields visible: Name ("Calendar Model"), Short description, primary language (English), and purpose (Virtual Agent) drop-downs, with **Cancel** and **Next** buttons. A progress indicator with steps (Define details / Import CSV) appears near the top. Illustrates step 6 of CSV import.

**Figure (p.1092):** Screenshot of the **IMPORT DATA FROM CSV** "Now, select which file you want to use" screen, showing a two-column preview area (Intent / Utterance) and a **Select file** control. Progress steps shown at top. Illustrates steps 8-9 of CSV import.

**Figure (p.1093):** Screenshot of the **CREATE USING PREBUILT MODEL** form "First, let's fill out some model details." Fields: Name ("Human Resources VA Model"), Short description ("Virtual Agent Model for responding to HR requests"), primary language (English), purpose (Virtual Agent), and business area (HR) drop-downs. **Cancel** and **Next** buttons. Illustrates step 6 of prebuilt-model creation.

**Figure (p.1094):** Two screenshots. (1) **CREATE USING PREBUILT MODEL** "First, let's decide which prebuilt model to use," with a **Prebuilt model** drop-down (value "HR NLU for VA," highlighted purple) and a progress bar (Define details / Select a prebuilt model / Select intents). (2) **Pick which intents to use** screen — a table with a select-all checkbox and columns Intent, Utterances, Entities. Rows include AddEmergencyContact (28 utterances, 4 entities), AskAQuestion (3, 0), Benefits (81, 0), CreateHRGeneralInquiryCase (92, 0), DeleteEmergencyContact (31, 1), GeneralHRInquiry (92, 0), NewHireOrientation (60, 0), PayDiscrepancy (59, 0, checkbox highlighted), RequestForLeave (61, 0), UpdateAddress (29, 0), UpdateEmail (34, 1). Caption notes "you select 10 intents." Illustrates choosing a prebuilt model and selecting intents.

**Figure (p.1095):** Documentation text page completing the prebuilt-model procedure and starting "Duplicate an NLU model" (Before you begin, About this task, Procedure). No UI screenshot.

**Figure (p.1096):** Screenshot of the model row **More options** menu, expanded to show: Assign to editor, Add a language, **Duplicate this model** (highlighted), Export model as CSV, and Delete this model. Below is the **Duplicate this Model** modal "Create a copy of Restaurant Model" with **Model name** and **Description** fields and a **Duplicate** button (with a purple arrow pointing to it). Illustrates duplicating a model.

**Figure (p.1097):** Screenshot of the model **More options** menu again (Assign to editor, Add a language, Duplicate this model, **Export model as CSV** highlighted, Delete this model). Illustrates the Export model as CSV action.

**Figure (p.1098):** Two screenshots for adding a model to an update set. (1) The platform navigator with `sys_nlu_model.list` typed in the filter (All / Favorites / History tabs visible). (2) The `sys_nlu_model` list view (a wide table of model records). Illustrates steps 1-2 of the update-set procedure.

**Figure (p.1099):** Several screenshots illustrating the update-set workflow: (1) a model record in `sys_nlu_model` with a banner prompt "This record is in the ITSM... application, but Global is the current application" and a highlighted edit link; (2) the **Related Links** area with **Add model to current update set**; (3) an error banner "You are attempting to add a record to the system default update set" with a **New Local Update Set** link and a "Failed at 100%" progress indicator; (4) a new update set record form (Submit and Make Current). Illustrates steps 4-6.

**Figure (p.1100):** Documentation text page continuing the multi-scope update-set steps (parent/child update sets, Batch Base, State = Complete, Export Update Set Batch to XML) and starting "Delete an NLU model" with a Warning callout. No UI screenshot.

**Figure (p.1101):** Two screenshots. (1) A model-list row showing columns Model, Status, Last Published, Created for, Enabled Intents, Mapped Intents, Total Entries, Editors, with a highlighted **More options** control. (2) The **Delete HR NLU for VA EFL1** confirmation modal with the checkbox "All references to this model will be deleted," and **Cancel** / **Delete model** buttons. Illustrates the delete confirmation.

**Figure (p.1102):** Screenshot of the **Build and train your model** card on the model overview, with sub-items and a highlighted **View phase** button (purple box). Illustrates how to enter the build phase. The rest of the page is text covering Intents, Entities, and Vocabulary concepts.

**Figure (p.1103):** Screenshot of the **Settings** tab of a model ("Model details / Settings"), showing fields: Name ("IT Model"), Short description, Language (English - en), Created for (Virtual Agent), Business area (optional), Confidence Threshold(%), and an **Ignore punctuation** checkbox (checked). A **Save** button appears. Illustrates the model Settings page.

**Figure (p.1104):** Screenshot of the **Build and train your model** phase, **Intents** tab. Shows a breadcrumb (Home > model name > Build and train your model), tabs Intents / Entities / Vocabulary / Test set, an intents table, and a right-side **Train model / Try model** panel. Illustrates the intents workspace and the up-to-750-intent guidance in the surrounding text.

**Figure (p.1105):** Screenshot of an intent details page **#UpdateEmail** with tabs Utterances / Associated entities / Conflicts / Settings, plus the **Train model / Try model** panel on the right. An utterances table lists rows (for example, "wrong email address," "my email is wrong") with Source "Manual," Score, Last modified, and edit/copy/delete icons. Illustrates the utterances list and per-utterance actions.

**Figure (p.1106):** Two screenshots. (1) An intent details page **#AddEmergencyContact** with a table of utterances (Name, Type, Associated entities, Utterances, Intent count). (2) The **Build and train your model** intents tab showing three issue cards (highlighted purple): "1 intent has low utterance count," "15 intents have low test utterance count," and "2 intents have critical conflicts." Illustrates intent issue cards.

**Figure (p.1107):** Documentation text page for "Create an NLU intent" (Before you begin, About this task with the AddMembersToDistributionList example, Procedure steps 1-7). No UI screenshot.

**Figure (p.1108):** Screenshot of the **Create an intent** modal "Fill in the properties for this intent" with **Intent name** ("PayDiscrepancy") and **Description** fields and an **Add intent** button. Below, a screenshot of the **Utterances** field with several entered training utterances (e.g., "There is something wrong with my pay check," "Something is wrong with my paycheck," "salary discrepancy," "incorrect paycheck issued") each with delete icons. Illustrates creating an intent and adding utterances.

**Figure (p.1109):** Documentation text page on "Reusing intents from prebuilt NLU models," "Prebuilt Virtual Agent model content," and a **Plugins / Descriptions** table for Virtual Agent conversation plugins. No standalone screenshot beyond the table.

**Figure (p.1110):** Documentation text page for "Import an NLU intent" (Before you begin, About this task listing what is/isn't imported, Procedure steps 1-4). No UI screenshot.

**Figure (p.1111):** Screenshot of the **Build and train your model** **Import intents** screen. Shows the intents issue cards at top, an **Import intents** button (highlighted), and a modal listing NLU models with an expandable table (columns Model Name, Utterances, All Intents, Created by, Last updated). The **OpenITTicket** intent row in "ITSM ITSM NLU Model for Virtual Agent Conversations (4G)" is checkbox-selected (highlighted). Illustrates selecting intents to import.

**Figure (p.1112):** Documentation/screenshot page for "Resolve intent issues." Repeats the **Build and train your model** intents tab with the three issue cards highlighted (1 low utterance count, 15 low test utterance count, 2 critical conflicts). Illustrates where issue cards appear.

**Figure (p.1113):** Two screenshots for resolving conflicts on intent **#GeneralHRInquiry**: (1) the **Conflicts** tab showing a numbered list of conflicting utterance pairs — the current intent's utterances on the left and the conflicting intent's utterances on the right; (2) a close-up of pointing to an utterance with a highlighted **trash icon** to remove it. Illustrates the conflict-resolution UI.

**Figure (p.1114):** Continuation screenshots of the **#GeneralHRInquiry** Conflicts tab (numbered conflicting utterance rows) and the close-up of removing an utterance. Reinforces conflict removal; surrounding text covers NO_INTENT/irrelevant utterance behavior.

**Figure (p.1115):** Screenshot of the **Build and train your model** **Entities** tab. Tabs Intents / Entities / Vocabulary / Test set, an entities table (Name, Type, Model availability, Annotated intents, Created by, Last updated, Enabled), and the Train/Try panel. The surrounding text explains the laptop/urgency entity example and lists the five user-defined entity types. Illustrates the entities workspace.

**Figure (p.1116):** Screenshot of the **Entity settings page** for entity "conferenceRoom." Shows tabs (Annotations / Settings), an **Entity name** field, **Type** ("Regular"/mapped), a highlighted **Model availability** checkbox, a **Source** area, and a **Save** button. Illustrates editing model availability and entity settings.

**Figure (p.1117):** Screenshot of the entity-creation popover invoked from an utterance "can't access door to parking garage." A small panel lists entity-type tabs with counts — Simple entities (2), Mapped entities (11), Pattern entities (4), System-derived entities (0), Open-ended entities (0) — and a highlighted **Create New Entity** button (red box). Illustrates starting a simple entity from an utterance word.

**Figure (p.1118):** Screenshot of the **Create a new entity** modal for a simple entity. Fields: **Entity Name** ("buildingaccess"), **Type** ("Simple"), and a highlighted **Model availability** checkbox, with **Cancel** / **Save** buttons. Below, an "Example utterance using a vocabulary source" screenshot shows a `@conferenceRoom` reference being selected in an utterance with a drop-down of values. Illustrates simple-entity creation and vocabulary-source annotation.

**Figure (p.1119):** Screenshot of an utterance "I have an urgent request ASAP / I have an urgent request" with the entity popover open. The popover lists Simple entities (3), **Mapped entities** (highlighted, count), Pattern entities, System-derived entities, Open-ended entities, with a highlighted **Create New Entity** button and a purple arrow. Below is a field-description table (Entity Name, Type, Model availability, Source, Provide values for this entity). Illustrates choosing Mapped entities and the form fields.

**Figure (p.1120):** Screenshot of the **Create a new entity** modal for a mapped entity. Fields: **Entity Name** ("priority"), **Type** ("Mapped"), **Model Availability** (checked), **Source** (radio with "Use this if you have a table or list..."), and **Provide values for this entity** ("high, medium, low") with an **Add** control. **Cancel** / **Save** buttons. Illustrates mapped-entity configuration.

**Figure (p.1121):** Screenshot showing the result of saving the mapped entity — the entity popover now lists the values (high / medium / low) under the entity, and a confirmation that the entity appears on the **Associated entities** tab. Illustrates the saved mapped entity.

**Figure (p.1122):** Documentation text page for "Create a pattern entity" (Before you begin, About this task with a regex Note, Procedure steps 1-5 selecting the #CheckITTicketStatus intent and the word INC1234567). No standalone screenshot.

**Figure (p.1123):** Screenshot of the **#CheckITTicketStatus** intent with the entity popover open on the utterance "I need to check the status of INC1234567." Below is the **Create a new entity** modal for a pattern entity: **Entity Name** ("incidentnumber"), **Type** ("Pattern"), **Model Availability**, and **Regex** ("INC\d{7}") with a "See documentation for Regular Expressions" link and **Cancel** / **Save** buttons. Illustrates pattern-entity creation.

**Figure (p.1124):** Documentation text page for "Create a system-derived entity" (Before you begin, About this task with the flight-booking/LOCATION example, Procedure steps 1-5). No standalone screenshot.

**Figure (p.1125):** Screenshot of the **#FlightBooking** intent. The utterance "Book a flight from San Diego to San Francisco" has the entity popover open (Simple/Mapped/Pattern/System-derived/Open-ended tabs with counts) and a highlighted **Create New Entity** button. Below, the **Create a new entity** modal for **FromLocation**: Type "System-derived," Model Availability, **Parent Entity** "LOCATION," with **Cancel** / **Save**. Illustrates creating the first system-derived entity.

**Figure (p.1126):** Large screenshot. The utterance "Book a flight from San Diego to San Francisco" with "from San Diego" and "to San Francisco" highlighted; the entity popover shows Simple entities (1), Mapped entities (0), Pattern entities (0), **System-derived entities (2)** highlighted, Open-ended entities (0), and a **Create New Entity** button (red box, arrow). Below, the **Create a new entity** modal for **ToLocation** (Type System-derived; Parent Entity LOCATION highlighted; Save highlighted). Illustrates creating the second system-derived entity.

**Figure (p.1127):** Two screenshots. (1) Result: the entity window shows both system-derived entities. (2) The **#FlightBooking** intent details page with the **Try model** test panel open — the utterance "book a flight from Dallas to San Jose" with a highlighted prediction result block listing the predicted intent and the entities used (FromLocation/ToLocation and LOCATION values). Illustrates testing system-derived entities.

**Figure (p.1128):** Documentation text page for "Create an open-ended entity" (Before you begin, About this task with the iPhone example and Notes about one open-ended entity per intent and vocabulary-source restriction, Procedure steps 1-5). No standalone screenshot.

**Figure (p.1129):** Large screenshot of the **#OrderMerch** entity window. Tabs Utterances (3) / Associated Entities (1) / Conflicts (0) / Settings. Utterances include "Can I buy some mugs," "How much is the polo shirt," "I want to order a hoodie" (with "a hoodie" highlighted). The entity popover shows Simple/Mapped/Pattern/System-derived entities (3 each) and **Open-ended entities (3)** highlighted, with a **Create New Entity** button (purple box). Below, the **Create a new entity** modal: Entity Name "merch," Type "Open-Ended," with an annotated example "I want to order an iPhone" labeled Context / Entity value / Intent / Entity, and a highlighted **Save** button. Illustrates open-ended entity creation.

**Figure (p.1130):** Screenshot of the **#OrderMerch** intent after saving, showing the merch open-ended entity annotated in an utterance, then a **Try model** panel where "I want to order a polo" is entered and the prediction shows the merch entity used for the "a polo" value. Illustrates testing the open-ended entity.

**Figure (p.1131):** Screenshot of the **Build and train your model** **Entities** tab with a highlighted **Import entity** button (purple box) and the entities table (System Entities and User Defined Entities). Illustrates step 4 of importing entities.

**Figure (p.1132):** Screenshot of the **Import Entity** modal. A list of applications/models is expandable (e.g., Universal Request NLU Model, NLU Common Model, HR Service Delivery NLU Model for Virtual Agent Conversations expanded) with entity rows showing checkboxes, Type, Created by, and Last updated; several entities (email, relationship, phonenumber, name) are checkbox-selected (highlighted). An **Import** button is shown. Below, a result table of imported entities under "User Defined Entities." Illustrates selecting and importing entities.

**Figure (p.1133):** Documentation page "Using regular expressions in entities" with a Note that ServiceNow supports Java regex only. Includes a **Create a new entity** modal screenshot for a **Knowledge base article** pattern entity: Entity Name "kbarticlenumber," Type "Pattern," Model Availability, **Regex** "KB\d{7}." Also begins the **Case number** example. Illustrates KB-article regex.

**Figure (p.1134):** Three **Create a new entity** modal screenshots for pattern entities: **Case number** (Entity Name "casenumber," Regex "CS\d{7}"), **Email address** (Entity Name "emailaddress," Model Availability checked, Regex "\b[a-zA-Z0-9&*/_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\b"), and the **Phone number** text example with regex "\d{10}|(?:\d{3}-){2}\d{4}|\(\d{3}\)\d{3}-?\d{4}." Illustrates regex formats for case, email, and phone entities.

**Figure (p.1135):** Screenshot of a **Create a new entity** modal for "captiveportalnumber" (Type Pattern, Regex shown), plus the "Regex resources" external-link list. Mostly text introducing NLU vocabulary. Illustrates a final regex entity example.

**Figure (p.1136):** Screenshot of the **Build and train your model** **Vocabulary** tab. A vocabulary table lists items with columns Vocabulary, Synonym, Type and edit/delete icons (e.g., credentials -> password Regular; ServiceNow [pattern] -> service now Regular; downhandle -> deskhandle Regular). The Train/Try panel is on the right. Below is the **Vocabulary item types** table (Regular / Pattern). Illustrates the vocabulary workspace.

**Figure (p.1137):** Documentation page on vocabulary sources and "Vocabulary usage in relation to an intent," including the **OrderSoftware** Utterance/Issue-and-Solution table (sfcrm and Word examples). No standalone screenshot.

**Figure (p.1138):** Documentation text page on the `\bIT\b` regex example, "Regex resources," and the start of "Create a regular vocabulary item" (Before you begin, About this task, Procedure steps 1-4). No standalone screenshot.

**Figure (p.1139):** Screenshot of the **Build and train your model** **Vocabulary** tab (tabs Intents (22) / Entities (16) / Vocabulary (28) / Test set (610)) with an **Add a vocabulary** control. Below, the **Add a vocabulary** modal: **Type** "Regular," **Vocabulary** ("credentials"), **Synonym** ("password"), with **Cancel** / **Save**. Illustrates adding a regular vocabulary item.

**Figure (p.1140):** Screenshot of the **Build and train your model** **Vocabulary** tab again with **Add a vocabulary**, then the **Add a vocabulary** modal with **Type** "Pattern" selected and fields for a regular expression and synonym (multi-factor authentication example). Illustrates adding a pattern vocabulary item.

**Figure (p.1141):** Screenshot of the **Add a vocabulary** modal for a pattern item (Type Pattern; Vocabulary regex; Synonym "multi-factor authentication") with **Save**. The surrounding text begins "Create a list vocabulary source." Illustrates the pattern vocabulary save.

**Figure (p.1142):** Screenshot of the **Vocabulary sources** page (Sensitive Tables / **My lists** tabs) with a **Create new list** control, then the **Create a new list to refer to** modal showing fields Handle ("@meetingroom"), Language ("English - en"), Synonym ("conference room"), **Enable Fuzzy Matching** (checkbox), and **Make case sensitive** (checkbox), with a **Create** button. Above is the field-description table (Handle, Language, Synonym, Enable Fuzzy Matching, Make case sensitive). Illustrates list-source creation.

**Figure (p.1143):** Screenshot of the **@meetingroom** list vocabulary source (Values / Properties tabs). Shows **Add list item**, an **Actual value** "Everest" with a green check, and an **Alternate values** field ("everest, ev01, c4") highlighted. Illustrates adding list items and alternate values.

**Figure (p.1144):** Screenshot of the **Add another table to refer to** page. A "Select the ServiceNow table..." instruction, with fields **Table** ("Location (cmn_location)"), **Handle** ("@Location"), and **Synonym** ("Location") highlighted with a purple box, and a **Show me an example** link. Illustrates step 4a of table-source creation.

**Figure (p.1145):** Screenshot of the **Fields** section of the table-source form. Two **Field name** rows — "Country (country)" and "City (city)" — each with an **Options** control; a highlighted **Fields can appear together e.g. [First name] [Last name]** checkbox; plus add/remove icons. Illustrates step 4b (selecting source fields).

**Figure (p.1146):** Screenshot of the **Advanced Options** section of the table-source form. Fields: **Language** ("English - en"), **Filter by** (condition area), **Refresh** ("Every 7 days," highlighted drop-down), **Enable Fuzzy matching** (checkbox), and **Make case sensitive** (checkbox), with a **Save** button. Illustrates step 4c (advanced options).

**Figure (p.1147):** Screenshot of the **ServiceNow Tables** tab of the **Vocabulary sources** page. A table lists sources (Vocabulary handle, Source table, Source field, Application, Current status, Refresh) with a highlighted **Sync lookup** icon on the right of a row. Illustrates manually syncing a table vocabulary source (and reappears as a labeled figure on this page).

**Figure (p.1148):** Screenshot of the **Utterance** tab of the Intent details page **#ResetPassword**. An utterance "I need to order a Mac" has a blue underline under "Mac" with a purple arrow pointing to it, indicating a pre-built vocabulary suggestion. Illustrates pre-built vocabulary recognition.

**Figure (p.1149):** Screenshot of the **#ResetPassword** intent showing the pre-built vocabulary popover for the underlined word "Mac," offering "What do you mean?" options — a pre-built suggested definition (radio) and "Provide a synonym" — with **Ignore** and **Confirm** buttons (Confirm highlighted). Illustrates choosing a pre-built definition or synonym.

**Figure (p.1150):** Three screenshots of accessing/using the default test set: (1) the **Build and train your model** **Test set** tab with a **Test Coverage 100%** indicator, **Import test utterances** / **Download test set** controls, and a "Type a test utterance here" field; (2) the model-list **Test Coverage** tile view (counts 21 / 16 / 28 / 1 / 100% highlighted); (3) the **Multi-model Batch Testing > Test sets** tab listing default test sets labeled **Default**. Illustrates the three ways to access the test set.

**Figure (p.1151):** Documentation text page on Test Coverage scoring, using the test set, characteristics of default test sets, and downloading/moving test sets. No standalone screenshot.

**Figure (p.1152):** Documentation text page for "Train and try your NLU model" (Before you begin, About this task, Procedure steps 1-4). No standalone screenshot.

**Figure (p.1153):** Screenshot of the **Build and train your model** card with a highlighted **View phase** button, then a screenshot of the phase open on the **Intents (39)** tab (Entities (35), Vocabulary (36), Test set (11)) with the right-side **Train model** panel highlighted purple — showing "TRAIN MODEL / The model was never trained," "Content changes: English - en, 39 intent(s), 25 entitie(s), 36 vocabulary," and a green **Train** button. Illustrates the Train model tab before training.

**Figure (p.1154):** Two screenshots of post-training recommendations: (1) the **Train model** tab showing "Last trained just now," "Content changes" (0 intents/entities/vocabulary), a **Train** button, and a highlighted card "Now that you have trained the model, we recommend you add test utterances for at least 60% of the intents and test the model" with an **Add to test set** button; (2) a card "Now that you have trained the model and have sufficient test utterances, test the model..." with a **Test model** button. Illustrates the two training outcomes (below vs. above 60% coverage).

**Figure (p.1155):** Screenshot of the **Build and train your model** phase showing content tiles and the **Try model** panel; an utterance "I need to update my home address" is entered with **Go**, returning a prediction. The surrounding numbered text explains the 76% threshold and the 97% UpdateAddress prediction. Illustrates trying an utterance.

**Figure (p.1156):** Documentation text page on "Providing prediction feedback" and Scenario 1 (thumbs up for "help with hr" -> #CreateHRGeneralInquiryCase). No standalone screenshot.

**Figure (p.1157):** Large screenshot of the **Try model** panel on "HR NLU for VA EFL1 - English (Primary)" (breadcrumb shows "Published 9 minutes ago"). The utterance "help with hr" returns **Published model prediction results, Confidence Threshold 76%**, **Top prediction(s)**: "CreateHRGeneralInquiryCase (96% - Intent)" with the **thumbs-up** icon highlighted (purple box). Illustrates Scenario 2 setup (thumbs up icon).

**Figure (p.1158):** Screenshot of the **Try model** panel for "help with hr" — Published model prediction results, Confidence Threshold 76%, Top prediction "CreateHRGeneralInquiryCase (96% - Intent)" with the **thumbs-down** icon highlighted (purple box). Caption: clicking it expands the "Provide feedback to improve this prediction" section. Illustrates Scenario 2 thumbs down.

**Figure (p.1159):** Screenshot of the **Try model** panel showing **Trained model prediction results, Confidence Threshold 60%**, a top prediction "CreateHRGeneralInquiryCase (71% - Intent), DURATION (Entity) - N01 (Value)" with a thumbs-down, and the expanded **Provide feedback to improve this prediction** section: highlighted **Its correct intent should be:** button, a drop-down ("I'm not sure what the correct intent is..."), a search field listing intents (CreateDistributionList, CreateHRGeneralInquiryCase, **Retrieve Work Location** highlighted). Illustrates choosing a corrected intent (Scenario 2/3).

**Figure (p.1160):** Large screenshot of the **Try model** panel with a non-English/English mixed utterance ("[Gurmukhi script] broke down"), **Trained model prediction results, Confidence Threshold 60%**, "No intent was predicted for this utterance," and a highlighted **Give feedback** link (purple box, arrow). Illustrates Scenario 3 (no prediction due to mixed languages).

**Figure (p.1161):** Large screenshot of the **Try model** panel for the same mixed-language utterance, now showing the expanded **What should've been predicted instead?** prompt (dotted highlight) with a drop-down set to **No intent should be predicted** and a **Save changes** button. Illustrates selecting "No intent should be predicted."

**Figure (p.1162):** Screenshot of the **Try model** panel with the **What should've been predicted instead?** drop-down expanded, listing **No intent should be predicted** (highlighted) plus intents (CreateDistributionList, CreateHRGeneralInquiryCase, Retrieve Work Location, StartIW), with a highlighted drop-down arrow. Caption introduces Scenario 4 (Exclude this model's predictions). Illustrates the intent drop-down.

**Figure (p.1163):** Two screenshots: (1) the **Try model** panel with "No intent should be predicted" selected and a highlighted **Save changes** button (purple arrow); (2) the model content page with a green confirmation banner at the top confirming the user feedback for the prediction is saved (with a connector line to the Try model panel). Illustrates the save confirmation (Scenario 4 result).

**Figure (p.1164):** Two screenshots: (1) the **Test and publish your model** card with a **View phase** button; (2) the **Test and publish your model** **Overview** page showing a model results table, **Run new test** / **Publish model** buttons, and a **Test run date** drop-down (value "2023-01-09 17:36:31"). Illustrates the test/publish overview.

**Figure (p.1165):** Screenshot of the test-results bar chart titled **"How often is NLU correctly predicting intents?"** with four colored bars and a legend: **Correct** (34.40%, blue, tallest), **Correct among multiple** (10.34%, light), **Missed** (34.40%, pink), **Incorrect** (20.69%, red). Below is the percentage-description table (Correct, Correct among multiple, Missed, Incorrect). Illustrates how to read test results.

**Figure (p.1166):** Documentation text page on Publish model, Multi-model Batch Testing, and "Test your model" (Before you begin, About this task). No standalone screenshot.

**Figure (p.1167):** Two screenshots for running a test: (1) the **Test and publish your model** Overview with a model table, **Run new test** button, and **Test run date** drop-down; (2) the **Confirm run new test** dialog ("Run new test on Test set - HR NLU for VA TIP?") with **Cancel** / **OK** buttons. Illustrates running a new test.

**Figure (p.1168):** Screenshot of the **Test and publish your model** card with a **View phase** button and the **Run new test** / **Publish model** buttons, accompanying the publish procedure. Illustrates locating the publish controls.

**Figure (p.1169):** Screenshot of the **#UpdateEmail** intent **Try model** panel comparing versions: the utterance "wrong email address" returns both **Published model** and **Trained model** prediction results side by side, with highlighted result blocks showing the confidence scores before and after changes. Illustrates draft-vs-published comparison.

**Figure (p.1170):** Documentation text page for "Irrelevance detection in NLU" (Summary information, Roles/Usage/Navigation). Repeats the #UpdateEmail comparison context above; no new standalone screenshot.

**Figure (p.1171):** Screenshot of the **NLU Workbench > Models** Virtual Agent page scrolled to the **Boost your model performance** section, showing horizontally scrollable cards including **Keep chats focused** and **Find and resolve conflicts**, with a highlighted **Go to irrelevance detection** button. Illustrates navigating to Irrelevance detection.

**Figure (p.1172):** Documentation text page on "Behavior of irrelevant utterances," "Conflict review" (with a Cross-model Conflict Review Note), and NO_INTENT handling. No standalone screenshot.

**Figure (p.1173):** Screenshot of the **Tune your model** card on the model overview, listing sub-items ("You have utterances that need feedback," "Give feedback on predictions...," "Improve model quality by adding feedback...") with a highlighted **Tune Model** button (purple box). Illustrates the Tune your model entry point.

**Figure (p.1174):** Screenshot of the model **Settings** tab for "HR NLU for VA EFL1" (Model details / Settings). Shows Name, Short description, Language (English - en), Created for (Virtual Agent), Business area (optional), an **Ignore punctuation** checkbox (checked), and the **Model threshold settings** section with **Provided type** options **Automatic (Optimal)** and **Manual** plus a Confidence Threshold(%) field and **Save** button. Illustrates model and threshold settings.
