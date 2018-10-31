from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import os
os.system('clear')  # on linux / os x

print("Date & time calculater -- Don't enter nothing, enter 0")
raw_input("Press Enter to continue...")
os.system('clear')  # on linux / os x
now = datetime.now()
days = input("How many days to add: ")
os.system('clear')  # on linux / os x
hours = input("How many hours to add: ")
os.system('clear')  # on linux / os x
mins = input("How many minutes to add: ")
os.system('clear')  # on linux / os x

print("What time is is now: " + str(now))
print("")
print("Time calcuated: " + str(now + timedelta(days=days, hours=hours, minutes=mins)))
print("")
print("Time diffrence: Days:" + str(days) + " Hours:" + str(hours) + " Minutes:" + str(mins))
print("")
raw_input("Press Enter to continue...")
os.system('clear')  # on linux / os x
