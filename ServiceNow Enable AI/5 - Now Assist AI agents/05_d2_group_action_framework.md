# Group Action Framework

_Source pages: 21–21 | Depth: 2_

---

<!-- page 21 -->
Step 2.1: Receive Incident Documentation:
Use Link Incident to Problem AI Agent to validate incident details and confirm no
existing problem linkage.
Step 2.2: Identify Relevant Problems:
•Execute search for relevant problems using incident short description.
•If no relevant problems found, inform the user: "No relevant problems found to
link." and proceed to Catalog Item Identification.
Step 2.3: Link Incident to Problem:
•Present most similar problem details to the user for approval.
•Upon user approval, link incident to problem using "Set problem to incident" tool;
confirm successful linkage to the user.
Step 3: Catalog Item Identification:
Identify and integrate relevant catalog items into the incident record.
Step 3.1: Receive Incident and Problem Context:
Use Find Catalog Item AI Agent to validate incident context and prepare for catalog
item search.
Step 3.2: Execute Catalog Item Search:
•Perform targeted search for relevant catalog items based on incident description.
•If no catalog items found, inform the user: "No relevant catalog items identified."
and proceed to final delivery.
Step 3.3: Integrate Catalog Item Details:
•Present catalog item choices to the user; upon selection, either add catalog item
details to incident additional comments or provide direct catalog item link.
•Confirm successful integration or delivery to the user and complete workflow.
Group Action Framework
Group Action Framework (GAF) is an intelligence feature on the ServiceNow AI Platform that
groups related records and applies actions to them using LLMs.
GAF overview
GAF is composed of two processes. The grouping process identifies clusters of similar records
(incident, cases, KB articles, etc.) and selects a set of representative records for the cluster.
The actioning process maps new records to clusters and executes large language model (LLM)
instructions for those clusters to achieve certain tasks, such as summarizing the contents of a
cluster or generating resolution steps based on steps that worked for records in that cluster. GAF
processes together benefit your AI agents and Now Assist generative features in multiple ways.