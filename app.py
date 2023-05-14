from src.features.filter_by_timerange import *
from src.features.pollution_by_neighborhood import *
from src.features.pollution_by_neighborhood_by_days import *


from src.visualization.bar_graph import *
from src.visualization.bar_graph_by_days import *

# DSTs = filterByTimerange(unique=True)

# pollutionDfs = findPollutionByNeighborhood(DSTs)

# plotCO2BarGraph(pollutionDfs)
# plotCOBarGraph(pollutionDfs)
# plotNoxBarGraph(pollutionDfs)

DSTs = filterByTimerange(unique=False)

df_means = findPollutionByNeighborhoodByDays(DSTs)

barGraphByDays(df_means)

print('success!')


