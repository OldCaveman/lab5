import csv
import datetime
from gdd import calculate

eventdates = (5/16/2008, 5/5/2008, 4/22/2008, 4/19/2008, 4/18/2008, 4/4/2008, 7/9/2007, 7/12/2007, 7/9/2007, 7/3/2007, 7/10/2007, 6/14/2007, 6/10/2007, 5/25/2007, 5/30/2007, 5/29/2007, 5/17/2007, 5/17/2007, 5/20/2007, 5/12/2007, 5/12/2007, 5/12/2007, 5/7/2007, 4/8/2007) 



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
            if date.date() > datetime.date(2006, 1, 1):
                value += calculate(high, low, base=50)
                print value
            #reset values for next day
            if last_day != None and date.date().year != last_day.date().year:
                value = 0
            last_day = date
            high = -1000
            low = 1000
            
