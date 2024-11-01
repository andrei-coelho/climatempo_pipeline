from src.clima_model import *
from util.config import get_session
from datetime import datetime, timedelta 


def save_data_clima(clima:ClimaDetalhado|ClimaResumoDiario):
    session = get_session()
    session.add(clima)
    session.commit()
    session.close()

def get_rows_clima_detalhado(dia:DateTime):
    
    session = get_session()
    
    dia_inicio = datetime.combine(dia, datetime.min.time())
    dia_fim = datetime.combine(dia, datetime.max.time())

    res = session.execute("select * from clima_detalhado where data_hora >= :dia_inicio and data_hora <= :dia_fim ", {
        "dia_inicio":dia_inicio,
        "dia_fim":dia_fim
    })

    registros = res.fetchall()
    session.close()
    return registros 