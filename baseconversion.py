# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:52:39 2020

@author: Jacob Folsom
"""

try:
    debug = True
except NameError:
    debug = False
    
import sys


def bin_to_dec(binarystring):
    # given a number represented in the form of a string of 1s and 0s,
    # convert it to a decimal integer
    decimalint = 0
    position = 0
    length = len(binarystring)
    if debug is True: print('About to start for loop with length:', length)
    for position in range(length):
        if debug is True: print('-starting for loop, position', position, '--')
        digit = binarystring[position]
        if debug is True: print('digit:', digit)
        exp = length - position - 1
        if debug is True: print('exp:', exp)
        # This digit expresses a value of 1 or 0 x 10^exp, where exp is
        # how far to the left it is from the last digit
        if digit == '0':
            decimalint = decimalint    # intentionally do nothing
            if debug is True:
                print('executed "0" branch, decimalint remains', decimalint)
        elif digit == '1':
            decimalint += 2**exp
            if debug is True:
                print('executed "1" branch, decimalint is now', decimalint)
        else:
            print('Please use a string of ones and zeros')
            sys.exit
    if debug is True: print('about to leave for loop')
    return decimalint


def decint_to_bin(decimalint):
    if decimalint < 0:
        isneg = True
    else:
        isneg = False
    binstring = ''
    remainder = abs(decimalint)
    while remainder > 0:     # for each digit
        binstring = str(remainder % 2) + binstring
        remainder = remainder // 2
        if debug is True: print('new binstring:', binstring)
        if debug is True: print('new remainder:', remainder)
    if isneg is True:
        binstring = '-' + binstring
    return binstring

def decfloat_to_bin(decimalfloat):
    if decimalfloat < 0:
        isneg = True
    else:
        isneg = False
    count = 0
    decimalfloat = abs(decimalfloat)
    while decimalfloat%1 != 0:
        count += 1
        decimalfloat *= 2
    if debug is True:
        print('about to pass ind(decimalfloat) to decint_to_bin ...')
        print('...decimalfloat is', decimalfloat, 'and count is', count)
    bincoef = decint_to_bin(int(decimalfloat))
    if debug is True: print('deciin_to_bin returned bincoef:', bincoef)
    placement = count - len(bincoef)
    binstring = bincoef
    if debug is True:
        print('about to enter for loop to add 0s to the front')
        print('binstring', binstring)
    for i in range(count-len(binstring)):
        if debug is True: print('i:', i)
        binstring = '0' + binstring
        if debug is True: print('new binstring', binstring)
    if debug is True: print('just left for loop, binstring:', binstring)
    binstring = binstring[:-count] + '.' + binstring[-count:]
    if isneg is True:
        binstring = '-' + binstring
    return binstring
    
  
if __name__ == '__main__':
    binstring = '10011'
    print(binstring, 'in decimal is', bin_to_dec(binstring))
    decimalinteger = 8
    print(decimalinteger, 'in binary is', decint_to_bin(decimalinteger))
    decimalfloat = 3/64
    print(decimalfloat, 'in binary is', decfloat_to_bin(decimalfloat))
