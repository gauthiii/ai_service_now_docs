# Evaluation Dashboard References
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Topic 35 of 35 | Role: AI Risk & Compliance Officer Reference

---

## What Is This?

The Evaluation Dashboard is the AI quality measurement system within AICT. It uses LLM-based automated evaluation to assess the quality of Now Assist Virtual Agent and AI agent conversations across nine defined metrics. This reference document covers every technical component of the evaluation framework: scheduled jobs, tables, system properties, business rules, flows, flow actions, script includes, evaluation metrics, score calculation methodology, and the complete flow execution logic for both single-conversation and batch evaluation.

For a Risk & Compliance Officer, the evaluation framework provides the **quality assurance evidence layer** of AI governance — the data that answers "Is our AI performing as intended?" and "Is it hallucinating, drifting, or producing incoherent responses?"

---

## Components Installed with the Evaluation Dashboard

Several types of components are part of the Evaluation tab: scheduled jobs, tables, system properties, business rules, flows, flow actions, and script includes.

---

## Scheduled Jobs

| Job Name | Schedule | Description |
|---|---|---|
| **CE Populate Value Aggregates Chats – Daily** | Daily | Randomly selects 1,000 conversations from yesterday. Extracts chat duration and classifies as small/medium/large. Classifies chats where a Knowledge article or catalog item was invoked. For evaluated chats, classifies conversations based on chat performance and populates data into the Evaluation Value Aggregates table |
| **Evaluation Value Calculation – Runs Only Once After Install** | Post-install, once | Deletes all records in Evaluation Value Aggregates, runs calculations again, stores aggregated value from the first evaluation date. Ensures baseline data is established after initial installation |

---

## Tables Installed

### Core Tables

| Label | Table Name |
|---|---|
| Evaluation | `sn_na_conv_eval_evaluation` |
| Evaluation configurations | `sn_na_conv_eval_evaluation_configurations` |
| Evaluation Metrics | `sn_na_conv_eval_evaluation_metrics` |
| Evaluation Set | `sn_na_conv_eval_evaluation_set` |
| Evaluation Value Aggregates | `sn_na_conv_eval_evaluation_value_aggregates` |

### Remote Tables

Remote tables are computed definitions, not physical storage — they calculate results on demand when queried:

| Table Name | Description |
|---|---|
| `sn_na_conv_eval_st_value_calcs` (Conversation Evaluator Value Calculations) | For the given query: calculates time savings and efficiency % for small, medium, and large chats; also returns time savings and efficiency when a Knowledge article or catalog item was invoked |
| `sn_na_conv_eval_weekly_cals` (Conversation weekly calculations) | Same calculations as above but broken down by week of the selected date range; supports weekly efficiency trend charts |

---

## System Properties

| Property | Default | Description |
|---|---|---|
| `sn_na_conv_eval.errorBandMinRecords` | **30** | Minimum number of records required to calculate the error band for upper and lower deviation. Below this threshold, adjusted scores revert to raw auto-eval scores |
| `sn_na_conv_eval.evalWeights` | — | Contains weights for each evaluation metric used in computing total or composite scores |
| `sn_na_conv_eval.maxEvaluateCount` | **200** | Maximum number of records to evaluate per day. Once this limit is hit, no further evaluations run until the next day |
| `sn_na_conv_eval.total_sampled_conv_count` | **1,000** | Total number of conversations that can be sampled for value calculations per daily run |
| `sn_na_conv_eval.value_chat_classifier` | **4, 10** | Defines conversation size boundaries based on inbound message count in `sys_cs_message`: ≤4 = Small; 5–10 = Medium; >10 = Large |
| `sn_na_conv_eval.ce_value_calculation_weights` | — | Value calculation weight values for each type of evaluated chat |
| `sn_na_conv_eval.eval_value_rerun_status` | — | Tracks status of the post-install value calculation rerun. When complete, script changes this to false to prevent repeated reruns |

> **Risk Officer Note on `value_chat_classifier` (4, 10):** Small conversations (≤4 inbound messages) represent minimal AI engagement — a one-question, one-answer exchange. Only medium and large conversations represent substantive AI-assisted work that generates meaningful productivity value. If your AI deployments are primarily handling very short interactions, the Value dashboard will report minimal productivity gains — not because the AI is failing, but because the conversations are too brief to generate measurable value. Tune this property to match your deployment context.

