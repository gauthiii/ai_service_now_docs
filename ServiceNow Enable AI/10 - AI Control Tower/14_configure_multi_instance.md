# Configure Multi-instance Management for AI Control Tower
> ServiceNow Zurich Release | AI Control Tower Documentation  
> Role: AI Risk & Compliance Officer Reference

---

## What Is This?

Multi-instance management is Step 3 of the AICT configuration sequence. It enables a **production (manager) instance** of AI Control Tower to control, manage, and communicate with **multiple sub-production (managed) instances**. This is the mechanism for organizations that have AI assets being developed in non-production environments and need a governed pathway to promote them to production.

---

## Prerequisites and Restrictions

**Available from:** Yokohama release onwards

**NOT supported on:**
- Government Community Cloud (GCC)
- On-premises instances

**Plugin requirement:**
- The plugin `com.glide.mif.mtls` must be active
- If not active: submit a support request with Now Support for MIF features to install it

**Role required:** AI steward (`sn_ai_governance_ai_steward`)

**Version requirement (as of May 2026):**
> "Confirm that both the prod and sub-prod instances are running the same AI Control Tower core version (6.2.4), which is the minimum supported version."

If there is an upgrade to version 6.2.4 in a sub-prod, it is advisable to upgrade the prod instance to 6.2.4 as well to confirm the multi-instance framework functions correctly.

---

## Configuration Procedure

**Steps:**

1. **Log in to all sub-prod instances** and select the prod (managed) instance as the **manager** for the AI Control Tower application
2. **Verify the configuration** by logging in to the prod instance and navigating to the **managed instances tab** under the Multi-instance setup page — all sub-prod (managed) instances should appear in this list

---

## What Multi-instance Synchronizes

### AI Inventory Information

When configured, a scheduled job starts synchronizing the following from sub-prod to prod:
- AI systems
- AI models
- Prompts
- Datasets
- **AI agents** (added in the September 2025 release)

The scheduled job synchronizes AI inventory information **from sub-prod instances to the prod instance** — the flow is unidirectional: sub-prod → prod.

### Rules Synchronization

Multi-instance setup also synchronizes **Automation Rules** — but in the reverse direction:
- Rules flow **from prod to sub-prod instances**
- This ensures consistent governance rules are applied across all environments

### Asset State During Multi-instance Sync — Critical Governance Point

The documentation explicitly addresses how asset states are handled during sync:

> "The AI inventory in production reflects the true state of your assets like models, datasets, or skills from a production standpoint. Even if a model or dataset is active in a sub-prod (lower) environment, it's still considered as under development from a prod perspective, since it's being tested and not yet live."

> "For this reason, you don't synchronize asset states across environments. An asset's state changes to deployed only when the asset and its related records are activated in the production system."

> "In summary, the state represents the overall lifecycle of the asset, not its local status in a specific environment."

**What this means in practice:**

| Sub-prod Asset State | State After Sync to Prod |
|---|---|
| Active in sub-prod | Considered "In Development" from prod's perspective |
| Deployed in sub-prod | Still "In Development" from prod's perspective |
| Retired in sub-prod | Propagated accordingly |

**The key principle:** A sub-prod asset being "Active" or "Deployed" in the lower environment does not mean it is "Deployed" in AICT governance terms from the prod instance's perspective. Only when the asset and its related records are activated in the production system does it become "Deployed" in AICT.

> **Risk Officer Note:** This state separation is a governance safeguard. It prevents sub-prod development work from contaminating the production governance record. An AI model active in a test environment is not a production deployment — and AICT treats it accordingly. This prevents "false deployed" records in your prod governance inventory. However, it also means the prod Risk & Compliance dashboard does not reflect sub-prod testing activity — which is correct governance behavior, but can confuse teams expecting to see all environments in one view.

---

## Preferences That Sync from Prod to Sub-prod

Two preferences can optionally be pushed from prod to all sub-prod instances:

### Data Sharing Preference

