#  -moduels= those moduels which comes directly with python installation.

# random
# datetime
# urllink


# random

import random
# print(dir(random))

# print(random.random()) # random floating value between 0 and 1
# print(random.randint(100000,999999))
# print(random.randrange(100000,999999))
# print(random.randrange(100000,999999,3))



# a=["swiggy50","swiggy2020","swiggy2030","swiggy4567","swiggy3456"]
# print(random.choice(a))

# print(random.choices(a, k=2))

# enter user name :ramesh
# password: Ramesh@3w3

# import datetime
from datetime import datetime,timedelta
# print(dir(datetime))
now_date=datetime.now()
# print(now_date)

# now_utc_date=datetime.utcnow()
# print(now_utc_date)
# print(type(now_date))
# print(now_date.date())
# print(now_date.time())
# print(now_date.date().day)
# print(now_date.time().hour)
# after_30days=now_date + timedelta(days=30)
# print(after_30days)

# after_20min=now_date+timedelta(minutes=12)
# print(after_20min)

# strftime (this is for converting python datetime to string)
# strp   (this is for converting into python datetime)
# converted_date=now_date.strftime('%y-%d-%m  %A %w %B %p'  )
# print(converted_date)


# strptime()

# str_date="23 nov 2022 11:04 Am"   # subscption start date.
# converted_date=datetime.strptime(str_date,'%d %b %Y %I: %M %p')
# print(converted_date)

# convert_datetime=now_date.strftime('%y %d %M %A %p')
# print(convert_datetime)

# urlib

# import urllib.request

# bata=urllib.request.urlopen("https://www.python.org/downloads/windows/")
# print(bata)
# print(bata.code)
# print(bata.read())
# ptint(alooo)






