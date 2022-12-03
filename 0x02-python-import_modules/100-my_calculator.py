#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys
    ops = {"+", "-", "*", "/"}

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit(1)
    else:
        result = 0
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        op = sys.argv[2]

        if op not in ops:
            print("Unknown operator. Available operators: +, -, * and /")
            quit(1)
        else:
            if op == "+":
                result = calculator_1.add(a, b)
            elif op == "-":
                result = calculator_1.sub(a, b)
            elif op == "*":
                result = calculator_1.mul(a, b)
            else:
                result = calculator_1.div(a, b)
            print("{} {} {} = {}".format(a, op, b, result))
