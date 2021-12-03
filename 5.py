f = open('3.csv', 'r')
lines = f.readlines()
b = len(lines[0])
i = 0
code = str()
while i < b - 1:
    x = 0
    y = 0
    for l in lines:
        if int(l[i]) == 1:
            x += 1
        else:
            y += 1
    if x > y:
        code = code + '1'
    else:
        code = code + '0'
    i += 1
print('gamma', int(code,2))
i = 0
epsilon = str()
while i < len(code):
    if int(code[i]) == 1:
        epsilon = epsilon + '0'
    else:
        epsilon = epsilon + '1'
    i += 1
print('epsilon', int(epsilon,2))
print('antwoord: ', int(code,2)*int(epsilon,2))
