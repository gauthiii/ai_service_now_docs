# Exploring Natural Language Understanding

_Source: ServiceNow Now Assist documentation, pages 1070-1083._

## Overview

ServiceNow Natural Language Understanding (NLU) provides an **NLU Workbench** and an **NLU inference service** that you can use to enable the system to learn and respond to human-expressed intent. By entering natural language examples into the system, you help it understand word meanings and contexts so it can infer user or system actions.

Natural Language Understanding (NLU) is a component of artificial intelligence natural-language processing that deals with machine-reading comprehension. Predictive Intelligence uses NLU so the system can understand word meanings and word contexts to infer user or system actions.

### NLU terminology

In NLU parlance, these terms identify the key language components the system uses to classify, parse, and otherwise process natural language content.

- **Intent** — Something a user wants to do or what you want your application to handle, such as granting access.
- **Utterance** — A natural language example of a user intent. For example, a text string in an incident's short description, a chat entry, or an email subject line. Utterances are used to build and train intents and should therefore not include several or ambiguous meanings or intents.
- **Entity** — The object of, or context for, an action. For example: a laptop, a user role, or a priority level.
- **System entity** — These are predefined in an instance and have highly reusable meanings, such as date, time, and location.
- **User defined entity** — These are created in the system by users and can be built from words in the utterances they create.
- **Common Entity** — A context commonly used and extracted via a pre-defined entity model, such as currency, organization, people, or quantity.
- **Vocabulary** — Vocabulary is used to define or overwrite word meanings. For example, you can assign the synonym "Microsoft" to the acronym "MS".
- **NLU Model** — A collection of utterance examples and their associated intents and entities that the system uses as a reference to infer intents and entities in a new utterance. The NLU Workbench comes with pre-built NLU models for specific business units, such as an ITSM model. You can also create custom models.

### NLU Workbench

Use the NLU Workbench to create morphological representations of human language. These models enable you to create intents and entities expressed in natural language utterances. Any ServiceNow application can invoke an NLU model to get an inference of intents and entities in a given utterance.

Using the `nlu_admin` role, you build your models in the NLU Workbench, where you create, train, test, and publish them iteratively.

For information on how to build and use an NLU model, see: *Create an NLU model*.

### NLU inference service

Natural Language Understanding provides an NLU inference service that helps the system to understand natural language and drive intelligent actions. This service trains and predicts intents and entities for a given user utterance in your model so that its text translates into machine-understandable formats, such as APIs and parameters.

The system uses an inference API to train NLU algorithms by using sample record data to identify intents and entities that are strong candidates for accurate prediction.

### NLU model consumption

Other ServiceNow applications consume NLU model output, such as Virtual Agent.

For example, Virtual Agent administrators can configure a Virtual Agent Designer conversation flow to consume NLU models so that agent chatbots can better understand user statements in the conversation. For more information on how Virtual Agent consumes NLU models, see: *Natural Language Understanding (NLU) topic discovery in Virtual Agent*.

## Features

### Natural Language Understanding benefits

| Benefit | Feature | Users |
| --- | --- | --- |
| Use the NLU Workbench to create models for Virtual Agent and AI Search. | NLU Workbench | NLU Administrator |
| Build the model's content by adding intents, entities, vocabulary, and test set utterances. Your NLU model content determines how the model responds to user inputs. | Model Management | NLU Administrator |
| Add a language to an existing NLU model by translating it. Use one of several translation options to add a secondary model in a supported language. | Model Management | NLU Administrator |
| Virtual Agent administrators can access and update their NLU models from within the Virtual Agent Designer user interface. | Virtual Agent Integration | Virtual Agent Administrator |

### Get started (workflow categories)

The Get started overview presents four categories of tasks:

- **Explore** — Learn about NLU concepts and features.
- **Use** — Create, test, translate, and publish your NLU models.
- **Integrate** — Learn how Virtual Agent administrators can update NLU models from within Virtual Agent Designer.
- **Reference** — Learn about using models in different languages for use in other applications.

