#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    new_list = [x * y for x, y in my_list]
    sum_num = 0
    sum_num = sum(new_list)
    divisor = 0
    for i in range(len(my_list)):
        divisor = divisor + my_list[i][1]

    return sum_num / divisor
