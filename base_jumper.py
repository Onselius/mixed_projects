#! /usr/bin/python3
# base_jumper.py - Change number from one base to another. 
# Takes 3 arguments: number to convert, base number is in, base to convert to

import sys

# Verify arguments
def check_args(list_of_vars):
    if len(list_of_vars) != 3:
        print("Must supply 3 arguments")
        return False
    for value in list_of_vars[1:]:
        if not value.isdigit():
            print("Must supply numeric arguments")
            return False
    for value in list_of_vars[1:]:
        if 2 > int(value) or int(value) > 16:
            print("Only accepts bases between 2 and 16")
            return False
    return True

def convert_from_hex(number):
    hexadecimal = {"A": 10,
                    "B": 11,
                    "C": 12,
                    "D": 13,
                    "E": 14,
                    "F": 15}
    return hexadecimal[number]

def convert_to_hex(number):
    hexadecimal = {10: "A",
                    11: "B",
                    12: "C",
                    13: "D",
                    14: "E",
                    15: "F"}
    return hexadecimal[number]

def convert_to_decimal(number, base): # Make list of number and reverse it. Replace hex numbers with dec numbers. 
    base = int(base)
    list_of_digits = []
    decimal = 0
    for i in number:
        if not i.isdigit():
            i = convert_from_hex(i)
        digit = int(i)
        list_of_digits.append(digit)
    list_of_digits = list(reversed(list_of_digits))
    for i in range(len(list_of_digits)):
        decimal += list_of_digits[i] * (base**i)
    return decimal

def convert_from_decimal(number, end_base): # Keep track of remainder and end value when dividing with base. Save remainder in reverse
    end_base = int(end_base)
    list_of_digits = []
    remainder = 0
    while number > 0:
        remainder = number % end_base
        if remainder > 9:
            remainder = convert_to_hex(remainder)
        list_of_digits.append(remainder)
        number = int(number / end_base)

    result = ""
    for i in list(reversed(list_of_digits)):
        result += str(i)
    return(result)

def convert_number(number, start_base, end_base):
    decimal_number = convert_to_decimal(number, start_base)
    result = convert_from_decimal(decimal_number, end_base)
    print(result)

if not check_args(sys.argv[1:]):
    sys.exit

convert_number(sys.argv[1], sys.argv[2], sys.argv[3])
