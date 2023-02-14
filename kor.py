import math

ex, ey, mx, my = 2, 3.5, 6, 5.2

def circleter(x1, y1, x2, y2):
    rad = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    terulet = math.pi * rad**2
    return terulet

terulet = circleter(ex, ey, mx, my)

terulett = str(terulet)

def circleker(x1, y1, x2, y2):
    rad = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    kerulet = math.pi * rad*2
    return kerulet

kerulet = circleker(ex, ey, mx, my)

kerulett = str(kerulet)

print("Terület: " + terulett + " Kerület: " + kerulett)