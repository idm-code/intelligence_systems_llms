
import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, Tool
from langchain_openai import OpenAI
from langchain.agents.agent_types import AgentType

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

def get_capital(country: str) -> str:
    capitals = {
        "españa": "Madrid",
        "spain": "Madrid",
        "francia": "París",
        "france": "París",
        "alemania": "Berlín",
        "germany": "Berlín"
    }
    key = country.strip().lower()
    return capitals.get(key, "No tengo esa información")

tools = [
    Tool(
        name="CapitalLookup",
        func=get_capital,
        description="Devuelve la capital de un país. Usa el nombre exacto del país."
    )
]

llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

if __name__ == "__main__":
    question = "¿Cuál es la capital de Alemania?"
    print(agent.run(question))
