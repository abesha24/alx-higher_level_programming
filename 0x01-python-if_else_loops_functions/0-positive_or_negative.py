#!/usr/bin/python3
import random
number1 = random.randint(-10, 10)
if number1 > 0:
    print("{} is positive".format(number1))
elif number1 == 0:
    print("{} is zero".format(number1))
else:
    print("{} is negative".format(number1))
