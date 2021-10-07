empty_list = [] # Create an empty list

empty_list.append(10) #using an index won’t work until the items are added
ages = [19, 21, 20] # A named list with comma separated values
student1_details = [20, "Michael Brennan", 77.5] # Lists can hold a variety of data types
student2_details = [33, "Mairead Gallagher", 65]
class_of_students = [student1_details, student2_details, "module  title", [2, 3, 4]]
group_of_students = student1_details + student2_details  #creates 1 newlist with contents of previous two
       # [20, 'Michael Brennan', 77.5, 33, 'Mairead Gallagher', 65]


'''Print list examples'''

print("{}".format(ages[1]))
print("{0} \t\t{1} \t{2}".format(student1_details[0], student1_details[1], student1_details[2]))
print("{}".format(student1_details))
print("{}".format(class_of_students[0][1]))

'''Is item in list'''




