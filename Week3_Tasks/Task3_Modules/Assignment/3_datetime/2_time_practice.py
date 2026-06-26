import datetime
# ====================================================================
# 1) datetime.time

# datetime.time(hr,min,sec,micro sec) -> display a time
t = datetime.time(12,30,45,10000)
print(t)

# ====================================================================

# 2) datetime.datetime

# 2a) datetime.datetime(y,m,d,hr,min,sec,micro sec) -> display both date and time

dt = datetime.datetime(2004,4,10,9,25,43,80000)
print(dt)

# 2b) datetime.timedelta(days=,hours=,etc...)
dt = datetime.datetime(2026,6,24,12,30,45,10000)
dt_delta= datetime.timedelta(hours=12)
print(dt + dt_delta)

# 2c) today vs now vs utcnow

today = datetime.datetime.today()
print(today) # returns current local datetime with timezone of none

# from datetime import datetime, timezone, timedelta
# IST = timezone(timedelta(hours=5, minutes=30))
# print(datetime.now(IST)) # gives us an option to pass timezone 

utc_now = datetime.datetime.utcnow()
print(utc_now) # gives current utc time but tz info still set to null 


# ====================================================================

