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
            return {'calc': 'java -cp ./jv/ calc', 
                    'branch': 'java -cp ./jv/ branch',
                    'loop': 'java -cp ./jv/ loop'}[sys.argv[2]]
        elif sys.argv[1] == 'c':
            return {'calc': './c1/calc', 
                    'branch': './c1/branch',
                    'loop': './c1/loop'}[sys.argv[2]]
        else:
            return None
    except:
        return None

def run_all():
    logging.basicConfig(format='%(message)s',
                        filename=f'./data/all_funcs.log',
                        level=logging.DEBUG)
    all_funcs = ('./py/calc.py', './py/branch.py', './py/loop.py', 
                 './pl/calc.pl', './pl/branch.pl', './pl/loop.pl', 
                 ['java', 'calc'], ['java', 'branch'], ['java', 'loop'],
                 './c1/calc', './c1/branch','./c1/loop')
    for c, func in enumerate(all_funcs):
        lang = ('Python', 'Perl', 'Java', 'C')[c//3]
        if lang == 'Java':
            if 'jv' not in os.getcwd():
                os.chdir('jv')
        elif lang == 'C':
            if 'jv' in os.getcwd():
                os.chdir('..')
        func_name = ''
        if 'calc' in func:
            func_name = 'Calc'
        elif 'loop' in func:
            func_name = 'Loop'
        elif 'branch' in func:
            func_name = 'Branch'
        for i in range(NUM_OF_LOOPS):
            start = time.time()
            subprocess.run(func)
            logging.info(f'{i},{lang},{func_name},{time.time() - start}')


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
        
        for i in range(NUM_OF_LOOPS):
            start = time.time()
            subprocess.run(subfunc, capture_output=True)
            logging.info(f'{i},{lang},{func_name},{time.time() - start}')
        print('done')
    else:
        run_all()


if __name__ == '__main__':
    main()
