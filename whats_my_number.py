#! /usr/bin/python3
# whats_my_number.py

# Finding a number that matches the following:
# Has two or more digits
# Is prime
# Does not contain a 1 or 7
# The sum of all of the digits is less then or equal to 10
# The first two digits add up to be odd
# The second to last digit is even and greater then 1
# The last digit is equal to how many digits are in the number

# Conclusion before testing:
# Must be a three digit number, since last digit adds up to number of digits and primes are odd

def check_contains(number):
    if "1" in number or "7" in number:
        return False
    return True

def check_sum(number):
    checksum = 0
    for i in number:
        checksum += int(i)
    if checksum > 10:
        return False
    return True

def check_first_two(number):
    checksum = 0
    for i in number[:2]:
        checksum += int(i)
    if checksum % 2 == 0:
        return False
    return True

def check_middle(number):
    number = int(number[1:2])
    if number % 2 == 0 and number > 1:
        return True
    return False

numbers = []

for i in range(203, 999, 10):
    i = str(i)
    if check_contains(i) and check_sum(i) and check_first_two(i) and check_middle(i):
        numbers.append(str(i))


print(numbers)
print(len(numbers))
# Must add check for prime, save that for later.
