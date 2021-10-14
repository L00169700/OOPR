empty_list = [] # Create an empty list

empty_list.append(10) #using an index won’t work until the items are added
ages = [19, 21, 20] # A named list with comma separated values
student1_details = [20, "Michael Brennan", 77.5] # Lists can hold a variety of data types
student2_details = [33, "Mairead Gallagher", 65]
class_of_students = [student1_details, student2_details, "module  title", [2, 3, 4]]
group_of_students = student1_details + student2_details  #creates 1 newlist with contents of previous two
       # [20, 'Michael Brennan', 77.5, 33, 'Mairead Gallagher', 65]


print("{}".format(class_of_students[3][2]))
#index out of range if [4][0]

ages[1] = 33
print("{} \n".format(ages[1]))

group_of_students = class_of_students[0:2]
print(group_of_students)
print("1st student, 2nd datum is : {0}".format(group_of_students[0][1]))


second_group_of_students=student1_details+student2_details #joining two lists
third_group_of_students=[] # create an empty list
third_group_of_students+=second_group_of_students #add second group to existing contents of third group

print("Is Michael in list? {}".format(("Michael" in group_of_students[0][1])))
print("Is Michael in list? {}".format(("Michael" in group_of_students[0]))) #why is it different?