# Configure Third-Party LLMs Using AI Control Tower
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Role: AI Risk & Compliance Officer Reference

---

## What Is This?

This section provides the step-by-step procedure for configuring third-party Large Language Models (LLMs) and Small Language Models (SLMs) in AI Control Tower. While Topic 7 explained the concepts (regional vs. global routing, fallback, spillover, impact summary), this topic documents the actual configuration procedure — what you click, what you select, and what consents are required.

The documented procedure focuses on **APJC region** configuration as the primary example, covering both Regional and Global data routing paths.

---

## Before You Begin

**Role required:** AI steward (`sn_ai_governance_ai_steward`)

**Navigation:** `All > AI Control Tower > Configurations > Controls > AI model providers`

---

## Configuration Procedure

### Step 1: Open the AI Model Providers Edit View

1. Navigate to `All > AI Control Tower > Configurations > Controls > AI model providers`
2. Select **Edit**

You will configure LLMs through one of two data routing types:
- **Regional** — routes requests to datacenters within your region
- **Global** — routes requests to the globally best datacenter

---

### Path A: Configure LLMs via Regional Data Routing

**Step 3a.** Select **Regional**

All allowed model providers are displayed:
- Now LLM Service
- AWS Claude
- Azure OpenAI
- Google Gemini

**Step 3b.** Select the model providers according to your organizational policies

> **Risk Officer Note:** "According to your organizational policies" is the key phrase. Provider selection is a governance decision, not just a technical one. Each provider you enable must have been through your vendor risk assessment process. For healthcare (CareAtlas), consider: Does each provider have a BAA (Business Associate Agreement) in place? What data does each provider receive? What are the data retention and processing terms? Only enable providers that have passed your vendor governance process.

**Step 3c.** Azure OpenAI spillover prompt

When Azure OpenAI is selected, you are asked: **"Allow Spillover?"** which would redirect traffic to Global data routing when regional capacity is exceeded.

- Select **Yes** to enable spillover (accepts potential global routing when Azure regional capacity is full)
- Select **No** to keep traffic strictly regional

**Step 3d.** Select **Save**

A **Data routing confirmation consent request** appears, informing you to provide consent.

> **Risk Officer Note:** The consent request is a legally meaningful step. By clicking "Agree and proceed," you are confirming organizational agreement to the data routing configuration and its data processing implications. This consent should be documented as part of your data governance record. Before agreeing, verify that your organization's Data Protection Officer or legal team has reviewed the implications of the selected routing configuration.

**Step 3e.** Select **Agree and proceed**

**Step 3f.** Select **Save**

**Result:** Third-party LLMs configured with Regional data routing for APJC region.

---

### Path B: Configure LLMs via Global Data Routing

**Step 4a.** Select **Global**

All allowed model providers are displayed (same list, different routing):
- AWS Claude
- Azure OpenAI
- Google Gemini
- Now LLM Service

**Important note from the documentation:**
> "Selecting global data routing redirects your data processing location to a global datacenter."

This is a data residency warning. Global data routing means your LLM requests — and any data contained in them — may be processed in any geographic region, not just your home region.

**Step 4b.** Select all the model providers (or a subset per policy)

**Step 4c.** Select **Save**

**Result:** Third-party LLMs configured with Global data routing.

---

## Available Model Providers by Routing Type

| Provider | Regional Routing | Global Routing |
|---|---|---|
| Now LLM Service | Available | Available |
| AWS Claude | Available | Available |
| Azure OpenAI | Available (with optional spillover to global) | Available |
| Google Gemini | Available | Available |

---

## The Consent Request — What It Means

The **"Data routing confirmation consent request"** that appears before saving is not just a UI confirmation dialog. It is:

1. **An informed consent mechanism** — the platform forces you to explicitly acknowledge the data routing implications before they take effect
2. **A governance record trigger** — once you click "Agree and proceed," the configuration change is logged in the Audit logs with your user identity and timestamp
3. **An organizational accountability step** — the AI steward accepting this consent is taking responsibility for the routing configuration on behalf of the organization

**What the consent covers:**
- Acknowledgment that data will be routed per the selected configuration
- Understanding that regional routing constrains data to regional datacenters
- Understanding that global routing removes geographic constraints on data processing

> **Risk Officer Note:** The AI steward clicking "Agree and proceed" should not be making this decision unilaterally. The consent represents an organizational commitment regarding data processing location. It should follow a documented approval process involving: (1) Legal/DPO review of routing implications, (2) Business approval from the appropriate data owner, (3) AI steward execution of the agreed configuration. Document this chain of approval in your change management record.

---

## Audit Log Entry for Provider Configuration

After completing either path, the configuration change appears in the Audit logs:

| Field | Content |
|---|---|
| Timestamp | Date and time of the change |
| User | The AI steward who made the change |
| Changed category | "AI model providers" |
| Changed setting | Data routing type, selected providers, fallback status |
| After change | New configuration state |
| Before change | Previous configuration state |

---

## Scenarios Not Covered by This Procedure

This documented procedure covers the APJC region example. The documentation references two other scenarios:

**Regulated markets:**
- Data routing configuration is NOT available (locked)
- Provider list is limited and read-only
- No configuration steps required or possible by the AI steward
- Reference: Explore the third-party LLMs and regions (Topic 7)

**AMS & EMEA regions:**
- LLMs follow regional data routing configurations
- No global routing option
- All allowed providers are visible
- Reference: Explore the third-party LLMs and regions (Topic 7)

---

## Integration with Fallback and Impact Summary

After configuring providers, use the Impact Summary to understand the effect of your choices before committing:

1. In the AI model providers edit view, select **Preview impact** before saving
2. Review the Impact Summary table:
   - With Fallback OFF: "AI systems require deactivation" column shows which systems will go offline
   - With Fallback ON: "AI systems supported by fallback providers" shows non-compliant systems running on fallback
3. Select an entry to open the **Support Matrix** — all AI systems with their provider assignments
4. Adjust your provider selection if needed, then proceed with the consent and save steps above

---

## Post-Configuration Verification

After configuring third-party LLMs, verify:

- [ ] Selected providers appear as active in the AI model providers list
- [ ] Data routing type matches your organizational policy (Regional or Global)
- [ ] No AI systems are unexpectedly deactivated (check the Impact Summary's deactivation column)
- [ ] Fallback status is documented and intentional
- [ ] Azure OpenAI spillover setting matches your data residency requirements
- [ ] Configuration change appears in Audit logs with correct user, timestamp, and before/after values
- [ ] Consent was provided by an authorized individual following organizational approval process

---

## Key Takeaways for AI Risk & Compliance Officers

1. **Provider selection is a governance decision, not just a technical one** — each enabled provider must have cleared vendor risk assessment and, in healthcare, have a BAA in place.
2. **The consent request has legal significance** — "Agree and proceed" is an organizational commitment about data processing location; it should not be clicked without documented prior approval.
3. **Azure OpenAI spillover means potential global routing** — selecting Yes to spillover accepts that Azure regional capacity exhaustion will route data globally; this is a data residency risk.
4. **Global data routing removes geographic data processing constraints** — explicitly prohibited in some regulatory frameworks; verify before selecting.
5. **The procedure covers APJC only** — regulated market and AMS/EMEA scenarios have different procedures and constraints (see Topic 7).
6. **Always use Preview impact before saving** — the AI systems require deactivation column prevents operational surprises.
7. **Audit logs capture the consent** — every provider configuration change is logged with the approving user; this is your evidence trail.
8. **Routing changes should follow change management** — AI steward executing provider configuration is implementing an approved organizational decision, not making one unilaterally.

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 820–821*
