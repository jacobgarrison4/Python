from math import *

def list_reverse(a_list):
    n = 1
    new = ""
    for n in range(len(a_list)+1):
        new += a_list[-n]
        n += 1
    print(new)
