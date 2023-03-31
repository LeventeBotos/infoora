import csv
import improv


def func():
    with open('data.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))


def li():
    lis = ["Roli", "Bulcsu", "Peti", "Levi"]
    lis.append("Gergo")
    print(lis)
    a = 0
    li2 = []
    h = improv.inp("Mennyit kérsz?", "int")
    while a < h:
        li2.append(input(f'Név {a + 1}: '))
        a += 1
    lis = lis + li2
    print(lis)
