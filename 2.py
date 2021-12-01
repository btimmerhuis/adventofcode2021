f = open('input.csv','r')
lines = f.readlines()
print(type(lines))

i = 0
inc = 0
while i < len(lines) - 3:
    a = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
    b = int(lines[i+3]) + int(lines[i+1]) + int(lines[i+2])
    if b > a:
        inc += 1
    i += 1

print(inc)