> **Risk Officer Note on `maxEvaluateCount` (200):** Only 200 conversations are evaluated per day by the daily batch job. With the 10% sampling rate applied during flow execution, this means approximately 2,000 conversations need to complete per day before the 200 limit is reached. In low-traffic environments, all eligible conversations may be evaluated; in high-traffic environments, a representative sample is evaluated. Quality metrics reflect the sampled population, not all conversations.

---

## Business Rules Installed

| Name | When | Insert | Update | Filter Conditions |
|---|---|---|---|---|
| Add info message for Evaluation set | after | TRUE | TRUE | `stateCHANGESTOInProgress^evaluation_type=conversation^` |
| Scale Up labeling metric | before | TRUE | TRUE | `metric_type=Labeling^metric_nameINhel...` |
| updateLabelingScoresOnEvaluation | after | TRUE | TRUE | `metric_type=Labeling^raw_scoreVALCHANGES` |
| Update deviation scores | before | TRUE | TRUE | `metric_type=LLMGenerated^scoreVALCHANGES^EQ` |
| getAutoEvalCompositeScore | after | FALSE | TRUE | `stateCHANGESTOComplete^total_scoreI...` |

---

## Flows Installed

| Flow | Description | Default State |
|---|---|---|
| **Execute Evaluation** | Performs evaluations when conversations are completed. Trigger: Conversation table (`sys_cs_conversation`) state = Complete, device type = Web Client / Slack / Teams / Bot to Bot / Messenger | **Deactivated by default** |
| **Execute Batch Evaluation** | Performs batch evaluations of up to 100 completed virtual agent conversations at once. Trigger: Evaluation set (`sn_na_conv_eval_evaluation_set`) created or updated with Evaluation Type = Conversation | Available for manual batch runs |

> **Risk Officer Note:** The Execute Evaluation flow is deactivated by default. Real-time evaluation on every conversation completion creates performance load. The recommended approach is the nightly scheduled job. If you need real-time evaluation visibility (e.g., for live monitoring of a high-risk AI deployment), activate the flow but test performance impact in non-production first. The flow enforces a 200/day cap (`maxEvaluateCount`) and 10% sampling regardless of whether it is real-time or batch.

---

## Flow Actions Installed

| Flow Action | Description |
|---|---|
| **Randomize conversations** | Performs randomization of conversations and returns 100 conversations randomly from a given query |
| **invokeApiDefinition** | Invokes OneExtend Capability in the LLM — the core skill invocation action that calls each evaluation skill |
| **Chat Classifier Eval** | Returns title, category (IT/HR), and whether evaluation should be executed for a given conversation |
| **buildTranscript** | Builds the full annotated conversation transcript with `[User]:` and `[Virtual Agent]:` tags, Knowledge article and catalog item handling |
| **evalExecuteCondition** | Checks if the transcript is good enough to be evaluated (validates length, content, channel, scope) |

---

## Script Includes Installed

| Script Include | Description |
|---|---|
| `evalExecuteCondition` | Use this script include to update the evaluation condition |
| `evalUtils` | Primary utility function for the Evaluator — core logic for transcript building and metric invocation |

---

## Evaluation Metrics

All metrics are rated on a scale of 3 or 5, then scaled to 5. The Evaluation dashboard shows each metric for the selected date range. Conversations can be filtered by metric.

