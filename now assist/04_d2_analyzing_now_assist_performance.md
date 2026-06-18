# Analyzing Now Assist performance

_Source pages: 56–108 | Depth: 2_

---

<!-- page 56 -->
12. Select an option from the Select a record to test the configurations drop-down menu.
13.Select Preview and Done.
Analyzing Now Assist performance
Use the Now Assist Analytics dashboard to monitor the usage and performance of generative AI
features and capabilities offered under Now Assist.
https://player.vimeo.com/video/1063716199?
h=247ef99aa4&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479
Get started
Explore Configure
Learn more about Now Assist Analytics Configure Now Assist Analytics
Use Reference
Use Now Assist Analytics Learn about user roles
in Now Assist Analytics
Troubleshoot and get help
•Ask questions and explore other resources for in the ServiceNow Community
•Search the Known Error Portal for known error articles
•Contact Customer Service and Support
AI limitations
This application uses artificial intelligence (AI) and machine learning, which are rapidly evolving fields of study that generate predictions based on patterns
in data. As a result, this application may not always produce accurate, complete, or appropriate information. Furthermore, there is no guarantee that this
application has been fully trained or tested for your use case. To mitigate these issues, it is your responsibility to test and evaluate your use of this application for
accuracy, harm, and appropriateness for your use case, employ human oversight of output, and refrain from relying solely on AI-generated outputs for decision-
making purposes. This is especially important if you choose to deploy this application in areas with consequential impacts such as healthcare, finance, legal,
employment, security, or infrastructure. You agree to abide by ServiceNow’s AI Acceptable Use Policy , which may be updated by ServiceNow.

<!-- page 57 -->
Data processing
This application requires data to be transferred from ServiceNow customers' individual instances to a centralized ServiceNow environment, which may be located
in a different data center region from the one where your instance is, and potentially to a third-party cloud provider, such as Microsoft Azure. This data is handled
per ServiceNow's internal policies and procedures, including our policies available through our CORE Compliance Portal .
Data collection
ServiceNow collects and uses the inputs, outputs, and edits to outputs of this application to develop and improve ServiceNow technologies including ServiceNow
models and AI products. Customers can opt out of future data collection at any time, as described in the Now Assist Opt-Out page.
Exploring Now Assist Analytics
Learn how Now Assist Analytics enables users with the Now Assist Analytics Viewer or Now
Assist Analytics Admin role to monitor the usage, value, and performance of generative AI
features and capabilities offered under Now Assist.
Now Assist Analytics overview
The Now Assist Analytics dashboard is built on the Platform Analytics experience. The
dashboard contains indicators and breakdowns that provide actionable insights into the usage,
value, and performance of your Now Assist implementation, including Now Assist Guardian, Now
Assist context menu, and search.
Now Assist Analytics users
Users
User Description
Now Assist Analytics Admin Now Assist Analytics admins monitor usage, value, and
performance of the Now Assist implementation, including Now
Assist Guardian, Now Assist context menu, and search. They
also configure skill-dashboard mappings to view individual skill
usage and performance indicators.
Now Assist Analytics Viewer View the dashboard pages to monitor usage and performance
indicators.
Now Assist Analytics benefits
Now Assist Analytics benefits
Benefit Feature Users
Monitor usage, value, and adoption of Now Assist Analytics
•Usage and adoption
Now Assist, skill performance, Now Assist Admin or Now Assist
•
Guardian, Now Assist context menu, and Analytics Viewer
search. •Skills performance
•Now Assist
Guardian analytics
•Now Assist context
menu analytics
•User search
analyzer

<!-- page 58 -->
What to explore next
To learn more about configuring and using Now Assist Analytics, see:
•Configuring Now Assist Analytics
•Using Now Assist Analytics
•Now Assist Analytics reference
Configuring Now Assist Analytics
Configure the Now Assist Analytics dashboard to view the usage, value, and performance
indicators of Now Assist.
Configuration overview
Now Assist Analytics requires at least one Now Assist application, for example, Now Assist for
Customer Service Management (CSM), to be installed and configured on your instance. See
Installing Now Assist Analytics for more information.
The following is an optional configuration task used to map a Now Assist skill to a dashboard.
Map a skill to a dashboard to view skill usage and performance indicators.
Domain Separation
Now Assist Analytics supports domain separation only for indicators using the following data
collection jobs.
•[GenAI Analytics] Daily Data Collection
•[GenAI Analytics] Historical Data Collection
•[Now Assist Analytics] Daily Data Collection
•[Now Assist Analytics] Historical Data Collection
See Approaches to Performance Analytics with domain separation for more information on
applying domain separation configuration.
Note: Be sure to check the Run as field in the data collection job records has a valid user.
Installing Now Assist Analytics
You can install the Now Assist Analytics application (sn_na_analytics) with Now Assist
applications if you have the admin role.
Installation requirements
You must be on Zurich Patch 0 or later.
Now Assist Analytics is included as a dependency for all Now Assist applications. It is not
recommended to install the application by itself. Instead, you can install Now Assist applications
from the Now Assist Admin console or directly from the ServiceNow Store. For details, see Install
Now Assist plugins.

<!-- page 59 -->
Now Assist Admin console plugin installation
Compatibility matrix
Now Assist Analytics has a dependency on Now Assist Admin. Be sure to have the compatible
version of the Now Assist Admin console based on the following compatibility matrix.
Now Assist Admin console
Now Assist Analytics version Release
version
Now Assist Analytics 2.0.14 Now Assist Admin 5.0.7 Zurich Patch 1
Now Assist Analytics 1.1.11 Now Assist Admin 4.1.16 Zurich Patch 0
Map a skill to a dashboard
Map a Now Assist skill to a dashboard to view skill performance indicators and skill details.
Before you begin
Be sure to map a dashboard with a skill in the same domain.
Note: You can only map a skill to a dashboard. Mapping a feature (that consists of multiple
skills) is currently not supported.
If you're mapping a skill to a custom dashboard, be sure to share appropriate access to the
dashboard. See Share a Platform Analytics dashboard for more information.
Roles required: sn_na_analytics.admin and sn_nowassist_admin.nsa_admin
Procedure
1.Navigate to the All menu and enter sn_na_analytics_configuration.list.
The Now Assist Analytics Configuration [sn_na_analytics_configuration] table
appears.
2. Create a new mapping by selecting New
3. On the form, fill in the fields.

