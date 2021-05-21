#!/usr/bin/python3
"""Contains definition of text_indentation() function"""


def text_indentation(text):
    """Print given text with 2 new lines after '.', '?', and ':' characters.

    Args:
        text (str): Text to be formatted.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    t1 = text.strip()
    t2 = t1.replace(". ", ".")
    t3 = t2.replace(": ", ":")
    t4 = t3.replace("? ", "?")
    for c in t4:
        if c == '.':
            print(".\n")
        elif c == '?':
            print("?\n")
        elif c == ':':
            print(":\n")
        else:
            print(c, end='')
