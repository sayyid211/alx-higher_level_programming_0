#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            res = "FizzBuzz"
        elif i % 5 == 0:
            res = "Buzz"
        elif i % 3 == 0:
            res = "Fizz"
        else:
            res = i
        print("{} ".format(res), end='')
