s = set()
with open('in') as f:
    for l in f.read().splitlines():
        q = l.split(',')
        q = [int(x) for x in q]
        s.add(tuple(q))
q = list(s)

D = []
for i in range(3):
    l = [0, 0, 0]
    for dx in [-1, 1]:
        l[i] = dx
        D.append(tuple(l))

ret = 0
for (a, b, c) in q:
    for da, db, dc in D:
        t = (a + da, b + db, c + dc)
        if t not in s:
            ret += 1
print(ret)