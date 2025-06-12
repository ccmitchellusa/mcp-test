import asyncio
import os
import logging
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
#from langchain_openai import ChatOpenAI
#from langchain_groq import ChatGroq
#from langchain_anthropic import ChatAnthropic
#from langchain_litellm import ChatLiteLLM
from mcp_use import MCPAgent, MCPClient

logging.basicConfig(level=logging.DEBUG)

async def main():
    # Load environment variables
    load_dotenv()

    # Create MCPClient from config file
    client = MCPClient.from_config_file(
        os.path.join(os.path.dirname(__file__), "mcp.json")
    )

    # Create LLM
    llm = ChatOllama(model="granite3.3")
    # llm = ChatOllama(model="qwen3")
    # llm = ChatLiteLLM(model="watsonx/ibm/granite-3-3-8b-instruct")
    # llm = ChatOpenAI(model="gpt-4o-mini")
    # llm = ChatAnthropic(model="claude-3-5-sonnet-20240620")
    # llm = ChatGroq(model="llama3-8b-8192")

    # Create agent with the client
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    # Run the query
    result = await agent.run(
        "List resource groups in my account",
        max_steps=30,
    )
    print(f"\nResult: {result}")

if __name__ == "__main__":
    asyncio.run(main())