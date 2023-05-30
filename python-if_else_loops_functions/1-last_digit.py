#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

ld = "Last digit of"
g_five = "and is greater than 5"
l_six = "and is less than 6 and not 0"
zero = "and is 0"

if (number >= 0):
    last_digit = number % 10
else:
    last_digit = number % -10

if last_digit > 5:
    print("{0:s} {1:d} is {2:d} {3:s}".format(ld, number, last_digit, g_five))
elif last_digit < 6 and last_digit != 0:
    print("{0:s} {1:d} is {2:d} {3:s}".format(ld, number, last_digit, l_six))
else:
    print("{0:s} {1:d} is {2:d} {3:s}".format(ld, number, last_digit, zero))
