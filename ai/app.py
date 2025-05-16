import streamlit as st
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
import pandas as pd
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

load_dotenv()

engine = create_engine(os.getenv(f"DATABASE_URL"))
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    description="Procurar mais informacoes na internet",
    tools=[DuckDuckGoTools()],      # Add DuckDuckGo tool to search the web
    show_tool_calls=True,           # Shows tool calls in the response, set to False to hide
    markdown=True                   # Format responses in markdown
)

st.title("Agente IA com Agno + Groq")

# Consulta os dados
@st.cache_data
def load_data():
    try:
        with Session() as session:
            query = text("SELECT * FROM crypto_prices")
            df = pd.read_sql(query, engine)
            return df
    except Exception as e:
        return pd.DataFrame()

df = load_data()

if df.empty:
    st.error(f"Erro ao carregar os dados do banco. Execute o arquivo elt/sql.py antes de continuar.")
else:
    # Filtros interativos
    cryptos = df["cryptocurrency"].unique()
    selected_crypto = st.selectbox("Selecione uma moeda", cryptos)

    # Filtra os dados da moeda escolhida
    filtered_df = df[df["cryptocurrency"] == selected_crypto]

    # Exibe os dados
    st.dataframe(filtered_df, column_config={
        "price": st.column_config.NumberColumn(
            format="$ %.8f"
        )
    })

    prompt_input = st.text_area("Pergunte alguma coisa:")

    if st.button("Executar análise") and prompt_input.strip() and not df.empty:
        with st.spinner("Executando análise com IA..."):
            prompt = f"""
            { prompt_input }
            
            {df.head().to_csv(index=False)}
            """
            
            resposta = agent.run(prompt).content
            st.markdown("### Análise da IA:")
            st.write(resposta)
    elif df.empty:
        st.warning("Não há dados para consulta.")