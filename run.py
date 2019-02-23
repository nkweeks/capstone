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


def run_pl(func='all'):
    '''This function runs the perl script to be benchmarked'''
    funcs = {'calc': 'calc.pl', 'loop': 'loop.pl', 'branch': 'branch.pl'}
    return funcs[func]

def run_py(func='all'):
    '''This function runs the python script to be benchmarked'''
    pass


def run_jv(func='all'):
    '''This function runs the java script to be benchmarked'''
    pass


def run_c1(func='all'):
    '''This function runs the c script to be benchmarked'''
    pass


def main():
    '''This function runs the program and calls the particular language 
    function combination '''
    funcs = {run_pl: 'Perl', run_py: 'Python', run_jv: 'Java', run_c1: 'C'}
    print(sys.argv)
    prog = funcs
    for func in funcs.keys():
        print(funcs.get(func))


if __name__ == '__main__':
    main()
