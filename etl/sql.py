from datetime import datetime
from time import sleep
import requests
from sqlalchemy import Column, DateTime, Integer, Numeric, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(os.getenv(f"DATABASE_URL"))
Session = sessionmaker(bind=engine)
Base = declarative_base()

class CryptoPrice(Base):
    __tablename__ = "crypto_prices"
    
    id = Column(Integer, primary_key=True)
    cryptocurrency = Column(String, nullable=False)
    currency = Column(String, nullable=False)
    price = Column(Numeric(precision=18, scale=8), nullable=False)
    timestamp = Column(DateTime, nullable=False, default=datetime.now())
    
Base.metadata.create_all(engine)
    
def extract_data_from_api():
    api_url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao buscar dados da API: {response.status_code}")
    
def transform_data(data):
    price = data["data"]["amount"]
    criptocurrency = data["data"]["base"]
    currency = data["data"]["currency"]
    
    transformed_data = CryptoPrice(
        price = price,
        cryptocurrency = criptocurrency,
        currency = currency,
        timestamp = datetime.now()
    )
    
    return transformed_data

def load_data_db(transformed_data):
    with Session() as session:
        session.add(transformed_data)
        session.commit()
    
if __name__ == "__main__":
    while True:
        # Extract
        data = extract_data_from_api()
        
        # Transform
        transformed_data = transform_data(data)
        
        # Load
        load_data_db(transformed_data)
        
        print("Dados carregados!")
        sleep(15)