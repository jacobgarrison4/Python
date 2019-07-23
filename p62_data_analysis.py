"""
Data Analysis
CIS 210 F17 project 6

Authors: Jacob Garrison

Credits: Python Programming in Context

Data Analysis provides basic data analysis
including the mean, median, mode, and a frequency
table of a given set of data.
"""

def main():
    """(None) -> None

    >>> main()
    Mean:  3.780748663101608
    Median:  3.3
    Mode:  [2.5]
    ITEM FREQUENCY
    2.5      18
    2.6      15
    2.7      14
    2.8      12
    2.9      11
    3.0      4
    3.1      10
    3.2      6
    3.3      7
    3.9      1
    4.0      3
    4.1      3
    4.2      5
    4.3      6
    4.4      6
    4.5      6
    4.6      8
    4.7      6
    4.8      9
    4.9      9
    5.0      4
    5.1      6
    5.2      3
    5.3      4
    5.4      1
    5.5      1
    5.7      2
    5.8      1
    6.0      1
    6.2      1
    6.3      1
    6.4      1
    6.6      1
    6.7      1
    None

    main prints a report of the mean,
    median, mode, and a frequency
    table of earthquake data.
    """
    equakes = [5.3, 3.0, 2.6, 4.4, 2.9, 4.8, 4.3,
    2.6, 2.9, 4.9, 2.5, 4.8, 4.2, 2.6,
    4.8, 2.7, 5.0, 2.7, 2.8, 4.3, 3.1,
    4.1, 2.8, 5.8, 2.5, 3.9, 4.8, 2.9,
    2.5, 4.9, 5.0, 2.5, 3.2, 2.6, 2.7,
    4.8, 4.1, 5.1, 4.7, 2.6, 2.9, 2.7,
    3.3, 3.0, 4.4, 2.7, 5.7, 2.5, 5.1,
    2.5, 4.4, 4.6, 5.7, 4.5, 4.7, 5.1,
    2.9, 3.3, 2.7, 2.8, 2.9, 2.6, 5.3,
    6.0, 3.0, 5.3, 2.7, 4.3, 5.4, 4.4,
    2.6, 2.8, 4.4, 4.3, 4.7, 3.3, 4.0,
    2.5, 4.9, 4.9, 2.5, 4.8, 3.1, 4.9,
    4.4, 6.6, 3.3, 2.5, 5.0, 4.8, 2.5,
    4.2, 4.5, 2.6, 4.0, 3.3, 3.1, 2.6,
    2.7, 2.9, 2.7, 2.9, 3.3, 2.8, 3.1,
    2.5, 4.3, 3.2, 4.6, 2.8, 4.8, 5.1,
    2.7, 2.6, 3.1, 2.9, 4.2, 4.8, 2.5,
    4.5, 4.5, 2.8, 4.7, 4.6, 4.6, 5.1,
    4.2, 2.8, 2.5, 4.5, 4.6, 2.6, 5.0,
    2.8, 2.9, 2.7, 3.1, 2.6, 2.5, 3.2,
    3.2, 5.2, 2.8, 3.2, 2.6, 5.3, 5.5,
    2.7, 5.2, 6.4, 4.2, 3.1, 2.8, 4.5,
    2.9, 3.1, 4.3, 4.9, 5.2, 2.6, 6.7,
    2.7, 4.9, 3.0, 4.9, 4.7, 2.6, 4.6,
    2.5, 3.2, 2.7, 6.2, 4.0, 4.6, 4.9,
    2.5, 5.1, 3.3, 2.5, 4.7, 2.5, 4.1,
    3.1, 4.6, 2.8, 3.1, 6.3]
    #print("Mean: ", mean(equakes))
    #print("Median: ", median(equakes))
    #print("Mode: ", mode(equakes))
    #print(frequencyTable(equakes))

def mean(alist):
    """(list) -> float

    >>> mean([1])
    1.0
    >>> mean([1,2,3,4,5])
    3.0
    >>> mean([])
    'List empty'
    >>> mean('ceioso')
    'Input must be a list'
    >>> mean([1,2,3,'a'])
    'Input must be a list of integers'

    mean returns the mean value of alist.
    """
    if type(alist) != list:
        error1 = "Input must be a list"
        return error1
    elif len(alist) == 0:
        error2 = "List empty"
        return error2
    for x in alist:
        if type(x) == bool or type(x) == str:
            error3 = "Input must be a list of integers"
            return error3
    else:
        mean = sum(alist) / len(alist)
        return mean

