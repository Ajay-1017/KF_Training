import datetime
import pytz # python time zone package

# 1) time with utc

# tz_t = datetime.datetime(2026,6,24,12,30,45,10000,tzinfo=pytz.utc)
# print(tz_t)

# ====================================================================

# 2) Get the current UTC time and convert it to Chennai (Asia/Kolkata) time using astimezone()

tz_now = datetime.datetime.now(tz=pytz.utc)
print(tz_now)


my_tz = tz_now.astimezone(pytz.timezone('Asia/kolkata'))
print(my_tz)

# 2a) Direct method to get the current date and time in the chennai(Asia/Kolkata) timezone

curr_time = datetime.datetime.now(pytz.timezone("Asia/kolkata"))
print(curr_time)

# ====================================================================

# 3) current utc time using utcnow()

# tz_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
# print(tz_utcnow)


# ====================================================================

# 4) print all timezones

# for tz  in pytz.all_timezones:
#     print(tz)

# ====================================================================


# 5) convert india to dubai time using localize()

# curr_time = datetime.datetime.now()
# chennai_time = pytz.timezone("Asia/kolkata")
# tz_chennai = chennai_time.localize(curr_time)

# print(tz_chennai)
# dubai = tz_chennai.astimezone(pytz.timezone("Asia/dubai"))
# print(dubai)

# ====================================================================

# 6) strftime -> convert datetime to string
dt= datetime.datetime.now(pytz.timezone("Asia/kolkata"))
print(dt.strftime('%B %d ,%Y'))

# 6a) strftime -> convert string to datetime

dt_str = datetime.datetime.strptime('June 26 ,2026','%B %d ,%Y')
print(dt_str)

# ====================================================================

