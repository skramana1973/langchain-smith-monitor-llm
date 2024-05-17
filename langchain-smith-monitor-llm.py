from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("OPENAI_API_KEY")
print("OPENAI_API_KEY   :   ", key)

llm = ChatOpenAI()
# llm.invoke("What is lang smith in lang chain?")

print(llm.predict("What is lang smith in lang chain?"))