<!-- page 60 -->
Now Assist Analytics Configuration record form
Field Description
Dashboard The Dashboard that you want to map to a
skill. Use the lookup icon ( ) to search for
and select the dashboard.
Application The application that contains the record.
Document Table Table that contains configured skills.
Use the lookup icon ( ) to search for
and select the Now Assist Skill Config
[sn_nowassist_skill_config] table.
Document Id The Skill that you want to map to the
dashboard. Use the lookup icon ( ) to
search for and select the skill that you want to
map to the dashboard.
Active Check box used to enable or disable the
mapping.
Order Order to set that determines the priority of
the mapping in cases where multiple skills
are mapped to the same dashboard.
4.Select Submit.
What to do next
After you've completed the mapping, go to the Skill details page and select the skill from the
drop-down list to verify that the mapped dashboard is displayed.
Using Now Assist Analytics
The Now Assist Analytics dashboard provides indicators and breakdowns that help monitor the
performance of generative AI features, capabilities, and skills active on your instance.
Access the dashboard by navigating to All > Now Assist Admin > Analytics. You must
have Now Assist Analytics Admin [sn_na_analytics_admin] or Now Assist Analytics Viewer
[sn_na_analytics_viewer] role to view the dashboard. The following sections explain the
dashboard pages in more detail.
Usage and adoption
The Usage and adoption dashboard page contains key usage and performance indicators that
help you evaluate the adoption of Now Assist in your organization.
The Usage and adoption dashboard page is the landing page for the dashboard. The Usage
and adoption dashboard page contains two tabs that provide insights on usage summary and
adoption.
The Usage summary page includes indicators on total and daily Now Assist actions, skill
distribution and engagement trend, and daily unique users who have engaged with Now Assist.
The Adoption page tracks the departments with the highest Now Assist usage, comparison of
actions by department, and feedback and error details. Use the date range, channel, and product
filters to view usage and adoption indicators for the selected period, Now Assist channel, and
product, respectively. The default date range is 30 days.

<!-- page 61 -->
Usage and adoption dashboard page
The indicators on the Usage and adoption dashboard page provide the following insights. See
Now Assist Analytics dashboard indicator details for information on data source and calculations
behind each indicator on the page.
•Skills engagement trend for a selected period can reveal skills that have been used more
frequently or less frequently.
•Total and daily actions for a selected period can reveal the scale of Now Assist actions
executed. The trend line in the visualization shows periods of increased or declining
engagement.
•Average and daily unique users can reveal user engagement with Now Assist.
Usage summary indicators
Total Now Assist actions
This area of the dashboard shows the total number of Now Assist actions in the
selected date range. A single use of a Now Assist skill represents an action. Select
a filter combination to view the number of actions by products or Now Assist
channels. For example, you can view the number of Now Assist actions executed
through the Now Assist in Virtual Agent channel for Now Assist for Customer Service
Management (CSM) product.

<!-- page 62 -->
Total Now Assist actions indicator
Daily Now Assist actions
This area of the dashboard shows the number of Now Assist actions executed per
day in the selected date range.
Daily Now Assist actions indicator
Average daily unique users engaging with Now Assist
This area of the dashboard shows the average number of daily unique users who
engaged with Now Assist actions in the selected date range. Average number of
daily unique users is an indicator of the level of Now Assist engagement across
selected Now Assist products and channels.

<!-- page 63 -->
Average number of unique users per day who triggered actions
indicator
Daily unique users engaging with Now Assist
This area of the dashboard shows the daily unique users who engaged with Now
Assist actions in the selected date range.
Daily unique users engaging with Now Assist indicator
Skill group distribution
This area of the dashboard shows the skill usage in a trend chart for the selected
filters. The visualization is interactive. Use the Group by filter to apply predefined
breakdowns. Hover over the trend lines to see the number of times that each skill
was used. Selecting one or more items in the legend removes the trend line for
those items. You can compare and contrast skill usage distribution in a date range
to understand in-demand skills, and skills that are low on usage and need further
analysis.

<!-- page 64 -->
Skill group distribution indicator
Daily usage comparison by workflow
This area of the dashboard shows the number of Now Assist actions executed per
day against each workflow in the selected date range. Hover over a bar to view the
count of Now Assist actions executed for a workflow on that day.
Daily usage comparison by workflow indicator
Skill engagement trend
This area of the dashboard shows the skill usage in a trend chart for the selected
filters. The visualization is interactive. Hover over the trend lines to see the number
of times that each skill was executed. Selecting one or more skills in the legend
removes the trend line for those skills. You can compare and contrast skill usage
levels in a date range to understand in-demand skills, and skills that are low on
usage and need further analysis.
Skills engagement trend indicator
Adoption indicators
Departments with highest usage
This area of the dashboard shows the departments with the highest usage of Now
Assist actions in the selected date range. Hover over the horizontal bars to view the
count of actions for a particular department.

<!-- page 65 -->
Departments with highest usage indicator
Now Assist actions comparison by user department
This area of the dashboard shows the number and type of Now Assist actions
executed against each department in the selected date range.
Now Assist actions comparison by user department indicator
Feedback details
This area of the dashboard shows the number of Now Assist actions, number of
feedback provided by users of Now Assist actions, and number of Now Assist
actions with positive feedback in the selected date range.
Feedback details indicator
Error details
This area of the dashboard shows the number of Now Assist actions and the
number of Now Assist actions resulting in errors.
Error details indicator

<!-- page 66 -->
Skills performance
Use the Skills performance dashboard page to view usage and performance indicators of one or
more Now Assist skills that are active.
The Skills performance dashboard page contains indicators that help you analyze the usage
and performance of active skills. Use the Date range, Product, and Skills filters to break down
by date range, Now Assist product, and skill, respectively. The filter selection applies to all
visualizations on the page. See Now Assist Analytics dashboard indicator details for information
on the data and calculations behind each indicator.
Skill Performance dashboard page
The indicators on the Skills performance dashboard page provide the following insights. See
Now Assist Analytics dashboard indicator details for information on the data and calculations
behind each indicator.
•Skills usage trend visualization for a selected period can reveal skills that have been used
more frequently or less frequently.
•The Number of actions visualization for a selected period can reveal the scale of Now Assist
skill executions. The trend line comparison shows the increasing or decreasing trend from the
previous period.
•The Total daily active users indicator shows a breakdown of daily active users by product and
skill.
Select the View skill details button to view the usage and performance indicators of skills
mapped to a dashboard.
Skills performance indicators
Skills engagement trend
This area of the dashboard shows the skill usage in a trend chart for the selected
filters. The visualization is interactive. Hover over the trend lines to see the number

