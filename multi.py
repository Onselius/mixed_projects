#! /usr/bin/python3
# multi.py - Take one numeric argument show table for that number

import sys

if len(sys.argv) != 2:
    print("Must enter an argument")
    sys.exit()
elif not sys.argv[1].isdigit():
    print("Must enter a numeric argument")
    sys.exit()

number = int(sys.argv[1])

horisontal = [i+1 for i in range(number)]
print(horisontal)

for y in horisontal:
    for x in horisontal:
        number = str(x * y).ljust(5)
        print(number, end="")
    print()
