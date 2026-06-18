# Multilingual Model Management

_Source: ServiceNow Now Assist documentation, pages 1175-1188._

## Overview

Multilingual Natural Language Understanding (NLU) models let the system understand user input in several languages. The NLU Workbench helps you manage and maintain a consistent structure for content across languages so you can provide a unified experience.

Multilingual model management provides a way for you to group, oversee, and update your NLU models.

### Primary and secondary languages

- A **primary language** is the source language you choose when creating a model. Models that use a primary language are considered **primary models**.
- Primary models can be translated into different languages. Those translated models are referred to as **secondary models**, and the languages in which they are translated are referred to as **secondary languages**.
- The NLU Workbench home displays primary and secondary language models nested under the model name. Select the arrow to the left of the model name to expand the language group.

The designation for the model language works as follows:

- **Primary models** have a language you assign to them during model creation, listed as `English (Primary)`. The language of the primary model is the source language for the translations that follow later in the secondary models.
- **Secondary models** are translated copies of the primary model. Each secondary model uses a different language, such as Brazilian Portuguese, Polish, or Finnish.
- Any supported language can be the primary language for a primary model or the secondary language for a secondary model.
- Within a model group, you can't have two secondary models that use the same language.

For more information on the languages available in NLU, see *NLU language support*.

## Features

- **Language grouping** to organize various language versions of models into primary and secondary models, indicating the primary language and primary model for the group. (Grouping languages is optional.)
- **Primary-to-secondary content synchronization**, so the names of intents and entities stay consistent across all models in a group.
- **Translation of models** using one of several translation modes (Use AI, Use a third party, or No translation).
- **Review workflow** that flags secondary models, intents, and vocabulary with a `Needs review` state until they are manually reviewed before publishing.
- **Model language navigation** via a drop-down list on the Model details page to move between languages in a model group.
- **Duplication** of primary models, secondary models, and entire model groups (using the `nlu_admin` role).
- **Editor delegation**, where an `nlu_admin` assigns the `nlu_editor` role to users to review and edit translations.
- **Importing primary model content to secondary models** after the initial translation, so updates can be pushed without retranslating the entire primary model.

### Multilingual language support

- Multilingual models are supported in **17 languages**.
- Some of these languages support only intents, not entities. If the language is intent-only, your primary model entities will not be translated or copied. For more information, see *NLU language support*.

## Functionalities

### Implementing language grouping

There are two methods for ensuring that model languages are grouped:

- You can add a language to a primary model in the model's **More options** menu, which automatically creates a secondary language model with translation options. For more information on adding and translating a language, see *Translate a multilingual model*.
- You can access the instance model migration page directly by visiting:
  `<instance_name>.service-now.com/$nlu-studio.do#/model-migration`.
  For more information on language grouping using this method, see *Model language grouping*.

### Primary and secondary model interactions

To ensure consistency within a model group, the names of intents and entities in all secondary models are the same as the content in the primary model.

- New intents can only be created in a **primary model**. Creating an intent in a primary model adds the intent to all the secondary models within the model group, but without any utterances in them. New intents are inactive by default.
- New entities can also be created in secondary models for languages that support entities. Adding an entity in a primary model creates it across all secondary models within the model group, if valid.
- When you add an intent to a primary model, the intent is added to all of its secondary models. Every intent in a secondary model is mapped to its corresponding intent in the primary model. This mapping ensures that any application that uses these intents can access all the secondary intents through their corresponding primary intents.
- When you delete an intent or entity in a primary model, its corresponding intents and entities are also deleted in its secondary models. The secondary models follow the status of the primary model content. Although you can't delete intents in secondary models, you can deactivate them.
- You can't delete an entity created in a secondary model if it's a copy of a corresponding entity created in the primary model. However, you can add or delete an entity in a secondary model if it doesn't have a corresponding entity in the primary model.
- Whenever you translate a model or add intents and entities to secondary models, the model must be reviewed. Secondary models marked with **Needs review** must be manually reviewed before publishing.
- If every intent in a secondary model is deactivated, then the **Train** and **Try** buttons are also deactivated in the model. However, even if only one intent is enabled in the model, you can train and test the model. Ensure that some intents are enabled in your secondary models to translate them.

