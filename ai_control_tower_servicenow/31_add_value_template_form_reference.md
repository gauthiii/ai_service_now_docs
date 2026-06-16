# Add Value Template Form — Field Reference
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Topic 31 of 35 | Role: AI Risk & Compliance Officer Reference

---

## What Is This?

The Add value template form is the interface through which AI stewards and asset owners define the formula for calculating productivity value from an AI asset. This document is the authoritative, standalone field-by-field reference for that form — every field, every option, every constraint, and every governance implication.

This is a reference document. For the procedural workflow (how to create, edit, map, and publish templates), see Topic 21: Using Value Templates.

---

## Form Structure

The form has three sections:

| Section | Purpose |
|---|---|
| **Calculation builder** | Defines the formula — Usage × Time × Acceptance Rate |
| **Attributes** | Names and categorizes the template |
| **Calculation output** | Scopes the template to an instance |

The formula output is always in **minutes per day**.

---

## Section 1: Calculation Builder

### Persona

| Property | Detail |
|---|---|
| **Purpose** | The user role for whom value is being calculated |
| **Options** | Agent, Developer, Other, Requestor |
| **Default** | Other |
| **Behavior** | Value calculations per this template apply only to the selected persona |

**Example:** If the AI asset is Incident Summarization and persona = Agent, value calculations reflect Agent-role usage only.

**Governance note:** Different user populations derive different productivity gains from the same AI asset. An agent summarizing 50 incidents per day saves more time than a developer who uses the same skill occasionally. Create persona-specific templates when evidence supports differentiated value measurement.

---

### Usage

| Property | Detail |
|---|---|
| **Purpose** | The usage metric — the daily count of AI asset invocations |
| **Type** | Performance Analytics indicator |
| **Critical constraint** | Must be a **daily** usage indicator |
| **Custom metric** | If a custom indicator is added, usage value is derived from the indicator |

**Example:** For Incident Summarization, usage = daily executions of the Incident Summarization skill.

**Governance note:** The daily constraint is non-negotiable. A weekly or monthly indicator produces incorrect daily calculations. Always verify the aggregation period of the indicator before mapping it to the Usage field.

---

### Time Value Type

| Property | Detail |
|---|---|
| **Purpose** | Determines how the time component is sourced |
| **Options** | Constant, Indicator |
| **Constant** | Use when you have a fixed, known average time saved per execution |
| **Indicator** | Use when you have a measured metric for actual time saved |

---

### Time Constant

| Property | Detail |
|---|---|
| **Purpose** | A fixed time value (in minutes) used as the time component |
| **Unit** | Minutes |
| **Active when** | Time value type = Constant |

**Example:** For Incident Summarization, the time constant = average time saved per invocation, e.g., 0.2 minutes.

**Governance note — most common error:** Time constant = **time saved** (the human time delta attributable to the AI), NOT the time the AI takes to run. "AI ran in 2 seconds" is not a time constant. "Without AI this task took 5 minutes; with AI it takes 3 minutes, so time saved = 2 minutes" — 2 minutes is the time constant.

---

### Time Indicator

| Property | Detail |
|---|---|
| **Purpose** | Average time saved per invocation, derived from a custom Performance Analytics indicator |
| **Unit** | Minutes |
| **Active when** | Time value type = Indicator |

**Example:** For Incident Summarization, the time indicator derives from a custom indicator that measures agent time-on-task before and after AI assistance.

**Governance note:** Using an indicator produces evidence-based time savings data rather than assumptions. For high-value AI systems justifying significant investment, time indicators are the governance standard. A constant is an assumed value; an indicator is a measured value.

---

### Acceptance Rate Type

| Property | Detail |
|---|---|
| **Purpose** | Determines how the acceptance rate component is sourced |
| **Options** | Constant, Indicator |
| **Constant** | Use when using a target or estimated acceptance rate |
| **Indicator** | Use when you have measured actual acceptance |

---

### Acceptance Rate Constant

| Property | Detail |
|---|---|
| **Purpose** | Fixed percentage representing the portion of AI outputs accepted by users |
| **Unit** | Percentage |
| **Constraint** | Value must be between 1 and 100 |
| **Default across AICT** | 50% (conservative default) |
| **Active when** | Acceptance rate type = Constant |

**Example:** For Incident Summarization at 90% acceptance rate constant — 90% of AI-generated summaries are used without significant modification.

**Governance note:** The 50% default is an assumption, not a measurement. The Value Template review task in the Assess lifecycle stage exists specifically to validate that this assumption is realistic. "Acceptance rate 50% assumed — no measurement data" is a valid finding in close notes; "looks reasonable" is not. For regulated AI programs, acceptance rate should be measured and documented.

