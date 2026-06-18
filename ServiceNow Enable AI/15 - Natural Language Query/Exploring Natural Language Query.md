# Exploring Natural Language Query

## SOURCE INFORMATION

* SECTION NAME: Natural Language Query
* SUBSECTION NAME: Exploring Natural Language Query
* SOURCE FILE NAME: Natural Language Query.pdf
* PAGE RANGE: 1234-1235
* EXTRACTION DATE: 2026-06-17

---

# CONTENT

## Natural Language Query

Natural Language Query (NLQ) enables you to query the data in your instance by entering plain language requests into the user interface.

## Get started

Choose one of these tiles to get started.

| Tile | Source text |
|---|---|
| Explore | Learn about NLQ concepts and features. |
| Use | Use NLQ to query your data with requests in natural language. |
| Configure | Set up NLQ for your environment. |
| References | Get details about properties and roles installed with NLQ. |

![Explore tile icon](_assets/page-1234-get-started-explore-icon.png)
![Use tile icon](_assets/page-1234-get-started-use-icon.png)
![Configure tile icon](_assets/page-1234-get-started-configure-icon.png)
![References tile icon](_assets/page-1234-get-started-references-icon.png)

## Exploring Natural Language Query

NLQ is a ServiceNow AI Platform feature that is active by default. Use NLQ to query the data in your instance by entering plain language requests into the user interface.

ServiceNow® NLQ translates natural language user input into glide record queries. The queries are rendered into an executable structured format, such as a JavaScript Object Notation (JSON) file or a visual definition. The output, in whichever format, is the response to the user's request.

> **Note:** When a user enters a request directly into the user interface (UI), the text of the request is called an utterance in tables such as NLQ logs.

NLQ is a ServiceNow AI Platform feature that is active by default and supports the following data operations:

* Driving table suggestion
* Filtering
* Grouping and aggregations
* Sorting
* Data visualization (single score, list, bar chart, pie chart, time series)
* Business calendar
* Single number
* Multi-table

For more information, see Using Natural Language Query.

NLQ doesn't support domain separation. It also doesn't support on-premise instances.

### Language support

NLQ supports American English by default. For all applications and features except CMDB, NLQ also supports queries in Spanish, French, French Canadian, German, and Japanese.

You must first activate the languages on your instance for NLQ to parse queries in those languages. For more information, see Activate a language.

### Using NLQ in other applications and features

Other ServiceNow® applications and features can consume NLQ functionality. See the following resources for more information.

**Features that can consume NLQ**

| Application or feature | Information |
|---|---|
| Analytics Q & A | Create a report with Analytics Q&A |
| Configuration Management Database (CMDB) | Query your CMDB data without needing to know table relationships or data structures.<br><br>* Querying the CMDB<br>* Intelligent Search for CMDB<br><br>English is the only supported language for CMDB. |
| NLQ with AI Search in global search | NLQ Genius Results in AI Search (supports English only) |
| List V2 | Filter through any platform list by entering in a plain-language request. |

---

## IMAGE DESCRIPTIONS

### Repeated page header logo - source pages 1234-1235

* **What is shown:** The ServiceNow logo appears in the upper-left page header on each reviewed page.
* **Objects present:** Black lowercase `service` text, green `now` accent, and a small registered trademark symbol.
* **Visible text:** `servicenow®`.
* **Business purpose:** Identifies the documentation publisher and product brand.
* **Technical purpose:** Repeated page header branding; it does not change the NLQ procedure content.
* **Color meaning:** Green is used as the ServiceNow brand accent.

### Get started tile grid - source page 1234

* **What is shown:** A two-by-two tile grid under the heading `Get started`, separated by thin gray horizontal and vertical rules.
* **Objects present:** Four navigation tiles: `Explore`, `Use`, `Configure`, and `References`.
* **All visible text:**
  * `Explore` - `Learn about NLQ concepts and features.`
  * `Use` - `Use NLQ to query your data with requests in natural language.`
  * `Configure` - `Set up NLQ for your environment.`
  * `References` - `Get details about properties and roles installed with NLQ.`
* **Icon details:**
  * `Explore`: telescope outline with a green lens.
  * `Use`: human outline with a green oval base.
  * `Configure`: wrench/gauge outline with a green gear.
  * `References`: open-book outline with a green page block and black page lines.
* **Diagram components and relationships:** The grid visually maps four major learning paths to the same Natural Language Query section. There are no arrows or process flows.
* **Business purpose:** Helps readers choose whether to learn concepts, use the feature, configure it, or consult reference material.
* **Technical purpose:** Acts as a section navigation launcher for NLQ documentation categories.
* **Security boundaries:** None shown.
* **Color meaning:** Green highlights ServiceNow-branded icon accents; gray lines divide tile areas.

