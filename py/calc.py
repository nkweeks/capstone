#!/usr/bin/env python3.7
# calc.py

from time import time_ns

NUM_OF_LOOPS = 1000

def pow(x, y):
    if y <= 1:
        return x
    else:
        return x * pow(x, y-1)


def main():
    start = time_ns()
    for j in range(100):
        for i in range(1, NUM_OF_LOOPS+1):
            # Exponent
            x = pow(i, 3)
            # Multiply
            x = x * 3
            # Divide 
            x = x // i
            # Add
            x = x + i
            # Subtract
            x = x - i
        end = time_ns()
    print( (end-start) / 1000000000)


if __name__ == '__main__':
    main()
