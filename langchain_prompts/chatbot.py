from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
load_dotenv()

chat = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash")

chat_history=[
    SystemMessage(content="You are a helpful assistant")
]

while True:
    user_input=input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input=="exit":
        break
    result=chat.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content[0]["text"]))
    print("AI: ",result.content[0]["text"])

print(chat_history)