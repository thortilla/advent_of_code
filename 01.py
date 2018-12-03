#########################################
#                                       #
#              PART ONE                 #
#                                       #
#########################################

freq = 0
with open('01_input') as f:
    for line in f.readlines():
        freq = freq + int(line)
print freq

#########################################
#                                       #
#              PART TWO                 #
#                                       #
#########################################

found = False
freq = 0
past_freq = []
i = 0
while not found:
    f = open('01_input')
    for line in f.readlines():
        freq = freq + int(line)
        if freq in past_freq:
            found = True
            break
        past_freq.append(freq)
    i = i+1
    f.close()
print freq
f.close()