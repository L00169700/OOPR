"""
#
# File : func_1.py
# Created ：10/10/2021 21:41
# Author ：R.G. Lennon
# Version ：v1.0.0
# Licencing : (C) 2021 Rodrigo V. Lima, LYIT
# Available under GNU Public License (GPL)
# Description ：Functions Called or not
"""


def print_hi(student_name):
    print(f"Hello {student_name}!")


if __name__ == "__main__":
    '''....'''
    print_hi("Dian")

print("I print anyway")


def print_lnum(lnum):
 """
 Prints a welcome message.
 Demonstrates passing a variable into a function
  Parameters:
 lnum LYIT lnumber of student
 Returns:
 none
 """
 print(f'Hi, {lnum}')
 return


 def print_name(student_name):
    fname, lname = str(student_name).split(" ")
    print(f'Hi {fname} {lname}, welcome to LYIT!')
    return

 if __name__ == '__main__':
    print_name('Ruth Lennon') # Call the print_name function
 # print_lnum is not called so do not print details