<!-- page 67 -->
of times that each skill was used. Selecting one or more skills in the legend removes
the trend line for those skills. You can compare and contrast skill usage levels in
a date range to understand in-demand skills, and skills that are low on usage and
need further analysis.
Skills usage trend indicator
Number of actions
This area of the dashboard shows the number of Now Assist actions for the selected
date range, product, and skill. A single use of a skill represents an action. The
headline number is an indicator of the scale of skill usage across products. The
trend line comparison shows the increase or decrease in the number of actions
from the previous period.

<!-- page 68 -->
Number of actions indicator
Total daily active users
This area of the dashboard shows the cumulative number of daily active users
who have used Now Assist products with one or more active skills. Select a filter
combination to see skill usage patterns. For example, you can visualize the number
of users who have used the Chat Summarization skill across all products in the last
month.

<!-- page 69 -->
Total daily active users indicator
Total daily active users by skills
This area of the dashboard shows the number of daily active users who have used
Now Assist skills in the selected date range. When you hover over a date in the
visualization, a pop-over shows all active skills with the count of users against each
skill. Select a filter combination to visualize patterns in user activity.
Total daily active users by skills indicator
Skill details
Use the Skill details dashboard page to view usage and performance indicators of a skill.

<!-- page 70 -->
The Skill details dashboard page contains indicators pertaining to a specific skill. The indicators
provide insight into skill usage and performance. Select a skill from the drop-down list to view
the indicators. The drop-down lists both active and inactive skills. Each skill has a subtitle that
identifies the skill family that it belongs to, for example, ITSM, HR, and so on. Use the date range
filter to view skill usage and performance over a certain period. The date range filter selection
applies to all visualizations on the page. See Now Assist Analytics dashboard indicator details for
information on the data and calculations behind each indicator.
Skill details dashboard page
The indicators on the Skill details dashboard page provide the following insights. See Now Assist
Analytics dashboard indicator details for information on the data and calculations behind each
indicator.
•Skill engagement trend visualization for a selected period can reveal patterns in skill usage.
•Acceptance rate visualization shows how well the skill met the requirements of users who
used the skill. A high acceptance rate for a skill is an indicator of good performance. A low
acceptance rate among skill users indicates that the skill doesn’t meet the requirements either
fully or partially.
•The number of actions visualization for a selected period can reveal the scale of the skill
executions. The trend line comparison shows the increasing or decreasing trend from the
previous period.
•The daily active users visualizations show a breakdown of daily active users by skill to help you
see user activity on the skill.
Skill details indicators
The indicators on skill details pages might differ based on the skill selected. For example,
summarization skills might have different set of indicators compared to generation skills because
each skill is mapped to its own dashboard that contains a set of indicators related to the skill.
The Now Assist Analytics dashboard comes with some default skill-to-dashboard mappings to
get you started. The default dashboards are visible to users with the Now Assist Analytics Viewer
[sn_na_analytics.viewer] role. You can create your own dashboards and map them to skills. See
Create a dashboard with the in-line editor and Map a skill to a dashboard for more information
on creating custom dashboards and mapping them to skills, respectively.
The following indicators are for the Flow Generation skill.

<!-- page 71 -->
Skill usage trend indicator
This area of the dashboard shows the Flow Generation skill usage in a trend chart
for the selected filters. The visualization is interactive. Hover over the trend lines to
see the number of times the Flow Generation skill was used.
Skill usage trend indicator
Total Flow Generation actions indicator
This area of the dashboard shows the number of flow generation actions for the
selected date range. A single use of the Flow Generation skill represents an action.
The headline number is an indicator of the scale of flow generation skill usage
across products. The trend line comparison shows the increase or decrease in the
number of actions from the previous period.
Total flow generation actions indicator
Accepted flow generation actions indicator
This area of the dashboard shows the number of flow generation actions, that is, the
number of flow generation skill executions that resulted in flows that were accepted
by the users.

<!-- page 72 -->
Accepted flow generation actions indicator
Acceptance rate indicator
This area of the dashboard shows the acceptance rate of Flow Generation skill
based on user acceptance of the flow. The percentage is calculated using the
formula: (Total number of accepted flow generation actions/Total number of flow
generation actions) x 100.
Acceptance rate indicator
Custom skill details
Use the Custom skill details dashboard page to view usage and performance indicators of
custom skills.

<!-- page 73 -->
The Custom skill details dashboard page contains indicators pertaining to a custom skill. The
indicators provide insight into skill usage and performance. Select a skill from the Skills drop-
down list to view the indicators. The drop-down lists both active and inactive skills. Each skill has
a subtitle that identifies the skill family that it belongs to, for example, ITSM, HR, and so on. Use
the date range filter to view skill usage and performance over a certain period. The date range
filter selection applies to all visualizations on the page. See Now Assist Analytics dashboard
indicator details for information on the data and calculations behind each indicator.
Custom skill details dashboard page
The indicators on the Custom skill details dashboard page provide the following insights. See
Now Assist Analytics dashboard indicator details for information on the data and calculations
behind each indicator.
•Skill engagement trend visualizations for a selected period can reveal patterns in skill usage
across workflows, products, and features.
•The daily unique users visualization shows a breakdown of daily unique users by the selected
skill to help you see user activity and engagement with the skill.
•Acceptance rate visualization shows how well the skill met the requirements of users who
used the skill. A high acceptance rate for a skill is an indicator of good performance. A low
acceptance rate among skill users indicates that the skill doesn’t meet the requirements either
fully or partially.
•Skills feedback visualization shows that the feedback recorded based on user response to
each skill execution in the selected date range.
Skill details indicators
The Custom skill details page contains a common set of indicators that give you insights into
custom skills. Only those skills where the skill family is Other or the category is Custom are
shown in the skills filter on the page.
The following indicators are common across all custom skills.
Number of custom skills created
This area of the dashboard shows the number of custom skills created by the users
in the selected date range.

<!-- page 74 -->
Number of custom skills created indicator
Number of custom skills activated
This area of the dashboard shows the number of custom skills activated by the
users in the selected date range.

<!-- page 75 -->
Number of custom skills activated indicator
Number of prompts in active custom skills
This area of the dashboard shows the number of prompts in active custom skills in
the selected date range.
Number of prompts in active custom skills indicator
Number of Assists consumed by custom skills

