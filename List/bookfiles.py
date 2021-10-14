books = [] # empty list

for i in range(0,4):
    books.append(input("Enter Details:"))


for i in range(0,4):
    print("{0} has a value of {1}".format(i, books[i]))


