#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            element = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            element = 0
        except TypeError:
            print("wrong type")
            element = 0
        except IndexError:
            print("out of range")
            element = 0
        finally:
            result.append(element)
    return result
