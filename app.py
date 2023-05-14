from src.features.filter_by_timerange import *

from src.features.pollution_by_neighborhood import *
from src.features.co2_by_neighbordhood import *
from src.features.co2_per_busID import *
from src.features.co2_per_line import *
from src.features.busID_by_neighbordhood import *
from src.features.registers_by_neighborhood import *
from src.features.time_per_neighborhood import *

from src.visualization.bar_graph import *
from src.visualization.bar_graph_by_days import *

DSTs = filterByTimerange('2022-02-10', '2022-02-10')

#df_means = co2ByNeighbordhood(DSTs)
#bus_lines = co2PerLine(DSTs)
#bus_ids = busIDByNeighbordhood(DSTs, 'Maré')
#number = registersByNeighborhood(DSTs, 'Ricardo de Albuquerque')
#barGraphByDays(df_means)
time = timePerNeighborhood(DSTs, 'Engenheiro Leal')
print(time)
print('success!')


