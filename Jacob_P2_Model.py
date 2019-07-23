#===============================================================================
# P2_Model.py
# Created by Anthony Hornof - 4-8-2016
# Modified by Jacob Garrison - 4-27-16
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
    def __init__(self, world_size, humans):

        self.__world_size = None
        self.__humans = []

    #===========================================================================
    def __str__(self):

        return self.describe_all()

    #===========================================================================
    def get_world_size(self):
        return self.__world_size

    #===========================================================================
    def get_valid_location(self, arg1, arg2=None):
        '''
        Determine if a location is in the world.  If yes, returns a tuple of ints.
        This function is made polymorphic by using "switch on type".

        Parameters: #arg1 and arg2 are ints, OR
                    arg1 and arg2 are strings, OR
                    #arg1 is a tuple of two ints, and no arg2 is provided, OR
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

        if arg1 >= 10 and arg2 <= 30:
            return (arg1, arg2)

        if int(arg1) >= 10 and int(arg2) <= 30:
            return (int(arg1), int(arg2))

        if arg1[0] >= 10 and arg1[1] <= 30:
            return (arg1[0], arg1[1])

        if int(arg1[0]) >= 10 and int(arg1[1]) <= 30:
            return (int(arg1[0]), int(arg1[1]))

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

        cmd = arg_list.split()
        if cmd[1] = "world":
            self.__world_size = (int(cmd[2]))
            print("Creating world of size %s" % self.get_world_size())

        if cmd[1] = "human":
            self.__humans.append(cmd[1])
            self.name = cmd[2]
            self.get_valid_location(cmd[3], cmd[4])
            return "Creating human", self.__name, "at location", self.__location()

    #===========================================================================
    def get_human(self, name):
        '''
        # Takes a name string.  Looks for a human with that name.  If one exists,
        #   returns that human.  If one does not, returns None.

        Parameters: name, a string
        Returns:    Either a pointer to a human object, or None
        '''

        if name in self.__humans:
            return name

        return None

    #===========================================================================
    def describe_all(self):
        '''
        Each of the simulation objects describes itself in text.
        ( ) -> None
        '''

        return 'The contents of the world are as follows:'
        return 'The world is of size %s' %self.get_world_size()
        for i in self.__humans:
            return self.__humans[i], "is at location:", self.__location


#===============================================================================
class Human:
    '''
    A human in the simulation.
    '''

    def __init__(self, name, location):
        self.__name = name.lower
        self.__location = location

    def __str__(self):
        # < STUDENTS ADD CODE HERE >

    def get_name(self):
        return self.__name

    def move_to(self, location):
        self.__location = location


