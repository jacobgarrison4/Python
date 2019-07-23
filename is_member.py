"""
is_member.py: Recursive implementation of is_member() on a set
              represented by a sorted list of integers
Authors: Jacob Garrison 

CIS 210 assignment 4, part 1, Fall 2015. 
"""
import argparse      # Used in main program to get PIN code from command line
from test_harness import testEQ  # Used in CIS 210 for test cases 

## Constants used by this program

def gen_set(set_file):
    """
    Takes a file containing lines of numbers and converts
    it into a sorted list.
    """
    the_set = []
    for line in set_file:
        the_set.append(int(line))
    the_set = sorted(the_set)
    return the_set

def is_member(set, number):
    """
    Takes a sorted list of integers and serarches the list
    for a given number. Returns True if the number is in
    the list and False otherwise.
    """
    num = set[len(set)//2]
    if number == num:
        return True
    elif len(set) == 1:
        return False
    elif number < num:
        return is_member(set[:len(set)//2], number)
    elif number > num:
        return is_member(set[len(set)//2:], number)
    else:
        return False

def run_tests():
    """
    This function runs a set of tests to help you debug your
    program as you develop it.
    """
    l = [-27, -12, -5, -1, 0, 2, 3, 6, 8, 10, 13, 25, 46, 99]
    print("**** TESTING --- Check membership of locally-defined set")
    print(l)
    testEQ("-99 is False", is_member(l, -99), False)
    testEQ("115 is False", is_member(l, 115), False)
    testEQ("-27 is True", is_member(l, -27), True)
    testEQ("99 is True", is_member(l, 99), True)
    testEQ("0 is True", is_member(l, 0), True)
    testEQ("-4 is False", is_member(l, -4), False)
    testEQ("14 is False", is_member(l, 14), False)
    print("*** End of provided test cases.  Add some of your own? ****")

def main():
    """
    Interaction if run from the command line.
    """
    parser = argparse.ArgumentParser(description="Recursive implementation of is_member()")
    parser.add_argument("set", type=argparse.FileType('r'),
                        help="A text file containing set elements, one per line.")
    parser.add_argument("number", type=int, help="number to check for membership")
    args = parser.parse_args()  # gets arguments from command line
    set_file = args.set
    number = args.number
    the_set = gen_set(set_file)
    if is_member(the_set, number):
        print(number, "is an element of the set")
    else:
        print(number, "is not an element of the set")

if __name__ == "__main__":
    run_tests()
    # main()

