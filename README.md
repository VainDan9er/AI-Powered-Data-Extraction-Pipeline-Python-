AI-Powered Data Extraction Pipeline
Python pipeline that automatically extracts structured candidate information from unstructured documents (PDF and Word) and securely stores it in a local SQLite database.
By leveraging LangChain and the DeepSeek-Chat model, the project transforms raw resume text into strictly typed data objects before committing them to a relational database.

Key Features
Multi-Format Parsing: Automatically extracts text from both PDF and DOCX files using custom LangChain loaders.
Structured AI Extraction: Uses DeepSeek LLM with a strict Pydantic schema (PersonInfo) for consistent, hallucination-free JSON outputs.
Streamlined LCEL Chain: Clean, declarative pipeline built with LangChain Expression Language.
Secure Storage: Saves data to local SQLite using parameterized queries to prevent SQL injection.
Robust Error Handling: Graceful try/except blocks ensure the pipeline continues even with corrupted files.

Tech Stack
Language: Python 3.13+
AI Framework: LangChain, LangChain-DeepSeek
Data Validation: Pydantic
Database: SQLite 
File Parsing: PyPDF, Docx2txt
