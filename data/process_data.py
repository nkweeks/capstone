#!/usr/bin/env python3.7

'''
Process the data file
'''

import pandas as pd
import matplotlib.pyplot as plt
from itertools import product


def main():
    df = pd.read_csv('data.csv', names=['lang', 'func', 'time'])
    langs = ['C', 'Java', 'Python', 'Perl']
    funcs = ['Branch', 'Calc', 'Loop']
    prev = ''
    which_func = 0
    print(funcs[which_func])
    print(f'{"Language":14}{"Time":>10}    {"Std Deviation":^14}  {"High":^10}{"Low":^10}')
    for i, (func, lang) in enumerate(product(funcs, langs)):
        lang_func_df = df[(df.lang == lang) & (df.func==func)]
        m = round(lang_func_df['time'].mean(), 6)
        s = round(lang_func_df['time'].std(), 6)
        high = round(lang_func_df['time'].max(), 6)
        low = round(lang_func_df['time'].min(), 6)
        print(f'{lang:14}{m:>10.6}    {s:<14.6}  {high:<10.6}{low:<10.6}')
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
                print(f'{"Language":14}{"Time":>10}    {"Std Deviation":^14}  {"High":^10}{"Low":^10}')
            except:
                pass


if __name__ == '__main__':
    main()
