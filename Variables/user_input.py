price1 = 99.99
price2 = 9.99
print("{0:<30s} {1:6.2f}".format("Python for DevOps", price1))
print("{0:<30s} {1:6.2f}".format("Python for DevOps", price2))
print("_"*37 )
print("{0:<30s} {1:6.2f}".format("Total", price1+price2))

answer=input("Do you wish to continue?")
print("Your answer was:{0}".format(answer))

title2="Customer:J. Bloggs"
print("{0:<30s}".format(title2))

silent = input()
