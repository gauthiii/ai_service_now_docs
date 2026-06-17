### Knowledge Base Readiness for Now Assist on the ServiceNow AI Platform


Customization and Now Assist
Customizing your ServiceNow instance is often necessary to meet unique business needs, but
it can introduce unintended consequences for Now Assist features. Changes to field names, UI
actions, workflows, or table structures may disrupt how Now Assist skills and agents operate. For
example, modifying field states or labels can interfere with skill conditions and input mapping,
while altering default UI actions may prevent agents from triggering correctly. Custom resolution
workflows might conflict with the logic embedded in native skills, and table-level variations
can affect where and how Now Assist functions across workflows. These customizations can
also create upgrade friction, requiring additional testing, rework, or reconfiguration to ensure
compatibility with new platform releases.
To mitigate these risks, you can use tools like the Now Assist Readiness Evaluation app to
identify high-impact customizations and plan for remediation before deploying or upgrading AI
features. For more information, see Now Assist Readiness Evaluation.
To maintain compatibility with Now Assist while accommodating custom configurations, several
mitigation strategies are available:
•Duplicate skills before adapting them.
•Adjust skill inputs and role conditions to reflect organizational processes.
•Add additional input sources, such as related tables or emails.
For more advanced needs, build custom generative AI skills tailored to your unique business
requirements, allowing for deeper integration without compromising core functionality.
For more information about customizing AI solutions, see How to approach building custom
generative AI solutions using Now Assist in the ServiceNow Community.
Knowledge Base readiness for Now Assist on the ServiceNow AI Platform
The knowledge base is the engine that enables Now Assist to deliver intelligent, accurate,
and context-aware responses across AI Search, Q&A Genius Results, and other AI-powered
experiences.
When users ask questions, Now Assist taps into your knowledge articles to generate answers
that reflect your organization’s expertise and policies. This means the quality, clarity, and
structure of your knowledge content directly influence the effectiveness of AI responses.
Outdated, inconsistent, or poorly written articles can lead to incorrect outputs and user
frustration. That’s why maintaining a clean, well-organized knowledge base is critical—not just for
documentation, but for enabling reliable AI performance.
The Knowledge Management Overview dashboard is a powerful tool for assessing AI readiness.
It provides key usage metrics such as article views, helpfulness ratings, and feedback trends,
helping content owners identify high-performing articles and prioritize updates to low-usage or
outdated content. For more information, see Knowledge Management Overview dashboard .
High-level checklist
1. Review existing KB articles and knowledge bases
Get the total count of published KB articles and the number of active knowledge
bases.
Why? To scope clean-up and identify high-priority content.
See: Knowledge Management Overview dashboard
2. Review the structural formatting of KB articles
© 2026 ServiceNow, Inc. All rights reserved. 27
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.

Check for consistent template use (KCS-based, Q&A, Issue-Cause-Resolution, etc.).
Ensure that the Knowledge Management Advanced plugin is active.
If you're using custom templates, determine whether they follow a consistent format.
Also ensure that key steps are clearly defined and consistently populated.
Why? Using templates consistently improves LLM understanding and
summarization.
See:
•Knowledge article templates
•Activate the Knowledge Management Advanced plugin
3. Ensure metadata completeness in KB articles
Make sure that fields such as Meta, Meta Description, Category, Author, and Validity
are populated.
Why? This practice enables precise AI filtering and targeting.
See:
•Create a knowledge article
•Best practices to use your knowledge articles with Now Assist (generative AI)
(ServiceNow Community)
4. Perform maintenance audits
Flag KB articles that have not been updated in a year or more, that have no
metadata, are duplicates, or are about to expire.
Why? Outdated content degrades user trust and AI performance.
See:
•Knowledge Management Overview dashboard
•Retire a knowledge article
•Identify and review duplicate Knowledge articles (requires Now Assist in
Knowledge Management)
5. Review top searched queries
Identify search queries and articles for optimization, and limit Now Assist Q&A
functionality to high-quality, optimized KB articles.
Why? This prevents low-value content from surfacing in answers.
See: Knowledge Management dashboard
Service Catalog readiness for Now Assist on the ServiceNow AI Platform
A well-structured Service Catalog is essential to unlocking the full potential of Now Assist. As
the backbone of many self-service workflows, the catalog enables Now Assist to interpret user
requests accurately, present the right options, and minimize friction in the experience.
When catalog items are clearly defined and conversationally enabled, Now Assist in Virtual
Agent can surface them more effectively, leading to higher self-service rates and better issue
deflection.
© 2026 ServiceNow, Inc. All rights reserved. 28
ServiceNow, the ServiceNow logo, Now, and other ServiceNow marks are trademarks and/or registered trademarks of ServiceNow, Inc., in the United States and/or other countries.
Other company names, product names, and logos may be trademarks of the respective companies with which they are associated.