<!-- page 76 -->
This area of the dashboard shows the number of Assists consumed by custom skills
in the selected date range.
Number of Assists consumed by custom skills indicator
Count of invocations
This area of the dashboard shows the count of invocations for the custom skills in
the selected date range.
Count of invocations indicator
Daily unique users engaging with the skill
This area of the dashboard shows the number of unique users per day who
engaged with the skill in the selected date range. The bar chart shows a trend of
increase or decrease in the number of unique users to help you understand periods
of high and low skill engagement.

<!-- page 77 -->
Daily unique users engaging with the skill indicator
Skill engagement trend by workflows
This area of the dashboard shows the skill usage across workflows in a bar chart for
the selected date range. The visualization is interactive. Hover over the bars to see
the number of times the skill was used in each of the workflows.
Skill engagement trend by workflows indicator
Skill engagement trend by products
This area of the dashboard shows the skill usage across Now Assist products in a
bar chart for the selected date range. The visualization is interactive. Hover over the
bars to see the number of times the skill was used in each of the products.
Skill engagement trend by products indicator
Skill engagement trend by features
This area of the dashboard shows the skill usage across Now Assist features in a
bar chart for the selected date range. The visualization is interactive. Hover over the
bars to see the number of times the skill was used in each of the features.
Skill engagement trend by features indicator

<!-- page 78 -->
Executed successfully
This area of the dashboard shows the acceptance rate of the selected skill based
on user feedback. The percentage is calculated using the formula: (Total number of
accepted skill executions/Total number of skill executions) x 100.
Executed successfully indicator
Skills feedback
This area of the dashboard shows the feedback recorded for each execution of the
selected skill. User feedback is categorized into the following:
•Accepted (edited & non-edited): The user accepted the skill output with or without
further edits to the output.
•Rejected: The user rejected the skill output.
•Canceled: The user canceled the skill execution.
•Ignored: The user didn't take any action based on the skill output.
Skills feedback indicator

<!-- page 79 -->
Now Assist Guardian analytics
Monitor the performance of guardrails enabled through Now Assist Guardian.
The Now Assist Guardian analytics dashboard helps admins monitor and evaluate the
effectiveness of offensive content and prompt injection guardrails in tracking and analyzing
requests sent to large language models (LLM) and their responses.
Now Assist Guardian dashboard page
The indicators on the Now Assist Guardian dashboard page provide the following insights.
•Average latency as a result of active offensive content and prompt injection guardrails. High
latency could mean increased guardrail activity in the period.
•Count and percentage of offensive content and prompt injection occurrences.
•Skills where offensive content and prompt injection occurrences were detected.
Apply the filters on the dashboard to view guardrail activity for skills in a date range. See Now
Assist Analytics dashboard indicator details for information on the data and calculations behind
each indicator.
Offensive content indicators
Guardrail-added latency
This area of the dashboard shows the average latency as a result of the active
offensive content guardrail for the selected skills and date range.

<!-- page 80 -->
Guardrail-added latency indicator
Percentage flagged as offensive
This area of the dashboard shows the percentage of requests and responses to and
from the LLM service that are flagged for offensive content.
Percentage flagged as offensive indicator
Total offensive content occurrences
This area of the dashboard shows the total number of offensive content
occurrences for the selected skills and date range.

<!-- page 81 -->
Total offensive content occurrences indicator
Categories of offensive content
This area of the dashboard shows a breakdown of offensive content occurrences by
the categories. If content is deemed to be offensive under more than one category,
for example, toxic and defamatory, the occurrence is counted individually toward
both the categories. For more information on offensive content categories, see Now
Assist Guardian.
Categories of offensive content indicator
Offensive content occurrences by skill
This area of the dashboard shows the number of offensive content occurrences
over time by the skills in which the content is detected.
Offensive content occurrences by skill indicator

<!-- page 82 -->
Prompt injection indicators
Guardrail-added latency
This area of the dashboard shows the average latency as a result of the active
prompt injection guardrail for the selected skills and date range.
Guardrail-added latency indicator
Percentage flagged as prompt injection
This area of the dashboard shows the percentage of requests and responses to and
from the LLM service that are flagged for offensive content.
Percentage flagged as prompt injection indicator
Total prompt injection occurrences
This area of the dashboard shows the total number of offensive content
occurrences for the selected skills and date range.

<!-- page 83 -->
Total prompt injection occurrences indicator
Prompt injection occurrences by skill
This area of the dashboard shows the number of prompt injection occurrences over
time by the skills where prompt injection attempts were detected.
Prompt injection occurrences by skill indicator
User search analyzer
Gain insights into user search queries and results provided by Now Assist.
The User search analyzer dashboard page contains indicators that help admins understand the
effectiveness of search in enhancing the self-service experience. Equipped with insights from
the dashboard, Knowledge admins can improve Knowledge content and availability for search.

<!-- page 84 -->
User search analyzer dashboard page
The indicators on the User search analyzer dashboard page provide the following insights. See
Now Assist Analytics dashboard indicator details for information on the data and calculations
behind each indicator.
•Search queries that yielded Knowledge Base articles and catalog items as Genius Result.
•Distribution of search queries by the source that they originated from, for example, Now Assist
in Virtual Agent, Service Portal.
•List of the most common queries that did or didn’t yield genius results.
User search analyzer indicators
Queries with Genius Results
This area of the dashboard total number of search queries that had a Genius Result
returned by Now Assist.
Note: A query can have more than one genius result.

<!-- page 85 -->
Queries with Genius Results indicator
Genius Result Engagement
This area of the dashboard shows the number of genius results returned by Now
Assist that covers the interactions like "Ask a follow up" or "Show full answer", and
clicking on citations within the result card.
Genius Result engagement indicator
Genius Result response time

<!-- page 86 -->
This area of the dashboard shows the average response time taken for a Genius
Result to load.
Genius Result response time indicator
Genius Result to chat handoff
This area of the dashboard shows the number of times users clicked the Ask a
follow-up button within the synthesized Genius Result.
Genius Result to chat handoff indicator
Genius Results citation engagement

<!-- page 87 -->
This area of the dashboard shows the number of interactions with citations within
Genius Result returned by Now Assist.
Genius Results citation engagement indicator
Feedback (Thumbs up)
This area of the dashboard shows the count for positive feedback for Genius Result
returned by Now Assist.
Feedback (Thumbs up) indicator
Feedback (Thumbs down)

