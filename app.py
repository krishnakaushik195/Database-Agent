import streamlit as st
from langchain_community.utilities import SQLDatabase
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("Missing API key. Please set GROQ_API_KEY in your environment.")
    st.stop()

# Database URIs (Use environment variables for security)
db_uris = {
    "sys": os.getenv("SYS_DB_URI"),
    "chinook": os.getenv("CHINOOK_DB_URI"),
    "sakila": os.getenv("SAKILA_DB_URI"),
}

# Validate DB connections
db_connections = {}
for name, uri in db_uris.items():
    if uri:
        try:
            db_connections[name] = SQLDatabase.from_uri(uri)
        except Exception as e:
            st.warning(f"Failed to connect to {name}: {e}")

if not db_connections:
    st.error("No database connections available.")
    st.stop()

# Function to retrieve schemas
def get_schema(db_name):
    return db_connections[db_name].get_table_info()

# Prompts
schema_matching_prompt_template = """You are an intelligent assistant. Based on the following database schema, check where this user's question belongs. Respond strictly with yes or no.
Schema:{schema}
Question: {question}
Match:"""
schema_matching_prompt = ChatPromptTemplate.from_template(schema_matching_prompt_template)

generate_sql_prompt_template = """Generate only the SQL query to answer the user's question:
{schema}
Question: {question}
SQL Query:"""
generate_sql_prompt = ChatPromptTemplate.from_template(generate_sql_prompt_template)

visualization_prompt_template = """Format the following data as a clean table:
{query_result}
"""
visualization_prompt = ChatPromptTemplate.from_template(visualization_prompt_template)

# Initialize the Groq LLM
llm = ChatGroq()

# Determine relevant database
def determine_relevant_database(question):
    for db_name in db_connections.keys():
        schema = get_schema(db_name)
        formatted_prompt = schema_matching_prompt.format(schema=schema, question=question)
        response = llm.invoke(formatted_prompt).content.strip().lower()
        if response == "yes":
            return db_name
    return None

# Execute a SQL query
def run_query(database, query):
    try:
        return db_connections[database].run(query)
    except Exception as e:
        return f"Error: {e}"

# Streamlit UI
st.title("Database Agent")
user_question = st.text_input("Enter your question:")

if user_question:
    selected_database = determine_relevant_database(user_question)

    if not selected_database:
        st.error("No matching database found.")
    else:
        st.success(f"Selected Database: {selected_database}")
        schema = get_schema(selected_database)
        formatted_sql_prompt = generate_sql_prompt.format(schema=schema, question=user_question)
        generated_sql = llm.invoke(formatted_sql_prompt).content.strip()
        st.subheader("Generated SQL Query:")
        st.code(generated_sql)

        query_result = run_query(selected_database, generated_sql)
        if "Error" in query_result:
            st.error(query_result)
        else:
            formatted_visualization_prompt = visualization_prompt.format(query_result=query_result)
            formatted_output = llm.invoke(formatted_visualization_prompt).content
            st.subheader("Query Results:")
            st.write(formatted_output)
