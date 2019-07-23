#Jacob Garrison
#CIS 210 Winter
#February 1st, 2016

#Question 1
price = 19.99
total_number = 25
total_price = round((price * total_number),2)
print(total_price)
    
#Question 2
def ctemp_to_ftemp(ctemp):
    '''(number) -> float

    Converts any temperature in degrees
    celcius to degrees fahrenheit.

    >>>ctemp_to_ftemp(100)
    212.0
    '''
    ftemp = ctemp * 9/5 + 32
    print(ftemp)