### Troubleshoot and get help

- Virtual Agent & NLU community page
- Search the Known Error Portal for known error articles
- Contact Customer Service and Support

## Functionalities

### Activation plugins

Activate the following plugins to activate the NLU Workbench. (Activate these plugins if they aren't already active in your instance.)

| Plugin | Description |
| --- | --- |
| **NLU Workbench - Core** (`com.glide.nlu`) | Installs the required tables for persisting NLU models that are created using the NLU Workbench. |
| **NLU Workbench** (`com.snc.nlu_studio`) | Enables the creation of Natural Language Understanding (NLU) models. These models can understand the intent (action) and entities (details about the action) for a given user utterance. Any ServiceNow application can invoke an NLU model. Requires the NLU Workbench - Core plugin and the NLU Common Model plugin. |
| **Predictive Intelligence** (`com.glide.platform_ml`) | Enables the NLU Service APIs used for model creation and inference. Enables the creation of machine learning solutions that are trained on data in your instance. Provides frameworks for classification, similarity, and clustering. A trained solution can be invoked by any application by using a prediction API. |
| **NLU Common Model** (`com.glide.nlu.model`) | Packages all language NLU common models. Also includes commonly used pattern entities that can be imported and used in any NLU model in the NLU Workbench. Commonly used patterns like email, phone, and ServiceNow specific pattern entities such as INT, RITM are made available. Requires the NLU Workbench - Core plugin. |
| **NLU Active Learning-Properties** (`com.glide.nlu.active_learning_properties`) | Enables the `nlu_admin` to configure the system properties for the Expert Feedback Loop application. If you don't use the Expert Feedback Loop application, this plugin is not used and can safely be ignored. For more information about the system properties for the Expert Feedback Loop, see the NLU Expert Feedback Loop documentation. |

The following two plugins are for apps associated with a for-fee subscription and are available on the ServiceNow Store. Installing these apps adds additional features to the NLU Workbench. Contact your account manager if you are interested in these apps.

| Plugin | Description |
| --- | --- |
| **Intent Discovery** (`sn_nlu_discovery`) | Delivers the Intent Discovery feature, which identifies user intents by analyzing incident/case data. Use this application to help identify which intents to model and build for Virtual Agent conversations to attain maximum deflection. For more information, see *Install Intent Discovery*. |
| **NLU Workbench - Advanced Features** (`sn_nlu_workbench`) | Delivers the Model Performance, Multi-model Batch Testing, Cross-model Conflict Review, and Expert Feedback Loop features. For more information, see *Install NLU Workbench - Advanced Features*. |

### Roles

NLU Workbench is installed with these roles. To learn more about managing per-user subscriptions, see *Managing per-user subscriptions in Subscription Management* and contact your account representative.

> **Important:** Avoid granting an admin role when more specialized roles are available.

#### NLU user [`nlu_user`]

Users who have read access to models in NLU Workbench.

- **Contains roles:** None.
- **Groups (assigned by default):** None.
- **Special considerations:** This role is installed with NLU Workbench - Core. This role does not have access to NLU Model Performance.

#### NLU editor [`nlu_editor`]

Users who can edit NLU models assigned to them in NLU Workbench.

- **Contains roles:** `import_admin`, `sn_ace.ace_user`, `nlu_user`
- **Groups (assigned by default):** None.
- **Special considerations:** This role is installed with NLU Workbench - Core.

#### NLU administrator [`nlu_admin`]

Users who can use NLU Workbench to manage NLU models.

- **Contains roles:** `sn_ace.ace_user`, `sn_nlu_workbench.nlu_feedback_admin`, `nlu_editor`, `nlu_user`
- **Groups (assigned by default):** None.
- **Special considerations:** This role is installed with NLU Workbench - Core.

#### NLU feedback admin [`sn_nlu_workbench.nlu_feedback_admin`]

Data labelling (NLU feedback) Admin role — to manage data labelling across models also ability to optimize models.

- **Contains roles:** `sn_ace.ace_user`, `platform_ml_write`, `platform_ml_create`, `ml_labeler`
- **Groups (assigned by default):** None.
- **Special considerations:** This role is installed with NLU Workbench - Advanced Features. For more information, see *NLU Workbench - Advanced Features*. This role is used in Expert Feedback Loop modules. For more information, see *NLU Expert Feedback Loop* or *Issue Auto Resolution Tuning in NLU*.

### NLU Workbench properties

Refer to these system properties for the Natural Language Understanding (NLU) application. To access your system properties, use the `admin` or `nlu_admin` role and the following path in the application navigator: **All > NLU Workbench > Settings**.

#### Model Settings

| Label / Name | Default value | Plugin | Recommended usage |
| --- | --- | --- | --- |
| Maximum number of utterances per intent<br>`glide.nlu.utterances_per_intent.value_limit` | 200 | NLU Workbench | Use fewer than 200 utterances per intent to keep your model well balanced in terms of intent size. **Note:** Value must be greater than 5 and less than or equal to 300. |
| Maximum number of records in a Table vocabulary source<br>`glide.platform_ml.api.max_nlu_lookupsource_records` | 100,000 | NLU Workbench | Keep the value under 100,000. |
| Maximum number of values in a List vocabulary source<br>`glide.nlu.static_lookup.value_limit` | 1,000 | NLU Workbench | Keep the value under 1,000. |
| Enable pre-built vocabulary for software names<br>`glide.mlpredictor.option.nlu.@LookupSources:software` | enabled | NLU Workbench | Enable pre-built vocabulary so the system can recognize software names. |
| Enable pre-built vocabulary for hardware names<br>`glide.mlpredictor.option.nlu.@LookupSources:hardware` | enabled | NLU Workbench | Enable pre-built vocabulary so the system can recognize hardware names. |

#### Advanced Settings

| Label / Name | Default value | Plugin | Recommended usage |
| --- | --- | --- | --- |
| Maximum number of records for Intent Discovery classification<br>`sn_nlu_discovery.intent_discovery_max_classification_limit` | 300,000 | Intent Discovery | Keep the number of records less than 500,000. |
| Minimum number of records for Intent Discovery classification<br>`sn_nlu_discovery.intent_discovery_min_classification_limit` | 10,000 | Intent Discovery | Use at least 10,000 records to get high quality results. |
| Minimum number of records for NLU performance analysis<br>`sn_nlu_workbench.glide.nlu.performance.min_clustering_records` | 5,000 | NLU Workbench - Advanced Features | Use at least 5,000 records to get high quality results. |
| NLU Conflict Detection - Moderate Threshold<br>`sn_nlu_workbench.glide.nlu.conflict.moderate_threshold` | .85 | NLU Workbench - Advanced Features | Must be a decimal between 0 and 1. Keep this threshold less than the Critical Threshold. |
| NLU Conflict Detection - Critical Threshold<br>`sn_nlu_workbench.glide.nlu.conflict.critical_threshold` | .95 | NLU Workbench - Advanced Features | Must be a decimal between 0 and 1. Keep this threshold greater than the Moderate Threshold. |
| The maximum number of rows in a batch test import file<br>`sn_nlu_workbench.glide.nlu.batch_test.max_import_rows` | 10,000 | NLU Workbench - Advanced Features | Make sure your batch test import file has no more than 10,000 rows. |
| The maximum number of utterances to display for feedback in the expert feedback loop<br>`glide.mlpredictor.option.nlu.activeLearning.label_candidate_table.max_response` | 300 | NLU Workbench - Advanced Features | Pull no more than 300 utterances from your users' Virtual Agent chat logs to display for feedback in the Expert Feedback Loop application. |
| The minimum number of utterances a user should review before tuning the model<br>`sn_nlu_workbench.glide.nlu.optimize.min_labeled_data` | 100 | NLU Workbench - Advanced Features | Provide and save feedback for at least 100 utterances from your users' Virtual Agent chat logs so you can execute the Tune Model feature in the Expert Feedback Loop application. |
| The maximum number of records to fetch from Virtual Agent chat logs<br>`glide.mlpredictor.option.nlu.activeLearning.va_chat_logs.max_row_limit` (default - 3000) | 3,000 | NLU Workbench - Advanced Features | If there is high NLU usage, increasing the default value to a maximum of 50,000 records will increase the data available for the active learning job to filter up on and display in the Expert Feedback Loop application to give feedback on. |
| Size limit on Label Candidate Table (used for pruning the table)<br>`glide.mlpredictor.option.nlu.activeLearning.label_candidate_table.max_data_size` (default - 10000) | 10,000 | NLU Workbench - Advanced Features | The recommended usage for this property is the same as the property above. |
| Size limit on Labeled Data Table (used for pruning the table)<br>`glide.mlpredictor.option.nlu.activeLearning.label_table.max_data_size` (default - 10000) | 10,000 | NLU Workbench - Advanced Features | The recommended usage for this property is the same as the property above. |
| Enable this property to unblock your instance during NLU model training. The training will be scheduled for an off-peak time, and we will notify you when it's done.<br>`glide.mlpredictor.scheduled.nlu.model.training` | False | NLU Workbench - Advanced Features | False |

To get more feedback data from Virtual Agent (VA) chat logs, refer to the *Procuring additional VA feedback data on demand* section in the Expert Feedback Loop documentation.

### NLU language support

The NLU Workbench application provides support for creating NLU models in different languages for use in other applications, such as Virtual Agent.

The platform supports NLU for **17 languages**. Ten of these languages available to your models have both intent and entity support; the remaining 7 languages have intent-only support. (Japanese entity support includes character annotation.)

> **Note:** Install the language plugins for languages you want to use in NLU. Installing and activating language plugins ensures that the languages are available in your instance. For more information see *Activate a language*.

- **With intent and entity support**, NLU can understand sophisticated utterances such as intent-entity relationships, system entities, and user-defined entities. NLU relays this information to Virtual Agent, and the user is usually taken directly to the conversation topic that offers resolution.
- **With intent-only support**, the focus is on intent recognition. With Virtual Agent using NLU, users are directed to the desired conversation topic, where qualifying follow-up questions may be asked before being taken to a topic that offers resolution.

Utterances for all languages are case insensitive during intent prediction.

All languages support intents, vocabulary, batch testing, NLU performance, fast training, and Virtual Agent model use.

#### NLU feature support by language

| Language | NLU feature supported |
| --- | --- |
| English | System-defined entities, user-defined entities, vocabulary sources, pre-built vocabulary, intent discovery, conflict review, expert feedback loop, Search model use. |
| French | System-defined entities, user-defined entities, vocabulary sources, intent discovery, conflict review, Search model use. |
| Spanish | System-defined entities, user-defined entities, vocabulary sources, intent discovery, conflict review, Search model use. |
| German | System-defined entities, user-defined entities, vocabulary sources, intent discovery, conflict review, Search model use. |
| Japanese | System-defined entities, user-defined entities, vocabulary sources, intent discovery, conflict review, Search model use. |
| Portuguese | System-defined entities, user-defined entities, vocabulary sources. |
| Swedish | Virtual Agent model use. |
| Italian | User-defined entities, vocabulary sources. |
| Chinese (simplified) | Virtual Agent model use. |
| Brazilian Portuguese | System-defined entities, user-defined entities, vocabulary sources. |
| Dutch | User-defined entities, vocabulary sources. |
| French Canadian | User-defined entities, vocabulary sources. |
| Polish | Virtual Agent model use. |
| Korean | Virtual Agent model use. |
| Danish | Virtual Agent model use. |
| Finnish | Virtual Agent model use. |
| Norwegian | Virtual Agent model use. |

### NLU Service updates

Refer to this documentation so you are up to date with changes to the NLU Service. The NLU Service helps the system to understand natural language and drive intelligent actions. This service trains and predicts intents and entities for a given user utterance in your NLU model so it can understand human-expressed natural language, whether spoken or written. The source of this documentation is **KB0953693**.

This service is updated independently of your instance upgrade, and without any action required by you. These updates are done on a bi-monthly basis (once every two months) to improve the quality of NLU model training and predictions. Major updates are aligned with family releases such as Rome, San Diego, Tokyo, etc. Minor updates are automatically updated so you are using the latest version when you retrain an NLU model. While most of these updates don't impact your existing use of NLU, there may be some changes you need to be aware of.

#### May 2023 NLU Service update

- Introduced dialog acts to enable natural mid-conversation in Virtual Agent (VA) and improve conversation fluidity. Affirm, negate, and modify dialog acts are supported in English and enabled by default for all new VA topics.
- Migrated all languages to use new language models, boosting average intent prediction quality by 10% across all languages.
- Enabled customers to manage and edit irrelevant utterances for their models to improve irrelevance detection.
- Removed the requirement for a model to have 2 or more intents in the model, making it easier for end-to-end topic testing in VA.

#### March 2023 NLU Service update

- Improved intent/entity detection through better handling of common words in vocabulary sources.
- Improved latency and memory utilization for system entity (NER) detection.
- Updated version support so that customers will need to use newer versions of the NLU Service and cannot point to n-2 releases older than their current glide version.

#### January 2023 NLU Service update

- Created the new DATE-TIME system entity (English only) for use in Virtual Agent.
- Added vocabulary source and entity support (simple, mapped, and open ended) for the Dutch and Italian languages, and system entity support for Portuguese and Brazilian Portuguese.
- Upgraded the ServiceNow Language Model for the Danish, Swedish, Finnish, and Norwegian languages, improving their average prediction quality by 17% from Tokyo.
- Improved the handling of punctuation in entities and special characters in vocabulary sources.
- Incorporated feedback provided on intent predictions by admin users in the NLU Workbench to improve model training data for Virtual Agent.

### NLU models

Use NLU models to apply ServiceNow Natural Language Understanding on your instances. Create, manage, test, and publish NLU models with the NLU Workbench.

A model is a collection of utterances, intents, entities, and vocabulary that the system uses to respond to natural language inputs from your users. The model takes the natural language input from your users and matches it to actions to be performed by the system.

The utterances in your model data are examples of what your users might ask for. These examples are used to train your model to recognize which system actions to perform in response. These system actions are called **intents**.

#### NLU Workbench homepage — tabs, fields, and columns

There are three tabs on the NLU Workbench homepage: **Virtual Agent**, **Issue Auto Resolution**, and **AI Search**. The Virtual Agent tab opens by default. Select the correct tab for your application.

- **Search field** — Use the Search field to look for models by name.
- **All Languages filter** — The default setting of the All Languages filter displays all models regardless of their language. You can filter models by language using the list in All Languages. To learn more about the available languages, see *NLU language support*.
- **Multilingual grouped models** — If you have a multilingual grouped model, its row in the list of models has an arrow on the left side. Select the arrow to expand the group so that all language versions of the model are displayed. For more information on model languages and grouping, see *Multilingual model management*.
- **Used In VA column** — Indicates whether a model has already been linked to another application such as Virtual Agent. For AI Search, this column indicates whether the model has already been linked to a Genius Result.
- **Mapped Intents column** — Displays a count of intents that have been mapped or linked to Virtual Agent topics.
- **Boost your model performance section** — Scroll down the NLU Workbench homepage to view this section. It displays cards you can use to access functions that are available to your model type.

Other columns observed in the Virtual Agent models list include: **Model**, **Status**, **Used In VA**, **Model Type**, **Enabled Intents**, **Mapped Intents**, and **Last Modified**.

#### Model applications

The output of your NLU models can be consumed by the ServiceNow applications **Virtual Agent**, **Issue Auto Resolution**, and **AI Search**. The NLU Workbench homepage organizes each application's models by tab. In the list of models, different columns are displayed depending on the application.

**NLU Models for Virtual Agent** (for more information on Virtual Agent, see *Virtual Agent*):

- The tab for Virtual Agent displays a list of models. Select a model name to open an overview page for that model.
- The **Show Prebuilt Models** toggle is off by default. Switch this toggle on to display read-only models that can be copied and used as the basis for your custom models.
- The **Boost your model performance** section displays a total of 5 cards for functions available to Virtual Agent.

**NLU Models for IAR (Issue Auto Resolution):** Fewer functions and columns are displayed for IAR than for the other applications in NLU Workbench. This is because the IAR model is prebuilt and is configured in the IAR Admin console.

- When you select the name of your IAR model in NLU Workbench, you are taken to **IAR Tuning** rather than to a model overview. For more information, see *Issue Auto Resolution Tuning in NLU*.
- The **Show Prebuilt Models** toggle is not displayed.
- The **Create new model** button is not displayed because the prebuilt model is used directly.
- The section **Boost your model performance** is not displayed.

For more information on setting up IAR, see *Using Issue Auto Resolution*.

## Instructions / Procedures

### Procedure: Activate the NLU Workbench

**Before you begin** — Role required: `admin`

**About this task** — Activate the listed plugins if they aren't already active in your instance.

1. Navigate to **All > System Applications > All Available Applications > All**.
2. Find the following plugins using the filter criteria and search bar: **NLU Workbench - Core** (`com.glide.nlu`), **NLU Workbench** (`com.snc.nlu_studio`), **Predictive Intelligence** (`com.glide.platform_ml`), and **NLU Common Model** (`com.glide.nlu.model`).
   - You can search for the plugin by its name or ID. If you cannot find a plugin, you might have to request it from ServiceNow personnel.
3. Select **Install** to start the installation process.
   - **Note:** When domain separation and delegated Admin are enabled in an instance, the administrative user must be in the global domain. Otherwise, the following error appears: `Application installation is unavailable because another operation is running: Plugin Activation for <plugin name>.`
   - You will see a message after installation is completed. For information about the components installed with a plugin, see *Find components installed with an application*.

### Procedure: Access NLU models in the NLU Workbench

- Use the `nlu_admin` role to access the NLU Workbench.
- Navigate to **NLU Workbench > Models**.
- On the homepage, select the correct tab for your application (**Virtual Agent**, **Issue Auto Resolution**, or **AI Search**). The Virtual Agent tab opens by default.
- Use the **Search** field to look for models by name; use the **All Languages** filter to filter models by language.
- For a multilingual grouped model, select the arrow on the left side of its row to expand the group and display all language versions.

### Procedure: Access system properties (settings)

- Use the `admin` or `nlu_admin` role.
- Navigate via the application navigator path: **All > NLU Workbench > Settings**.

## Figures, Diagrams & Screenshots

**Decorative (recurring, p.1070–1083):** The ServiceNow wordmark logo appears at the top-left of every page. Standard copyright/trademark footer text appears at the bottom of every page (omitted from this reference per style).

**Figure (p.1071) — "Get started" tile set (Explore / Use):** Two decorative card tiles introducing the Get started workflow. The left card, **Explore**, shows a circular green line-art icon (concentric/orbit style) above the caption "Learn about NLU concepts and features." The right card, **Use**, shows a green gear/cog icon above the caption "Create, test, translate, and publish your NLU models." These tiles illustrate the first two of four entry points into NLU.

**Figure (p.1072) — "Get started" tile set (Integrate / Reference):** Continuation of the Get started tiles at the top of the page. The left card, **Integrate**, shows a green icon (gear/cycle motif) above the caption "Learn how Virtual Agent administrators can update NLU models from within Virtual Agent Designer." The right card, **Reference**, shows a green open-book icon above the caption "Learn about using models in different languages for use in other applications." Together with the p.1071 tiles, these depict the four-part Explore / Use / Integrate / Reference navigation model.

**Figure (p.1081) — "Overview of how user input is transformed to a system action" (process flow diagram):** A horizontal three-stage flow diagram with green icons connected by bold black right-pointing arrows. Stage 1 is a green speech/chat bubble icon containing three dots, labeled **"User input (natural language)."** A black arrow points right to Stage 2, a green stacked-database/cylinder icon (layered disks) labeled **"NLU model."** A second black arrow points right to Stage 3, a green laptop icon with a white checkmark on its screen, labeled **"System action or response."** The diagram illustrates the core NLU pipeline: a user's natural-language utterance is received, processed/matched by the NLU model, and translated into a concrete system action or response.

**Figure (p.1082, top) — NLU Workbench homepage / Virtual Agent models list (screenshot):** A screenshot of the **NLU Workbench** homepage. A heading reads "NLU Workbench" with the subtitle "Create, manage, and tune your NLU models to better understand what your users are saying." with a "Learn more" link. Below are three tabs: **Virtual Agent (VA)** (active/underlined in green), **Issue Auto Resolution (IAR)**, and **AI Search**. Under the tabs is the section title "Virtual Agent models" with a "**+ Create new model**" button on the right. A controls row shows a **Search** input box, a "**Show Prebuilt Models**" toggle (shown off), and an "**All Languages**" dropdown. The table header row lists the columns: **Model**, **Status**, **Used In VA**, **Model Type**, **Enabled Intents**, and **Mapped Intents**. The first data row begins to show a model with Status "Draft." This screenshot illustrates the homepage layout, tab navigation, search/filter controls, and the model list columns.

**Figure (p.1082, bottom) — Expanded multilingual grouped model (screenshot):** A second screenshot of the "Virtual Agent models" list showing an expanded multilingual group. The "**+ Create new model**" button, **Search** box, "**Show Prebuilt Models**" toggle (off), and "**All languages**" dropdown appear at the top. The column headers are **Model**, **Status**, **Used In VA**, **Model Type**, **Enabled Intents**, **Mapped Intents**, and **Last Modified**. A group row labeled "**ITSM model for Virtual Agent**" (count badge "2") has an expansion arrow (chevron) on its left, shown in the expanded/down state. Two child rows are displayed: "**English (Primary)**" — Status "Draft Saved", Used In VA "No", Enabled Intents "6", Mapped Intents "0", Last Modified "2023-06-22 12:09:54"; and "**Brazilian Portuguese**" — Status "Draft Saved", Used In VA "No", Enabled Intents "6", Mapped Intents "0", Last Modified "2023-06-26 14:22:21". This illustrates how selecting the left-side arrow expands a grouped model to reveal all of its language versions.

**Figure (p.1083, top) — "Boost your model performance" cards (screenshot):** A screenshot of the "Boost your model performance" section, displaying two cards side by side (part of a carousel; previous/next circular navigation arrows appear below, with the green right "next" arrow active). The left card, "**Tune your model**," shows a line-art icon of a document with a circular-refresh symbol and reads "Provide and gather feedback on real end-user chats from your org's subject matter experts," with a "**Go to Expert Feedback Loop**" button (with an external-link icon). The right card, "**Discover new intents**," shows a line-art icon of a list/document with a magnifying glass and reads "Analyze your users chat and task data to identify which intents you should create next," with a "**Go to Intent Discovery**" button (with an external-link icon). This illustrates the action cards used to access model-improvement functions (the Virtual Agent tab provides a total of 5 such cards).
