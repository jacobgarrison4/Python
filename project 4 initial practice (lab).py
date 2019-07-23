#try code here, (Model)

import utils

def check_inputs(x_list):
    for each in x_list:
        if int(each) == 1:
            raise utils.ContainsOne
        elif int(each) == 2:
            raise utils.ContainsTwo('Error: 2 is present')
        else:
            print(each, sep='\t')
    print()

#utilities, (exceptions)

class ContainsOne(Exception):
    pass

class ContainsTwo(Exception):
    pass

#practice code, (controller)

import try_code_here

while True:
    x = input("enter number seperated by space: ")
    if x == 'quit':
        break
    x = x.split()
    print(x[1])
    try:
        try_code_here.check_inputs(x)
    except utils.ContainsTwo as err:
        print(err)
    except utils.ContainsOne:
        print('1 is in input')
        
