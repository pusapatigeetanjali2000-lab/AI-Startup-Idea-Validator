from crewai import Agent
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o")

market_agent = Agent(
    role="Market Research Analyst",
    goal="Analyze startup market opportunities",
    backstory="Expert in startup ecosystem and business intelligence",
    verbose=True,
    llm=llm
)