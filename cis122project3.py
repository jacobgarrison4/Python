#Problem 0
#Part 1
def max_trans1(a,b,c):
    ''' (int) -> int
input three different weight limits for three bridges
and it returns the max weight limit that can be transported.

>>>max_trans(1,2,3)
1
>>>max_trans1(9,6,3)
3
>>>max_trans1(0,0,0)
0
'''
    return min(a,b,c)

#Part 2
def max_trans2(a,b,c,d,e):
    ''' (int) -> int
input five weight limits from five bridges that make two paths,
and it returns the max weight limit that can be transported.

>>>max_trans2(126,238,326,413,515)
413
>>>max_trans2(222,110,411,54,73)
110
>>>max_trans2(227,337,135,56,73)
135
'''
    x = min(a,b,c)
    y = min(d,e)
    return max(x,y)

#Problem 1
def tip_calc(bill):
    ''' (float) -> float
input total restaraunt bill and it returns the tip amount
of 18% of the bill.

>>>tip_calc(28.60)
$5.15
>>>tip_calc(48)
$8.64
>>>tip_calc(10)
$1.8
'''
    tip = '$' + str(round((bill * .18),2))
    print(tip)

#Problem 2
def nice_name():
    '''(str) -> str
Input name and it will output your name surrounded by stars.
'''
    name = input('What is your name?')
    print('**..**>..<**..**>..<\n..    ', str.upper(name), '\t  ..\n>..<**..**>..<**..**')

#Problem 3
def monogram():
    ''' (str, str, str) -> str
Input your first name, middle initial, and last name, and it
will output your capitalized initials in monogram order.
'''
    FN = input('Please enter your first name')
    MI = input('Please enter your middle initial')
    LN = input('Please enter your last name')
    print(str.upper(FN[0]) + str.upper(LN[0]) + str.upper(MI))

#Problem 4
def char_ct(s1, s2, ch):
    '''(str, str, str) -> int

    precpndition: len(ch) == 1

    Returns the total number of times that ch occurs in s1 and s2.

    >>>char_ct('color', 'yellow', 'l')
    3
    >>>char_ct('red', 'blue', 'l')
    1
    >>>char_ct('green', 'purple', 'b')
    0
    '''
    return (s1 + s2).count(ch)
