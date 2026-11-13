from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-1.5B-Instruct"
)

chat = ChatHuggingFace(llm=llm)

response = chat.invoke("What is the capital of India?")

print(response.content)