> **Note:** When training and testing, prediction scores for similar utterances across primary and secondary models can be different. The context comes across differently among languages due to inherent structural variations.

For more information on intent interactions, see *Import primary model content to a secondary model*.

#### Navigating between languages

When looking at a model, you can navigate between languages in the model group. On a **Model details** page, use the **Model language** drop-down list to navigate to other models.

### Duplicating grouped models and model groups

Using the `nlu_admin` role, you can duplicate primary models, secondary models, and entire model groups. You can duplicate just the primary model or a set of secondary models from among the model group.

System behaviors you may encounter when you duplicate these models:

- If you duplicate a secondary model that's in a model group, the duplicated version becomes a separate primary model that is outside that model group.
- All intents are duplicated. The duplicated intent maintains the same **Enabled** status as the original intent.
- When duplicating a primary model, you can duplicate a set of secondary models, or all of the secondary models along with it. This action creates a model group comprised of duplicated versions, with the respective original models marked as the source models.
- When duplicating a model group, you can choose an existing secondary model to be the primary model for the duplicated group.
- If you select a secondary model in an existing model group as a new primary model while duplicating the group, all the deactivated entities are enabled for the duplicated version of the secondary model. The secondary model becomes the primary model in the new duplicated model group.
- If you duplicate a primary model without any secondary model, the duplicated version becomes a separate primary model.

For more information, see *Duplicate an NLU model*.

### Translation modes

To translate a primary model and create a secondary model, you must choose a translation mode. The modes appear in the user interface as individual cards used in Step 4 of the translation procedure. Activated cards appear surrounded by a thin green border; only activated cards can be selected as your translation mode. For the **Use AI** and **Use a third party** modes, selecting the **Add** button on an activated card starts the translation.

The **No translation** mode is active by default and available for all languages. The **Use AI** and **Use a third party** modes are activated only when the Localization Framework (LF) settings for the secondary language are in place.

> **Note:** Before you add a new model in a secondary language, you must ensure that the Localization Framework (LF) settings for the secondary language are completed.

| Translation mode | Description |
| --- | --- |
| **Use AI** | Translate using machine-intelligence providers such as Google. Selecting the card creates a translated secondary model. Machine translations may be incorrect or too literal, so review the translated content for accuracy. For more information, see *Dynamic Translation*. To activate the Use AI mode, Localization Framework must be configured and activated. |
| **Use a third party** | Request translation by a professional translation team. When you select this mode, an LF task is created per the LF language group settings for the secondary language. When the translations are completed, the translated model is created and ready for review. For more information, see *Localization Framework* and *Translation modes*. |
| **No translation** | Default. Manually translate your primary language into a secondary language. Selecting this mode creates a draft secondary model with the intent names the same as that of the primary model. These intents are disabled by default, and you must enter your utterances manually. Names of intents and names of entities imported from the primary model aren't editable. Names of entities that you create directly in the secondary model are editable. This mode is also helpful if you want to draft and save the primary model first, and then translate your utterances later. |

### Roles

| Role | Capability |
| --- | --- |
| `nlu_admin` | Full management: create, add, publish, delete, and duplicate models; translate models; import primary content to secondary; assign editors; group/duplicate models; enable/disable intents in any model. Required to initiate translation, duplicate models, and group models. |
| `admin` | Equivalent permissions to `nlu_admin` for translating and importing content (listed as an accepted role for those procedures). |
| `nlu_editor` | Delegated content work on assigned models only. Can train/test the model, mark items as reviewed, modify the confidence threshold, edit content, and review translations. Cannot create, publish, or delete a model; cannot initiate a translation; cannot assign editors. |

### What an assigned NLU editor can do

When assigned to a model, the `nlu_editor` can:

