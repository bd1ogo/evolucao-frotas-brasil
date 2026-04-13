from etl.extract import extract
from etl.transform import transform
from etl.load import load

def run_pipeline():
    print("Iniciando pipeline \n")
    df = extract()
    df = transform(df)
    load(df)
    print("\n Pipeline executado com sucesso!")

if __name__ == "__main__":
    run_pipeline()
