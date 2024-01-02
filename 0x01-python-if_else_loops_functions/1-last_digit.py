#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
absolute = number
if absolute < 0:
    absolute = absolute * -1
    last = absolute % 10
    if last != 0:
        last = last * -1
else:
    last = absolute % 10
if last > 5:
    print(f"Last digit of {number} is {last} and is greater than 5")
elif last == 0:
    print(f"Last digit of {number} is {last} and is 0")
else:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
