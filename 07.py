import string
import copy
#########################################
#                                       #
#              PART ONE                 #
#                                       #
#########################################

def parse_input():
    return_steps = {}
    with open('07_input') as f:
        for line in f.readlines():
            words = line.split(' ')
            pre_step = words[1]
            post_step = words[7]
            if pre_step not in return_steps:
                return_steps[pre_step] = []
            if post_step not in return_steps:
                return_steps[post_step] = [pre_step]
            else:
                return_steps[post_step].append(pre_step)
    return return_steps

def make_sequence(s):
    final_list = []
    while len(s) > 0:
        step_to_append = find_step_to_append(s)
        final_list.append(step_to_append)
        remove_step_from_prerequisites(step_to_append, s)
    return final_list

def find_step_to_append(s):
    sorted_keys = sorted(s.keys())
    for k in sorted_keys:
        if len(s.get(k)) == 0:
            del s[k]
            return k

def remove_step_from_prerequisites(step_to_append, s):
    for k,v in s.iteritems():
        if step_to_append in v:
            del v[v.index(step_to_append)]


steps = parse_input()
seq = make_sequence(copy.deepcopy(steps))
print "".join(seq)

#########################################
#                                       #
#              PART TWO                 #
#                                       #
#########################################

#TOPOLOGICAL SORT TODO