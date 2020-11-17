# Datetime Module - How to work with Dates, Times, Timedeltas, and Timezones


import datetime
# import pytz

# Naive
d = datetime.date(2020, 11, 17)
print(d)

# today
tday = datetime.date.today()
print(tday)


# weekday() - Monday is 0 and Sunday is 6
# print(tday)

# isoweekday() - Monday is 1 and Sunday is 7
# print(tday)


# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

tdelta = datetime.timedelta(hours=12)

# print(tday + tdelta)

# date2 = date1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(1990, 7, 19)

till_bday = tday - bday

# print(till_bday.days)


# datetime.time
t = datetime.time(9, 30, 45, 100000)


# dt = datetime.datetime.today()
# dtnow = datetime.datetime.now()
# print(dir(datetime.datetime))
# print(dt)
# print(dtnow)


# pytz for time zones
dt = datetime.datetime(2020, 7, 19, 16, 30, 45, tzinfo=pytz.UTC)
# print(dir(dt))
print(dt)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

dt_utcnow2 = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(dt_utcnow2)

# for tz in pytz.all_timezones:
#     print(tz)

# to print time locally in Nairobi
dt_mtn = dt_utcnow.astimezone(pytz.timezone('Africa/Nairobi'))
print(dt_mtn)

dt_mtn = datetime.datetime.now()

mtn_tz = pytz.timezone('US/Mountain')
dt_mtn = mtn_tz.localize(dt_mtn)

# print(dt_mtn)

dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
# print(dt_east)

# print(dt_mtn.strftime('%B %d, %Y'))

dt_str = 'July 19, 2020'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

# strftime - Datetime to String
# strptime - String to Datetime


