from src.features.filter_by_timerange import filterByTimerange
from src.features.co2_per_line import *
from src.visualization.pollution_per_line import *

def getCo2PerLine():
    DSTs = filterByTimerange('2022-02-10', '2022-02-19')
    df = co2PerLine(DSTs)
    plotCo2PerLine(df, 3)

    return df