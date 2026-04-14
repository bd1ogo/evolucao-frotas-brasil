import mysql.connector
import os
from dotenv import load_dotenv

def load(df):
    print("\n[LOAD] Conectando ao MySQL...")

    load_dotenv(dotenv_path=".env")
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")

    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = conn.cursor()

    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    print("[LOAD] Banco criado/verificado")
    cursor.close()
    conn.close()

    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS frota (
            id INT AUTO_INCREMENT PRIMARY KEY,
            ano INT,
            tipo VARCHAR(20),
            quantidade INT,
            estado VARCHAR(2),
            total_ano INT
        )
    """)
    print("[LOAD] Tabela criada/verificada")

    cursor.execute("DELETE FROM frota")

    print("[LOAD] Inserindo dados...")

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO frota (ano, tipo, quantidade, estado, total_ano)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            row["ano"],
            row["tipo"],
            row["quantidade"],
            row["estado"],
            row["total_ano"]
        ))
    conn.commit()

    cursor.close()
    conn.close()

    print("[LOAD] Dados inseridos com sucesso!")