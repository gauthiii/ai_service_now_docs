# Explore Now Assist AI Asset Discovery
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Role: AI Risk & Compliance Officer Reference

---

## What Is This?

Now Assist AI Asset Discovery is the automated synchronization process that pulls ServiceNow-native AI assets — models, datasets, prompts, skills, and agentic AI components — directly into the AI Control Tower's AI Asset Inventory. Unlike Enterprise AI Discovery (which finds third-party cloud assets), Now Assist discovery operates entirely within the ServiceNow platform, syncing assets that already exist in the Now Platform's own configuration tables.

This is the mechanism by which your instance's built-in AI capabilities (Now Assist skills, AI agents, prompts, and models) automatically appear in the governance inventory without manual entry.

---

## Why This Matters for Governance

Every Now Assist skill, AI agent, and model deployed on your ServiceNow instance is a governed AI asset — or should be. Without the sync, you would have to manually enter every skill into AICT. With the sync, the inventory self-populates from authoritative source tables.

However, auto-sync introduces its own governance risk: **what syncs automatically may not be what governance has approved**. The sync reflects the operational state of the platform, not the governance-approved state. This gap — between what exists technically and what has been reviewed — is the primary compliance concern with auto-discovery.

---

## Source and Target Tables

All Now Assist AI asset discovery syncs from specific Now Platform source tables to AICT target tables:

| Asset Type | Source Table | Target Tables |
|---|---|---|
| **Models** | `sys_generative_ai_model_config` | `alm_ai_model_digital_asset`, `cmdb_ai_model_product_model` |
| **Datasets** | `sys_one_extend_test_dataset` | `alm_ai_dataset_digital_asset`, `cmdb_ai_dataset_product_model` |
| **Skills (AI Systems)** | `sn_nowassist_skill_config` | `alm_ai_system_digital_asset`, `cmdb_ai_system_product_model` |
| **Prompts** | `sys_generative_ai_config` | `alm_ai_prompt_digital_asset`, `cmdb_ai_prompt_product_model` |
| **Tools** | `sn_aia_tool` | `sn_ent_ai_tool` |
| **AI Agents** | `sn_aia_agent` | `alm_ai_system_digital_asset`, `cmdb_ai_system_product_model` |
| **Agent-Tool Mapping** | `sn_aia_agent_tool_m2m` | `sn_ent_ai_system_subcomponent_m2m` |
| **Agent Use Cases** | `sn_aia_usecase` | `alm_ai_system_digital_asset`, `cmdb_ai_system_product_model` |
| **Usecase-Agent Mapping** | `sn_aia_team_member` | `sn_ent_ai_system_subcomponent_m2m` |

> **Risk Officer Note:** The digital asset tables (`alm_ai_*_digital_asset`) are the governance layer records — these are the records you see in AICT and attach lifecycle, assessments, and risk classifications to. The CMDB tables (`cmdb_ai_*_product_model`) are the configuration management records that link to the broader CMDB for impact analysis and relationship tracking. Both must be populated for full governance coverage.

---

## Inclusion Rules: What Gets Synced and What Doesn't

Not everything in the source tables syncs to AICT. Each asset type has explicit inclusion criteria:

### Skills (AI Systems from `sn_nowassist_skill_config`)

The sync logic is:

**Step 1 — For default skills (platform-provided):**
- If the skill is **Active** → Insert into AICT
- If the skill is **NOT Active** → Insert ONLY if it belongs to the **custom skill category AND is published**
- Platform skills and their children are excluded from sync (non-platform skills only)

**Step 2 — If the skill already exists in AICT and the source record is updated:**
Changes are applied, with this state mapping:

| Source State (Now Assist) | Target State in AICT |
|---|---|
| Active | Deployed |
| Published or Draft | In Development |
| Retired | Retired |
| **Deleted** | **No update made** |

