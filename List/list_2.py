grades=[1,2,3]
nu_grades=[grades]*2 #note the square brackets around the list name
print("{}".format(nu_grades))
nu_grades[0][0]=6
print("Repeated list after change {}".format(nu_grades)) #note that the 6 appears in both elements!

my_range= list(range(1,5))
print(my_range) # list of range


stu_grades = [['L12312',45,56],['L56435',44,67]]

print("LNun: {}".format(stu_grades[0][0]))
print("Grade 1: {}".format(stu_grades[0][1]))

len(grades) #Find the length of the list
grades.sort()
grades.pop([6]) #remove the item at position 6
grades.clear() #remove all items from the list
grades.reverse() #reverse the order of the items in the list
grades.remove(2) #remove the first item found with the value “2”
grades.count(2) #count the number of times 2 appears in the list
