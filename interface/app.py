from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import streamlit as st
import pandas as pd
import plotly.express as px

load_dotenv()

engine = create_engine(os.getenv(f"DATABASE_URL"))
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

st.set_page_config(page_title="Crypto Dashboard", layout="wide")

st.title("📊 Dashboard de Preços de Criptomoedas")

# Consulta os dados
@st.cache_data
def load_data():
    query = text("SELECT * FROM crypto_prices")
    df = pd.read_sql(query, engine)
    return df

df = load_data()

# Filtros interativos
cryptos = df['cryptocurrency'].unique()
selected_crypto = st.selectbox("Selecione uma moeda", cryptos)

# Filtra os dados da moeda escolhida
filtered_df = df[df['cryptocurrency'] == selected_crypto]

# Exibe os dados
st.dataframe(filtered_df)

fig = px.line(
    filtered_df,
    x='timestamp',
    y='price',
    title=f'Preço da Criptomoeda: {selected_crypto}',
    labels={'price': 'Preço', 'timestamp': 'Data'},
)

# Exibe o gráfico interativo
st.plotly_chart(fig, use_container_width=True)