empty_list = [] # Create an empty list

empty_list.append(10) #using an index won’t work until the items are added
ages = [19, 21, 20] # A named list with comma separated values
student1_details = [20, "Michael Brennan", 77.5] # Lists can hold a variety of data types
student2_details = [33, "Mairead Gallagher", 65]
class_of_students = [student1_details, student2_details, "module  title", [2, 3, 4]]
group_of_students = student1_details + student2_details  #creates 1 newlist with contents of previous two
       # [20, 'Michael Brennan', 77.5, 33, 'Mairead Gallagher', 65]

grades=[1,2,3]
nu_grades=[grades]*2 #note the square brackets around the list name
print("{}".format(nu_grades))
nu_grades[0][0]=6
print("Repeated list after change {}".format(nu_grades)) #note that the 6 appears in both elements!
