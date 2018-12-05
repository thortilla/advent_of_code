#########################################
#                                       #
#              PART ONE                 #
#                                       #
#########################################

def parse_input():
    f = open('05_input')
    line = f.readline()
    f.close()
    return line

def react(u):
    i = 0
    units_list = list(u)
    j = len(units_list)
    while i < j:
        if i+1 < j:
            if units_list[i] != units_list[i+1] and units_list[i].lower() == units_list[
                i+1].lower():
                del units_list[i+1]
                del units_list[i]
                i = i - 1
                j = len(units_list)
            else:
                i = i+1
        else:
            i = i+1
    return "".join(units_list)

units = parse_input()
print len(react(units))

#########################################
#                                       #
#              PART TWO                 #
#                                       #
#########################################

def get_units_distinct(u):
    units_list = [c.lower() for c in u]
    units_distinct = []
    for c in units_list:
        if c not in units_distinct:
            units_distinct.append(c)
    return units_distinct

def make_units_dict(u, d):
    units_dict = {}
    for c in d:
        units_dict[c] = "".join([char for char in u if char != c.lower()])
        units_dict[c] = "".join([char for char in units_dict[c] if char !=
                                 c.upper()])
        units_dict[c] = react(units_dict[c])
    return units_dict

def get_shortest(u):
    min = len(units)
    min_k = None
    for k,v in u_dict.iteritems():
        if len(v) < min:
            min = len(v)
            min_k = k
    return {'min':min,'min_k':min_k}


distinct = get_units_distinct(units)
u_dict = make_units_dict(units, distinct)
print get_shortest(u_dict)