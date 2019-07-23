"""
Binary Encoding and Decoding
CIS 210 F17 Project 4

Authors: Jacob Garrison

Credits: Python Programming in Context

Takes input from user, a non-negative integer, and
converts it to binary and prints it. Then converts
back to decimal form and prints the value.
"""

def main():
    """(None) -> None

    Asks user for input and changes the
    input to binary then back to the
    original.
    """
    number = int(input("Enter a non-negative integer: "))
    binary = dtob(number)
    print(binary)
    decimal = btod(binary)
    print(decimal)

def dtob(n):
    """(int) -> str

    Takes non-negative integer and returns
    its binary representation.

    >>> dtob(27) #Basic
    '11011'
    >>> dtob(0) #Edge
    '0'
    >>> dtob(2)
    '10'
    """
    binary = ''
    if n == 0:
        return '0'
    while n > 0:
        remainder = str( n % 2 )
        n = n // 2
        binary += remainder

    binary = binary[::-1]

    return binary

def btod(b):
    """(str) -> int

    Takes a binary representation of an integer
    as input and returns the corresponding integer.

    >>> btod('0') #Edge
    0
    >>> btod('1101') #Basic
    13
    >>> btod('111111')
    63
    """
    decimal = 0
    power = len(b) - 1
    for ch in b:
        num = int(ch)
        decimal += ( num * ( 2 ** power) )
        power -= 1

    return decimal

def dtobr(n):
    """(int) -> str

    Same as dtob, only a recursive version.

    >>> dtobr(27) #Basic
    '11011'
    >>> dtobr(0) #Edge
    '0'
    >>> dtobr(-1)
    'n must be a positive integer'
    >>> dtobr(2)
    '10'
    >>> dtobr(44)
    '101100'
    >>> dtobr('n')
    'n must be a positive integer'
    """
    if type(n) != int or n < 0:
        return 'n must be a positive integer'
    if n == 0:
        return '0'
    if n == 1:
        return '1'
    remainder = str( n % 2 )
    num = n // 2
    return dtobr(num) + remainder

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

main()
