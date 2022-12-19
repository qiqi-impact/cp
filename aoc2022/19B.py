from functools import cache

bp = []
i = 0
with open('in') as f:
    for l in f.read().splitlines():
        # if i%6 == 0:
        bp.append([])
        # if 1 <= i%6 <= 4:
        l = l.split(' ')
        for w in l:
            try:
                x = int(w)
                bp[-1].append(x)
            except:
                pass
        # i += 1
# print(bp)

MX = 0
@cache
def dfs(a, b, c, d, ra, rb, rc, rd, t, bpi):
    global MX
    if t == 0:
        MX = max(MX, d)
        return d
    if d + t * rd + (t - 1) * t // 2 <= MX:
        return 0
    ret = dfs(a + ra, b + rb, c + rc, d + rd, ra, rb, rc, rd, t-1, bpi)
    if a >= bp[bpi][4] and c >= bp[bpi][5]:
        ret = max(ret, dfs(a - bp[bpi][4] + ra, b + rb, c - bp[bpi][5] + rc, d + rd, ra, rb, rc, rd + 1, t-1, bpi))
    if t > 1:
        if a >= bp[bpi][2] and b >= bp[bpi][3]:
            ret = max(ret, dfs(a - bp[bpi][2] + ra, b - bp[bpi][3] + rb, c + rc, d + rd, ra, rb, rc + 1, rd, t-1, bpi))
        if t > 2:
            if a >= bp[bpi][1]:
                ret = max(ret, dfs(a - bp[bpi][1] + ra, b + rb, c + rc, d + rd, ra, rb + 1, rc, rd, t-1, bpi))
        if a >= bp[bpi][0]:
            ret = max(ret, dfs(a - bp[bpi][0] + ra, b + rb, c + rc, d + rd, ra + 1, rb, rc, rd, t-1, bpi))
    
    return ret

for bpi in [0]:
    dfs(0, 0, 0, 0, 1, 0, 0, 0, 32, bpi)
    print(bpi, MX)
    break

#states
# ore, clay, obs, geode, #robots for each, time