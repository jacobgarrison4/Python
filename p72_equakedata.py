"""
Earthquake data
CIS 210 F17 project 7

Author: Jacob Garrison

Credits: Python Programming in Context

Analyises earthquake data
"""
from p62_data_analysis import *

def main():
    '''()-> None

    Calls: equake_readf, equake_analysis, equake_report
    Top level function for earthquake data analysis.

    Returns None.
    '''
    fname = 'equake25f.txt'
    mags = equake_readf(fname)
    mmm = equake_analysis(mags)
    equake_report(mmm, mags)
    return None

def equake_readf(fname):
    """(str) -> list

    Reads the magnitudes from a file
    and returns them in a list.

    >>> equake_readf('equake50f.txt')
    [5.2, 5.1, 6.0, 5.9, 5.6, 5.7, 5.0, 5.0, 5.2, 5.1, 5.4, 5.2, 5.6]
    """
    with open(fname, 'r') as myf:
        myf.readline()
        mylist = []
        for line in myf:
            values = line.split(',')
            mylist.append(float(values[4]))
    return mylist

def equake_analysis(magnitudes):
    """(list) -> tuple

    Analyses and returns the mean,
    median, and mode of magnitudes.

    >>> equake_analysis([5.2, 5.1, 6.0, 5.9, 5.6, 5.7, 5.0, 5.0, 5.2, 5.1, 5.4, 5.2, 5.6])
    [5.384615384615385, 5.2, [5.2]]
    """
    qmean = mean(magnitudes)
    qmed = median(magnitudes)
    qmode = mode(magnitudes)
    data = []
    data.append(qmean)
    data.append(qmed)
    data.append(qmode)
    return data

def equake_report(mmm, magnitudes):
    """(tuple, list) -> None

    Reports the mean, median, and
    mode of earthquake data. Also
    prints a frequency table.
    """
    qmean = mmm[0]
    qmed = mmm[1]
    qmode = mmm[2]
    count = len(magnitudes)
    print("There have been", count, "earthquakes over the past 25 years.")
    print("Mean magnitude is: ", qmean)
    print("Median magnitude is: ", qmed)
    print("Mode(s) of magnitude is: ", qmode)
    frequencyTable(magnitudes)
    return None

main()
