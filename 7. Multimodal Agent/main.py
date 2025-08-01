from langchain.agents import initialize_agent, Tool
from langchain.llms import Ollama
from langchain.agents.agent_types import AgentType

import pandas as pd
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

# Tool 1: análisis de CSV
def analizar_csv(instruccion: str) -> str:
    try:
        df = pd.read_csv("ventas.csv")
        resultado = eval(instruccion, {"df": df})
        return str(resultado)
    except Exception as e:
        return f"Error CSV: {str(e)}"

# Tool 2: lectura de PDF
def leer_pdf(path: str = "documento.pdf") -> str:
    try:
        doc = fitz.open(path)
        texto = ""
        for page in doc:
            texto += page.get_text()
        return texto[:1000] + "..." if len(texto) > 1000 else texto
    except Exception as e:
        return f"Error PDF: {str(e)}"

# Tool 3: OCR de imagen
def leer_imagen(path: str = "factura.webp") -> str:
    try:
        img = Image.open(path)
        texto = pytesseract.image_to_string(img)
        return texto[:1000] + "..." if len(texto) > 1000 else texto
    except Exception as e:
        return f"Error Imagen: {str(e)}"

# Configuramos las herramientas
tools = [
    Tool(
        name="CSVAnalyzer",
        func=analizar_csv,
        description="Analiza un archivo CSV llamado ventas.csv. Usa instrucciones como 'df.groupby(\"País\")[\"Total\"].sum()'"
    ),
    Tool(
        name="PDFReader",
        func=leer_pdf,
        description="Lee texto del archivo PDF llamado documento.pdf"
    ),
    Tool(
        name="ImageOCR",
        func=leer_imagen,
        description="Extrae texto de la imagen llamada factura.webp usando OCR"
    ),
]

# Inicializamos el agente
llm = Ollama(model="gemma3:4b")

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Ejemplos usando todas las herramientas
print("---- CSVAnalyzer ----")
print(agent.run("¿Cuál es el total de ventas por país en ventas.csv? Usa la herramienta CSVAnalyzer con 'df.groupby(\"País\")[\"Total\"].sum()'"))

print("\n---- PDFReader ----")
print(agent.run("¿Qué texto aparece en el PDF documento.pdf? Usa la herramienta PDFReader."))

print("\n---- ImageOCR ----")
print(agent.run("¿Qué texto aparece en la imagen factura.webp? Usa la herramienta ImageOCR."))
