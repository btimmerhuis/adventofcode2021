f = open('3.csv', 'r')
data = f.readlines()
items = []
for i in data:
    items.append(i.strip())

def remove_items(lines,mask,index):
    keep = []
    for l in lines:
        print('checking',l,'mask',mask)
        if int(l[index]) != mask:
            print('removing',l)
        else:
            print('keeping: ', l)
            keep.append(l)
    return keep


def oxy(lines,index):
    print(lines,index)
    if len(lines) == 1:
        o = int(lines[0],2)
        print(o)
        return o
    else:
        x = 0
        y = 0
        for l in lines:
            if int(l[index]) == 1:
                x += 1
            else:
                y += 1
        print(x,y)
        if x >= y:
            print('mask 1')
            lines = remove_items(lines,1,index=index)
        else:
            print('mask 0')
            lines = remove_items(lines,0,index=index)
    return oxy(lines,index+1)

def co2(lines,index):
    print(lines,index)
    if len(lines) == 1:
        c = int(lines[0],2)
        print(c)
        return c
    else:
        x = 0
        y = 0
        for l in lines:
            if int(l[index]) == 1:
                x += 1
            else:
                y += 1
        print(x,y)
        if x < y:
            lines = remove_items(lines,1,index=index)
        else:
            lines = remove_items(lines,0,index=index)
    return co2(lines,index+1)

o = oxy(items,0)
c = co2(items,0)
print(o*c)
