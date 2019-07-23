#Problem 0 (a)
def transcribe(S):
    '''(str) -> str
Function transcribes the letters in DNA to the letters in RNA.

transcribe('ACGT TGCA')
'UGCAACGU'
transcribe('GATTACA')
'CUAAUGU'
'''
    rna_string = ''
    for ch in S:
        if ch == 'A':
            rna_string += 'U'
        elif ch == 'C':
            rna_string += 'G'
        elif ch == 'G':
            rna_string += 'C'
        elif ch == 'T':
            rna_string += 'A'
        else:
            pass
    return rna_string
#Problem 0 (b)
def transcribe1(S):
    '''(str) -> str
Function transcribes the letters in DNA to the letters in RNA.

transcribe('ACGT TGCA')
'UGCAACGU'
transcribe('GATTACA')
'CUAAUGU'
'''
    rna_string = ''
    ctr = 0
    while ctr < len(S):
        x = S[ctr]
        if x == 'A':
            rna_string += 'U'
        elif x == 'C':
            rna_string += 'G'
        elif x == 'G':
            rna_string += 'C'
        elif x == 'T':
            rna_string += 'A'
        else:
            pass
        ctr += 1
    return rna_string

#Problem 1
from turtle import *
import random
def mars_explore_main(num_trips):
    '''() -> None

    main function for mars_explore:
        set up print and graphical output
        then call mars_explore repeatedly

    data is printed; None value is returned

    >>> mars_explore_main()
    '''
    # label for print output   
    print("xpos", "\t",
          "ypos", "\t",
          "water", "\t",
          "temp")           

    # set up graphical output
    reset()
    title("Mars Rover")
    display_color = "blue"
    color(display_color)
    shape('square')
    stamp()   # draw the rover

    speed(0)
    cntr = 0
    while cntr <= num_trips:
        mars_explore()
        cntr += 1
    return None
    
def rover_loc():
    '''() -> int
return random number for rover location

>>>rover_loc()
120
'''
    return random.randint(-275,275)

def water_content():
    '''() -> int
return random number for water content in ppm

>>>water_content()
56
'''
    return random.randint(1,290)

def temperature():
    '''() -> int
return random number for temperature in fahrenheit

>>>temp()
-107
'''
    return random.randint(-178,1)

def mars_explore():
    '''() -> (int, int, int, int)
return random numbers for location, water content and temperature

>>>mars_explore
7 -54 128 -120
'''
    x = rover_loc()
    y = rover_loc()
    xpos = x
    ypos = y
    water = water_content()
    temp = temperature()
    setposition(x,y)
    stamp()
    print(xpos, '\t', ypos, '\t', water, '\t', temp)
    return #None

#Problem 2
from turtle import *

def spirolateral(name):
    '''(string) -> None

    Draw a spirolateral of the input name.
    No value is returned.

    For example,
    spirolateral('Ducks')
    '''
    name = name.upper() 
    start = ord('A')
    multiplier = 5

    ctr = 0
    while ctr < len(name):
        ch = name[ctr]
        letter_place = ord(ch) - start + 1
        fd(letter_place * multiplier)
        rt(90)
        ctr += 1

    return #None

def spirolateral2(name):
    '''(string) -> None

    Draw a spirolateral of the input name.
    No value is returned.

    For example,
    spirolateral('Ducks')
    '''
    name = name.upper() 
    start = ord('A')
    multiplier = 5

    for ch in name:
        letter_place = ord(ch) - start + 1
        fd(letter_place * multiplier)
        rt(90)

    return #None

def spirolateral_main(name):
    '''(str) -> None
Calls the function spirolateral as many times as there are letters in name
'''
    cntr = 0
    while cntr < (len(name)):
        spirolateral(name)
        cntr += 1
    return None

#Problem 3
def rats(weight, rate):
    '''(number, number) -> int
Function prints rats weight each week until rat weighs 1.5 times
its original weight. Then prints how many weeks it took.
'''
    time = 0
    start_weight = weight
    while weight <= (1.5 * start_weight):
        print(round(weight, 3))
        weight = weight + (rate * weight)
        time += 1

    print("It took", time, "weeks for the rat to weigh 1.5 times its original weight")
    
#Problem 4 (a)
    '''(str) -> None
Function prints True if a character in the string is upper case
and prints False otherwise.
'''
def any_uc_alpha(astring):
    for x in astring:
        if x.isupper():
            return True
        else:
            return False
        
#Problem 4 (b)
        '''(str) -> None
Function prints True if there are at least 2 numbers in the string,
prints False otherwise.
'''
def two_numbers(astring):
    cntr = 0
    for x in astring:
        if x.isdigit():
            cntr += 1
        if cntr>= 2:
            return True
        else:
            return False
    if astring.isdigit() >= 2:
        return True
    else:
        return False
    
#Problem 4 (c)
    '''(str) -> None
Function prints True if there are any special characters in astring,
prins False otherwiser.
'''
    def any_special_char(astring):
        string_ch = 0
        for x in astring:
            if x == '!' or x == '@' or x == '#' or x == '$' or x == '%' or x == '^' or x == '&':
                string_ch += 1
        if string_ch >= 1:
            return True
        else:
            return False
