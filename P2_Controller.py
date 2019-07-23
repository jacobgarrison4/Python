#===============================================================================
# P2_Controller.py
# Created by Anthony Hornof - 5-2-2016
# Revised by: Jacob Garrison
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
# Create a Model object and assign it to a global variable called "the_model"
# Create a local instance of a Controller and have it start the run() function.

    global the_model
    the_model = P2_Model.Model()

    c = Controller()
    c.run()

#===============================================================================
class Controller:
#===============================================================================
    '''
    The controller object handles user keyboard input and provides textual to
    the console.  It follows the model view-controller software design pattern.
    '''

    #===========================================================================
    def __init__(self):

        # Local "private" member variables

        # File with list of commands to be executed (initialized to default).
        self.__input_filename = "commands.txt"

        # File object currently being read from.  This is also used to indicate
        #   whether the system is currently getting lines from the user or a file.
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

            # If there are no arguments to process, just loop.
            if len(line_list) == 0:
                continue    # Loop to the top of the while loop.

            #=======================================
            # In this loop, make sure that:
            # 1. The first word of the command line is viable, such as that the
            #    command truly exists, or the human truly exists.
            # 2. The number of arguments that come after the first word are the
            #    correct number that would be needed given the first word, or
            #    provide at least the minimum number of arguments that could be
            #    needed based on the first word in the line.

            # If the command is...

            #=======================================
            # '<human>' command - tell a human object to do something
            if the_model.get_human(line_list[0]):
                self.do_human_command(line_list)

            #=======================================
            # 'create'
            elif line_list[0]=='create' and len(line_list) > 2:     # Change 2 to 3 for P3.
                # Send the arguments to the Model's create object function.
                if the_model.create_sim_object(line_list[1:]):
                    # If an error was returned.
                    print("Unrecognized command:", line)

            #=======================================
            # 'status'                      (Make sure there are NO args.)
            elif line_list[0]=='status' and len(line_list) == 1:
                # Get and print a text string from the Model of each
                #   simulation object describing itself.
                the_model.describe_all( )

            #=======================================
            # 'open'
            elif line_list[0]=='open' and len(line_list) == 2:
                # Overwrite the input-filename member-variable.
                self.__input_filename = line_list[1]
                # Attempt to open the file.
                self.open_input_file()

            #=======================================
            # 'quit'
            # Prompt again and quit.
            elif line_list[0] == 'quit' and line_list[1:]==[]:
                print("Are you sure you want to quit? (Y/N) ", end='')
                line = self.get_next_input_line()
                if line.lower() == 'y':
                    break

            #=======================================
            # 'q'
            # A hidden convenient fast way to quit.  Remove before distributing or testing.
            elif line_list[0] == 'q' and line_list[1:]==[]:
                break

            #=======================================
            # Unrecognized command
            else:
                print("Unrecognized command:", line)


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

        # If there is currently a command-line input file open, then use it.
        if self.__input_file_object:

            # Get the line.
            getline = self.__input_file_object.readline().strip()

            # If it is not empty, show it and return it.
            if getline:
                print ("FILE>", getline)
                return getline
            else:
                # Else close the file and set self.__input_file_object to None.
                self.__input_file_object.close()
                self.__input_file_object = None
                print ("Closing file.")
                return ''

        # Else, input is currently being provided by the user's keystrokes.
        else:

            # Issue the prompt
            print("> ", end='')

            # Get and return the command line from the user.
            return input()


    #===========================================================================
    def open_initial_input_file (self):
        '''
        Attempt to open a file for an initial set of commands.
        ( ) -> None
        If a filename was entered as a command line argument, overwrite the
          controller's member variable with that new filename.
        '''

        # If a filename was entered as an argument, overwrite the default initial
        #   input filename with this new filename.
        if len(sys.argv) > 1 and sys.argv[1]:
            self.__input_filename = sys.argv[1]
        # Attempt to open the input file.
        self.open_input_file( )


    #===========================================================================
    def open_input_file (self):
        '''
        ( ) -> None
        Attempts to open the filename in the input file member variable to
          execute a set of commands.
        '''

       # If an initial file exists and is readable.
        if (os.path.isfile( self.__input_filename ) and
                os.access( self.__input_filename, os.R_OK)):

            # Then open that file.
            print ("Reading file:", self.__input_filename)
            self.__input_file_object = open ( self.__input_filename )

        else:
            # Else error.
            print ("Error: Could not open and read input file:", self.__input_filename)


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

        # Keep a pointer to the human
        human_obj = the_model.get_human(args[0])

        # Make sure the rest of the command is in a correct form.

        #=======================================================================
        # 'move' command
        if len(args) > 1 and args[1] == 'move':

           #=======================================================================
            # move <x> <y>
            if len(args) == 4:
                # Create a location tuple from the final two args
                location = (args[2], args[3])
            #=======================================================================
            # Invalid move command.
            else:
                print("Error: Invalid move command.")
                return

            # If it is a valid location, move the human to it.
            if location and the_model.get_valid_location(location):
                # Then move the human to that location.
                human_obj.move_to(the_model.get_valid_location(location))
            else:
                print("Error: Invalid location.")

        else:
            print("Error: Invalid human command.")


#===============================================================================
main ()
#===============================================================================

