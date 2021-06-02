#!/usr/bin/python3
"""
Script that reads stdin line by line and computes relevant metrics
"""

if __name__ == "__main__":
    import sys

    size = 0
    status_tally = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    linenum = 0
    try:
        for line in sys.stdin:
            tokens = line.split()
            if len(tokens) >= 2:
                num = linenum
                if tokens[-2] in status_tally:
                    status_tally[tokens[-2]] += 1
                    linenum += 1
                    try:
                        size += int(tokens[-1])
                        if num == linenum:
                            linenum += 1
                    except:
                        if num == linenum:
                            continue
            if linenum % 10 == 0:
                print("File size: {}".format(size))
                for key, value in sorted(status_tally.items()):
                    if value:
                        print("{}: {}".format(key, value))
        print("File size: {:d}".format(file_size))
        for key, value in sorted(status_tally.items()):
            if value:
                print("{}: {}".format(key, value))

    except KeyboardInterrupt:
        print("File size: {}".format(size))
        for key, value in sorted(status_tally.items()):
            if value:
                print("{}: {}".format(key, value))
