# AI Control Tower Roles — Reference
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Topic 32 of 35 | Role: AI Risk & Compliance Officer Reference

---

## What Is This?

This is the complete, standalone roles reference for AI Control Tower and AI Risk and Compliance — the definitive access control specification for the entire AICT ecosystem. It documents every role installed with AICT and AIRC, their system role names, responsibilities, sub-roles inherited, and governance implications.

For procedural role assignment guidance, see Topic 13 (Configure AI Control Tower) and Topic 28 (Roles, in the reference section). This document is the canonical reference you return to for access reviews, separation of duties analysis, and policy documentation.

---

## Role Sets Overview

Two distinct application sets install roles:

| Application | Role Set Prefix | Governs |
|---|---|---|
| AI Control Tower (`sn_ai_governance`, `sn_ai_asset_mgmt`) | `sn_ai_governance_*`, `sn_ai_asset_mgmt.*` | AICT workspace, asset lifecycle, configuration |
| AI Risk and Compliance (`sn_grc_ai_gov`, `sn_ai_case_mgmt`) | `sn_grc_ai_gov.*`, `sn_ai_case_mgmt.*` | GRC assessments, risks, controls, cases |

---

## AICT Roles

### AI Steward — `sn_ai_governance_ai_steward`

The primary governance role. The organization decides who receives this role. Adding users to the **AI Stewards group** grants additional playbook-related permissions.

**Inherited sub-roles:**

| Sub-role | Capability |
|---|---|
| `sn_nowassist_admin.user` | Now Assist administration |
| `sn_ai_governance.workspace_admin` | AICT workspace administration |
| `sn_aia.admin` | AI Agent administration |
| `aig_admin` | AI Governance administration |
| `sn_mcp_client.admin` | MCP Client administration |
| `sn_align_core.apw_user` | Create/update/delete portfolio plans, road maps, planning items |
| `it_demand_manager` | Manage inflow, screening, and prioritization of IT demands |
| `it_project_manager` | IT project management application user |
| `sn_apw_advanced.pf_user` | Create/view/update/delete Product Feedback records |

**Full responsibilities:**

*Platform configuration and governance:*
- Configuring AI Control Tower
- Adoption of AI governance practices
- Adoption of managing AI Control Tower and linking the AI asset inventory
- Execution of AI Control Tower initiatives
- Understanding AI assets and AI Control Tower policies

*Asset management:*
- Creating AI assets
- Completing the AI asset lifecycle
- Collaboration of cross-functional teams to confirm organization policies are adhered to

*Approval workflows:*
- Creating AI Control Tower Approval Playbook for Now Assist approvals
- Approving or rejecting approval requests

*Configuration:*
- Configure third-party LLMs and SLMs
- Configure Multi-instance management
- Add and edit a value template
- Using the access map

*AI Discovery:*
- Activate or deactivate hyperscaler connections
- Select hyperscaler connections to discover agents and usage on-demand

*AI Gateway:*
- Add an MCP server via AI Agent Studio
- Set up MCP client connections

> **Risk Officer Note:** The AI Steward is the most privileged governance role in the ecosystem — it inherits AI Agent admin (`sn_aia.admin`), full MCP client admin, and workspace admin. Assign with minimum necessary access principle. The number of active AI Stewards should reflect operational need, not convenience. All AI Steward assignments must be documented, approved, and reviewed quarterly.

---

### AI Control Tower Workspace User — `sn_ai_governance_workspace_user`

**Inherited sub-roles:** None

**Responsibilities:**
- Own and manage AI assets
- Access the AI Control Tower home page
- Exclusive access to the AI portfolio tab

> **Risk Officer Note:** This is the read/observe role. Assign to executives, compliance observers, audit team members, and business stakeholders who need AI portfolio visibility without governance editing rights.

---

### AI Asset Owner / Product Owner — `sn_ai_asset_mgmt.ai_asset_owner`

**Inherited sub-roles:** None

**Responsibilities:**
- Confirm AI assets are represented accurately and kept up to date
- Manage AI assets (systems, models, datasets, prompts) through lifecycle from intake to retirement
- Access My overview, Value, and Adoption tabs
- Create AI assets from the AI Control Tower home page
- Mark the deploy phase of the AI asset lifecycle task complete

