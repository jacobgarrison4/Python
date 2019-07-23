'''
Jacob Garrison

Finds the position of a target value within a given sorted list

CIS 210 Winter 2016
'''
import doctest

def is_memberR(alist, number):
    """
    Takes a sorted list of integers and serarches the list
    for a given number. Returns True if the number is in
    the list and False otherwise.

    >>> is_memberR([1,3,5,7],6)
    False
    >>> is_memberR([0,1,2,5,8,9],5)
    True
    >>> is_memberR([0,1,2,5,8,9],3)
    False
    >>> is_memberR([0,1,4,5,6,8],4)
    True
    >>> is_memberR([0,1,2,3,4,5,6],3)
    True
    >>> is_memberR([1,3],1)
    True
    >>> is_memberR([2,10],10)
    True
    >>> is_memberR([99,100],101)
    False
    >>> is_memberR([42],42)
    True
    >>> is_memberR([43],44)
    False
    >>> is_memberR([],99)
    False
    """
    if len(alist) == 0:
        return False
    num = alist[len(alist)//2]
    if number == num:
        return True
    elif len(alist) == 1:
        return False
    elif number < num:
        return is_memberR(alist[:len(alist)//2], number)
    elif number > num:
        return is_memberR(alist[len(alist)//2:], number)
    else:
        return False

def is_memberI(alist, number):
    """
    Takes a sorted list of integers and serarches the list
    for a given number. Returns True if the number is in
    the list and False otherwise.

    >>> is_memberI([1,3,5,7],4)
    False
    >>> is_memberI([0,1,2,5,8,9],3)
    False
    >>> is_memberI([0,1,4,5,6,8],4)
    True
    >>> is_memberI([0,1,2,3,4,5,6],3)
    True
    >>> is_memberI([1,3],1)
    True
    >>> is_memberI([2,10],10)
    True
    >>> is_memberI([99,100],101)
    False
    >>> is_memberI([42],42)
    True
    >>> is_memberI([43],44)
    False
    >>> is_memberI([],99)
    False
    """
    if len(alist) ==0:
        return False
    first = 0
    last = len(alist)-1
    found = False
    while first <= last and not found:
        middle = (first + last) // 2
        if alist[middle] == number:
            found = True
        else:
            if number < alist[middle]:
                last = middle - 1
            else:
                first = middle + 1

        return found

def test_is_member(f):
    if ((f([1,3,5,7],6)) == False and\
       (f([0,1,2,5,8,9],5)) == True and\
       (f([0,1,2,5,8,9],3)) == False and\
       (f([0,1,4,5,6,8],4)) == True and\
       (f([0,1,2,3,4,5,6],3)) == True and\
       (f([1,3],1)) == True and\
       (f([2,10],10)) == True and\
       (f([99,100],101)) == False and\
       (f([42],42)) == True and\
       (f([43],44)) == False and\
       (f([],99)) == False):
        return True
    else:
        return False
       
print(doctest.testmod())
