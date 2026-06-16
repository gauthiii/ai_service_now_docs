# AI Control Tower Reference
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Role: AI Risk & Compliance Officer Reference

---

## What Is This?

The AI Control Tower Reference section is the technical and operational master reference for the entire AICT platform. It consolidates the canonical definitions, form fields, role specifications, table structures, data model attributes, and evaluation framework details that underpin every governance activity in AICT.

This document serves as the index and overview of the Reference section. The subsequent four topics (27–30) cover each sub-section in depth. This file covers the structure, purpose, and how the reference materials relate to each other and to day-to-day governance operations.

---

## Structure of the Reference Section

The AICT Reference section contains five sub-sections:

| Sub-section | Topic # | What It Covers |
|---|---|---|
| **Add value template form** | 27 | Complete field definitions for the value template creation form — the authoritative field-by-field reference for building value calculations |
| **AI Control Tower roles** | 28 | Every role installed with AICT and AIRC, their responsibilities, and the sub-roles each contains — the access control architecture |
| **Tables installed with AI Control Tower** | 29 | Every database table installed by the AICT core plugin — the technical foundation for integrations, reporting, and custom development |
| **AI asset data model attributes** | 30 | The extended attribute set for each AI asset type in the CMDB and digital asset tables — the data schema for the AI inventory |
| **Evaluation dashboard references** | 30 | Scheduled jobs, tables, system properties, flows, metrics, and calculation logic for the evaluation framework |

---

## How the Reference Fits Into AICT Operations

The reference section is not documentation for initial setup — it is the **operational reference** you return to when:

- **Building value templates:** The Add value template form (Topic 27) tells you exactly what each field means and how it affects calculations
- **Assigning roles:** The Roles section (Topic 28) tells you who can do what, and what sub-roles each role carries — critical for access governance
- **Writing integrations or reports:** The Tables section (Topic 29) gives you the exact table names and field structures needed for API calls, Flow Designer integrations, or custom reports
- **Extending the data model:** The Data model attributes section (Topic 30) tells you what attributes already exist on each AI asset type so you do not create redundant custom fields
- **Troubleshooting evaluations:** The Evaluation references (Topic 30) give you the exact flows, properties, and calculation logic to diagnose why evaluation scores may be unexpected

---

## Key Reference Principle for Risk & Compliance Officers

The reference section is the ground truth when the operational documentation says something is "configured" or "stored" — the reference tells you *where* it is stored and *what structure* it takes.

For example:
- The operational docs say "risk classification is stored on the asset" — the reference tells you the field name is `risk_score` on the `ai_asset` table with data type `choice`
- The operational docs say "the AI steward approves assets" — the reference tells you the exact role name is `sn_ai_governance_ai_steward` and it contains `sn_aia.admin`, `aig_admin`, `sn_mcp_client.admin`, and others

This precision matters for: writing governance policy that references specific system controls, building audit reports that query specific tables and fields, designing integrations that consume AICT data, and verifying that role assignments in your instance match the documented specifications.

---

## Quick Navigation Guide

| If you need to... | Go to |
|---|---|
| Look up what a value template field does | Topic 27: Add value template form |
| Understand what each role can do | Topic 28: AI Control Tower roles |
| Find the database table name for an AICT entity | Topic 29: Tables installed with AI Control Tower |
| Understand what attributes an AI model record carries | Topic 30: AI asset data model attributes |
| Debug why evaluation scores are not calculating | Topic 30: Evaluation dashboard references |
| Verify the exact role name for an API permission check | Topic 28: AI Control Tower roles |
| Write a query against AI case data | Topic 29: Tables installed |

---

## Context: Why Reference Documentation Matters for Governance

In a mature AI governance program, the reference documentation is what enables:

1. **Policy specificity** — governance policies that reference "the `risk_score` field on `ai_asset`" are enforceable and auditable; policies that say "risk is tracked in AICT" are not
2. **Audit evidence** — auditors ask for specific field values from specific tables; knowing the table structure lets you produce precise evidence
3. **Role governance** — access reviews require knowing exactly which permissions each role grants; the Roles reference provides this
4. **Integration reliability** — any system that reads from or writes to AICT tables needs the exact table and field names from the reference
5. **Custom development control** — knowing what fields already exist prevents redundant customization and keeps the data model clean

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, p. 861*
