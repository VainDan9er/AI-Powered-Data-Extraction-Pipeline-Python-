AI-Powered Data Extraction Pipeline
Python pipeline that automatically extracts structured candidate information from unstructured documents (PDF and Word) and securely stores it in a local SQLite database.
By leveraging LangChain and the DeepSeek-Chat model, the project transforms raw resume text into strictly typed data objects before committing them to a relational database.

Key Features
Multi-Format Document Parsing: Automatically detects and extracts raw text from both .pdf and .docx files using custom LangChain document loaders.
Structured AI Extraction: Utilizes DeepSeek LLM constrained by a strict Pydantic schema (PersonInfo) to guarantee consistent JSON-like outputs without model hallucinations.
Streamlined LCEL Chain: Implements LangChain Expression Language (prompt | structured_ai_agent) for clean, declarative data flow management.
Secure Database Storage: Persists data to a local SQLite database using parameterized queries to eliminate the risk of SQL injection and format exceptions.
Graceful Error Handling: Wrapped in robust try/except blocks to ensure the pipeline continues processing even if a single document is corrupted or unreadable.

Tech Stack
Language: Python 3.13+
AI Framework: LangChain, LangChain-DeepSeek
Data Validation: Pydantic
Database: SQLite 
File Parsing: PyPDF, Docx2txt
