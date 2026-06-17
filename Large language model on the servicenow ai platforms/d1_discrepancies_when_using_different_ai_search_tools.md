# Discrepancies when using different AI search tools

*Source: document pages 126–126 (PDF chunk pages 26–26)*

---



<!-- doc page 126 -->

Resources for writing LLM instructions for Now Assist skills (continued)
Skill Reference
Code generation General guidelines for code generation
Flow generation Exploring flow generation
LLM topic skill for Virtual
Agent
Now Assist Skill Kit General guidelines for Now Assist Skill Kit
RPA bot generation General guidelines for RPA bot generation
Test generation Design considerations for prompting
UI generation General guidelines UI generation
Long term stable models
Long term stable (LTS) models support regulated industries, such as financial institutions, with
stronger AI lifecycle management, governance, transparency, and compliance tools.
Long term stable models enable you to adopt AI confidently while supporting customers in their
operational and compliance needs. These models also integrate with tools like AI Control Tower
to support customers with governance, monitoring, and compliance controls along with guidance
for implementing AI responsibly.
LTS models provide predictable AI updates, longer model stability windows, and early access
testing for smoother adoption.
You can configure long terms stable models in AI Control Tower. You can also navigate to
Manage model providers section in the Now Assist settings and select Now LLM Service-LTS as
a provider for specific Now Assist skills.
Discrepancies when using different AI search tools
Different AI search tools may return different answers for the same or similar searches. This
difference in results is expected. It occurs because each large language model (LLM) uses a
different approach to find results and generate answers that match your search.
Overview of how LLMs create responses
Large Language Models don’t retrieve answers from a single source. Instead, they generate
responses by predicting the next most likely word, one at a time, based on patterns they’ve
learned from the data they were trained on.
Because of that, several factors can make the answers vary each time. The factors include:
•Probability
•Multiple good answers
•Context sensitivity
•LLM variation
Answer generation involves probability, context, and variation. Therefore, responses to the same
question can differ slightly each time it is asked, and from provider to provider.

ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

| Skill | Reference |
| --- | --- |
| Code generation | General guidelines for code generation |
| Flow generation | Exploring flow generation |
| LLM topic skill for Virtual Agent |  |
| Now Assist Skill Kit | General guidelines for Now Assist Skill Kit |
| RPA bot generation | General guidelines for RPA bot generation |
| Test generation | Design considerations for prompting |
| UI generation | General guidelines UI generation |
