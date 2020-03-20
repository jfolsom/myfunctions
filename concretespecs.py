#!python3
"""
Jacob Folsom 02/27/20
rev 0.01
accepts a job number, no dashes.
outputs any existing specs and latest revision date, then
asks for new specs
"""

debug = False
import pprint
import pickle
import cercopsfunctions
import os
import datetime

def lookupnumber(pnumber):    
    """
    accept a string that is the id number of a project
    look up that string in the dictionary of all projects.
    look up the lates update in the dictionary of dates.
        if it's not listed there, give the user the option to add todays date
    return the dictionary of specs and the latest update
    """
    assert type(pnumber) == str, 'e1'
    thisproject = allprojects.get(pnumber, {})
    try:
        updated = dates[pnumber]
    except KeyError:
        updated = 'never'
        print('never checked for specs,'
                   'enter current date to indicate you checked for specs today')
        newdate = input('or enter "." to leave it as never having been checked: ')
        if newdate != '.':
            dates[pnumber] = newdate
            updated = dates[pnumber]
    assert type(thisproject) == dict, 'e2'
    assert type(updated) == str, 'e3'
    return thisproject, updated


def mainloop():
    todays_specs = ''
    while True:
        try:
            pnumber = input('enter a project number, no dashes, or "." to stop: ')
        except KeyboardInterrupt:
            pnumber = input('received a keyboard interrupt.  Enter "q" to close, or reenter your data')
            if pnumber == 'q':
                raise
        if pnumber == ".":
            break
        thisproject, updated = lookupnumber(pnumber)
        print('project specs for', pnumber, 'are:')
        pprint.pprint(thisproject)
        print('and it was last updated')
        pprint.pprint(updated)
        while True:
            try:
                wanttoadd = input('To add a spec, enter the key, else type "."'+
                              ' or "del" to delete all specs for that project: ')
            except KeyboardInterrupt:
                wanttoadd = input('received a keyboard interrupt.  Enter "q" to close, or reenter your data')
                if pnumber == 'q':
                    raise
            if wanttoadd == 'del':
                try:
                    del allprojects[pnumber]
                except KeyError:
                    print('no specs exist for that project')
            elif wanttoadd != ".":
                # Didn't enter '.', so lets add the users spec
                dates[pnumber] = str(datetime.date.today())
                specvalue = input('enter the value, or "del" to delete all'+
                                  'values for this key: ')
                if pnumber in allprojects.keys():
                    # Add to existing subdictionary if it already exists ...
                    if specvalue == 'del':
                        try:
                            del allprojects[pnumber][wanttoadd]
                        except KeyError:
                            print('no specs exist for that key')
                    else:
                        allprojects[pnumber][wanttoadd] = specvalue                   
                else:
                    # ... else create a new subdictionary
                    allprojects[pnumber] = {wanttoadd:specvalue}
            else:
                break
        if pnumber in allprojects.keys():
            for key, value in allprojects[pnumber].items():
                todays_specs += pnumber+key+': '+value+'\n'
    return todays_specs
    
if __name__ == '__main__':   
    filename = 'concretespecs.pickle'
    outfilename = 'todays_specs.txt'
    todays_specs = ''
    print('about to load a dictionary from',
          'pickle file', filename)
    print('make sure that file is in the cwd, (cwd is', os.getcwd(),')')
    allprojects = cercopsfunctions.loaddictionary(filename)
    dates = allprojects['dates']
    assert type(dates) == dict, 'object dates is not a dict'
    print('after loading, length of allprojects is', len(allprojects))
    if debug is True: pprint.pprint(allprojects)
    if debug is True: pprint.pprint(dates)
    todays_specs = mainloop()
    # place the updated dates subdictionary back into the main dict b4 dump:
    allprojects['dates'] = dates
    print('about to dump a pickled dictionary of length', len(allprojects))
    print('today\'s specs saved in file', outfilename)
    cercopsfunctions.dumpdictionary(allprojects, filename)
    print('Today\'s specs:\n', todays_specs, sep='')
    cercopsfunctions.stringtofile(todays_specs, outfilename)
    unneeded = input('press enter to close window')

    