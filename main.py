import asyncio
import os
from dotenv import load_dotenv
from agent_framework.openai import OpenAIChatClient

# Load environment variables from .env file
load_dotenv()

async def main():

    client = OpenAIChatClient(
        api_key=os.getenv('API_KEY'),
        base_url=os.getenv('BASE_URL'),
        model_id=os.getenv('MODEL_ID')
    )

    agent = client.create_agent(
        instructions="You are good for creating travel plans.",
        name="TravelAgent"
    )


    result = await agent.run("Make 2 days travel plan for sugar mountain , NC.")
    print(result.text)

asyncio.run(main())
