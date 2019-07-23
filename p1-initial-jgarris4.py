# ===============================================================================
# P1_starter.py
# Created by Anthony Hornof - 3-28-2016
# Modified by Jacob Garrison - 3-29-2016
# Version 0.4
# Implementation for Spring 2016 CIS 211 Project 1
# ===============================================================================

'''
    Processes the input file line by line.
    First line must be REQUIRED_FIRST_LINE.
    Subsequent lines must be one of the following:
        sim_object_type="World" size="<int>,<int>"
        sim_object_type="Robot" name="<name>"
            robot_type="Searcher | Supplier | Carrier | Extinguisher | Nozzle"
            location="<int>,<int>"
        sim_object_type="Person" name="<name>" location="<int>,<int>"
    Input files straying from this formatting cause a failure.

    File lines are put into SIM_OBJECT_LIST, which is a list of line_lists, with
    one line_list per line.  Each line_list has one element for each name=value
    pair in the input line, only the value from each name=value pair, and the
    "<int>,<int>" size and location strings converted to (<int>, <int>) tuples.

    SIM_OBJECT_LIST is then "pretty printed" to the console.
'''

import sys  # for argv
import os  # for os.path.isfile() and os.access()


# ===============================================================================
# STARTER CODE
# ===============================================================================
def main():
    # ===============================================================================
    '''
    Opens and processes the input file. Provides user feedback on how it went.
    Returns: False for success, True for failure
    '''

    # Initialize global constants.
    initialize_global_constants()

    # Provide initial user feedback.
    print(MSG_PROGRAM_STARTUP)

    # Create the list of simulation objects that will be created from the file.
    simulation_object_list = []

    # Get the input filename and create an input file object.
    input_file_object = get_inputfile_object()

    # If input_file_object was set to 1, an error occurred.
    if input_file_object == 1:
        # Terminate with an error.
        return True

    # Initialize line_counter, the line number that is currently being read in.
    line_counter = 1

    # Set an error code that will be used when program terminates.
    error_code = False  # True = an error occurred.  False = no error.

    # Process the first line of the file.
    # If there is an error reading the first line...
    if read_first_line(input_file_object, line_counter):
        # Error: The first line was incorrect.
        error_code = True

    else:
        # Otherwise the first line was correct.  Proceed with the rest.
        line_counter += 1  # Increment the line counter.

        # If there is an error reading subsequent lines...
        if read_subsequent_lines(input_file_object, line_counter, simulation_object_list):
            # Error: A subsequent line was incorrect.
            error_code = True

        else:
            # Else the file was successfully read in.
            # A good simulation_object_list was created.
            # "Pretty print" the list of simulation objects.
            pprint_simulation_object_list(simulation_object_list)

            # "Normal" end of reading in a file occurs here

    # Close file
    #input_file_object.close()

    # Exit program
    return error_code


