# Configuring Knowledge Graph

_Source: ServiceNow Now Assist documentation, pages 991-993._

## Overview

This subtopic covers planning and configuring the Knowledge Graph implementation. Knowledge Graph is a ServiceNow AI Platform feature that is available with activation of any ServiceNow generative AI application. It covers the configuration overview, configuring the large language model (LLM) for Knowledge Graph, and configuring the Microsoft OneDrive application for Knowledge Graph (used to fetch user-specific external data such as shared files for people citation in Virtual Agent).

## Features

- Knowledge Graph plugins are installed by default on activation of any ServiceNow generative AI application.
- Configure Knowledge Graph for Virtual Agent (including prebuilt integration for Slot filling).
- Support for Workflow Data Fabric to retrieve data from different systems without moving them, ensuring efficiency and security with sensitive information.
- Choose which LLM service provider to use for Knowledge Graph (NowLLM, Claude Large, GPTLarge, or Gemini).
- Configure the Microsoft OneDrive application to authenticate Microsoft SharePoint and fetch external data such as shared files used for people citation in Virtual Agent.

## Functionalities

### Configuration overview

Knowledge Graph is a ServiceNow AI Platform feature that is available with activation of any ServiceNow generative AI application. On activation, the following Knowledge Graph plugins are installed by default:

- Graph QL plugin
- Knowledge Graph application

To implement Knowledge Graph adoption, you must configure Knowledge Graph for Virtual Agent. For pre-built integration with Now Assist Virtual Agent for Slot filling, configure Knowledge Graph in Virtual Agent. Refer to "Configuring assistants overview" for admin-guided setup.

Knowledge Graph supports Workflow Data Fabric, which enables users to retrieve data from different systems without moving them. This ensures efficiency and security when working with sensitive information. To configure and integrate the Workflow Data Fabric tables for Knowledge Graph, see "Managing data fabric tables in Workflow Data Fabric Hub."

### LLM options for Knowledge Graph

LLMs are part of the foundation for Knowledge Graph. Different LLMs can provide slightly different performance and responses. You can select which LLM to use for your Knowledge Graph schema. The default-toggle options are:

- TextToResult (NowLLM)
- TextToResult (Claude Large)
- TextToResult (GPTLarge)
- TextToResult (Gemini)

### Microsoft OneDrive application configuration components

Knowledge Graph uses the Microsoft OneDrive application for authentication of Microsoft SharePoint, required to fetch external data such as shared files used for people citation in Virtual Agent. To complete the configuration, you must:

- Create the Microsoft OneDrive application.
- Set up the Knowledge Graph application on the Microsoft OneDrive tenant.
- Update Microsoft OneDrive permissions for delegated access.
- Create a new client secret and complete the authentication process.

Relevant ServiceNow records/settings include:

- **Application registry** (All > System OAuth > Application registry) — the **KG MS OneDrive Delegated Connector** record, with Client ID, Client secret, Authorization URL, Token URL (with `[tenantId]` placeholder), and Redirect URL fields.
- Microsoft Graph delegated permissions: `offline.access` and `Sites.Read.All`.
- Redirect URI / Front-channel logout URL: `https://<instanceURL>/oauth_redirect.do`.

## Instructions / Procedures

### Configure LLM for Knowledge Graph

**Before you begin** — Different LLMs can provide slightly different performance and responses. Role required: `admin`.

**Procedure:**

1. Navigate to **All > sys_one_extend_capability.list > TextToResult**.
2. Open the **TextToResult** record and select **OneExtend Definition Configs** (related list).
3. For one of the following options, change the value of the **default** field to True:
   - TextToResult (NowLLM)
   - TextToResult (Claude Large)
   - TextToResult (GPTLarge)
   - TextToResult (Gemini)

   Once you select the default LLM, ensure that the **Default** field value for another LLM is set to False.
4. Select the LLM to open the record and update the default field to True.

### Configure Microsoft OneDrive application for Knowledge Graph

Use Microsoft SharePoint for fetching user-specific external data, such as shared files, from external services through a Knowledge Graph API.

**Before you begin** — Knowledge Graph uses the Microsoft OneDrive application for authentication of Microsoft SharePoint required to fetch external data such as shared files used for people citation in Virtual Agent. To view the shared files, configure the Microsoft OneDrive application with Knowledge Graph. Role required: `admin`.

**Procedure:**

1. Go to portal.azure.com and select **view** to Manage Microsoft Entra ID.
2. To register the app, do the following:
   - Select **Manage > App registration** and select **New Application**.
   - Add a **Name** for the application.
   - Select **Accounts in this organizational directory only** single-tenant apps for use.
   - Select **Register**.

   > **Note:** Copy and save the Application ID and Tenant ID for future reference.
3. Once the new application is registered, add the client credentials:
   - Select **Add a certificate or secret**.
   - Select **New client secret** and add Description and Expiry duration.
   - Select **Add**.
   - Ensure that you copy and save the **New client secret value** that is created.
4. Select **Overview** from the left navigation pane to add the redirect URL.
   - Select **Add a redirect URI**.
   - Select **Add a platform** from the platform configurations section.
   - Add `https://<instanceURL>/oauth_redirect.do` in the **Redirect URIs** and **Front-channel logout URL** fields on the configure web page.

     > **Note:** Replace the `<instanceURL>` with your instance path. Example: `abc.service-now.com`.
   - Select both the **Access token** and **ID tokens** option from the "Select the token you would like to be issued for authorization endpoint" section.
   - Select **Configure**.
5. Select **Manage > App permissions** from the left navigation pane to add permissions.
   - Select **Add a permission**.
   - Select **Microsoft Graph**.
   - Select **Delegated permission**.
   - Add and select `offline.access` and `Sites.Read.All` in the Select permissions section.
   - Select **Add permissions**.
   - Ensure that the **Admin consent required** field is set to Yes for the newly added Microsoft Graph.
6. Go to your ServiceNow instance to change the Application registry settings:
   - Select **All > System OAuth > Application registry**.
   - Select **KG MS OneDrive Delegated Connector**.
   - Add the copied Application ID in the **Client ID** field.
   - Add the Client secret in the **Client secret** field.
   - Add the Tenant ID in the placeholder for `[tenantId]` in the **Authorization URL** and **Token URL** field.
   - Ensure that the **Redirect URL** is correct.
   - Select **Update**.

## Figures, Diagrams & Screenshots

The pages in this subtopic (991-993) are text-only procedure pages and do not contain screenshots, diagrams, or other graphics. The only recurring graphic is the ServiceNow wordmark/logo in the page header, which is decorative.
