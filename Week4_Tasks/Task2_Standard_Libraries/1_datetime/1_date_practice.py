import datetime

# 1) datetime.date(y,m,d) -> display a date

date = datetime.date(2004,4,10)
print(date)

# 2) datetime.date.today() -> today date

tday = datetime.date.today()

print(tday) # returns whole date
print(tday.year) # returns year
print(tday.weekday())  # weekday() follows [monday-0 .... sunday-6]
print(tday.isoweekday()) # isoweekday() follows [monday-1 .... sunday-7]

# 3) date.timedelta() -> difference b/w dates or times

tdelta = datetime.timedelta(days=7)
bday = datetime.date(2027,4,10)

print(tday + tdelta) # 7 days from now
print(tday - tdelta) # 7 days before from now


till_bday = bday-tday   
print(till_bday.days) # no of days between the two days but include (start/end) not both 
print(till_bday.total_seconds()) # returns total seconds between the days

