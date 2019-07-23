#Jacob Garrison
#ZiptoBar takes a zip code and it in bafr code form in turtle graphics
#CIS 210 Project 5.1

import time	# Used to pause program before exit
import turtle	# Used in function to print the bar code

SLEEP_TIME = 30	# number of seconds to sleep after drawing the barcode
ENCODINGS = [[1, 1, 0, 0, 0],	# encoding for '0'
             [0, 0, 0, 1, 1],	# encoding for '1'
             [0, 0, 1, 0, 1],   # encoding for '2'
             [0, 0, 1, 1, 0],	# encoding for '3'
             [0, 1, 0, 0, 1],	# encoding for '4'
             [0, 1, 0, 1, 0],	# encoding for '5'
             [0, 1, 1, 0, 0],	# encoding for '6'
             [1, 0, 0, 0, 1],	# encoding for '7'
             [1, 0, 0, 1, 0],	# encoding for '8'
             [1, 0, 1, 0, 0]	# encoding for '9'
            ]
SINGLE_LENGTH = 25	# length of a short bar, long bar is twice as long

def compute_check_digit(digits):
    """
    Compute the check digit for use in ZIP barcodes
    args:
        digits: list of 5 integers that make up zip code
    returns:
        check digit as an integer
    """
    digits = str(digits)
    sum = 0
    for i in range(len(digits)):
        sum = sum + int(digits[i])
    check_digit = 10 - (sum % 10)
    if (check_digit == 10):
        check_digit = 0
    return check_digit

def draw_bar(my_turtle, digit):
    '''(turtle, int) -> turtle graphic

    draws one line of a bar code either full
    or half length

    >>>draw_bar(turtle, 9)

    '''
    my_turtle.left(90)
    if digit == 0:
        length = SINGLE_LENGTH
    else:
        length = 2 * SINGLE_LENGTH
    my_turtle.forward(length)
    my_turtle.up()
    my_turtle.backward(length)
    my_turtle.right(90)
    my_turtle.forward(10)
    my_turtle.down()

def draw_zip(my_turtle, zip):
    '''(turtle, int) -> turtle graphic

    Takes a zip code anf uses the draw_bar function
    to represent specific numbers in a zip code

    >>>draw_zip(turtle, 97267)

    '''
    ct = 0
    draw_bar(my_turtle, 1)
    while ct < 5:
        a = str(zip)
        num = int(a[ct])
        for i in range(len(a)):
            draw_bar(my_turtle, ENCODINGS[num][i])
        ct += 1

    for i in range(len(a)):
        draw_bar(my_turtle, ENCODINGS[compute_check_digit(zip)][i])
    draw_bar(my_turtle, 1)
