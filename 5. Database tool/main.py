from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain_community.llms import Ollama
from langchain.memory import ConversationBufferMemory
import sqlite3

# Crea función para ejecutar consultas SQL en una base de datos SQLite
def consultar_sqlite(query: str) -> str:
    try:
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()
        conn.close()
        return str(resultados)
    except Exception as e:
        return f"Error en la consulta: {e}"

# Definimos la tool para SQLite
sqlite_tool = Tool(
    name="SQL Query Tool",
    func=consultar_sqlite,
    description=(
        "Ejecuta consultas SQL sobre una base de datos SQLite local llamada data.db. "
        "La base de datos tiene una tabla llamada 'usuarios' con los campos 'id' y 'nombre'. "
        "Úsalo para leer tablas o extraer datos. Asegúrate de que las consultas son correctas."
    )
)

# Creamos la memoria y el modelo local
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
llm = Ollama(model="gemma3:4b")

# Inicializamos el agente solo con la herramienta de SQLite
agent = initialize_agent(
    tools=[sqlite_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)

# Ejemplo de interacción
agent.run("¿Cuáles son los nombres de todos los usuarios en la base de datos?")
