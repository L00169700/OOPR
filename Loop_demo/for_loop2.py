for i in range(5, 10):
 print(i)
#Simplified Bizz, Buzz game
for i in range(1, 10):
     if i == 5:
         print("Buzz")
         print("bizz")
print("\n")


#Stop when you find a 6
#break statement stops the loop
for i in range(1, 10):
     if i == 6:
        print("Found")
     break
     print("Not Yet")
print("It was found at {}".format(i))
#iterate over letters
from string import ascii_lowercase
for ch in ascii_lowercase:
 print(ch)