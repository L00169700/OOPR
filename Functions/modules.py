"""
#
# File : modules.py
# Created ：10/10/2021 21:41
# Author ：R.G. Lennon
# Version ：v1.0.0
# Licencing : (C) 2021 Rodrigo V. Lima, LYIT
# Available under GNU Public License (GPL)
# Description ：Functions Called or not
"""

import random # import the random module
import os #import the operatiing ssystem
import sys #import standart output
import math # for common mathematical functions


for i in range(5):
    print(random.randint(1,10))

env_tup = tuple(os.environ)

for i in range(5):
    sys.stdout.write(f"{env_tup[i]}") # print without new line


print(f"the factorial of 4 is (1x2x3x4) {math.factorial(4)}")
print(f"mathematics value pi is {math.pi}")

