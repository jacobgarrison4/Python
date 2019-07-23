"""
String Reverse
CIS 210 F17 Project 5

Authors: Jacob Garrison

Credits: Python Programming in Context

stringreverse takes a string and returns the string in reverse,
both iteratively and recursively.
"""

def main():
    """(None) -> None

    main asks the user for input and uses
    the input to call stringreverse.
    """
    string = str(input("Enter a string to be reversed: "))
    print(strReverseR(strReverseI(string)))

def strReverseR(s):
    """(str) -> None

    Takes a string argument and returns the string in reverse.

    >>> strReverseR('CIS 210') #Basic
    '012 SIC'
    >>> strReverseR('c') #Boundary
    'c'
    >>> strReverseR('') #Empty
    ''
    """
    if s == 1:
        return s
    elif len(s) == 0:
        return s
    else:
        return s[-1] + strReverseR(s[:-1])
    return s

def strReverseI(s):
    '''(str) -> None

    strReverseL takes a string and returns the string in reverse

    >>> strReverseI('happy')#Basic
    'yppah'
    >>> strReverseR('h') #Boundary
    'h'
    >>> strReverseR('') #Empty
    ''
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

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

#main()
