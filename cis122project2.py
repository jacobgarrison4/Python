# Problem 0
def kilo_to_miles(num):
        ''' (int)-> float

        Return an integer representing miles that has been converted from kilometers.

        >>> kilo_to_miles(5)
        3.125
        >>> kilo_to_miles(10)
        6.25
        >>> kilo_to_miles(0)
        0.0
        '''
        return num / 1.6

# Problem 1
def tip_calc(total_bill):
        ''' (int)-> float

        Return three different tip amounts for 15, 18, and 20 percent of a total bill.

        >>> tip_calc(10)
        (1.5, 1.79999999999998, 2.0)
        >>> tip_calc(28.60)
        (4.29, 5.148, 5.7200000000001)
        >>> tip_calc(50)
        (7.5, 9.0, 10.0)
        '''
        return total_bill * .15 , total_bill * .18 , total_bill * .20

# Problem 2
# (a)
def convert_to_celsius(temp):
        ''' (int)-> float

        Return a temperature in celcius converted from fahrenheit.

        >>> convert_to_celsius(212)
        100.0
        >>> convert_to_celsius(32)
        0.0
        >>> convert_to_celsius(70)
        21.11111111111
        '''
        return (temp - 32) * (5/9)

# (b)
def convert_to_fahrenheit(temp):
        ''' (int)-> float

        Return a temperature in fahrenheit converted from celsius.

        >>> convert_to_fahrenheit(100)
        212.0
        >>>convert_to_fahrenheit(0)
        32.0
        >>> convert_to_fahrenheit(21.1)
        69.98
        '''
        return (temp * (9/5)) + 32

# Problem 3
# (a)
def chirps_to_ftemp(chirps):
        ''' (int)-> int

        Reutrn a temperature in fahrenheit converted from the number of cricket
        chirps in 14 seconds then adding 40.

        >>> chirps_to_ftemp(30)
        70
        >>> chirps_to_ftemp(55)
        95
        >>> chirps_to_ftemp(0)
        40
        '''
        return chirps + 40

# (b)
def chirps_to_ctemp(chirps):
        ''' (int)-> float

        Return a temperature in celsius converted from the number of cricket
        chirps in 25 seconds, then divided by 3 and add 4.

        >>> chirps_to_ctemp(48)
        20.0
        >>> chirps_to_ctemp(93)
        35.0
        >>> chirps_to_ctemp(0)
        4.0
        '''
        return chirps / 3 + 4

# (c)
def chirps_to_ctemp2(chirps):
        ''' (int)-> float

        Input the number of chirps in 14 seconds and convert to fahrenheit by adding 40,
        then convert to celsius by subtracting 32 and multiplying by (5/9).

        >>> chirps_to_ctemp2(30)
        21.1111111111
        >>> chirps_to_ctemp2(55)
        35.0
        >>> chirps_to_ctemp2(0)
        4.444444444445
        '''
        return ((chirps + 40) - 32) * (5/9)

# Problem 4
def minimum_payment(balance):
        ''' (int)-> float

        Return a minimum payment from a certain balance; either 2.5 percent
        of the balance or 15 dollars, which ever is greater. If the balance
        is below 15 dollars, the minimum payment is the balance.

        >>> minimum_payment(1000)
        25.0
        >>> minimum_payment(800)
        20.0
        >>> minimum_payment(25)
        15
        >>> minimum_payment(10)
        10
        '''
        if balance < 15:
                return balance
        x = 15
        y = balance * .025
        return max (x,y)
