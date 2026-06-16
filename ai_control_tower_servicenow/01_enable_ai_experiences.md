# Enable AI Experiences
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Role: AI Risk & Compliance Officer Reference

---

## What Is This?

"Enable AI Experiences" is the entry point and foundational section of AI Control Tower. It establishes the platform, its purpose, and the critical legal and compliance disclaimers every AI Risk & Compliance Officer must be aware of before any deployment or governance activity begins.

---

## Platform Purpose

AI Control Tower is a platform that **connects different parts of an organization to accelerate AI adoption**. It is the central governance hub for all AI assets — systems, models, datasets, and prompts — across the enterprise.

The platform organizes its function into four quadrants:

| Quadrant | What It Covers |
|---|---|
| **Explore** | Learn how to manage and track all AI systems and AI assets |
| **Configure** | Configure all AI Control Tower workflows |
| **Use** | Learn how to use AI Control Tower operationally |
| **Reference** | Get details on components such as roles and tables |

Additionally, there is a **Risk and Compliance** entry point which leads to the AI Risk and Compliance application — the module for ethically managing AI capabilities, mitigating AI risks, and ensuring regulatory compliance.

---

## AI Limitations Disclaimer (Critical for Risk Officers)

The documentation includes a formal AI limitations disclosure that governs every use of the platform. As an AI Risk & Compliance Officer, this is binding context:

> *"This application uses artificial intelligence (AI) and machine learning, which are rapidly evolving fields of study that generate predictions based on patterns in data. As a result, this application may not always produce accurate, complete, or appropriate information. Furthermore, there is no guarantee that this application has been fully trained or tested for your use case."*

### Obligations stated in the disclaimer:

1. **Test and evaluate** — It is the customer's responsibility to test and evaluate the application for accuracy, harm, and appropriateness for the specific use case.
2. **Employ human oversight** — AI-generated outputs must not be the sole basis for decision-making. Human oversight of output is required.
3. **Do not rely solely on AI outputs** — Especially critical in consequential domains:
   - Healthcare
   - Finance
   - Legal
   - Employment
   - Security
   - Infrastructure
4. **Abide by AI Acceptable Use Policy** — All users must comply with ServiceNow's AI Acceptable Use Policy (which may be updated by ServiceNow).

> **Risk Officer Note:** These disclaimers are not just legal boilerplate. They define the governance baseline. Any deployment of AICT-governed AI assets in consequential domains must have documented human oversight mechanisms and a tested evaluation process. These obligations should be reflected in your AI governance policies and vendor risk assessments.

---

## Data Processing (Critical for Privacy & Data Governance)

> *"This application requires data to be transferred from ServiceNow customers' individual instances to a centralized ServiceNow environment, which may be located in a different data center region from the one where your instance is, and potentially to a third-party cloud provider, such as Microsoft Azure."*

### Key data governance implications:

- Data may cross **regional boundaries** — relevant for GDPR, DPDP Act, and other jurisdictional data residency requirements.
- Data may be transferred to **Microsoft Azure** (third-party cloud).
- Governed by ServiceNow's internal policies and CORE Compliance Portal.

> **Risk Officer Note:** Before enabling AICT, verify your organization's data residency requirements. If your instance is in a regulated jurisdiction (EU, India, Australia IRAP, FedRAMP), confirm that cross-border data transfers are permissible under applicable law and your DPA with ServiceNow.

---

## Data Collection & Opt-Out

> *"ServiceNow collects and uses the inputs, outputs, and edits to outputs of this application to develop and improve ServiceNow technologies including ServiceNow models and AI products."*

- Customers **can opt out** of future data collection at any time.
- Opt-out is managed through the **Now Assist Opt-Out page**.
- Controls exist to enable/disable both data collection and data processing.

> **Risk Officer Note:** If your organization's data classification policy restricts sharing operational AI inputs/outputs with vendors for model training, the opt-out must be activated before go-live. This should be a standard item in your AI vendor onboarding checklist.

---

## Availability Restrictions (Regional & Regulatory)

The following restrictions apply and are enforced by ServiceNow:

| Restriction Type | Details |
|---|---|
| **In-country SKUs** | Not all model providers available. See KB1584492. |
| **Restricted environments** | FedRAMP, NSC DOD IL5, Australia IRAP-Protected data centers, self-hosted — some features unavailable. See KB0743854. |
| **Regional availability** | Some features available only in certain regions. |
| **Regulated Markets** | Some AI products and skills not available. See KB2593939. |

> **Risk Officer Note:** These restrictions directly affect what AI features can be activated in regulated environments. Audit these restrictions against your deployment geography and regulatory profile before committing to any AICT-based compliance demonstration or production deployment.

---

## Relationship to AI Risk and Compliance

The "Enable AI experiences" section explicitly links to the **AI Risk and Compliance application** as a primary downstream module. The AICT platform is the governance and visibility layer; the AI Risk and Compliance module is the formal GRC layer that runs assessments, tracks risks, and manages regulatory compliance. They share the same AI asset inventory as their common data foundation.

---

## Key Takeaways for AI Risk & Compliance Officers

1. AICT is a **governance platform first** — its value is visibility, lifecycle management, and risk identification at scale.
2. The platform's own AI limitations disclaimer **creates obligations** — human oversight, testing, and policy compliance are required, not optional.
3. Data flows across regions and to third-party cloud — **data residency and DPA review** is a prerequisite.
4. Data collection opt-out must be **consciously decided** before go-live.
5. Regulated environments have feature restrictions — **check KB articles** before planning governance demonstrations.
6. The Risk and Compliance application is a **separate but integrated module** — AICT provides the asset inventory; AIRC runs the governance workflows on top of it.

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 692–695*
