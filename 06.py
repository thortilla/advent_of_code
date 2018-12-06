import sys
#########################################
#                                       #
#              PART ONE                 #
#                                       #
#########################################

def parse_input():
    coords = []
    with open('06_input') as f:
        for line in f.readlines():
            coords.append((int(line.split(',')[0]),
                           int(line.split(',')[1].rstrip())))
    return coords

def get_corners(c):
    minX = c[0][0]
    maxX = 0
    minY = c[0][1]
    maxY = 0
    for xy in c:
        if minX > xy[0]:
            minX = xy[0]
        if minY > xy[1]:
            minY = xy[1]
        if maxX < xy[0]:
            maxX = xy[0]
        if maxY < xy[1]:
            maxY = xy[1]
    return {'maxX':maxX,'maxY':maxY,'minX':minX,'minY':minY}

def make_table(coor,corn):
    table = [['X' for x in range(0,corn.get('maxX'))]
             for x in range(0, corn.get('maxY'))]

    for row in range(0,len(table)):
        for cell in range(0,len(table[row])):
            table[row][cell] = get_minimum(coor, row, cell)
    i = 0

    return table

def make_exclusions(table):
    ex = []
    for row in table:
        if row[0] not in ex:
            ex.append(row[0])
        if row[len(row)-1] not in ex:
            ex.append(row[len(row)-1])
    for cell in table[0]:
        if cell not in ex:
            ex.append(cell)
    for cell in table[len(table)-1]:
        if cell not in ex:
            ex.append(cell)
    return ex


def get_maximum_area(table, ex):
    areas = {}
    for row in range(0,len(table)):
        for cell in range(0,len(table[row])):
            if table[row][cell] not in ex:
                if table[row][cell] in areas:
                    areas[table[row][cell]] = areas[table[row][cell]] + 1
                else:
                    areas[table[row][cell]] = 1
    max = 0
    for k,v in areas.iteritems():
        if max < v:
            max = v
    return max


def get_minimum(coor, row, cell):
    min = sys.maxint
    i = 0
    j = 0
    for c in coor:
        x = c[1]-1
        y = c[0]-1
        d = abs(row - x) + abs(cell - y)
        if min == d:
            j = 'X'
        if min > d:
            min = d
            j = i
        i = i+1
    return j

coordinates = parse_input()
corners = get_corners(coordinates)
t = make_table(coordinates,corners)
ex = make_exclusions(t)
max = get_maximum_area(t,ex)
print max

#########################################
#                                       #
#              PART TWO                 #
#                                       #
#########################################

MAX_DISTANCE = 10000
def calc_region(coor, table):
    size = 0
    for row in range(0,len(table)):
        for cell in range(0,len(table[row])):
            sum = 0
            for c in coor:
                x = c[1]-1
                y = c[0]-1
                d = abs(row - x) + abs(cell - y)
                sum = sum + d
            if sum < MAX_DISTANCE:
                size = size + 1
    return size

print calc_region(coordinates,t)