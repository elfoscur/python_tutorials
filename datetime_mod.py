# https://www.coursera.org/learn/python-programming/supplement/OuShh/datetime-module-quick-reference

import datetime

date1 = datetime.date(2018, 2, 18)


print(date1)

today = datetime.date.today()

print(today)


print(date1 == today)
print(date1 > today)

difference = date1 - today

print(type(difference))  # timedelta object

print(difference.days, difference.seconds)

print(datetime.MINYEAR, datetime.MAXYEAR)  # 1 - 9999
