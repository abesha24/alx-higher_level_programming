#!/usr/bin/python3

def uppercase(str):
    """Print a string in uppercase."""
    for cc in str:
        if ord(cc) >= 97 and ord(cc) <= 122:
            cc = chr(ord(cc) - 32)
        print("{}".format(cc), end="")
    print("")
