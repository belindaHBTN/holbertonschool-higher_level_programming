#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_zero = (0, 0)
    new_tuple_a = tuple_a + tuple_zero # (1, 0, 0) (0, 0)
    new_tuple_b = tuple_b + tuple_zero

    new_tuple =((new_tuple_a[0] + new_tuple_b[0]), (new_tuple_a[1] +
        new_tuple_b[1]))
    return new_tuple
