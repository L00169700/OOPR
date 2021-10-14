"""
#
# File : screen_ex.py
# Created ：10/10/2021 21:41
# Author ：R.G. Lennon
# Version ：v1.0.0
# Licencing : (C) 2021 Rodrigo V. Lima, LYIT
# Available under GNU Public License (GPL)
# Description ：Functions Called or not
"""

num = 3
inc_by = 2

def increase_value(original_value, increment_by):
    print("inside method")
    print(f"original value {original_value} id {id(original_value)}")
    print(f"increment by{increment_by} id {id(increment_by)}")
    original_value+increment_by
    print(f"update version: {original_value} new id {id(original_value)}")


if  __name__ == '___main__':
    print("called in main")
    print(f"num {num} id {id(num)}")
    print(f"inc_by{id(inc_by)} inc_by id{id(inc_by)}")
    increase_value(num, inc_by)
    print("called main function")
    print(f"num {num} num id {id(num)}")
    print(f"inc_by {id(inc_by)} inc Id{id(inc_by)}")
