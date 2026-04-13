import pandas as pd

def extract():
    df = pd.read_csv("data/raw/frota.csv")
    print("\n[EXTRACT] Dados Carregados: ")
    print(df.head())
    return df
