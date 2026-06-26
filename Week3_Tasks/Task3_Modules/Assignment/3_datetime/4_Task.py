
# 3) Display the current date, time, and weekday.

import datetime

curr_date_time = datetime.datetime.today()

print("curr_date :",curr_date_time.date())
print("curr_time :",curr_date_time.time())
print("curr_day :",curr_date_time.strftime("%A"))
