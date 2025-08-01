# Sistemas Inteligentes con LLM y Herramientas

Este proyecto muestra cómo crear agentes inteligentes que responden preguntas usando modelos de lenguaje (LLM) y herramientas personalizadas, empleando LangChain, LangChain OpenAI y LangChain Ollama. Incluye ejemplos tanto con modelos en la nube (OpenAI) como con modelos locales (Ollama).

## Estructura del proyecto

- `.env`: Contiene la clave de API de OpenAI.
- `.gitignore`: Excluye archivos sensibles como `.env`.
- `1. Zero-Shot Agent + Tool/main.py`: Agente con OpenAI y herramienta personalizada para consulta de capitales.
- `2. LLM Basic Agent Langchain/main.py`: Agente con modelo local (Ollama) y herramienta calculadora básica.
- `3. Multitool Agent Langchain/main.py`: Agente con modelo local y múltiples herramientas (calculadora, búsqueda y lectura de archivos).
- `4. Conversation Memory/main.py`: Agente con modelo local, múltiples herramientas y memoria conversacional.
- `5. Database tool/main.py`: Agente con modelo local y herramienta para consultas SQL sobre una base de datos SQLite.
- `6. Data Analysis Tool/main.py`: Agente con modelo GPT-4 (OpenAI) para análisis y visualización de datos en CSV.
- `7. Multimodal Agent/main.py`: Agente con modelo local y herramientas para trabajar con datos multimodales: archivos PDF, imágenes y CSV.

## Descripción

### 1. Zero-Shot Agent + Tool (OpenAI)
Agente de tipo "Zero-Shot React Description" que utiliza una herramienta llamada `CapitalLookup` para consultar la capital de ciertos países. El agente decide cuándo usar la herramienta para responder preguntas geográficas.

**Ejemplo de uso:**
```python
python "1. Zero-Shot Agent + Tool/main.py"
```
Pregunta: ¿Cuál es la capital de Alemania?  
Respuesta esperada: Berlín

### 2. LLM Basic Agent Langchain (Ollama)
Agente que utiliza un modelo local (ejemplo: gemma3:4b) y una herramienta calculadora para realizar operaciones matemáticas simples.

**Ejemplo de uso:**
```python
python "2. LLM Basic Agent Langchain/main.py"
```
Pregunta: ¿Cuánto es 24 * 3 + 15?  
Respuesta esperada: 87

### 3. Multitool Agent Langchain (Ollama)
Agente que utiliza un modelo local (ejemplo: gemma3:4b) y varias herramientas:
- **Calculadora:** Realiza sumas simples, por ejemplo: `5 + 12`.
- **Buscar archivos:** Busca archivos por patrón en un directorio, por ejemplo: `*.txt, .` (busca archivos `.txt` en el directorio actual).
- **Leer archivo:** Lee el contenido de un archivo de texto dado su path.

**Ejemplo de uso:**
```python
python "3. Multitool Agent Langchain/main.py"
```
Preguntas de ejemplo:
- ¿Cuánto es 5 + 12?
- Busca archivos '.txt' en el directorio actual
- Lee el contenido de los archivos '*.txt'

### 4. Conversation Memory (Ollama)
Agente que utiliza un modelo local (ejemplo: gemma3:4b), varias herramientas y memoria conversacional para mantener el contexto entre preguntas y respuestas.

Herramientas disponibles:
- **Calculadora:** Realiza sumas simples, por ejemplo: `8 + 7`.
- **Buscar archivos:** Busca archivos por patrón en un directorio, por ejemplo: `*.txt, .`.
- **Leer archivo:** Lee el contenido de un archivo de texto dado su path.

La memoria permite que el agente recuerde interacciones previas y pueda responder preguntas sobre el historial de la conversación.

**Ejemplo de uso:**
```python
python "4. Conversation Memory/main.py"
```
Preguntas de ejemplo:
- Hola, ¿quién eres?
- ¿Cuánto es 8 + 7?
- ¿Recuerdas lo que acabamos de hacer?
- Busca archivos '.txt' en el directorio actual y lee el contenido del primero.
- Dime punto por punto todo lo que recuerdas

