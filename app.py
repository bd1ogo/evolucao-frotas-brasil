import streamlit as st
import pandas as pd
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_data():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    query = "SELECT * FROM frota"
    df = pd.read_sql(query, conn)
    conn.close()

    return df

st.set_page_config(page_title="Evolução Frotas Brasil", layout="wide")
st.title("Evolução das Frotas Elétricas e Híbridas no Brasil")

df = get_data()

st.subheader("Evolução da Frota ao Longo do Tempo")
df_ano = df.groupby("ano")["quantidade"].sum().reset_index()
st.line_chart(df_ano.set_index("ano"))

st.subheader("Comparação por Tipo de Veículo")
df_tipo = df.groupby("tipo")["quantidade"].sum().reset_index()
st.bar_chart(df_tipo.set_index("tipo"))

st.subheader("Ranking por Estado")
df_estado = df.groupby("estado")["quantidade"].sum().reset_index()
st.bar_chart(df_estado.set_index("estado"))

st.sidebar.header("Filtros")
tipo_selecionado = st.sidebar.selectbox(
    "Tipo de Veículo",
    options=df["tipo"].unique()
)
df_filtrado = df[df["tipo"] == tipo_selecionado]

st.subheader(f"Dados Filtrados: {tipo_selecionado}")
st.dataframe(df_filtrado)