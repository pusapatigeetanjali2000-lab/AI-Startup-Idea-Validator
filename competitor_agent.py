from crewai import Agent
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o")

competitor_agent = Agent(
    role="Competitor Analyst",
    goal="Find startup competitors and analyze strengths",
    backstory="Expert in competitive analysis",
    verbose=True,
    llm=llm
)