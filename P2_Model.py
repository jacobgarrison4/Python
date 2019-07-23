#===============================================================================
# P2_Model.py
# Created by Anthony Hornof - 5-2-2016
# Revised by: Jacob Garrison
# Version 0.2
# Implementation for Spring 2016 CIS 211 Project 2
# Derived in part from Dave Kieras' design and implementation of EECS 381 Proj 4
#===============================================================================

class Model:
    '''
    The Model object keeps track of everything in the simulated world.
    Only one Model should be created in each run of the simulation.
    '''

    #===========================================================================
    def __init__(self):
        self.__world_size = None
        self.__humans = []

    #===========================================================================
    def __str__(self):
        return "The world is of size " + str(self.__size)

    #===========================================================================
    def get_world_size(self):
        return self.__world_size

    #===========================================================================
    def get_valid_location(self, arg1, arg2=None):
        '''
        Determine if a location is in the world.  If yes, returns a tuple of ints.
        This function is made polymorphic by using "switch on type".

        Parameters: arg1 and arg2 are ints, OR
                    arg1 and arg2 are strings, OR
                    arg1 is a tuple of two ints, and no arg2 is provided, OR
                    arg1 is a tuple of two strings, and no arg2 is provided
        Returns:    a tuple of ints if the location is in the world
                    None otherwise.

        Examples of use if the world is of size 30:
        self.get_valid_location(10, 20) -> (10, 20)
        self.get_valid_location('10', '20') -> (10, 20)
        self.get_valid_location((10, 20)) -> (10, 20)
        self.get_valid_location('a', '20') -> None
        self.get_valid_location(1.0, 20) -> None
        '''

        # Switch on type.  If arguments are...

        # (int, int)
        if type(arg1) == type(arg2) == int:
            x = arg1
            y = arg2

        # (str, str)
        elif type(arg1) == type(arg2) == str and arg1.isdigit() and arg2.isdigit():
            x = int(arg1)
            y = int(arg2)

        # (tuple of two ints)
        elif (arg2 == None and type(arg1) == tuple and len(arg1)==2 and
                type(arg1[0])==int and type(arg1[1])==int):
            x = arg1[0]
            y = arg1[1]

        # (tuple of two strings which can convert into digits)
        elif (arg2 == None and type(arg1) == tuple and len(arg1)==2 and
                type(arg1[0])==str and type(arg1[1])==str and
                arg1[0].isdigit() and arg1[1].isdigit()):
            x = int(arg1[0])
            y = int(arg1[1])

        # Arguments not handled, or invalid location.
        else:
            # print("Error: Model.get_valid_location() arguments not handled.")
            return None # The provided arguments are not handled.

        # If the location is in the world, return True.
        if (x >= 0 and y >= 0 and
                x <= self.__world_size and y <= self.__world_size):
            return (x, y)
        else:
            return None

    #===========================================================================
    def create_sim_object(self, arg_list):
        '''
        Create a simulation object based on the contents of the arg_list.
        Parameters: arg_list, list of strings entered after "create" command
        Returns:    True for if the line cannot be parsed, False if it can be.

        The only assumption that can be made about the arg_list when entering
        this function is that there was at least one string in the command line
        after "create".
        '''

        MIN_WORLD_SIZE = 10
        MAX_WORLD_SIZE = 30

        # Continue here checking for all of the different objects that "create"
        # could be called to build.  For each, after checking for the string
        # that appeared after "create", make sure that any additional arguments
        # on the line are all permissable given the project specification.


        #=======================================================================
        # World
        if arg_list[0]=='world':
            # Else return error.

            # Verify that there is one additional argument and it is an integer.
            if len(arg_list) == 2 and arg_list[1].isdigit():
                size = int(arg_list[1])
            else:
                return True

            # If a world has aleady been created
            if (self.__world_size):
                # Then return an error.
                print("Error: World already exists.")
                return False  # Error was reported, so no need to return an error flag.

            # Verify size is in range.
            if size < MIN_WORLD_SIZE or size > MAX_WORLD_SIZE:
                print ("Error: World size is out of range.")
            else:
                # Else create the world.
                print('Creating world of size ', size, '.', sep='')
                self.__world_size = size

        #=======================================================================
        # Make sure a world exists.
        # If there is no world yet, then there can be no waypoints.
        elif not self.get_world_size():
            print ("Error: A world must be created before any other objects.")
            return False  # Error was reported, so no need to return an error flag.

        #=======================================================================
        # Human
        elif arg_list[0]=='human':

            # If the number of arguments is wrong
            if len(arg_list) != 4:
                return True # Return an error code.
            # If the name is not alphanumeric
            elif not arg_list[1].isalnum():
                print("Error: Name must be alphanumeric.")
                return False
            elif self.get_human(arg_list[1]):
                print("Error: Human already exists with that name.")
                return False
            # If <x> <y> is not a valid location
            elif not self.get_valid_location(arg_list[2], arg_list[3]):
                print("Error: Invalid location.")
                return False
            # Else this appears to be a valid input, and so
            #   create a human at the location.
            else:
                new_location = self.get_valid_location(arg_list[2], arg_list[3])
                print("Creating human ", arg_list[1].capitalize(), " at location ", new_location,".", sep='')
                self.__humans.append(Human(arg_list[1].lower(), new_location))

            # self.__humans.append

        #=======================================================================
        # Invalid create command.
        else:
            # print(invalid_create_command_string)
            return True # Return Error flag

    #===========================================================================
    def get_human(self, name):
        '''
        # Takes a name string.  Looks for a human with that name.  If one exists,
        #   returns that human.  If one does not, returns None.

        Parameters: name, a string
        Returns:    Either a pointer to a human object, or False
        '''
        for i in self.__humans:
            if i.get_name() == name:
                return i
        else:
            return None

    #===========================================================================
    def describe_all(self):
        '''
        Each of the simulation objects describes itself in text.

        ( ) -> None
        '''
        print("The contents of the world are as follows:")
        if self.get_world_size():
            print ("The world is of size ", self.get_world_size(), ".", sep='')
        for i in self.__humans:
            print (i)


class SimObject:

    def __init__(self, _name, _location):
        self._name = _name
        self._location = _location

    def __str__(self):
        return self._name + " at location " + str(self._location)

    def get_name(self):
        return self._name

    def get_location(self):
        return self._location


class Waypoint:

    def __init__(self, name, location):
        self.__name = name
        self.__location = location

    def __str__(self):
        return "Waypoint " + self.__name + " at location " + str(self.__location)

#===============================================================================
class Human:
    '''
    A human in the simulation.
    '''

    def __init__(self, name, location):
        # Private member variables.
        self.__name = name.lower()
        self.__location = location  # a tuple of integers

    def __str__(self):
        return "Human " + self.__name.capitalize() + " at location " + str(self.__location)

    def get_name(self):
        return self.__name

    def move_to(self, location):
        '''
        valid location in the world as a tuple of ints -> ( )
        '''
        self.__location = location
        print( "Human " + self.__name.capitalize() + " moved to location " + str(self.__location) + ".")


class Robot:

    def __inti__(self, name, location):
        self.__name = name.lower()
        self.__location = location

    def __str__(self):
        return "Robot " + self.__name.capitalize() + " at location " + str(self.__location)

class Fire:

    def __init__(self, location):
        self.__location = location

    def __str__(self):
        return "Fire at location " + str(self.__location)