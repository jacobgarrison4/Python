'''
Jacob Garrison

Finds the position of a target value within a given sorted list

CIS 210 Winter 2016
'''

def is_memberR(alist, number):
    """
    Takes a sorted list of integers and serarches the list
    for a given number. Returns True if the number is in
    the list and False otherwise.

    is_memberR([1,3,5,7],6)
    False
    is_memberR([0,1,2,5,8,9],5)
    True
    """
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

    is_memberI([1,3,5,7],6)
    False
    is_memberI([0,1,2,5,8,9],5)
    True
    """
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
