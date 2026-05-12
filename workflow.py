from typing import TypedDict
from langgraph.graph import StateGraph, END

# State
class GraphState(TypedDict):
    input: str
    market: str
    trends: str
    swot: str
    competitors: str
    business_model: str
    score: int
    validation: str

# Main AI Node
def startup_validator(state: GraphState):

    idea = state["input"]

    return {

        "market": f"The AI market for '{idea}' is rapidly growing with high demand.",

        "trends": """
- AI automation is increasing
- Businesses adopting GenAI rapidly
- AI SaaS market booming
- Personalized AI solutions trending
""",

        "swot": """
Strengths:
- High scalability
- AI driven automation

Weaknesses:
- Requires high-quality data
- Competitive market

Opportunities:
- Huge AI adoption globally
- SaaS revenue potential

Threats:
- Fast-moving competitors
- AI regulation risks
""",

        "competitors": """
- OpenAI
- Anthropic
- Perplexity AI
- Small niche AI startups
""",

        "business_model": """
- SaaS Subscription
- Freemium Plan
- API Access
- Enterprise Licensing
""",

        "score": 8,

        "validation": f"{idea} has strong startup potential in the AI industry."
    }

# Build Graph
builder = StateGraph(GraphState)

builder.add_node("validator", startup_validator)

builder.set_entry_point("validator")

builder.add_edge("validator", END)

# Compile
workflow = builder.compile()