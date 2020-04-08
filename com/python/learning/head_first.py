from datetime import datetime
from os import getcwd
import time
import random

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57,
        59]
where_am_i = getcwd()
print("You are at :", where_am_i)
for counter in range(5):
    current_second = datetime.today().second
    if current_second in odds:
        print("This second seems odd!")
    else:
        print("Not a odd second!")
    time.sleep(random.randint(2, 6))
