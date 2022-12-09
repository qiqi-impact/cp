def hm_to_intm(s):
    a, b = s.split(':')
    a = int(a)
    b = int(b)
    return a * 60 + b

sorted_int = []
stage = 0
test_values = None
with open("in") as f:
    for hours in f.read().splitlines():
        if len(hours) == 0:
            stage += 1
            continue
        if stage == 0:
            sorted_int.append([hm_to_intm(x) for x in hours.split(' - ')])
        else:
            test_values = [hm_to_intm(x) for x in hours.split(' - ')]

intervals = []
sorted_int.sort()
cur_start = cur_end = sorted_int[0][0]
for x, y in sorted_int:
    if x > cur_end:
        intervals.append([cur_start, cur_end])
    cur_end = y
intervals.append([cur_start, cur_end])

found = False
for x, y in intervals:
    if x <= test_values[0] and test_values[1] <= y:
        found = True
        break
print(found)

'''
input looks like:

04:20 - 12:30
19:00 - 21:45
14:00 - 17:30
12:30 - 14:00

18:00 - 21:45
'''