> **Risk Officer Note:** The "Deleted" mapping is the critical governance gap. If a skill is **deleted** from Now Assist without first being **retired**, the AICT record is NOT updated. The asset will appear as Deployed in AICT even after the skill is gone. This creates phantom deployed assets in your inventory. **Governance policy:** always retire a skill before deleting it. Establish this as a mandatory step in your AI asset decommissioning standard operating procedure.

### Models (from `sys_generative_ai_model_config`)
- Inclusion: `Active = true`
- Fields tracked: `active`, `max_tokens`, `model`, `supported_languages`, `domain_id`

### Datasets (from `sys_one_extend_test_dataset`)
- Inclusion: `Published = true` AND `eval_run` datasets only
- Fields tracked: `status`, `parent`, `name`, `description`

> **Risk Officer Note:** Only **published** evaluation datasets sync. Development or draft datasets do not appear in AICT. This means your AICT dataset inventory reflects only what has been formally published for evaluation — not every dataset used internally. Be aware of this gap if your governance framework requires tracking of all datasets, including development and test datasets.

### Prompts (from `sys_generative_ai_config`)
- Inclusion: Active prompts with active model AND linked skill
- Fields tracked: `active`, `prompt`, `model`, `name`, `version`

> **Risk Officer Note:** A prompt only syncs if it has BOTH an active model AND a linked skill. Prompts in development (with inactive models or no linked skill) do not appear in AICT. Your system prompt governance must account for prompts in the "pre-sync" state — they are operational artifacts even if not yet visible in AICT.

### AI Agents (from `sn_aia_agent`)
- Inclusion: `Active = true`
- Fields tracked: `name`, `description`, `role`, `instructions`, `sys_created_by`, `domain_id`

### Tools (from `sn_aia_tool`)
- Inclusion: All tool records (no active filter)
- Fields tracked: `name`, `description`, `type`, `active`, `sys_created_by`, `domain_id`
- Target: `sn_ent_ai_tool` (NOT the digital asset tables — tools are attributes, not governed assets)

### Agent Use Cases (from `sn_aia_usecase`)
- Inclusion: `Active = true`
- Fields tracked: `name`, `description`, `sys_created_by`, `domain_id`

### Relationship Mappings (Agent-Tool and Usecase-Agent)
- Agent-tool mapping: All agent-tool mappings sync from `sn_aia_agent_tool_m2m`
- Usecase-agent mapping: All usecase-agent mappings sync from `sn_aia_team_member`
- Both go to `sn_ent_ai_system_subcomponent_m2m`

---

## Field Synchronization Details by Asset Type

### Skills/AI Systems — Key Fields Synced

| Field | Source | Governance Relevance |
|---|---|---|
| `active` | Skill config | Drives Deployed/In Development state in AICT |
| `datasets` | Skill config | Links to dataset assets — enables chain tracing |
| `prompts` | Skill config | Links to prompt assets — enables prompt governance |
| `model` | Skill config | Links to model assets — enables model tracking |
| `sys_created_by` | Skill config | Asset creator identity — accountability |
| `domain_id` | Skill config | Domain scoping for multi-tenant instances |
| `name`, `description` | Skill config | Human-readable asset identification |

### Models — Key Fields Synced

| Field | Governance Relevance |
|---|---|
| `max_tokens` | Token limit configuration — relevant for cost and misuse controls |
| `model` | Model identifier — links to provider records |
| `supported_languages` | Scope of language support — relevant for global deployments |
| `domain_id` | Domain scoping |

---

## State Mapping: The Governance-to-Operational Bridge

The state mapping from Now Assist to AICT is the critical governance-to-operational alignment:

| Operational State (Now Assist) | Governance State (AICT) | What It Means |
|---|---|---|
| **Active** | **Deployed** | Skill is live and in use — full governance applies |
| **Published or Draft** | **In Development** | Skill is being developed — governance in progress |
| **Retired** | **Retired** | Skill has been formally decommissioned |
| **Deleted** | **No change** | Deletion bypasses governance — creates stale record |

