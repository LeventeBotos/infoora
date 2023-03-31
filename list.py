import csv


def func():
    with open('data.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))


def li():
    lis = ["a", "b", "x", "y"]
    print(lis)
