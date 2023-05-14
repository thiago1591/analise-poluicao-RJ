from datetime import datetime, timedelta

def datesBetween(initial_date, end_date):
    initial_date = datetime.strptime(initial_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    dates_between = []

    current_date = initial_date
    while current_date <= end_date:
        dates_between.append("G1-" + current_date.strftime('%Y-%m-%d') + ".parquet")
        current_date += timedelta(days=1)

    

    return dates_between