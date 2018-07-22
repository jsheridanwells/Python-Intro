#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes
  ahora = datetime.now()

  #### Date Formatting ####

  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
  print(ahora.strftime("the current year is: %Y")) # => 2018
  print(ahora.strftime("%a, %d, %B, %y")) # => sun, 22, July, 18


  # %c - locale's date and time, %x - locale's date, %X - locale's time
  print(ahora.strftime("locale date and time: %c")) # =>  uses current locale
  print(ahora.strftime("locale date: %x")) # =>
  print(ahora.strftime("locale time: %X")) # =>


  #### Time Formatting ####

  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
  print(ahora.strftime("current time: %I %M %S %p"))
  print(ahora.strftime("24-hour time: %H %M"))



if __name__ == "__main__":
  main();
