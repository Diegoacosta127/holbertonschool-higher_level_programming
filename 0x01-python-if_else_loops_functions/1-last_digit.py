#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    aux = number
else:
    aux = number * -1
print("Last digit of {:d} is {:d}".format(number, aux % 10), end=" ")
if aux % 10 > 5:
    print("and is greater than 5")
elif aux % 10 < 6 and aux % 10 != 0:
    print("and is less than 6 and not 0")
else:
    print("and is zero")