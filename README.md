# Database Agent

## 🚀 Overview
Database Agent is a Streamlit-based application that connects to multiple databases and utilizes AI-powered SQL generation to transform natural language queries into executable SQL statements. Powered by Groq's LLM, it identifies the relevant database, constructs optimized SQL queries, and presents the results in an interactive interface.

## ✨ Features
✅ **AI-Powered SQL Generation** – Convert natural language questions into SQL queries using **Groq LLM**.  
✅ **Automatic Database Selection** – Dynamically determines the most relevant database.  
✅ **Secure Database Connections** – Uses **environment variables** to handle database credentials securely.  
✅ **Interactive UI** – Built with **Streamlit** for intuitive interactions and easy query visualization.  

---

## 🛠 Installation  

### 📌 Prerequisites  
Ensure you have the following installed:  
- **Python 3.8+**  
- **pip** (Python package manager)  
- **MySQL Server** (for database connections)  

### 📥 Setup Steps  

```sh
# Clone the repository
git clone https://github.com/krishnakaushik195/Database-Agent.git
cd Database-Agent

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
echo "GROQ_API_KEY=your_groq_api_key" >> .env
echo "SYS_DB_URI=mysql+mysqlconnector://user:password@localhost:3306/sys" >> .env
echo "CHINOOK_DB_URI=mysql+mysqlconnector://user:password@localhost:3306/chinook" >> .env
echo "SAKILA_DB_URI=mysql+mysqlconnector://user:password@localhost:3306/sakila" >> .env

# Run the application
python app.py
