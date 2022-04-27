#!/usr/bin/python3
for n in range(90, 64, -1):
    if n % 2 == 0:
        n = n + 32
    print(chr(n), end="")