- Train and test the model.
- Export an NLU model as CSV.
- When a model or intent is in the **Needs review** state, mark it as **Reviewed**.
- Modify the model's confidence threshold.
- Edit the model name and description in **Settings**.
- Review, edit, and approve translated utterances.
- Add, edit, and delete training utterances.
- Annotate training utterances (add references to NLU vocabulary and NLU entities).
- Update entity properties (except the entity name in a secondary model).
- Add, edit, or delete the model's vocabulary.
- View the **Vocabulary sources** module (read only).
- Add, activate, and de-activate NLU intents in primary and secondary models.
- Resolve conflicting intents; also access the **Cross-model Conflict Review** module.
- View the **Irrelevance detection in NLU** module.
- Add, edit, or delete a test utterance in a test set; also access the **Multi-model Batch Testing** module.

> **Note:** The editor must be assigned to a model and in the model's application scope to take these actions, unless otherwise indicated.

The `nlu_editor` **cannot** do the following:

- Create, add, publish, or delete a model.
- Duplicate a model.
- Translate a model (initiate a translated secondary model).
- Import primary model content to a secondary (translated) model.
- Sync or edit vocabulary sources.
- View model performance.
- Provide feedback in NLU Expert Feedback Loop.
- Manage other editors, such as assigning an editor to a model or removing an editor from a model.

Additional editor assignment rules:

- You must assign an editor at the individual model level. You can't assign an editor at the model group level.
- The following models can't be assigned to an editor: **prebuilt models**, and **models that have a translation in progress**.
- You can assign up to **four editors** to a model at one time.

### Intent enablement behavior

An intent's state is represented in the **Enabled** column. Enabling of intents works in the following ways:

- Intents created in primary models are active by default.
- Intents from primary models are automatically created, but not enabled, in their secondary models (pending import).
- Disabling an intent in the primary model disables the corresponding intent in all secondary models.
- If an intent is disabled in the primary model, the intent can't be re-enabled in a secondary model.
- Enabling a disabled intent in the primary model does not enable the corresponding intents in the secondary models.
- Disabling intents in secondary models has no effect on the primary model or other secondary models.
- Secondary model intents that are marked with **Needs review** are disabled by default.
- If you disable a primary model intent that is mapped to a Virtual Agent (VA) topic, a confirmation message appears.
- If you disable a secondary model intent that is mapped to a VA topic, a confirmation message appears.
- NLU admins can enable and disable intents in any model.
- NLU editors can enable and disable intents only for models they are assigned to.

### Review workflow components

- **Mark as reviewed / Reviewed / Unmark Reviewed:** When a secondary model intent is reviewed, click **Mark as reviewed** to move the intent into the **Reviewed** state. You can undo this with the **Unmark Reviewed** button, but only if you remain on the Intent screen. If you leave the screen prematurely, the **Unmark Reviewed** button disappears and you won't be able to retrieve it.
- **Vocabulary review:** The editorial review also includes the **Vocabulary** section on the Model screen. Vocabulary translated from the primary model to the secondary model is marked with an **orange dot** and the **Needs review** state. You can edit or delete vocabulary items even while in review. After reviewing, click **Mark all reviewed** to mark all at once, which makes the orange dot disappear from the Vocabulary section.
- **Reviewed-intents counter:** Above the list of intents, a box shows a running count of the intents that need review (for example, `0 of 5`), which increases as you mark intents reviewed.

> **Note:** The **Train** and **Try** buttons on the Model screen are disabled until the vocabulary is reviewed, and the intents in the **Needs review** state are either reviewed or disabled.

> **Note:** When a model is in the **Needs review** state, it can't be trained, tested, or published. When it moves out of the **Needs review** state, you can then train and test the model.

> **Note:** An NLU editor can't create or publish a model. Only the NLU admin has permission to do this.

### Reviewing your grouped models

There are two things you can do on the **Review how we've grouped your models** screen when using the `nlu_admin` role:

