# ETL - Bitcoin

Este projeto realiza um processo ETL (Extract, Transform, Load) para coletar o preço do Bitcoin em tempo real usando a API pública da Coinbase, transformando e armazenando os dados em bancos de dados NoSQL (TinyDB) e SQL (via SQLAlchemy).

## Pré-requisitos

- Python 3.8 ou superior instalado
- pip (gerenciador de pacotes do Python)
- Banco de dados SQL compatível (ex: SQLite, PostgreSQL, MySQL)
- Variável de ambiente `DATABASE_URL` configurada para o banco SQL

## Tecnologias usadas

- **Python**: Linguagem principal do projeto
- **TinyDB**: Banco de dados NoSQL em arquivo JSON
- **SQLAlchemy**: ORM para bancos de dados relacionais
- **Requests**: Biblioteca para requisições HTTP
- **Coinbase API**: Fonte dos dados do preço do Bitcoin
- **python-dotenv**: Gerenciamento de variáveis de ambiente

## Estrutura do Projeto

```
.
├── data/
│   └── db.json
├── etl/
│   ├── nosql.py
│   └── sql.py
├── requirements.txt
└── README.md
```

## Como funciona

- **Extract:** Coleta o preço atual do Bitcoin via API da Coinbase.
- **Transform:** Formata os dados, adicionando timestamp e organizando os campos.
- **Load:** Insere os dados transformados em um banco TinyDB (`data/db.json`) ou em um banco SQL relacional.

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

## Como executar

- Para rodar o ETL com TinyDB (NoSQL):

  ```sh
  python etl/nosql.py
  ```

- Para rodar o ETL com banco SQL:

  ```sh
  python etl/sql.py
  ```

Os dados serão salvos e atualizados a cada 15 segundos.

## Dependências

- requests
- tinydb
- sqlalchemy
- python-dotenv

Veja todas as dependências em [`requirements.txt`](requirements.txt).

## Observações

- O script pode ser interrompido a qualquer momento com `Ctrl+C`.
- O banco de dados NoSQL é um arquivo JSON simples, fácil de manipular e visualizar.
- O banco SQL pode ser configurado conforme sua necessidade via variável de ambiente.

## Autor

Marco Vinicius
