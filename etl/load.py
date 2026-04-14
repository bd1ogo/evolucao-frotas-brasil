import mysql.connector
import os
from dotenv import load_dotenv

def load(df):
    print("\n[LOAD] Carregando variáveis de ambiente...")
    load_dotenv(dotenv_path=".env")
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")

    print("[LOAD] Conectando ao banco...")
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = conn.cursor()

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