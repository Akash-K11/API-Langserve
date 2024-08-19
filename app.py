from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms.ollama import Ollama
from dotenv import load_dotenv

print("Starting to load environment...")
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
print(f"OPENAI_API_KEY loaded: {'Yes' if openai_key else 'No'}")

app = FastAPI(
    title="Langchain API Server",
    version="1.0",
    description="A simple API Server using LLaMa 3.1 and GPT-40"
)

# Add a root path
@app.get("/")
async def root():
    return {"status": "ok", "message": "Server is running"}

print("Initializing models...")
try:
    gpt4o_model = ChatOpenAI(model_name="gpt-4o")
    print("GPT-4o model initialized")
except Exception as e:
    print(f"Error initializing GPT-4 model: {e}")

try:
    llama31_model = Ollama(model="llama3.1")
    print("LLaMa model initialized")
except Exception as e:
    print(f"Error initializing LLaMa model: {e}")

prompt = ChatPromptTemplate.from_template("Process this query: {query}")

print("Adding routes...")
add_routes(
    app,
    prompt | gpt4o_model,
    path="/gpt"
)

add_routes(
    app,
    prompt | llama31_model,
    path="/llama"
)

print("Routes added")

if __name__ == "__main__":
    print("Starting server...")
    uvicorn.run(app, host="127.0.0.1", port=8080)