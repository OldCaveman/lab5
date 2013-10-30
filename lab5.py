import csv
import datetime
from gdd import calculate


with open("Caven_Tullydata.csv") as infile:
    reader = csv.reader(infile)
    high = -1000
    low = 1000
    last_day = None
    for row in reader:
        # TODO: extract the date's high and low temps
        date = datetime.datetime.strptime(row[0][0:10], "%Y-%m-%d")
        temp = float(row[1])
        if temp > high:
            high = temp
        if temp < low:
            low = temp
        if date != last_day:
            value = calculate(high, low, base=50)
            print value
        # Do something with calculate(high, low, base=10)
        pass
