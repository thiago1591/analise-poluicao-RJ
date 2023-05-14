import pandas as pd
import sys

def filterByTimerange(unique):
        if unique==True: 
            dst0 = pd.read_parquet("dataset/DST-0/G1-2022-02-10.parquet")
            dstA = pd.read_parquet("dataset/DST-A/G1-2022-02-10.parquet")
            dstB = pd.read_parquet("dataset/DST-B/G1-2022-02-10.parquet")
            dstC = pd.read_parquet("dataset/DST-C/G1-2022-02-10.parquet")
            dstD = pd.read_parquet("dataset/DST-D/G1-2022-02-10.parquet")
            dstE = pd.read_parquet("dataset/DST-E/G1-2022-02-10.parquet")
            return {
                "dst0": dst0,
                "dstA": dstA,
                "dstB": dstB,
                "dstC": dstC,
                "dstD": dstD,
                "dstE": dstE
            }
        else:
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
             
