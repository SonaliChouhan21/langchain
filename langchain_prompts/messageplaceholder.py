from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


#chat template
chat_template=ChatPromptTemplate([
    ('system','You are a helpful customer support aggent'),
    MessagesPlaceholder(variable_name='Chat_history'),
    ('human','{query}')
])
chat_history=[]
#load chat history
with open(r'C:\Users\HP\OneDrive\Desktop\sonali\gen ai\langchain_prompts\chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

#create prompt
prompt = chat_template.invoke({'chat_history':chat_history, 'query':'Where is my refund'})

result=chat.invoke(prompt)