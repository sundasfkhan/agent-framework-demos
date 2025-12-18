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


    if result.value:
        person_info = result.value
        print(f"Name: {person_info.name}, Age: {person_info.age}, Occupation: {person_info.occupation}")
    else:
        print("No structured data found in response")

asyncio.run(main())