def median(alist):
    """(list) -> int

    >>> median([1])
    1
    >>> median([1,2,3])
    2
    >>> median([1,2,3,4])
    2.5
    >>> median([])
    'List empty'
    >>> median('ceioso')
    'Input must be a list'
    >>> median([1,2,3,'a'])
    'Input must be a list of integers'

    median returns the middle value
    in a sorted list.
    """
    if type(alist) != list:
        error1 = "Input must be a list"
        return error1
    elif len(alist) == 0:
        error2 = "List empty"
        return error2
    for x in alist:
        if type(x) == bool or type(x) == str:
            error3 = "Input must be a list of integers"
            return error3
    else:
        copylist = alist[:]
        copylist.sort()
        if isEven(len(copylist)):
            rightmid = len(copylist) // 2
            leftmid = rightmid - 1
            median = (copylist[leftmid] + copylist[rightmid]) / 2
        else:
            mid = len(copylist) // 2
            median = copylist[mid]
    return median

def isEven(n):
    """(int) -> bool

    >>> isEven(1)
    False
    >>> isEven(6)
    True
    >>> isEven('a')
    'Input must be an integer'

    isEven returns true if n is
    even and false if n is odd.
    """
    if type(n) != int:
        error1 = "Input must be an integer"
        return error1
    else:
        if n % 2 == 0:
            return True
        else:
            return False

def mode(alist):
    """(list) -> int

    >>> mode([1])
    [1]
    >>> mode([1,1,4,5,6,2,4,7,4,6,1,4])
    [4]
    >>> mode([1,1,1,2,3,4,4,4,5,6,7])
    [1, 4]
    >>> mode([])
    'List empty'
    >>> mode('ceioso')
    'Input must be a list'
    >>> mode([1,2,3,'a'])
    'Input must be a list of integers'

    mode returns the value(s) that
    occurred most in alist.
    """
    if type(alist) != list:
        error1 = "Input must be a list"
        return error1
    elif len(alist) == 0:
        error2 = "List empty"
        return error2
    #for x in alist:
        #if type(x) == bool or type(x) == str:
            #error3 = "Input must be a list of integers"
            #return error3
    else:
        countdict = genFrequencyTable(alist)
        countlist = countdict.values()
        maxcount = max(countlist)
        modelist = []
        for item in countdict:
            if countdict[item] == maxcount:
                modelist.append(item)
    return modelist

def frequencyTable(alist):
    """(list) -> None

    >>> frequencyTable([3,1,1,5,3,1,2,2,3,5,3,5,4,4,6,7,6,7,5,7,8,3,8,2,3,4,1,5,6,7])
    ITEM FREQUENCY
    1      4
    2      3
    3      6
    4      3
    5      5
    6      3
    7      4
    8      2
    >>> frequencyTable([])
    'List empty'
    >>> frequencyTable('ceioso')
    'Input must be a list'
    >>> frequencyTable([1,2,3,'a'])
    'Input must be a list of integers'

    this function prints out a
    frequency table based on the
    number of times an element
    from a list is shown in alist.
    """
    if type(alist) != list:
        error1 = "Input must be a list"
        return error1
    elif len(alist) == 0:
        error2 = "List empty"
        return error2
    #for x in alist:
        #if type(x) == bool or type(x) == str:
            #error3 = "Input must be a list of integers"
            #return error3
    else:
        countdict = genFrequencyTable(alist)
        itemlist = list(countdict.keys())
        itemlist.sort()
        print("ITEM", "FREQUENCY")
        for item in itemlist:
            print(item, "    ", countdict[item])
    return None

def genFrequencyTable(alist):
    """(list) -> dict

    >>> genFrequencyTable([1,3,8,4,3,1,9,3,4,7,3,8,1,8,2])
    {1: 3, 2: 1, 3: 4, 4: 2, 7: 1, 8: 3, 9: 1}
    >>> genFrequencyTable([])
    'List empty'
    >>> genFrequencyTable('ceioso')
    'Input must be a list'
    >>> genFrequencyTable([1,2,3,'a'])
    'Input must be a list of integers'

    Creates a frequency list in a dictionary.
    """
    if type(alist) != list:
        error1 = "Input must be a list"
        return error1
    elif len(alist) == 0:
        error2 = "List empty"
        return error2
    #for x in alist:
        #if type(x) == bool or type(x) == str:
            #error3 = "Input must be a list of integers"
            #return error3
    else:
        countdict = {}
        for item in alist:
            if item in countdict:
                countdict[item] += 1
            else:
                countdict[item] = 1
    return countdict


