#
# File : oop.py
# Created ：10/10/2021 21:41
# Author ：R.G. Lennon
# Version ：v1.0.0
# Licencing : (C) 2021 Rodrigo V. Lima, LYIT
# Available under GNU Public License (GPL)
# Description ：Oop


class VM:
    vm_num=0

    def __init__(self, vm_id, vm_owner):
        self.vm_id = vm_id
        self.vm_owner = vm_owner
        VM.vm_num+=1

    
    def print_total_vms(self):
        print(f"there are {VM.vm_num} vms in use")


    def print_vm_details(self):
        print(f"VM ID: {self.vm_id} , owner {self.vm_owner}")