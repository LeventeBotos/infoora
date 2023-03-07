import improv as impr

x = impr.inp("1", "float")
y = impr.inp("2", "float")  # 32
z = impr.inp("3", "float")

print(impr.inp("4", "bool"))

if x < y + z and y < z + x and z < x + y:
    print("har y")
else:
    print("har n")

if z**2 == x**2 + y**2 or x**2 == z**2 + y**2 or y**2 == x**2 + z**2:
    print("pit y")
else:
    print("pit n")
