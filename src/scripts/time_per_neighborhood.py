from src.features.time_per_neighborhood import *
from src.features.filter_by_timerange import *

def getTimePerNeighborhood():
    DSTs = filterByTimerange('2022-02-10', '2022-02-19')
    time = timePerNeighborhood(DSTs)
    return time