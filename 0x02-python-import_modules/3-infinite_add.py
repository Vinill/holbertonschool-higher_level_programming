#!/usr/bin/python
if __name__ == "__main__":
    import sys
    num = 0
    for i in range(1, len(sys.argv)):
        num = num + int(sys.argv[i])
    print("{:d}".format(num))
