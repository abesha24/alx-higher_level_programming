#!/usr/bin/python3

def islower(c):
    """Check for lower case characters."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
