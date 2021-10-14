"""
#
# File : func_scope_3.py
# Created ：10/10/2021 21:41
# Author ：R.G. Lennon
# Version ：v1.0.0
# Licencing : (C) 2021 Rodrigo V. Lima, LYIT
# Available under GNU Public License (GPL)
# Description ：Functions Called or not
"""

def overloading_sample(num_1, num_2=10):
  
    total_inner = num_1+num_2
    print(total_inner)
    return total_inner


if __name__ == '__main__':
    total = overloading_sample(99,1000)
    print(f"in main, total is {total}")
    total = overloading_sample(50)
    print(f"in main, total is {total}")

def multi_samvple(num_1, num_2=10):
    num_1 = num_1 * 2
    num_2 = 123
    return num_1, num_2

def list_rtn_sample2(list1):
    list1 = list1 * 2
    return list1


def list_rtn_sample():
    ages = [19,21,20]
    return ages


if __name__ == '__main__':
    val_1, val_2 = multi_samvple(4,6)
    print(f"value 1{val_1} and value 2 {val_2}")
    print(f"full return was {multi_samvple(12,14)}")
    print(f"list example {list_rtn_sample()}")
    print(list_rtn_sample2([1,2,3]))

