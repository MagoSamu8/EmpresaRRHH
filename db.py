import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    try:
        server = os.getenv("DB_SERVER")
        database = os.getenv("DB_NAME")
        trusted = os.getenv("DB_TRUSTED_CONNECTION")

        connection = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"Trusted_Connection={trusted};"
        )
        return connection

    except Exception as e:
        print("Error de conexión:", e)
        return None
