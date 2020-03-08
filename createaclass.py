#! python3
"""
Created on Sat Mar  7 15:04:33 2020
version 0.2 Sat Mar 8 15:00:00 2020 Add blank __lt__ and __str__
@author: cerit

Create a basic class definition with init, gets and set
First argument is class name, remaining arguments are attribute names.
All of these can
be entered as system arguments when calling the program, or, if not, the
script will ask.
"""

import sys


def creategetset(attribute):
    # Supply an attribute name, create a string for a get and
    # a string for a set
    getstr  = '    def get'+attribute+'(self):\n'
    getstr += '        return self.'+attribute+'\n\n'
    getstr += '    def set'+attribute+'(self, '+attribute+'):\n'
    getstr += '        self.'+attribute+' = '+attribute+'\n'
    return getstr
# Get the name of the class from launch arguments or input
try:
    classname = sys.argv[1]
except IndexError:
    classname = input('Enter the name of the class: ')

# Ok, now do the same for a list of up to four attributes
attributes = []
i = -1
while True:
    i += 1
    try:
        attributes.append = sys.argv[i+2]
    except IndexError:
        nextatt = input('Enter the name of an attribute or ".": ')
        if nextatt == '.':
            break
        else:
            attributes.append(nextatt)

classdefstr = 'class %s(object):\n' % classname

initfirstline = '    def __init__(self'
initnextlines = ''
getsets = []
for attribute in attributes:
    initfirstline += ', '+attribute
    initnextlines += '        self.'+attribute+' = '+attribute+'\n'
    getsets.append(creategetset(attribute))
initfirstline += '):\n'
blankstrstr = '    def __str__(self):\n        pass\n'
blankltstr = '    def __lt__(self):\n        pass\n'
print(classdefstr, initfirstline, initnextlines, sep='')
for i in getsets:
    print(i)
print(blankstrstr)
print(blankltstr)