- When enabled: the data sharing preference from production is applied to all sub-prod instances
- Default: Off
- Note: All preferences for sub-prod instances are available in **read-only mode** when Multi-instance is configured and enabled

### Data Overflow Processing and Bursting Preference

- When enabled: data overflow and bursting preferences from production are applied to all sub-prod instances
- Default: Off

> **Risk Officer Note:** These preference sync options give you centralized control over data governance settings across all environments. For organizations with strict data handling policies (healthcare, financial services), enabling data sharing and overflow preference sync ensures that sub-prod environments do not inadvertently operate under looser data handling settings than production. Enable these if consistent data governance posture across all environments is a compliance requirement.

---

## Trust Configuration

For Cross-instance application trust configuration, the documentation references a separate section on Cross-instance application trust configuration. This involves:
- mTLS (mutual TLS) configuration between instances
- The `com.glide.mif.mtls` plugin that must be active
- Trust certificate management between prod and sub-prod instances

---

## AI Gateway in Configurations

The Configurations page includes the AI Gateway section with three tabs that are relevant to multi-environment governance:

**Settings tab:**
- Pause/resume all AI Gateway transactions (emergency stop across the instance)
- When paused: "Currently on" status shows; Pause button available

**AI connections tab:**
- Lists all allowed AI connections on the Gateway
- Exportable as PDF, JSON, Excel, CSV
- Columns: Name, Allowed on AI Gateway, Last updated by, Updated

**Global MCP clients tab:**
- View and add Global MCP clients
- CIMD = Client ID Metadata Document support
- Global clients, once created, are automatically available across ALL MCP servers

---

## Multi-instance Setup Page Navigation

**Navigate to:** `AI Control Tower > Configurations > Multi-instance setup`

This page shows:
- **Managed instances tab** — lists all sub-prod instances configured to sync with this prod instance
- **AI inventory information** — sub-prod instances selected for synchronization
- **Data sharing preference** — toggle (default: off)
- **Data overflow processing and bursting preference** — toggle (default: off)

---

## Governance Implications of Multi-instance Management

### For Risk & Compliance Officers

Multi-instance management creates a clear **environment lifecycle pathway** for AI assets:

```
Sub-prod development environment
    |
    v (sync: AI systems, models, prompts, datasets, agents)
Production (manager) instance — AICT governance applies
    |
    v (rules sync: automation rules pushed down)
Sub-prod instances receive consistent governance rules
```

This architecture means:
1. **All AI assets developed in sub-prod are visible to the prod AICT** — nothing can bypass the production governance view
2. **Asset states are environment-aware** — what's "active" in sub-prod is "in development" from a governance perspective
3. **Rules are centrally managed from prod** — governance rules cannot be overridden at the sub-prod level
4. **Data preferences are centrally controlled** — data sharing and overflow settings can be standardized across all environments

### Audit Trail Consideration

When a managed sub-prod instance is added or removed from the sync configuration, the audit logs first display a record of all instances being removed, followed by a separate record indicating the instance being added or removed. This creates an accurate audit trail of environment configuration changes.

---

## Key Takeaways for AI Risk & Compliance Officers

1. **Multi-instance is prod-centric** — prod is the governance authority; sub-prod instances are governed, not governing.
2. **Asset state does NOT sync** — an active sub-prod asset is "In Development" from prod's perspective; only prod activation changes governance state to "Deployed."
3. **Rules sync prod → sub-prod** — governance rules are pushed down centrally; sub-prod cannot override governance rules.
4. **Data preference sync is optional but recommended for regulated environments** — ensures consistent data governance posture across all instances.
5. **`com.glide.mif.mtls` plugin must be active** — this is the most common multi-instance configuration failure; check this plugin status first if multi-instance is not working.
6. **Version alignment is mandatory (6.2.4+)** — both prod and all sub-prod instances must run the same AICT core version; mismatched versions break the multi-instance framework.
7. **GCC and on-premises are not supported** — verify your cloud deployment model supports multi-instance before planning this capability.

---

*Source: ServiceNow AI Control Tower Documentation, Zurich Release, pp. 767–769, 820*
