def bd(length, midspan):
    x = length / 2
    b = midspan
    y = ( x / 10 ) + b
    return y

def td(length, midspan):
    x = - ( length / 2 )
    b = midspan
    y = ( x / 10 ) + b
    return y

def loglist(logs):
    count = 1
    for log in logs:
        print("Log ", count, ":")
        length = log[0]
        midspan = log[1]
        print("Butt Diameter is: ", bd(length, midspan))
        print("Tip Diameter is: ", td(length, midspan))
        count += 1
