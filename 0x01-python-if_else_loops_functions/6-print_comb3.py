#!/usr/bin/python3

"""Print all possible different combinations of two digits in ascending order.

    The two digits must be different - 01 and 10 are considered identical.
    """
for digit11 in range(0, 10):
    for digit12 in range(digit11 + 1, 10):
        if digit11 == 8 and digit12 == 9:
            print("{}{}".format(digit11, digit12))
        else:
            print("{}{}".format(digit11, digit12), end=", ")
