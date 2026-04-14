from etl.extract import extract
from etl.transform import transform
from etl.load import load
from database.init_db import init_db

def run_pipeline():
    print("Iniciando pipeline...\n")
    # Inicia o banco
    init_db()
    # Inicia ETL
    df = extract()
    df = transform(df)
    load(df)
    print("\nPipeline executado com sucesso!")

if __name__ == "__main__":
    run_pipeline()