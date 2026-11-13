from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding=OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)
documents=[
    "hmgjf jgfuyfuyf","ggiugiu hjguyg","jguy jg jfuf jhfj"]

result=embedding.embed_documents(documents)
print(str(result))