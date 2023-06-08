#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        if not my_list or not x:
            print("")
            return i
        for index in range(0, x):
            i = index
            print("{}".format(my_list[index]), end="")
        print("")
        return i + 1
    except IndexError:
        print("")
        return i
