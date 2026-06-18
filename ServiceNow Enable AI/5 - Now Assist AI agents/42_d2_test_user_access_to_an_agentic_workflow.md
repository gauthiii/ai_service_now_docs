# Test user access to an agentic workflow

_Source pages: 135–136 | Depth: 2_

---

<!-- page 135 -->
Note: If you don't have the roles necessary to pass the ACLs of the agentic workflow and
all of its AI agents and tools, you're notified that you don't have the necessary access and
the test won't execute.
Your AI agents start to execute the test autonomously to resolve the agentic workflow by taking
the input from the live agent as required.
Testing an agentic workflow
•A simulated chat experience begins on the Now Assist panel between your invoking user and
AI agent.
•At the top of the canvas, you can see information about the agentic workflow you're testing,
including its name, version, and description.
•A diagram shows the tasks and communication of the AI agents that are working together to
solve the case.
•A decision log records the thought process of each AI agent that is involved in solving the
agentic workflow.
Note: You can view the entire decision log by selecting Download logs.
You can restart the entire testing process at any time by selecting Restart.
Test user access to an agentic workflow
Run a manual test to verify that only the users you want to access the agentic workflow can do so.
Before you begin
Role required: sn_aia_admin and either admin or at least one role required by the ACL of the
agentic workflow being testing and each of the ACLs of its downstream components
About this task
You can establish the security settings for an agentic workflow in the guided setup to establish
which users can access it. See Define security controls for instructions on how to change the
user access settings. When you select Save and continue on that step of the guided setup, an
ACL is created that establishes limitations on which users can access the agentic workflow.
Once you have created these ACLs, you can verify that they work as intended by using the Test
access test type of a manual test of an agentic workflow.

<!-- page 136 -->
To see instructions for performing manual tests to evaluate performance, see Test performance
manually. For more information about automated tests, see Evaluate an agentic workflow.
Procedure
1.Navigate to All > AI Agent Studio > Testing.
2. Select Start manual test.
3. In the Test typeChoose a test type drop down, select Test access.
If you want to test the basics of how an agentic workflow works, select AI agent or
worfklow. The full instructions for that test type can be found in Test performance manually.
4.Search for or select the name of the agentic workflow you want to test.
5. Select an invoking user.
The invoking user can be the user that triggers the agentic workflow or it can be the invoking
user of an upstream component, such as an agentic workflow. For more information about how
the invoking user works, see Security for AI agents.
When you select an invoking user, the user roles are populated in the Invoking user
roles field. The field is read-only. If you want to change a user's roles, you must change the
user's User record. See Assign a role to a user .
6.Select Test access.
Result
The results of the access test are opened in the Access Analyzer in a new browser tab.
Access Analyzer identifies all the ACL calls made in the execution of the agentic workflow,
including its AI agents and tools, if any are present. You can see the results of each ACL to verify
that each one has the correct user access defined.
What to do next
If the results are different than what you expect or want, you can redefine the security controls of
the agentic workflow.
You can also test an agentic workflow's performance with either a manual test or automated
evaluations. See Test performance manually or Evaluate an agentic workflow.