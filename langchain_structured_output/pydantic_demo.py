from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict,Optional,Literal
from pydantic import BaseModel, Field

load_dotenv()

chat= ChatGoogleGenerativeAI(
    model="gemini-3.8-flash"
)
#schema
class Review(BaseModel):
    key_themes:list[str]=Field(description="write all key themes discussed in the review in a list")
    summary: str=Field(description="a brief summary of the review")
    sentiment:Literal['pos','neg']=Field(description="return sentiment of the review positive, negative or neutral")
    pros: Optional[list[str]]=Field(default=None,description="list all pros from the review")
    cons: Optional[list[str]]=Field(default=None,description="list all cons from the review")
    name: Optional[str]=Field(default=None,description="write the name of the reviewer")

structured_model=chat.with_structured_output(Review)

result=structured_model.invoke(""" I liked the structure of this phone and has some good apps and settings, but it discharges fast also the ui looks outdated compared to other brands. Hoping for a software update to fix this""")

print(result)