<!-- page 88 -->
This area of the dashboard shows the count for negative feedback for Genius Result
returned by Now Assist.
Feedback (Thumbs down) indicator
Genius Results with Knowledge Base
This area of the dashboard shows the number of search queries where Now Assist
returned Knowledge Base articles as Genius Result for the users to review.
Genius Results with Knowledge Base indicator
Genius Results with Catalog Item
This area of the dashboard shows the number of search queries where Now Assist
returned catalog items as Genius Result for the users to review.

<!-- page 89 -->
Genius Results with Catalog Item indicator
Top 10 queries with Knowledge Base Genius Result
This area of the dashboard shows the top ten search queries where Now Assist
returned Knowledge Base as Genius Result, with respective query count.

<!-- page 90 -->
Top 10 queries with Knowledge Base Genius Result
Top 10 queries with Catalog Item Genius Result
This area of the dashboard shows the top ten search queries where Now Assist
returned catalog items as Genius Result, with respective query count.

<!-- page 91 -->
Top 10 queries with Catalog Item Genius Result indicator
Now Assist context menu analytics
Monitor the usage and performance of the Now Assist context menu.
The Now Assist context menu dashboard helps admins to evaluate the effectiveness of context
menu actions in assisting agents with summarizing, creating, and editing emails and chat replies.

<!-- page 92 -->
Now Assist context menu dashboard page
The indicators on the Now Assist context menu dashboard page provide the following
insights. See Now Assist Analytics dashboard indicator details for information on the data and
calculations behind each indicator.
•Count and distribution of context menu actions in a date range. This indicator reveals the scale
of usage, and the most and least used actions.
•Acceptance and feedback on context menu actions. This indicator reveals actions that were
accepted or rejected by the users with a positive or negative feedback.
•Usage trend chart reveals patterns in usage of context menu actions over a date range.
Now Assist context menu indicators
Usage in this period
This area of the dashboard shows the total number of Now Assist context menu
actions used in the selected date range.
Usage in this period indicator
Acceptance distribution

<!-- page 93 -->
This area of the dashboard shows the distribution of Now Assist context menu
actions by their acceptance.
•Accepted: The user has inserted the context menu response into their workspace.
•Not Accepted: The user has closed the window or dialog box containing the
context menu response.
Acceptance distribution indicator
Usage trend by skill
This area of the dashboard shows the usage trend of Now Assist context menu
actions in the selected date range.
Usage trend by skill indicator
Capability distribution
This area of the dashboard shows the usage distribution of various Now Assist
context menu actions in the selected date range.
Capability distribution indicator
Responses by feedback

<!-- page 94 -->
This area of the dashboard shows a breakdown of Now Assist context menu
responses by the user feedback received.
•Accepted: The user gave a thumbs up on the context menu response.
•Rejected: The user gave a thumbs down on the context menu response.
Responses by feedback indicator
Now Assist Analytics reference
Now Assist Analytics reference topics include information about user roles and details of the
indicators on the dashboard.
Now Assist Analytics roles
Now Assist Analytics requires the following roles to view and manage the dashboard
functionality.
Now Assist Analytics Viewer [sn_na_analytics.viewer]
Users with the Now Assist Analytics Viewer role can view the Now Assist Analytics dashboard in
the Now Assist Admin console, and have read access to data source tables.
Contains Roles
List of roles contained within the role.
None.
Groups
List of groups that this role is assigned to by default.
None.
Special considerations
None.
Now Assist Analytics Admin [sn_na_analytics.admin]
Users with Now Assist Analytics Admin role can view the Now Assist Analytics dashboard in the
Now Assist Admin console, and read and write to some data source tables.

<!-- page 95 -->
Contains Roles
List of roles contained within the role.
Now Assist Analytics Viewer [sn_na_analytics.viewer].
Groups
List of groups this role is assigned to by default.
None.
Special considerations
Avoid granting an admin role when more specialized roles are available.
Now Assist Analytics dashboard indicator details
Indicator details help you understand the data and calculations behind an indicator that is
presented in the form of a visualization on the dashboard.
Now Assist Analytics indicators contain the following details: indicator type, data source,
calculation, available breakdowns, unit, and so on.
To access these indicators, navigate to Platform Analytics Administration > Indicators.
You must have the Now Assist Analytics Admin [sn_na_analytics_admin] role to access the
indicators.
These indicators collect data at a daily frequency. Data is only available for dates before the
current date. If you want to see results from the current day, you must wait until the next day.
Note: The Generative AI Usage Log [sys_gen_ai_usage_log] table is maint-only.
Usage and adoption indicator details
Indicator Available
Visualization Indicator source table Calculation Frequency Unit Precision
type breakdowns
Total AutomatedGenerative AI Usage Count By Daily 0
Now Log[sys_gen_ai_usageo_fl oagll ] Gen AI
Assist actions Feature,
actions By
Generative
AI Skill
Execution
Modality,
By Skill
Family,
By Skills
Config,
By Skills
Config,
By
Workflow
Daily AutomatedGenerative AI Usage Count By Daily 0
Now Log[sys_gen_ai_usageo_fl odga]ily Gen AI
Assist actions Feature,
actions By

<!-- page 96 -->
Indicator Available
Visualization Indicator source table Calculation Frequency Unit Precision
type breakdowns
Generative
AI Skill
Execution
Modality,
By Skill
Family,
By Skills
Config,
By Skills
Config,
By
Workflow
Average AutomatedGenerative AI Usage Average By Daily 0
daily Log[sys_gen_ai_usageo_fl odga]ily Gen AI
unique unique Feature,
users users By Skills
engaging Config,
with Now By Skill
Assist Family,
By
Generative
AI Skill
Execution
Modality
Daily AutomatedGenerative AI Usage Count By Daily 0
unique Log[sys_gen_ai_usageo_fl odga]ily Gen AI
users unique Feature,
engaging users By Skills
with Now Config,
Assist By Skill
Family,
By
Generative
AI Skill
Execution
Modality
Skill AutomatedGenerative AI Usage Count By Daily 0
group Log[sys_gen_ai_usageo_fl odga]ily Gen AI
distribution skill Feature,
executionBs y
grouped Generative
By AI Skill
Gen AI Execution
Feature, Modality,
By By Skill
GenerativFea mily,
AI Skill By Skills
ExecutionC onfig,
Modality, By Skills
By Skill Config,
Family, By
By Workflow

