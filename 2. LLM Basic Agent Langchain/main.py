from langchain_ollama import OllamaLLM
from langchain_community.tools import Tool
from langchain.agents import initialize_agent, AgentType

# Paso 1: Inicializar el modelo local (usando Ollama y DeepSeek como ejemplo)
llm = OllamaLLM(model="gemma3:4b")  # Puedes cambiar por mistral, llama2, etc.

# Paso 2: Crear una herramienta muy básica para demostración (calculadora, por ejemplo)
def simple_addition(input: str) -> str:
    try:
        result = eval(input)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

tools = [
    Tool(
        name="Simple Calculator",
        func=simple_addition,
        description="Realiza operaciones matemáticas simples. Ej: 2+2"
    )
]

# Paso 3: Crear el agente con el loop de pensamiento -> acción -> observación
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Paso 4: Ejecutar una consulta de ejemplo
response = agent.invoke("¿Cuánto es 24 * 3 + 15?")
print(response)
