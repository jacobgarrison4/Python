from test_harness import testEQ  # Used in CIS 210 for test cases 

## Constants used by this program

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

if __name__ == "__main__":
    run_tests()
