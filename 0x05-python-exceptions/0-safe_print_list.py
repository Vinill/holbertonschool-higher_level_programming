#!/usr/bin/python3
from tkinter import Y


def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            return(x)
    except IndexError:
        print("")