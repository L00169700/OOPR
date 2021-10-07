upper_sign = "^"
left_sign = "<"
right_sign = ">"
botton_sign = "v"
top_screen = upper_sign*60
inter_change = left_sign + " "*58 + right_sign
inter3 = inter_change+ "\n" +  inter_change + "\n" + inter_change
title = "Title"
print(upper_sign*60)
print(inter3)
print("{0} {1:^56} {2}".format(left_sign,title,right_sign))
print(inter3)
stringA = "A"
stringO = "Option"

print("{0}{1:>3}{2:>9}{3:>2}{4:>45}".format(left_sign, stringA, stringO, stringA.lower(), right_sign)) # right align
print(botton_sign*60)

#print("{0:^10d}, Age {1}".format(12345,21)) # center
