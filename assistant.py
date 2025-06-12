import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient

async def main():
    load_dotenv()
    client = MCPClient.from_config_file("server_config.json")
    llm = ChatOpenAI(model="gpt-4o")
    agent = MCPAgent(llm=llm, client=client, max_steps=30)
    async for chunk in agent.astream("What resource groups are there in my account?"):
        print(chunk["messages"], end="", flush=True)

if __name__ == "__main__":
    asyncio.run(main())