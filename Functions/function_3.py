"""
#
# File : function_3.py
# Created ：10/10/2021 21:41
# Author ：R.G. Lennon
# Version ：v1.0.0
# Licencing : (C) 2021 Rodrigo V. Lima, LYIT
# Available under GNU Public License (GPL)
# Description ：Functions Called or not
"""

def change_list(sample_list):
    sample_list = [99,98,96,97]
    print(f"sample list {sample_list}")


def main():
    sample_list = [1,2,3,4,5]
    print(f"sample of list before {sample_list}")
    change_list(sample_list)
    print(f"sample of list after {sample_list}")

main()
