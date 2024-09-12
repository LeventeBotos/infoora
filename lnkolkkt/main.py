number1i = input("első szám: ")
number2i = input("második szám: ")


def calcLnko(number1, number2):
 while number1 != 0 or number2 != 0:
        if (number1 > number2):
            number1 -= number2
        elif (number1 < number2):
            number2 -= number1
        elif (number1 == number2):
            return number1
        else:
            print("Hiba a számokkal")

def calckLkkt(number1, number2, lnko):
    return int(int(number1 * number2) / lnko)

if number1i.isnumeric() and number2i.isnumeric():
    number1 = int(number1i)
    number2 = int(number2i)
    
    lnko = calcLnko(number1, number2)
    print(f'A lenagyobb közös osztója {number1i} és {number2i}-nek: {lnko}')

    lkkt = calckLkkt(number1, number2, lnko)
    print(f'A legkissebb közös többszöröse {number1i} és {number2i}-nek: {lkkt}')
   
else: 
    print("Nem szám volt malamelyik bemenet!")