| Metric | Description | Risk Governance Relevance |
|---|---|---|
| **Request Completion** | Measures the virtual agent's ability to complete user requests by accurately identifying the user's intent and gathering all required information (slot filling). Score = lowest of Slot Filling and Intent Accuracy | Top-level completion indicator; low score = requests not being fulfilled |
| **Intent Accuracy** | Shows the virtual agent's ability to comprehend user requests, resulting in relevant responses | Critical for healthcare — misunderstanding patient requests can cause harm |
| **Slot Filling** | Shows the virtual agent's capability to interpret user responses and extract structured answers to required questions | Completeness of data collection — unfilled slots = incomplete service |
| **Smooth Flowing Conversation (Deadlock avoidance)** | Checks if the virtual agent responds dynamically, successfully moving the conversation forward without repetition | Identifies loops, dead ends, and conversational failures |
| **Context Retention** | Shows if the virtual agent retains and uses information provided during the conversation, including request interpretation and slot filling | Memory/context window governance — losing context mid-conversation = user frustration and potential errors |
| **Truthfulness (Hallucination Prevention)** | Shows if the virtual agent generated genuine responses grounded in the conversation, excluding fabrication or memory and comprehension failures | **Highest risk metric for healthcare** — fabricated medical information = patient safety risk |
| **Conciseness (Redundancy Avoidance)** | Checks the virtual agent's ability to avoid superfluous or verbose responses that don't contribute to the core intent | Quality metric — verbosity reduces adoption and increases confusion |
| **Coherence** | Checks for clear logical flow, structure, and organization of virtual agent responses | Communication quality — incoherent responses signal model drift or misconfiguration |
| **User Satisfaction** | Weighted average of all other metrics on which the conversation was evaluated | Composite quality score — the single number that summarizes overall performance |

> **Risk Officer Note — Minimum Thresholds for Healthcare AI:** For any patient-facing virtual agent in CareAtlas, establish minimum acceptable thresholds per metric before go-live and enforce them post-deployment. Suggested starting thresholds: Truthfulness ≥ 4.0/5.0 (hallucinations in clinical context are patient safety events); Intent Accuracy ≥ 3.5/5.0 (misunderstanding patient needs leads to wrong service delivery); Request Completion ≥ 3.5/5.0 (incomplete service = unmet patient need). Any metric falling below threshold should trigger an AI case and an immediate investigation.

---

## Score Calculation Methodology

### Metric-Level Deviation and Adjusted Score

To align auto-evaluation scores with human judgment over time, deviations are calculated from a rolling 6-month window of human-labeled scores:

**Upper Deviation**
- Condition: Number of human-labeled scores HIGHER than auto-evaluated scores in the last 6 months > 30
- Calculation: Take the top 90% of these cases → average the delta (human score − auto score) = Upper Deviation
- Effect: Adjusts auto score upward when humans consistently rate higher than the LLM evaluator

**Lower Deviation**
- Condition: Number of human-labeled scores LOWER than auto-evaluated scores in the last 6 months > 30
- Calculation: Take the top 90% of these cases → average the delta = Lower Deviation
- Effect: Adjusts auto score downward when humans consistently rate lower than the LLM evaluator

**Adjusted Score**
- If ≥30 distinct evaluations of BOTH upper and lower deviations exist for a given metric:
  - Error band = SUM(Avg labeling score − LLM score) / Distinct evaluations
  - **Adjusted Score = Auto-Eval Score + Error Band**
- If neither deviation reaches 30 records: **Adjusted Score = Auto-Eval Score** (uncalibrated)

---

### Evaluation-Level User Satisfaction Score Calculations

**Auto eval user satisfaction score:**
`SUM(metric score × metric weight) / SUM(metric weights)` — using all LLM-generated metric scores for the evaluation

**Human user satisfaction score:**
- Only calculated if at least one metric has been human-labeled
- For each metric: use labeled score if labeled; otherwise use LLM score
- `SUM(metric score × metric weight) / SUM(metric weights)`

**Gap:**
`Human user satisfaction score − Auto eval satisfaction score`

**Upper Deviation (evaluation level):**
If Gap is positive and there are >30 records → error band at top 90% = `SUM(Positive Gap) / Distinct evaluations`

**Lower Deviation (evaluation level):**
If Gap is negative and there are >30 records → error band at top 90% = `SUM(Negative Gap) / Distinct evaluations`

**Adjusted user satisfaction score:**
`SUM(Gap) / Distinct evaluations`

---

### Important Calculation Notes

1. **Aggregated score per chat** — even if multiple different requests are made by the user in one conversation, there is one evaluation record with one score per conversation (not per request)

2. **Performance Analytics indicators use evaluation date, not chat date** — if you run batch jobs on historical data, evaluations are counted on the evaluation date in aggregated scores, NOT the actual chat date. Historical batch evaluations do not backfill scores to original chat dates.

---

## Evaluation Flow — Single Conversation Logic

**Flow name:** Execute Evaluation

