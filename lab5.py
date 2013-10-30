import csv
import datetime
from gdd import calculate


with open("Caven_Tullydata.csv") as infile:
    reader = csv.reader(infile)
    high = -1000
    low = 1000
    last_day = None
    value = 0
    for row in reader:
        # TODO: extract the date's high and low temps
        date = datetime.datetime.strptime(row[0][0:10], "%Y-%m-%d")
        if len(row) > 1:
            temp = float(row[1])
            if temp > high:
                high = temp
            if temp < low:
                low = temp
        if date != last_day:
            if date.date() > datetime.date(2007, 1, 1):
                value += calculate(high, low, base=50)
                print value
            #reset values for next day
            if last_day != None and date.date().year != last_day.date().year:
                value = 0
            last_day = date
            high = -1000
            low = 1000
            
