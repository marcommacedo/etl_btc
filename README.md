# ETL - Bitcoin

Este projeto realiza um processo ETL (Extract, Transform, Load) para coletar o preço do Bitcoin em tempo real usando a API pública da Coinbase, transformando e armazenando os dados em bancos de dados NoSQL (TinyDB) e SQL (via SQLAlchemy). Também inclui um dashboard interativo feito com Streamlit para visualização dos dados coletados e um agente de IA para análise dos dados utilizando Agno + Groq.

## Pré-requisitos

- Python 3.8 ou superior instalado
- pip (gerenciador de pacotes do Python)
- Banco de dados SQL compatível (ex: SQLite, PostgreSQL, MySQL)
- Variável de ambiente `DATABASE_URL` configurada para o banco SQL
- Chave de API para o Groq (caso necessário para o agente IA)

## Tecnologias usadas

- **Python**: Linguagem principal do projeto
- **TinyDB**: Banco de dados NoSQL em arquivo JSON
- **SQLAlchemy**: ORM para bancos de dados relacionais
- **Requests**: Biblioteca para requisições HTTP
- **Coinbase API**: Fonte dos dados do preço do Bitcoin
- **python-dotenv**: Gerenciamento de variáveis de ambiente
- **Streamlit**: Dashboard interativo para visualização dos dados
- **Agno**: Framework para agentes de IA
- **Groq**: Modelo de linguagem utilizado pelo agente IA
- **DuckDuckGoTools**: Ferramenta de busca integrada ao agente IA
- **pandas**: Manipulação e análise de dados

## Estrutura do Projeto

```
.
├── data/
│   └── db.json
├── etl/
│   ├── nosql.py
│   └── sql.py
├── interface/
│   └── app.py
├── ai/
│   └── app.py
├── requirements.txt
└── README.md
```

## Como funciona

- **Extract:** Coleta o preço atual do Bitcoin via API da Coinbase.
- **Transform:** Formata os dados, adicionando timestamp e organizando os campos.
- **Load:** Insere os dados transformados em um banco TinyDB (`data/db.json`) ou em um banco SQL relacional.
- **Dashboard:** Visualize os dados coletados em tempo real através de um dashboard interativo com Streamlit.
- **Agente IA:** Permite análises inteligentes dos dados coletados, respondendo perguntas e realizando buscas na web via IA.

## Instruções de Instalação

1. Clone este repositório:
   ```sh
   git clone https://github.com/marcommacedo/etl_btc.git
   cd etl_btc
   ```

2. (Opcional) Crie e ative um ambiente virtual:
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

4. Configure a variável de ambiente `DATABASE_URL` para o seu banco SQL (exemplo para SQLite):
   ```sh
   DATABASE_URL=sqlite:///data/crypto_prices.db
   ```

5. (Opcional) Configure as variáveis de ambiente necessárias para o Groq/Agno, se aplicável.

## Como executar

- Para rodar o ETL com TinyDB (NoSQL):
  ```sh
  python etl/nosql.py
  ```

- Para rodar o ETL com banco SQL:

  ```sh
  python etl/sql.py
  ```

- Para rodar o dashboard com Streamlit:
  ```sh
  streamlit run interface/app.py
  ```

- Para rodar o agente IA com análise dos dados:
  ```sh
  streamlit run ai/app.py
  ```

Os dados serão salvos e atualizados a cada 15 segundos.

## Dependências

- requests
- tinydb
- sqlalchemy
- python-dotenv
- streamlit
- agno
- groq
- pandas

Veja todas as dependências em [`requirements.txt`](requirements.txt).

## Observações

- O script pode ser interrompido a qualquer momento com `Ctrl+C`.
- O banco de dados NoSQL é um arquivo JSON simples, fácil de manipular e visualizar.
- O banco SQL pode ser configurado conforme sua necessidade via variável de ambiente.
- O dashboard permite acompanhar em tempo real a evolução dos preços coletados.
- O agente IA permite análises inteligentes e respostas automáticas sobre os dados.
- Agora o projeto suporta tanto armazenamento NoSQL (TinyDB) quanto SQL relacional (SQLAlchemy), além de visualização via Streamlit e análise via IA.

## Autor

Marco Vinicius
