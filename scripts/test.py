import sys
import os

from src.features import filter_by_timerange


DSTs = filter_by_timerange('2022-02-10', '2022-02-10')

# df_means = co2_by_neighbordhood(DSTs)

# plotTopCo2NeighbordhoodWeekend(DSTs['co2_mean'], 3)

