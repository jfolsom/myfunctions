#!python3
# Jacob Folsom 02/26/20
# Remove number/tabs from text

import os
import re
import pprint

debug = False

def removepref(listofstrings):
    """
    input: a list of strings or filehandle for text document
    output: a new list of all the strings minus everything before the tab
    """
    assert type(listofstrings) == list, "didn't feed list of strings a list"
    regextab = re.compile(r"(^.+\t)(.+)")            #regex splits preface vs line
    newlist = []
    for line in listofstrings:
        assert type(line) == str, 'one of the items in listostrings isnt astring'
        linemo = regextab.search(line)
        try:
            if linemo.group(2) == None:
                print('no tab in place for line', line)
                print('left line in place')
                newlist.append(line)
            else:
                addstring = linemo.group(2)
                newlist.append(addstring)
        except AttributeError:
            print('no tab in place for line', line)
            print('left line in place')
            newlist.append(line)
    return newlist

def listtodoc(strings):
    onestring = '\n'.join(strings)
    return onestring
    
def writenewfile(bigstring):
    if not os.path.exists(outputfilename):
        newfile = open(outputfilename, 'w+')
        newfile.write(bigstring)
    else:
        print('output file already exists, try again')
if __name__ == '__main__':
    print('input file must be encoded in utf-8')
    filename = input('enter the input filename in the current working directory : ')
    outputfilename = input('enter the name of a file to create with output in the cwd: ')
    filehandle = open(filename, 'r', encoding="utf-8")
    oldlines = filehandle.readlines()
    newstrings = removepref(oldlines)
    bigstring = listtodoc(newstrings)
    writenewfile(bigstring)
	

