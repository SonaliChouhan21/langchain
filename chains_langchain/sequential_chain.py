from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

prompt1=PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variable=['topic']
)

prompt2=PromptTemplate(
    template='Generate a 5 pointer summary on the following text \n  {text}',
    input_variable=['text']
)

chat = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash")

parser =StrOutputParser()

chain=prompt1 | chat | parser | prompt2 | chat | parser
result=chain.invoke({'topic':'unemployment in india'})