**Important constraint:** If an AI asset gets deployed, the state of the task does not change anything automatically in the asset table or asset governance details record — the asset owner must explicitly mark the deploy phase task complete.

> **Risk Officer Note:** Every managed AI asset must have a named Asset Owner. Orphaned assets (no owner) are a governance risk — they have no accountability and may not be maintained or updated. Audit for orphaned assets monthly.

---

## AIRC Roles

### AI Risk and Compliance Admin — `sn_grc_ai_gov.ai_risk_and_compliance_admin`

**Inherited sub-roles:**

| Sub-role | Note |
|---|---|
| `sn_smart_asmt.template_manager` | — |
| `sn_grc_ai_gov.ai_risk_and_compliance_manager` | Inherits Manager role |
| `sn_smart_asmt.assessment_admin` | — |
| `sn_grc_workspace.state_model_admin` | — |
| `sn_smart_asmt.template_contributor` | — |
| `sn_ai_case_mgmt.ai_case_admin` | — |
| `sn_reg_body_mgmt.writer` | — |
| `sn_risk_advanced.ara_admin` | — |
| `sn_rec_pg_vertical.admin` | — |
| `sn_grc_ent_access.admin` | Requires GRC: Entity Based Access application |

**Responsibilities:**
- Set up risk and impact assessment frameworks
- Configure risk assessment methodologies, risk contribution factors, and impact assessment templates
- Define automation rules for impact assessments to determine applicable risks and controls based on assessment responses
- Set up and profile AI case types
- Delete AI systems
- Enable/disable Entity-Based Access for record types; configure Entity-Based Access settings

> **Risk Officer Note:** This is the framework design role. Assign to the AI Risk & Compliance program lead responsible for the governance architecture — not to operational analysts. The AIRC Admin defines how risk is measured; the Manager and Analyst apply those measurements.

---

### AI Risk and Compliance Manager — `sn_grc_ai_gov.ai_risk_and_compliance_manager`

**Inherited sub-roles:**

| Sub-role | Note |
|---|---|
| `sn_grc_ai_gov.ai_risk_and_compliance_analyst` | Inherits Analyst role |
| `sn_smart_asmt.template_contributor` | — |
| `sn_smart_asmt.template_manager` | — |
| `sn_risk_advanced.risk_asmt_project_manager` | — |
| `sn_ai_case_mgmt.ai_case_manager` | — |
| `sn_grc_ent_access.bulk_access_config_admin` | Requires GRC: Entity Based Access application |

**Responsibilities:**
- Access all AI systems on the system (no scoping to assigned records)
- Initiate impact assessments
- Manage the lifecycle of an AI system
- Initiate risk assessments
- Initiate control attestations
- Write and update access to the bulk access update configuration

---

### AI Risk and Compliance Analyst — `sn_grc_ai_gov.ai_risk_and_compliance_analyst`

**Inherited sub-roles:**

| Sub-role |
|---|
| `sn_ai_case_mgmt.ai_case_analyst` |
| `sn_smart_asmt.assessment_reader` |
| `sn_smart_asmt.template_reader` |
| `sn_grc_ai_gov.ai_risk_and_compliance_business_user` |
| `sn_grc_ai_gov.ai_risk_and_compliance_reader` |
| `sn_grc_workspace.user` |
| `sn_grc_workspace.state_model_reader` |
| `sn_risk_advanced.ara_creator` |
| `sn_risk_advanced.ara_assessor` |
| `sn_risk_advanced.ara_approver` |
| `sn_risk_advanced.risk_asmt_project_user` |

**Responsibilities (on assigned records only):**
- Initiate impact assessments
- Manage the lifecycle of an AI system
- Initiate risk assessments
- Initiate control attestations

**Key constraint:** Only on AI systems **assigned to them** — not all systems.

---

### AI Risk and Compliance Business User — `sn_grc_ai_gov.ai_risk_and_compliance_business_user`

**Inherited sub-roles:**

| Sub-role |
|---|
| `sn_grc_workspace.assessment_template_contributor` |
| `sn_smart_asmt.actor` |
| `sn_grc_workspace.user` |
| `sn_smart_asmt.assessment_reader` |
| `sn_risk_advanced.risk_asmt_project_reader` |

**Responsibilities:**
- Create AI case on the Employee Center
- Work on assigned tasks
- Perform control attestations

---

