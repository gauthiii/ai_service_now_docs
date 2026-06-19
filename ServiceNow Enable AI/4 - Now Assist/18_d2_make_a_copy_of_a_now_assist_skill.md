# Make a copy of a Now Assist skill

_Source pages: 168–172 | Depth: 2_

---

<!-- page 168 -->
Chat summarization skill configuration panel
5. Proceed to the next step when you've finished configuring the current step by selecting Save
and continue.
You can return to a previous step by selecting Back.
6.Apply the new settings after reviewing your changes by selecting Done.
Result
The skill is activated with your preferred settings. You can now install other plugins or activate
other skills.
Make a copy of a Now Assist skill
The 'Make a copy' feature enables you to create a copy of a Now Assist skill so that you can
experiment with skill settings and configure the skill to fit your business needs.
Before you begin
Role required: sn_generative_ai.nsa_admin
About this task
The skills that come with the Now Assist applications have default configurations that are
optimized to serve the most common use cases. If you want to change the skill settings, you can
edit a skill with the Now Assist Admin console or you can create a copy of the skill. Creating a
copy leaves the original skill configuration intact in case you want to use it later or want to create
another copy from the original. You can activate and configure the copies of the skills by using
the same guided setup as the default skills.
Note: The 'Make a copy' feature is not available for all Now Assist skills.

<!-- page 169 -->
Note: In a default scenario, only one version of a skill can be active at a time. If you create
and activate a copy of the skill, any previously activated version of the skill is deactivated.
Procedure
1.Navigate to All > Now Assist Admin > Features.
If you’re already in the Now Assist Admin console, select the Now Assist Features tab.
2. In the navigation pane, select the workflow of the skill that you want to copy, such as
Technology or Customer.
3. On the feature card that contains the default skill, select View details.
4.In the All available skills or Active skills section, select the more options icon next to the
skill that you want to make a copy of and select Make a copy.
Note: Only one version of a skill can be active at a time. If you create and activate a
copy of the skill, any previously activated version of the skill is deactivated.
5. In the modal, select Make a copy.
Result
A copy of the skill is generated and you're taken to the guided setup.
What to do next
Continue the steps in the guided setup to activate the skill. For more information, see Activate a
Now Assist skill.
If you're making a copy of the case or incident summarization skill and would like to learn more
about your options, see the documentation for configuring record summarization.
Configure case or incident summarization in the Now Assist Admin console
Configure case or incident summarization by using the guided setup in the Now Assist Admin
console. You can choose the input tables and fields as well as customize the prompt output for
copies of the record summarization skills.
https://player.vimeo.com/video/996395898?
h=e609c55303&badge=0&autopause=0&player_id=0&app_id=58479
Before you begin
You can only customize the input data and prompt output for a copy of a record summarization
skill. To learn more about making a skill copy, see Make a copy of a Now Assist skill. After you
create a skill copy, you can learn the steps to complete the skill setup here.
Role required: nsa_admin
About this task
By default, many settings for Now Assist record summarization are optimized for general use
cases. Review your goals for incorporating generative AI on your instance to determine whether
you want to make changes and what those changes are. After you have made a plan, you can
create a copy of a skill and modify the input sources and prompt output.

<!-- page 170 -->
Procedure
1.In the Name of the skill field, enter the skill name.
The default name adds (copy) to the end of the original skill name. For example, Case
summarization (copy). Changing the name to be more specific makes it easier to identify later if
you want to make changes.
2. Optional: Add a description for the skill.
3. Go to the next step by selecting Save and continue.
4.Choose the input fields and data sources for each input template.
The default options are selected for you. Some options are read only. After you make any
changes to the input template, you can save your work by selecting Save template.
a.Select an input template.
The three default input templates are for new records, records that are in progress, and
closed records.
b.Add the base input table fields by selecting New base input field, choosing a field, and
entering a field description.
Each base input table field requires a description. The description informs the large
language model (LLM) what the field is for and how the information should be interpreted.
The more information that you put in the description means that the model has more context
for the data.
c.Add or modify the rule conditions for the base table.
The rule conditions determine when the input template is used. Record summarization is
only available to the records that match the rule conditions of an input template.

<!-- page 171 -->
d. Optional: Add additional input data sources by selecting New data source and choosing
either Related Table or Activity: Email.
(Optional) Each related table is configured with input fields and descriptions. More specific
descriptions for related tables help provide more context to the LLM. Activity fields, such as
Email, don't have input fields that you can configure.
e. Optional: Add a filter condition to the related table.
(Optional) You can add more rule conditions to the related table. These rule conditions
determine whether the data from the additional data source is incorporated into the

<!-- page 172 -->
summary. You can generate summaries on cases that don't match additional data source
rule conditions as long as the base table rule conditions are met.
5. Select Save and continue.
6.Choose prompt output sections to appear in summaries by moving a prompt section in the
Available prompt sections list to the Final prompt sections list.
You can reorder sections by dragging the boxes in the Final prompt sections list. Some input
templates have sections that are marked with the lock icon ( ). These sections must appear
in the final summary, but you can still reorder them with any sections you have added.
7.In the Test response panel, select a record from the Choose a record field.
8.Generate a summary for the chosen record by selecting Run Test.