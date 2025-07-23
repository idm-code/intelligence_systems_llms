# Zero-Shot Agent + Tool con LLM

Este proyecto demuestra cómo crear un agente inteligente capaz de responder preguntas utilizando un modelo de lenguaje (LLM) y herramientas personalizadas. El agente utiliza la librería LangChain y OpenAI para procesar preguntas y, cuando es necesario, consultar una herramienta personalizada para obtener información específica.

## Estructura del proyecto

- `.env`: Contiene la clave de API de OpenAI.
- `.gitignore`: Excluye archivos sensibles como `.env`.
- `1. Zero-Shot Agent + Tool/main.py`: Código principal del agente y la herramienta personalizada.

## Descripción

El agente implementado es de tipo "Zero-Shot React Description". Se le proporciona una herramienta llamada `CapitalLookup`, que permite consultar la capital de ciertos países. Si el agente detecta que la pregunta requiere esta información, utiliza la herramienta para responder.

### Ejemplo de uso

Al ejecutar el script principal, el agente responde a la pregunta:

## Requisitos

- Python 3.8+
- Paquetes: `langchain`, `langchain_openai`, `python-dotenv`

Instalación de dependencias:

```sh
pip install langchain langchain_openai python-dotenv
```
