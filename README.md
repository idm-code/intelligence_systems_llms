# Sistemas Inteligentes con LLM y Herramientas

Este proyecto muestra cómo crear agentes inteligentes que responden preguntas usando modelos de lenguaje (LLM) y herramientas personalizadas, empleando LangChain, LangChain OpenAI y LangChain Ollama. Incluye ejemplos tanto con modelos en la nube (OpenAI) como con modelos locales (Ollama).

## Estructura del proyecto

- `.env`: Contiene la clave de API de OpenAI.
- `.gitignore`: Excluye archivos sensibles como `.env`.
- `1. Zero-Shot Agent + Tool/main.py`: Agente con OpenAI y herramienta personalizada para consulta de capitales.
- `2. LLM Basic Agent Langchain/main.py`: Agente con modelo local (Ollama) y herramienta calculadora básica.
- `3. Multitool Agent Langchain/main.py`: Agente con modelo local y múltiples herramientas (calculadora, búsqueda y lectura de archivos).

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

## Requisitos

- Python 3.8+
- Paquetes: `langchain`, `langchain_openai`, `langchain_ollama`, `langchain_community`, `python-dotenv`

Instalación de dependencias:

```sh
pip install langchain langchain_openai langchain_ollama langchain_community python-dotenv
```

## Notas

- Para modelos OpenAI, coloca tu clave en `.env`:
  ```
  OPENAI_API_KEY=tu_clave_aqui
  ```
- Para modelos Ollama, asegúrate de tener Ollama instalado y el modelo descargado.
- LangChain recomienda migrar agentes nuevos a LangGraph para mayor flexibilidad y funcionalidades avanzadas.

## Créditos

Desarrollado como ejemplo para sistemas inteligentes con LLM y herramientas personalizadas usando LangChain, OpenAI y Ollama.
