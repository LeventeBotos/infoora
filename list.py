import csv
import improv


def func():
    with open('data.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))


def selling():
    lis = []
    bsum, dsum = 0, 0
    while True:
        resp = improv.inp('Akarsz hozzadni?', 'str')
        if resp == "y":
            add = improv.inp("mit?", "str")
            lis.append(add)
            print(lis)
        else:
            break
    print("done")
    count(bsum, dsum, lis)
    return lis


def count(bsum, dsum, lis):
    print(lis)
    print(dsum)
    print(bsum)
    while True:
        nt = 0
        if lis[n][0] == "B":
            bsum += 1
            print(bsum)
            n += 1
        else:
            print("no")
            break


def li(lis):
    a = 0
    li2 = []
    h = improv.inp("Mennyit adsz hozzá?", "int")
    while a < h:
        li2.append(input(f'Név {a + 1}: '))
        a += 1
    lis = lis + li2
    print(lis)


def spec(lis):
    h = improv.inp("Hanyadik elem helyett?", "int") - 1
    t = improv.inp("Milyen type lesz?", str)
    lis[h] = improv.inp("Ird be, kérlek", t)
    print(lis)

# import list

# lis = ["Roli", "Bulcsu", "Peti", "Levi"]
# lis.append("Gergo")

# list.spec(lis)
