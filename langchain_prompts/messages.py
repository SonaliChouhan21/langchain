from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chat= ChatGoogleGenerativeAI(
    model="gemini-3.8-flash"
)

message= [
    SystemMessage(content='You are a helpful Assistant'),
    HumanMessage(content="Tell me about lambda in AWS")
]

result=chat.invoke(message)

message.append(AIMessage(content=result.content))
print(message)
