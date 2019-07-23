"""
Test Reverse
CIS 210 F17 Project 6

Authors: Jacob Garrison

Credits: N/A

test_reverse is an automated testing
function for string reverse functions.
"""
from p52_stringreverse import *

def main():
    """(None) -> None

    main calls the test_reverse
    function with both of the
    string reverse functions
    as its input.
    """
    test_reverse(strReverseI)
    test_reverse(strReverseR)
    return None

def test_reverse(f):
    """(function) -> None

    test_reverse is an automated
    testing function which tests
    the string reverse functions
    and prints out a summary of
    the test.

    >>> test_reverse(strReverseR)
    Checking  ... its value  is correct!
    Checking a ... its value a is correct!
    Checking xyz ... its value zyx is correct!
    Checking testing123 ... its value 321gnitset is correct!
    Checking hello, world ... its value dlrow ,olleh is correct!
    """
    tests = ['', 'a', 'xyz', 'testing123', 'hello, world']
    answers = ['', 'a', 'zyx', '321gnitset', 'dlrow ,olleh']
    answer = 0
    for test in tests:
        print("Checking", test, '...', end='')
        result = f(test)
        if result == answers[answer]:
            print(' its value', result, 'is correct!')
        else:
            print(' Error: has wrong value', result, "expected ", answers[answer])
        answer += 1
    return None

main()
