#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta # is a span of time

# construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))

# print today's date
now = datetime.now()
print("ahora es ", now)

# print today's date one year from now
print("un ano desde ahor sera"  + str(now + timedelta(days=365)))

# create a timedelta that uses more than one argument
print(
  "en tres semanas sera " +
  str(now + timedelta(weeks=3))
)

# calculate the date 1 week ago, formatted as a string
hace_una_semana = datetime.now() - timedelta(weeks=1)
s = hace_una_semana.strftime("%A %B %d %Y")
print("hace una semana, era", s)

### How many days until April Fools' Day?
hoy_dia = date.today()
april_fools = date(hoy_dia.year, 4, 1)


# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if april_fools < hoy_dia:
  print("April fools already went by %d days ago" % (hoy_dia - april_fools).days)
  april_fools = april_fools.replace(year = hoy_dia.year + 1)


# Now calculate the amount of time until April Fool's Day
time_to_april_fools = april_fools - hoy_dia
print("it's just ", time_to_april_fools, "'til april fools")

