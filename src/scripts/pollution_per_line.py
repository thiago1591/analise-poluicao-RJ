from src.features.filter_by_timerange import filterByTimerange
from src.features.pollution_per_line import *
from src.visualization.pollution_per_line import *

def getCo2PerLine():
    DSTs = filterByTimerange('2022-02-10', '2022-02-19')
    df = co2PerLine(DSTs)
    plotCo2PerLine(df, 3)

def getCoPerLine():
    DSTs = filterByTimerange('2022-02-10', '2022-02-19')
    df = coPerLine(DSTs)
    plotCoPerLine(df, 3)

def getNoxPerLine():
    DSTs = filterByTimerange('2022-02-10', '2022-02-19')
    df = noxPerLine(DSTs)
    plotNoxPerLine(df, 3)