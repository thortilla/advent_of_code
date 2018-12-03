#########################################
#                                       #
#              PART ONE                 #
#                                       #
#########################################

occured_twice = []
occured_thrice = []
with open('02_input') as f:
    for line in f.readlines():
        list_line = list(line)
        had_thrice = False
        had_twice = False
        while len(list_line)>0:
            letter = list_line[0]
            if list_line.count(letter) == 2 and not had_twice:
                had_twice = True
                occured_twice.append(letter)
            elif list_line.count(letter) == 3 and not had_thrice:
                had_thrice = True
                occured_thrice.append(letter)
            for l in list_line:
                if l == letter:
                    list_line.remove(l)
print len(occured_thrice)*len(occured_twice)

#########################################
#                                       #
#              PART TWO                 #
#                                       #
#########################################

with open('02_input') as f:
    file = [l.rstrip() for l in f.readlines()]
found = False
items = []
pos = []
for item1 in file:
    for item2 in file:
        pos = [i for i in xrange(len(item1)) if item1[i] != item2[i]]
        if len(pos) == 1:
            items = [item1, item2]
            found = True
            break
    if found:
        break
print items[0][:pos[0]] + items[0][pos[0]+1:]