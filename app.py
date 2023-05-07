from src.features.filter_by_timerange import *
from src.features.pollution_by_neighborhood import *

from src.visualization.bar_graph import *

DSTs = filterByTimerange()
pollutionDfs = findPollutionByNeighborhood(DSTs)


plotCO2BarGraph(pollutionDfs)
# plotCOBarGraph(pollutionDfs)
# plotNoxBarGraph(pollutionDfs)

print('success!')
