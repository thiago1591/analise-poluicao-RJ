import pandas as pd
import sys

def filterByTimerange():
    # if(sys.argv.length == 0):
    #     getAll()
    # else:
    #     ...


    #getting the first day for now    
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
