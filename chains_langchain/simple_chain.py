from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

prompt=PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variable=['topic']
)

chat = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash")

parser= StrOutputParser()

chain=prompt | chat | parser

result=chain.invoke({'topic':'Ice Cream'})
chain.get_graph().print_ascii()