<!-- page 97 -->
Indicator Available
Visualization Indicator source table Calculation Frequency Unit Precision
type breakdowns
Skills
Config,
By
Skills
Config
Daily AutomatedGenerative AI Usage Count By Daily 0
usage Log[sys_gen_ai_usageo_fl og] Gen AI
comparison actions Feature,
by grouped By
workflow by Generative
workflowsAI Skill
Execution
Modality,
By Skill
Family,
By Skills
Config,
By Skills
Config,
By
Workflow
Skill AutomatedGenerative AI Usage Count By Daily 0
engagement Log[sys_gen_ai_usageo_fl og] Gen AI
trend actions Feature,
grouped By
by skill Generative
AI Skill
Execution
Modality,
By Skill
Family,
By Skills
Config,
By Skills
Config,
By
Workflow
DepartmenAtsu tomatedGenerative AI Usage Count By Daily 0
with Log[sys_gen_ai_usageo_fl og] Department,
highest actions By Skills
usage grouped Config
by user
department
and
sorted
by
descending
order
Now AutomatedGenerative AI Usage Count By Daily 0
Assist Log[sys_gen_ai_usageo_fl og] Department,
actions actions By Skills
comparison grouped Config

<!-- page 98 -->
Indicator Available
Visualization Indicator source table Calculation Frequency Unit Precision
type breakdowns
by user by user
department department
Feedback AutomatedGen AI Log Count By Skill Daily 0
details Metadata[sys_gen_ai_olof g_metaFdaamtai]ly,
actions By Skills
grouped Config
by Skill
Family
AutomatedGen AI Log Count By Daily 0
Metadata[sys_gen_ai_olof g_metaFdeaetad]back,
actions By Skill
with Family,
feedback By Skills
grouped Config
by Skill
Family
Formula Gen AI Log (Count By Skill Daily % 2
Metadata[sys_gen_ai_olof g_metaFdaamtai]ly,
actions By Skills
with Config
feedback/
Total
count of
actions)
x 100
grouped
by Skill
Family
AutomatedGen AI Log Count By Skill Daily 0
Metadata[sys_gen_ai_olof g_metaFdaamtai]ly,
actions By Skills
where Config,
By By
FeedbackF eedback
is
Accepted
grouped
by Skill
Family
Formula Gen AI Log (Count By Skills Daily % 2
Metadata[sys_gen_ai_olof g_metaCdaotnafi]g,
actions By Skill
where Family
By
Feedback
is
Accepted/
Total
count of
actions
with

<!-- page 99 -->
Indicator Available
Visualization Indicator source table Calculation Frequency Unit Precision
type breakdowns
feedback)
x 100
grouped
by Skill
Family
Error AutomatedGen AI Log Count By Skill Daily 0
details Metadata[sys_gen_ai_olof g_metaFdaamtai]ly,
actions By Skills
grouped Config
by Skill
Family
AutomatedGen AI Log Count By Gen Daily 0
Metadata[sys_gen_ai_olof g_metaAdIa Ltao]g
actions Metadata
with Status ,
error By Skill
status Family,
grouped By Skills
by Skill Config
Family
Formula Gen AI Log (Count By Skill Daily % 2
Metadata[sys_gen_ai_olof g_metaFdaamtai]ly,
actions By Skills
with Config
error
status/
Total
count of
generative
AI
metadata
records)
x 100
grouped
by Skill
Family
Skill performance indicator details
Indicator
Indicator Available
Visualization source Calculation Frequency Unit Precision
type breakdowns
table
Skill Automated Generative Count By Gen AI Daily 0
engagement AI Usage of skill Feature,
trend Log[sys_gene_xaei_cuustiaognes_ lBoyg ]
grouped Generative
by skill AI Skill
Execution
Modality,
By Skill

<!-- page 100 -->
Indicator
Indicator Available
Visualization source Calculation Frequency Unit Precision
type breakdowns
table
Family,
By Skills
Config, By
Workflow
Number of Automated Generative Count of By Gen AI Daily 0
actions AI Usage all skill Feature,
Log[sys_gene_xaei_cuustiaognes_lBoyg ]
Generative
AI Skill
Execution
Modality,
By Skill
Family,
By Skills
Config, By
Workflow
Total daily Automated Generative Count By Gen AI Daily 0
active AI Usage of daily Feature,
users Log[sys_genu_naiiq_uuesa ge_lBoyg ]Skills
users Config,
By Skill
Family, By
Generative
AI Skill
Execution
Modality
Total daily Automated Generative Count By Gen AI Daily 0
active AI Usage of daily Feature,
users by Log[sys_genu_naiiq_uuesa ge_lBoyg ]Skills
skills users Config,
grouped By Skill
by Skills Family, By
Config Generative
AI Skill
Execution
Modality
Skill details indicator details
Indicator
Indicator Available
Visualization source Calculation Frequency Unit Precision
type breakdowns
table
Skill Automated Generative Count By Gen AI Daily 0
engagement AI Usage of skill Feature,
trend Log[sys_gene_xaei_cuustiaognes_ lBoyg ]
grouped Generative
by Skills AI Skill
Config Execution
Modality,

<!-- page 101 -->
Indicator
Indicator Available
Visualization source Calculation Frequency Unit Precision
type breakdowns
table
By Skill
Family,
By Skills
Config, By
Workflow
Total skill Automated Generative Count By Gen AI Daily 0
actions AI Usage of skill Feature,
Log[sys_gene_xaei_cuustiaognes_lBoyg ]
Generative
AI Skill
Execution
Modality,
By Skill
Family,
By Skills
Config, By
Workflow
Accepted Automated Gen Count By Daily 0
skill AI Log of skill Feedback,
actions Metadata[syesx_egceunt_ioani_sl oBgy_ metadata]
where response
Feedback accepted
is without
Accepted edits,
By Skills
Config,
By Skill
Family
AcceptanceF ormula Gen (Count By Skills Daily % 0
rate AI Log of skill Config
Metadata[syesx_egceunt_ioani_sl og_metadata]
where
Feedback
is
Accepted/
Count
of skill
executions)x100
Daily Automated Generative Count By Gen AI Daily 0
active AI Usage of daily Feature,
users Log[sys_genu_naiiq_uuesa ge_lBoyg ]Skills
users Config,
By Skill
Family, By
Generative
AI Skill
Execution
Modality