- **Review and edit current model language groups** in the upper section. For existing language groups, any intent and entity mappings from Virtual Agent (VA) are displayed. To update VA mappings or to make one of the secondary languages the primary language in the group, select the **Edit** button. The page titled **Review what's in this grouping** opens. When you complete your edits, select the **Save** button.
- **Manually group models** in the **Here are your other models** section of the screen. Scroll down the page to view this section, if necessary. To set up a language grouping for a model, expand its **Group** button. The Group function opens the page titled **Group what's in these models**. You can expand the list of possible **Secondary models**, and then select the **Save** button. Any new groups are displayed in the upper section of **Review how we've grouped your models**, after refreshing the page.

> **Note:** The time it takes the system to group your models depends on the number and size of your models.

### Navigation paths and settings

- **NLU Workbench Models:** `All > NLU Workbench > Models`
- **Model migration / language grouping page:** `<instance_name>.service-now.com/$nlu-studio.do#/model-migration` (opens the page titled *Review how we've grouped your models*)
- **Localization Framework plugin:** `com.glide.localization_framework.installer`

## Instructions / Procedures

### Translate a multilingual model

Add a language to an existing NLU model by translating it. Use one of several translation options to add a secondary model in a supported language.

**Before you begin**

- Activate the Localization Framework (`com.glide.localization_framework.installer`) plugin. See *Localization Framework*.
- In your target application scope, create a primary language model, or use an existing primary model.
- Multilingualism is available for Virtual Agent and AI Search models.
- Role required: `nlu_admin` or `admin`.

> **Note:** The `nlu_editor` role cannot initiate a model translation, because the `nlu_editor` does not have permission to create a new model. See *Assign an NLU editor to a model*.

**About this task**

Translating a model creates a secondary model of the language you choose, in the same application scope as the primary model. The secondary model contains the same content as the primary; however, the intents of the secondary model are disabled and must be reviewed prior to publishing the secondary model.

In this example scenario, your primary model uses the English language and you're adding a version in the French language, without translating utterances.

**Procedure**

1. Navigate to `All > NLU Workbench > Models`. The Virtual Agent tab opens by default. If appropriate, select the **AI Search** tab.
2. Identify a primary model to which you want to assign a secondary language.
3. In the row of the primary model, select the more options menu, then select **Add a language**.
   > **Note:** You may need to scroll to the right to find the more options menu.
4. In the **Add a language to this model** window, choose the desired language for the secondary model and the translation method.
5. Select the **Add** button. The secondary model is created and the **Build and train your model** phase of the secondary model loads.

**What to do next**

If you chose to enable the model without translation, you must manually enter training utterances for each intent. If you choose to use software or a third-party translator, you must review the translations before you can continue working on the model.

Entering training utterances and reviewing secondary models can be delegated to users who have the `nlu_editor` role. For more information, see *Assign an NLU editor to a model* and *Resolve intent issues*.

### Enable or disable a secondary model intent

Enable and disable intents in your NLU models to make them active or inactive. Disable intents while editors or admins edit, review, or update content and translations.

**Before you begin**

Role required: `nlu_admin` or `nlu_editor`.

**About this task**

NLU admins and NLU editors can enable or disable intents in secondary models. If an intent is disabled, the model doesn't use it to make predictions, and it can't be accessed by any ServiceNow application using the model, such as Virtual Agent or Search.

Disabling intents gives editors time to review the intent translations and update them if needed. When you're satisfied with the content, enable the intent to make it accessible to other NLU models and ServiceNow applications.

In this review example, you have a list of disabled intents in the **Needs review** state. The goal is to review the translated content for a secondary model. When you complete your review, or if the content is fine as it is, you click **Mark as reviewed**, which moves the intent into the **Reviewed** state.

In this example scenario, you have applied the Use Software translation mode to translate a secondary model into the Japanese language. Because the translation hasn't been reviewed yet, the system marks the intents and the model with the **Needs review** state. In this example procedure, you're reviewing the intents in a model one at a time.

**Procedure**

1. Navigate to `All > NLU Workbench > Models`.
2. Locate one of your secondary models that has already been translated. In this example scenario, you locate the **Virtual Agent Conversation Setup JA** model. In the **Intents** section there is a list of five intents marked with the **Needs review** state, and a box above the list shows a running count of the intents that need review.
3. Click an intent **Name** so you can access the intent content. In this scenario, you click the **#End Conversations** intent name.
4. Review the secondary language translations of the model utterances, entities, and vocabulary, then update the content as needed. When you finish your review of the intent, the **Mark as reviewed** button appears.
5. Click **Mark as reviewed**. **Result:** The system updates the **#End Conversations** intent from the Mark as reviewed state to the **Reviewed** state. In addition, the reviewed intents box changes its running count from `0 of 5` to `1 of 5`.
6. If you're satisfied with your intent review, click the **Enable** button so the intent is available and can be accessed by any application, such as Virtual Agent (VA) or Search.

**What to do next**

Repeat Steps 1 through 6 for the four remaining intents in the list. As each intent review completes and is marked with the **Reviewed** state, the running count in the intents reviewed box increases toward `5 of 5`.

### Assign an NLU editor to a model

Assign an editor to review your NLU model translations and edit model content. Delegate the maintenance, testing, and optimization of model content to an editor.

**Before you begin**

- Create a model, or use an existing one. For translation review, create both primary and secondary (translated) models. For more information on multilingual model groups, see *Multilingual model management*.
- Assign the `nlu_editor` role to users. See *Assign a role to a user*.
- Role required: `nlu_admin`. The `nlu_editor` can't assign another editor to models.

**About this task**

The `nlu_admin` can delegate model content work to an `nlu_editor`. Assign language specialists as editors to review the consistency between primary and secondary (translated) models, or further localize the translation by editing intents and utterances. Delegate the maintenance of an existing model's content without affecting the model's published status.

First, an admin assigns the `nlu_editor` role to a user. Next, the NLU admin assigns the editor to a model. You must assign an editor at the individual model level — you can't assign an editor at the model group level. Prebuilt models and models that have a translation in progress can't be assigned to an editor.

In this example procedure, you add an NLU editor to a secondary model that needs reviewing.

**Procedure**

1. Navigate to `All > NLU Workbench > Models`. The Virtual Agent tab opens by default. Select the appropriate tab for your model.
2. Locate the name of your NLU model and scroll to the right end of its row. If your model is in a multilingual group, expand the group to find the individual model. Editors cannot be assigned to groups.
3. Select the model's **More options** menu, then select **Manage editors** in the list.
4. In the **Add editors** window, use the drop-down list and search bar to add the names of the editors you want to assign to the model.
5. Select **Add**. The editor is assigned to the model. A banner acknowledgement displays at the top of the screen. To add more editors, or remove editors, repeat this procedure.

**What to do next**

Assign more editors to the model, if necessary. You can assign up to four editors to a model at one time. To add more editors, or remove editors, repeat the above procedure.

### Import primary model content to a secondary model

When content in your primary NLU model is updated, you can import the updates directly to secondary models.

**Before you begin**

- Activate the Localization Framework (`com.glide.localization_framework.installer`) plugin. See *Localization Framework*.
- For Virtual Agent or AI Search models, create or use an existing primary model that has at least one secondary model.
- Role required: `nlu_admin` or `admin`.

**About this task**

You can import content from a primary model to a secondary model after the initial translation. If you modify the primary model, those changes can be imported to your secondary models without the need to translate the entire primary model once again. You can import primary model content to only one secondary model at a time.

**Procedure**

1. Navigate to `All > NLU Workbench > Models`. The Virtual Agent tab opens by default. Select the appropriate tab for your model.
2. Access a secondary model that has been translated under the primary model, and on **Build and train your model**, select **View phase**. By default you are taken to the **Intents** tab.
3. Select the **Check primary model for new content** button.

### Model language grouping (review and designate groups)

Language grouping makes it easier to manage your multilingual NLU models. You can review existing language groups and designate new language groups. Language grouping organizes your NLU models into primary and secondary models, and indicates the primary language and primary model for the group.

If you have added a new language to a model, a language group is created automatically, so you may already have existing language groups. For more information on adding and translating a new language model, see *Translate a multilingual model*.

To view current language groups and inspect possible new language groups, navigate to:

`<instance_name>.service-now.com/$nlu-studio.do#/model-migration`

The page titled **Review how we've grouped your models** opens. (See *Reviewing your grouped models* under Functionalities for the two available actions: editing current groups, and manually grouping models.)

## Figures, Diagrams & Screenshots

**Figure (p.1175) — Breakdown of current results (two bar-chart graphics):** A panel titled **Breakdown of current results** containing two side-by-side bar charts. The left chart is labeled "How is this prediction made with the current threshold?" and the right chart is labeled "How will this prediction look with the recommended threshold?" Each chart plots colored vertical bars (blue/red/grey series) representing prediction percentages across categories, with a legend at the bottom. This illustrates how test results compare a model's current confidence threshold against a recommended threshold, and how applying the recommendation may shift prediction percentages.

**Figure (p.1176) — Virtual Agent models list:** A screenshot of the NLU Workbench **Virtual Agent models** home page. A page header reads "Virtual Agent models" with a green **+ Create new model** button at top right. Below is a search bar, a "Show Prebuilt Models" toggle, and an "All languages" language filter drop-down. A models table lists rows with columns including **Model**, **Status**, **Used in VA**, **Model Type**, **Enabled Intents**, **Mapped Intents**, and **Last Modified**. Two example rows are visible — "English Primary" and "Brazilian Portuguese" — both with a Draft (Saved) status, demonstrating a primary model with a nested secondary language model and the modified dates.

**Figure (p.1177) — Viewing secondary models that need reviewing:** A table screenshot showing secondary language model rows. Columns include a key reviews/requests indicator, **Language**, and a Virtual Agent column. A row is flagged with a red/orange **Needs review** badge, illustrating how secondary models requiring review are surfaced in the list with their language and review status.

**Figure (p.1177) — Viewing model languages list:** A screenshot of a **Booking** model's **Model details** header. It shows the model name "Booking," a **Model language** drop-down list that is open, and a "updated 14 days ago" timestamp. The open drop-down displays selectable language entries: **English (Primary)**, **Finnish**, and **Brazilian Portuguese**. Below the header is a "Model details" section with an Intents row. This illustrates navigating between languages within a model group using the Model language drop-down.

**Figure (p.1178) — Review how we've grouped your models:** A screenshot of the model migration page titled **Review how we've grouped your models**. The page shows a grouped-models card/table with an example entry "VR Management RMA for Virtual Agent EN" labeled as the English Primary model, along with associated language/mapping columns and an action (Edit) control. This depicts the upper section of the model-migration screen where existing language groups are reviewed.

**Figure (p.1179) — Review what's in this grouping:** A screenshot of the **Review what's in this grouping** form. It shows a Primary model field set to an English-language model (English Primary) and rows of secondary models with their languages and intent/entity mappings (columns showing languages such as English and other secondary languages, plus mapped values). A **Save** button appears at top right. This illustrates editing the VA intent/entity mappings or promoting a secondary language to primary within a group.

**Figure (p.1179) — Group what's in these models:** A screenshot of the **Group what's in these models** form, reached from the **Group** button in the "Here are your other models" section. It shows a table of "your other models" with columns **Model**, **Language**, **Enabled Intents**, and **Entities** (e.g., a "Search custom model" with English language, 2 enabled intents, 1 entity, and a **Group** button). The grouping form lets you choose a Primary model and expand a list of possible Secondary models, with **Save** and **Cancel** controls. This depicts manually grouping models into a new language group.

**Figure (p.1181) — AI Search models with the more options menu (Add a language):** A screenshot of the **AI Search models** tab of the NLU Workbench. The page shows tabs (Virtual Agent tab, Issue Auto Resolution (IAR), AI Search), a search bar, a "Show Prebuilt Models" toggle, an "All languages" filter, and a models table with columns **Model Type**, **Enabled Intents**, **Mapped Intents**, **Last Modified**, and **Last Published**. One row's **more options** (three-dot) menu is expanded, showing a list of actions: Manage editors, **Add a language** (highlighted/outlined in red), Duplicate this model, Export model as CSV, and Delete this model. This illustrates Step 3 of the Translate procedure — selecting "Add a language" from the more options menu.

**Figure (p.1182) — Add a language to this model window:** A modal screenshot titled **Add a language to this model** with the subtitle "Choose an additional language and a translation method." It shows a **Primary language** field set to "English," an **Additional language** drop-down set to "French," and a "How to translate" row of three selectable cards: **Use AI** ("Automatically translate with AI"), **Use a third party** ("Request a translation from a professional translator"), and **No translation** ("Do not translate this utterance") — the No translation card is highlighted with a green border indicating it is active/selected. **Cancel** and a green **Add** button appear at the bottom right. This depicts Step 4 of the Translate procedure, choosing the language and translation mode.

**Figure (p.1182) — Intents list (Enabled column):** A screenshot of an **Intents list** table within a model. Columns include the intent **Name**, plus additional columns and an **Enabled** column on the right with toggle controls (one toggle highlighted in a purple/blue box). This illustrates how an intent's enabled/disabled state is represented in the Enabled column.

**Figure (p.1183) — Switch between the Reviewed and Unmark Reviewed states for an intent:** A screenshot of an intent detail screen for an ITSM model. The top shows breadcrumb/tab navigation and an intent named **#AddEmergencyContact**. At top right is a control (outlined in a purple box) for marking the intent — switching between **Reviewed** and **Unmark Reviewed** states. The body shows utterance content. This illustrates toggling an intent's review state, available only while you remain on the Intent screen.

**Figure (p.1184) — Items that require review:** A screenshot of an **ITSM** model intent screen. It shows breadcrumb/tab navigation with the ITSM model, intent content, and a highlighted action button at top right (outlined in purple) related to review. This depicts the items that require review during the editorial review of a secondary model, including intents and vocabulary in the Needs review state.

**Figure (p.1184) — The needs review state (Virtual Agent Conversation Setup JA):** A screenshot of the **Virtual Agent Conversation Setup JA** secondary model. A counter box near the top shows a running review count (`0 of 5`), and the **Intents** section lists five intents each marked with an orange/red **Needs review** badge. The first intent column shows intent names (including #End Conversations). This illustrates Step 2 of the review procedure — locating a translated Japanese secondary model whose five intents need review.

**Figure (p.1186) — Build and train your model (dashboard):** A screenshot of the **Build and train your model** phase of a model. The top displays summary tiles/metrics (counts such as number of intents, utterances, and entities). Below is a table/list of intents with columns and status indicators, plus a right-hand panel summarizing model details and actions. This depicts the model-building dashboard an NLU admin works in before assigning an editor.

**Figure (p.1187) — AI Search models with the more options menu (Manage editors):** A screenshot of the **AI Search models** tab showing the models table with columns **Model Type**, **Enabled Intents**, **Mapped Intents**, **Last Modified**, and **Last Published**. A row's **more options** (three-dot) menu is expanded, listing actions: **Manage editors** (highlighted), Add a language, Duplicate this model, Export model as CSV, and Delete this model. This illustrates Step 3 of the editor-assignment procedure — selecting "Manage editors."

**Figure (p.1187) — Add editors to the AI Search custom model ES model window:** A modal screenshot titled **Add editors to the AI Search custom model ES model**. It shows a **Language** field set to "Spanish," an **Editors** search field ("Search editors") outlined in purple, and **Cancel** and a green **Add** button at the bottom right. Beneath it a green success banner reads "Model 'AI Search Common Entities ES Copy' assigned to an editor," demonstrating the acknowledgement that appears after assigning an editor (Steps 4-5).

**Figure (p.1188) — Build and train your model (Check primary model for new content):** A screenshot of the **Build and train your model** phase for a secondary model, opened to the **Intents** tab. The page shows phase tiles/metrics at the top and an intents area, with a **Check primary model for new content** button highlighted (outlined in purple) at top right. This illustrates Step 3 of the import procedure — importing updated primary model content into the secondary model.

**Decorative elements:** The ServiceNow wordmark logo appears in the top-left header of every page (p.1175-p.1188) and is decorative.
