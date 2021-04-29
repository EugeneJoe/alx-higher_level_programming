#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    for n in names:
        if n.find("_") != 0:
            print(n)
