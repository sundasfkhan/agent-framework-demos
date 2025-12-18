import asyncio
from utility import get_openai_client
from agent_framework import ChatAgent, MCPStreamableHTTPTool


async def main():

    client = get_openai_client()
    sever=MCPStreamableHTTPTool(
            name="Microsoft Learn MCP",
            url="https://learn.microsoft.com/api/mcp",
            headers={"Authorization": "Bearer your-token"},
        )
    agent = client.create_agent(
        name="DocsAgent",
        instructions="You help with Microsoft documentation questions.",
    )


    result = await agent.run("How to create an Azure storage account using az cli?")
    print(result.text)

asyncio.run(main())
