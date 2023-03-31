import csv
import improv


def func():
    with open('data.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))


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
