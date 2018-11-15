#! /usr/bin/python3
# factors.py

# Finding out all the factors for a number.

import sys

def check_args():
    if len(sys.argv) != 2:
        print("Must enter a number")
        sys.exit()
    elif not sys.argv[1].isdigit():
        print("Must enter a number")
        sys.exit()
    else:
        return True

check_args()

number = int(sys.argv[1])
factors = [str(1), str(number)]

lower = 2
upper = number 

while lower < upper:
    if number % lower == 0:
        upper = int(number / lower)
        factors.append(str(lower))
        factors.append(str(upper))
    lower += 1
factors = list(set(factors))
factors.sort(key=int)
if len(factors) == 2:
    print("%s is a prime!" % (number))
factors = ", ".join(factors)
print(factors)
