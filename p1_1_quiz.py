''' 
CIS 210 STYLE
CIS 210 F17 Project 1

Author: Jacob Garrison

Credits: N/A

Add docstrings to Python functions implementing quiz 1 pseudocode.
'''

def q1(onTime, absent):
    '''(bool, bool) -> str

    Returns one of three responses based on whether
    or not a student was on time, absent, or neither.

    >>> q1(False, False)
    Better late than never.
    >>> q1(True, False)
    Hello!
    >>> q1(False, True)
    Is anyone there?
    '''
    if onTime:
        print('Hello!')
    elif absent:
        print('Is anyone there?')
    else:
        print('Better late than never.')

    return None

#q1(False, False)

def q2(age, salary):
    '''(int, int) -> bool

    Returns a Boolean based on if a person
    is under the age of 18 AND if they
    have a salary of less than 10000.

    >>> print(q2(18, 5000))
    False
    >>> print(q2(16, 5000))
    False
    >>> print(q2(20, 15000))
    True
    '''
    return (age < 18) and (salary < 10000)

#print(q2(18, 5000))
#print(q2(16, 5000))

def q3():
    '''(None) -> int

    Returns 4 if p > q, returns 5 if p < q AND q > 4,
    and returns 6 if p < q AND q < 4.
    Note: With p and q set inside the function
    q3 will always return only one result, 6.

    >>> print(q3())
    6
    '''
    p = 1
    q = 2
    result = 4
    if p < q:
        if q > 4:
            result = 5
        else:
            result = 6

    return result

#print(q3())

def q4(balance, deposit):
    '''(int, int) -> int

    Starts with a given balance and deposit
    amount and returns the new balance
    after the deposit amount has been
    added 10 times.

    >>> print(q4(100, 10))
    200
    '''
    count = 0
    while count < 10:
        balance = balance + deposit
        count += 1

    return balance

#print(q4(100, 10))

def q5(nums):
    '''(list) -> int

    Iterates through a list and returns
    the total number of positive integers
    in the list.

    >>> print(q5([0, 1, 2, 3, 4, 5]))
    6
    >>> print(q5([0, -1, 2, -3, 4, -5]))
    3
    '''
    result = 0
    i = 0
    while i < len(nums):
        if nums[i] >= 0:
            result += 1

        i += 1

    return result

#print(q5([0, 1, 2, 3, 4, 5]))
#print(q5([0, -1, 2, -3, 4, -5]))

def q6():
    '''(None) -> str

    Returns p after multiplying itself
    4 times.
    Note: The bug was in the while loop
    where it said i = 1. This would have
    created an infinite loop.

    >>> q6()
    2-power is 16
    '''
    i = 0
    p = 1
    while i < 4:
        p = p * 2
        i += 1

    print('2-power is', p)
    return None


#q6()


