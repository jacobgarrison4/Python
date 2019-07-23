#Problem 0
def word1():
    word = input('Enter a word ')
    if len(word) >= 5:
        return True
    else:
        return False
        
def word2():
    word = input('Enter a word ')
    if str.isalnum(word):
        return False
    else:
        return True

def word3():
    word = input('Enter a word ')
    if 'E' in word or 'e' in word:
        return False
    else:
        return True

#Problem 1
def grade_calculator():
    '''() -> None

    Prompt user to input a list of grades
    Adjust grades to correct weight
    Prints total grade as percent 

    For example,
    grade_calculator()
    Enter project 1 grade: 25
    Enter project 2 grade: 38
    Enter project 3 grade: 28
    Enter project 4 grade: 35
    Enter midterm 1 grade: 39
    83
    
    '''
    proj_so_far = 14    #4 projects, 3.5 weighted pts. each
    tests_so_far = 20   #1 midterm 20 pts. weighted
    ttl_points_possible = \
                        proj_so_far + tests_so_far
 
    p1adjust = 1.17 # 30 ttl pts, multiply by 1.17 to get to 35
    p2adjust = .875 # 40 ttl pts, multiply by .875 to get to 40
    p3adjust = 1.17 
    p4adjust = .875 
    last_adjust = 10 # now divide by 10
    m1adjust = .4  # 50 ttl pts, multiply by .4 to get to 20

    # initialize weighted totals
    proj_grade = 0
    exam_grade = 0

    p1 = float(input('Enter project 1 grade: '))
    proj_grade += p1 * p1adjust 

    p2 = float(input('Enter project 2 grade: '))
    proj_grade += p2 * p2adjust 

    p3 = float(input('Enter project 3 grade: '))
    proj_grade += p3 / p3adjust

    p4 = float(input('Enter project 4 grade: '))
    proj_grade += p4 / p4adjust

    proj_grade /= last_adjust

    m1 = float(input('Enter midterm 1 grade: '))
    exam_grade = m1 * m1adjust

    my_ttl = proj_grade + exam_grade
    my_score = my_ttl / ttl_points_possible * 100
    my_score = round(my_score)
    if my_score >= 90:
        print(my_score,'A')
    elif my_score >= 80:
        print(my_score,'B')
    elif my_score >= 70:
        print(my_score,'C')
    elif my_score >= 60:
        print(my_score,'D')
    else:
        print(my_score,'F')    
    return #None

#Problem 2
def safe_lead(lead):
    step1 = lead - 3
    ball = input('Does the leading team have the ball?(Yes or No) ')
    if ball == 'Yes':
        return (step1 + .5) ** 2
    else:
        return (step1 - .5) ** 2
    seconds_left = input('How many seconds are left? ')
    if step2 > seconds_left:
        return True
    else:
        return False
