import improv
import math

a = improv.inp("Szám 1: ", "float")
b = improv.inp("Szám 2: ", "float")
c = improv.inp("Szám 3: ", "float")

print(f'Oldalak: {a}, {b}, {c}')

if a > 0 and b > 0 and c > 0 and a < b + c and b < a + c and c < a+b:
    s = (a + b + c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(f"A háromszög területe: {area}.")
else:
    print("nem 3szog.")
