# Examples of using AI agents

_Source pages: 231–232 | Depth: 1_

---

<!-- page 231 -->
Tool calling records metric scores
The tool calling evaluation metric assesses whether an AI agent correctly
constructs tool calls by validating the accuracy, completeness, and formatting
of the inputs it provides.
(continued)
Number Score Description
•Input key completeness: 1 - True – All required parameters are
present with exact name matches, and no unexpected parameters are
included.
•Input value correctness: 1 - True – Tool input values are correctly
mapped.
•Input format correctness: 1 - True – Tool inputs are in the correct
format.
0 False One or more of input key completeness, input value completeness, or input
format completeness wasn't successful.
•Input key completeness: 0 - False – A mandatory parameter is either
missing, its name doesn't match exactly, or an unexpected parameter was
found.
•Input value correctness: 0 - False – Tool input values are not
correctly mapped.
•Input format correctness: 0 - False – Tool inputs are not in the
correct format.
Note: The values of the sub-metrics are aggregated using an AND operator. If any one
value is 0, then the entire tool calling records metric score will be 0.
Examples of using AI agents
Review different ways that you can leverage the Now Assist AI agents application in agentic
workflows across the platform.
AI agents Overview
AI agents in the Now Assist application provide automated solutions for a wide range of business
processes and operational challenges. These agents can work independently or as part of
hierarchical structures to handle complex workflows, reduce manual effort, and improve service
delivery efficiency. You can leverage AI agents across multiple departments including IT Service
Management, Customer Service Management, and Human Resources.
Incident Management and Resolution
AI agents can automate the entire incident lifecycle from initial triage to resolution. When an
incident is created and assigned to a designated service desk user, the agent automatically
retrieves incident details, searches for similar historical incidents, and analyzes relevant
knowledge base articles. Based on this research, the agent determines an appropriate resolution
path.

<!-- page 232 -->
If the agent has high confidence in the solution, it posts the resolution in the work notes and
closes the incident automatically. When confidence is lower, the agent documents its findings
and reassigns the incident to a technical support specialist for review. This approach reduces
mean time to resolution while ensuring quality control for complex issues.
Case Management Automation
Similar to incident management, AI agents can handle case workflows in customer service
scenarios. Agents analyze case details, match them with historical cases, search knowledge
articles, and provide recommended solutions or next steps. This automation helps customer
service teams handle higher volumes of cases while maintaining consistent quality in responses.
Cross-Functional Process Automation
AI agents can orchestrate workflows that span multiple departments and systems. For instance,
an onboarding agent might coordinate tasks across HR, IT, facilities, and finance departments,
ensuring new employees receive proper access, equipment, workspace setup, and orientation
materials. The agent can track progress, send reminders, escalate delays, and provide status
updates to stakeholders throughout the process.
Knowledge Management and Content Discovery
AI agents can assist users in finding relevant information by analyzing queries, searching across
multiple knowledge sources, and presenting contextualized results. These agents understand
the user's intent, consider their role and permissions, and deliver targeted information that helps
them complete tasks or resolve issues independently.
Virtual Agent Enhancement
AI agents can work behind the scenes to enhance Virtual Agent conversations by providing
intelligent responses, retrieving relevant information, and executing actions on behalf of users.
This integration creates more capable and helpful conversational experiences that can handle
complex queries and multi-step processes.
Implementation Considerations
When implementing AI agents, organizations should consider the following factors:
•Start with well-defined, repetitive processes that have clear success criteria
•Ensure adequate training data and knowledge base content for agents to reference
•Define appropriate confidence thresholds for automated actions versus human review
•Establish monitoring and quality assurance processes to track agent performance
•Plan for iterative improvements based on agent interaction data and outcomes
•Configure memory sharing appropriately for different hierarchy structures
•Consider scalability requirements when designing complex agent hierarchies
Resolve an incident
Help your live agents resolve an incident faster with Now Assist AI agents by using the Now
Assist panel.
https://player.vimeo.com/video/1098087911?
h=d89ede16f9&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479