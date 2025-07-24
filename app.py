import uvicorn
from fastapi import FastAPI, Request
from src.graph.graph_builder import Graph_Builder
from src.llm.groq_llm import GROQLLM
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv(override=True)

app = FastAPI()

# Ensure Langsmith is configured
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

@app.post("/blogs")
async def create_blogs(request: Request):
    """
    Endpoint to create blog content based on a given topic.
    """
    data = await request.json()
    topic = data.get('topic', '')

    if not topic:
        return {"error": "No topic provided."}

    # Initialize LLM
    llm = GROQLLM().get_llm()

    # Build and compile the graph
    graph = Graph_Builder(llm).compile_graph(usecase='topic')

    # Invoke the graph with the provided topic
    state = graph.invoke({"topic": topic})

    return {"data": state}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)


        


    


