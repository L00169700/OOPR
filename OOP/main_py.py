#
# File : oop.py
# Created ：10/10/2021 21:41
# Author ：R. Lima
# Version ：v1.0.0
# Licencing : (C) 2021 Rodrigo V. Lima, LYIT
# Available under GNU Public License (GPL)
# Description ：Oop

from OOP.abc_cls import ABC_CLS
from OOP.win_vm import WINVM
from cls_pkg.vm_Class import VM

vm1 = VM(1, "Michael") # created an obj with the required init values
vm2 = VM(2,"Rodrigo")

vm1.print_vm_details()
vm2.print_vm_details()

vm1.print_total_vms()
vm2.print_total_vms()

print("\n")

vm3 = WINVM('QA', 'KB01020304054')
vm3.print_dept()
vm3.print_vm_details()
vm3.print_total_vms()

#vm3.__str__() overrriding method called in main

ABC_CLS.register(WINVM) #winvm now is seen ial also an implementation

ans=issubclass(WINVM, ABC_CLS)
print(f"winvmis now a subclass of ABS_CLS: {ans}")
ans=issubclass(VM, ABC_CLS)
print(f"winvmis now a subclass of ABS_CLS: {ans}")
ans=isinstance(vm3, ABC_CLS)


