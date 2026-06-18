### Call a custom skill from a script

*Pages 41–42 of the source PDF*

Make any necessary changes to the prompt. 3.

4.If you have changed the prompt, test it.

5. When you're satisfied with your prompt, select Finalize prompt.

6.Select Publish.

What to do next A Now Assist admin must activate the skill. To learn more about how to activate a skill, see Activate a skill.

Activate a skill

After you create and publish a custom skill, you must activate it in Now Assist Admin. Activating the skill enables you to trigger the skill within the UI.

Before you begin Role required: admin

Procedure

1.Navigate to All > Now Assist Admin > Features.

Find the custom skill that you created. 2.

Select skill. 3. Activate Make sure you are in the correct application scope when you activate the skill. To learn more about application scopes, see Application scope .

Note: Some skills might need to be reviewed and approved by a data steward before you can activate it.

What to do next You can enable Now Assist Guardian for your skills. To learn more about Now Assist Guardian, see Now Assist Guardian

Call a custom skill from a script

You can use a script to call a custom skill.

Before you begin Role required: admin

Procedure

1.Navigate to > > Actions. All System UI UI

2. Create a UI action. For more information on creating UI actions, see Create a UI action .

Add your script. 3.

The following script is an example. You can replace the variables with your data.

| var inputsPayload = {}; |
| --- |
|  |
| // create the payload to deliver input data to the skill |
|  |
| inputsPayload[‘input name’] = { |
|  |
| tableName: 'table name', |
|  |
| sysId: 'sys_id', |
|  |
| queryString: '' |
|  |
| }; |
|  |
| //create the request by combining the capability sys ID and the skill config sys ID |
|  |
| var request = { |
|  |
| executionRequests: [{ |
|  |
| payload: inputsPayload, |
|  |
| capabilityId: ‘capability sys id’, |
|  |
| meta: { |
|  |
| skillConfigId: ‘skill config sys id’ |
|  |
| } |
|  |
| }], |
|  |
| mode: 'sync' |
|  |
| }; |
|  |
| //run the custom skill and get the output in a string format |
| try { |
| var output = sn_one_extend.OneExtendUtil.execute(request)['capabilities'][r equest.executionRequests[0].capabilityId]['response']; |
| var LLMOutput = JSON.parse(output).model_output; |
| } catch(e) { |
| gs.error(e); |
