from src.features.filter_by_timerange import *
from src.features.pollution_by_neighborhood import *
from features.co2_by_neighbordhood import *
from src.features.co2_per_busID import *
from src.features.co2_per_line import *

from src.visualization.bar_graph import *
from src.visualization.bar_graph_by_days import *

DSTs = filterByTimerange(unique=False)

df_means = co2ByNeighbordhood(DSTs)
bus_lines = co2PerLine(DSTs)
barGraphByDays(df_means)

print('success!')