### Informational note icon - source page 1234

* **What is shown:** A black circular information icon next to the `Note:` callout about the term `utterance`.
* **Objects present:** Filled black circle with a white lowercase `i`.
* **Visible text near the icon:** `Note: When a user enters a request directly into the user interface (UI), the text of the request is called an utterance in tables such as NLQ logs.`
* **Business purpose:** Distinguishes explanatory terminology from the main body text.
* **Technical purpose:** Clarifies that the UI-entered natural-language request is recorded as an `utterance` in NLQ tables and logs.

### External-link indicators - source page 1235

* **What is shown:** Small external-link icons appear beside linked documentation references such as `Activate a language`, `Querying the CMDB`, `Intelligent Search for CMDB`, and `NLQ Genius Results`.
* **Objects present:** Teal link text and small icon marks indicating linked resources.
* **Business purpose:** Signals that the reader can navigate to related ServiceNow documentation.
* **Technical purpose:** Identifies supporting pages for language activation, CMDB querying, and AI Search integration.

---

## TABLES

### Source-page carryover table above the Natural Language Query heading - source page 1234

> Boundary note: This table appears above the `Natural Language Query` heading on source page 1234 and belongs to the prior TOC section. It is captured here for page-completeness auditing but is not treated as Natural Language Query subsection content.

| Table | Description |
|---|---|
| [sn_nlu_discovery_cluster] |  |
| Discovery Report Definition<br>[sn_nlu_discovery_report_definition] | Includes the necessary information for generating reports. |

### Get started tiles - source page 1234

| Tile | Description |
|---|---|
| Explore | Learn about NLQ concepts and features. |
| Use | Use NLQ to query your data with requests in natural language. |
| Configure | Set up NLQ for your environment. |
| References | Get details about properties and roles installed with NLQ. |

### Features that can consume NLQ - source page 1235

| Application or feature | Information |
|---|---|
| Analytics Q & A | Create a report with Analytics Q&A |
| Configuration Management Database (CMDB) | Query your CMDB data without needing to know table relationships or data structures.<br><br>* Querying the CMDB<br>* Intelligent Search for CMDB<br><br>English is the only supported language for CMDB. |
| NLQ with AI Search in global search | NLQ Genius Results in AI Search (supports English only) |
| List V2 | Filter through any platform list by entering in a plain-language request. |

---

## FIGURES

### Figure: Get started tile grid - source page 1234

* **Figure type:** Navigation tile grid.
* **Components:** Four labeled tiles, four icons, gray dividers, and explanatory text beneath each icon.
* **Connections/arrows/flows:** No arrows, directional flows, or architectural connections are present.
* **Labels:** `Explore`, `Use`, `Configure`, `References`.
* **Technical purpose:** Groups NLQ documentation actions into learning, usage, configuration, and reference paths.
* **Security zones/boundaries:** None.

---

## QUALITY ASSURANCE NOTES

* PAGES REVIEWED: Source pages 1234-1235, corresponding to PDF pages 1-2.
* IMAGES REVIEWED: Repeated ServiceNow page header logo; four Get started tile icons; informational note icon; external-link indicators.
* TABLES REVIEWED: Pre-section carryover table on page 1234; Get started tile grid; `Features that can consume NLQ` table.
* FIGURES REVIEWED: Get started tile grid.
* OCR ISSUES FOUND: Parsed text contained layout loss for the tile grid and table boundaries; no unresolved OCR errors remain in this subsection.
* OCR ISSUES CORRECTED: Restored `ServiceNow®`, separated tile labels from descriptions, corrected table row grouping, and normalized link text spacing.
* RECHECK PASSES COMPLETED: 12.
* SECTION MAPPING: TOC maps this subsection under `Natural Language Query` beginning on source page 1234.
* SUBSECTION MAPPING: Content begins at `Exploring Natural Language Query` on source page 1234 and continues through the text before `Using Natural Language Query` on source page 1235. Section-level introduction and `Get started` content on the same page are included here to avoid losing unscoped section content.
* FOLDER NAME VERIFIED: `Natural Language Query`.
* FILE NAME VERIFIED: `Exploring Natural Language Query.md`.
* PAGE HEADER/FOOTER ACCOUNTING: Repeated page footer text reviewed: `© 2026 ServiceNow, Inc. All rights reserved. ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries. Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.` Page numbers reviewed: 1234 and 1235.
