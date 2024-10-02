import math
import createSzamHarmasok


def calcKeplet(a, b, c):
    s = (a + b + c) / 2 
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

class Haromszog:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def isTriangle(self):
        return (self.a + self.b > self.c and
                self.a + self.c > self.b and
                self.b + self.c > self.a)


haromszogek = []

# for i in range(9):
#     a = input(f"{i+1}. a oldala:")
#     b = input(f"{i+1}. b oldala:")
#     c = input(f"{i+1}. c oldala:")
#     haromszogek.append(Haromszog(a,b,c))

createSzamHarmasok.createSzamHarmasok()

i = open("/Users/leventebotos/infoora/szamharmasok.txt", "r")

for line in i:
    arr = line.split(",")
    haromszogek.append(Haromszog(float(arr[0]), float(arr[1]), float(arr[2])))



f = open("output.txt", "w")

for h in haromszogek:
    if h.isTriangle():
        f.write(f"{calcKeplet(h.a, h.b, h.c)} \n")
    else:
        print("Nem volt haromszog")
