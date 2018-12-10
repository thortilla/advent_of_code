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

from collections import defaultdict, deque

edges = defaultdict(list)
d_in = defaultdict(int)
queue = []
time = 0
current_nodes = []
workers = 5

def parse_input_for_second():
    for line in open('07_input'):
        words = line.split()
        x = words[1]
        y = words[7]
        edges[x].append(y)
        d_in[y] += 1
    #sort..
    for k in edges:
        edges[k] = sorted(edges[k])

def start_work():
    global queue
    while len(current_nodes) < workers and queue:
        x = min(queue)
        queue = [y for y in queue if y != x]
        current_nodes.append((time + 61 + ord(x) - ord('A'), x))

parse_input_for_second()

for k in edges:
    if d_in[k] == 0:
        queue.append(k)
start_work()

while current_nodes or queue:
    time, x = min(current_nodes)
    current_nodes = [y for y in current_nodes if y != (time, x)]
    for y in edges[x]:
        d_in[y] -= 1
        if d_in[y] == 0:
            queue.append(y)
    start_work()

print time