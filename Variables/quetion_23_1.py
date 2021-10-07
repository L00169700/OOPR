python_mission = """The mission of the Python Software Foundation is to promote, protect, 
and advance the Python programming language, and to support and facilitate 
the growth of a diverse and international community of Python programmers"""

print(python_mission.count("s",0,len(python_mission)))
print(python_mission.count("s",0,len(python_mission)))
print("The word returned is: {}".format(python_mission[25:34]))

print(python_mission.count("diverse",0,len(python_mission)))

string_is_a_number = "123455"
print(string_is_a_number.isnumeric())

drive = "C:"
divisory = "\\"
user= "user"
folder1 = "ndarby"
folder2 = "python3"
folder3 = "python-3-3-3"
folder4 = "bin"

print(drive + divisory + user +divisory+ folder1+divisory+folder2+divisory+folder3+divisory+folder4)


suffix_no = 1122
answer=input("Please provide your number  ")
print("Your answer was:{0}".format(answer))
start_l = "L"

s =0
for i in answer:
    s += 1

remaining_numbers = 8 - s
print(s)
print(remaining_numbers)
print("{0}{1}{2}".format(start_l,answer,"0"*remaining_numbers))



