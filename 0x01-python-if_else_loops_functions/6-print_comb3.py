#!/usr/bin/python3
def comb(L):
    n = 0
    for i in range(9):
        n = n + 1
        for j in range(n, 10):
            if i == 8 and j == 9:
                print("{}{}".format(L[i], L[j]))
            else:
                print("{}{}, ".format(L[i], L[j]), end="")


comb([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
