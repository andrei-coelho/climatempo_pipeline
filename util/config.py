import json
from   sqlalchemy.orm import sessionmaker 
from   sqlalchemy     import create_engine

config = None

try:
    with open("conf.json", 'r') as conf:
        config = json.load(conf)
except FileNotFoundError:
    print("Arquivo conf.json não encontrado.")
except json.JSONDecodeError:
    print("Erro ao decodificar conf.json. Verifique a formatação do JSON.")

conn = f"mysql+pymysql://{config['database']['user']}:{config['database']['pass']}@{config['database']['link']}/{config['database']['name']}"
engine = create_engine(conn)

def get_session():
    return sessionmaker(bind=engine)

def get_api_data():
    return config['api']