# AI Control Tower Roles
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Role: AI Risk & Compliance Officer Reference

---

## What Is This?

This is the complete roles reference for AI Control Tower and AI Risk and Compliance. It documents every role installed with AICT and AIRC, the responsibilities each role carries, and the sub-roles each role inherits. This is the authoritative access control specification for the AICT ecosystem.

For a Risk & Compliance Officer, the roles section is essential for: (1) designing your RBAC (Role-Based Access Control) model for AI governance, (2) conducting access reviews, (3) verifying that role assignments in your instance match intended permissions, and (4) ensuring separation of duties between governance functions.

---

## Role Taxonomy Overview

AICT and AIRC together define two sets of roles:

**AI Control Tower roles** — govern the AICT workspace, asset lifecycle, and configuration
**AI Risk and Compliance roles** — govern the GRC module: assessments, risks, controls, and cases

These two sets operate together but are separately defined. A person may hold roles from both sets.

---

## AI Control Tower Roles

### Role 1: AI Steward

**Role name:** `sn_ai_governance_ai_steward`

**Assignment:** The organization decides who receives the AI steward role. Adding users to the **AI Stewards group** grants additional permissions related to playbooks.

**Inherits these sub-roles:**

| Sub-role | Permission Granted |
|---|---|
| `sn_nowassist_admin.user` | Now Assist administration user |
| `sn_ai_governance.workspace_admin` | AICT workspace administration |
| `sn_aia.admin` | AI Agent administration |
| `aig_admin` | AIG (AI Governance) administration |
| `sn_mcp_client.admin` | MCP Client administration |
| `sn_align_core.apw_user` | Can create, update, and delete portfolio plans, free-form road maps, and planning items |
| `it_demand_manager` | Manages the inflow, screening, and facilitates prioritization of IT demands |
| `it_project_manager` | User of the project management application; manager of IT projects |
| `sn_apw_advanced.pf_user` | Can create, view, update, and delete Product Feedback records |

**Core responsibilities:**

| Category | Responsibilities |
|---|---|
| **Platform configuration** | Configuring AI Control Tower |
| **Governance adoption** | Adoption of AI governance practices; adoption of managing AI Control Tower and linking the AI asset inventory |
| **Execution** | Execution of AI Control Tower initiatives |
| **Policy** | Understand the AI assets and AI Control Tower policies |
| **Asset creation** | Creating AI assets |
| **Lifecycle** | Completing the AI asset lifecycle |
| **Cross-functional** | Collaboration of cross-functional teams within the organization to confirm that organization policies are adhered to |
| **Approval workflows** | Creating AI Control Tower Approval Playbook for Now Assist approvals; approving or rejecting approval requests |
| **Configuration** | Configure third-party LLMs and SLMs; configure multi-instance management |
| **Value** | Add and edit a value template |
| **Security** | Learning to use the access map |

**For AI Discovery:**
- Activate or deactivate hyperscaler connections
- Select hyperscaler connections to discover agents and usage on-demand

**For AI Gateway:**
- Add an MCP server via AI Agent Studio
- Set up MCP client connections

> **Risk Officer Note:** The AI Steward is the most powerful governance role in AICT. It inherits admin permissions for AI Agents (`sn_aia.admin`), the full MCP client admin (`sn_mcp_client.admin`), and workspace admin rights. This role should be assigned with the same care as a system administrator — with documented justification, periodic access review, and clear organizational accountability. The number of AI Stewards should be minimized to what is operationally necessary.

---

### Role 2: AI Control Tower Workspace User

**Role name:** `sn_ai_governance_workspace_user`

**Contains roles:** None

**Responsibilities:**
- Own and manage AI assets
- Access the AI Control Tower home page
- Exclusive access to the AI portfolio tab

> **Risk Officer Note:** The Workspace user role is the read/observe role for stakeholders who need visibility into the AI asset portfolio without governance editing rights. Assign to: executives monitoring AI adoption, compliance observers, audit team members, and business stakeholders who need portfolio visibility.

---

### Role 3: AI Asset Owner / Product Owner

**Role name:** `sn_ai_asset_mgmt.ai_asset_owner`

**Contains roles:** None

**Responsibilities:**

| Responsibility | Detail |
|---|---|
| **Data accuracy** | Confirm that AI assets are represented accurately and kept up to date |
| **Lifecycle management** | Manage AI assets (systems, models, datasets, prompts) through their asset lifecycle from intake to retirement |
| **Portal access** | Access My overview, Value, and Adoption tabs |
| **Asset creation** | Creating an AI asset from the AI Control Tower home page using Create AI Asset icon |
| **Deploy phase completion** | Marking the deploy phase of the AI asset lifecycle task complete |

