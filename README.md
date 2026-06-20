AI-Powered Data Extraction & Storage Pipeline
An automated document processing system built with Python that transforms unstructured text from files (like PDFs and Word documents) into cleanly structured database records using Generative AI.
Key Features:
Multi-Format Ingestion: Automatically parses and extracts raw text from .pdf, .doc, and .docx files using modular LangChain document loaders.
Intelligent AI Parsing: Leverages the DeepSeek LLM via a LangChain LCEL pipeline to analyze text and extract targeted information with zero creativity (deterministic parsing).
Strict Data Validation: Utilizes Pydantic schemas (BaseModel) to enforce rigid data types, ensuring the AI output maps perfectly to database columns.
Secure SQL Storage: Automatically streams the validated data into a local SQLite database using parameterized queries to prevent SQL injection vulnerabilities.
Tech Stack: Python, LangChain (LCEL), DeepSeek API, Pydantic, SQLite, os library.
