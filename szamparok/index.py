
def calcLnko(number1, number2):
 while number1 != 0 :
        while number2 != 0 :
            if (number1 > number2):
                number1 -= number2
            elif (number1 < number2):
                number2 -= number1
            elif (number1 == number2):
             return number1
            else:
                print("Hiba a számokkal")
        return number2
 return number1
        

def isRelPrime(i, j):
    lnko = calcLnko(i, j)
    if lnko == 1:
        return True
    else: 
        return False

list = []
for i in range(100):
    for j in range(i, 100):
        if isRelPrime(i, j):
            print(f"{i} és {j} relativ primek")
            list.append(f"{i} és {j}")

print(len(list))

## I think I have it done...