**Trigger:**
- Table: Conversation table `sys_cs_conversation`
- Condition: State = Complete
- Device type: Web Client, Slack, Teams, Bot to Bot, Messenger

**Sequence of execution:**

**Action 0: Check daily evaluation count**
- Query evaluation table for today's record count
- If count < `maxEvaluateCount` (default 200): continue
- If count ≥ limit: end flow

**Action 1: evalExecuteCondition — 10% Sampling**
- Invokes `evalExecuteCondition.executeEvaluation` script include with conversation reference
- Generates random number (1–100)
- **Proceeds only if ≤10** (10% random sampling)
- Returns true/false

**Action 2: Conditional Branch**
- If true: proceed
- If false: stop

**Action 3: Lookup Interaction Table**
- Matches conversation's channel metadata with interaction table to fetch related records

**Action 4: Application Scope Filter**
- If interaction's application scope contains `hr`: skip (HR conversations excluded)
- Otherwise: continue

**Action 5: buildTranscript**

Constructs the detailed annotated transcript:

- **Message tagging:** `[User]:` for user messages; `[Virtual Agent]:` for VA responses
- **Knowledge articles:** Replace genius results with full article body; annotate with `[Virtual Agent]: Help articles for user query:` wrapped in `Article_Start/Article_End`
  - Skip if KB is HR-scoped or inaccessible
  - Truncate at 10,000 words if over limit
  - If attached file (PDF/Word/Txt): use genius result instead
- **Catalog Items:** Extract name, short description, description; annotate as `[Virtual Agent]: Please choose one of the below options:` with citation number
- **Live agent exclusions:** Skip if first message routes to live agent OR if live agent invoked within first 120 words

**Outputs from buildTranscript:**
- ExecuteEvaluation (true/false)
- Chat Transcript
- Knowledge articles or catalog items referred
- Sys_id of first live agent invocation (if any)
- List of skills to invoke (all evaluation skills)
- Additional evaluation logs

**Action 6: Conditional Branch**
- If ExecuteEvaluation = true: continue

**Action 7: Chat Classifier Eval**
- Builds initial transcript from `sys_cs_message`
- Invokes Chat topic classifier to determine:
  - Should the conversation be evaluated? (true/false)
  - Topic Name
  - Category (IT/HR)
- If ExecuteEvaluation = true: proceed

**Action 8: Create/Update Evaluation Record**
- Creates record in `sn_na_conv_eval_evaluation` with:
  - Document Conversation: conversation reference
  - State: Processing
  - Topic, Category, KB/catalog references, first live agent sys_id, type, initiating user, message log

**Action 9: For each evaluation skill**

Repeats for each skill flagged in Action 6:

**Skills invoked:**
- Coherence Chat Evaluation
- Conciseness Chat Eval
- Context Retention
- Inadequate Slot Filling Chat Eval
- Intent Accuracy Chat Eval
- Smooth Flowing Conversation Chat Eval
- Truthfulness Hallucination Chat Eval

**Action 10: invokeApiDefinition**
- Inputs: Skill name, conversation, transcript, evaluation ID
- Calls Now Assist Skill API **asynchronously**
- Post-processing in `sys_generative_ai_response_validator` parses:
  - Score
  - Reason for Score
  - Examples for the reasoning
- Creates child metric records in `sn_na_conv_eval_evaluation_metrics` linked to parent evaluation

**Action 11: Wait 7 seconds**
- Pause between each skill to manage rate limits / throttling

---

### Request Completion Score Logic

Request Completion is NOT scored by an independent evaluation skill. It is computed by a business rule as:

```
IF (Slot Filling score > Intent Accuracy score):
    Request Completion = Intent Accuracy score
    Reason = Intent Accuracy reason

ELSE IF (Slot Filling score < Intent Accuracy score):
    Request Completion = Slot Filling score
    Reason = Slot Filling reason

ELSE (equal scores):
    Request Completion = both scores
    Reason = both reasons
```

**Rationale:** A request is only complete if both intent was understood (Intent Accuracy) AND all required information was collected (Slot Filling). The weaker of the two determines completeness.

---

### Special Behaviors and Exclusion Rules

