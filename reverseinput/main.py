string = input("Add meg a bemenetet: ")
arr = list()
out = ""

for s in string:
    arr.append(s)

arr.reverse()

for c in arr:
   out += c

print(out)
