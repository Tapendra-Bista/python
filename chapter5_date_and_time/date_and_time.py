
from datetime import datetime
import pytz
from dateutil import tz
dt = datetime.strptime("2016-04-15T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")
newdt = datetime.now()
print(dt)
print(newdt)


local = tz.gettz() # Local time
PT = tz.gettz('US/Pacific') # Pacific time
dt_l = datetime(2015, 1, 1, 12, tzinfo=local) # I am in EST
dt_pst = datetime(2015, 1, 1, 12, tzinfo=PT)
dt_pdt = datetime(2015, 7, 1, 12, tzinfo=PT) # DST is handled automatically
print(dt_l)
# 2015-01-01 12:00:00-05:00
print(dt_pst)
# 2015-01-01 12:00:00-08:00
print(dt_pdt)




pt = pytz.timezone('US/Pacific')
print(pt)
dt_pst = pt.localize(datetime.now())
print(dt_pst)


# time
currentTime = datetime.now().time()
print(currentTime)



