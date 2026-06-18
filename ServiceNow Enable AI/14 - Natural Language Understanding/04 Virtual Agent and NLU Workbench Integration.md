# Virtual Agent and NLU Workbench Integration

_Source: ServiceNow Now Assist documentation, pages 1189-1190._

## Overview

The **Virtual Agent and NLU Workbench integration** lets Virtual Agent administrators access and update their Natural Language Understanding (NLU) models from within the Virtual Agent Designer user interface. Rather than switching back and forth between separate tools, administrators can manage the NLU models that power their conversation topics directly inside Virtual Agent Designer.

This subtopic describes:

- How the Virtual Agent and NLU Workbench integration works.
- The setup tasks, roles, and details required to connect an NLU model to a Virtual Agent conversation topic.
- How to publish topics from Virtual Agent once a model is ready in the NLU Workbench.

> **Note:** If you have Now Assist in Virtual Agent, you can continue to use your existing NLU topics and migrate them into new LLM topics using the topic migration feature within Virtual Agent Designer. For more information on topic migration, see *Migrate NLU topics to LLM topics*.

## Features

The integration provides the following capabilities:

- Access and update NLU models from within the Virtual Agent Designer user interface.
- Create NLU models and their associated intents in the NLU Workbench for use in conversation topics.
- Apply an NLU model to a conversation topic by selecting the model, intent, and topic switching behavior in Topic Properties.
- Configure entity extraction by setting NLU properties on input controls used in the topic flow.
- Optionally activate **Dialog Acts** so Virtual Agent can respond flexibly when users make a modification mid-conversation.
- Update NLU intent utterances from within Virtual Agent Designer (after the model is associated with a topic).
- Train, test, and publish the NLU model from within Virtual Agent Designer.
- Map a published model and intent to a topic and publish it seamlessly with a single Publish action.
- Continue to use existing NLU topics, with the option to migrate them into new LLM topics (when Now Assist in Virtual Agent is available).

## Functionalities

### Required roles

- Creating an NLU model and its associated intents in the NLU Workbench requires the **admin** or **nlu_admin** role.
- After the NLU model is complete and associated with a Virtual Agent conversation topic, administrators with the **virtual_agent_admin** or **admin** role can update NLU intent utterances and train, test, and publish the NLU model from within Virtual Agent Designer.

### Components and tools involved

| Component | Role in the integration |
| --- | --- |
| **NLU Workbench** | Where administrators create the NLU model and its associated intents, and where the model is published before it can be used. |
| **Virtual Agent General Settings** | Where NLU is enabled, the NLU service provider is selected, and languages are enabled for language-specific NLU models. |
| **Virtual Agent Designer** | Where administrators apply the NLU model to a conversation topic (via Topic Properties), set entity extraction on input controls, update utterances, and train/test/publish the model. |
| **Topic Properties** (in Virtual Agent Designer) | Where the NLU model, the NLU intent, the topic switching behavior, and Dialog Acts are selected/configured for a topic. |

### Virtual Agent General Settings tasks

In Virtual Agent General Settings, administrators must complete the following:

- Enable NLU.
- Select the NLU service provider.
- If using language-specific NLU models, enable the languages for those models.

### Topic Properties / input control settings

To apply an NLU model to a conversation topic in Virtual Agent Designer:

- In **Topic Properties**, select the NLU model, the NLU intent, and the topic switching behavior.
- For input controls used in the topic flow, set the NLU properties for entity extraction.

### Dialog Acts

Optionally, administrators can activate **Dialog Acts** to enable Virtual Agent to respond flexibly when users make a modification in mid-conversation.

- Currently available response types are **Modify**, **Affirm**, and **Negate**.
- Responses are based on the last **5 exchanges** in the conversation.
- Dialog Acts can be configured for **English only**, in Topic Properties.
- For more information, see *Dialog Acts for Virtual Agent*.

### Actions available after model association

After the NLU model is complete and associated with a Virtual Agent conversation topic, administrators with the **virtual_agent_admin** or **admin** role can do the following from within the Virtual Agent Designer user interface:

- Update NLU intent utterances.
- Train, test, and publish the NLU model.

For more information, see *Natural Language Understanding (NLU) topic discovery in Virtual Agent*.

### Publishing behavior

