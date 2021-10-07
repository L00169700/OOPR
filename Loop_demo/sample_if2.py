grade = input("Enter a grade: ")
grade = int(grade) # type cast – change the string grade to an integer and put it back in
 # the same variable!
module1 = "python"
# note that the operators and, or, not are valid
if (grade >= 70) and (module1 == "python"):
 print('You have earned a Distinction!') # Comments can be placed anywhere
 # Remember that comments should be included to explain
 # all interesting sections of code!
elif grade >= 60:
 print("You have earned a M.1.")
elif grade >= 50:
 print("You have earned a M.2.")
elif grade >= 40:
 print('You have passed')
else:
 print("Please try again")
