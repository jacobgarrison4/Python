def ctemp_to_ftemp(ctemp):
        ''' (int)-> float

        Return a temperature in fahrenheit converted from celsius (ctemp).

        >>> convert_to_fahrenheit(100)
        212.0
        >>>convert_to_fahrenheit(30)
        86.0
        >>> convert_to_fahrenheit(21.1)
        69.98
        '''
        return (ctemp * (9/5)) + 32
