"""
Square Root
CIS 210 F17 Project 2

Authors: Jacob Garrison

Credits: Python Programming in Context

Approximate sqrt of a given number with iterative function
"""

from math import *

def mysqrt(n, k):
    """(int, int) -> float

    Returns an approximation of the square root
    of a givven number after a given number
    of iterations through a function.

    >>> mysqrt(25, 5)
    5.000023178253949
    >>>  mysqrt(25, 10)
    5.0
    >>> mysqrt(10000, 10)
    100.00000025490743
    """
    value = 1
    for x in range( 1 , k + 1 ):
        value = round( ( ( 1 / 2 ) * ( value + ( n / value ) ) ) , 5 )
        
    return value

def sqrt_compare(number, iterations):
    """(int, int) -> int

    Calls mysqrt function to find square root
    through a function and compares it to
    the math lib sqrt value and returns a
    percdentage error.

    >>> sqrt_compare(10000, 8)
    For 10000 using 8 iterations:
    mysqrt value is: 101.20218365353946
    math lib sqrt value is: 100.0
    This is a 1.2 percent error.
    """
    
