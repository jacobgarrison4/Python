#(0)
def double_preceding(values):
    '''(list of ints) -> None

    Update each value in a list
    with twice the preceding
    value, and the first item
    with 0.

    >>>double_preceding(1,2,3,4,5)
    0 2 4 6 8
    >>>double_preceding(2,-4,6,-8,10)
    0 4 -8 12 -16
    >>>double_preceding(0,0,0,0,0)
    0 0 0 0 0
    >>>double_preceding(-5,-4,-3,-2,-1)
    0 -10 -8 -6 -4
    '''
    temp = values[0]
    values[0] = 0
    for i in range(1,len(values)):
        values[i], temp = temp * 2, values[i]
    print(values)

#(1)
def passwordChecker(psw):
    '''(str) -> boolean

    Checks password to see if
    it passes all of the rules
    that SecuriCorp has set; returns
    True if password is secure,
    returns False otherwise.

    >>>	passwordChecker('111111')			
	False
    >>>	passwordChecker('#Qwerty')
        False
    >>>	passwordChecker('#qwErty')
        False
    >>>	passwordChecker('#Qw9rty')				
	False
    >>>	passwordChecker('#Qw99rty')
	True
    >>>	passwordChecker('Two34!')		
	False
    >>>	passwordChecker('A99!')				
	False
    >>>	passwordChecker('Abyz9!')			
	False
    >>>	passwordChecker('qwerty99!')	
	False
    >>>	passwordChecker('Qwerty99')		
	False
    >>>	passwordChecker('')
	False
    >>>	passwordChecker('OK99!!')
	True
    >>>	passwordChecker('$100abC')
        True
    '''
    if frequent(psw) is False or length(psw) is False or capital(psw) is False or numbers(psw) is False or bad_letter(psw) is False or symbol(psw) is False:
        return False
    else:
        return True
    
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

    frequent_passwords = ['password','Two34!','qwerty','letmein','trustno1','111111','passw0rd']
    if psw in frequent_passwords:
        return False
    else:
        return True
    
def length(psw):
    if len(psw) >= 5:
        return True
    else:
        return False

def capital(psw):
    ct = 0
    for ch in psw:
        if ch.isupper():
            ct += 1
    if ct >= 1:
        return True
    else:
        return False

def numbers(psw):
    ct = 0
    for ch in psw:
        if ch.isdigit():
            ct += 1
    if ct >= 2:
        return True
    else:
        return False

def bad_letter(psw):
    if 'E' in psw or 'e' in psw:
        return False
    else:
        return True

def symbol(psw):
    ct = 0
    spec_symb = ['!','@','#','$','%','^','&']
    for ch in psw:
        if ch in spec_symb:
            ct += 1
    if ct >= 1:
        return True
    else:
        return False

#(2)
def processfile():
    '''(file open for reading) -> None

    Function opens a file, creates
    a list of each item in the file,
    sorts the list, and prints it.

    For	example, for a text file that lists the	days of	the week:
    Monday
    Tuesday
    Wednesday
    Thursday
    Friday	Saturday	Sunday
    
    >>> processfile('project9.txt')
    Friday	Saturday	Sunday
    Monday
    Thursday
    Tuesday
    Wednesday
    '''
    file = open('favorite_foods.txt','r')
    contents = file.readlines()
    x = list(contents)
    x.sort()
    for food in x:
        print(food)

#(3)
import calendar
def whatDay(day,month,year):
    '''(int,int,int) -> str

    Function takes input of day,
    month, and year, and returns
    the day of the week of which
    the date will be on.

    >>> whatDay(13,10,2015)
    Tuesday
    '''
    day = calendar.weekday(year,month,day)
    if day == 0:
        print('Monday')
    if day == 1:
        print('Tuesday')
    if day == 2:
        print('Wednesday')
    if day == 3:
        print('Thursday')
    if day == 4:
        print('Friday')
    if day == 5:
        print('Saturday')
    if day == 6:
        print('Sunday')
    return None






















    