# ===============================================================================
# STARTER CODE
# ===============================================================================
def initialize_global_constants():
    # ===============================================================================
    '''
    () -> False
    '''

    # Global constants

    global DEFAULT_INPUT_FILENAME
    DEFAULT_INPUT_FILENAME = "world.txt"

    # Output messages to be used for all user feedback.

    global MSG_PROGRAM_STARTUP
    global MSG_OPENING_FILE
    global MSG_ERROR_OPENNING_FILE

    MSG_PROGRAM_STARTUP = "\nRunning Rescue Robot Simulation Program"
    MSG_OPENING_FILE = "Opening input file:"
    MSG_ERROR_OPENNING_FILE = "Cannot find and read input file:"

    # Used for parsing the input file.

    global REQUIRED_FIRST_LINE
    REQUIRED_FIRST_LINE = "Initial World State of the Rescue Robot Simulation:"

    # Token identifiers

    global SIM_OBJECT_TYPE_IDENTIFIER
    global WORLD
    global PERSON
    global ROBOT
    global SIM_OBJECT_TYPE_WORLD
    global SIM_OBJECT_TYPE_PERSON
    global SIM_OBJECT_TYPE_ROBOT
    global OBJECT_TYPES

    SIM_OBJECT_TYPE_IDENTIFIER = "sim_object_type="
    WORLD = "World"
    PERSON = "Person"
    ROBOT = "Robot"
    SIM_OBJECT_TYPE_WORLD = SIM_OBJECT_TYPE_IDENTIFIER + WORLD
    SIM_OBJECT_TYPE_PERSON = SIM_OBJECT_TYPE_IDENTIFIER + PERSON
    SIM_OBJECT_TYPE_ROBOT = SIM_OBJECT_TYPE_IDENTIFIER + ROBOT
    OBJECT_TYPES = (SIM_OBJECT_TYPE_WORLD,
                    SIM_OBJECT_TYPE_PERSON,
                    SIM_OBJECT_TYPE_ROBOT)

    global ROBOT_TYPE_IDENTIFIER
    global SEARCHER
    global SUPPLIER
    global CARRIER
    global EXTINGUISHER
    global NOZZLE
    global ROBOT_TYPE_SEARCHER
    global ROBOT_TYPE_SUPPLIER
    global ROBOT_TYPE_CARRIER
    global ROBOT_TYPE_EXTINGUISHER
    global ROBOT_TYPE_NOZZLE
    global ROBOT_TYPES

    ROBOT_TYPE_IDENTIFIER = "robot_type="
    SEARCHER = "Searcher"
    SUPPLIER = "Supplier"
    CARRIER = "Carrier"
    EXTINGUISHER = "Extinguisher"
    NOZZLE = "Nozzle"
    ROBOT_TYPE_SEARCHER = ROBOT_TYPE_IDENTIFIER + SEARCHER
    ROBOT_TYPE_SUPPLIER = ROBOT_TYPE_IDENTIFIER + SUPPLIER
    ROBOT_TYPE_CARRIER = ROBOT_TYPE_IDENTIFIER + CARRIER
    ROBOT_TYPE_EXTINGUISHER = ROBOT_TYPE_IDENTIFIER + EXTINGUISHER
    ROBOT_TYPE_NOZZLE = ROBOT_TYPE_IDENTIFIER + NOZZLE
    ROBOT_TYPES = (SEARCHER, SUPPLIER, CARRIER, EXTINGUISHER, NOZZLE)

    global SIZE_IDENTIFIER
    global NAME_IDENTIFIER
    global LOCATION_IDENTIFIER

    SIZE_IDENTIFIER = "size="
    NAME_IDENTIFIER = "name="
    LOCATION_IDENTIFIER = "location="

    # The line signatures show the elements that must match up against lines in the input file.
    #  LINE_SIGNATURE_TUPLE = (
    #   (â€˜sim_object_type=Worldâ€™, â€˜size=â€™),
    #   (â€˜sim_object_type=Personâ€™,  â€˜name=â€™, â€˜location=â€™),
    #   (â€˜sim_object_type=Robotâ€™, â€˜name=â€™, â€˜robot_type=â€™,  â€˜location=â€™))

    global LINE_SIGNATURE_TUPLE
    LINE_SIGNATURE_TUPLE = (
        # World line-signature
        (SIM_OBJECT_TYPE_WORLD, SIZE_IDENTIFIER),
        # Person line-signature
        (SIM_OBJECT_TYPE_PERSON, NAME_IDENTIFIER, LOCATION_IDENTIFIER),
        # Robot line-signature
        (SIM_OBJECT_TYPE_ROBOT, NAME_IDENTIFIER, ROBOT_TYPE_IDENTIFIER, LOCATION_IDENTIFIER))

    # Number of items that should be included in the line signature for each object type
    # (These should really be extracted from above.)
    global NUM_WORLD_TOKENS
    global NUM_ROBOT_TOKENS
    global NUM_PERSON_TOKENS

    NUM_WORLD_TOKENS = 2  # Line_identifier, Size
    NUM_PERSON_TOKENS = 3  # Line_identifier, Name and Location
    NUM_ROBOT_TOKENS = 4  # Line_identifier, Name, Type, and Location

    return False


