from langchain.agents import initialize_agent, Tool
from langchain_community.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
from langchain.tools import tool
import pandas as pd
import matplotlib.pyplot as plt
import textwrap
import os
from dotenv import load_dotenv

# Cargar variables de entorno (incluida la API key de OpenAI)
load_dotenv()

# Tool: análisis y visualización de datos
@tool
def data_analysis_tool(instruction: str) -> str:
    """
    Ejecuta código Python para analizar datos del archivo 'ventas.csv' y generar visualizaciones.
    Proporciona directamente el código Python, por ejemplo:
    "df.groupby('País')['Total'].sum().plot(kind='bar'); plt.savefig('output.png')"
    Las columnas disponibles son: 'ID_Venta', 'Fecha', 'Cliente', 'Producto', 'Categoría', 'Cantidad', 'Precio_Unitario', 'Total', 'Medio_Pago', 'País'.
    """
    try:
        df = pd.read_csv("ventas.csv")
        import io
        import contextlib

        code_to_run = f"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ventas.csv')
{instruction}
"""
        code_to_run = textwrap.dedent(code_to_run)

        with contextlib.redirect_stdout(io.StringIO()) as f:
            exec(code_to_run, {"df": df, "plt": plt})

        return f"Operación realizada. Resultado:\n{f.getvalue()}\n(Revisa si se generó un gráfico en 'output.png')"
    except Exception as e:
        return f"Error al analizar los datos: {str(e)}"

# Inicialización del modelo GPT-4
llm = ChatOpenAI(model="gpt-4", temperature=0)

tools = [
    Tool(
        name="DataAnalyzer",
        func=data_analysis_tool,
        description=(
            "Ejecuta código Python para analizar datos del archivo 'ventas.csv' y generar visualizaciones. "
            "Proporciona directamente el código Python, por ejemplo: "
            "\"df.groupby('País')['Total'].sum().plot(kind='bar'); plt.savefig('output.png')\" "
            "Las columnas disponibles son: 'ID_Venta', 'Fecha', 'Cliente', 'Producto', 'Categoría', 'Cantidad', 'Precio_Unitario', 'Total', 'Medio_Pago', 'País'."
        )
    )
]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Ejemplo de pregunta (en lenguaje natural, GPT-4 sí puede traducirlo a código Python)
agent.run("Haz un gráfico de barras con el total de ventas por región y guárdalo como 'output.png'")
