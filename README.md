# ETL - Bitcoin

Este projeto realiza um processo ETL (Extract, Transform, Load) para coletar o preço do Bitcoin em tempo real usando a API pública da Coinbase, transformando e armazenando os dados em um banco de dados NoSQL (TinyDB).

## Pré-requisitos

- Python 3.8 ou superior instalado
- pip (gerenciador de pacotes do Python)

## Tecnologias usadas

- **Python**: Linguagem principal do projeto
- **TinyDB**: Banco de dados NoSQL em arquivo JSON
- **Requests**: Biblioteca para requisições HTTP
- **Coinbase API**: Fonte dos dados do preço do Bitcoin

## Estrutura do Projeto

```
.
├── data/
│   └── db.json
├── etl/
│   └── nosql.py
├── requirements.txt
└── README.md
```

## Como funciona

- **Extract:** Coleta o preço atual do Bitcoin via API da Coinbase.
- **Transform:** Formata os dados, adicionando timestamp e organizando os campos.
- **Load:** Insere os dados transformados em um banco TinyDB (`data/db.json`).

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

## Como executar

Execute o script ETL:

```sh
python etl/nosql.py
```

Os dados serão salvos e atualizados a cada 15 segundos no arquivo `data/db.json`.

## Dependências

- requests
- tinydb

Veja todas as dependências em [`requirements.txt`](requirements.txt).

## Observações

- O script pode ser interrompido a qualquer momento com `Ctrl+C`.
- O banco de dados é um arquivo JSON simples, fácil de manipular e visualizar.

## Autor

Marco Vinicius
