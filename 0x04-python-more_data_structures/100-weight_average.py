#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    multi1 = 0
    multi2 = 0
    for x in my_list:
        multi1 = multi1 + (x[0] * x[1])
        multi2 = multi2 + (x[1])
    return(multi1 / multi2)

