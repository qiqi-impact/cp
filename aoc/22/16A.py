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

NZ = len(nzidx)

@cache
def dfs(lv, bm, t):
    if t == 0:
        return 0

    name, cur, adj, idx = anodes[lv]
    
    pressure = 0
    for i in range(NZ):
        if bm & (1 << i):
            pressure += anodes[nzidx[i]][1]
    
    ret = pressure * t
    for other in adj:
        ret = max(ret, pressure + dfs(other, bm, t-1))

    if lv in nzd and not ((1 << nzd[lv]) & bm):
        ret = max(ret, pressure + dfs(lv, bm ^ (1 << nzd[lv]), t-1))
    
    return ret

print(dfs(nodes['AA'][3], 0, 30))

