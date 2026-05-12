from crewai import Agent
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o")

swot_agent = Agent(
    role="Business Strategist",
    goal="Generate SWOT analysis",
    backstory="Expert startup strategist",
    verbose=True,
    llm=llm
)