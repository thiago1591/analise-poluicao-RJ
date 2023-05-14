import pandas as pd
from src.utils.get_timerange import *

def filterByTimerange(initial_date: str, end_date: str):
    arquivos = datesBetween(initial_date, end_date)
    arquivos = ['G1-2022-02-13.parquet', 'G1-2022-02-14.parquet', 'G1-2022-02-15.parquet', 'G1-2022-02-16.parquet', 'G1-2022-02-17.parquet', 'G1-2022-02-18.parquet', 'G1-2022-02-19.parquet']

    dstAs = [pd.read_parquet('dataset/DST-A/' + arquivo) for arquivo in arquivos]
    dstBs = [pd.read_parquet('dataset/DST-B/' + arquivo) for arquivo in arquivos]
    dstDs = [pd.read_parquet('dataset/DST-D/' + arquivo) for arquivo in arquivos]
    dstEs = [pd.read_parquet('dataset/DST-E/' + arquivo) for arquivo in arquivos] 
    
    return {
        "dstA": dstAs,
        "dstB": dstBs,
        "dstD": dstDs,
        "dstE": dstEs
    }
        
