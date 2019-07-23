import doctest

#(0)
def ttriangle(n):
    '''int -> None

    Prints a right triangle with n lines,
    where the first line prints 1 'T'
    and the last line prints n 'T's.
    If n is <= 0, do not print anything.
    None value is returned.

    >>> ttriangle(6)    
    T
    TT
    TTT
    TTTT
    TTTTT
    TTTTTT

    >>> ttriangle(1)
    T

    >>> ttriangle(0)
    >>>

    >>> ttriangle(-3)
    >>>

    >>> ttriangle(4)
    T
    TT
    TTT
    TTTT
    '''
    ct = 1
    while ct <= n:   #Changed from < to <=       
        print('T' * ct)
        ct += 1

    return #None

#(1)
def find_min_and_max(values):
    '''(string) -> None

    Find the maximum and minimum values in a
    non-empty string of integers and print them.
    None value is returned.

    Precondition: all characters in values are
    integers between 0 and 9 inclusive

    >>> find_min_and_max('45312')   #normal min 1 max 5
    The minimum value is 1.
    The maximum value is 5.

    >>> find_min_and_max('8675309')
    The minimum value is 0.
    The maximum value is 9.

    >>> find_min_and_max('0')
    The minimum value is 0.
    The maximum value is 0.

    >>> find_min_and_max('111')
    The minimum value is 1.
    The maximum value is 1.

    >>> find_min_and_max('684148')
    The minimum value is 1.
    The maximum value is 8.

    >>> find_min_and_max('4444777755666666')
    The minimum value is 4.
    The maximum value is 7.

    >>> find_min_and_max('65')
    The minimum value is 5.
    The maximum value is 6.
    '''
    mmin = '0'        
    mmax = '0'       
    for value in values:
        if value > mmax:
            mmax = value
        if value < mmin:
            mmin = value

    #print('The minimum value is', mmin)
    #print('The maximum value is', mmax) #Changed minimum to maximum

    #or
    print('The minimum value is {}.'.format(mmin))
    print('The maximum value is {}.'.format(mmax)) #Added a period at the end

    return #None

#(2)
def my_average(dataset):
    '''(string) -> float

    Returns average of values in input string values,
    but zeros do not count at all.  Return 0 if there
    is no real data.

    Precondition: all characters in dataset are
    integers between 0 and 9 inclusive
    
    >>> my_average('23')    #normal, no zeros
    2.5
    >>> my_average('203')   #normal, a zero
    2.5
    >>> my_average('0')
    0
    >>> my_average('')
    0
    >>> my_average('8675309')
    6.333333333333333
    >>> my_average('02020202')
    2.0
    >>> my_average('000')
    0
    >>> my_average('0123456789')
    5.0
    '''
    count = 0
    total = 0
    for value in dataset:
        if value != '0':
            total += int(value)
            count += 1
        if value == '0':        #Added if statement so the count would not
            total += int(value) #go up when the value was '0'
            count ==  count
    if count == 0:              #Added if statement so when there was no real
        print('0')              #data, it would return '0'
    elif count >= 0:
        avg = total / count
        return avg

#(3)
def minutesToHours(minutes):
    '''(number) -> float

    convert input minutes to hours;
    return hours

    >>> minutesToHours(60)
    1.0
    >>> minutesToHours(90)
    1.5
    >>> minutesToHours(0)
    0.0
    '''
    hours = minutes / 60
    hours = round(hours, 2)
    return hours            #Changed 'print' to 'return'
    
def hoursToDays(hours):
    '''(number) -> float

    convert input hours to days;
    return days

    >>> hoursToDays(24)
    1.0
    >>> hoursToDays(100)
    4.17
    >>> hoursToDays(0)
    0.0
    '''
    days = hours / 24
    days = round(days, 2)   #Added so it would round properly
    return days

def daysToYears(days):
    '''(number) -> float

    convert input days to years;
    return years

    >>> daysToYears(365)
    1.0
    >>> daysToYears(100)
    0.27
    >>> daysToYears(0)
    0.0
    '''
    years = days / 365      #Deleted 'days = 365' because it was always
    years = round(years, 2) #making years == 1.0
    return years

def minutesToYears(m):
    '''(int) -> float

    input number m minutes is converted to
    equivalent number of years. return years.
    call auxiliary functions to do each step

    >>> minutesToYears(525600)
    1.0
    >>> minutesToYears(5256000)
    10.0
    >>> minutesToYears(394200)
    0.75
    >>> minutesToYears(0)
    0.0
    '''
    w = minutesToHours(m)   #Added vaiables so we could jump between functions
    x = hoursToDays(w)
    y = daysToYears(x)

    return y
    
