import pandas as pd
from src.utils.get_timerange import *
from src.utils.map_cod_bairro_to_nome_bairro import *

def filterByTimerange(initial_date: str, end_date: str):
    arquivos = datesBetween(initial_date, end_date)

    dstAs = [pd.read_parquet('dataset/DST-A/' + arquivo) for arquivo in arquivos]
    dstBs = [pd.read_parquet('dataset/DST-B/' + arquivo) for arquivo in arquivos]
    dstDs = [pd.read_parquet('dataset/DST-D/' + arquivo) for arquivo in arquivos]
    dstEs = [pd.read_parquet('dataset/DST-E/' + arquivo) for arquivo in arquivos] 

    dstBs = addNeighborhoodName(dstBs)
    
    return {
        "dstA": dstAs,
        "dstB": dstBs,
        "dstD": dstDs,
        "dstE": dstEs
    }
        