**Important constraint:** If the AI asset gets deployed, the state of the task doesn't change anything automatically in the asset table or the asset governance details record. The asset owner must explicitly mark the deploy phase task complete.

> **Risk Officer Note:** The AI Asset Owner is the accountability role — the person responsible for keeping the asset record accurate and managing it through its lifecycle. Every managed AI asset should have a named Asset Owner. An asset with no Owner is an orphaned asset — a governance risk. Periodically audit for orphaned assets (no `Managed by` value) and assign owners.

---

## AI Risk and Compliance Roles

### Role 4: AI Risk and Compliance Admin

**Role name:** `sn_grc_ai_gov.ai_risk_and_compliance_admin`

**Inherits these sub-roles:**

| Sub-role |
|---|
| `sn_smart_asmt.template_manager` |
| `sn_grc_ai_gov.ai_risk_and_compliance_manager` |
| `sn_smart_asmt.assessment_admin` |
| `sn_grc_workspace.state_model_admin` |
| `sn_smart_asmt.template_contributor` |
| `sn_ai_case_mgmt.ai_case_admin` |
| `sn_reg_body_mgmt.writer` |
| `sn_risk_advanced.ara_admin` |
| `sn_rec_pg_vertical.admin` |
| `sn_grc_ent_access.admin` *(requires GRC: Entity Based Access application)* |

**Responsibilities:**
- Set up risk and impact assessment frameworks
- Configure risk assessment methodologies, risk contribution factors, and impact assessment templates
- Define automation rules for impact assessments to determine applicable risks and controls based on assessment responses
- Set up and profile AI case types
- Delete AI systems
- Enable or disable Entity-Based Access for record types associated with entity properties, and configure Entity-Based Access settings

**Note:** GRC: Entity Based Access application must be installed for `sn_grc_ent_access.admin` to be available.

> **Risk Officer Note:** The AIRC Admin is the configuration owner for the entire AI Risk and Compliance framework. They set up the assessment templates that determine how risk scores are calculated, define which regulations are mapped to which controls, and configure the case type taxonomy. This role should be assigned to your AI Risk & Compliance program lead — the person responsible for the governance framework design, not just its operation.

---

### Role 5: AI Risk and Compliance Manager

**Role name:** `sn_grc_ai_gov.ai_risk_and_compliance_manager`

**Inherits these sub-roles:**

| Sub-role |
|---|
| `sn_grc_ai_gov.ai_risk_and_compliance_analyst` |
| `sn_smart_asmt.template_contributor` |
| `sn_smart_asmt.template_manager` |
| `sn_risk_advanced.risk_asmt_project_manager` |
| `sn_ai_case_mgmt.ai_case_manager` |
| `sn_grc_ent_access.bulk_access_config_admin` *(requires GRC: Entity Based Access application)* |

**Responsibilities:**
- Access all AI systems on the system
- Initiate impact assessments
- Manage the lifecycle of an AI system
- Initiate risk assessments
- Initiate control attestations
- Write and update access to the bulk access update configuration

> **Risk Officer Note:** The AIRC Manager is the operational lead for the AI Risk and Compliance program — they can initiate all assessment types and manage AI system lifecycles. Assign to: AI Risk Managers, Compliance Managers, and senior governance analysts who need full assessment management capability.

---

### Role 6: AI Risk and Compliance Analyst

**Role name:** `sn_grc_ai_gov.ai_risk_and_compliance_analyst`

**Inherits these sub-roles:**

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

**Key constraint:** Analysts can only perform these tasks on **AI systems assigned to them** — not on all systems in the instance.

> **Risk Officer Note:** The scoping of the Analyst role to assigned records only is a governance strength — it enforces least-privilege by ensuring analysts only see and act on their designated assets. This prevents unauthorized access to other teams' AI systems and creates clean accountability. Assign analysts to specific AI systems via the asset assignment process.

---

### Role 7: AI Risk and Compliance Business User

**Role name:** `sn_grc_ai_gov.ai_risk_and_compliance_business_user`

**Inherits these sub-roles:**

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

> **Risk Officer Note:** The Business User role is designed for front-line staff and business stakeholders who participate in governance without being governance professionals. Their primary activities: responding to assigned assessment tasks (e.g., confirming a control is in place) and submitting AI cases through the Employee Center portal. This role enables broad organizational participation in AI governance without exposing sensitive configuration capabilities.

---

### Role 8: AI Risk and Compliance Reader

**Role name:** `sn_grc_ai_gov.ai_risk_and_compliance_reader`

**Inherits these sub-roles:**

| Sub-role |
|---|
| `sn_grc_workspace.user` |
| `sn_grc_workspace.state_model_reader` |

**Scope:** Read access to AI systems and AI impact assessments.

---

### Role 9: AI System Reader

