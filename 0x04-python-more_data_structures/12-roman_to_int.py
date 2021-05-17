#!/usr/bin/python3


def roman_to_int(roman_string):
    """Converts a Roman Numeral to an integer"""
    if type(roman_string) is not str or roman_string is None:
        return 0
    else:
        roman_dec = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
                     "D": 500, "M": 1000}
        decs = [roman_dec.get(x) for x in roman_string]
        res = 0
        for i in range(len(decs)):
            res += decs[i]
            if decs[i - 1] < decs[i] and i != 0:
                res -= (decs[i - 1] + decs[i - 1])
        return res