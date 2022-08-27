from collections import defaultdict
import heapq

l = [
  { 'id': 1, 'name': 'Jassie', 'department': 'AB' },
  { 'id': 2, 'name': 'Kim', 'department': 'AB' },
  { 'id': 3, 'name': 'Jordan', 'department': 'AB' },
  { 'id': 4, 'name': 'Natalia', 'department': 'MN' },
  { 'id': 5, 'name': 'John', 'department': 'AB' },
  { 'id': 6, 'name': 'Jake', 'department': 'CA' },
  { 'id': 7, 'name': 'Austin', 'department': 'GH' },
  { 'id': 8, 'name': 'Peter', 'department': 'KM' },
  { 'id': 9, 'name': 'Irina', 'department': 'GH' },
]

dept_to_person = defaultdict(list)
cts = defaultdict(int)
for x in l:
    dp = x['department']
    dept_to_person[dp].append(x['name'])
    cts[dp] += 1
h = []
for k, v in cts.items():
    heapq.heappush(h, (-v, k))

ret = []
while len(h) >= 2:
    a, b = heapq.heappop(h)
    c, d = heapq.heappop(h)
    ret.append([dept_to_person[b].pop(), dept_to_person[d].pop()])
    if a != -1:
        heapq.heappush(h, (a+1, b))
    if c != -1:
        heapq.heappush(h, (c+1, d))
print(ret)


