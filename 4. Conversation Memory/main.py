from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain_community.llms import Ollama
from langchain.tools import tool
from langchain.memory import ConversationBufferMemory

import os
import fnmatch

# Tool 1: Suma
@tool
def sumar(a_b: str) -> str:
    """Devuelve la suma de dos números. Escribe como '5 + 3'."""
    try:
        # Limpiar comillas y espacios igual que en el directorio 3
        clean = a_b.replace("'", "").replace('"', "").strip()
        a, b = map(float, [x.strip() for x in clean.split("+")])
        return str(a + b)
    except Exception as e:
        return f"Error en la suma: {str(e)}"

# Tool 2: Buscar archivos
@tool
def buscar_archivos(input_str: str) -> str:
    """Busca archivos por nombre o patrón (como '*.txt') dentro de un directorio. Input: '<patron>, <directorio>' (el directorio es opcional, por defecto es el actual)."""
    try:
        # Limpiar comillas del input completo primero
        clean_input = input_str.replace("'", "").replace('"', "").strip()
        
        partes = [p.strip() for p in clean_input.split(",")]
        patron = partes[0]
        
        # Usar el directorio especificado, o el actual (.) si no se proporciona.
        directorio = partes[1] if len(partes) > 1 and partes[1] else "."
            
        encontrados = []
        for root, dirs, files in os.walk(directorio):
            for filename in fnmatch.filter(files, patron):
                encontrados.append(os.path.join(root, filename))
        return "\n".join(encontrados) if encontrados else "No se encontraron archivos"
    except Exception as e:
        return f"Error buscando archivos: {str(e)}"

# Tool 3: Leer archivo
@tool
def leer_archivo(ruta: str) -> str:
    """Lee el contenido de un archivo de texto plano dado su path completo."""
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            contenido = f.read()
        return contenido[:1500]  # Limitamos la respuesta
    except Exception as e:
        return f"No se pudo leer el archivo: {str(e)}"

# Inicialización del modelo y memoria
llm = Ollama(model="gemma3:4b")  # Cambia por "deepseek-coder" si prefieres
memoria = ConversationBufferMemory(memory_key="chat_history")

# Lista de herramientas
tools = [sumar, buscar_archivos, leer_archivo]

# Agente con memoria
agente = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memoria,
    verbose=True
)

# Ejemplos de conversación
print(agente.run("Hola, ¿quién eres?"))  # Prueba inicial
print(agente.run("¿Cuánto es 8 + 7?"))   # Usa herramienta de suma
print(agente.run("¿Recuerdas lo que acabamos de hacer?"))  # Verifica memoria
print(agente.run("Busca archivos '.txt' en el directorio actual y lee el contenido del primero."))  # Busca y lee archivos
print(agente.run("¿Recuerdas lo que acabamos de hacer?"))  # Verifica memoria
print(agente.run("Dime punto por punto todo lo que recuerdas"))  # Verifica memoria
