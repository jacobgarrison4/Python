'''
FizzBuzz Game
CIS 210 F17 Project 1 part 2

Author: Jacob Garrison

Credits: N/A

Starting at 1 and going to a given number
n, the program will display "fizz" if the
number is divisble by 3, "buzz" if the number
is divisble by 5, and display the number itself
if neither are true.
'''

def fb(n):
    '''(int) -> None

    Starting at 1 and going to a given number
    n, the program will display "fizz" if the
    number is divisble by 3, "buzz" if the number
    is divisble by 5, and display the number itself
    if neither are true.

    >>> fb(10)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    Game Over
    '''

    count = 1
    while count <= n:
        if count % 15 == 0:
            print('fizzbuzz')
        elif count % 3 == 0:
            print('fizz')
        elif count % 5 == 0:
            print('buzz')
        else:
            print(count)
        count += 1

    print('Game Over')
    return None