| Condition | Behavior |
|---|---|
| Sampling rate | Only 10% of conversations randomly chosen for evaluation |
| Channel filter | Only Web, Slack, Teams, Bot to Bot, Messenger — other channels excluded |
| HR scope filter | Conversations with `_hr_` in application scope excluded |
| HR Knowledge articles | KB articles in HR scope or inaccessible → conversation skipped |
| KB article size limit | Articles >10,000 words truncated at 10,000 |
| Attached KB files (PDF/Word/Txt) | Use genius result instead of file content |
| Live agent at start | If first message routes to live agent → skip |
| Live agent within 120 words | If live agent invoked within first 120 words → skip |
| Already evaluated | Batch flow checks prior evaluations; skips duplicates |

---

## Evaluation Flow for Batch Evaluations

**Flow name:** Execute Batch Evaluation

**Trigger:**
- Table: Evaluation set `sn_na_conv_eval_evaluation_set`
- Condition: State changes to In Progress AND Evaluation type = Conversation

**Inputs:**
- Evaluation Set record with: Query filter (targeting conversations), Evaluation type = Conversation, State = In Progress
- LLM/Skills: Chat Topic Classifier + all evaluation skills

**High-level behavior:**
- Reads the query filter and randomly samples up to 100 conversations
- Skips already-evaluated conversations
- Excludes HR-scoped interactions
- Uses Chat Topic Classifier to validate eligibility; extracts Topic and Category
- Builds transcript with controlled Knowledge article and catalog source inclusion
- Applies live agent exclusions
- Creates Evaluation records; asynchronously invokes all selected evaluation skills
- Writes scores and rationale to metrics table

**Batch execution sequence:**

**Action 1:** Guard clause — if query filter is empty, stop
**Action 2:** Randomize conversations — execute query, randomly select up to 100 (cap at 100 if more)
**Action 3:** Duplicate check — for each conversation sys_id, check `sn_na_conv_eval_evaluation` for existing records; skip if already evaluated or in progress
**Action 4:** Interaction lookup — resolve interaction; if application scope contains `hr`, skip
**Action 5:** buildTranscript — same as single conversation flow (same KB, catalog, live agent rules)
**Action 6:** If Block — branch if ExecuteEvaluation = true
**Action 7:** Chat Classifier Eval — validate eligibility, extract Topic and Category
**Action 8:** Create/Update evaluation record — `sn_na_conv_eval_evaluation` with State = processing
**Action 9:** For loop over skills — for each skill: invokeApiDefinition (asynchronous) + Wait 7 seconds

**Skills invoked in batch (same as single conversation):**
- Coherence Chat Evaluation
- Conciseness Chat Eval
- Context Retention
- Inadequate Slot Filling Chat Eval
- Intent Accuracy Chat Eval
- Smooth Flowing Conversation Chat Eval
- Truthfulness Hallucination Chat Eval

---

## Key Takeaways for AI Risk & Compliance Officers

1. **Execute Evaluation flow is OFF by default** — activate only after testing performance impact; the nightly job is the recommended approach
2. **Only 10% of conversations are evaluated** — metrics are statistically representative, not exhaustive; understand the sampling before drawing conclusions from small datasets
3. **200 evaluations/day cap** — in high-traffic environments, not all eligible conversations will be evaluated; tune `maxEvaluateCount` if you need more coverage
4. **Adjusted scores require 30+ human labels** — before this threshold, raw auto-eval scores are used; invest in human labeling programs to calibrate the evaluation system
5. **HR conversations are always excluded** — if your virtual agent serves HR use cases, evaluation metrics will not cover those interactions; plan alternative quality monitoring
6. **Batch evaluations credit to evaluation date, not chat date** — historical batch runs skew trend charts toward evaluation date; account for this in longitudinal analysis
7. **Truthfulness and Intent Accuracy are your highest-risk metrics for healthcare** — establish minimum thresholds before production deployment and trigger AI cases when thresholds are breached
8. **Request Completion = min(Intent Accuracy, Slot Filling)** — not a separate LLM evaluation; it is a computed business rule output
9. **The 7-second wait between skills** is a rate limiting control — be aware that a single conversation evaluation takes at minimum 49 seconds (7 skills × 7 seconds each) to complete asynchronously

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 872–883*
