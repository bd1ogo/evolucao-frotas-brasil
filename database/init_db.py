import mysql.connector
import os
from dotenv import load_dotenv

def init_db():
    print("\n[DB] Inicializando banco de dados...")
    load_dotenv(dotenv_path=".env")
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")

    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = conn.cursor()

    with open("database/schema.sql", "r") as file:
        sql_script = file.read()

    for statement in sql_script.split(";"):
        if statement.strip():
            cursor.execute(statement)
    conn.commit()

    cursor.close()
    conn.close()
    print("[DB] Banco e tabela prontos!")