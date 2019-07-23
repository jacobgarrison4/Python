"""
Majors Count
CIS 210 F17 project 7

Author: Jacob Garrison

Credits: Python Programming in Context

majors count reads a file and reports the
most common major in the class and also
reports a frequency chart of all majors.
"""
from p62_data_analysis import *

def main():
    """() -> None

    Calls: majors_readf, majors_analysis, majors_report
    Top level function for analysis of CIS 210 majors data.
    
    > majors_main()
    """
    fname = 'majors_cis210f17.txt'
    majorsli = majors_readf(fname)
    majors_mode = majors_analysis(majorsli)
    majors_report(majors_mode, majorsli)
    return None

def majors_readf(fname):
    """(str) -> list

    Creates a list of majors from a file.

    >>> majors_readf('majors_cis210f17.txt')
    ['CIS', 'EC', 'PS', 'GSS', 'PBA', 'SDSC', 'CIS', 'CIS', 'MATH', 'CIS', 'CIS',
    'PSY', 'CIS', 'GSS', 'PDS', 'CIS', 'CIS', 'PS', 'CIS', 'CIS', 'PHYS', 'CIS',
    'UNDL', 'ATCH', 'CIS', 'PHYS', 'UNDL', 'CIS', 'CIS', 'EC', 'PBA', 'EC', 'CIS',
    'PEN', 'CIS', 'MATH', 'CEP', 'CIS', 'CIS', 'BI', 'CIS', 'MACS', 'GEOG', 'MATH',
    'UNDL', 'CIS', 'PEN', 'UNDL', 'CIS', 'UNDL', 'CIS', 'MUS', 'UNDL', 'MACS', 'CIS',
    'CIS', 'CH', 'CIS', 'CIS', 'CIS', 'CH', 'CIS', 'CIS', 'CIS', 'CIS', 'UNDL',
    'GEOG', 'CIS', 'CIS', 'CIS', 'CIS', 'MATH', 'MATH', 'PEN', 'PBA', 'ATCH', 'CIS',
    'CIS', 'PHYS', 'MACS', 'UNDL', 'CIS', 'CIS', 'UNDL', 'MATH', 'CIS', 'CIS', 'UNDL'
    , 'PBA', 'CIS', 'MACS', 'CIS', 'J', 'CIS', 'BI', 'MATH', 'UNDL', 'EC', 'CIS',
    'BI', 'EC', 'MATH', 'CIS', 'MATH', 'MATH', 'CIS', 'CIS', 'UNDL', 'MATH', 'CIS',
    'MUS', 'PBA', 'PS', 'CIS', 'CIS', 'CIS', 'UNDL', 'CIS', 'PBA', 'HPHY', 'UNDL',
    'ACTG', 'CEP', 'CIS', 'CIS', 'CIS', 'CIS', 'PHYS', 'CIS', 'CIS', 'MATH', 'MACS',
    'UNDL', 'CIS', 'CIS', 'CIS', 'UNDL', 'CIS', 'ERTH', 'CIS', 'CIS', 'CIS', 'CIS',
    'MATH', 'CIS', 'PBA', 'UNDL', 'UNDL', 'CIS', 'PHYS', 'BI', 'CIS', 'UNDL', 'CH',
    'CIS', 'EC', 'CIS', 'MATH', 'UNDL', 'CIS', 'GS', 'UNDL', 'UNDL', 'UNDL', 'MATH',
    'PSY', 'UNDL', 'CIS', 'CIS', 'UNDL', 'CIS', 'CIS', 'UNDL', 'CIS']
    """
    with open(fname, 'r') as myf:
        myf.readline()
        mylist = []
        for line in myf:
            values = line.strip().split()
            mylist.append(values[0])
    return mylist

def majors_analysis(majorsli):
    """(list) -> str

    Returns the most frequent item in a list.

    >>> majors_analysis(['cis', 'cis', 'cis', 'math', 'math', 'psy']
    cis
    >>> majors_analysis([])
    no items in list
    """
    if len(majorsli) == 0:
        error1 = "no items in list"
        return error1
    else:
        mostmajor = mode(majorsli)
        return mostmajor

def majors_report(majors_mode, majorsli):
    """(str, list) -> None

    reports the mode and a frequency table.
    """
    print("Most represented major(s):\n", majors_mode)
    frequencyTable(majorsli)
    return None

main()
