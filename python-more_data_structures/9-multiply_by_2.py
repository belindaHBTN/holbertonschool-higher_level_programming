#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    dictionary_copy = a_dictionary.copy()

    for key in dictionary_copy:
        dictionary_copy[key] = dictionary_copy[key] * 2
    return dictionary_copy
