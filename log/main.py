import math

# Given expression log2(x) = 5
base = int(input("Logaritmus alapja  \n"))
result = int(input("Logaritmus megoldása \n" ))

if base == "": base = 2
if result == "": result = 5

# To find x, we use the property x = base^result
x = base ** result

print("The solution for x is:", x)
