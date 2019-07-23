# Problem 0
ttl_shirts = 10
ttl_yellow = 4
ttl_green = 6
ycost = 25
gcost = 20
ttl_cost = ( ttl_yellow * ycost ) + (ttl_green * gcost )
print(ttl_cost)

# Problem 1
# 5
# 125
# 123
# 123

# Problem 2
# 1
# 10
# 20
# 20

# Problem 3
temp = 0
ftemp = ( temp * ( 9 / 5 ) ) + 32
ctemp = ( ftemp - 32 ) * ( 5 / 9 )
print(temp, ftemp, ctemp)

# Problem 4
# The song is referring to the total amount of minutes in a year
minutes_per_hour = 60
minutes_per_day = minutes_per_hour * 24
minutes_per_year = minutes_per_day * 365
print(minutes_per_year)

# Problem 5
day1_amount = .01
day28_amount = day1_amount * ( 2 ** 28 )
print(day28_amount)
# I would take one cent doubled each day because even in the months with the fewest days (28) I would get more than $2 million

# (xc) Challenge
day1_amount = .01
day29_amount = day1_amount * ( 2 ** 29 )
day30_amount = day1_amount * ( 2 ** 30 )
day31_amount = day1_amount * ( 2 ** 31 )
print(day29_amount, day30_amount, day31_amount)
# If it were a month with 30 or 31 days I would take the one cent doubled every day; otherwise I would take the immediate $10 million

