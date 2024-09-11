number1i = input("első szám: ")
number2i = input("második szám: ")

if number1i.isnumeric() and number2i.isnumeric():
    numbaer1 = int(number1i)
    number2 = int(number2i)
    
    while number1 != 0 or number2 != 0:
        if (number1 > number2):
            number1 -= number2
        elif (number1 < number2):
            number2 -= number1
        elif (number1 == number2):
            print(f'A lenagyobb közös osztója {number1i} és {number2i}-nek: {number1}')
            number1 = 0
            number2 = 0
        else:
            print("Hiba a számokkal")
else: 
    print("Nem szám volt malamelyik bemenet!")