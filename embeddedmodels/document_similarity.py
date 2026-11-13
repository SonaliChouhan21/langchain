from langchain_ollama import OllamaEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embedding = OllamaEmbeddings(
    model="nomic-embed-text",dimensions=300
)
documents=[
    "Sonali thinks that the weather is pleasant today.",
    "Sameer learning LangChain with Gemini.",
    "According to surbhi Open source models can run locally.",
    "Yukti says that Embeddings are useful for RAG applications.",
    "Mama thinks that Ollama makes it easy to use Llama models."
]
query="tell me about Sonali"

doc_embeddings = embedding.embed_documents(documents)
query_embedding=embedding.embed_query(query)

scores=cosine_similarity([query_embedding],doc_embeddings)[0]
index,score=sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("similarity score is: ",score)