#!/usr/bin/env python3

# Project:   python-meatball
# Copyright: (c) 2021, Rye Miller

import random
import time
from datetime import datetime

odds = [
    1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23,
    25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45,
    47, 49, 51, 53, 55, 57, 59
]

right_this_minute = datetime.today().minute

for i in range(5):
    if right_this_minute in odds:
        print("This minute seems a little odd")
    else:
        pass
        print("Not an odd minute at all!")

    wait_time = random.randint(1, 60)
    time.sleep(wait_time)
