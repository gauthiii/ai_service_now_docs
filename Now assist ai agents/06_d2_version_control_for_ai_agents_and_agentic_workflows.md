# Version control for AI agents and agentic workflows

_Source pages: 22–24 | Depth: 2_

---

<!-- page 22 -->
•Improves consistency and quality of agentic and generative AI features by using the best
examples from groups of records.
•Reduces the cost of LLM calls by only executing on the representative records.
•Scales to accommodate large amounts of data because selected records can represent any
size cluster.
Skills used in GAF
Multiple skills are involved in GAF setup and execution. They are modular, so not all executions
will use all skills, but they can be used together in tandem. These skills are used exclusively for
GAF and currently cannot be included on their own in custom agentic workflows.
Grouping skill
Clusters related records using machine learning techniques.
Topic-labeling skill
Adds human-readable names to the clusters using an LLM to make the clusters
easier to identify.
Action strategy skill
Selects representative records from each cluster for the mapper and reducer skills
to use.
Action mapper skill
Runs LLM inference calls for the selected representative records, producing a
record summary for the selected records.
Action reducer skill
Uses the generated summaries created by the mapper skill to produce a single
summary for the entire cluster.
GAF and Now Assist in AI Search
GAF uses AI Search to improve its effectiveness and can use it as a fallback option in case GAF
does not return any results. GAF can work without Now Assist in AI Search, but if it is enabled
then GAF has optimized prediction. The optimized prediction feature increases clustering
capacity up to 500,000 records and improves recall speed.
See Install Now Assist in AI Search and Set up AI Search for Group Action Framework for more
information on configuring AI Search for GAF.
Version control for AI agents and agentic workflows
Version control enables you to track changes made to instructions sent to the LLM for AI agents
and agentic workflows.
Version control overview
When creating an AI agent or agentic workflow, the List of steps field is important because
it provides the context necessary for the large language model (LLM) to accomplish tasks. You
can use version control to create multiple versions of the List of steps field in the guided
setup. Tracking your changes with version control helps enable you to experiment and test new
instructions. You can create versions, edit and refine versions, and revert to previous versions as
needed.

<!-- page 23 -->
Version control modal
Creating versions
You can create a version by selecting View versions > New version in the guided setup of an
AI agent or agentic workflow. Doing so brings up the Create a new version modal where
you can name the version and make changes. Naming your version enables you to identify what
changes were made to make it easier to track.
You can choose to make the new version active immediately by selecting the Set as active
toggle.
For more information about writing effective descriptions and instructions, see General
guidelines for creating AI agents and agentic workflows.
When creating a new version, you also have the option to use Now Assist to refine your current
List of steps. You must already have an active version for this option to be available.
Selecting View versions > Refine version brings up the modal where Now Assist generates and
displays a new List of steps for you to review. You can change any of the generated text, or
you can use it as it was generated. Select Create to use the new, refined version.

<!-- page 24 -->
Create a new version modal
Changing between versions
When you have multiple versions of the same List of steps field, you can switch which one
is active at any time. Choosing to make a new version active enables you to test it and evaluate
its effectiveness.
If you’re updating an agentic workflow, you can execute an agentic evaluation run to measure
performance.
You can decide which version is active by selecting View versions in the guided setup. Toggle
the Set as active field and save your changes to make the new version active.
Testing different versions
You can test different versions of an agentic workflow or AI agent from the AI Agent Studio
Testing page. The Version selector dropdown displays both active and inactive versions with
the currently active version marked as (Active). You can also start evaluation runs for specific
versions by selecting Set up evaluation run.

> **[Screenshot: Version control modal — View all versions]**
> A modal dialog titled "View all versions" with an X close button. Left sidebar shows four section tabs with radio buttons: "Section 8" (selected, filled circle), "Section 6" (empty circle), "Add sections" (empty), "Expertise" (filled/dot indicating active). Main content area shows fields: "Version number: 4", "Updated by: abel.tuter", "Updated on: 6/26/2025", and a "Set as active" toggle (currently off). "Version name *" field contains "Section 8". "List of steps * ⓘ" with "Instruction for LLM" link top-right. A multi-line text area shows: "Section 1: Incident Logging / 1. Create a new incident record in the system. / 2. Enter the date of the incident… / 3. Enter the time… / 4. Enter a description… / 5. Enter the reporter's information… / 6. Assign a unique identifier… // Section 2: Incident Assignment / 7. Identify the type of issue reported…" (text truncated). Footer buttons: "View version logs ↗" link (left), "Cancel" and teal "Save" buttons (right).

> **[Screenshot: Create a new version modal]**
> Modal dialog titled "Create a new version" with X close button. Fields shown: "Version number: 2", "Created by: abel.tuter", "Created on: 6/24/2025", and "Set as active" toggle (ON, blue). "Version name *" field contains "New Section 8". "List of steps * ⓘ" with "Instruction for LLM" link top-right. Same multi-line steps text area as View all versions modal, showing Section 1: Incident Logging (steps 1-6) and beginning of Section 2: Incident Assignment (step 7). Footer: "Cancel" and teal "Create" buttons.