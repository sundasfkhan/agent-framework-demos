import asyncio
from utility import get_openai_client
from typing import Annotated
from agent_framework import ai_function

@ai_function
def get_weather(location: Annotated[str, "The city and state, e.g. San Francisco, CA"]) -> str:
    """Get the current weather for a given location."""
    return f"The weather in {location} is cloudy with a high of 15°C."


async def main():

    client = get_openai_client()

    weather_agent = client.create_agent(
        name="WeatherAgent",
        instructions="You are a helpful weather assistant.",
        tools=get_weather,
    )

    urdu_agent = client.create_agent(
        instructions="You are a helpful assistant who responds in Urdu.",
        tools=weather_agent.as_tool()
    )

    result = await urdu_agent.run("What is the weather like in Karachi, Pakistan?")
    print(result.text)

asyncio.run(main())
