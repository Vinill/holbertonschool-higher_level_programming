#!/usr/bin/python3
from ast import For
from re import I


def list_division(my_list_1, my_list_2, list_length):
    list_div = []
    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            list_div.append(result)
    return(list_div)
