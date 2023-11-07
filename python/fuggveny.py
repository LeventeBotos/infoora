try:
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
except:
    print("Számot adj meg!")

def mer(x1, y1, x2, y2):
    meredek = (y2-y1)/(x2-x1)
    return meredek

def ymetszes(x1, y1, x2, y2):
    ymetsz = ((y2-y1)/(x2-x1)) * x1
    return ymetsz

meredek = mer(x1, y1, x2, y2)

ymetsz = ymetszes(x1, y1, x2, y2)


print("Az egyenes egyenlete: y=", meredek, "+", ymetsz)