> **Risk Officer Note:** The state mapping creates a governance obligation: when a skill transitions from Active to Retired in the Now Platform, the AICT record should automatically reflect this. Monitor your AICT inventory for "Deployed" assets whose corresponding skill config records are no longer active — these are governance anomalies that require investigation.

---

## What Does NOT Sync

Being explicit about what is out of scope for Now Assist discovery:

| Asset Category | Why It Doesn't Sync |
|---|---|
| Third-party AI assets (AWS, Azure, GCP, etc.) | Covered by Enterprise AI Discovery via SGC, not Now Assist discovery |
| Inactive/non-published models | Inclusion criteria require Active = true |
| Draft/development-only datasets | Inclusion criteria require Published = true |
| Platform skills and their children | Explicitly excluded from skill sync |
| Prompts without a linked active model | Inclusion criteria require active model + linked skill |
| Deleted skills | State = "Deleted" produces no AICT update |

> **Risk Officer Note:** The gap between what AICT shows and what actually exists in the Now Platform is a function of these exclusions. Run periodic reconciliation reports comparing `sn_nowassist_skill_config` (total active skills) against `alm_ai_system_digital_asset` (total AICT system records) to identify uncovered assets.

---

## Additional Reference

For detailed documentation on the model, dataset, prompt, and skill sync process, ServiceNow maintains KB article **KB2674041** in the Now Support Knowledge Base. This article covers edge cases, troubleshooting, and recent updates to the sync logic.

---

## Governance Implications for Managed vs. Unmanaged Assets

When assets sync from Now Assist to AICT, they appear in the **Unmanaged** section by default. The sync populates the record but does NOT automatically:
- Assign a lifecycle phase
- Trigger a governance playbook
- Assign a risk classification
- Create an assessment

**Exception:** Initiating a steward review for an unmanaged asset (or an Automation Rule qualifying the asset) transitions it to Managed and triggers the lifecycle.

> **Risk Officer Note:** Auto-synced assets start as Unmanaged — they are visible in AICT but not governed. The act of moving an asset from Unmanaged to Managed is the governance decision. Without this transition, 293 AI systems can exist in your AICT inventory (as seen in your CareAtlas instance) and still carry zero governance. The sync gives you visibility; the Managed/Unmanaged transition gives you control.

---

## Monitoring and Troubleshooting the Sync

**Confirm sync health:**
- The KB2674041 article covers the full sync process and troubleshooting
- Verify the scheduled sync job is active (job name not specified in documentation — check with ServiceNow admin)
- After any bulk operation in Now Assist (deploying multiple skills, retiring agents), allow time for sync to propagate

**Signs of sync issues:**
- Assets active in Now Assist but not visible in AICT (may be excluded by inclusion criteria or sync failure)
- Assets showing "Deployed" in AICT but inactive/deleted in Now Assist (stale records from deletion without retirement)
- Missing relationship links (agent-tool M2M not populated even though tools exist)

---

## Key Takeaways for AI Risk & Compliance Officers

1. **Auto-sync populates AICT but does NOT govern** — synced assets start as Unmanaged; governance requires explicit transition to Managed.
2. **Deleted skills leave stale AICT records** — enforce a retire-before-delete policy for all skill decommissioning.
3. **Not all assets sync** — inactive models, draft datasets, unpublished prompts, and platform skills are all excluded.
4. **State mapping creates governance obligations** — monitor for Deployed AICT records whose source skills are no longer active.
5. **Third-party AI assets require Enterprise AI Discovery** — Now Assist discovery is ServiceNow-internal only.
6. **Relationship tables are as important as asset records** — if agent-tool M2M records are missing, tool-level risk cannot be assessed at the system level.
7. **Reconcile AICT against source tables periodically** — the gap between raw skill count and AICT record count reveals governance coverage gaps.

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 777–778, 86–88*
