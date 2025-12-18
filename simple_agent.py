import asyncio
from utility import get_openai_client

async def main():

    client = get_openai_client()

    agent = client.create_agent(
        instructions="You are good for creating travel plans.",
        name="TravelAgent"
    )


    result = await agent.run("Make 2 days travel plan for sugar mountain , NC.")
    print(result.text)

asyncio.run(main())
