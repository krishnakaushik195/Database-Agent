Database Agent

Overview

Database Agent is a Streamlit-based application that connects to multiple databases and utilizes AI to generate SQL queries based on natural language input. The application integrates Groq's LLM to determine the relevant database, generate SQL queries, and format query results for easy visualization.

Features

Natural Language to SQL: Converts user questions into SQL queries using Groq LLM.

Automatic Database Selection: Identifies the relevant database schema.

Secure Connection Handling: Uses environment variables for database credentials and API keys.

Interactive UI: Built with Streamlit for easy interaction and visualization.

Installation

Prerequisites

Ensure you have the following installed:

Python 3.8+

pip

MySQL server (for database connections)

Steps

Clone the repository:

git clone https://github.com/yourusername/database-agent.git
cd database-agent

Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies:

pip install -r requirements.txt

Set up environment variables:
Create a .env file in the root directory and add:

GROQ_API_KEY=your_groq_api_key
SYS_DB_URI=mysql+mysqlconnector://user:password@host:port/sys
CHINOOK_DB_URI=mysql+mysqlconnector://user:password@host:port/chinook
SAKILA_DB_URI=mysql+mysqlconnector://user:password@host:port/sakila

Run the application:

streamlit run app.py

Usage

Enter a natural language question in the input box.

The system will determine the most relevant database.

It will generate an SQL query.

The query executes, and the results are displayed as a table.

Contributing

Contributions are welcome! Follow these steps:

Fork the repository.

Create a feature branch (git checkout -b feature-name).

Commit changes (git commit -m "Add feature").

Push to the branch (git push origin feature-name).

Open a pull request.

License

This project is licensed under the MIT License. See LICENSE for details.

Acknowledgments

Groq for the AI-powered SQL generation.

Streamlit for the interactive UI framework.
