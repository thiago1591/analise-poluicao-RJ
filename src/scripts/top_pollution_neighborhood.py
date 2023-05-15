

from src.features.pollution_by_neighbordhood import *
from src.features.filter_by_timerange import *
from src.visualization.pollution_by_neighborhood import *

def top3Co2Neighbordhood():
    DSTs = filterByTimerange('2022-02-10', '2022-02-19')

    df_means = pollutionByNeighbordhood(DSTs)

    plotTopCo2Neighbordhood(df_means['co2_mean'], 3)

def top10Co2Neighbordhood():
    DSTs = filterByTimerange('2022-02-10', '2022-02-19')

    df_means = pollutionByNeighbordhood(DSTs)

    plotTopCo2Neighbordhood(df_means['co2_mean'], 10)

def top3Co2NeighbordhoodInWeekend():
    DSTs = filterByTimerange('2022-02-12', '2022-02-13')

    df_means = pollutionByNeighbordhood(DSTs)

    plotTopCo2NeighbordhoodWeekend(df_means['co2_mean'], 3)

def top3Co2NeighbordhoodInWeek():
    DSTs = filterByTimerange('2022-02-14', '2022-02-18')

    df_means = pollutionByNeighbordhood(DSTs)

    plotTopCo2NeighbordhoodWeek(df_means['co2_mean'], 3)

def top3Co2NeighbordhoodCompareWeekAndWeekend():
    DSTsWeekend = filterByTimerange('2022-02-12', '2022-02-13')
    DSTsWeek = filterByTimerange('2022-02-14', '2022-02-18')

    df_weekend_means = pollutionByNeighbordhood(DSTsWeekend)
    df_week_means = pollutionByNeighbordhood(DSTsWeek)

    plotTopCo2NeighbordhoodCompareWeekAndWeekend(df_weekend_means['co2_mean'], df_week_means['co2_mean'], 3)

def top3CoNeighbordhood():
    DSTs = filterByTimerange('2022-02-10', '2022-02-19')

    df_means = pollutionByNeighbordhood(DSTs)

    plotTopCoNeighbordhood(df_means['co_mean'], 3)

def top3CONeighbordhoodInWeekend():
    DSTs = filterByTimerange('2022-02-12', '2022-02-13')

    df_means = pollutionByNeighbordhood(DSTs)

    plotTopCoNeighbordhoodWeekend(df_means['co_mean'], 3)

def top3NoxNeighbordhoodInWeek():
    DSTs = filterByTimerange('2022-02-14', '2022-02-18')

    df_means = pollutionByNeighbordhood(DSTs)

    plotTopCo2NeighbordhoodWeek(df_means['nox_mean'], 3)

def top3NoxNeighbordhood():
    DSTs = filterByTimerange('2022-02-10', '2022-02-19')

    df_means = pollutionByNeighbordhood(DSTs)

    plotTopNoxNeighbordhood(df_means['nox_mean'], 3)

def top3NoxNeighbordhoodInWeekend():
    DSTs = filterByTimerange('2022-02-12', '2022-02-13')

    df_means = pollutionByNeighbordhood(DSTs)

    plotTopNoxNeighbordhoodWeekend(df_means['nox_mean'], 3)

def top3NoxNeighbordhoodInWeek():
    DSTs = filterByTimerange('2022-02-14', '2022-02-18')

    df_means = pollutionByNeighbordhood(DSTs)

    plotTopNoxNeighbordhoodWeek(df_means['nox_mean'], 3)