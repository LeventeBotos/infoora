def calculate_crc(azonosito):
    osszeg = 0
    for i in range(0, 10):
     osszeg += int(azonosito[i]) * (10 - i)
    return osszeg % 11

def calculate_crc_legacy(azonosito):
    osszeg = 0
    for i in range(0, 10):
       osszeg += int(azonosito[i]) * (i + 1)
    return osszeg % 11

# Felhasználói bemenet
azonosito = input("Adj meg egy 11 jegyű számot\n")

nem = azonosito[0]
birthDate = f"{azonosito[1]}{azonosito[2]}{azonosito[3]}{azonosito[4]}{azonosito[5]}{azonosito[6]}"
sorszam = f"{azonosito[7]}{azonosito[8]}{azonosito[9]}"
crc = int(azonosito[10])

print("Nem:", nem)
print("Születési dátum:", birthDate)
print("Sorszám:", sorszam)
print("CRC:", crc)

calculated_crc = calculate_crc(azonosito)
calculated_crc_legacy = calculate_crc_legacy(azonosito)


if calculated_crc == crc or calculated_crc_legacy == crc:
        print("A személyi azonosító szám érvényes.")
else:
        print(f"Hibás személyi szám! A helyes CRC számjegy: {calculated_crc} {calculated_crc_legacy}")