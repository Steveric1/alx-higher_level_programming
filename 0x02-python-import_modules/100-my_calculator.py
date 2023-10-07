#!/usr/bin/python3

if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div
    import sys

    arg = len(sys.argv)
    operator = ['+', '-', '*', '/']

    if arg != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if sys.argv[2] not in operator:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]

    if op == '+':
        res = add(a, b)
        print("{} + {} = {}".format(a, b, res))
    elif op == '-':
        res = sub(a, b)
        print("{} - {} = {}".format(a, b, res))
    elif op == '*':
        res = mul(a, b)
        print("{} * {} = {}".format(a, b, res))
    elif op == '/':
        res = div(a, b)
        print("{} / {} = {}".format(a, b, res))
