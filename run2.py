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
import time
import logging


def get_lang():
    lang = {'pl': 'Perl', 'py': 'Python', 'jv': 'Java', 'c': 'C'}
    try:
        return lang[sys.argv[1]]
    except:
        return None


def get_funcname():
    try:
        return sys.argv[2].title()
    except:
        return None


def get_subfunc():
    try:
        if sys.argv[1] == 'py':
            return {'calc': './py/calc.py', 
                    'branch': './py/branch.py',
                    'loop': './py/loop.py'}[sys.argv[2]]
        elif sys.argv[1] == 'pl':
            return {'calc': './pl/calc.pl', 
                    'branch': './pl/branch.pl',
                    'loop': './pl/loop.pl'}[sys.argv[2]]
        elif sys.argv[1] == 'jv':
            return {'calc': 'java ./jv/calc', 
                    'branch': 'java ./jv/branch',
                    'loop': 'java ./jv/loop'}[sys.argv[2]]
        elif sys.argv[1] == 'c':
            return {'calc': './c1/calc', 
                    'branch': './c1/branch',
                    'loop': './c1/loop'}[sys.argv[2]]
        else:
            return None
    except:
        return None

def run_all():
    print('run all')

def main():
    '''This function runs the program and calls the particular language 
    function combination '''

    lang = get_lang()
    func_name = get_funcname()
    subfunc = get_subfunc()
    
    if lang and func_name and subfunc:
        logging.basicConfig(format='%(message)s',
                            filename=f'./data/{lang}{func_name}.log',
                            level=logging.DEBUG)
        
        for i in range(100):
            start = time.time()
            subprocess.run(subfunc, capture_output=True)
            logging.info(f'{i},{lang},{func_name},{time.time() - start}')
        print('done')
    else:
        run_all()


if __name__ == '__main__':
    main()
