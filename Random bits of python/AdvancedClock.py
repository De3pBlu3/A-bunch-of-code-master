import calendar
from datetime import datetime
import time
import os
os.system('clear')  # on linux / os x

var = 1

def dateandtime():
    var = 1
    while var == 1 :  # This constructs an infinite loop
        now = datetime.now()
        print (now.strftime("Time: %x, %X"))
        time.sleep(1)
        os.system('clear')  # on linux / os x

def realtime():
    var = 1
    while var == 1 :
        now = datetime.now()
        print (now.strftime("Time: %X"))
        time.sleep(1)
        os.system('clear')  # on linux / os x

def realdate():
    var = 1
    while var == 1 :
        now = datetime.now()
        print (now.strftime("Time: %x"))
        time.sleep(1)
        os.system('clear')  # on linux / os x


ans=True
while ans:
    print ("""
    1.Time & Date
    2.Time
    3.Date
    4.Exit/Quit
    """)
    ans=raw_input("What would you like to display? ")
    if ans=="1":
      os.system('clear')  # on linux / os x
      dateandtime()
      ans=False
    elif ans=="2":
      os.system('clear')  # on linux / os x
      realtime()
      ans=False
    elif ans=="3":
       os.system('clear')  # on linux / os x
       realdate()
       ans=False
    elif ans=="4":
      os.system('clear')  # on linux / os x
      print("Goodbye")
      time.sleep(1)
      os.system('clear')  # on linux / os x
      quit()
    elif ans !="":
      os.system('clear')
      print("\n Not Valid Choice, Try again")
