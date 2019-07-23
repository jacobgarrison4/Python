'''
Cricket Chirps to Temperature. Assignment 1.1, CIS 210
Author: Jacob Garrison

Translates the number of cricket chirps in a given amount of time to the
relative temperature in degrees fahrenheit and celsius.
'''
from ctemp_to_ftemp import ctemp_to_ftemp
def chirps_to_ftemp(c25):
        ''' (num)-> float

        Return a temperature in celsius converted from the number of cricket
        chirps in 25 seconds, then divided by 3 and add 4.

        >>> chirps_to_ctemp(30)
        57.2
        >>> chirps_to_ctemp(55)
        72.2
        >>> chirps_to_ctemp(100)
        99.2
        '''
        pass
        return None

from ctemp_to_ftemp import ctemp_to_ftemp
def chirps_to_ftemp(c25):
        ''' (num)-> float

        Return a temperature in celsius converted from the number of cricket
        chirps in 25 seconds, then divided by 3 and add 4.

        >>> chirps_to_ctemp(30)
        57.2
        >>> chirps_to_ctemp(55)
        72.2
        >>> chirps_to_ctemp(100)
        99.2
        '''
        ctemp = c25 / 3 + 4
        ftemp = ctemp_to_ftemp(ctemp)
        print('The estimated temperature based on ', c25, 'chirps in 25 seconds is ', ftemp, 'degrees fahrenheit.')
        return None