---

### Acceptance Rate Indicator

| Property | Detail |
|---|---|
| **Purpose** | Dynamic acceptance rate derived from a custom Performance Analytics indicator |
| **Constraint** | Must be a **daily** indicator with value between 1 and 100 |
| **Active when** | Acceptance rate type = Indicator |

**Example:** For Incident Summarization, the acceptance rate indicator tracks the ratio of AI summaries applied to tickets (acceptance actions / total executions).

**Governance note:** An acceptance rate indicator is the evidence-based alternative to an assumed constant. It should track observable user behavior — copy to clipboard, "apply to record," "accept suggestion" button clicks — as a proxy for genuine acceptance.

---

## Section 2: Attributes

### Template Name

| Property | Detail |
|---|---|
| **Constraint** | Must be unique across all templates |
| **Best practice** | Name format: `[Asset Name] — [Persona] — [Metric Type]` |
| **Example** | "Incident Summarization — Agent — Custom Indicators" |

---

### Value Template Category

| Property | Detail |
|---|---|
| **Examples** | Productivity, Efficiency, Accuracy |
| **Purpose** | Organizes and filters templates in the templates list |
| **Governance note** | Use consistent category names aligned to your AI governance reporting taxonomy |

---

### Department

| Property | Detail |
|---|---|
| **Purpose** | Business unit or department associated with the template |
| **Effect** | Enables department-level value reporting on the Value dashboard |

---

### Description

| Property | Detail |
|---|---|
| **Purpose** | What the template does and how it contributes to measuring value |
| **Governance standard** | Should document: formula logic, data sources for each component, assumptions made, who validated the assumptions, date of last validation |

---

## Section 3: Calculation Output

### Instance

| Property | Detail |
|---|---|
| **Purpose** | Specifies which instance the template applies to |
| **Multi-instance use** | Validate formula in non-production before publishing to production |
| **Testing delay** | Same-instance: up to 10 minutes; cross-instance: up to 30 minutes |
| **During testing** | Cannot edit or resend; can work on other templates |

---

## The Formula

```
Daily Value (minutes) = Usage × Time × (Acceptance Rate / 100)
```

**Default template examples from the docs:**

| Asset Type | Formula Components | Example Calculation |
|---|---|---|
| ServiceNow skill | Daily executions × avg time/execution × 50% | 1,500 × 0.2 × 0.90 = 270 min/day |
| ServiceNow AI agent | Daily executions × avg time/execution × 50% | 1,000 × 1.5 × 0.50 = 750 min/day |
| AWS / Microsoft AI agent | Daily invocations × 15 min (fixed) × 50% | — |
| ServiceNow AI use case | Daily invocations × avg time/invocation × 50% | — |

**Note on AWS/Microsoft agents:** The 15-minute fixed time constant is a platform default, not a measured value. Replace with a custom indicator based on actual data for credible ROI reporting.

---

## Complete Field Summary

| Field | Section | Type | Default | Constraint |
|---|---|---|---|---|
| Persona | Calculation builder | Choice | Other | Agent / Developer / Other / Requestor |
| Usage | Calculation builder | PA Indicator | — | Daily indicator only |
| Time value type | Calculation builder | Choice | — | Constant or Indicator |
| Time constant | Calculation builder | Number (min) | — | Active when type = Constant |
| Time indicator | Calculation builder | PA Indicator | — | Active when type = Indicator |
| Acceptance rate type | Calculation builder | Choice | — | Constant or Indicator |
| Acceptance rate constant | Calculation builder | Number (%) | — | 1–100; active when type = Constant |
| Acceptance rate indicator | Calculation builder | PA Indicator | — | Daily; 1–100; active when type = Indicator |
| Template name | Attributes | String | — | Unique |
| Value template category | Attributes | Choice | — | Productivity / Efficiency / Accuracy |
| Department | Attributes | Reference | — | — |
| Description | Attributes | Long text | — | — |
| Instance | Calculation output | Reference | — | For multi-instance scoping |

---

## Key Takeaways for AI Risk & Compliance Officers

1. **Time constant = time saved, not AI runtime** — most common error; it must represent human productivity delta
2. **50% acceptance rate is an assumption** — the Value Template review task must validate it with evidence
3. **Usage and acceptance rate indicators must be daily** — non-daily aggregation breaks the formula
4. **Publishing updates ALL instances** — test cross-instance first (30-min window); cannot edit during testing
5. **One template per asset** — no AI system can have two templates; publishing a new one replaces the existing one
6. **Description field is governance documentation** — it should record data sources, assumptions, and validation history

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 861–863*
