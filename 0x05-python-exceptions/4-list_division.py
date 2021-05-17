#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """
       Divide list_length elements of my_list_1 by corresponding element of
       my_list_2.

       Description:
       Generates a new list whose elements are the quptent of the division.
       Handles IndexError and ZeroDivisionError exceptions
       """

    res_1 = []
    res = 0
    for n in range(0, list_length):
        try:
            res = float(my_list_1[n]) / my_list_2[n]
            res_1.append(res)
        except ZeroDivisionError:
            print("division by 0")
            res_1.append(0)
        except TypeError:
            print("wrong type")
            res_1.append(0)
        except IndexError:
            print("out of range")
            res_1.append(0)
        finally:
            pass
    return res_1
