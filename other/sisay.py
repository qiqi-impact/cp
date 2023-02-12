from functools import cache
from collections import deque

@cache
def f(x):
	if len(x) == 0:
		return ['']
	if len(x) == 1:
		return []
	ret = []
	for i in range(1, len(x)):
		pref = x[i] * int(x[:i])
		for y in f(x[i+1:]):
			ret.append(pref + y)
	return ret

INPUT = '121'
s = set([INPUT])
q = deque([INPUT])

while q:
    for v in f(q.popleft()):
        if v not in s:
            s.add(v)
            q.append(v)
print(list(s))