**Role name:** `sn_grc_ai_gov.ai_risk_and_compliance_ai_system_reader`

**Contains roles:** N/A

**Scope:** Read access to AI systems on AI Control Tower workspace AND AI Risk and Compliance workspace.

> **Risk Officer Note:** The distinction between Reader and AI System Reader is subtle but important: the Reader has access to AI systems AND impact assessments; the AI System Reader has read access to AI systems across both workspaces but the assessment access scope may differ. Use AI System Reader for stakeholders who need cross-workspace visibility of assets without assessment data access.

---

## AI Case Management Roles

### Role 10: AI Case Business User

**Role name:** `sn_ai_case_mgmt.ai_case_business_user`

**Contains roles:** `sn_grc_case_mgmt.grc_case_business_user`

**Scope:** Create AI case and AI inquiry on the Employee Center.

---

### Role 11: AI Case Analyst

**Role name:** `sn_ai_case_mgmt.ai_case_analyst`

**Contains roles:**
- `sn_grc_case_mgmt.grc_case_analyst`
- `sn_ai_case_mgmt.ai_case_business_user`

**Responsibilities (on assigned records only):**
- Identify and manage impacted and related areas such as policies, regulations, and enterprise-wide compliance risks
- Identify and manage issues related to impacted areas to eliminate the root causes

---

### Role 12: AI Case Manager

**Role name:** `sn_ai_case_mgmt.ai_case_manager`

**Contains roles:**
- `sn_ai_case_mgmt.ai_case_analyst`
- `sn_grc_case_mgmt.grc_case_manager`

**Scope:** Can review all AI cases, AI inquiries, and their associated information (no scoping to assigned records — full visibility).

---

### Role 13: AI Case Admin

**Role name:** `sn_ai_case_mgmt.ai_case_admin`

**Contains roles:**
- `sn_grc_case_mgmt.grc_case_admin`
- `sn_ai_case_mgmt.ai_case_manager`

**Responsibilities:**
- Manage type profiles to segregate AI cases
- Set up assignment rules
- Delete AI cases

---

## Separation of Duties Matrix

For a mature AI governance program, the following separation of duties should be designed into role assignments:

| Function | Role(s) | Should NOT also have |
|---|---|---|
| AI system creation and submission | AI asset owner | AI steward (avoid self-approval) |
| AI steward approval/rejection | AI steward | AI asset owner of the same asset |
| Risk assessment framework setup | AIRC Admin | AI Case Analyst (avoid self-assessment) |
| Risk assessment execution | AIRC Manager / Analyst | AIRC Admin (avoid self-certification) |
| AI case creation | AI Case Business User / Analyst | AI Case Admin of same case |
| AI case management and oversight | AI Case Manager | The AI system owner being investigated |

> **Risk Officer Note:** The platform does not enforce all of these separations automatically — it requires organizational policy and careful role assignment to maintain. During periodic access reviews, check for users who hold both AI Asset Owner AND AI Steward for the same asset, as this creates a self-approval risk where an asset owner can approve their own asset.

---

## Complete Role Quick Reference

| Role Name | Role ID | Key Capability |
|---|---|---|
| AI Steward | `sn_ai_governance_ai_steward` | Full AICT governance + configuration + approvals |
| AICT Workspace User | `sn_ai_governance_workspace_user` | Portfolio visibility; asset ownership |
| AI Asset Owner | `sn_ai_asset_mgmt.ai_asset_owner` | Asset lifecycle management; submit for review |
| AIRC Admin | `sn_grc_ai_gov.ai_risk_and_compliance_admin` | Framework setup; assessment template design |
| AIRC Manager | `sn_grc_ai_gov.ai_risk_and_compliance_manager` | All assessment initiation; full system lifecycle |
| AIRC Analyst | `sn_grc_ai_gov.ai_risk_and_compliance_analyst` | Assessment execution on assigned systems |
| AIRC Business User | `sn_grc_ai_gov.ai_risk_and_compliance_business_user` | Task completion; control attestation; Employee Center cases |
| AIRC Reader | `sn_grc_ai_gov.ai_risk_and_compliance_reader` | Read-only on systems and assessments |
| AI System Reader | `sn_grc_ai_gov.ai_risk_and_compliance_ai_system_reader` | Read-only on AI systems across both workspaces |
| AI Case Business User | `sn_ai_case_mgmt.ai_case_business_user` | Create cases via Employee Center |
| AI Case Analyst | `sn_ai_case_mgmt.ai_case_analyst` | Work assigned cases; manage impacted areas |
| AI Case Manager | `sn_ai_case_mgmt.ai_case_manager` | Full case visibility and management |
| AI Case Admin | `sn_ai_case_mgmt.ai_case_admin` | Case type admin; assignment rules; delete cases |

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 863–868*
