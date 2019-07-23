#===============================================================================
# P2_Controller.py
# Created by Anthony Hornof - 4-8-2016
# Modified by Jacob Garrison - 4-27-16
# Version 0.2
# Implementation for Spring 2016 CIS 211 Project 2
# Derived in part from Dave Kieras' design and implementation of EECS 381 Proj 4
#===============================================================================

import sys  # for argv
import os   # for os.path.isfile() and os.access()

import P2_Model

#===============================================================================
def main ():
#===============================================================================
# Create a global Model object and assign it to a global variable called "the_model"
# Create a local instance of a Controller and have it start the run() function.

    global the_model

     # < STUDENTS ADD CODE HERE >

#===============================================================================
class Controller:
#===============================================================================
    '''
    The controller object handles user keyboard input and provides textual to
    the console.  It follows the model view-controller software design pattern.
    '''

    #===========================================================================
    def __init__(self, input_filename, input_file_object):

        self.__input_filename = default command filename
        self.__input_file_object = None

    #===========================================================================
    def run(self):
    #===========================================================================
        '''
        () -> None.
        Process the command lines for the human-robot simulation.
        '''

        print("Starting Human-Robot Interaction Simulation.")

        # Attempt to open an input file for an initial set of commands
        self.open_initial_input_file()

        #=======================================================================
        # Command loop
        while True:

            # Get the next line of input whether it is from the user or a file.
            line = self.get_next_input_line()
            line_list = line.lower().split()

            # < STUDENTS ADD CODE HERE >


    #===========================================================================
    # Manage the command line input file
    #===========================================================================

    def get_next_input_line(self):
        '''
        ( ) -> string
        • Displays the prompt.
        • Returns the next line to be processed, or '' if there is no line.
        • Gets the next line of text either from an input file or from the user,
          depending on the current setting of current_input_mode.
        • When reading from an input file, and either a blank line or an end of file
          is encountered, close the input file and set the file object var to None.
        '''

        # < STUDENTS ADD CODE HERE >


    #===========================================================================
    def open_initial_input_file (self):
        '''
        Attempt to open a file for an initial set of commands.
        ( ) -> None
        If a filename was entered as a command line argument, overwrite the
          controller's member variable with that new filename.
        '''

        # < STUDENTS ADD CODE HERE >


    #===========================================================================
    def open_input_file (self):
        '''
        ( ) -> None
        Attempts to open the filename in the input file member variable to
          execute a set of commands.
        '''

        # < STUDENTS ADD CODE HERE >


    #===========================================================================
    # Execute commands
    #===========================================================================

    def do_human_command(self, args):
        '''
        Parameters: args, a list of arguments that is already confirmed to be
                          nonempty with the first argument a human in the model.
        Returns:    None (All errors are reported within, so no need to return
                          an error flag.)

        Processes the remainder of the arguments to insure that they at least
        represent valid locations on the map.  If they are valid,
        call the appropriate function calls in the model to build them.
        '''

        # < STUDENTS ADD CODE HERE >


#===============================================================================
main ()
#===============================================================================

