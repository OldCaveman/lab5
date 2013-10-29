import csv
import datetime
from gdd import calculate


with open("Caven_Tullydata.csv") as infile:
    reader = csv.reader(infile)
    for row in reader:
        # TODO: extract the date's high and low temps
        # Do something with calculate(high, low, base=10)
        pass
