import os
import pyodbc
from dotenv import load_dotenv
from sqlalchemy import create_engine
from urllib.parse import quote_plus

load_dotenv(r"D:\CHATBOT\.env")

# Environment variables
DB_SERVER = os.getenv("DB_SERVER")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
AZURE_SQL_USER = os.getenv("AZURE_SQL_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DRIVER = os.getenv("DB_DRIVER", "ODBC Driver 18 for SQL Server")
AUTH_MODE = "SQL"

if AUTH_MODE == "SQL":  
    DB_SERVER = os.getenv("DB_SERVER")
    DB_NAME = os.getenv("DB_NAME")

server_part = f"{DB_SERVER},{DB_PORT}" if DB_PORT else DB_SERVER

# ---------------------------------------------
# Build pyodbc connection string dynamically
# ---------------------------------------------
def build_conn_str():
    if not DB_SERVER or not DB_NAME:
        raise ValueError("❌ Missing required database environment variables (DB_SERVER or DB_NAME).")
        
    # ✅ SQL Authentication (for Azure/dev tunnel)
    if AUTH_MODE == "SQL":
        # ✅ SQL Authentication (Azure / remote)
        if not AZURE_SQL_USER or not DB_PASSWORD:
            raise ValueError("❌ Missing AZURE_SQL_USER or DB_PASSWORD for SQL Authentication.")
        conn_str = (
            f"Driver={{{DB_DRIVER}}};"
            f"SERVER={server_part};"
            f"DATABASE={DB_NAME};"
            f"UID={AZURE_SQL_USER};"
            f"PWD={DB_PASSWORD};"
            "Encrypt=yes;"
            "TrustServerCertificate=yes;"
            "Connection Timeout=30;"
        )
    else:       
        # ✅ Windows Authentication (for local)
        conn_str = (
            f"Driver={{{DB_DRIVER}}};"
            f"SERVER={server_part};"
            f"DATABASE={DB_NAME};"
            "Trusted_Connection=yes;"
            "TrustServerCertificate=yes;"
            "Connection Timeout=30;"
        )
    return conn_str
           
# ---------------------------------------------
# Establish database connection
# ---------------------------------------------
def get_connection():
    """
    Creates and returns a new database connection.
    """
    try:
        conn_str = build_conn_str()
        print(f"Connecting to {DB_SERVER} (using mode: {AUTH_MODE}...")
        print(f"pyodbc version: {pyodbc.version}")

        conn = pyodbc.connect(conn_str, autocommit=False, timeout=20)
        print("Database connected successfully!")
        return conn

    except pyodbc.Error as e:
        print("Database connection failed.")
        print(f"Error details: {e}")
        raise

