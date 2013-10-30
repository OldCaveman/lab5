import csv
import datetime
from gdd import calculate


with open("Caven_Tullydata.csv") as infile:
    reader = csv.reader(infile)
    high = max
    for row in reader:
        # TODO: extract the date's high and low temps
        date = datetime.strptime(row[0], "%Y-%m-%d")
        print date
        # Do something with calculate(high, low, base=10)
        pass
