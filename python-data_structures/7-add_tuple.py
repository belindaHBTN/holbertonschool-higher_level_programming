#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_zero = (0, 0)
    n_tuple_a = tuple_a + tuple_zero
    n_tuple_b = tuple_b + tuple_zero

    n_tuple = ((n_tuple_a[0] + n_tuple_b[0]), (n_tuple_a[1] + n_tuple_b[1]))
    return n_tuple
