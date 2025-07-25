from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain_community.llms import Ollama
from langchain.tools import tool

import os
import fnmatch

# Herramienta 1: Calculadora
@tool
def sumar(a_b: str) -> str:
    """Devuelve la suma de dos números. Escribe como '5 + 12'."""
    try:
        # Limpiar comillas y espacios
        clean = a_b.replace("'", "").replace('"', "").strip()
        a, b = map(float, [x.strip() for x in clean.split("+")])
        return str(a + b)
    except Exception as e:
        return f"Error en la suma: {str(e)}"

# Herramienta 2: Buscar archivos en el sistema
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

# Herramienta 3: Leer contenido de un archivo
@tool
def leer_archivo(ruta: str) -> str:
    """Lee el contenido de un archivo de texto plano dado su path completo."""
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            contenido = f.read()
        return contenido[:1500]  # Limitamos la respuesta
    except Exception as e:
        return f"No se pudo leer el archivo: {str(e)}"

# Modelo LLM vía Ollama
llm = Ollama(model="gemma3:4b")  # Cambia a "deepseek-coder" si lo prefieres

# Inicializamos el agente
herramientas = [sumar, buscar_archivos, leer_archivo]

agente = initialize_agent(
    tools=herramientas,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Ejemplo de uso
pregunta = "¿Cuánto es 5 + 12?"
agente.run(pregunta)

pregunta2 = "Busca archivos '.txt' en el directorio actual"
agente.run(pregunta2)

pregunta3 = "Lee el contenido de los archivos '*.txt'"
agente.run(pregunta3)
