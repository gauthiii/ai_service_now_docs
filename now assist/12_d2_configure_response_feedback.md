# Configure response feedback

_Source pages: 155–155 | Depth: 2_

---

<!-- page 155 -->
Property Possible values Default value Definition
directly to all
queries without
asking follow-up
questions.
◦low - clarification is
triggered for highly
ambiguous queries.
◦high - clarification
is triggered more
frequently, covering
a broader range of
ambiguous queries.
4.To view the disambiguation data, in the filter navigator field, enter
sys_generative_ai_log.
Configure response feedback
Configure the response feedback options that appear when users select thumbs up or thumbs
down on a Now Assist in Virtual Agent or Now Assist panel response.
Before you begin
Role required: admin
Procedure
1.In the filter navigator field, enter
sys_now_assist_deployment_config_attributes.list to display the Now
Assist Deployment Config Attributes table.
2. In the selection fields, select Name from the drop-down list and enter granular in the
Search field.
3. If you want to change whether negative granular feedback is enabled for Now Assist in Virtual
Agent, select is_negative_granular_feedback_enabled that has Now Assist in Virtual Agent
(default) as the Deployment Configuration.
4.On the next screen, change the value to true if you want negative granular feedback to be
enabled or to false if you do not want negative granular feedback to be enabled.
5. Select Submit.
6.If you want to change whether positive granular feedback is enabled for Now Assist in Virtual
Agent, select is_positive_granular_feedback_enabled that has Now Assist in Virtual Agent
(default) as the Deployment Configuration.
7.On the next screen, change the value to true if you want positive granular feedback to be
enabled or to false if you do not want positive granular feedback to be enabled.
8.Select Submit.
9.To configure the feedback options, in the filter navigator field, enter
sys_now_assist_message_bundle.list to display the Now Assist Message Bundles
table.
10.In the selection fields, select for text from the drop-down list and enter granular in the
Search field.
11. Do one of the following: