#!/usr/bin/env python3.7

from time import time_ns

NUM_OF_LOOPS = 10

def pow(x, y):
    if y <= 1:
        return x
    else:
        return pow(x, y-1) + pow(x, y-2)


def main():
    start = time_ns()
    for i in range(1, NUM_OF_LOOPS+1):
        # Exponent
        i = pow(i, i)
        # Multiply
        i = i * i
        # Divide 
        i = i / i
        # Add
        i = i + i
        # Subtract
        i = i - i
    end = time_ns()
    print( (end-start) / 1000000000)


if __name__ == '__main__':
    main()
