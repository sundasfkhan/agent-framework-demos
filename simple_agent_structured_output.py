import asyncio
from utility import get_openai_client
from pydantic import BaseModel

class PersonInfo(BaseModel):
    """Information about a person."""
    name: str | None = None
    age: int | None = None
    occupation: str | None = None



async def main():

    client = get_openai_client()

    agent = client.create_agent(
        name="HelpfulAssistant",
        instructions="You are a helpful assistant that extracts person information from text."
    )


    result =  await agent.run(
            "Please provide information about John Smith, who is a 35-year-old software engineer.",
            response_format=PersonInfo
        )
    print(result.text)

asyncio.run(main())
