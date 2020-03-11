#!python3

# print a list of lists

import os
import pickle

def printlistoflines(listoflists):
    for y in range(len(picture)):
        for x in range(len(row1)):
            print(picture[y][x], end='')
        print('\n')
        
def receive_validinteger():
    # Receive an input, and check that it is a valid integer.  If no,
    # Keep asking
    while True:
        print('Enter a positive integer:')
        try:
            userinput = int(float(input()))
        except ValueError:
            print('Python can\'t make an integer out of that.')
            print('Maybe you used a comma in your number? That\'s')
            print('too fancy for me.')
            continue
        if isinstance(userinput, int) and userinput > 0:
            return userinput
            break
        else:
            print("That number is not positive.")


def stringweightloss(longstring, listofedits):
    # Search long string for chuncks to edit out from listofedits.  List of
    # edits will frequently come from a regex.findall(longstring).  Return the
    # string with the listofedits removed.
    # v0.0.1 JF 2019-11-28 Not yet checked.
    for naughtybit in listofedits:
        startcutat = longstring.index(naughtybit)
        lengthofcutis = len(naughtybit)
        endcutat = startcutat + lengthofcutis
        longstring = longstring[:startcutat] + longstring[endcutat:]
    return longstring

def stringtosections(longstring, listofsectionbreaks):
    # Search long string for a list of section breaks.  List of
    # breaks will frequently come from a regex.findall(longstring).  Return the
    # a list of strings containing each sections contents.  DOES NOT keep
    # section names.
    # v0.0.1 JF 2019-11-28 Not yet checked.
    stringremainder = longstring
    listofsections = ['']
    for sectionbreak in listofsectionbreaks:
        # For each substring in the list provided, first, find where it starts and
        # mark that position.
        startcutat = stringremainder.index(sectionbreak)
        # Then figure out where the substring stops 
        lengthofcutis = len(sectionbreak)
        endcutat = startcutat + lengthofcutis
        # Add the section to the list, then chop off the first section and
        # the sectionbreak from the longstring.
        listofsections.append(stringremainder[:startcutat])
        stringremainder = stringremainder[endcutat:]
    return listofsections
    
def loaddictionary(filename):
    inpickle = open(filename, 'rb')
    returndict = pickle.load(inpickle)
    inpickle.close()
    return returndict

def dumpdictionary(outdict, filename):
    outpickle = open(filename, 'wb')
    pickle.dump(outdict, outpickle)
    outpickle.close()

def stringtofile(astring, filename):
    print('I\'m about to overwrite the file', filename,
          'in the current working directory', os.getcwd())
    cani = input('Is that okay? (type "y"): ')
    if cani == 'y':
        outfileh = open(filename, "w+")
        outfileh.write(astring)
        outfileh.close()
    else:
        print('permission denied!',
               'My feelings are hurt and I shall do nothing.  NOTHING!')

    
