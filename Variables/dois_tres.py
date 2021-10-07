#formatted literals example
name="Ruth"
str=f"Hello {name}" #a string literal can be built using f in front of the

print(str)
calc=f"Ten by twenty is: {10*20}" #calculations can be carried out
print(calc)


def build_orderline(price1, title1):
 str1=f"{title1:<30s} {price1:6.2f}"
 return str1
ln=build_orderline(99.99, "Python for DevOps in LYIT")
print(ln)
