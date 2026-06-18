# Exploring Generative AI Controller

_Source pages: 186–188 | Depth: 2_

---

<!-- page 186 -->
Explore Configure
Explore Generative AI Configure Generative AI
concepts and terminology. Controller provider capabilities.
Reference
Reference for Generative AI Controller.
Troubleshoot and get help
•ServiceNow Community
•Search the Known Error Portal for known error articles
•Contact Customer Service and Support
AI limitations
This application uses artificial intelligence (AI) and machine learning, which are rapidly evolving fields of study that generate predictions based on patterns
in data. As a result, this application may not always produce accurate, complete, or appropriate information. Furthermore, there is no guarantee that this
application has been fully trained or tested for your use case. To mitigate these issues, it is your responsibility to test and evaluate your use of this application for
accuracy, harm, and appropriateness for your use case, employ human oversight of output, and refrain from relying solely on AI-generated outputs for decision-
making purposes. This is especially important if you choose to deploy this application in areas with consequential impacts such as healthcare, finance, legal,
employment, security, or infrastructure. You agree to abide by ServiceNow’s AI Acceptable Use Policy , which may be updated by ServiceNow.
Data processing
This application requires data to be transferred from ServiceNow customers' individual instances to a centralized ServiceNow environment, which may be located
in a different data center region from the one where your instance is, and potentially to a third-party cloud provider, such as Microsoft Azure. This data is handled
per ServiceNow's internal policies and procedures, including our policies available through our CORE Compliance Portal .
Data collection
ServiceNow collects and uses the inputs, outputs, and edits to outputs of this application to develop and improve ServiceNow technologies including ServiceNow
models and AI products. Customers can opt out of future data collection at any time, as described in the Now Assist Opt-Out page.
Exploring Generative AI Controller
Learn more about generative AI concepts and how to integrate third-party generative AI into the
ServiceNow AI Platform to create content, summarize task records, and analyze user sentiment.

<!-- page 187 -->
Generative AI Controller overview
Complex algorithms and deep learning models learn patterns and use that knowledge to
generate new outputs. With Generative AI Controller, you can generate content directly within
the ServiceNow AI Platform.
Generative AI Controller integrates with external LLMs, including ones by OpenAI, Azure OpenAI,
Google Cloud (AI Studio and Vertex), Aleph Alpha, IBM watsonx, and Amazon Bedrock. These
capabilities are available in Workflow Studio flows, Virtual Agent topics, and scripting like
background scripts and business rules.
Generative AI Controller benefits
Benefit Feature
Integrate with third-party AI service providers to customize OpenAI, Azure OpenAI,
your AI experience Google AI, IBM watsonx and
Amazon Bedrock.
Get started with Generative AI Controller
•The Generative AI Controller application is installed with any Now Assist application.
•Sign up and create an account with a generative AI provider.
◦To sign up with OpenAI, go to their official platform website .
◦To get started with Azure OpenAI, go to their documentation .
◦To start using AI Studio with Gemini API, go to the AI Studio homepage .
◦To use Vertex AI on the Google Cloud, go to the Vertex AI homepage .
◦To get started with Aleph Alpha, go to their website and create an Aleph Alpha API account.
◦To get started with IBM watsonx, go to Getting started with IBM watsonx as a Service .
◦To get started with Amazon Bedrock, set up an IAM user with the correct permissions and
then explore the Converse API .
•Configure credentials for your preferred AI service provider for the Generative AI Controller
capabilities.
Domain separation and Generative AI Controller
Domain separation is supported for Generative AI Controller. Domain separation enables you to
separate data, processes, and administrative tasks into logical groupings called domains. You
can control several aspects of this separation, including which users can see and access data.
Support level: Standard
•Includes all aspects of Basic level support.
•Application properties are domain-aware as needed.
•Business logic: The service provider (SP) creates or modifies processes per customer. The use
cases reflect proper use of the application by multiple SP customers in a single instance.
•The instance owner must configure the minimum viable product (MVP) business logic and data
parameters per tenant as expected for the specific application.

<!-- page 188 -->
Sample use case: An Admin must be able to make comments required when a record closes for
one tenant, but not for another.
For more information on support levels, see Application support for domain separation .
Domain separation enables you to create partitions in the application data and administrative
processes. Because the generative AI tables are domain separated, Generative AI Controller
supports domain separation for OneExtend capabilities. The capabilities are the basic building
blocks for Virtual Agent Designer topics, components, flows, and scripts that use generative AI.
With domain separation, you can isolate the data and control access so that users in one domain
don’t have access to the capabilities of another domain.
For more details on domain separation and Virtual Agent, check out the documentation .
How domain separation works in Generative AI Controller
Domain separation is possible at the generative AI OneExtend capability level. Records that are
related to the execution and configuration of OneExtend capabilities, such as log tables that are
accessible to ServiceNow personnel, are also separated according to the capability's domain.
If you want to create a copy of an existing generative AI capability in a different domain, you
must create a record in the OneExtend Capabilities (sys_one_extend_capability) table. See the
reference for Generative AI Controller for more information about the OneExtend Capabilities
table.
You set the domain when the record is created. The domain is based on the domain that you're
in at the time that you create the record. When you're creating a capability record, you can use an
existing OneExtend Capability record as a blueprint to help confirm that the capability works as
intended.
After you create the OneExtend Capability record, you must create records for the following
attribute and config records in the new domain:
•OneExtend Capability Attribute records with the same values as the capability in the global
domain.
•A OneExtend Capability Definition that corresponds to the new capability.
•A OneExtend Definition Config definition record that includes the OneExtend Capability
Definition for the new domain.
You can also create these records by using the related lists in the OneExtend Capability record
default view.
Note: The OneExtend Capability Definition record that you add must be the same as
the capability that you want in the new domain. For example, if you’re creating a capability
in a new domain for sentiment analysis, you could add the Sentiment Analysis (OpenAI
Completion) record. Adding the Summarize (OpenAI Completion) Config could result in
unexpected behavior. The OneExtend Definition Config record that you select should
include the OneExtend Capability Definition record that you added.
Use cases
With domain-separated capabilities, you can build different Virtual Agent topics, flows with
Workflow Studio, or different background and business rule scripts that are also domain
separated.
Related topics
Domain separation for service providers