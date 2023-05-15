from src.features.pollution_per_busID import *
from src.features.filter_by_timerange import *
from src.visualization.pollution_per_bus import *

def getCo2PerBus():
    DSTs = filterByTimerange('2022-02-10', '2022-02-19')
    df = co2PerBusID(DSTs)
    plotCo2PerBus(df, 3)

def getCoPerBus():
    DSTs = filterByTimerange('2022-02-10', '2022-02-19')
    df = coPerBusID(DSTs)
    plotCoPerBus(df, 3)

def getNoxPerBus():
    DSTs = filterByTimerange('2022-02-10', '2022-02-19')
    df = noxPerBusID(DSTs)
    plotNoxPerBus(df, 3)