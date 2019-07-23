name = 'Darth Vader'

target_string = 'D a r t h  V a d e r '

ctr = 0
result = ''
while ctr < len(name):
    ch = name[ctr]
    result += ch + ' '
    ctr += 1
result = ''
for ctr in name:
    result += ctr + ' '


print(result)
