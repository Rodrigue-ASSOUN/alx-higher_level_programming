#!/usr/bin/python3
import sys
arguments = sys.argv[1:]
length = len(arguments) - 1
print("{} arguments:".format(length))

if length == 0:
    print("0 arguments.")
else:
    for i, arg in enumerate(arguments, start = 1):
        print("{}: {}".format(i, arg))

if __name__ == "__main__":
    pass
