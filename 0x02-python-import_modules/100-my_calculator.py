#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    arg_num = len(sys.argv) - 1
    if arg_num != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif sys.argv[2] not in "+-*/":
        print("Unkown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == "+":
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif sys.argv[2] == "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif sys.argv[2] == "*":
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif sys.argv[2] == "/":
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
