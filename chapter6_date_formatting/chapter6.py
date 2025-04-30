# time between two date-times
from datetime import datetime
a = datetime(2016,10,6,0,0,0)
b = datetime(2016,10,1,23,59,59)
a-b
days =     (a-b).days
totalSecond = (a-b).total_seconds()
print(days)
print(totalSecond)

datetime_for_string = datetime(2016,10,1,0,0)
datetime_string_format = '%b %d %Y, %H:%M:%S'
datetime.strftime(datetime_for_string,datetime_string_format)
# Oct 01 2016, 00:00:00
#Section 6.3: Parsing string to datetime object
#Uses C standard format codes.

datetime_string = 'Oct 1 2016, 00:00:00'
datetime_string_format = '%b %d %Y, %H:%M:%S'
datetime.strptime(datetime_string, datetime_string_format)
# datetime.datetime(2016, 10, 1, 0, 0)