When your model is published in the NLU Workbench, it's ready to use in Virtual Agent Designer. When editing a topic, click the **Properties** tab to select a model and intent to map to that topic. When you click **Publish**, the model and intent are mapped to that topic and published seamlessly.

## Instructions / Procedures

This subtopic describes the integration conceptually and lists the configuration tasks rather than presenting a single numbered, step-by-step walkthrough. The required tasks and sequence are summarized below.

### Integration setup tasks

1. **Create the NLU model and intents.** As Virtual Agent administrators create and configure their conversation topics, they must first create their NLU model and its associated intents in the NLU Workbench. This action requires the NLU Workbench and the **admin** or **nlu_admin** role.

2. **Complete Virtual Agent General Settings tasks:**
   - Enable NLU.
   - Select the NLU service provider.
   - If using language-specific NLU models, enable the languages for those models.

3. **Apply the NLU model to a conversation topic in Virtual Agent Designer:**
   - In Topic Properties, select the NLU model, the NLU intent, and the topic switching behavior.
   - For input controls used in the topic flow, set the NLU properties for entity extraction.

4. **(Optional) Activate Dialog Acts** in Topic Properties (English only) to enable flexible responses (Modify, Affirm, Negate) based on the last 5 exchanges.

5. **Maintain and publish the model from Virtual Agent Designer.** After the model is associated with a topic, administrators with the **virtual_agent_admin** or **admin** role can update NLU intent utterances and train, test, and publish the NLU model.

### Procedure: Publishing topics from Virtual Agent

1. Publish your model in the NLU Workbench. When published there, it's ready to use in Virtual Agent Designer.
2. When editing a topic in Virtual Agent Designer, click the **Properties** tab.
3. Select a model and intent to map to that topic.
4. Click **Publish**. The model and intent are mapped to that topic and published seamlessly.

> **Note (related procedure shown on the same page set — importing/translating content for secondary models):** By default, newly imported intents are disabled in secondary models. Activate any imported intents manually. To import new content into a secondary model: in the banner select **Import**; then in the *Import and translate new content from your primary model* window, choose a translation method and select **Import**. The new content begins translating, and when finished the translated content must be reviewed.
>
> **What to do next:** Make sure that each of your secondary models receive the new content from the primary model. Review all the new, translated content before publishing the secondary models.

## Figures, Diagrams & Screenshots

**Figure (p.1189):** Screenshot of the **NLU model "Build and train your model" screen** (the import/translate flow for a secondary model). At the top of the screen is a blue informational banner reading *"Import and translate the content to keep this model updated,"* with a summary of the updates in the primary model. Below the banner is a page header titled **"Build and train your model"** with action buttons on the right. The main work area shows a horizontal row of small content tiles/cards (representing intents or content blocks). A right-hand panel lists model details/status. An inline **Note** callout (yellow info icon) states: *"By default, newly imported intents are disabled in secondary models. Activate any imported intents manually."* The screenshot illustrates where the administrator selects **Import** in the banner (step 4) to begin importing new content from the primary model.

**Figure (p.1189):** Screenshot of the **"Import and translate new content from your primary model" dialog window**. The modal is titled *"Import and translate new content from your primary model."* It contains fields for choosing a **translation method**, including options such as *Translate using* with language dropdowns (e.g., an English / German selection) and radio-button choices for how to translate (for example, using machine translation / automatic translation versus using a third-party translation), plus a *"What's next?"* explanatory section describing that the content will be machine-translated and review will be required. At the bottom right are **Cancel** and **Import** buttons. This figure illustrates step 5 of the import procedure: choosing a translation method and selecting **Import**, after which the new content begins translating and the translated content must be reviewed.

**Figure (p.1190):** Screenshot of the **Virtual Agent Designer Topic "Properties" tab** used when publishing topics from Virtual Agent. The screen shows a topic editing canvas with tabs across the top (the **Properties** tab is selected). The Properties panel contains form fields for mapping NLU to the topic — including a field/dropdown to **select an NLU model** and a field/dropdown to **select an intent** to map to the topic, along with additional topic configuration options (such as topic switching behavior). The illustration demonstrates that after a model is published in the NLU Workbench, the administrator uses this Properties tab to select a model and intent, and that clicking **Publish** maps the model and intent to the topic and publishes it seamlessly.

**Decorative elements:** Each page carries the standard **ServiceNow** wordmark/logo in the top-left header and the repeated footer copyright/trademark boilerplate (omitted from this document).
