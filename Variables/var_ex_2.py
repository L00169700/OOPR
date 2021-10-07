import string

choice = 'a'
str = "This is a long string with nothing to say."
paragraph = '''This is a very long string which can run over multiple lines if desired and can still
contain single ‘ or double “ quotes within it '''

print(str[0]) #prints the first letter in the string
print(str[3:8]) #prints from index 3 to 8
print(str[8:]) #prints from index 8 to the end
print(str[-1]) #prints the last character in the string
print(str[-2]) #prints the second last character in the string
len(str) #prints the length of the string

print(str.capitalize())
print(str.center)
#print(str.count("long",0 , len(str)))
print(str.find("long"))
print(str.isdigit())
print(str.isnumeric())
print(str.isspace())
print(str.len())