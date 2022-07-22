from collections import defaultdict

def distinct_paths(n, e, v):
    cc = list(range(n))
    counts = [defaultdict(int) for _ in range(n)]
    for i in range(n):
        counts[i][v[i]] += 1

    def root(i):
        if cc[i] != i:
            cc[i] = root(cc[i])
        return cc[i]

    def join(i, j):
        ri = root(i)
        rj = root(j)
        if ri != rj:
            if (v[ri], ri) < (v[rj], rj):
                cc[rj] = ri
                for k in counts[rj]:
                    counts[ri][k] += counts[rj][k]
            else:
                cc[ri] = rj
                for k in counts[ri]:
                    counts[rj][k] += counts[ri][k]
        return ri != rj

    g = defaultdict(set)
    for x, y in e:
        g[x-1].add(y-1)
        g[y-1].add(x-1)

    vis = [False] * n
    vv = sorted(zip(v, list(range(n))))
    ret = 0
    for x, i in vv:
        for j in g[i]:
            if vis[j]:
                if join(i, j):
                    ri = root(i)
                    ret += counts[ri][x] - 1
        vis[i] = True
    return ret

print(distinct_paths(5, [[1,2], [1,3], [3, 4], [3, 5]], [2, 3, 1, 2, 3]))
