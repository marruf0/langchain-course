from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from tavily import TavilyClient

load_dotenv()
tavily = TavilyClient()

@tool
def search(query: str) -> str:
    """
    Tool that search information in internet

    Args:
        query: the query to search for
    Return:
        the search result
    """
    print(f"searching for {query}")
    operation = tavily.search(query=query)
    return operation

prompt= "whats the weather in hermosillo"

#llm = ChatOllama(temperature=0, model="gpt-oss") # For open source (no payment) models
llm = ChatOpenAI(temperature=0, model="gpt-5")
tools_list = [search]
agent = create_agent(model=llm, tools=tools_list)

def main():
    print("hello")
    result = agent.invoke({"messages":HumanMessage(content="whats the weather in hermosillo")})
    print(result)


if __name__ == "__main__":
    main()