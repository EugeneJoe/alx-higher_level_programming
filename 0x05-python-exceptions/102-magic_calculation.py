#!/usr/bin/python3


def magic_calculation(a, b):
    """Perform magic calculation"""
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                result = a + b
            else:
                result += (a ** b) / i
        except Exception:
            print('Too far')
        return result
