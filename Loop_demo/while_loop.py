#sample while loop
max=5
counter=0
total=0
while counter <= max :
 total+=9.99
 counter+=1
print("The final amount is: {0:5.2f}".format(total))
#While true sample
text=""
while 1:
     print ("Enter name")
     uname=input()
     if(uname == "joe"):
        break
print("Finished")


if __name__ == "__main__":
    text = ""
    while 1:
        print("Enter name")
        uname = input()
        if uname == "joe":
            break
        print("\n Sorry, try again!\n")
    print("Finish")
