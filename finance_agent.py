from crewai import Agent
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o")

finance_agent = Agent(
    role="Financial Analyst",
    goal="Estimate TAM SAM SOM and revenue potential",
    backstory="Startup financial modeling expert",
    verbose=True,
    llm=llm
)