<!-- page 102 -->
Custom skills indicator details
Indicator
Indicator Available
Visualization source Calculation Frequency Unit Precision
type breakdowns
table
Skill Automated Generative Count of By Daily 0
engagement AI Usage custom Custom
trend by Log[sys_gens_kailil_ usage_lSokgi]ll
workflows executions (Workflow
grouped Type), By
by Custom
workflows Skill
(Feature
Type), By
Custom
Skill
(Product
Type), By
Custom
Skill
Completion
Status,
By Skills
Config
Skill Automated Generative Count of By Daily 0
engagement AI Usage custom Custom
trend by Log[sys_gens_kailil_ usage_lSokgi]ll
products executions (Workflow
grouped Type), By
by Custom
products Skill
(Feature
Type), By
Custom
Skill
(Product
Type), By
Custom
Skill
Completion
Status,
By Skills
Config
Skill Automated Generative Count of By Daily 0
engagement AI Usage custom Custom
trend by Log[sys_gens_kailil_ usage_lSokgi]ll
features executions (Workflow
grouped Type), By
by Custom
features Skill
(Feature
Type), By
Custom
Skill

<!-- page 103 -->
Indicator
Indicator Available
Visualization source Calculation Frequency Unit Precision
type breakdowns
table
(Product
Type), By
Custom
Skill
Completion
Status,
By Skills
Config
Daily Automated Generative Count of By Skills Daily 0
unique AI Usage unique Config
users Log[sys_genu_saei_rsu swahgoe _log]
engaging executed
with the custom
skill skills
Executed Formula Generative (Count of By Skills Daily % 2
successfully AI Usage custom Config
Log[sys_gens_kailil_ usage_log]
executions
with
status
Completed/
Count of
custom
skill
executions)x100
Skills Automated Generative Count By Daily 0
feedback AI Usage Feedback,
Log[sys_gen_ai_usage_lBoyg ]Skills
Config
Now Assist Guardian offensive content guardrail indicator details
Indicator
Indicator Available
Visualization source Calculation Frequency Unit Precision
type breakdowns
table
Guardrail- Automated Generative Average By Skills Daily Milliseconds0
added AI time taken Config
latency Metric[sys_gbeyn tehrea tive_ai_metric]
guardrail
to
evaluate
offensive
content
Percentage Formula Generative (Count of By Skills Daily % 0
flagged as AI offensive Config
offensive Metric[sys_gceonneteranttiv e_ai_metric]
occurrences/
Total
number

<!-- page 104 -->
Indicator
Indicator Available
Visualization source Calculation Frequency Unit Precision
type breakdowns
table
of LLM
calls for
which the
guardrail
was
enabled)x100
Total Automated Generative Count of By Gen Daily 0
offensive AI offensive AI metric
content Metric[sys_gceonneteranttiv e_avi_amlueet,r ic]
occurrences occurrencesBy Skills
Config
Categories Automated Generative Count of By Daily 0
of AI offensive Offensiveness
offensive Metric[sys_gceonneteranttiv e_aTi_ympee,t ric]
content occurrencesB y Skills
grouped Config
by
categories
Offensive Automated Generative Count of By Gen Daily 0
content AI offensive AI metric
occurrences Metric[sys_gceonneteranttiv e_avi_amlueet,r ic]
by skill occurrencesB y Skills
grouped Config
by skill
Now Assist Guardian prompt injection guardrail indicator details
Indicator
Indicator Available
Visualization source Calculation Frequency Unit Precision
type breakdowns
table
Guardrail- Automated Generative Average By Skills Daily Milliseconds0
added AI time taken Config
latency Metric[sys_gbeyn tehrea tive_ai_metric]
guardrail
to
evaluate
prompt
injection
Percentage Formula Generative (Count of By Skills Daily % 0
flagged AI prompt Config
as prompt Metric[sys_ginejneecrtaiotinv e_ai_metric]
injection occurrences/
Total
number
of LLM
calls for
which the
guardrail

<!-- page 105 -->
Indicator
Indicator Available
Visualization source Calculation Frequency Unit Precision
type breakdowns
table
was
enabled)x100
Total Automated Generative Count of By Gen Daily 0
prompt AI prompt AI metric
injection Metric[sys_ginejneecrtaiotinv e_avi_amlueet,r ic]
occurrences occurrencesBy Skills
Config
Prompt Automated Generative Count of By Gen Daily 0
injection AI prompt AI metric
occurrences Metric[sys_ginejneecrtaiotinv e_avi_amlueet,r ic]
by skill occurrencesB y Skills
grouped Config
by skill
User search analyzer indicator details
Indicator
Indicator Available
Visualization source Calculation Frequency Unit Precision
type breakdowns
table
Queries Automated Search Count of AIS Daily 0
with Event[sys_sesaeracrhc_he vent]Search
Genius queries Application
Results where
Genius
Result
Displayed
= true
Genius Automated Genius Count of AIS Daily 0
Result Result genius Search
engagement Event results Application
Action[sys_swehaercrhe _genius_result_event_action]
Card Type
= Now
Assist
Multi-
Content
Response
and
Action
Type =
Show Full
Answer
or Action
Type =
Ask a
Follow Up
or Action
Type =
uxf_client_action

<!-- page 106 -->
Indicator
Indicator Available
Visualization source Calculation Frequency Unit Precision
type breakdowns
table
Genius Automated Search Average AIS Daily Seconds 0
Result Signal (Genius Search
response Event[sys_seRaerscuhl_t signalA_pevpelincta]tion
time Response
Time in
Seconds)
Genius Automated Genius Count of AIS Daily 0
Result Result queries Search
to chat Event where Application
handoff Action[sys_sCeaarrdch T_ygpeen ius_result_event_action]
= Now
Assist
Multi-
Content
Response
and
Action
Type =
Ask a
Follow Up
Genius Automated Genius Count of AIS Daily 0
Results Result queries Search
citation Event where Application
engagement Action[sys_sCeaarrdch T_ygpeen ius_result_event_action]
= Now
Assist
Multi-
Content
Response
and
Action
Type =
uxf_client_action
Feedback Automated Genius Count of AIS Daily 0
(Thumbs Result queries Search
up) Event where Application
Action[sys_sCeaarrdch T_ygpeen ius_result_event_action]
= Now
Assist
Multi-
Content
Response
and
Action
Type =
Feedback
and
Action
Value =
Helpful

