from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

chat= ChatGoogleGenerativeAI(
    model="gemini-3.8-flash"
)
#schema
class Review(TypedDict):
    summary: str
    sentiment: str

structured_model=chat.with_structured_output(Review)

result=structured_model.invoke(""" I liked the structure of this phone and has some good apps and settings, but it discharges fast also the ui looks outdated compared to other brands. Hoping for a software update to fix this""")

print(result)