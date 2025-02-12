jeladastext = open('/Users/leventebotos/infoora/autokmozgasa/jeladas.txt', "r")
sorok = jeladastext.read().split("\n")
ertekek = []

for sor in sorok:
    ertekek.append(sor.split("\t"))
    # print(sor)

latestHour = 0
latestHourIndexes = []
latestMin = 0
latestMinIndexes = []
latestHourDriverPlate = ""

for i, e in enumerate(ertekek):  
    driverPlate, hour, minute = e[0], int(e[1]), int(e[2])  

    if hour > latestHour:
        latestHour = hour
        latestHourIndexes = [i]
        latestMin = minute  
        latestMinIndexes = [i]
        latestHourDriverPlate = driverPlate 

    elif hour == latestHour:
        latestHourIndexes.append(i)

        if minute > latestMin:
            latestMin = minute
            latestMinIndexes = [i] 
            latestHourDriverPlate = driverPlate  
        elif minute == latestMin:
            latestMinIndexes.append(i)

print("2. feladat:")
print(f'Az utolsó jeladás időpontja {latestHour}:{latestMin}, a jármű rendszáma {latestHourDriverPlate}')

print("3. feladat:")
print(f'Az első jármű {ertekek[0]}')

def isFirst(e):
    return ertekek[0][0] == e[0] if ertekek else False 


if ertekek: 
    firstCar = filter(isFirst, ertekek)
    times = []
    for f in list(firstCar):
        times.append(f'{f[1]}:{f[2]}')
    print(f'Jeladásainak időpontjai: {" ".join(times)}')

