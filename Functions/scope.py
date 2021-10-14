"""
#
# File : scope.py
# Created ：10/10/2021 21:41
# Author ：R.G. Lennon
# Version ：v1.0.0
# Licencing : (C) 2021 Rodrigo V. Lima, LYIT
# Available under GNU Public License (GPL)
# Description ：Functions Called or not
"""

def overloading_sample(num_1, num_2=10):
    total = 0 #this is a local var
    total = num_1+num_2
    print(total)
    return


total = 0
overloading_sample(99,10000)
overloading_sample(50)
print(total)

