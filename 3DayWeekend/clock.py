import calendar
from datetime import datetime
import time
import os
os.system('clear')  # on linux / os x

def realtime():
    now = datetime.now()
    print (now.strftime("Time: %x, %X"))


try:
    while True:
        realtime()
        time.sleep(1)
except KeyboardInterrupt:
    print('Manual break by user')
