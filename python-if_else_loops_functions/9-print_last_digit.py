#!/usr/bin/python3
def print_last_digit(number):
    l_d = 0
    if number > 0:
        l_d = number % 10
    elif number < 0:
        l_d = (-number) % 10
    print("{:d}".format(l_d), end="")
    return l_d
