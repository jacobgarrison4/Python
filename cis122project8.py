import doctest

#(0)
def same_first_last(L):
    '''(list) -> boolean

    Precondition:  len(L) >= 2
    

    Returns True if the first item of the list is
    the same as the last; else returns False.


    >>> same_first_last([3, 4, 2, 8, 3])
    True
    >>> same_first_last(['apple', 'banana', 'pear'])
    False
    >>> same_first_last([4.0, 4.5])
    False
    '''

    return L[0] == L[-1]

#(1)
def is_longer(L1, L2):
    '''(list, list) -> boolean


    Return True if the length of L1
    is longer than the length of L2;
    else return False


    >>> is_longer([1, 2, 3], [4, 5])
    True
    >>> is_longer(['abcdef'], ['ab', 'cd'])
    False
    >>> is_longer(['a', 'b', 'c'], [1, 2, 3])
    False
    '''
    
    return len(L1) > len(L2)

#(2)
def frequent(psw):
    '''(str) -> boolean

    Return False if psw in in
    a list of frequently used
    passwords; else returns True.

    >>> frequent('password')
    False
    >>> frequent('Bond007')
    True
    >>> frequent('trustno1')
    False
    '''

    frequent_passwords = ['password','One234!','qwerty','letmein','trustno1','111111','passw0rd']
    if psw in frequent_passwords:
        return False
    else:
        return True


#(3)
def mySum(L):
    '''(list) -> int

    precondition: L must contain only integers

    Returns the sum of all
    of the integers in the
    list L.

    >>> mySum([1,2,3])
    6
    >>> mySum([2,4,6,2])
    14
    >>> mySum([])
    0
    >>> mySum([1,2,3,-2])
    4
    '''

    total = 0
    for num in L:
        total += num
    return total

#(4)
def middle(L):
    '''(list) -> int

    When L is odd, it returns
    the item in the middle of
    the list L' otherwise,
    returns 999999.

    >>> middle([8,0,100,12,1])
    100
    >>> middle([8,0,100,12])
    999999
    >>> middle([])
    999999
    >>> middle(['middle',7,'art',22,89,'seventeen',65])
    22
    '''

    if len(L) % 2 != 1:
        print('999999')
    else:
        return L[((len(L)-1)//2)]

    
#(5)
def check(cardnum):
    '''(str) -> boolean

    <function description goes here>
    
    >>> check('2768 3424 2345 2358')
    False
    >>> check('9384 3495 3297 0121')
    True
    >>> check('1876 0954 325009182')
    False
    >>> check('0000000000000000')
    False
    >>> check('0000 0000 0000 000')
    False
    >>> check('0 0 0 0000000000000')
    False
    >>> check('')
    False
    >>> check('0000 0000')
    False
    >>> check('0123 4567 8902 4568')
    True
    >>> check('0123 4567 89AB EFGH')
    False
    >>> check('0123 4567 89AB 5555')
    False
    '''

    if len(cardnum) != 19 or cardnum[4] != ' ' or cardnum[9] != ' ' or cardnum[14] != ' ':
        return False
    cardnum = cardnum.replace(" ", '')
    if len(cardnum) != 16 or not cardnum.isdigit():
        return False
    L = map(int, cardnum)
    if sum(L) % 10 != 0:
        return False
    return True



        


    

    




    

    

