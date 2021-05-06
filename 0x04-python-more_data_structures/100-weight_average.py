#!/usr/bin/python3


def weight_average(my_list=[]):
    """Returns the weighted average of all integers.

       my_list format: each element is a tuple of the form
                       (<score>, <weight>)
    """
    if len(my_list) == 0:
        return 0
    prod = 0
    weight_sum = 0
    for i in range(len(my_list)):
        prod += my_list[i][0] * my_list[i][1]
        weight_sum += my_list[i][1]
    return prod/weight_sum
