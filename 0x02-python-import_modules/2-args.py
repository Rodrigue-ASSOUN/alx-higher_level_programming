#!/usr/bin/python3
import sys
arguments = sys.argv[1:]
length = len(arguments)

if length == 0:
    print("0 arguments.")
else:
    print("{} argument(s):".format(length))
    for i, arg in enumerate(arguments, start=1):
        print("{}: {}".format(i, arg))

if __name__ == "__main__":
    pass
