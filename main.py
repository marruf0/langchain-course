from dotenv import load_dotenv
from typing import List
from pydantic import BaseModel, Field

##### Libraries for calling the AI models
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

##### Libraries for Agents creation
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
#from tavily import TavilyClient # Replace by langchain-tavily
from langchain_tavily import TavilySearch
from langchain.tools import tool

load_dotenv()

#tavily = TavilyClient() #not in use because we change the library 
#llm = ChatOllama(temperature=0, model="gpt-oss") # For open source (no payment) models
llm = ChatOpenAI(temperature=0, model="gpt-5")
prompt= "whats the weather in hermosillo"

class Source(BaseModel):
    """
    Schema for a source used by the agent
    """
    url:str = Field(description= "The URL of the source")

class AgentResponse(BaseModel):
    """
    Schema for agent response with answer and source
    """
    answer:str = Field(description="The agent's answer to the query")
    sources:List[Source] = Field(default_factory=list, description="the list of sources used to generate the answer")


########################## TOOL LIST SECTION ##########################
# @tool
# def search(query: str) -> str:
#     """
#     Tool that search information in internet

#     Args:
#         query: the query to search for
#     Return:
#         the search result
#     """
#     print(f"searching for {query}")
#     operation = tavily.search(query=query)
#     return operation


tools_list = [TavilySearch()]
agent = create_agent(model=llm, tools=tools_list, response_format=AgentResponse)

def main():
    print("hello")
    result = agent.invoke({"messages":HumanMessage(content="whats the weather in hermosillo")})
    print(result)
    print(' ')
    print(result['structured_response'])
    print(' ')
    print(result['structured_response'].answer)
    print(' ')
    print(result['structured_response'].sources)
    print(' ')


if __name__ == "__main__":
    main()