#===============================================================================
# P4_Model.py
# Created by Anthony Hornof - 4-28-2016
# Modified by Jacob Garrison - 5-24-16
# Version 0.1
# Implementation for Spring 2016 CIS 211 Project 4
# Derived in part from Dave Kieras' design and implementation of EECS 381 Proj 4
#===============================================================================

# import P4_View
import P4_Utility

# global constants. (You must define them as global if you intend to re-assign.)
WORLD_STRING = 'world'
WAYPOINT_STRING = 'waypoint'
HUMAN_STRING = 'human'
ROBOT_STRING = 'robot'
FIRE_STRING = 'fire'


class Model:
    '''
    The Model object keeps track of everything in the simulated world.
    Only one Model should be created in each run of the simulation.
    '''

    #===========================================================================
    # Initializer and other Special Functions
    #===========================================================================
    def __init__(self):
        self.__world_size = None
        self.__sim_objects = []  # all SimObjects but the Waypoints
        self.__waypoints = []
        self.__humans = []
        self.__robots = []
        self.__fires = []
        self.__time = 0

        global the_model
        the_model = self

        # A pointer to the view in the MVC design. If there were
        # more than one view, this would be a list of all views.
        self.__view = None

    #===========================================================================
    def describe_all(self):
        '''
        Each of the simulation objects describes itself in text.
        ( ) -> None
        '''
        print("The contents of the world are as follows:")
        if self.__world_size:
            print ("The world is of size ", self.__world_size, ".", sep='')
        for i in self.__waypoints:
            print (i)
        for i in self.__humans:
            print (i)
        for i in self.__robots:
            print (i)
        for i in self.__fires:
            print (i)

    #===========================================================================
    # Model-View-Controller coordination methods
    #===========================================================================
    def attach_view(self, v):
        self.__view = v

    #===========================================================================
    def notify_location(self, name, location):
        '''
        The model has been notified, probably by a SimObject, that a SimObject's
        location may have changed.  Broadcast this information to the View.
        '''
        self.__view.update_object(name, location)


    #===========================================================================
    # Creation Methods
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
        if arg_list[0] == WORLD_STRING:
            # Else return error.

            # Verify that there is one additional argument and it is an integer.
            if len(arg_list) == 2 and arg_list[1].isdigit():
                size = int(arg_list[1])
            else:
                raise BadMsgError

            # If a world has aleady been created
            if (self.__world_size):
                # Then return an error.
                print("Error: World already exists.")
                raise BadMsgError  # Error was reported, so no need to return an error flag.

            # Verify size is in range.
            if size < MIN_WORLD_SIZE or size > MAX_WORLD_SIZE:
                print ("Error: World size is out of range.")
            else:
                # Else create world, and notify all views that the world is
                #   being created."

                print('Creating world of size ', size, '.', sep='')
                # Set the World size member variable.
                self.__world_size = size

                # Update the View object(s) world size.
                self.__view.create(size)

        #=======================================================================
        # Make sure a world exists.
        # If there is no world yet, then there can be no waypoints.
        elif not self.__world_size:
            print ("Error: A world must be created before any other objects.")
            raise BadMsgError  # Error was reported, so no need to return an error flag.

        #=======================================================================
        # Waypoint, human, robot, or fire
        # Verify the number and type of arguments, and location.
        elif arg_list[0] in (WAYPOINT_STRING, HUMAN_STRING, ROBOT_STRING, FIRE_STRING):

            # Verify that there are two arguments, two integers each of which
            #   is <= world_size.

            # If there are NOT three more arguments, the second and third being ints...
            if not (len(arg_list) == 4 and arg_list[2].isdigit() and
                        arg_list[3].isdigit()):
                # Then return error flag.
                raise BadMsgError

            # Convert the two integer arguments into a tuple of integers.
            location = (int(arg_list[2]), int(arg_list[3]))

            # Get the name for all subsequent operations. Store all names as lowercase.
            name = arg_list[1].lower()

            #===================================================================
            # Waypoint

            if arg_list[0] == WAYPOINT_STRING:

                # If the waypoint name is not a single letter
                if not name.isalpha() or not len(name) == 1:
                    print('Error: Waypoint names must be single letters.')
                    raise BadMsgError  # Error was reported, so no need to return an error flag.

                # If a waypoint already exists with that name or at that location, report error.
                for w in self.__waypoints:
                    if name == w.get_name() or location == w.get_location():
                        print ("Error: Waypoint", w.get_name().upper(), "already exists at location", w.get_location())
                        raise BadMsgError  # Error was reported.

                # Okay, there is NO Waypoint at that location.
                else:

                    # If the location is invalid, return an error.
                    if not the_model.get_valid_location(location):
                        print("Error: Invalid location.")
                        raise BadMsgError

                    else:
                        # Create the waypoint! All of the parameters checked out.
                        print("Creating waypoint", name.upper(), "at location", location)
                        # Create the new waypoint, and add it to the list of Waypoints
                        self.__waypoints.append( Waypoint(name, location) )
                        # Update the view with the new waypoint
                        self.__view.add_landmark(name, location)


            #=======================================================================
            # Human, Robot, or Fire
            elif arg_list[0] in (HUMAN_STRING, ROBOT_STRING, FIRE_STRING):

                # If the name is not alphanumeric
                if not arg_list[1].isalnum():
                    print("Error: Name must be alphanumeric.")
                    raise BadMsgError

                # If an object already exists with that name.
                if self.get_object(arg_list[1]):

                    # Get a nice pritable class name using __class__.__name__
                    print("Error:", self.get_object(arg_list[1]).get_class_name(), "already exists with that name.")
                    raise BadMsgError

                # If the location is invalid, return an error.
                if not the_model.get_valid_location(location):
                    print("Error: Invalid location.")
                    raise BadMsgError

                # If we got this far, it seems to be a valid input,  so
                #   create an object at the location.
                location = self.get_valid_location(arg_list[2], arg_list[3])
                name = arg_list[1]
                print("Creating ", arg_list[0]," ", name.capitalize(), " at location ", location,".", sep='')

                # For each type of sim object, create the object and add it to its list.
                if arg_list[0] == HUMAN_STRING:
                    # Create the Human
                    new_sim_obj = Human(name, location)
                    # Add the human to the list of Humans.
                    self.__humans.append(new_sim_obj)
                elif arg_list[0] == ROBOT_STRING:
                    # Create the Robot
                    new_sim_obj = Robot(name, location)
                    # Add the robot to the list of SimObjects.
                    self.__robots.append(new_sim_obj)
                else: # arg_list[0] == FIRE_STRING:
                    # Create the Robot
                    new_sim_obj = Fire(name, location)
                    # Add the robot to the list of SimObjects.
                    self.__fires.append(new_sim_obj)

                # Also add the new sim object to the list of all SimObjects as well.
                self.__sim_objects.append(new_sim_obj)

                # Update the view with the new Sim Object
                self.__view.update_object(name, location)

            else:
                raise BadMsgError # Error

        else:
            raise BadMsgError # Error

    #===========================================================================
    # More Complex Accessor Methods
    #===========================================================================
    def get_time(self):
        '''
        returns time
        '''
        return self.__time

    #===========================================================================
    def get_waypoint_location(self, name):
        '''
        # Takes a name string.  Looks for a waypoint with that name.  If one exists,
        #   returns its location.  If one does not, returns None.

        Parameters: name, a string
        Returns:    Either a location of a Waypoint, or False
        '''

        for i in self.__waypoints:
            if i.get_name() == name:
                return i.get_location()
        else:
            return None

    #===========================================================================
    def fire_at_location(self, location):
        '''
        returns a fire at given location if one exists. If location
            does not exist, returns None.
        '''
        if location.get_valid_location() == True:
            return "Fire at location ", location
        else:
            return None

    #===========================================================================
    def delete_fire(self, name):
        '''
        Delete from the View  and the Model a fire with the given name
        '''
        for i in self.__fires:
            if i.get_name() == name:
                self.__fires.remove(self, name)
        else:
            return None

    #===========================================================================
    def get_human(self, name):
        '''
        Takes a name string.  Looks for a human with that name.  If one exists,
            returns that human.  If one does not, returns None.
        '''
        for i in self.__humans:
            if i.get_name() == name:
                return i
        else:
            return None

    #===========================================================================
    def get_robot(self, name):
        '''
        Takes a name string.  Looks for a robot with that name.  If one exists,
            returns that robot.  If one does not, returns None.
        '''
        for i in self.__robots:
            if i.get_name() == name:
                return i
        else:
            return False

    #===========================================================================
    def get_fire(self, name):
        '''
        Takes a name string. Looks for a fire with that name. If one exists,
            returns that fire. If one does not, returns None.
        '''
        for i in self.__fires:
            if i.get_name() == name:
                return i
        else:
            return None

    #===========================================================================
    def get_object(self, name):
        '''
        Takes a name string.  Looks for any sim object with that name.  If one
            exists, returns that sim object.  If one does not, returns None.
        '''
        for i in self.__sim_objects:
            if i.get_name() == name:
                return i
        else:
            return False

    #===========================================================================
    def get_valid_location(self, arg1, arg2=None):
        # Possibly change to get_location() and have it always return a tuple of
        # two ints
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
            return None # The provided arguments are not handled.

        # If the location is in the world, return True.
        if (x >= 0 and y >= 0 and
                x <= self.__world_size and y <= self.__world_size):
            return (x, y)
        else:
            return None

