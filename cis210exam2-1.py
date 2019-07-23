#Jacob Garrison
#CIS 210 Exam 2

#2
def calcCost(pounds):
    '''(int) -> float

    calcCost takes in one parameter, pounds of oranges,
    and returns the cost including shipping.

    >>>calcCost(15)
    10.70
    >>>calcCost(101)
    38.32
    >>>calcCost(0)
    No Order Placed
    '''
    if pounds == 0:
        print('No Order Placed')
    elif pounds < 100:
        cost = round(((.32 * pounds) + 7.50),2)
        return cost
    elif pounds >= 100:
        cost = round(((.32 * pounds) + 6.00),2)
        return cost
        
#1
length = len(play_list)
