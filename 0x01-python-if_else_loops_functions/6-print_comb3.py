#!/usr/bin/python3

for i in range(0, 9):
    for n in range(i, 10):
        if i != n and i != 8:
            print("{}{},".format(i, n), end=" ")
        elif i == 8 and i != n:
            print("{}{}".format(i, n), end="\n")
