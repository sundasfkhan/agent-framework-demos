"""AG-UI server example."""

import os

from agent_framework import ChatAgent
from agent_framework_ag_ui import add_agent_framework_fastapi_endpoint
from fastapi import FastAPI
from utility import get_openai_client


client = get_openai_client()

# Create the AI agent
agent = client.create_agent(
    name="AGUIAssistant",
    instructions="You are a helpful assistant.",
)



# Create FastAPI app
app = FastAPI(title="AG-UI Server")

# Register the AG-UI endpoint
add_agent_framework_fastapi_endpoint(app, agent, "/")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8888)