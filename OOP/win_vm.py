#
# File : oop.py
# Created ：10/10/2021 21:41
# Author ：R. Lima
# Version ：v1.0.0
# Licencing : (C) 2021 Rodrigo V. Lima, LYIT
# Available under GNU Public License (GPL)
# Description ：Oopv

from cls_pkg.vm_Class import VM

class WINVM(VM): #make winvm a child of vm class
    def __init__(self, vm_dept, patch):
        super(WINVM,self).__init__(3,"Pietra")  
        self.vm_dept = vm_dept  #unique instance
        self.patch = patch

    
    def print_dept(self):
        print(f"Dept: {self.vm_dept} patch {self.patch}")


    def __str__(self):
        #overriding the str method
        print(f"VM ID: {self.vm_id} , owner {self.vm_owner}")
        print(f"Dept: {self.vm_dept} patch {self.patch}")