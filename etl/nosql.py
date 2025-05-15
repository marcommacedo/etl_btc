import requests
from tinydb import TinyDB
from datetime import datetime
from time import sleep

def extract_data_from_api():
    api_url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao buscar dados da API: {response.status_code}")

def transform_data(data):
    value = data["data"]["amount"]
    criptocurrency = data["data"]["base"]
    currency = data["data"]["currency"]
    
    transformed_data = {
        "value": value,
        "criptocurrency": criptocurrency,
        "currency": currency,
        "timestamp": datetime.now().isoformat()
    }
    
    return transformed_data

def load_data_db(transform_data):
    db = TinyDB("data/db.json")
    db.insert(transformed_data)

if __name__ == "__main__":
    while True:
        # Extract
        data = extract_data_from_api()
        
        # Transform
        transformed_data = transform_data(data)
        
        # Load
        load_data_db(transform_data)
        
        print("Dados carregados!")
        sleep(15)