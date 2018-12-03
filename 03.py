#########################################
#                                       #
#              PART ONE                 #
#                                       #
#########################################

fabric = [['#' for i in range(0,1000)] for j in range(0,1000)]

def parse_claims(claims):
    c = {}
    for claim in claims:
        c[claim.split(' ')[0]] = {
            'h_offset': int(claim.split(' ')[2].split(',')[0]),
            'v_offset': int(claim.split(' ')[2].split(',')[1].split(':')[0]),
            'width': int(claim.split(' ')[3].split('x')[0]),
            'height': int(claim.split(' ')[3].split('x')[1])
        }
    return c

def draw_on_fabric(claims, fabric):
    for k, claim in claims.iteritems():
        x = claim.get('h_offset')
        y = claim.get('v_offset')
        for i in range(y, y+claim.get('height')):
            for j in range(x, x+claim.get('width')):
                if fabric[i][j] == '#':
                    fabric[i][j] = k
                else:
                    fabric[i][j] = 'X'
    return fabric

def count_overlaps(fabric):
    count = 0
    for i in fabric:
        for j in i:
            if j == 'X':
                count = count+1
    return count

with open('03_input') as f:
    claims = [line.rstrip() for line in f]

claims = parse_claims(claims)
fabric = draw_on_fabric(claims, fabric)
count = count_overlaps(fabric)

print count

#########################################
#                                       #
#              PART TWO                 #
#                                       #
#########################################

def get_intact(claims, fabric):
    for k, claim in claims.iteritems():
        intact = True
        x = claim.get('h_offset')
        y = claim.get('v_offset')
        for i in range(y, y+claim.get('height')):
            for j in range(x, x+claim.get('width')):
                if fabric[i][j] == 'X':
                    intact = False
        if intact:
            return k

intact = get_intact(claims, fabric)
print intact