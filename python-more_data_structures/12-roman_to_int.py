#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_dict = {"M": 1000, "C": 100, "D": 500, "X": 10, "L": 50, "I": 1, "V": 5}

    if type(roman_string) is not str or roman_string is None:
        return 0

    num = 0
    for i in range(len(roman_string)):
        if i == len(roman_string) - 1:
            num = num + roman_dict.get(roman_string[i])
        elif roman_dict.get(roman_string[i]) < roman_dict.get(roman_string[i + 1]):
            num = num - roman_dict.get(roman_string[i])
        else:
            num = num + roman_dict.get(roman_string[i])

    return num
