Real-Time Multilingual Query Handler

Overview

This project implements a backend service that handles multilingual user queries by translating them into English in real time. It uses FastAPI as the web framework and OpenAI's GPT-3 API for translation. The goal is to build a scalable and modular system that processes and responds to queries in multiple languages seamlessly.

What Has Been Done

1. Backend Logic (backend folder)

translation_engine.py  
Implements the core translation functionality using OpenAI's GPT-3 model. It takes text in any language and returns an English translation.

response_generator.py  
Adds a layer on top of translation that generates responses based on the translated input. This file can be extended for more advanced conversational or logic-based responses.

server.py  
Contains FastAPI route definitions.  
Includes a root endpoint that provides basic usage information.  
Provides a POST /translate endpoint that receives user queries, processes the translation, and returns both the translated output and a system-generated response.

__init__.py  
Marks the backend folder as a valid Python package.

2. Utilities (utils folder)

config.py  
Handles configuration, such as the OpenAI API key. Supports environment variables for secure configuration.

prompts.py  
Stores prompt templates for OpenAI requests to ensure centralized and maintainable prompt usage.

language_detection.py  
Contains placeholders for future language detection integration.

evaluation.py  
Contains placeholder utilities for future translation quality and system evaluation features.

__init__.py  
Marks the utils folder as a valid Python package.

3. Data (data folder)

sample_inputs.txt  
Includes sample multilingual queries used for testing and debugging the translation system.

4. Testing (tests folder)

test_translation.py  
Includes unit tests for verifying translation engine behavior.

test_ui.py  
Tests API responses using FastAPI's TestClient to ensure all endpoints behave correctly.

5. Root-Level Files

app.py  
The main entry script used to start the FastAPI server with automatic reload during development.

requirements.txt  
Lists all required dependencies needed to install and run the application.

.gitignore  
Contains ignore rules for Git version control.

README.md  
Documentation describing the project structure and functionality.

Usage Instructions

1. Set your OpenAI API key as an environment variable using the name OPENAI_API_KEY, or manually update the utils/config.py file.

2. Install required packages by running:
pip install -r requirements.txt

3. Start the backend server using:
uvicorn backend.server:app --reload

4. Test the system by sending a POST request to /translate with a form-data parameter named query.

Future Enhancements

Language detection for smarter routing and processing.  
Frontend UI to make the system user-friendly.  
Translation evaluation utilities and extended logging.  
A more advanced response generator for conversational or task-specific responses.
