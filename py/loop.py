#!/usr/bin/env python3.7
# loop.py

from time import time_ns

NUM_OF_LOOPS = 100

def main():
    start = time_ns()
    for i in range(0, NUM_OF_LOOPS):
        for j in range(0, NUM_OF_LOOPS):
            for p in range(0, NUM_OF_LOOPS):
                pass
    end = time_ns()
    print( (end-start) / 1000000000)


if __name__ == '__main__':
    main()