### AI Risk and Compliance Reader — `sn_grc_ai_gov.ai_risk_and_compliance_reader`

**Inherited sub-roles:** `sn_grc_workspace.user`, `sn_grc_workspace.state_model_reader`

**Scope:** Read access to AI systems and AI impact assessments.

---

### AI System Reader — `sn_grc_ai_gov.ai_risk_and_compliance_ai_system_reader`

**Inherited sub-roles:** N/A

**Scope:** Read access to AI systems on AI Control Tower workspace AND AI Risk and Compliance workspace.

---

## AI Case Management Roles

### AI Case Business User — `sn_ai_case_mgmt.ai_case_business_user`

**Contains:** `sn_grc_case_mgmt.grc_case_business_user`

**Scope:** Create AI case and AI inquiry on the Employee Center.

---

### AI Case Analyst — `sn_ai_case_mgmt.ai_case_analyst`

**Contains:** `sn_grc_case_mgmt.grc_case_analyst`, `sn_ai_case_mgmt.ai_case_business_user`

**Responsibilities (on assigned records only):**
- Identify and manage impacted and related areas such as policies, regulations, and enterprise-wide compliance risks
- Identify and manage issues related to impacted areas to eliminate the root causes

---

### AI Case Manager — `sn_ai_case_mgmt.ai_case_manager`

**Contains:** `sn_ai_case_mgmt.ai_case_analyst`, `sn_grc_case_mgmt.grc_case_manager`

**Scope:** Review all AI cases, AI inquiries, and associated information (full visibility, no record scoping).

---

### AI Case Admin — `sn_ai_case_mgmt.ai_case_admin`

**Contains:** `sn_grc_case_mgmt.grc_case_admin`, `sn_ai_case_mgmt.ai_case_manager`

**Responsibilities:**
- Manage type profiles to segregate AI cases
- Set up assignment rules
- Delete AI cases

---

## Separation of Duties Matrix

| Function | Assigned Role | Must NOT Also Hold |
|---|---|---|
| Submit AI asset for review | AI Asset Owner | AI Steward for the same asset (self-approval risk) |
| Approve/reject AI assets | AI Steward | AI Asset Owner of the same asset |
| Design assessment framework | AIRC Admin | AIRC Analyst (self-certification risk) |
| Execute risk assessments | AIRC Manager / Analyst | AIRC Admin for same scope |
| Create AI cases | AI Case Business User / Analyst | AI Case Admin of same case |
| Investigate and manage cases | AI Case Manager | Owner of the AI system being investigated |

---

## Quick Reference Table

| Role | System Name | Scope | Key Capability |
|---|---|---|---|
| AI Steward | `sn_ai_governance_ai_steward` | All assets | Full AICT governance + configuration + approvals |
| AICT Workspace User | `sn_ai_governance_workspace_user` | All assets (read) | Portfolio visibility; asset ownership |
| AI Asset Owner | `sn_ai_asset_mgmt.ai_asset_owner` | Own assets | Asset lifecycle; submit for review |
| AIRC Admin | `sn_grc_ai_gov.ai_risk_and_compliance_admin` | All | Framework setup; assessment template design |
| AIRC Manager | `sn_grc_ai_gov.ai_risk_and_compliance_manager` | All | All assessments; full system lifecycle |
| AIRC Analyst | `sn_grc_ai_gov.ai_risk_and_compliance_analyst` | Assigned only | Assessment execution |
| AIRC Business User | `sn_grc_ai_gov.ai_risk_and_compliance_business_user` | Assigned tasks | Task completion; attestation; Employee Center |
| AIRC Reader | `sn_grc_ai_gov.ai_risk_and_compliance_reader` | All (read) | Read systems and assessments |
| AI System Reader | `sn_grc_ai_gov.ai_risk_and_compliance_ai_system_reader` | All (read) | Read AI systems across both workspaces |
| AI Case Business User | `sn_ai_case_mgmt.ai_case_business_user` | — | Create cases via Employee Center |
| AI Case Analyst | `sn_ai_case_mgmt.ai_case_analyst` | Assigned | Work cases; manage impacted areas |
| AI Case Manager | `sn_ai_case_mgmt.ai_case_manager` | All | Full case visibility and management |
| AI Case Admin | `sn_ai_case_mgmt.ai_case_admin` | All | Case type admin; assignment rules; delete |

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 863–868*
