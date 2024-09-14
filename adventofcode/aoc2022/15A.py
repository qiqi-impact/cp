BIG = 2000000
yb = set()
ls = []
with open('in') as f:
    for l in f.read().splitlines():
        nums = []
        cur = 0
        neg = 1
        found = False
        for c in l:
            if '0' <= c <= '9':
                cur *= 10
                found = True
                cur += int(c)
            elif c == '-':
                neg = -1
            elif found:
                nums.append(cur * neg)
                found = False
                cur = 0
                neg = 1
        nums.append(cur * neg)
        ls.append(nums)
        if nums[3] == BIG:
            yb.add(nums[2])
yb = sorted(yb)
dist = [abs(x[2] - x[0]) + abs(x[3] - x[1]) for x in ls]

intv = []
for i, (a, b, c, d) in enumerate(ls):
    v = dist[i] - abs(BIG - b)
    if v < 0:
        continue
    intv.append((a - v, a + v))
    # print(ls[i], intv[-1])
intv.sort()
# print(intv)

full = []
s = intv[0][0]
e = intv[0][1]
for idx in range(1, len(intv)):
    x, y = intv[idx]
    if x > e:
        full.append((s, e))
        s = x
    e = max(e, y)
full.append((s, e))

ret = 0
for x, y in full:
    for z in yb:
        if x <= z <= y:
            ret -= 1
    ret += y - x + 1
print(ret)