#===============================================================================
    def update(self):
        '''
        Updates all sim objects and increments time by 1 minute
        '''
        self.__time = self.__time + 1

        return None

#===============================================================================
# OTHER CLASSES
#===============================================================================

#===============================================================================
class SimObject:

    def __init__(self, name, location):
        # Private member variables.
        self._name = name.lower()
        self._location = location  # a tuple of integers

    def __str__(self):
        return self._name.capitalize() + " at location " + str(self._location)

    def get_name(self):
        return self._name

    def get_class_name(self):
        ''' Returns 'Human', 'Robot', or 'Fire' as appropriate.'''
        return self.__class__.__name__

    def get_location(self):
        return self._location

#===============================================================================
class Waypoint (SimObject):
    '''
    A Waypoint in the simulation.
    '''

    def __str__(self):
        return "Waypoint " + super().__str__()

#===============================================================================
class Fire (SimObject):
    '''
    A Waypoint in the simulation.
    '''

    def __init__(self, name, location):
        # Private member variables.
        self._size = 500 # heat release rate, in kW
        super().__init__(name, location)

    def __str__(self):
        return "Fire " + super().__str__()

#===============================================================================
class Traveler (SimObject):

        # Update the view

    def move_to(self, location):

        print( self.get_class_name(), " " , self.get_name().capitalize(), " moved to location ",
               location, '.', sep='')

        # Change the object's location
        self._location = location  # a tuple of integers

        # Notify the Model that an object of this name now has this location.
        the_model.notify_location(self._name, location)


#===============================================================================
class Human (Traveler):
    '''
    A human in the simulation.
    '''

    def __str__(self):
        return "Human " + super().__str__()

#===============================================================================
class Robot (Traveler):
    '''
    A robot in the simulation.
    '''
    def __init__(self, name, location):
        # Private member variables.
        self._carrying_human = None
        self._water_capacity = 100 # gallons
        self._water_level = 0
        super().__init__(name, location)

    def __str__(self):
        return "Robot " + super().__str__()



