def check(x, y):
    if (x > 0 and y > 0 or x < 0 and y < 0 or x == 0 and y == 0):
        return True
    else:
        return False


def checkp(x, y):
    if (x * y > 0) or (x == 0 and y == 0):
        return True
    else:
        return False
