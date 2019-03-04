#!/usr/bin/env python3.7

'''
This program runs and gathers benchmark data about programs written in different languages
Usage: ./run.py [language] [function]
Examples:
    ./run.py -py -calc
    ./run.py -c -all
'''
__author__ = 'Nathaniel Weeks'
__version__ = '0.0.1'


import subprocess
import sys
import os
import time
import logging

NUM_OF_LOOPS = 10

def get_lang():
    lang = {'pl': 'Perl', 'py': 'Python', 'jv': 'Java', 'c': 'C'}
    try:
        return lang[sys.argv[1]]
    except:
        return None


def get_func():
    funcs = ('./c1/branch', './c1/calc', './c1/loop',
            ('java', '-cp', './jv/', 'branch'),
            ('java', '-cp', './jv/', 'calc'),
            ('java', '-cp', './jv/', 'loop'),
            './py/branch.py', './py/calc.py', './py/loop.py',
            './pl/branch.pl', './pl/calc.pl', './pl/loop.pl')
    for func in funcs:
        yield func


def run_all():
    logging.basicConfig(format='%(message)s',
                        filename=f'./data/AllLangs.log',
                        level=logging.DEBUG,
                        filemode = 'w')

    lang = ['C', 'Java', 'Python', 'Perl']

    for i, func in enumerate(get_func()):
        num_loops = 100
        for k in range(num_loops):
            r = subprocess.run(func, capture_output=True).stdout.decode().strip()
            func_out = (['Branch', 'Calc', 'Loop']*num_loops)[(k+num_loops*i)//num_loops]
            logging.info(f'{k+num_loops*i},{lang[i//(3)]},{func_out},{r}')


def main():
    '''This function runs the program and calls the particular language 
    function combination '''
    run_all()


if __name__ == '__main__':
    main()
