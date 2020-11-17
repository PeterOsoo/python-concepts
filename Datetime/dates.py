import datetime
import pytz

# Naive
d = datetime.date(2020, 11, 17)
print(d)

# today
tday = datetime.date.today()
# print(tday)

# timedelta
tdelta = datetime.timedelta(hours=32)
# print(tday + tdelta)


dt = datetime.datetime.today()
dtnow = datetime.datetime.now()
# print(dir(datetime.datetime))
# print(dt)
# print(dtnow)

# pytz for time zones
dt = datetime.datetime(2020, 7, 19, 16, 30, 45, tzinfo=pytz.UTC)
# print(dir(dt))
print(dt)


dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

# to print time locally in Nairobi
dt_mtn = dt_utcnow.astimezone(pytz.timezone('Africa/Nairobi'))
print(dt_mtn)
