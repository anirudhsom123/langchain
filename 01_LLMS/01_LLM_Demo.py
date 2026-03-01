import langchain_google_genai
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

# Load your GOOGLE_API_KEY from your .env file
load_dotenv()

# Initialize the Gemini model
llm=langchain_google_genai.ChatGoogleGenerativeAI(model="gemini-2.5-flash")
# llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Invoke the model
response = llm.invoke("What is the capital of India?")

print(response.content)