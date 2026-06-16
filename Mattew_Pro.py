import os
import sqlite3
from typing import Optional
from pydantic import BaseModel, Field
from langchain_deepseek import ChatDeepSeek
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader

class PersonInfo(BaseModel):
    first_name: Optional[str] = Field(description="The person's first or given name")
    last_name: Optional[str] = Field(description="The person's last name or surname")
    age: Optional[int] = Field(description="The person's age. Null if not mentioned.")
    work_position: Optional[str] = Field(description="The person's job title or work position")

def setup_database(database_name="personnel_data.db"):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS personnel (
            id integer primary key autoincrement,
            first_name text,
            last_name text,
            age integer,
            work_position text,
            source_file text
        )
    ''')
    connection.commit()
    return connection

def insert_into_database(connection, record: PersonInfo, filename: str):
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO personnel (first_name, last_name, age, work_position, source_file)
        VALUES (?, ?, ?, ?, ?)
    ''', (record.first_name, record.last_name, record.age, record.work_position, filename))
    connection.commit()
    print(f"Successfully saved {record.first_name} {record.last_name} to database.")

def load_document(file_path: str) -> str:
    ext = os.path.splitext(file_path)[1].lower()
    
    try:
        if ext == '.pdf':
            loader = PyPDFLoader(file_path)
        elif ext in ['.doc', '.docx']:
            loader = Docx2txtLoader(file_path)
        else:
            raise ValueError(f"Unsupported file format: {ext}")
        pages = loader.load()
        full_text = "\n".join([page.page_content for page in pages])
        return full_text
        
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None

def process_file(file_path: str, database_connection):
    print(f"\nProcessing: {file_path}...")
    
    document_text = load_document(file_path)
    if not document_text:
        return

    ai_agent = ChatDeepSeek(
        model="deepseek-chat", 
        temperature=0,
        api_key="WRITE_YOUR_API_KEY_YES!") #put your api key here
    
    structured_ai_agent = ai_agent.with_structured_output(PersonInfo)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert data extraction algorithm. "
                   "Extract the requested information from the text. "
                   "If a piece of information is not present, leave it completely null."),
        ("human", "Extract data from the following document:\n\n{text}")
    ])

    extraction_chain = prompt | structured_ai_agent
    print("Extracting data via AI Agent...")
    extracted_data = extraction_chain.invoke({"text": document_text})
    filename = os.path.basename(file_path)
    insert_into_database(database_connection, extracted_data, filename)

def main():
    database_connection = setup_database()
    files_to_process = [
        "sample_profile.pdf"
    ] # put files, which you need to extract
    
    for file in files_to_process:
        if os.path.exists(file):
            process_file(file, database_connection)
            print("\n")
        else:
            print(f"File not found: {file}. Please ensure the path is correct.")
            
    database_connection.close()
    print("\nAll processing complete.")

main()

