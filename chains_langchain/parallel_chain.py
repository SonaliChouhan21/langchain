from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnableParallel

load_dotenv()


model1 = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash")

model2 = ChatOllama(
    model="llama3.2"
)

prompt1=PromptTemplate(
    template='Generate short amd simple notes from the following text \n {text}',
    input_variable=['text']
)

prompt2=PromptTemplate(
    template='Generate 5 short question and answers from the following text \n {text}',
    input_variable=['text'])

prompt3=PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n  notes ->{notes} and quiz -> {quiz}',

    input_variable=['notes','quiz'])

parser =StrOutputParser()

parallel_chain = RunnableParallel({
    'notes':prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser}
)

merge_chain = prompt3 | model2 | parser

chain= parallel_chain | merge_chain

text="""Cloud computing service models are based on the concept of sharing on-demand computing resources, software, and information over the internet. Companies or individuals pay to access a virtual pool of shared resources, including compute, storage, and networking services, which are located on remote servers that are owned and managed by service providers. 

One of the many advantages of cloud computing is that you only pay for what you use. This allows organizations to scale faster and more efficiently without the burden of having to buy and maintain their own physical data centers and servers.  

In simpler terms, cloud computing uses a network (most often, the internet) to connect users to a cloud platform where they request and access rented computing services. A central server handles all the communication between client devices and servers to facilitate the exchange of data. Security and privacy features are common components to keep this information secure and safe.  

When adopting cloud computing architecture, there is no one-size-fits-all. What works for another company may not suit you and your business needs. In fact, this flexibility and versatility is one of the hallmarks of cloud, allowing enterprises to quickly adapt to changing markets or metrics.

There are three different cloud computing deployment models: public cloud, private cloud, and hybrid cloud.

Types of cloud computing deployment models
Public cloud
Public clouds are run by third-party cloud service providers. They offer compute, storage, and network resources over the internet, enabling companies to access shared on-demand resources based on their unique requirements and business goals.

Private cloud
Private clouds are built, managed, and owned by a single organization and privately hosted in their own data centers, commonly known as “on-premises” or “on-prem.” They provide greater control, security, and management of data while still enabling internal users to benefit from a shared pool of compute, storage, and network resources.

Hybrid cloud
Hybrid clouds combine public and private cloud models, allowing companies to leverage public cloud services and maintain the security and compliance capabilities commonly found in private cloud architectures.

What are the types of cloud computing services?
There are three main types of cloud computing service models that you can select based on the level of control, flexibility, and management your business needs: 

Infrastructure as a service (IaaS)
Infrastructure as a service (IaaS) offers on-demand access to IT infrastructure services, including compute, storage, networking, and virtualization. It provides the highest level of control over your IT resources and most closely resembles traditional on-premises IT resources.

Platform as a service (PaaS)
Platform as a service (PaaS) offers all the hardware and software resources needed for cloud application development. With PaaS, companies can focus fully on application development without the burden of managing and maintaining the underlying infrastructure.

Software as a service (SaaS)
Software as a service (SaaS) delivers a full application stack as a service, from underlying infrastructure to maintenance and updates to the app software itself. A SaaS solution is often an end-user application, where both the service and the infrastructure is managed and maintained by the cloud service provider.

What are the benefits of cloud computing?
It’s flexible

Due to the architecture of cloud computing, enterprises and their users can access cloud services from anywhere with an internet connection, scaling services up or down as needed.

It’s efficient

Enterprises can develop new applications and rapidly get them into production—without worrying about the underlying infrastructure.

It offers strategic value

Because cloud providers stay on top of the latest innovations and offer them as services to customers, enterprises can get more competitive advantages—and a higher return on investment—than if they’d invested in soon-to-be obsolete technologies.

It’s secure

Enterprises often ask, What are the security risks of cloud computing? They are considered relatively low. Cloud computing security is generally recognized as stronger than that in enterprise data centers, because of the depth and breadth of the security mechanisms cloud providers put into place. Plus, cloud providers’ security teams are known as top experts in the field.

It’s cost-effective

Whatever cloud computing service model is used, enterprises only pay for the computing resources they use. They don’t need to overbuild data center capacity to handle unexpected spikes in demand or business growth, and they can deploy IT staff to work on more strategic initiatives.

Solve your business challenges with Google Cloud
New customers get $300 in free credits to spend on Google Cloud.
Talk to a Google Cloud sales specialist to discuss your unique challenge in more detail.
How cloud computing can help your organization
The pace of innovation—and the need for advanced computing to accelerate this growth—makes cloud computing a viable option to advance research and speed up new product development. Cloud computing can give enterprises access to scalable resources and the latest technologies without needing to worry about capital expenditures or limited fixed infrastructure. What is the future of cloud computing? It’s expected to become the dominant enterprise IT environment.

If your organization experiences any of the following, you’re probably a good candidate for cloud computing:

High business growth that outpaces infrastructure capabilities
Low utilization of existing infrastructure resources
Large volumes of data that are overwhelming your on-premises data storage resources
Slow response times with on-premises infrastructure
Delayed product development cycles due to infrastructure constraints
Cash flow challenges due to high computing infrastructure expenses
Highly mobile or distributed user population
These scenarios require more than traditional data centers can provide.

Use cases """

result=chain.invoke({'text':text})

chain.get_graph().print_ascii()




