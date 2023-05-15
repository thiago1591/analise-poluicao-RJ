from src.scripts.pollution_per_bus import *
from src.scripts.top_pollution_neighborhood import *
from src.scripts.time_per_neighborhood import *
from src.scripts.pollution_per_line import *

def main():
    reportRequestList = [8]
    generateReport(reportRequestList)
  
def generateReport(reportRequestList):
    if 0 in reportRequestList:
        top3Co2Neighbordhood()
    if 1 in reportRequestList:
        top3Co2NeighbordhoodInWeekend()
    if 2 in reportRequestList:
        top3Co2NeighbordhoodInWeek()
    if 3 in reportRequestList:
        getCo2PerLine()
    if 4 in reportRequestList:
        getCo2PerBus()
    if 5 in reportRequestList:
        getCoPerBus()
    if 6 in reportRequestList:
        getNoxPerBus()
    if 7 in reportRequestList:
        getCoPerLine()
    if 8 in reportRequestList:
        getNoxPerLine()


main()
print('success!')


