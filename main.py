from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch


load_dotenv()



#creating a tool that searches the internet



llm = ChatOllama(temperature=0, model="qwen3:0.6b")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools )

def main():
    print("Hello from langchain-course2!")
    result = agent.invoke({"messages": [HumanMessage(content = "What is the weather in Tokyo?")]})
    print(result)
    
    for msg in result["messages"]:
        msg.pretty_print()
if __name__ == "__main__":
    main()