<!-- page 107 -->
Indicator
Indicator Available
Visualization source Calculation Frequency Unit Precision
type breakdowns
table
Feedback Automated Genius Count of AIS Daily 0
(Thumbs Result queries Search
down) Event where Application
Action[sys_sCeaarrdch T_ygpeen ius_result_event_action]
= Now
Assist
Multi-
Content
Response
and
Action
Type =
Feedback
and
Action
Value
= Not
Helpful
Genius Automated Search Count of AIS Daily 0
Results Signal queries Search
with KB Genius where Application
Result Source
Triggered Table =
Event[sys_sekabr_ckhn_oswiglnedalg_egenius_result_triggered_event]
Genius Automated Search Count of AIS Daily 0
Results Signal queries Search
with Genius where Application
Catalog Result Source
Item Triggered Table =
Event[sys_sesacr_ccha_t_siitgenmal_genius_result_triggered_event]
Top 10 Automated Search Top 10 Not Daily Not Not
queries Signal queries Applicable Applicable Applicable
with KB Genius with count
Genius Result of genius
Result Triggered results
Event where
[sys_search_Ssoigunrcael_ genius_result_triggered_event]
Table =
kb_knowledge
Top 10 Automated Search Top 10 Not Daily Not Not
queries Signal queries Applicable Applicable Applicable
with Genius with count
Catalog Result of genius
Item Triggered results
Genius Event where
Result [sys_search_Ssoigunrcael_ genius_result_triggered_event]
Table =
sc_cat_item

<!-- page 108 -->
Now Assist context menu analytics indicator details
Indicator
Indicator Available
Visualization source Calculation Frequency Unit Precision
type breakdowns
table
Usage Automated Generative Count of By NAcm Daily 0
in this AI actions implicit
period Log[sys_genwehraetrieve _ai_lofege]dback,
Source By Skills
is Now Config, By
Assist Feedback,
context By Status,
menu By Skill
Capability
AcceptanceA utomated Generative Count of By NAcm Daily 0
distribution AI actions implicit
Log[sys_genwehraetrieve _ai_lofege]dback,
content By Skills
generated Config, By
by Now Feedback,
Assist By Status,
context By Skill
menu Capability
grouped
by
Accepted
or Not
Accepted
Usage Automated Generative Count of By NAcm Daily 0
trend by AI context implicit
skill Log[sys_genmereantiuv e_ai_lofege]dback,
actions By Skills
grouped Config, By
by Now Feedback,
Assist By Status,
skills By Skill
Capability
Capability Automated Generative Count of By NAcm Daily 0
distribution AI context implicit
Log[sys_genmereantiuv e_ai_lofege]dback,
actions By Skills
grouped Config, By
by Feedback,
capability By Status,
By Skill
Capability
Responses Automated Generative Count of By NAcm Daily 0
by AI actions implicit
feedback Log[sys_genwehraetrieve _ai_lofege]dback,
feedback By Skills
for the Config, By
content Feedback,
generated By Status,

> **[Screenshot: Now Assist Admin console plugin installation page]**
> The "Install product plugins" page showing three workflow category cards in a horizontal row: Technology (stylised people/chart icon, "Use Now Assist to elevate day-to-day operations and increase employee agility", "Browse plugins" button), Customer (stylised person icon, "Use Now Assist to improve customer experiences and deepen brand loyalty", "Browse plugins" button), Employee (stylised person icon, "Use Now Assist to boost employee engagement and strengthen morale", "Browse plugins" button). Background is white.
>
> **[Screenshot: Now Assist Analytics Configuration table]**
> ServiceNow list view of the "Now Assist Analytics Configurations [sn_na_analytics_configuration]" table. Table columns: Active, Dashboard, Document Id, Document Table, Order, Domain. Two visible rows: Row 1 – Active: true, Dashboard: Flow Generation, Document Id: Generative AI Feature Mapping: Flow Generation, Document Table: Generative AI Feature Mapping [sys_gen_ai_feature_mapping], Order: 100, Domain: global. Row 2 – Active: true, Dashboard: Case summarization, Document Id: Generative AI Feature Mapping: Case summarization, same Document Table, Order: 100, Domain: global.

> **[Screenshot: Usage and adoption dashboard page in Now Assist Analytics]**
> Full-width screenshot of the Now Assist Analytics "Usage and Adoption" dashboard. Left sidebar navigation shows: Usage and Adoption (selected, expanded showing Usage Summary and Adoption sub-items), Self-Service Performance, Skill Performance, Now Assist Guardian, User Search Analyser, Now Assist Context Menu, Value Insights. Main area shows "Usage Summary" and "Adoption" tabs (Usage Summary active). Filter bar: Date "2025-02-0…", Channels "Select", Products "Select".
>
> Four KPI/chart widgets in a 2×2 grid: Top-left: "Total Now Assist actions" showing "3232" in large bold text with upward trend indicator "↑ 3228 (90700.0%) since previous period Jan 7 – Jan 31", line chart below showing spike around Feb 10–13, label "Sum for Feb 1 – Feb 25". Top-right: "Daily Now Assist actions" line chart with y-axis up to 4000 counts, x-axis labels Feb 1 through Feb 25, single large spike visible around Feb 10. Bottom-left: "Average daily unique users engaging with Now Assist" showing "828" in large bold text, "↑ 28 (23033.3%) since previous period", line chart with matching spike pattern, label "Avg for Feb 1 – Feb 25". Bottom-right: "Daily unique users engaging with Now Assist" line chart, same time axis, spike visible.

> **[Screenshot: Total Now Assist actions indicator – close-up]**
> A single KPI widget titled "Total Now Assist actions" showing the count "3225" in very large bold teal/black text with a cursor icon alongside it. Below: "↑ 3225 since previous period Dec 22, 2024 – Jan 20". A small line chart below shows a flat baseline then a sharp upward spike. Footer: "Sum for Jan 21 – Feb 19."
>
> **[Screenshot: Daily Now Assist actions indicator – line chart]**
> Line chart titled "Daily Now Assist actions" with y-axis labelled "Actions" ranging 0–3000 (gridlines at 1000, 2000, 3000). X-axis shows dates from Jan 21 through Feb 20 with labels Jan 21, Jan 24, Jan 27, Jan 30, Feb 2, Feb 5, Feb 8, Feb 11, Feb 14, Feb 17, Feb 20. A single sharp teal spike rises to approximately 3000 around Feb 11, with a smaller secondary spike the following day. Rest of the chart is flat near zero. Legend below reads "Gen AI Actions per day."
