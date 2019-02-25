#!/usr/bin/env python3.7
'''branch.py'''

from time import time_ns

NUM_OF_LOOPS = 1000000000


def main():
    start = time_ns()
    for i in range(0, NUM_OF_LOOPS):
        if i % 1:
            pass
        if i % 2:
            pass
        if i % 3:
            pass
        if i % 4:
            pass
        if i % 5:
            pass
        if i % 6:
            pass
        if i % 7:
            pass
        if i % 8:
            pass
        if i % 9:
            pass
        if i % 10:
            pass
    end = time_ns()
    print( (end-start) / 1000000000)


if __name__ == '__main__':
    main()
