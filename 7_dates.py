#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime # imports standard modules



def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()

  print('la fecha es ', today)

  # print out the date's individual components
  print('components::', today.month, today.day, today.year)

  # retrieve today's weekday (0=Monday, 6=Sunday)
  days = [
    'monda',
    'tuesday',
    'wednesday',
    'thursday',
    'friday',
    'saturday',
    'sunday'
  ]
  print('today\'s weekday number is', today.weekday()) # => 6
  print('which is', days[today.weekday()])

  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  currentDate = datetime.now()
  print(currentDate)

  # Get the current time
  time = datetime.time(currentDate)
  print('la hora es', time)



if __name__ == "__main__":
  main();
