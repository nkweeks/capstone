#!/usr/bin/env python3.7

'''
Process the data file
'''

import pandas as pd
import matplotlib.pyplot as plt
from itertools import product


def proc():

    df = pd.read_csv('data.csv', names=['lang', 'func', 'time'])
    langs = ['C', 'Java', 'Python', 'Perl']
    funcs = ['Branch', 'Calc', 'Loop']
    prev = ''
    which_func = 0
    print(funcs[which_func])
    print(f'{"Language":14}{"Time":>10}{"Std Deviation":>18}')
    for i, (func, lang) in enumerate(product(funcs, langs)):
        lang_func_df = df[(df.lang == lang) & (df.func==func)]
        m = round(lang_func_df['time'].mean(), 6)
        s = round(lang_func_df['time'].std(), 6)
        print(f'{lang:14}{m:>10.6}{s:>18.6}')
        plt.plot(range(1,101), lang_func_df['time'], label=lang)
        if (i+1) % 4 == 0:
            prev = func
            plt.xlabel('Run')
            plt.ylabel('Time (Seconds)')
            plt.title(f'{func}')
            plt.legend(loc='upper right')
            plt.xlim(0,100)
            plt.ylim(0)
            plt.show()
            try:
                which_func += 1

                print(f'\n\n{funcs[which_func]}')
                print(f'{"Language":14}{"Time":>10}{"Std Deviation":>18}')
            except:
                pass


def main():
    proc()


if __name__ == '__main__':
    main()
