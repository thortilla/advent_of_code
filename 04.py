#########################################
#                                       #
#              PART ONE                 #
#                                       #
#########################################

from datetime import datetime
from datetime import timedelta

class WorkDay:
    guard_id = None
    asleep = None
    awake = None

    def __init__(self, gid = None):
        self.guard_id = gid
        self.asleep = []
        self.awake = []

    def set_guard(self, gid):
        self.guard_id = gid

    def get_guard(self):
        return self.guard_id

    def add_asleep(self,d):
        self.asleep.append(d)

    def add_awake(self,d):
        self.awake.append(d)

    def get_night(self):
        midnight = ["O" for i in range(0,59)]
        for i in range(0,len(self.asleep)):
            for j in range(
                    int(self.asleep[i][int(self.asleep[i].find(":"))+1:]),
                    int(self.awake[i][int(self.awake[i].find(":"))+1:])):
                midnight[j] = "X"
        return ''.join(midnight)

def parse_input():
    timetable = {}
    with open('04_input') as f:
        for line in f.readlines():
            time = line[line.find(" ")+1:line.find("]")]
            date = line[line.find("[")+1:line.find(" ")]
            guard_id = line[line.find("#"):line.find("#") + line[line.find(
                "#"):].find(" ")]
            if "23:" in time:
                d = datetime.strptime(date, "%Y-%m-%d")
                d = d + timedelta(days=1)
                y = d.year
                d = d.replace(year=1900)  # strftime can't handle < y1900
                new_date = datetime.strftime(d, "%Y-%m-%d")
                new_date = str(y) + new_date[new_date.find("-"):]
                if new_date in timetable:
                    timetable[new_date].set_guard(guard_id)
                else:
                    timetable[new_date] = WorkDay(guard_id)
            elif date not in timetable:
                timetable[date] = WorkDay()
                if guard_id != "":
                    timetable[date].set_guard(guard_id)
                elif "falls" in line:
                    timetable[date].add_asleep(time)
                else:
                    timetable[date].add_awake(time)
            elif timetable[date].get_guard() is None and guard_id != "":
                timetable[date].set_guard(guard_id)
            else:
                if "falls" in line:
                    timetable[date].add_asleep(time)
                else:
                    timetable[date].add_awake(time)
    return timetable

def sum_for_guards():
    guards = {}
    for k,v in timetable.iteritems():
        if v.get_guard() not in guards:
            guards[v.get_guard()] = 0
        for hour in v.get_night():
            if hour == 'X':
                guards[v.get_guard()] = guards[v.get_guard()] + 1

    return guards

def get_max():
    max = 0
    max_guard = None
    for k,v in _sum.iteritems():
        if v > max:
            max = v
            max_guard = k
    return {'max':max,'max_guard':max_guard}

def get_most_asleep():
    minutes = [0 for i in range(0,59)]
    for k,v in timetable.iteritems():
        if v.get_guard() == _max.get('max_guard'):
            night = v.get_night()
            for i in range(0,59):
                if night[i] == 'X':
                    minutes[i] = minutes[i] + 1
    return minutes.index(max(minutes))

timetable = parse_input()
_sum = sum_for_guards()
_max = get_max()
most_asleep = get_most_asleep()
guard_num = _max.get('max_guard')[_max.get('max_guard').find("#")+1:]
print int(guard_num) * most_asleep

#########################################
#                                       #
#              PART TWO                 #
#                                       #
#########################################

def most_frequent_asleep_minute_of_guard():
    guard_minutes = {}
    for k,v in timetable.iteritems():
        if v.get_guard() not in guard_minutes:
            guard_minutes[v.get_guard()] = [0 for i in range(0,59)]
        night = v.get_night()
        for i in range(0,59):
            if night[i] == 'X':
                guard_minutes[v.get_guard()][i] = guard_minutes[
                                                        v.get_guard()][i] + 1
    max = 0
    max_minute = 0
    max_guard = None
    for guard, hours in guard_minutes.iteritems():
        minute = 0
        for hour in hours:
            if hour > max:
                max = hour
                max_minute = minute
                max_guard = guard
            minute = minute + 1
    print "{}->    {}*{}={}".format(max,max_minute,max_guard[1:],int(max_guard[
                                                         1:])*max_minute)

most_frequent_asleep_minute_of_guard()