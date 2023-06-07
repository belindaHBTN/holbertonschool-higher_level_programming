#!/usr/bin/python3

def no_c(my_string):
    string_no_c = my_string.translate({ord("c"): None})
    string_no_c_C = string_no_c.translate({ord("C"): None})
    return string_no_c_C
