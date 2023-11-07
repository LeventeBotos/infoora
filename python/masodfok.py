deg0 = float(input("0dfok: \n"))
deg1 = float(input("1dfok: \n"))
deg2 = float(input("2dfok: \n"))
x = float(input("X:\n"))


def fv(p0, p1, p2, x):
    y = p2*x**2 + p1*x + p0
    return(y)


print(f"X = {x}nél Y={fv(deg0, deg1, deg2, x)}")
