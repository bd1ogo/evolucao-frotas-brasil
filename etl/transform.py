def transform(df):
    print("\n[TRANSFORM]: Iniciando transformação dos Dados")
    df = df.dropna()

    df["ano"] = df["ano"].astype(int)
    df["quantidade"] = df["quantidade"].astype(int)
    df["total_ano"] = df.groupby("ano")["quantidade"].transform("sum")

    print("\n[TRANSFORM] Dados transformados: ")
    print(df.head())
    return df
