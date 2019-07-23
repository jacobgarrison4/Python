'''Jacob Garrison
Project 8
CIS 210 W16
'''

def mean(alist):
    mean = sum(alist) // len(alist)
    return mean

def genFrequencyTable(alist):
    countd = {}

    for i in alist:
        if i in countd:
            countd[i] += 1
        else:
            countd[i] = 1

    itemlist = list(countd.keys())
    itemlist.sort()

    print("Major", "Frequency")

    for k in itemlist:
        print(k, "        ", countd[k])


def mode(alist):
    countdict = {}

    for item in alist:
        if item in countdict:
            countdict[item] += 1
        else:
            countdict[item] = 1

    countlist = countdict.values()
    maxcount = max(countlist)

    modelist = [ ]
    for item in countdict:
        if countdict[item] == maxcount:
            modelist.append(item)
            
    return modelist

def majorsf_to_li(majorsf):
    alist = []
    for lines in majorsf:
        alist.append(lines)

    return alist

def frequencyTable(alist):
    gft = genFrequencyTable(alist)

    return gft

def report(alist):
    print("Most represented Major:")
    print(mode(alist))
    frequencyTable(alist)

def majors_main():
    '''() -> None

    Calls:  majorsf_to_li, report

    Top level function for analysis of
    data in file of majors of students
    in CIS 210 W16.

    Access major file, create list
    of relevant data, and report the mode
    and frequency table for the data in the file.

    Returns None.

    >>> majors_main()
    '''
    with open('majors_CIS210_W16.txt', 'r') as majorsf:
        
        majorsli = majorsf_to_li(majorsf)
        
    report(majorsli)

    return None
        
