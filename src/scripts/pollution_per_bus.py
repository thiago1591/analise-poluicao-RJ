from src.features.co2_per_busID import co2PerBusID
from src.features.filter_by_timerange import filterByTimerange
from src.visualization.pollution_per_bus import plotCo2PerBus

def getCo2PerBus():
    DSTs = filterByTimerange('2022-02-10', '2022-02-19')
    df = co2PerBusID(DSTs)
    plotCo2PerBus(df, 3)