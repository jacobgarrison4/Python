#Jacob Garrison
#strReverse takes a string and returns the string in reverse
#CIS 210 Project 5.2

def strReverseR(s):
    """(str) -> None

    Takes a string argument and returns the string in reverse.

    >>>strReverseR('CIS 210')
    '012 SIC'
    """
    if s == 1:
        return s
    elif len(s) == 0:
        return s
    else:
        return s[-1] + strReverseR(s[:-1])
    return s

def strReverseL(s):
    '''(str) -> None

    strReverseL takes a string and returns the string in reverse

    >>>strReverseL('happy')
    'yppah'
    '''

    letters = list(s)
    reverse_letters = []
    x = int(len(s))
    while x > 0:
        reverse_letters += letters[x-1]
        x -= 1
    else:
        return ''.join(reverse_letters)
        print(reverse_letters)
    
