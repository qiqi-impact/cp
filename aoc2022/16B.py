from functools import cache

nodes = {}
anodes = []
nzidx = []
nzd = {}

with open('in') as f:
    for l in f.read().splitlines():
        name = l[6:8]
        cur = 0
        for c in l:
            if '0' <= c <= '9':
                cur = cur * 10 + int(c)
        q = l.find('valves ')
        if q == -1:
            idx = l.find('valve ')+len('valve ')
        else:
            idx = l.find('valves ')+len('valves ')
        adj = l[idx:].split(', ')
        nodes[name] = [name, cur, adj]
        anodes.append(nodes[name])
        nodes[name].append(len(anodes)-1)
        if cur > 0:
            nzidx.append(len(anodes)-1)

nzidx.sort()
for i, e in enumerate(nzidx):
    nzd[e] = i

for k in nodes:
    l = nodes[k]
    l[2] = [nodes[x][3] for x in l[2]]

# print(anodes)

# path = []

NZ = len(nzidx)

@cache
def dfs(lv, ev, bm, t):
    if t == 0:
        return 0

    name, cur, adj, idx = anodes[lv]
    ename, ecur, eadj, eidx = anodes[ev]
    
    pressure = 0
    for i in range(NZ):
        if bm & (1 << i):
            pressure += anodes[nzidx[i]][1]
    
    ret = pressure * t
    for other in adj:
        for eother in eadj:
            ret = max(ret, pressure + dfs(other, eother, bm, t-1))

    if lv in nzd and not ((1 << nzd[lv]) & bm):
        for eother in eadj:
            ret = max(ret, pressure + dfs(lv, eother, bm ^ (1 << nzd[lv]), t-1))

    if ev in nzd and not ((1 << nzd[ev]) & bm):
        for other in adj:
            ret = max(ret, pressure + dfs(other, ev, bm ^ (1 << nzd[ev]), t-1))

    if (lv in nzd and not ((1 << nzd[lv]) & bm)) and (ev in nzd and not ((1 << nzd[ev]) & bm)):
         ret = max(ret, pressure + dfs(lv, ev, bm ^ (1 << nzd[lv]) ^ (1 << nzd[ev]), t-1))
    
    return ret

print(dfs(nodes['AA'][3], nodes['AA'][3], 0, 26))

