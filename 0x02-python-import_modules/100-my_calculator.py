#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if sys.argv[2] != '+' and sys.argv[2] != '-'\
       and sys.argv[2] != '*' and sys.argv[2] != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    if sys.argv[2] == '+':
        print("{} {} {} = {}"
              .format(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]),
                      int(sys.argv[1]) + int(sys.argv[3])))
    if sys.argv[2] == '-':
        print("{} {} {} = {}"
              .format(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]),
                      int(sys.argv[1]) - int(sys.argv[3])))
    if sys.argv[2] == '*':
        print("{} {} {} = {}"
              .format(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]),
                      int(sys.argv[1]) * int(sys.argv[3])))
    if sys.argv[2] == '/':
        print("{} {} {} = {}"
              .format(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]),
                      int(sys.argv[1]) / int(sys.argv[3])))