### 5. Database tool (Ollama + SQLite)
Agente que utiliza un modelo local (ejemplo: gemma3:4b) y una herramienta para ejecutar consultas SQL sobre una base de datos SQLite local (`data.db`). Permite consultar la tabla `usuarios` con los campos `id` y `nombre`.

**Ejemplo de uso:**
```python
python "5. Database tool/main.py"
```
Preguntas de ejemplo:
- ¿Cuáles son los nombres de todos los usuarios en la base de datos?
- Haz una consulta SQL para mostrar el campo 'nombre' de la tabla 'usuarios'.

### 6. Data Analysis Tool (OpenAI GPT-4 + CSV)
Agente que utiliza GPT-4 (OpenAI) y una herramienta para ejecutar código Python sobre el archivo `ventas.csv` y generar análisis o visualizaciones automáticas.

Herramientas disponibles:
- **Análisis de datos:** Ejecuta instrucciones Python sobre el DataFrame `df` cargado desde `ventas.csv`. Las columnas disponibles son:  
  `'ID_Venta', 'Fecha', 'Cliente', 'Producto', 'Categoría', 'Cantidad', 'Precio_Unitario', 'Total', 'Medio_Pago', 'País'`.

**Ejemplo de uso:**
```python
python "6. Data Analysis Tool/main.py"
```
Preguntas de ejemplo:
- Haz un gráfico de barras con el total de ventas por país y guárdalo como 'output.png'
- ¿Cuál es el país con mayor número de ventas?
- ¿Cuántas ventas se hicieron por cada medio de pago?

### 7. Multimodal Agent (Ollama + PDF/Imagen/CSV)
Agente que utiliza un modelo local (ejemplo: gemma3:4b) y herramientas para trabajar con datos multimodales: archivos PDF, imágenes y CSV.

Herramientas disponibles:
- **CSVAnalyzer:** Analiza el archivo `ventas.csv` usando instrucciones Python, por ejemplo: `df.groupby("País")["Total"].sum()`.
- **PDFReader:** Extrae texto del archivo PDF `documento.pdf`.
- **ImageOCR:** Extrae texto de la imagen `factura.webp` usando OCR.

**Ejemplo de uso:**
```python
python "7. Multimodal Agent/main.py"
```
Preguntas de ejemplo:
- ¿Cuál es el total de ventas por país en ventas.csv?
- ¿Qué texto aparece en el PDF documento.pdf?
- ¿Qué texto aparece en la imagen factura.webp?

---

## Requisitos

- Python 3.8+
- Paquetes: `langchain`, `langchain_openai`, `langchain_ollama`, `langchain_community`, `python-dotenv`, `pandas`, `matplotlib`, `PyMuPDF`, `pytesseract`, `Pillow`

Instalación de dependencias:

```sh
pip install langchain langchain_openai langchain_ollama langchain_community python-dotenv pandas matplotlib PyMuPDF pytesseract Pillow
```

## Notas

- Para modelos OpenAI, coloca tu clave en `.env`:
  ```
  OPENAI_API_KEY=tu_clave_aqui
  ```
- Para modelos Ollama, asegúrate de tener Ollama instalado y el modelo descargado.
- Para el ejemplo de base de datos, ejecuta primero `crear_db.py` en el directorio `5. Database tool/` para crear y poblar la base de datos.
- Para el análisis de datos, asegúrate de tener el archivo `ventas.csv` en el directorio correspondiente.
- Para el agente multimodal, asegúrate de tener los archivos `documento.pdf`, `factura.webp` y `ventas.csv` en el directorio `7. Multimodal Agent/`.
- LangChain recomienda migrar agentes nuevos a LangGraph para mayor flexibilidad y funcionalidades avanzadas.

## Créditos

Desarrollado como ejemplo para sistemas inteligentes con LLM y herramientas personalizadas usando LangChain, OpenAI y Ollama.