# ===============================================================================
def get_inputfile_object():
    # ===============================================================================
    '''
    Check the command line for an argument.  If one was there, use it as the
    filename.  Otherwise, use DEFAULT_INPUT_FILENAME.  Open the file.

    If file is successfully openned:
        print MSG_OPENING_FILE
        Return: a file object for that file

    If the file cannot be openned:
        print MSG_ERROR_OPENNING_FILE
        Return: True
    '''

    open("Sample_Input_File_1.txt", 'r')
    print(MSG_OPENING_FILE)

# ===============================================================================
def read_first_line(file_object, line_number):
    # ===============================================================================
    ''' Read in the first line of the file and confirm it matches REQUIRED_FIRST_LINE.
        If it does not match, call declare_error() and return True

        Parameters: file_object, the input file object.
                    line_number, the current line number being read in.
        Returns:    False for success, True for failure
    '''

    with open("Sample_Input_File_1.txt", 'r') as file:
        firstline = file.readline()
        if firstline != REQUIRED_FIRST_LINE:
            declare_error(line_number,firstline)

        else:
            return False


# ===============================================================================
def read_subsequent_lines(file_object, line_number, simulation_obj_list):
    # ===============================================================================
    ''' Read and parse the next line of the file, confirm it matches one of the
        line signatures, such as ('sim_object_type=World', 'size=')

        Parameters: file_object, the input file object.
                    line_number, the current line number being read in.
                    simulation_obj_list, the list of converted lines.
        Returns: False for success, True for failure

        Convert the line in the file to a list of strings, with one string per
            name=value pair (such as "name=Joe").  Make sure that each line matches
            up with one of the line "signatures" in the constant definitions.
            Modify this line_list to only include the value portion of the pair,
            calling extract_line_using_signature (...) to get the each line list.
            Append each modified line_list to the simulation_obj_list( ).

        If success: Return False.
        If failure: Call declare_error (...) and Return True.
    '''

    # < STUDENTS ADD CODE HERE >


# ===============================================================================
def extract_line_using_signature(line_signature, line_list):
    # ===============================================================================
    '''
    Takes a line_signature such as
        ('sim_object_type=Person', 'name=', 'location=')
    and a line_list such as
        ['sim_object_type=Person', 'name=Junling', 'location=12,45']
    Returns a new list of just the values such as
        ['Person', 'Junling', (12, 45)]
    Note that the strings of integer pairs have no spaces in them.
    '''

    # < STUDENTS ADD CODE HERE >


# ===============================================================================
def convert_ici_string_to_tuple(ici_string):
    # ===============================================================================
    '''
    Takes a string in the form of "<int1>,<int2>" and returns a tuple (<int1>, <int2>)

    Parameter:
            ici_string: a string with an int, comma, and int, like "12,34"
    Return: If success, a tuple of the two ints
            If error, an empty tuple.

    An error occurs if the input is not in the form of "<int1>,<int2>",
      such as if there is a space character in the string.
    '''

    # < STUDENTS ADD CODE HERE >


# ===============================================================================
# STARTER CODE
# ===============================================================================
def declare_error(line_number, line_text):
    # ===============================================================================
    '''
    Identifies the first line in the input file that violates the file specification.
    Prints out an error message with the line_number and line_text that get passed in.
    No return value.
    '''
    LINE_START = "Input file error in line " + str(line_number) + ":"
    print(LINE_START, ' "', line_text, '"', sep="")


# ===============================================================================
# STARTER CODE
# ===============================================================================
def pprint_simulation_object_list(sim_obj_list):
    # ===============================================================================
    '''
    "Pretty print" the simulation_object_list.
     No input parameters or return values.
    '''
    print()
    print("Simulation Object List:")
    for line in sim_obj_list:
        if line[0] == WORLD:
            print("World of size", line[1])
        elif line[0] == ROBOT:
            print(line[2], ' robot "', line[1], '" appears at ', line[3], sep="")
        elif line[0] == PERSON:
            print('Person "', line[1], '" appears at ', line[2], sep="")
        else:
            print("Unexpected line in simulation object list:", line)

    return


# ===============================================================================
main()
# ===============================================================================
