f = open('input.csv','r')
lines = f.readlines()
print(type(lines))

i = 0
inc = 0
while i < len(lines) - 1:
    if int(lines[i+1]) > int(lines[i]):
        print('{} is groter dan {}'.format(int(lines[i+1]),int(lines[i])))
        inc += 1
    i += 1

print(inc)

