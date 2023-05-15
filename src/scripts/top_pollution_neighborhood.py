

from src.features.pollution_by_neighbordhood import *
from src.features.filter_by_timerange import *
from src.visualization.pollution_by_neighborhood import *

def top3Co2Neighbordhood():
    DSTs = filterByTimerange('2022-02-10', '2022-02-19')

    df_means = co2ByNeighbordhood(DSTs)

    plotTopCo2Neighbordhood(df_means['co2_mean'], 3)

def top10Co2Neighbordhood():
    DSTs = filterByTimerange('2022-02-10', '2022-02-19')

    df_means = co2ByNeighbordhood(DSTs)

    plotTopCo2Neighbordhood(df_means['co2_mean'], 10)

def top3Co2NeighbordhoodInWeekend():
    DSTs = filterByTimerange('2022-02-12', '2022-02-13')

    df_means = co2ByNeighbordhood(DSTs)

    plotTopCo2NeighbordhoodWeekend(df_means['co2_mean'], 3)

def top3Co2NeighbordhoodInWeek():
    DSTs = filterByTimerange('2022-02-14', '2022-02-18')

    df_means = co2ByNeighbordhood(DSTs)

    plotTopCo2NeighbordhoodWeek(df_means['co2_mean'], 3)

def top3Co2NeighbordhoodCompareWeekAndWeekend():
    DSTsWeekend = filterByTimerange('2022-02-12', '2022-02-13')
    DSTsWeek = filterByTimerange('2022-02-14', '2022-02-18')

    df_weekend_means = co2ByNeighbordhood(DSTsWeekend)
    df_week_means = co2ByNeighbordhood(DSTsWeek)

    df_means = plotTopCo2NeighbordhoodCompareWeekAndWeekend(df_weekend_means['co2_mean'], df_week_means['co2_mean'], 3)

