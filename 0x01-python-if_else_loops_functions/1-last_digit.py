#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    aux = number % 10
else:
    aux = -number % 10
print("Last digit of",number,"is", aux, end=" ")
if aux > 5:
    print("and is greater than 5")
elif aux < 6 and aux != 0:
    print("and is less than 6 and not 0")
else:
    print("and is 0")
